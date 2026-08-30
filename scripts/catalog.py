#!/usr/bin/env python3
"""Validate Exempla's learner-centered catalog and generate Markdown."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REPOSITORY_RE = re.compile(r"^[^/\s]+/[^/\s]+$")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
SAFE_PATH_PATTERN = (
    r"^(?!/)(?!.*\/$)(?!\.{1,2}(?:/|$))(?!.*\/\.{1,2}(?:/|$))"
    r"(?![^/]*\.[eE][nN][vV](?:\.[^/]*)?(?:/|$))"
    r"(?!.*\/[^/]*\.[eE][nN][vV](?:\.[^/]*)?(?:/|$))"
    r"(?!.*//)(?!.*\\).+$"
)
SAFE_PATH_RE = re.compile(SAFE_PATH_PATTERN)
QUALITY_FIELDS = (
    "source_quality",
    "architecture",
    "naming_and_idiom",
    "tests",
    "documentation",
    "traceability",
    "maintainability",
    "educational_value",
)
DIMENSION_FIELDS = (
    "language_technique",
    "behavioral_reasoning",
    "design_span",
    "constraint_burden",
)
NOVICE_ACCESSIBILITY_FIELDS = (
    "floor",
    "central_concepts",
    "incidental_concepts",
    "reason",
)
SOURCE_KINDS = ("production", "educational-exemplar")
SOURCE_KIND_LABELS = {
    "production": "Production software",
    "educational-exemplar": "Educational exemplar",
}
LEVEL_CAPACITY = {1: 3, 2: 3, 3: 2, 4: 2, 5: 2}
REPOSITORY_FIELDS = (
    "slug",
    "path_slug",
    "repository",
    "url",
    "primary_language",
    "language_evidence",
    "description",
    "source_kind",
    "purpose_evidence",
    "why_study",
    "learn",
    "prerequisites",
    "concepts_developed",
    "coding_relevance",
    "learning_path",
    "learning_level",
    "quality",
    "inspection",
    "license",
    "github",
)
OPTIONAL_REPOSITORY_FIELDS = ("novice_accessibility",)
LEGACY_REPOSITORY_FIELDS = tuple(
    "real_world_evidence" if field == "purpose_evidence" else field
    for field in REPOSITORY_FIELDS
    if field != "source_kind"
)
CATALOG_SCHEMA_VERSION = 5
COMPLETE_CATALOG_SIZE = 20 * sum(LEVEL_CAPACITY.values())
LEVEL_LABELS = {
    1: "First real code",
    2: "Guided real-world patterns",
    3: "Intermediate production software",
    4: "Advanced",
    5: "Expert",
}


class CatalogError(Exception):
    """Raised when a catalog resource cannot be loaded safely."""


def is_dotenv_name(name: str) -> bool:
    """Return True for .env, *.env, .env.*, and *.env.* names."""
    lowered = name.lower()
    return lowered == ".env" or lowered.endswith(".env") or ".env." in lowered


def is_safe_relative_path(value: str) -> bool:
    """Accept canonical POSIX repository paths while excluding dotenv variants."""
    if not value or SAFE_PATH_RE.fullmatch(value) is None:
        return False
    path = PurePosixPath(value)
    return (
        not path.is_absolute()
        and str(path) == value
        and path.parts
        and all(part not in (".", "..") for part in path.parts)
        and not any(is_dotenv_name(part) for part in path.parts)
    )


def load_json(path: Path) -> dict[str, Any]:
    if any(is_dotenv_name(part) for part in path.parts):
        raise CatalogError(f"refusing to inspect dotenv-like path: {path}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise CatalogError(f"missing file: {path}") from error
    except json.JSONDecodeError as error:
        raise CatalogError(f"invalid JSON in {path}: {error.msg} at line {error.lineno}") from error
    if not isinstance(value, dict):
        raise CatalogError(f"top level must be an object: {path}")
    return value


def calculate_learning_level(
    language: int, behavior: int, design: int, constraints: int
) -> int:
    """Calculate the pre-accessibility rubric level from the four scores."""
    scores = (language, behavior, design, constraints)
    if any(type(score) is not int or not 1 <= score <= 5 for score in scores):
        raise ValueError("all learning-level scores must be integers from 1 through 5")
    level = (sum(scores) + 2) // 4
    if 4 in scores:
        level = max(level, 3)
    if 5 in scores:
        level = max(level, 4)
    if level == 5 and sum(score == 5 for score in scores) < 2:
        level = 4
    return level


def calculate_published_level(rubric_level: int, accessibility_floor: int) -> int:
    """Apply the novice-accessibility floor to a structurally low rubric level."""
    if type(rubric_level) is not int or not 1 <= rubric_level <= 5:
        raise ValueError("rubric level must be an integer from 1 through 5")
    if type(accessibility_floor) is not int or not 1 <= accessibility_floor <= 3:
        raise ValueError("accessibility floor must be an integer from 1 through 3")
    return max(rubric_level, accessibility_floor)


def require_object(value: Any, path: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append(f"{path}: expected object")
        return {}
    return value


def require_exact_keys(
    value: dict[str, Any],
    required: tuple[str, ...],
    path: str,
    errors: list[str],
    *,
    optional: tuple[str, ...] = (),
) -> None:
    missing = [key for key in required if key not in value]
    if missing:
        errors.append(f"{path}: missing fields {', '.join(missing)}")
    unexpected = sorted(set(value) - set(required) - set(optional))
    if unexpected:
        errors.append(f"{path}: unexpected fields {', '.join(unexpected)}")


def require_text(value: Any, path: str, errors: list[str], minimum: int = 1) -> str:
    if not isinstance(value, str) or len(value.strip()) < minimum:
        errors.append(f"{path}: expected at least {minimum} non-whitespace characters")
        return ""
    return value.strip()


def require_text_list(
    value: Any,
    path: str,
    errors: list[str],
    *,
    minimum_items: int = 1,
    unique: bool = False,
) -> list[str]:
    if not isinstance(value, list) or len(value) < minimum_items:
        errors.append(f"{path}: expected at least {minimum_items} text item(s)")
        return []
    result: list[str] = []
    for index, item in enumerate(value):
        text = require_text(item, f"{path}[{index}]", errors)
        if text:
            result.append(text)
    if unique and len(result) != len(set(result)):
        errors.append(f"{path}: duplicate value")
    return result


def require_score(value: Any, path: str, errors: list[str]) -> int | None:
    if type(value) is not int or not 1 <= value <= 5:
        errors.append(f"{path}: expected integer from 1 through 5")
        return None
    return value


def require_date(value: Any, path: str, errors: list[str]) -> str:
    text = require_text(value, path, errors)
    if text:
        try:
            date.fromisoformat(text)
        except ValueError:
            errors.append(f"{path}: expected ISO date YYYY-MM-DD")
    return text


def validate_repository(
    entry: Any,
    language: dict[str, Any],
    index: int,
    seen_paths: set[tuple[str, str]],
    repository_counts: Counter[str],
    seen_repository_buckets: set[tuple[str, int, str]],
    seen_slugs: set[str],
    *,
    legacy_source_policy: bool = False,
) -> list[str]:
    """Validate one accepted learning-path record.

    Historical audit snapshots may retain the pre-source-class evidence field;
    canonical records must always use the current source policy.
    """
    errors: list[str] = []
    prefix = f"catalog/{language['slug']}.json repositories[{index}]"
    item = require_object(entry, prefix, errors)
    require_exact_keys(
        item,
        LEGACY_REPOSITORY_FIELDS if legacy_source_policy else REPOSITORY_FIELDS,
        prefix,
        errors,
        optional=OPTIONAL_REPOSITORY_FIELDS,
    )

    slug = require_text(item.get("slug"), f"{prefix}.slug", errors)
    if slug and not SLUG_RE.fullmatch(slug):
        errors.append(f"{prefix}.slug: use lowercase letters, digits, and single hyphens")
    if slug in seen_slugs:
        errors.append(f"{prefix}.slug: duplicate within language: {slug}")
    if slug:
        seen_slugs.add(slug)

    path_slug = require_text(item.get("path_slug"), f"{prefix}.path_slug", errors)
    if path_slug and not SLUG_RE.fullmatch(path_slug):
        errors.append(
            f"{prefix}.path_slug: use lowercase letters, digits, and single hyphens"
        )

    repository = require_text(item.get("repository"), f"{prefix}.repository", errors)
    if repository and not REPOSITORY_RE.fullmatch(repository):
        errors.append(f"{prefix}.repository: expected owner/name")
    repository_key = repository.lower()
    if repository and path_slug:
        path_key = (repository_key, path_slug)
        if path_key in seen_paths:
            errors.append(
                f"{prefix}.path_slug: duplicate catalog path: {repository}/{path_slug}"
            )
        else:
            seen_paths.add(path_key)
        repository_counts[repository_key] += 1
        if repository_counts[repository_key] > 2:
            errors.append(
                f"{prefix}.repository: {repository} exceeds the two-path catalog maximum"
            )

    url = require_text(item.get("url"), f"{prefix}.url", errors)
    expected_url = f"https://github.com/{repository}" if repository else ""
    if url and expected_url and url.rstrip("/") != expected_url:
        errors.append(f"{prefix}.url: expected {expected_url}")

    primary_language = require_text(
        item.get("primary_language"), f"{prefix}.primary_language", errors
    )
    if primary_language and primary_language != language["name"]:
        errors.append(
            f"{prefix}.primary_language: expected catalog language {language['name']}"
        )
    require_text(item.get("language_evidence"), f"{prefix}.language_evidence", errors, 20)
    require_text(item.get("description"), f"{prefix}.description", errors, 20)
    source_kind = "production"
    purpose_field = "real_world_evidence" if legacy_source_policy else "purpose_evidence"
    if not legacy_source_policy:
        source_kind = require_text(item.get("source_kind"), f"{prefix}.source_kind", errors)
        if source_kind and source_kind not in SOURCE_KINDS:
            errors.append(
                f"{prefix}.source_kind: expected production or educational-exemplar"
            )
    for field in (purpose_field, "why_study"):
        require_text(item.get(field), f"{prefix}.{field}", errors, 20)
    require_text_list(item.get("learn"), f"{prefix}.learn", errors)
    prerequisites = require_text_list(
        item.get("prerequisites"), f"{prefix}.prerequisites", errors
    )
    concepts_developed = require_text_list(
        item.get("concepts_developed"), f"{prefix}.concepts_developed", errors
    )
    normalized_prerequisites = {
        item.casefold().strip().rstrip(".") for item in prerequisites
    }
    for concept_index, concept in enumerate(concepts_developed):
        if concept.casefold().strip().rstrip(".") in normalized_prerequisites:
            errors.append(
                f"{prefix}.concepts_developed[{concept_index}]: duplicates a prerequisite"
            )

    coding = require_object(item.get("coding_relevance"), f"{prefix}.coding_relevance", errors)
    require_exact_keys(coding, ("gate", "domain_context", "reason"), f"{prefix}.coding_relevance", errors)
    gate = require_text(coding.get("gate"), f"{prefix}.coding_relevance.gate", errors)
    if gate and gate != "pass":
        errors.append(f"{prefix}.coding_relevance.gate: expected constant pass")
    require_text_list(
        coding.get("domain_context"),
        f"{prefix}.coding_relevance.domain_context",
        errors,
        minimum_items=0,
    )
    require_text(coding.get("reason"), f"{prefix}.coding_relevance.reason", errors, 20)

    learning_path = require_object(item.get("learning_path"), f"{prefix}.learning_path", errors)
    require_exact_keys(
        learning_path,
        ("goal", "start_here", "supporting_files", "trace"),
        f"{prefix}.learning_path",
        errors,
    )
    require_text(learning_path.get("goal"), f"{prefix}.learning_path.goal", errors, 20)
    start_here = require_object(
        learning_path.get("start_here"), f"{prefix}.learning_path.start_here", errors
    )
    require_exact_keys(start_here, ("path", "reason"), f"{prefix}.learning_path.start_here", errors)
    start_path = require_text(
        start_here.get("path"), f"{prefix}.learning_path.start_here.path", errors
    )
    require_text(
        start_here.get("reason"), f"{prefix}.learning_path.start_here.reason", errors, 20
    )
    if start_path and not is_safe_relative_path(start_path):
        errors.append(
            f"{prefix}.learning_path.start_here.path: expected canonical safe non-dotenv relative path"
        )
    supporting_files = require_text_list(
        learning_path.get("supporting_files"),
        f"{prefix}.learning_path.supporting_files",
        errors,
        unique=True,
    )
    for file_index, file_path in enumerate(supporting_files):
        if not is_safe_relative_path(file_path):
            errors.append(
                f"{prefix}.learning_path.supporting_files[{file_index}]: expected canonical safe non-dotenv relative path"
            )
    if start_path and start_path in supporting_files:
        errors.append(
            f"{prefix}.learning_path.supporting_files: must contain paths in addition to start_here.path"
        )
    require_text(learning_path.get("trace"), f"{prefix}.learning_path.trace", errors, 20)

    learning_level = require_object(
        item.get("learning_level"), f"{prefix}.learning_level", errors
    )
    require_exact_keys(
        learning_level,
        ("level", *DIMENSION_FIELDS, "placement"),
        f"{prefix}.learning_level",
        errors,
    )
    level = require_score(learning_level.get("level"), f"{prefix}.learning_level.level", errors)
    scores: dict[str, int | None] = {}
    for dimension in DIMENSION_FIELDS:
        judgment = require_object(
            learning_level.get(dimension), f"{prefix}.learning_level.{dimension}", errors
        )
        require_exact_keys(
            judgment,
            ("score", "signals", "reason"),
            f"{prefix}.learning_level.{dimension}",
            errors,
        )
        scores[dimension] = require_score(
            judgment.get("score"), f"{prefix}.learning_level.{dimension}.score", errors
        )
        require_text_list(
            judgment.get("signals"), f"{prefix}.learning_level.{dimension}.signals", errors
        )
        require_text(
            judgment.get("reason"), f"{prefix}.learning_level.{dimension}.reason", errors, 20
        )
    require_text(learning_level.get("placement"), f"{prefix}.learning_level.placement", errors, 20)
    ordered_scores = tuple(scores[name] for name in DIMENSION_FIELDS)
    rubric_level: int | None = None
    if None not in ordered_scores:
        rubric_level = calculate_learning_level(*ordered_scores)  # type: ignore[arg-type]

    accessibility_floor: int | None = None
    accessibility_present = "novice_accessibility" in item
    if accessibility_present:
        accessibility = require_object(
            item.get("novice_accessibility"),
            f"{prefix}.novice_accessibility",
            errors,
        )
        require_exact_keys(
            accessibility,
            NOVICE_ACCESSIBILITY_FIELDS,
            f"{prefix}.novice_accessibility",
            errors,
        )
        floor = accessibility.get("floor")
        if type(floor) is not int or not 1 <= floor <= 3:
            errors.append(
                f"{prefix}.novice_accessibility.floor: expected integer from 1 through 3"
            )
        else:
            accessibility_floor = floor
        require_text_list(
            accessibility.get("central_concepts"),
            f"{prefix}.novice_accessibility.central_concepts",
            errors,
            minimum_items=0,
        )
        require_text_list(
            accessibility.get("incidental_concepts"),
            f"{prefix}.novice_accessibility.incidental_concepts",
            errors,
            minimum_items=0,
        )
        require_text(
            accessibility.get("reason"),
            f"{prefix}.novice_accessibility.reason",
            errors,
            20,
        )

    if rubric_level is not None and rubric_level <= 2 and not accessibility_present:
        errors.append(
            f"{prefix}.novice_accessibility: required when rubric Level is {rubric_level}"
        )

    if level is not None and rubric_level is not None:
        expected_level = rubric_level
        if accessibility_floor is not None:
            expected_level = calculate_published_level(
                rubric_level, accessibility_floor
            )
        if level != expected_level:
            profile = "/".join(str(score) for score in ordered_scores)
            if accessibility_floor is None:
                errors.append(
                    f"{prefix}.learning_level.level: scores {profile} require rubric Level {expected_level}, not {level}"
                )
            else:
                errors.append(
                    f"{prefix}.learning_level.level: rubric Level {rubric_level} and accessibility floor {accessibility_floor} require Level {expected_level}, not {level}"
                )
    if (
        not legacy_source_policy
        and source_kind == "educational-exemplar"
        and level is not None
        and level > 2
    ):
        errors.append(
            f"{prefix}.source_kind: educational-exemplar may publish only at Level 1 or 2, not Level {level}"
        )
    if repository and level is not None:
        bucket_key = (language["slug"], level, repository_key)
        if bucket_key in seen_repository_buckets:
            errors.append(
                f"{prefix}.repository: {repository} appears twice in {language['name']} Level {level}"
            )
        else:
            seen_repository_buckets.add(bucket_key)

    quality = require_object(item.get("quality"), f"{prefix}.quality", errors)
    require_exact_keys(quality, QUALITY_FIELDS, f"{prefix}.quality", errors)
    for field in QUALITY_FIELDS:
        require_text(quality.get(field), f"{prefix}.quality.{field}", errors, 20)

    inspection = require_object(item.get("inspection"), f"{prefix}.inspection", errors)
    require_exact_keys(
        inspection,
        ("commit", "inspected_at", "reviewers", "files"),
        f"{prefix}.inspection",
        errors,
    )
    commit = require_text(inspection.get("commit"), f"{prefix}.inspection.commit", errors)
    if commit and not COMMIT_RE.fullmatch(commit):
        errors.append(f"{prefix}.inspection.commit: expected 40 lowercase hexadecimal characters")
    require_date(inspection.get("inspected_at"), f"{prefix}.inspection.inspected_at", errors)
    require_text_list(inspection.get("reviewers"), f"{prefix}.inspection.reviewers", errors)
    files = require_text_list(
        inspection.get("files"), f"{prefix}.inspection.files", errors, minimum_items=3, unique=True
    )
    for file_index, file_path in enumerate(files):
        if not is_safe_relative_path(file_path):
            errors.append(
                f"{prefix}.inspection.files[{file_index}]: expected canonical safe non-dotenv relative path"
            )
    for path_name, path_value in [
        ("start_here.path", start_path),
        *((f"supporting_files[{item_index}]", value) for item_index, value in enumerate(supporting_files)),
    ]:
        if path_value and path_value not in files:
            errors.append(f"{prefix}.learning_path.{path_name}: must also appear in inspection.files")

    license_info = require_object(item.get("license"), f"{prefix}.license", errors)
    require_exact_keys(license_info, ("spdx", "urls"), f"{prefix}.license", errors)
    require_text(license_info.get("spdx"), f"{prefix}.license.spdx", errors)
    license_urls = require_text_list(
        license_info.get("urls"), f"{prefix}.license.urls", errors, unique=True
    )
    license_prefix = f"{expected_url}/blob/{commit}/" if expected_url and commit else ""
    for url_index, license_url in enumerate(license_urls):
        if license_prefix and not license_url.startswith(license_prefix):
            errors.append(
                f"{prefix}.license.urls[{url_index}]: expected URL pinned to {repository} commit {commit}"
            )
            continue
        license_path = license_url.removeprefix(license_prefix) if license_prefix else ""
        if license_path and not is_safe_relative_path(license_path):
            errors.append(f"{prefix}.license.urls[{url_index}]: URL contains an unsafe path")
        if license_path and license_path not in files:
            errors.append(f"{prefix}.license.urls[{url_index}]: license path must appear in inspection.files")

    github = require_object(item.get("github"), f"{prefix}.github", errors)
    require_exact_keys(
        github,
        ("primary_language", "archived", "metadata_checked_at"),
        f"{prefix}.github",
        errors,
    )
    require_text(github.get("primary_language"), f"{prefix}.github.primary_language", errors)
    if type(github.get("archived")) is not bool:
        errors.append(f"{prefix}.github.archived: expected boolean")
    require_date(github.get("metadata_checked_at"), f"{prefix}.github.metadata_checked_at", errors)
    return errors


def validate_schema(root: Path) -> list[str]:
    """Catch drift between the published JSON Schema and the manual validator."""
    errors: list[str] = []
    try:
        schema = load_json(root / "catalog" / "schema.json")
    except CatalogError as error:
        return [str(error)]
    if (
        schema.get("properties", {}).get("schema_version", {}).get("const")
        != CATALOG_SCHEMA_VERSION
    ):
        errors.append(
            f"catalog/schema.json: schema_version must be the constant {CATALOG_SCHEMA_VERSION}"
        )
    repository = schema.get("$defs", {}).get("repository", {})
    if tuple(repository.get("required", ())) != REPOSITORY_FIELDS:
        errors.append("catalog/schema.json: repository required fields differ from the validator")
    repository_properties = repository.get("properties", {})
    if not all(field in repository_properties for field in OPTIONAL_REPOSITORY_FIELDS):
        errors.append("catalog/schema.json: optional repository fields differ from the validator")
    if tuple(repository_properties.get("source_kind", {}).get("enum", ())) != SOURCE_KINDS:
        errors.append("catalog/schema.json: source kinds differ from the validator")
    accessibility = schema.get("$defs", {}).get("noviceAccessibility", {})
    if tuple(accessibility.get("required", ())) != NOVICE_ACCESSIBILITY_FIELDS:
        errors.append("catalog/schema.json: novice accessibility fields differ from the validator")
    quality = schema.get("$defs", {}).get("quality", {})
    if tuple(quality.get("required", ())) != QUALITY_FIELDS:
        errors.append("catalog/schema.json: quality fields differ from the validator")
    license_schema = repository.get("properties", {}).get("license", {})
    if license_schema.get("required") != ["spdx", "urls"]:
        errors.append("catalog/schema.json: license evidence must use spdx and urls")
    safe_path_pattern = schema.get("$defs", {}).get("safePath", {}).get("pattern")
    if safe_path_pattern != SAFE_PATH_PATTERN:
        errors.append("catalog/schema.json: safePath pattern differs from the validator")
    return errors


def validate_languages(data: dict[str, Any]) -> tuple[list[dict[str, Any]], list[str]]:
    """Validate the separate, intentionally schema-version-1 language registry."""
    errors: list[str] = []
    if data.get("schema_version") != 1:
        errors.append("catalog/languages.json schema_version: expected 1")
    require_date(data.get("selected_at"), "catalog/languages.json selected_at", errors)
    baseline = require_object(data.get("baseline"), "catalog/languages.json baseline", errors)
    required_baseline = ("name", "url", "published_at", "rule")
    missing_baseline = [field for field in required_baseline if field not in baseline]
    if missing_baseline:
        errors.append(f"catalog/languages.json baseline: missing fields {', '.join(missing_baseline)}")
    for field in ("name", "url", "rule"):
        require_text(baseline.get(field), f"catalog/languages.json baseline.{field}", errors)
    require_date(baseline.get("published_at"), "catalog/languages.json baseline.published_at", errors)
    raw_languages = data.get("languages")
    if not isinstance(raw_languages, list):
        errors.append("catalog/languages.json languages: expected list")
        return [], errors
    if len(raw_languages) != 20:
        errors.append(f"catalog/languages.json languages: expected 20, found {len(raw_languages)}")
    languages: list[dict[str, Any]] = []
    slugs: set[str] = set()
    names: set[str] = set()
    for index, raw_language in enumerate(raw_languages):
        prefix = f"catalog/languages.json languages[{index}]"
        language = require_object(raw_language, prefix, errors)
        required = ("order", "slug", "name", "source", "source_rank")
        missing = [field for field in required if field not in language]
        if missing:
            errors.append(f"{prefix}: missing fields {', '.join(missing)}")
        if language.get("order") != index + 1:
            errors.append(f"{prefix}.order: expected {index + 1}")
        slug = require_text(language.get("slug"), f"{prefix}.slug", errors)
        name = require_text(language.get("name"), f"{prefix}.name", errors)
        require_text(language.get("source"), f"{prefix}.source", errors)
        require_text(language.get("source_rank"), f"{prefix}.source_rank", errors)
        if slug and not SLUG_RE.fullmatch(slug):
            errors.append(f"{prefix}.slug: invalid slug")
        if slug in slugs:
            errors.append(f"{prefix}.slug: duplicate {slug}")
        if name in names:
            errors.append(f"{prefix}.name: duplicate {name}")
        slugs.add(slug)
        names.add(name)
        if slug and name:
            languages.append(language)
    return languages, errors


def validate_novice_accessibility_audit(
    root: Path,
    languages: list[dict[str, Any]],
    canonical_entries: dict[tuple[str, str], dict[str, Any]],
) -> tuple[list[str], dict[str, Any]]:
    """Validate the lower-rung audit and expose its reconciliation state."""
    state: dict[str, Any] = {
        "capacity_by_repository": {},
        "records_by_repository": {},
        "replacement_by_repository": {},
    }
    path = root / "research" / "novice-accessibility-audit.json"
    if not path.exists():
        return [], state
    try:
        audit = load_json(path)
    except CatalogError as error:
        return [str(error)], state

    errors: list[str] = []
    prefix = "research/novice-accessibility-audit.json"
    require_exact_keys(
        audit,
        (
            "schema_version",
            "audited_at",
            "baseline",
            "method",
            "records",
            "capacity_alternates",
            "replacement_research",
            "progression_sanity_checks",
            "summary",
        ),
        prefix,
        errors,
    )
    if audit.get("schema_version") != 1:
        errors.append(f"{prefix} schema_version: expected 1")
    require_date(audit.get("audited_at"), f"{prefix}.audited_at", errors)
    require_text(audit.get("baseline"), f"{prefix}.baseline", errors, 40)
    method = require_object(audit.get("method"), f"{prefix}.method", errors)
    require_exact_keys(
        method,
        ("rubric_level", "published_level", "tests", "capacity"),
        f"{prefix}.method",
        errors,
    )
    require_text(method.get("rubric_level"), f"{prefix}.method.rubric_level", errors)
    require_text(
        method.get("published_level"), f"{prefix}.method.published_level", errors
    )
    method_tests = require_text_list(
        method.get("tests"), f"{prefix}.method.tests", errors, unique=True
    )
    if len(method_tests) != 5:
        errors.append(f"{prefix}.method.tests: expected the five accessibility tests")
    require_text(method.get("capacity"), f"{prefix}.method.capacity", errors, 20)

    language_by_slug = {language["slug"]: language for language in languages}
    alternate_entries: dict[tuple[str, str], dict[str, Any]] = {}
    alternates = audit.get("capacity_alternates")
    if not isinstance(alternates, list):
        errors.append(f"{prefix}.capacity_alternates: expected list")
        alternates = []
    alternate_fields = (
        "repository",
        "path_slug",
        "status",
        "displaced_from",
        "reason",
        "catalog_entry",
    )
    for index, raw_alternate in enumerate(alternates):
        item_prefix = f"{prefix}.capacity_alternates[{index}]"
        alternate = require_object(raw_alternate, item_prefix, errors)
        require_exact_keys(alternate, alternate_fields, item_prefix, errors)
        repository = require_text(
            alternate.get("repository"), f"{item_prefix}.repository", errors
        )
        path_slug = require_text(
            alternate.get("path_slug"), f"{item_prefix}.path_slug", errors
        )
        if alternate.get("status") != "qualified-capacity-alternate":
            errors.append(
                f"{item_prefix}.status: expected qualified-capacity-alternate"
            )
        require_text(alternate.get("reason"), f"{item_prefix}.reason", errors, 20)
        displaced = require_object(
            alternate.get("displaced_from"), f"{item_prefix}.displaced_from", errors
        )
        require_exact_keys(
            displaced, ("language_slug", "level"), f"{item_prefix}.displaced_from", errors
        )
        language_slug = displaced.get("language_slug")
        if language_slug not in language_by_slug:
            errors.append(f"{item_prefix}.displaced_from.language_slug: unknown language")
        if displaced.get("level") != 3:
            errors.append(f"{item_prefix}.displaced_from.level: expected 3")
        entry = require_object(
            alternate.get("catalog_entry"), f"{item_prefix}.catalog_entry", errors
        )
        key = (repository.lower(), path_slug)
        if key in alternate_entries:
            errors.append(f"{item_prefix}: duplicate capacity alternate")
        alternate_entries[key] = entry
        state["capacity_by_repository"].setdefault(repository.lower(), []).append(entry)
        if entry.get("repository") != repository or entry.get("path_slug") != path_slug:
            errors.append(f"{item_prefix}.catalog_entry: identity differs from alternate")
        language = language_by_slug.get(language_slug)
        if language:
            errors.extend(
                validate_repository(
                    entry,
                    language,
                    index,
                    set(),
                    Counter(),
                    set(),
                    set(),
                    legacy_source_policy=True,
                )
            )
        if entry.get("learning_level", {}).get("level") != 3:
            errors.append(f"{item_prefix}.catalog_entry: expected published Level 3")

    records = audit.get("records")
    if not isinstance(records, list):
        errors.append(f"{prefix}.records: expected list")
        records = []
    record_fields = (
        "language_slug",
        "repository",
        "path_slug",
        "pinned_commit",
        "old_level",
        "rubric_level",
        "central_concepts",
        "incidental_concepts",
        "accessibility_floor",
        "final_level",
        "novice_orientation_judgment",
        "accessibility_tests",
        "jargon_prerequisite_findings",
        "source_files_inspected",
        "decision",
        "prose_changes",
        "capacity_result",
    )
    test_fields = (
        "five_minute_orientation",
        "no_hidden_course",
        "prediction",
        "jargon",
        "prerequisite_stack",
    )
    seen_records: set[tuple[str, str]] = set()
    old_counts: Counter[int] = Counter()
    for index, raw_record in enumerate(records):
        item_prefix = f"{prefix}.records[{index}]"
        record = require_object(raw_record, item_prefix, errors)
        require_exact_keys(record, record_fields, item_prefix, errors)
        language_slug = record.get("language_slug")
        if language_slug not in language_by_slug:
            errors.append(f"{item_prefix}.language_slug: unknown language")
        repository = require_text(
            record.get("repository"), f"{item_prefix}.repository", errors
        )
        path_slug = require_text(
            record.get("path_slug"), f"{item_prefix}.path_slug", errors
        )
        key = (repository.lower(), path_slug)
        if key in seen_records:
            errors.append(f"{item_prefix}: duplicate audited path")
        seen_records.add(key)
        state["records_by_repository"].setdefault(repository.lower(), []).append(record)
        commit = require_text(
            record.get("pinned_commit"), f"{item_prefix}.pinned_commit", errors
        )
        if commit and not COMMIT_RE.fullmatch(commit):
            errors.append(f"{item_prefix}.pinned_commit: expected 40 lowercase hexadecimal characters")
        old_level = record.get("old_level")
        rubric_level = record.get("rubric_level")
        floor = record.get("accessibility_floor")
        final_level = record.get("final_level")
        if old_level not in (1, 2):
            errors.append(f"{item_prefix}.old_level: expected 1 or 2")
        else:
            old_counts[old_level] += 1
        if rubric_level != old_level:
            errors.append(f"{item_prefix}.rubric_level: expected unchanged old Level")
        if type(floor) is not int or not 1 <= floor <= 3:
            errors.append(f"{item_prefix}.accessibility_floor: expected integer 1 through 3")
        elif final_level != max(rubric_level, floor):
            errors.append(f"{item_prefix}.final_level: must equal max(rubric level, floor)")
        central = require_text_list(
            record.get("central_concepts"),
            f"{item_prefix}.central_concepts",
            errors,
            minimum_items=1,
            unique=True,
        )
        incidental = require_text_list(
            record.get("incidental_concepts"),
            f"{item_prefix}.incidental_concepts",
            errors,
            minimum_items=0,
            unique=True,
        )
        require_text(
            record.get("novice_orientation_judgment"),
            f"{item_prefix}.novice_orientation_judgment",
            errors,
            20,
        )
        accessibility_tests = require_object(
            record.get("accessibility_tests"),
            f"{item_prefix}.accessibility_tests",
            errors,
        )
        require_exact_keys(
            accessibility_tests,
            test_fields,
            f"{item_prefix}.accessibility_tests",
            errors,
        )
        for field in test_fields:
            require_text(
                accessibility_tests.get(field),
                f"{item_prefix}.accessibility_tests.{field}",
                errors,
            )
        require_text(
            record.get("jargon_prerequisite_findings"),
            f"{item_prefix}.jargon_prerequisite_findings",
            errors,
            20,
        )
        files = require_text_list(
            record.get("source_files_inspected"),
            f"{item_prefix}.source_files_inspected",
            errors,
            minimum_items=2,
            unique=True,
        )
        for file_index, file_path in enumerate(files):
            if not is_safe_relative_path(file_path):
                errors.append(
                    f"{item_prefix}.source_files_inspected[{file_index}]: expected canonical safe non-dotenv relative path"
                )
        if record.get("decision") not in (
            "keep-level-1",
            "keep-level-2",
            "relevel-to-2",
            "relevel-to-3",
            "remove",
        ):
            errors.append(f"{item_prefix}.decision: invalid audit decision")
        require_text(record.get("prose_changes"), f"{item_prefix}.prose_changes", errors)
        require_text(record.get("capacity_result"), f"{item_prefix}.capacity_result", errors)
        entry = canonical_entries.get(key) or alternate_entries.get(key)
        if entry is None:
            errors.append(f"{item_prefix}: audited path is neither published nor preserved")
        else:
            if entry.get("inspection", {}).get("commit") != commit:
                errors.append(f"{item_prefix}: audited pin differs from resolved path")
            if entry.get("learning_level", {}).get("level") != final_level:
                errors.append(f"{item_prefix}: final Level differs from resolved path")
            accessibility = entry.get("novice_accessibility", {})
            if accessibility.get("floor") != floor:
                errors.append(f"{item_prefix}: accessibility floor differs from resolved path")
            if accessibility.get("central_concepts") != central:
                errors.append(f"{item_prefix}: central concepts differ from resolved path")
            if accessibility.get("incidental_concepts") != incidental:
                errors.append(f"{item_prefix}: incidental concepts differ from resolved path")

    if old_counts != Counter({1: 3, 2: 35}):
        errors.append(f"{prefix}.records: expected 3 Level 1 and 35 Level 2 starting paths")
    if set(alternate_entries) - seen_records:
        errors.append(f"{prefix}.capacity_alternates: every alternate needs an audit record")

    replacement_records = audit.get("replacement_research")
    if not isinstance(replacement_records, list):
        errors.append(f"{prefix}.replacement_research: expected list")
        replacement_records = []
    replacement_fields = (
        "language_slug",
        "trigger",
        "accepted_repositories_reviewed",
        "prior_alternates_and_rejections_reviewed",
        "exact_pin_accessibility_rechecks",
        "fresh_external_discovery",
        "accepted",
        "open_levels_after",
        "conclusion",
    )
    for index, raw_replacement in enumerate(replacement_records):
        item_prefix = f"{prefix}.replacement_research[{index}]"
        replacement = require_object(raw_replacement, item_prefix, errors)
        require_exact_keys(replacement, replacement_fields, item_prefix, errors)
        expected_language = languages[index] if index < len(languages) else None
        language_slug = replacement.get("language_slug")
        if expected_language and language_slug != expected_language["slug"]:
            errors.append(
                f"{item_prefix}.language_slug: expected {expected_language['slug']}"
            )
        require_text(replacement.get("trigger"), f"{item_prefix}.trigger", errors)
        require_text_list(
            replacement.get("accepted_repositories_reviewed"),
            f"{item_prefix}.accepted_repositories_reviewed",
            errors,
            minimum_items=1,
            unique=True,
        )
        if not isinstance(replacement.get("prior_alternates_and_rejections_reviewed"), list):
            errors.append(
                f"{item_prefix}.prior_alternates_and_rejections_reviewed: expected list"
            )
        rechecks = replacement.get("exact_pin_accessibility_rechecks")
        if not isinstance(rechecks, list):
            errors.append(f"{item_prefix}.exact_pin_accessibility_rechecks: expected list")
            rechecks = []
        accepted = require_text_list(
            replacement.get("accepted"),
            f"{item_prefix}.accepted",
            errors,
            minimum_items=0,
            unique=True,
        )
        accepted_from_rechecks: set[str] = set()
        accepted_levels_from_rechecks: Counter[int] = Counter()
        for recheck_index, raw_recheck in enumerate(rechecks):
            recheck_prefix = (
                f"{item_prefix}.exact_pin_accessibility_rechecks[{recheck_index}]"
            )
            recheck = require_object(raw_recheck, recheck_prefix, errors)
            recheck_fields = (
                "repository",
                "pinned_commit",
                "source_files_inspected",
                "rubric_level",
                "accessibility_floor",
                "central_concepts",
                "incidental_concepts",
                "decision",
                "reason",
            )
            require_exact_keys(recheck, recheck_fields, recheck_prefix, errors)
            repository = require_text(
                recheck.get("repository"), f"{recheck_prefix}.repository", errors
            )
            commit = require_text(
                recheck.get("pinned_commit"), f"{recheck_prefix}.pinned_commit", errors
            )
            if commit and not COMMIT_RE.fullmatch(commit):
                errors.append(f"{recheck_prefix}.pinned_commit: invalid commit")
            files = require_text_list(
                recheck.get("source_files_inspected"),
                f"{recheck_prefix}.source_files_inspected",
                errors,
                minimum_items=2,
                unique=True,
            )
            for file_index, file_path in enumerate(files):
                if not is_safe_relative_path(file_path):
                    errors.append(
                        f"{recheck_prefix}.source_files_inspected[{file_index}]: expected canonical safe non-dotenv relative path"
                    )
            floor = recheck.get("accessibility_floor")
            rubric = recheck.get("rubric_level")
            if rubric not in (1, 2) or type(floor) is not int or not 1 <= floor <= 3:
                errors.append(f"{recheck_prefix}: invalid rubric level or accessibility floor")
            require_text_list(
                recheck.get("central_concepts"),
                f"{recheck_prefix}.central_concepts",
                errors,
                minimum_items=1,
                unique=True,
            )
            require_text_list(
                recheck.get("incidental_concepts"),
                f"{recheck_prefix}.incidental_concepts",
                errors,
                minimum_items=0,
                unique=True,
            )
            require_text(recheck.get("reason"), f"{recheck_prefix}.reason", errors, 20)
            decision = recheck.get("decision")
            if decision == "accept-level-2":
                accepted_from_rechecks.add(repository)
                state["replacement_by_repository"][repository.lower()] = recheck
                if rubric in (1, 2) and type(floor) is int and 1 <= floor <= 3:
                    expected_level = max(rubric, floor)
                    accepted_levels_from_rechecks[expected_level] += 1
                    matching_entries = [
                        entry
                        for (entry_repository, _), entry in canonical_entries.items()
                        if entry_repository == repository.lower()
                    ]
                    if not any(
                        entry.get("inspection", {}).get("commit") == commit
                        and entry.get("learning_level", {}).get("level") == expected_level
                        for entry in matching_entries
                    ):
                        errors.append(
                            f"{recheck_prefix}: accepted replacement differs from catalog"
                        )
            elif decision != "retain-qualified-alternate-at-level-3":
                errors.append(f"{recheck_prefix}.decision: invalid replacement decision")
        if set(accepted) != accepted_from_rechecks:
            errors.append(f"{item_prefix}.accepted: does not match accepted rechecks")
        fresh = require_object(
            replacement.get("fresh_external_discovery"),
            f"{item_prefix}.fresh_external_discovery",
            errors,
        )
        require_exact_keys(
            fresh, ("run", "reason"), f"{item_prefix}.fresh_external_discovery", errors
        )
        if type(fresh.get("run")) is not bool:
            errors.append(f"{item_prefix}.fresh_external_discovery.run: expected boolean")
        require_text(
            fresh.get("reason"), f"{item_prefix}.fresh_external_discovery.reason", errors, 20
        )
        open_levels = require_object(
            replacement.get("open_levels_after"), f"{item_prefix}.open_levels_after", errors
        )
        require_exact_keys(open_levels, ("1", "2"), f"{item_prefix}.open_levels_after", errors)
        historical_counts = Counter(
            record.get("final_level")
            for record in records
            if isinstance(record, dict)
            and record.get("language_slug") == language_slug
            and record.get("decision") != "remove"
            and record.get("final_level") in (1, 2)
        )
        expected_open = {
            str(level): 2
            - historical_counts[level]
            - accepted_levels_from_rechecks[level]
            for level in (1, 2)
        }
        if open_levels != expected_open:
            errors.append(
                f"{item_prefix}.open_levels_after: differs from historical audited outcomes"
            )
        require_text(replacement.get("conclusion"), f"{item_prefix}.conclusion", errors, 20)
    if replacement_records and len(replacement_records) != len(languages):
        errors.append(f"{prefix}.replacement_research: expected one pass per language")

    progression = audit.get("progression_sanity_checks")
    if not isinstance(progression, list):
        errors.append(f"{prefix}.progression_sanity_checks: expected list")
        progression = []
    progression_fields = (
        "language_slug",
        "published_progression",
        "reasonable_increase",
        "level_1_friendlier_than_level_2",
        "level_2_prepares_for_level_3",
        "jargon_progression",
        "novice_start",
        "result",
    )
    progression_slugs: list[str] = []
    for index, raw_check in enumerate(progression):
        item_prefix = f"{prefix}.progression_sanity_checks[{index}]"
        check = require_object(raw_check, item_prefix, errors)
        require_exact_keys(check, progression_fields, item_prefix, errors)
        language_slug = check.get("language_slug")
        if language_slug not in language_by_slug:
            errors.append(f"{item_prefix}.language_slug: unknown language")
        elif language_slug in progression_slugs:
            errors.append(f"{item_prefix}.language_slug: duplicate progression check")
        progression_slugs.append(language_slug)
        published = require_object(
            check.get("published_progression"),
            f"{item_prefix}.published_progression",
            errors,
        )
        require_exact_keys(
            published, ("1", "2", "3"), f"{item_prefix}.published_progression", errors
        )
        for level in ("1", "2", "3"):
            require_text_list(
                published.get(level),
                f"{item_prefix}.published_progression.{level}",
                errors,
                minimum_items=0,
                unique=True,
            )
        for field in progression_fields[2:-1]:
            require_text(check.get(field), f"{item_prefix}.{field}", errors, 20)
        if check.get("result") not in ("pass", "pass-with-explicit-gap"):
            errors.append(f"{item_prefix}.result: expected pass or pass-with-explicit-gap")
    if len(progression) < 5:
        errors.append(f"{prefix}.progression_sanity_checks: expected at least five languages")
    for required_slug in ("javascript", "php"):
        if required_slug not in progression_slugs:
            errors.append(
                f"{prefix}.progression_sanity_checks: missing required {required_slug} check"
            )

    summary = require_object(audit.get("summary"), f"{prefix}.summary", errors)
    summary_fields = (
        "level_1_before",
        "level_1_after",
        "level_2_before",
        "level_2_after",
        "promoted",
        "demoted",
        "removed_for_quality",
        "displaced_for_capacity",
        "removed",
        "replaced",
        "remaining_gaps",
    )
    require_exact_keys(summary, summary_fields, f"{prefix}.summary", errors)
    historical_low_counts = Counter(
        record.get("final_level")
        for record in records
        if record.get("decision") != "remove"
    )
    historical_low_counts[2] += len(state["replacement_by_repository"])
    expected_summary = {
        "level_1_before": 3,
        "level_1_after": historical_low_counts[1],
        "level_2_before": 35,
        "level_2_after": historical_low_counts[2],
        "promoted": sum(
            1 for record in records if record.get("final_level", 0) > record.get("old_level", 0)
        ),
        "demoted": sum(
            1 for record in records if record.get("final_level", 0) < record.get("old_level", 0)
        ),
        "removed_for_quality": sum(
            1 for record in records if record.get("decision") == "remove"
        ),
        "displaced_for_capacity": len(alternates),
        "removed": len(alternates)
        + sum(1 for record in records if record.get("decision") == "remove"),
        "replaced": len(state["replacement_by_repository"]),
        "remaining_gaps": 75,
    }
    if summary != expected_summary:
        errors.append(f"{prefix}.summary: does not match audited outcomes and catalog")
    return errors, state


def validate_rebuild_reconciliation(
    root: Path,
    canonical_entries: dict[tuple[str, str], dict[str, Any]],
    novice_state: dict[str, Any] | None = None,
) -> list[str]:
    """Keep the v1 re-review partition reconciled as new candidates are added."""
    audit_path = root / "research" / "learner-centered-rebuild.json"
    rejections_path = root / "research" / "rejections.json"
    if not audit_path.exists() and not rejections_path.exists():
        return []
    if not audit_path.exists() or not rejections_path.exists():
        return ["research: rebuild audit and rejection history must exist together"]
    try:
        audit = load_json(audit_path)
        rejections = load_json(rejections_path)
    except CatalogError as error:
        return [str(error)]
    errors: list[str] = []
    decisions = audit.get("decisions")
    rejection_records = rejections.get("rejections")
    if not isinstance(decisions, list) or len(decisions) != 200:
        return ["research/learner-centered-rebuild.json: expected 200 decisions"]
    if not isinstance(rejection_records, list):
        return ["research/rejections.json rejections: expected list"]
    entries_by_repository: dict[str, list[dict[str, Any]]] = {}
    for entry in canonical_entries.values():
        entries_by_repository.setdefault(entry["repository"].lower(), []).append(entry)
    capacity_alternate_keys: set[str] = set()
    remediation_path = root / "research" / "learner-centered-remediation.json"
    if remediation_path.exists():
        try:
            remediation = load_json(remediation_path)
        except CatalogError as error:
            errors.append(str(error))
            remediation = {}
        alternates = remediation.get("score_guardrail_migration", {}).get(
            "capacity_alternates", []
        )
        if isinstance(alternates, list):
            capacity_alternate_keys = {
                alternate.get("repository", "").lower()
                for alternate in alternates
                if isinstance(alternate, dict)
                and isinstance(alternate.get("repository"), str)
            }
    if novice_state:
        capacity_alternate_keys.update(novice_state["capacity_by_repository"])
    decision_keys = [
        item.get("repository", "").lower() for item in decisions if isinstance(item, dict)
    ]
    if len(decision_keys) != 200 or len(set(decision_keys)) != 200:
        errors.append("research/learner-centered-rebuild.json: decisions must be unique")
    removed_keys = [
        item.get("repository", "").lower()
        for item in decisions
        if isinstance(item, dict) and item.get("decision") == "remove"
    ]
    rejection_keys = [
        item.get("repository", "").lower()
        for item in rejection_records
        if isinstance(item, dict)
    ]
    cutover_starts = [
        index
        for index in range(len(rejection_keys) - len(removed_keys) + 1)
        if rejection_keys[index : index + len(removed_keys)] == removed_keys
    ]
    if len(cutover_starts) != 1:
        errors.append(
            "research/rejections.json: expected exactly one ordered cutover-removal block"
        )
    for decision in decisions:
        if not isinstance(decision, dict):
            errors.append("research/learner-centered-rebuild.json: decision must be an object")
            continue
        repository = decision.get("repository", "")
        key = repository.lower()
        outcome = decision.get("decision")
        if outcome == "retain":
            entries = entries_by_repository.get(key, [])
            if not entries and key not in capacity_alternate_keys:
                errors.append(f"research reconciliation: retained repository missing: {repository}")
            elif entries and not any(
                entry.get("inspection", {}).get("commit") == decision.get("pinned_commit")
                for entry in entries
            ):
                errors.append(f"research reconciliation: retained pin changed: {repository}")
        elif outcome == "remove":
            matching_historical_path = [
                entry
                for entry in entries_by_repository.get(key, [])
                if entry.get("inspection", {}).get("commit")
                == decision.get("pinned_commit")
                and entry.get("learning_path", {}).get("start_here", {}).get("path")
                == decision.get("learning_path", {}).get("start_path")
            ]
            if matching_historical_path:
                errors.append(
                    f"research reconciliation: removed repository path is still accepted: {repository}"
                )
        else:
            errors.append(f"research reconciliation: invalid decision for {repository}")
    return errors


def validate_gap_research(
    root: Path,
    languages: list[dict[str, Any]],
    canonical_entries: dict[tuple[str, str], dict[str, Any]],
    novice_state: dict[str, Any] | None = None,
) -> list[str]:
    """Reconcile the incremental post-cutover research record with the catalog."""
    path = root / "research" / "learner-centered-gap-research.json"
    if not path.exists():
        return []
    try:
        audit = load_json(path)
        rejections = load_json(root / "research" / "rejections.json")
    except CatalogError as error:
        return [str(error)]
    errors: list[str] = []
    entries_by_repository: dict[str, list[dict[str, Any]]] = {}
    for entry in canonical_entries.values():
        entries_by_repository.setdefault(entry["repository"].lower(), []).append(entry)
    novice_state = novice_state or {
        "capacity_by_repository": {},
        "records_by_repository": {},
        "replacement_by_repository": {},
    }
    capacity_by_repository = novice_state["capacity_by_repository"]
    records_by_repository = novice_state["records_by_repository"]
    replacement_by_repository = novice_state["replacement_by_repository"]
    require_exact_keys(
        audit,
        (
            "schema_version",
            "research_started_at",
            "cutover_commit",
            "target",
            "languages",
            "summary",
        ),
        "research/learner-centered-gap-research.json",
        errors,
    )
    if audit.get("schema_version") != 1:
        errors.append("research/learner-centered-gap-research.json schema_version: expected 1")
    require_date(
        audit.get("research_started_at"),
        "research/learner-centered-gap-research.json research_started_at",
        errors,
    )
    commit = require_text(
        audit.get("cutover_commit"),
        "research/learner-centered-gap-research.json cutover_commit",
        errors,
    )
    if commit and not COMMIT_RE.fullmatch(commit):
        errors.append(
            "research/learner-centered-gap-research.json cutover_commit: expected 40 lowercase hexadecimal characters"
        )
    records = audit.get("languages")
    if not isinstance(records, list):
        return errors + ["research/learner-centered-gap-research.json languages: expected list"]
    if len(records) > len(languages):
        errors.append("research/learner-centered-gap-research.json languages: too many records")
    candidate_keys: set[str] = set()
    accepted_total = 0
    rejected_total = 0
    rejection_records = rejections.get("rejections", [])
    record_fields = (
        "order",
        "language_slug",
        "language",
        "researched_at",
        "starting_entries",
        "gaps_before",
        "discovery_channels",
        "candidates",
        "accepted",
        "rejected",
        "gaps_after",
        "conclusion",
    )
    candidate_fields = (
        "repository",
        "pinned_commit",
        "discovered_via",
        "inspection_files",
        "decision",
        "coding_relevance_status",
        "coding_relevance_evidence",
        "quality_status",
        "quality_evidence",
        "decision_evidence",
        "second_review",
    )
    for index, raw_record in enumerate(records):
        prefix = f"research/learner-centered-gap-research.json languages[{index}]"
        record = require_object(raw_record, prefix, errors)
        require_exact_keys(record, record_fields, prefix, errors)
        expected_language = languages[index]
        if record.get("order") != index + 1:
            errors.append(f"{prefix}.order: expected {index + 1}")
        if record.get("language_slug") != expected_language["slug"]:
            errors.append(f"{prefix}.language_slug: expected {expected_language['slug']}")
        if record.get("language") != expected_language["name"]:
            errors.append(f"{prefix}.language: expected {expected_language['name']}")
        researched_at = require_date(record.get("researched_at"), f"{prefix}.researched_at", errors)
        channels = record.get("discovery_channels")
        if not isinstance(channels, list) or len(channels) < 3:
            errors.append(f"{prefix}.discovery_channels: expected at least 3 channels")
            channels = []
        channel_ids = [
            channel.get("id")
            for channel in channels
            if isinstance(channel, dict) and isinstance(channel.get("id"), str)
        ]
        if len(channel_ids) != len(channels) or len(set(channel_ids)) != len(channel_ids):
            errors.append(f"{prefix}.discovery_channels: channel ids must be present and unique")
        for channel_index, raw_channel in enumerate(channels):
            channel_prefix = f"{prefix}.discovery_channels[{channel_index}]"
            channel = require_object(raw_channel, channel_prefix, errors)
            require_exact_keys(channel, ("id", "channel", "sources", "evidence"), channel_prefix, errors)
            require_text(channel.get("id"), f"{channel_prefix}.id", errors)
            require_text(channel.get("channel"), f"{channel_prefix}.channel", errors, 10)
            require_text_list(
                channel.get("sources"), f"{channel_prefix}.sources", errors, unique=True
            )
            require_text(channel.get("evidence"), f"{channel_prefix}.evidence", errors, 20)
        starting_entries = record.get("starting_entries")
        if not isinstance(starting_entries, list):
            errors.append(f"{prefix}.starting_entries: expected list")
            starting_entries = []
        starting_levels = Counter(
            item.get("level") for item in starting_entries if isinstance(item, dict)
        )
        expected_before = {str(level): 2 - starting_levels[level] for level in range(1, 6)}
        if record.get("gaps_before") != expected_before:
            errors.append(f"{prefix}.gaps_before: does not match starting entries")
        candidates = record.get("candidates")
        if not isinstance(candidates, list):
            errors.append(f"{prefix}.candidates: expected list")
            candidates = []
        accepted = record.get("accepted")
        rejected = record.get("rejected")
        if not isinstance(accepted, list) or not isinstance(rejected, list):
            errors.append(f"{prefix}: accepted and rejected must be lists")
            accepted = []
            rejected = []
        candidate_decisions: dict[str, str] = {}
        for candidate_index, raw_candidate in enumerate(candidates):
            candidate_prefix = f"{prefix}.candidates[{candidate_index}]"
            candidate = require_object(raw_candidate, candidate_prefix, errors)
            coding_status = candidate.get("coding_relevance_status")
            quality_status = candidate.get("quality_status")
            scored = coding_status == "pass" and quality_status == "pass"
            required_candidate_fields = candidate_fields + (
                ("scores", "calculated_level") if scored else ()
            )
            require_exact_keys(candidate, required_candidate_fields, candidate_prefix, errors)
            repository = require_text(
                candidate.get("repository"), f"{candidate_prefix}.repository", errors
            )
            if repository and not REPOSITORY_RE.fullmatch(repository):
                errors.append(f"{candidate_prefix}.repository: expected owner/name")
            key = repository.lower()
            if key in candidate_keys:
                errors.append(f"{candidate_prefix}.repository: duplicate gap candidate")
            if key:
                candidate_keys.add(key)
            pinned_commit = require_text(
                candidate.get("pinned_commit"), f"{candidate_prefix}.pinned_commit", errors
            )
            if pinned_commit and not COMMIT_RE.fullmatch(pinned_commit):
                errors.append(
                    f"{candidate_prefix}.pinned_commit: expected 40 lowercase hexadecimal characters"
                )
            discovered_via = require_text_list(
                candidate.get("discovered_via"),
                f"{candidate_prefix}.discovered_via",
                errors,
                unique=True,
            )
            for channel_id in discovered_via:
                if channel_id not in channel_ids:
                    errors.append(
                        f"{candidate_prefix}.discovered_via: unknown channel id {channel_id}"
                    )
            inspection_files = require_text_list(
                candidate.get("inspection_files"),
                f"{candidate_prefix}.inspection_files",
                errors,
                minimum_items=3,
                unique=True,
            )
            for file_index, file_path in enumerate(inspection_files):
                if not is_safe_relative_path(file_path):
                    errors.append(
                        f"{candidate_prefix}.inspection_files[{file_index}]: expected canonical safe non-dotenv relative path"
                    )
            if coding_status not in ("pass", "fail"):
                errors.append(
                    f"{candidate_prefix}.coding_relevance_status: expected pass or fail"
                )
            if quality_status not in ("pass", "fail"):
                errors.append(f"{candidate_prefix}.quality_status: expected pass or fail")
            require_text(
                candidate.get("coding_relevance_evidence"),
                f"{candidate_prefix}.coding_relevance_evidence",
                errors,
                20,
            )
            require_text(
                candidate.get("quality_evidence"),
                f"{candidate_prefix}.quality_evidence",
                errors,
                20,
            )
            require_text(
                candidate.get("decision_evidence"),
                f"{candidate_prefix}.decision_evidence",
                errors,
                20,
            )
            decision = candidate.get("decision")
            candidate_decisions[repository] = decision
            calculated = None
            if scored:
                scores = require_object(
                    candidate.get("scores"), f"{candidate_prefix}.scores", errors
                )
                require_exact_keys(scores, DIMENSION_FIELDS, f"{candidate_prefix}.scores", errors)
                ordered_scores = tuple(
                    require_score(
                        scores.get(name), f"{candidate_prefix}.scores.{name}", errors
                    )
                    for name in DIMENSION_FIELDS
                )
                calculated = candidate.get("calculated_level")
                if None not in ordered_scores:
                    expected_level = calculate_learning_level(*ordered_scores)  # type: ignore[arg-type]
                    if calculated != expected_level:
                        errors.append(
                            f"{candidate_prefix}.calculated_level: scores require Level {expected_level}"
                        )
            second_review = require_object(
                candidate.get("second_review"), f"{candidate_prefix}.second_review", errors
            )
            require_exact_keys(
                second_review,
                ("reviewer", "status", "notes"),
                f"{candidate_prefix}.second_review",
                errors,
            )
            require_text(
                second_review.get("reviewer"), f"{candidate_prefix}.second_review.reviewer", errors
            )
            require_text(
                second_review.get("notes"),
                f"{candidate_prefix}.second_review.notes",
                errors,
                20,
            )
            if second_review.get("status") != "agree":
                errors.append(f"{candidate_prefix}.second_review.status: expected agree")
            if decision == "accept":
                accepted_total += 1
                if not scored:
                    errors.append(f"{candidate_prefix}: acceptance requires both gates to pass")
                entries = entries_by_repository.get(key, [])
                capacity_entries = capacity_by_repository.get(key, [])
                resolved_entries = entries + capacity_entries
                if not resolved_entries:
                    errors.append(f"{candidate_prefix}: accepted candidate missing from catalog")
                else:
                    matching_pin = [
                        entry
                        for entry in resolved_entries
                        if entry.get("inspection", {}).get("commit")
                        == candidate.get("pinned_commit")
                    ]
                    if not matching_pin:
                        errors.append(f"{candidate_prefix}: accepted pin differs from catalog")
                    elif not any(
                        entry.get("learning_level", {}).get("level") == calculated
                        for entry in matching_pin
                    ):
                        novice_records = records_by_repository.get(key, [])
                        if not any(
                            record.get("pinned_commit") == candidate.get("pinned_commit")
                            and record.get("rubric_level") == calculated
                            and any(
                                entry.get("learning_level", {}).get("level")
                                == record.get("final_level")
                                for entry in matching_pin
                            )
                            for record in novice_records
                        ):
                            errors.append(
                                f"{candidate_prefix}: accepted Level differs from catalog"
                            )
            elif decision == "reject":
                rejected_total += 1
                if key in replacement_by_repository:
                    replacement = replacement_by_repository[key]
                    matching_entries = entries_by_repository.get(key, [])
                    if not any(
                        entry.get("inspection", {}).get("commit")
                        == replacement.get("pinned_commit")
                        and entry.get("learning_level", {}).get("level")
                        == max(
                            replacement.get("rubric_level", 0),
                            replacement.get("accessibility_floor", 0),
                        )
                        for entry in matching_entries
                    ):
                        errors.append(
                            f"{candidate_prefix}: later novice-accessibility acceptance differs from catalog"
                        )
                matching_rejections = [
                    item
                    for item in rejection_records
                    if isinstance(item, dict)
                    and item.get("repository", "").lower() == key
                    and item.get("inspected_at") == researched_at
                    and item.get("evidence") == candidate.get("decision_evidence")
                ]
                if len(matching_rejections) != 1:
                    errors.append(f"{candidate_prefix}: expected one matching rejection record")
            else:
                errors.append(f"{candidate_prefix}.decision: expected accept or reject")
        if set(accepted) != {
            repository for repository, decision in candidate_decisions.items() if decision == "accept"
        }:
            errors.append(f"{prefix}.accepted: does not match candidate decisions")
        if set(rejected) != {
            repository for repository, decision in candidate_decisions.items() if decision == "reject"
        }:
            errors.append(f"{prefix}.rejected: does not match candidate decisions")
        gaps_after = require_object(record.get("gaps_after"), f"{prefix}.gaps_after", errors)
        require_exact_keys(
            gaps_after,
            tuple(str(level) for level in range(1, 6)),
            f"{prefix}.gaps_after",
            errors,
        )
        for level in range(1, 6):
            value = gaps_after.get(str(level))
            if type(value) is not int or not 0 <= value <= 2:
                errors.append(
                    f"{prefix}.gaps_after.{level}: expected historical gap from 0 through 2"
                )
    summary = require_object(
        audit.get("summary"), "research/learner-centered-gap-research.json summary", errors
    )
    if summary.get("languages_completed") != len(records):
        errors.append("research/learner-centered-gap-research.json summary: language count differs")
    if summary.get("accepted_new_total") != accepted_total:
        errors.append("research/learner-centered-gap-research.json summary: accepted count differs")
    if summary.get("rejected_new_total") != rejected_total:
        errors.append("research/learner-centered-gap-research.json summary: rejected count differs")
    historical_summary = {"current_entry_total": 125, "remaining_gap_total": 75}
    for field, expected in historical_summary.items():
        if summary.get(field) != expected:
            errors.append(
                f"research/learner-centered-gap-research.json summary.{field}: expected historical value {expected}"
            )
    return errors


def validate_lower_level_expansion_audit(
    root: Path,
    languages: list[dict[str, Any]],
    canonical_entries: dict[tuple[str, str], dict[str, Any]],
) -> list[str]:
    """Reconcile the source-policy expansion audit with baseline and catalog data."""
    path = root / "research" / "lower-level-expansion-audit.json"
    if not path.exists():
        return []
    prefix = "research/lower-level-expansion-audit.json"
    try:
        audit = load_json(path)
        baseline = load_json(root / "research" / "lower-level-expansion.json")
        rejections = load_json(root / "research" / "rejections.json")
    except CatalogError as error:
        return [str(error)]

    errors: list[str] = []
    top_fields = (
        "schema_version",
        "audited_at",
        "baseline",
        "policy",
        "before",
        "after",
        "additions",
        "remaining_lower_level_gaps",
        "language_passes",
        "educational_exemplars",
        "serious_rejections_added_this_pass",
        "progression_checks",
        "source_class_leakage",
        "educational_quality_samples",
        "candidate_verification",
        "verification",
    )
    require_exact_keys(audit, top_fields, prefix, errors)
    if audit.get("schema_version") != 1:
        errors.append(f"{prefix}.schema_version: expected 1")
    audited_at = require_date(audit.get("audited_at"), f"{prefix}.audited_at", errors)

    baseline_ref = require_object(audit.get("baseline"), f"{prefix}.baseline", errors)
    require_exact_keys(baseline_ref, ("path", "commit"), f"{prefix}.baseline", errors)
    if baseline_ref.get("path") != "research/lower-level-expansion.json":
        errors.append(f"{prefix}.baseline.path: expected canonical baseline path")
    if baseline_ref.get("commit") != baseline.get("baseline_commit"):
        errors.append(f"{prefix}.baseline.commit: differs from baseline record")

    gate_names = (
        "complete_artifact",
        "clear_educational_purpose",
        "exemplary_source_quality",
        "verifiable_behavior",
        "useful_documentation",
        "stable_inspectable_revision",
        "public_source_and_license",
        "genuine_learning_value",
        "novice_accessibility_compliance",
        "no_level_gaming",
    )
    unresolved_phrase = "unresolved after production and educational-exemplar research"
    policy = require_object(audit.get("policy"), f"{prefix}.policy", errors)
    require_exact_keys(
        policy,
        (
            "target_capacity",
            "complete_grid",
            "unresolved_gap_phrase",
            "educational_gate",
        ),
        f"{prefix}.policy",
        errors,
    )
    expected_capacity = {str(level): capacity for level, capacity in LEVEL_CAPACITY.items()}
    if policy.get("target_capacity") != expected_capacity:
        errors.append(f"{prefix}.policy.target_capacity: differs from canonical capacity")
    if policy.get("complete_grid") != COMPLETE_CATALOG_SIZE:
        errors.append(f"{prefix}.policy.complete_grid: expected {COMPLETE_CATALOG_SIZE}")
    if policy.get("unresolved_gap_phrase") != unresolved_phrase:
        errors.append(f"{prefix}.policy.unresolved_gap_phrase: expected required phrase")
    if policy.get("educational_gate") != list(gate_names):
        errors.append(f"{prefix}.policy.educational_gate: expected all ten gates in order")

    baseline_catalog = require_object(
        baseline.get("catalog"), "research/lower-level-expansion.json.catalog", errors
    )
    baseline_levels = baseline_catalog.get("paths_by_level", {})
    before_expected = {
        "accepted_paths": baseline_catalog.get("accepted_paths"),
        "paths_by_level": baseline_levels,
    }
    current_levels = Counter(
        entry.get("learning_level", {}).get("level")
        for entry in canonical_entries.values()
    )
    after_expected = {
        "accepted_paths": len(canonical_entries),
        "paths_by_level": {
            str(level): current_levels[level] for level in range(1, 6)
        },
    }
    if audit.get("before") != before_expected:
        errors.append(f"{prefix}.before: does not match the preserved baseline")
    if audit.get("after") != after_expected:
        errors.append(f"{prefix}.after: does not match the canonical catalog")

    language_name_to_slug = {
        language["name"]: language["slug"] for language in languages
    }
    entries_by_language: dict[str, list[dict[str, Any]]] = {
        language["slug"]: [] for language in languages
    }
    for entry in canonical_entries.values():
        language_slug = language_name_to_slug.get(entry.get("primary_language"))
        if language_slug:
            entries_by_language[language_slug].append(entry)

    additions = require_object(audit.get("additions"), f"{prefix}.additions", errors)
    require_exact_keys(
        additions,
        ("production", "educational_exemplar", "paths"),
        f"{prefix}.additions",
        errors,
    )
    raw_addition_paths = additions.get("paths")
    if not isinstance(raw_addition_paths, list):
        errors.append(f"{prefix}.additions.paths: expected list")
        raw_addition_paths = []
    addition_keys: set[tuple[str, str]] = set()
    addition_repositories_by_language: dict[str, set[str]] = {
        language["slug"]: set() for language in languages
    }
    addition_slugs_by_language: dict[str, set[str]] = {
        language["slug"]: set() for language in languages
    }
    addition_source_counts: Counter[str] = Counter()
    for index, raw_addition in enumerate(raw_addition_paths):
        item_prefix = f"{prefix}.additions.paths[{index}]"
        addition = require_object(raw_addition, item_prefix, errors)
        require_exact_keys(
            addition,
            (
                "language_slug",
                "repository",
                "path_slug",
                "source_kind",
                "level",
                "pinned_commit",
            ),
            item_prefix,
            errors,
        )
        repository = require_text(addition.get("repository"), f"{item_prefix}.repository", errors)
        path_slug = require_text(addition.get("path_slug"), f"{item_prefix}.path_slug", errors)
        key = (repository.lower(), path_slug)
        if key in addition_keys:
            errors.append(f"{item_prefix}: duplicate added path")
        addition_keys.add(key)
        entry = canonical_entries.get(key)
        if entry is None:
            errors.append(f"{item_prefix}: added path is not in the canonical catalog")
            continue
        language_slug = language_name_to_slug.get(entry.get("primary_language"))
        if addition.get("language_slug") != language_slug:
            errors.append(f"{item_prefix}.language_slug: differs from canonical entry")
        if addition.get("source_kind") != entry.get("source_kind"):
            errors.append(f"{item_prefix}.source_kind: differs from canonical entry")
        if addition.get("level") != entry.get("learning_level", {}).get("level"):
            errors.append(f"{item_prefix}.level: differs from canonical entry")
        if addition.get("pinned_commit") != entry.get("inspection", {}).get("commit"):
            errors.append(f"{item_prefix}.pinned_commit: differs from canonical entry")
        if entry.get("learning_level", {}).get("level") not in (1, 2):
            errors.append(f"{item_prefix}: lower-level expansion addition must be Level 1 or 2")
        addition_source_counts[entry.get("source_kind")] += 1
        if language_slug:
            addition_repositories_by_language[language_slug].add(repository)
            addition_slugs_by_language[language_slug].add(path_slug)
    before_total = before_expected.get("accepted_paths")
    if type(before_total) is int and len(raw_addition_paths) != len(canonical_entries) - before_total:
        errors.append(f"{prefix}.additions.paths: count does not equal catalog growth")
    if additions.get("production") != addition_source_counts["production"]:
        errors.append(f"{prefix}.additions.production: does not match added paths")
    if additions.get("educational_exemplar") != addition_source_counts["educational-exemplar"]:
        errors.append(
            f"{prefix}.additions.educational_exemplar: does not match added paths"
        )

    baseline_lower_records = baseline_catalog.get("lower_levels_by_language")
    if not isinstance(baseline_lower_records, list):
        errors.append("research/lower-level-expansion.json: expected lower-level language records")
        baseline_lower_records = []
    baseline_lower_by_slug = {
        record.get("language_slug"): record
        for record in baseline_lower_records
        if isinstance(record, dict)
    }
    passes = audit.get("language_passes")
    if not isinstance(passes, list):
        errors.append(f"{prefix}.language_passes: expected list")
        passes = []
    pass_slugs: list[str] = []
    for index, raw_pass in enumerate(passes):
        item_prefix = f"{prefix}.language_passes[{index}]"
        record = require_object(raw_pass, item_prefix, errors)
        require_exact_keys(
            record,
            (
                "language_slug",
                "before",
                "after",
                "gaps_after",
                "discovery_channels",
                "prior_research_revisited",
                "educational_search",
                "candidates",
                "accepted_path_slugs",
                "gap_status",
            ),
            item_prefix,
            errors,
        )
        expected_language = languages[index] if index < len(languages) else None
        language_slug = record.get("language_slug")
        pass_slugs.append(language_slug)
        if expected_language and language_slug != expected_language["slug"]:
            errors.append(
                f"{item_prefix}.language_slug: expected {expected_language['slug']}"
            )
        baseline_record = baseline_lower_by_slug.get(language_slug, {})
        expected_before = {
            "1": baseline_record.get("level_1"),
            "2": baseline_record.get("level_2"),
        }
        current_lower = Counter(
            entry.get("learning_level", {}).get("level")
            for entry in entries_by_language.get(language_slug, [])
            if entry.get("learning_level", {}).get("level") in (1, 2)
        )
        expected_after = {"1": current_lower[1], "2": current_lower[2]}
        expected_gaps = {
            "1": LEVEL_CAPACITY[1] - current_lower[1],
            "2": LEVEL_CAPACITY[2] - current_lower[2],
        }
        if record.get("before") != expected_before:
            errors.append(f"{item_prefix}.before: differs from baseline")
        if record.get("after") != expected_after:
            errors.append(f"{item_prefix}.after: differs from canonical catalog")
        if record.get("gaps_after") != expected_gaps:
            errors.append(f"{item_prefix}.gaps_after: differs from target capacity")
        require_text_list(
            record.get("discovery_channels"),
            f"{item_prefix}.discovery_channels",
            errors,
            minimum_items=3,
            unique=True,
        )
        require_text_list(
            record.get("prior_research_revisited"),
            f"{item_prefix}.prior_research_revisited",
            errors,
            minimum_items=1,
            unique=True,
        )
        require_text(
            record.get("educational_search"),
            f"{item_prefix}.educational_search",
            errors,
            20,
        )
        candidates = record.get("candidates")
        if not isinstance(candidates, list) or len(candidates) < 2:
            errors.append(f"{item_prefix}.candidates: expected multiple candidates")
            candidates = []
        accepted_repositories: set[str] = set()
        rejected_count = 0
        for candidate_index, raw_candidate in enumerate(candidates):
            candidate_prefix = f"{item_prefix}.candidates[{candidate_index}]"
            candidate = require_object(raw_candidate, candidate_prefix, errors)
            require_exact_keys(
                candidate,
                ("repository", "decision", "evidence"),
                candidate_prefix,
                errors,
            )
            candidate_repository = require_text(
                candidate.get("repository"), f"{candidate_prefix}.repository", errors
            )
            decision = candidate.get("decision")
            if decision not in (
                "accepted",
                "rejected",
                "retained-lower",
                "retained-higher",
            ):
                errors.append(f"{candidate_prefix}.decision: invalid research decision")
            if decision == "accepted":
                accepted_repositories.add(candidate_repository)
            if decision == "rejected":
                rejected_count += 1
            require_text(candidate.get("evidence"), f"{candidate_prefix}.evidence", errors, 20)
        if rejected_count < 1:
            errors.append(f"{item_prefix}.candidates: expected at least one rejected candidate")
        if accepted_repositories != addition_repositories_by_language.get(language_slug, set()):
            errors.append(f"{item_prefix}.candidates: accepted repositories differ from additions")
        accepted_path_slugs = require_text_list(
            record.get("accepted_path_slugs"),
            f"{item_prefix}.accepted_path_slugs",
            errors,
            minimum_items=0,
            unique=True,
        )
        if set(accepted_path_slugs) != addition_slugs_by_language.get(language_slug, set()):
            errors.append(f"{item_prefix}.accepted_path_slugs: differs from additions")
        if sum(expected_gaps.values()) > 0:
            if record.get("gap_status") != unresolved_phrase:
                errors.append(f"{item_prefix}.gap_status: expected required unresolved phrase")
        elif record.get("gap_status") != "target filled":
            errors.append(f"{item_prefix}.gap_status: expected target filled")
    if pass_slugs != [language["slug"] for language in languages]:
        errors.append(f"{prefix}.language_passes: expected one ordered pass per language")

    expected_lower_gaps = {
        "1": sum(
            LEVEL_CAPACITY[1]
            - sum(
                entry.get("learning_level", {}).get("level") == 1
                for entry in entries_by_language[language["slug"]]
            )
            for language in languages
        ),
        "2": sum(
            LEVEL_CAPACITY[2]
            - sum(
                entry.get("learning_level", {}).get("level") == 2
                for entry in entries_by_language[language["slug"]]
            )
            for language in languages
        ),
    }
    expected_lower_gaps["total"] = expected_lower_gaps["1"] + expected_lower_gaps["2"]
    if audit.get("remaining_lower_level_gaps") != expected_lower_gaps:
        errors.append(
            f"{prefix}.remaining_lower_level_gaps: differs from canonical catalog"
        )

    educational_records = audit.get("educational_exemplars")
    if not isinstance(educational_records, list):
        errors.append(f"{prefix}.educational_exemplars: expected list")
        educational_records = []
    audited_educational_keys: set[tuple[str, str]] = set()
    for index, raw_record in enumerate(educational_records):
        item_prefix = f"{prefix}.educational_exemplars[{index}]"
        record = require_object(raw_record, item_prefix, errors)
        require_exact_keys(
            record,
            (
                "language_slug",
                "repository",
                "path_slug",
                "pinned_commit",
                "level",
                "ordinary_scores",
                "novice_accessibility_floor",
                "inspected_files",
                "qualification",
            ),
            item_prefix,
            errors,
        )
        repository = require_text(record.get("repository"), f"{item_prefix}.repository", errors)
        path_slug = require_text(record.get("path_slug"), f"{item_prefix}.path_slug", errors)
        key = (repository.lower(), path_slug)
        audited_educational_keys.add(key)
        entry = canonical_entries.get(key)
        if entry is None or entry.get("source_kind") != "educational-exemplar":
            errors.append(f"{item_prefix}: does not resolve to an educational exemplar")
            continue
        language_slug = language_name_to_slug.get(entry.get("primary_language"))
        if record.get("language_slug") != language_slug:
            errors.append(f"{item_prefix}.language_slug: differs from catalog")
        if record.get("pinned_commit") != entry.get("inspection", {}).get("commit"):
            errors.append(f"{item_prefix}.pinned_commit: differs from catalog")
        level = entry.get("learning_level", {}).get("level")
        if record.get("level") != level:
            errors.append(f"{item_prefix}.level: differs from catalog")
        expected_scores = {
            field: entry.get("learning_level", {}).get(field, {}).get("score")
            for field in DIMENSION_FIELDS
        }
        if record.get("ordinary_scores") != expected_scores:
            errors.append(f"{item_prefix}.ordinary_scores: differs from catalog")
        floor = entry.get("novice_accessibility", {}).get("floor")
        if record.get("novice_accessibility_floor") != floor:
            errors.append(f"{item_prefix}.novice_accessibility_floor: differs from catalog")
        inspected_files = require_text_list(
            record.get("inspected_files"),
            f"{item_prefix}.inspected_files",
            errors,
            minimum_items=2,
            unique=True,
        )
        for file_index, file_path in enumerate(inspected_files):
            if not is_safe_relative_path(file_path):
                errors.append(
                    f"{item_prefix}.inspected_files[{file_index}]: expected canonical safe non-dotenv relative path"
                )
        if inspected_files != entry.get("inspection", {}).get("files"):
            errors.append(f"{item_prefix}.inspected_files: differs from catalog inspection")
        qualification = require_object(
            record.get("qualification"), f"{item_prefix}.qualification", errors
        )
        require_exact_keys(qualification, gate_names, f"{item_prefix}.qualification", errors)
        for gate_name in gate_names:
            gate_prefix = f"{item_prefix}.qualification.{gate_name}"
            gate = require_object(qualification.get(gate_name), gate_prefix, errors)
            require_exact_keys(gate, ("pass", "evidence"), gate_prefix, errors)
            if gate.get("pass") is not True:
                errors.append(f"{gate_prefix}.pass: every educational gate must pass")
            require_text(gate.get("evidence"), f"{gate_prefix}.evidence", errors, 20)
    canonical_educational_keys = {
        key
        for key, entry in canonical_entries.items()
        if entry.get("source_kind") == "educational-exemplar"
    }
    if audited_educational_keys != canonical_educational_keys:
        errors.append(
            f"{prefix}.educational_exemplars: must audit every canonical educational exemplar"
        )

    rejection_records = rejections.get("rejections")
    if not isinstance(rejection_records, list):
        errors.append("research/rejections.json.rejections: expected list")
        rejection_records = []
    expected_rejection_keys = {
        (
            language_name_to_slug.get(record.get("language")),
            record.get("repository"),
            record.get("failed_requirement"),
        )
        for record in rejection_records
        if isinstance(record, dict) and record.get("inspected_at") == audited_at
    }
    audited_rejections = audit.get("serious_rejections_added_this_pass")
    if not isinstance(audited_rejections, list):
        errors.append(f"{prefix}.serious_rejections_added_this_pass: expected list")
        audited_rejections = []
    audited_rejection_keys: set[tuple[Any, Any, Any]] = set()
    for index, raw_rejection in enumerate(audited_rejections):
        item_prefix = f"{prefix}.serious_rejections_added_this_pass[{index}]"
        rejection = require_object(raw_rejection, item_prefix, errors)
        require_exact_keys(
            rejection,
            (
                "language_slug",
                "repository",
                "failed_requirement",
                "decision_evidence",
                "full_record",
            ),
            item_prefix,
            errors,
        )
        key = (
            rejection.get("language_slug"),
            rejection.get("repository"),
            rejection.get("failed_requirement"),
        )
        if key in audited_rejection_keys:
            errors.append(f"{item_prefix}: duplicate serious rejection")
        audited_rejection_keys.add(key)
        require_text(
            rejection.get("decision_evidence"),
            f"{item_prefix}.decision_evidence",
            errors,
            20,
        )
        if rejection.get("full_record") != "research/rejections.json":
            errors.append(f"{item_prefix}.full_record: expected canonical rejection record")
    if audited_rejection_keys != expected_rejection_keys:
        errors.append(
            f"{prefix}.serious_rejections_added_this_pass: differs from dated rejection records"
        )

    expected_progression_slugs = {
        language["slug"]
        for language in languages
        if any(
            entry.get("learning_level", {}).get("level") in (1, 2)
            for entry in entries_by_language[language["slug"]]
        )
    }
    progression = audit.get("progression_checks")
    if not isinstance(progression, list):
        errors.append(f"{prefix}.progression_checks: expected list")
        progression = []
    progression_slugs: set[str] = set()
    for index, raw_check in enumerate(progression):
        item_prefix = f"{prefix}.progression_checks[{index}]"
        check = require_object(raw_check, item_prefix, errors)
        require_exact_keys(
            check,
            (
                "language_slug",
                "level_1_order",
                "level_2_order",
                "level_3_order",
                "ordering_rationale",
                "level_2_to_3",
                "result",
            ),
            item_prefix,
            errors,
        )
        language_slug = check.get("language_slug")
        if language_slug in progression_slugs:
            errors.append(f"{item_prefix}.language_slug: duplicate progression check")
        progression_slugs.add(language_slug)
        for level, field in ((1, "level_1_order"), (2, "level_2_order"), (3, "level_3_order")):
            published_order = require_text_list(
                check.get(field),
                f"{item_prefix}.{field}",
                errors,
                minimum_items=0,
                unique=True,
            )
            expected_order = [
                entry.get("slug")
                for entry in entries_by_language.get(language_slug, [])
                if entry.get("learning_level", {}).get("level") == level
            ]
            if published_order != expected_order:
                errors.append(f"{item_prefix}.{field}: differs from published order")
        require_text(
            check.get("ordering_rationale"),
            f"{item_prefix}.ordering_rationale",
            errors,
            20,
        )
        require_text(check.get("level_2_to_3"), f"{item_prefix}.level_2_to_3", errors, 20)
        if check.get("result") not in ("pass", "pass-with-explicit-gap"):
            errors.append(f"{item_prefix}.result: invalid progression result")
    if progression_slugs != expected_progression_slugs:
        errors.append(f"{prefix}.progression_checks: missing lower-level language")

    higher_entries = [
        entry
        for entry in canonical_entries.values()
        if entry.get("learning_level", {}).get("level") in (3, 4, 5)
    ]
    educational_entries = [
        entry
        for entry in canonical_entries.values()
        if entry.get("source_kind") == "educational-exemplar"
    ]
    leakage = require_object(
        audit.get("source_class_leakage"), f"{prefix}.source_class_leakage", errors
    )
    require_exact_keys(
        leakage,
        (
            "level_3_to_5_paths_checked",
            "all_level_3_to_5_paths_are_production",
            "educational_exemplars_checked",
            "educational_exemplars_above_level_2",
            "baseline_paths_preserved",
            "baseline_paths_reclassified_as_educational",
            "visible_source_disclosure",
            "evidence",
        ),
        f"{prefix}.source_class_leakage",
        errors,
    )
    expected_leakage = {
        "level_3_to_5_paths_checked": len(higher_entries),
        "all_level_3_to_5_paths_are_production": all(
            entry.get("source_kind") == "production" for entry in higher_entries
        ),
        "educational_exemplars_checked": len(educational_entries),
        "educational_exemplars_above_level_2": sum(
            entry.get("learning_level", {}).get("level", 0) > 2
            for entry in educational_entries
        ),
        "baseline_paths_preserved": before_total,
        "baseline_paths_reclassified_as_educational": 0,
        "visible_source_disclosure": "pass",
    }
    for field, expected in expected_leakage.items():
        if leakage.get(field) != expected:
            errors.append(f"{prefix}.source_class_leakage.{field}: expected {expected}")
    require_text(
        leakage.get("evidence"), f"{prefix}.source_class_leakage.evidence", errors, 20
    )

    quality_samples = audit.get("educational_quality_samples")
    if not isinstance(quality_samples, list):
        errors.append(f"{prefix}.educational_quality_samples: expected list")
        quality_samples = []
    sampled_repositories: set[str] = set()
    for index, raw_sample in enumerate(quality_samples):
        item_prefix = f"{prefix}.educational_quality_samples[{index}]"
        sample = require_object(raw_sample, item_prefix, errors)
        require_exact_keys(sample, ("repository", "result", "evidence"), item_prefix, errors)
        repository = require_text(sample.get("repository"), f"{item_prefix}.repository", errors)
        sampled_repositories.add(repository.lower())
        if sample.get("result") != "pass":
            errors.append(f"{item_prefix}.result: expected pass")
        require_text(sample.get("evidence"), f"{item_prefix}.evidence", errors, 20)
    expected_sampled_repositories = {
        entry.get("repository", "").lower() for entry in educational_entries
    }
    if sampled_repositories != expected_sampled_repositories:
        errors.append(
            f"{prefix}.educational_quality_samples: expected every educational exemplar"
        )

    candidate_verification = audit.get("candidate_verification")
    if not isinstance(candidate_verification, list):
        errors.append(f"{prefix}.candidate_verification: expected list")
        candidate_verification = []
    verified_repositories: set[str] = set()
    for index, raw_check in enumerate(candidate_verification):
        item_prefix = f"{prefix}.candidate_verification[{index}]"
        check = require_object(raw_check, item_prefix, errors)
        require_exact_keys(check, ("repository", "method", "result", "evidence"), item_prefix, errors)
        repository = require_text(check.get("repository"), f"{item_prefix}.repository", errors)
        verified_repositories.add(repository.lower())
        require_text(check.get("method"), f"{item_prefix}.method", errors)
        if check.get("result") not in ("pass", "pass-with-runtime-unavailable"):
            errors.append(f"{item_prefix}.result: invalid verification result")
        require_text(check.get("evidence"), f"{item_prefix}.evidence", errors, 20)
    expected_verified_repositories = {key[0] for key in addition_keys}
    if verified_repositories != expected_verified_repositories:
        errors.append(f"{prefix}.candidate_verification: expected every added repository")

    verification = require_object(
        audit.get("verification"), f"{prefix}.verification", errors
    )
    require_exact_keys(
        verification,
        (
            "generated_pages",
            "unit_tests",
            "catalog_validation",
            "generated_output_check",
            "complete_validation",
        ),
        f"{prefix}.verification",
        errors,
    )
    for field in (
        "generated_pages",
        "unit_tests",
        "catalog_validation",
        "generated_output_check",
    ):
        check = require_object(
            verification.get(field), f"{prefix}.verification.{field}", errors
        )
        required = ("command", "result", "tests_run") if field == "unit_tests" else ("command", "result")
        require_exact_keys(check, required, f"{prefix}.verification.{field}", errors)
        require_text(check.get("command"), f"{prefix}.verification.{field}.command", errors)
        if check.get("result") not in ("pending", "pass"):
            errors.append(f"{prefix}.verification.{field}.result: expected pending or pass")
        if field == "unit_tests":
            tests_run = check.get("tests_run")
            if type(tests_run) is not int or tests_run < 0:
                errors.append(f"{prefix}.verification.unit_tests.tests_run: expected non-negative integer")
    complete_check = require_object(
        verification.get("complete_validation"),
        f"{prefix}.verification.complete_validation",
        errors,
    )
    require_exact_keys(
        complete_check,
        ("run", "reason"),
        f"{prefix}.verification.complete_validation",
        errors,
    )
    if complete_check.get("run") is not False:
        errors.append(
            f"{prefix}.verification.complete_validation.run: incomplete catalog must not claim a complete run"
        )
    require_text(
        complete_check.get("reason"),
        f"{prefix}.verification.complete_validation.reason",
        errors,
        20,
    )
    return errors


def validate_catalog(root: Path = ROOT, complete: bool = False) -> list[str]:
    catalog_dir = root / "catalog"
    try:
        language_data = load_json(catalog_dir / "languages.json")
    except CatalogError as error:
        return [str(error)]
    languages, errors = validate_languages(language_data)
    errors.extend(validate_schema(root))
    seen_paths: set[tuple[str, str]] = set()
    repository_counts: Counter[str] = Counter()
    seen_repository_buckets: set[tuple[str, int, str]] = set()
    canonical_entries: dict[tuple[str, str], dict[str, Any]] = {}
    total = 0
    for language in languages:
        path = catalog_dir / f"{language['slug']}.json"
        try:
            data = load_json(path)
        except CatalogError as error:
            errors.append(str(error))
            continue
        expected_top_fields = ("schema_version", "language_slug", "repositories")
        require_exact_keys(data, expected_top_fields, f"catalog/{language['slug']}.json", errors)
        if data.get("schema_version") != CATALOG_SCHEMA_VERSION:
            errors.append(
                f"catalog/{language['slug']}.json schema_version: expected {CATALOG_SCHEMA_VERSION}"
            )
        if data.get("language_slug") != language["slug"]:
            errors.append(
                f"catalog/{language['slug']}.json language_slug: expected {language['slug']}"
            )
        repositories = data.get("repositories")
        if not isinstance(repositories, list):
            errors.append(f"catalog/{language['slug']}.json repositories: expected list")
            continue
        expected_order = sorted(
            repositories,
            key=lambda entry: entry.get("learning_level", {}).get("level", 99)
            if isinstance(entry, dict)
            else 99,
        )
        if repositories != expected_order:
            errors.append(
                f"catalog/{language['slug']}.json repositories: expected nondecreasing Level order"
            )
        total += len(repositories)
        seen_slugs: set[str] = set()
        for index, entry in enumerate(repositories):
            errors.extend(
                validate_repository(
                    entry,
                    language,
                    index,
                    seen_paths,
                    repository_counts,
                    seen_repository_buckets,
                    seen_slugs,
                )
            )
            if (
                isinstance(entry, dict)
                and isinstance(entry.get("repository"), str)
                and isinstance(entry.get("path_slug"), str)
            ):
                canonical_entries[
                    (entry["repository"].lower(), entry["path_slug"])
                ] = entry
        levels = Counter(
            entry.get("learning_level", {}).get("level")
            for entry in repositories
            if isinstance(entry, dict) and isinstance(entry.get("learning_level"), dict)
        )
        for level in range(1, 6):
            count = levels[level]
            capacity = LEVEL_CAPACITY[level]
            if count > capacity:
                errors.append(
                    f"catalog/{language['slug']}.json: Level {level} has {count} entries; maximum is {capacity}"
                )
            if complete and count != capacity:
                errors.append(
                    f"catalog/{language['slug']}.json: Level {level} requires {capacity} entries; found {count}"
                )
    novice_errors, novice_state = validate_novice_accessibility_audit(
        root, languages, canonical_entries
    )
    errors.extend(novice_errors)
    errors.extend(
        validate_rebuild_reconciliation(root, canonical_entries, novice_state)
    )
    errors.extend(validate_gap_research(root, languages, canonical_entries, novice_state))
    errors.extend(
        validate_lower_level_expansion_audit(root, languages, canonical_entries)
    )
    if complete and total != COMPLETE_CATALOG_SIZE:
        errors.append(
            f"complete catalog requires {COMPLETE_CATALOG_SIZE} learning paths; found {total}"
        )
    return errors


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def path_url(entry: dict[str, Any], path: str) -> str:
    return (
        f"{entry['url']}/blob/{entry['inspection']['commit']}/"
        + quote(path, safe="/")
    )


def render_index(languages: list[dict[str, Any]], catalogs: dict[str, dict[str, Any]]) -> str:
    total = sum(len(catalogs[language["slug"]]["repositories"]) for language in languages)
    lines = [
        "# Languages",
        "",
        "Choose a language, then browse from Level 1 — First real code through Level 5 — Expert.",
        "",
        "**Production software** is built primarily for real users or systems. **Educational exemplars** are complete software artifacts intentionally chosen for teaching clarity and are allowed only at Levels 1 and 2.",
        "",
        "Exempla deliberately allows high-quality educational software at Levels 1 and 2 because production code often assumes professional concepts before a novice has learned them. Difficulty and novice-accessibility standards do not change, every entry discloses its source type, and Level 3 begins the production-only part of the ladder.",
        "",
        "If you can write small programs in the language, Level 1 is designed as your first comfortable source-reading step. An empty Level 1 means Exempla has not yet found a path gentle enough to publish there; it is not advice to skip straight to Level 2.",
        "",
        f"The catalog currently contains **{total} qualified learning paths across {len(languages)} languages**. Empty cells are honest research gaps.",
        "",
        "| Language | Entries | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for language in languages:
        repositories = catalogs[language["slug"]]["repositories"]
        counts = Counter(entry["learning_level"]["level"] for entry in repositories)
        lines.append(
            f"| [{markdown_escape(language['name'])}]({language['slug']}/README.md) | "
            + f"{len(repositories)} | "
            + " | ".join(str(counts[level]) for level in range(1, 6))
            + " |"
        )
    lines.extend(
        [
            "",
            "Read [how learning levels work](../docs/learning-levels.md), the "
            "[coding-relevance and quality gates](../docs/qualification.md), or the "
            "[language selection rationale](../docs/language-selection.md).",
            "",
            "_Generated by `python3 scripts/catalog.py generate`; do not edit by hand._",
            "",
        ]
    )
    return "\n".join(lines)


def render_repository(entry: dict[str, Any]) -> list[str]:
    level = entry["learning_level"]
    language = level["language_technique"]
    behavior = level["behavioral_reasoning"]
    design = level["design_span"]
    constraints = level["constraint_burden"]
    learning_path = entry["learning_path"]
    start = learning_path["start_here"]
    inspection = entry["inspection"]
    context = entry["coding_relevance"]["domain_context"]
    lines = [
        f"### [{entry['repository']}]({entry['url']})",
        "",
        f"**Language {language['score']} / Behavior {behavior['score']} / Design {design['score']} / Constraints {constraints['score']} → Level {level['level']}**",
        "",
        f"**Source:** {SOURCE_KIND_LABELS[entry['source_kind']]}",
        "",
        entry["description"],
        "",
        f"**Why study it:** {entry['why_study']}",
        "",
    ]
    if entry["source_kind"] == "educational-exemplar":
        lines.extend(
            [
                "Levels 1–2 may use intentionally instructive software when it provides a gentler path into reading good source code.",
                "",
            ]
        )
    if context:
        lines.extend(["**Short context:**", ""])
        lines.extend(f"- {item}" for item in context)
        lines.append("")
    lines.extend(["**Prerequisites:**", ""])
    lines.extend(f"- {item}" for item in entry["prerequisites"])
    lines.extend(["", "**Concepts this path develops:**", ""])
    lines.extend(f"- {item}" for item in entry["concepts_developed"])
    lines.extend(["", "**What you can learn:**", ""])
    lines.extend(f"- {item}" for item in entry["learn"])
    lines.extend(
        [
            "",
            "**Learning path:**",
            "",
            f"- **Goal:** {learning_path['goal']}",
            f"- **Start here:** [`{start['path']}`]({path_url(entry, start['path'])}) — {start['reason']}",
            "- **Then read:**",
        ]
    )
    for file_path in learning_path["supporting_files"]:
        lines.append(f"  - [`{file_path}`]({path_url(entry, file_path)})")
    lines.extend(
        [
            f"- **Trace:** {learning_path['trace']}",
            "",
            "**Why this level:**",
            "",
            f"- **Language technique {language['score']}:** {language['reason']}",
            f"- **Behavioral reasoning {behavior['score']}:** {behavior['reason']}",
            f"- **Design span {design['score']}:** {design['reason']}",
            f"- **Constraint burden {constraints['score']}:** {constraints['reason']}",
        ]
    )
    accessibility = entry.get("novice_accessibility")
    if accessibility:
        central = "; ".join(accessibility["central_concepts"]) or "None recorded."
        incidental = "; ".join(accessibility["incidental_concepts"]) or "None recorded."
        lines.extend(
            [
                f"- **Novice accessibility floor {accessibility['floor']}:** {accessibility['reason']}",
                f"  - **Central concepts:** {central}",
                f"  - **Incidental concepts:** {incidental}",
            ]
        )
    lines.extend([f"- **Placement:** {level['placement']}", ""])
    evidence_links = ", ".join(
        f"[evidence {index}]({url})"
        for index, url in enumerate(entry["license"]["urls"], start=1)
    )
    lines.extend(
        [
            f"**License:** {entry['license']['spdx']} ({evidence_links})",
            "",
            "<details>",
            "<summary>Quality and review evidence</summary>",
            "",
            f"**Purpose evidence:** {entry['purpose_evidence']}",
            "",
            f"**Language evidence:** {entry['language_evidence']}",
            "",
            "**Coding relevance:**",
            "",
            entry["coding_relevance"]["reason"],
            "",
        ]
    )
    if context:
        lines.extend(["The learner-facing short context appears above.", ""])
    else:
        lines.extend(["No specialist domain context is required.", ""])
    lines.extend(["**Eight-part quality gate:**", ""])
    labels = {
        "source_quality": "Source quality",
        "architecture": "Architecture",
        "naming_and_idiom": "Naming and idiom",
        "tests": "Tests",
        "documentation": "Documentation",
        "traceability": "Traceability",
        "maintainability": "Maintainability",
        "educational_value": "Educational value",
    }
    lines.extend(
        f"- **{labels[field]}:** {entry['quality'][field]}" for field in QUALITY_FIELDS
    )
    reviewed_files = ", ".join(f"`{path}`" for path in inspection["files"])
    archive_note = " Archived repository." if entry["github"]["archived"] else ""
    lines.extend(
        [
            "",
            f"**Inspection record:** commit `{inspection['commit']}`, inspected {inspection['inspected_at']}. Review passes: {'; '.join(inspection['reviewers'])}. Files inspected: {reviewed_files}. GitHub Linguist label: {entry['github']['primary_language']}.{archive_note}",
            "",
            "</details>",
            "",
        ]
    )
    return lines


def render_language(language: dict[str, Any], data: dict[str, Any]) -> str:
    if data.get("schema_version") != CATALOG_SCHEMA_VERSION:
        raise CatalogError(
            f"cannot generate from a schema-version-{data.get('schema_version')} language catalog"
        )
    repositories = data["repositories"]
    lines = [
        f"# {language['name']}",
        "",
        f"{len(repositories)} qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).",
        "",
        "**Source legend:** Production software is built primarily for real users or systems. Educational exemplars are complete teaching-oriented software and may appear only at Levels 1 and 2.",
        "",
        "[← All languages](../README.md)",
        "",
    ]
    for level in range(1, 6):
        lines.extend([f"## Level {level} — {LEVEL_LABELS[level]}", ""])
        entries = [entry for entry in repositories if entry["learning_level"]["level"] == level]
        if not entries:
            empty_message = (
                "No qualified learning path has been published at this level. "
                "An empty Level 1 means Exempla has not yet found a path gentle "
                "enough to publish here; learners are not being told to jump to "
                "Level 2."
                if level == 1
                else "No qualified learning path has been published at this level. Standards are not lowered to fill a slot."
            )
            lines.extend([empty_message, ""])
        else:
            for entry in entries:
                lines.extend(render_repository(entry))
    lines.extend(
        [
            f"_Generated from `catalog/{language['slug']}.json`; do not edit by hand._",
            "",
        ]
    )
    return "\n".join(lines)


def generated_files(root: Path = ROOT) -> dict[Path, str]:
    language_data = load_json(root / "catalog" / "languages.json")
    languages, errors = validate_languages(language_data)
    if errors:
        raise CatalogError("cannot generate from invalid languages.json:\n" + "\n".join(errors))
    catalogs = {
        language["slug"]: load_json(root / "catalog" / f"{language['slug']}.json")
        for language in languages
    }
    if any(
        data.get("schema_version") != CATALOG_SCHEMA_VERSION
        for data in catalogs.values()
    ):
        raise CatalogError(
            f"cannot generate until every language catalog uses schema version {CATALOG_SCHEMA_VERSION}"
        )
    output = {root / "languages" / "README.md": render_index(languages, catalogs)}
    for language in languages:
        output[root / "languages" / language["slug"] / "README.md"] = render_language(
            language, catalogs[language["slug"]]
        )
    return output


def write_generated(root: Path = ROOT) -> None:
    for path, content in generated_files(root).items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def check_generated(root: Path = ROOT) -> list[str]:
    try:
        expected = generated_files(root)
    except CatalogError as error:
        return [str(error)]
    errors: list[str] = []
    for path, content in expected.items():
        if not path.exists():
            errors.append(f"missing generated file: {path.relative_to(root)}")
        elif path.read_text(encoding="utf-8") != content:
            errors.append(f"stale generated file: {path.relative_to(root)}")
    return errors


def print_errors(errors: list[str]) -> None:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate_parser = subparsers.add_parser("validate", help="validate canonical catalog data")
    validate_parser.add_argument(
        "--complete",
        action="store_true",
        help="require the complete 3/3/2/2/2 grid for every language",
    )
    subparsers.add_parser("generate", help="regenerate learner-facing Markdown")
    check_parser = subparsers.add_parser(
        "check-generated", help="fail when generated Markdown is missing or stale"
    )
    check_parser.add_argument(
        "--complete", action="store_true", help="also require the complete 240-entry corpus"
    )
    args = parser.parse_args(argv)

    if args.command == "validate":
        errors = validate_catalog(complete=args.complete)
        if errors:
            print_errors(errors)
            return 1
        print(
            "Catalog data is valid."
            + (
                f" Complete corpus: {COMPLETE_CATALOG_SIZE} entries."
                if args.complete
                else ""
            )
        )
        return 0
    if args.command == "generate":
        errors = validate_catalog()
        if errors:
            print_errors(errors)
            return 1
        write_generated()
        print("Generated learner-facing Markdown.")
        return 0
    errors = validate_catalog(complete=args.complete)
    errors.extend(check_generated())
    if errors:
        print_errors(errors)
        return 1
    print(
        "Generated Markdown is current."
        + (
            f" Complete corpus: {COMPLETE_CATALOG_SIZE} entries."
            if args.complete
            else ""
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

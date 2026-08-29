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
REPOSITORY_FIELDS = (
    "slug",
    "repository",
    "url",
    "primary_language",
    "language_evidence",
    "description",
    "real_world_evidence",
    "why_study",
    "learn",
    "prerequisites",
    "coding_relevance",
    "learning_path",
    "learning_level",
    "quality",
    "inspection",
    "license",
    "github",
)


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
    """Calculate the public level from the four path-centered scores."""
    scores = (language, behavior, design, constraints)
    if any(type(score) is not int or not 1 <= score <= 5 for score in scores):
        raise ValueError("all learning-level scores must be integers from 1 through 5")
    level = (sum(scores) + 2) // 4
    if 5 in scores:
        level = max(level, 4)
    if level == 5 and sum(score == 5 for score in scores) < 2:
        level = 4
    return level


def require_object(value: Any, path: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append(f"{path}: expected object")
        return {}
    return value


def require_exact_keys(
    value: dict[str, Any], required: tuple[str, ...], path: str, errors: list[str]
) -> None:
    missing = [key for key in required if key not in value]
    if missing:
        errors.append(f"{path}: missing fields {', '.join(missing)}")
    unexpected = sorted(set(value) - set(required))
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
    seen_repositories: set[str],
    seen_slugs: set[str],
) -> list[str]:
    """Validate one accepted schema-version-2 record."""
    errors: list[str] = []
    prefix = f"catalog/{language['slug']}.json repositories[{index}]"
    item = require_object(entry, prefix, errors)
    require_exact_keys(item, REPOSITORY_FIELDS, prefix, errors)

    slug = require_text(item.get("slug"), f"{prefix}.slug", errors)
    if slug and not SLUG_RE.fullmatch(slug):
        errors.append(f"{prefix}.slug: use lowercase letters, digits, and single hyphens")
    if slug in seen_slugs:
        errors.append(f"{prefix}.slug: duplicate within language: {slug}")
    if slug:
        seen_slugs.add(slug)

    repository = require_text(item.get("repository"), f"{prefix}.repository", errors)
    if repository and not REPOSITORY_RE.fullmatch(repository):
        errors.append(f"{prefix}.repository: expected owner/name")
    repository_key = repository.lower()
    if repository_key in seen_repositories:
        errors.append(f"{prefix}.repository: duplicate across catalog: {repository}")
    if repository:
        seen_repositories.add(repository_key)

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
    for field in ("description", "real_world_evidence", "why_study"):
        require_text(item.get(field), f"{prefix}.{field}", errors, 20)
    require_text_list(item.get("learn"), f"{prefix}.learn", errors)
    require_text_list(item.get("prerequisites"), f"{prefix}.prerequisites", errors)

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
    if level is not None and None not in ordered_scores:
        expected_level = calculate_learning_level(*ordered_scores)  # type: ignore[arg-type]
        if level != expected_level:
            profile = "/".join(str(score) for score in ordered_scores)
            errors.append(
                f"{prefix}.learning_level.level: scores {profile} require Level {expected_level}, not {level}"
            )

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
    if schema.get("properties", {}).get("schema_version", {}).get("const") != 2:
        errors.append("catalog/schema.json: schema_version must be the constant 2")
    repository = schema.get("$defs", {}).get("repository", {})
    if tuple(repository.get("required", ())) != REPOSITORY_FIELDS:
        errors.append("catalog/schema.json: repository required fields differ from the validator")
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


def validate_rebuild_reconciliation(
    root: Path, canonical_entries: dict[str, dict[str, Any]]
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
    decision_keys = [
        item.get("repository", "").lower() for item in decisions if isinstance(item, dict)
    ]
    if len(decision_keys) != 200 or len(set(decision_keys)) != 200:
        errors.append("research/learner-centered-rebuild.json: decisions must be unique")
    rejection_counts = Counter(
        item.get("repository", "").lower()
        for item in rejection_records
        if isinstance(item, dict)
    )
    for decision in decisions:
        if not isinstance(decision, dict):
            errors.append("research/learner-centered-rebuild.json: decision must be an object")
            continue
        repository = decision.get("repository", "")
        key = repository.lower()
        outcome = decision.get("decision")
        if outcome == "retain":
            entry = canonical_entries.get(key)
            if entry is None:
                errors.append(f"research reconciliation: retained repository missing: {repository}")
            elif entry.get("inspection", {}).get("commit") != decision.get("pinned_commit"):
                errors.append(f"research reconciliation: retained pin changed: {repository}")
        elif outcome == "remove":
            if key in canonical_entries:
                errors.append(f"research reconciliation: removed repository is still accepted: {repository}")
            if rejection_counts[key] != 1:
                errors.append(
                    f"research reconciliation: removal needs exactly one rejection record: {repository}"
                )
        else:
            errors.append(f"research reconciliation: invalid decision for {repository}")
    return errors


def validate_catalog(root: Path = ROOT, complete: bool = False) -> list[str]:
    catalog_dir = root / "catalog"
    try:
        language_data = load_json(catalog_dir / "languages.json")
    except CatalogError as error:
        return [str(error)]
    languages, errors = validate_languages(language_data)
    errors.extend(validate_schema(root))
    seen_repositories: set[str] = set()
    canonical_entries: dict[str, dict[str, Any]] = {}
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
        if data.get("schema_version") != 2:
            errors.append(f"catalog/{language['slug']}.json schema_version: expected 2")
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
            key=lambda entry: (
                entry.get("learning_level", {}).get("level", 99)
                if isinstance(entry, dict)
                else 99,
                entry.get("repository", "").lower() if isinstance(entry, dict) else "",
            ),
        )
        if repositories != expected_order:
            errors.append(
                f"catalog/{language['slug']}.json repositories: expected level/repository order"
            )
        total += len(repositories)
        seen_slugs: set[str] = set()
        for index, entry in enumerate(repositories):
            errors.extend(
                validate_repository(entry, language, index, seen_repositories, seen_slugs)
            )
            if isinstance(entry, dict) and isinstance(entry.get("repository"), str):
                canonical_entries[entry["repository"].lower()] = entry
        levels = Counter(
            entry.get("learning_level", {}).get("level")
            for entry in repositories
            if isinstance(entry, dict) and isinstance(entry.get("learning_level"), dict)
        )
        for level in range(1, 6):
            count = levels[level]
            if count > 2:
                errors.append(
                    f"catalog/{language['slug']}.json: Level {level} has {count} entries; maximum is 2"
                )
            if complete and count != 2:
                errors.append(
                    f"catalog/{language['slug']}.json: Level {level} requires 2 entries; found {count}"
                )
    errors.extend(validate_rebuild_reconciliation(root, canonical_entries))
    if complete and total != 200:
        errors.append(f"complete catalog requires 200 repositories; found {total}")
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
        "Choose a language, then browse from Level 1 (most approachable) through Level 5 (most demanding).",
        "",
        f"The catalog currently contains **{total} qualified repositories across {len(languages)} languages**. Empty cells are honest research gaps.",
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
    lines = [
        f"### [{entry['repository']}]({entry['url']})",
        "",
        f"**Language {language['score']} / Behavior {behavior['score']} / Design {design['score']} / Constraints {constraints['score']} → Level {level['level']}**",
        "",
        entry["description"],
        "",
        f"**Real-world evidence:** {entry['real_world_evidence']}",
        "",
        f"**Language evidence:** {entry['language_evidence']}",
        "",
        f"**Why study it:** {entry['why_study']}",
        "",
        "**What you can learn:**",
        "",
    ]
    lines.extend(f"- {item}" for item in entry["learn"])
    lines.extend(["", "**Prerequisites:**", ""])
    lines.extend(f"- {item}" for item in entry["prerequisites"])
    lines.extend(["", "**Coding relevance:**", "", entry["coding_relevance"]["reason"], ""])
    context = entry["coding_relevance"]["domain_context"]
    if context:
        lines.extend(["Required domain context:", ""])
        lines.extend(f"- {item}" for item in context)
        lines.append("")
    else:
        lines.extend(["No specialist domain context is required.", ""])
    lines.extend(
        [
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
            f"- **Placement:** {level['placement']}",
            "",
            "**Quality-gate evidence:**",
            "",
        ]
    )
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
            f"**Inspection record:** commit `{inspection['commit']}`, reviewed {inspection['inspected_at']} by {', '.join(inspection['reviewers'])}. Files sampled: {reviewed_files}. GitHub Linguist label: {entry['github']['primary_language']}.{archive_note}",
            "",
        ]
    )
    evidence_links = ", ".join(
        f"[evidence {index}]({url})"
        for index, url in enumerate(entry["license"]["urls"], start=1)
    )
    lines.extend(
        [
            f"**License:** {entry['license']['spdx']} ({evidence_links})",
            "",
        ]
    )
    return lines


def render_language(language: dict[str, Any], data: dict[str, Any]) -> str:
    if data.get("schema_version") != 2:
        raise CatalogError("cannot generate from a schema-version-1 language catalog")
    repositories = sorted(
        data["repositories"],
        key=lambda entry: (entry["learning_level"]["level"], entry["repository"].lower()),
    )
    lines = [
        f"# {language['name']}",
        "",
        f"{len(repositories)} qualified repositories. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).",
        "",
        "[← All languages](../README.md)",
        "",
    ]
    for level in range(1, 6):
        lines.extend([f"## Level {level}", ""])
        entries = [entry for entry in repositories if entry["learning_level"]["level"] == level]
        if not entries:
            lines.extend(
                [
                    "No qualified repository has been published at this level. Standards are not lowered to fill a slot.",
                    "",
                ]
            )
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
    if any(data.get("schema_version") != 2 for data in catalogs.values()):
        raise CatalogError("cannot generate until every language catalog uses schema version 2")
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
        "--complete", action="store_true", help="require exactly two entries per level and language"
    )
    subparsers.add_parser("generate", help="regenerate learner-facing Markdown")
    check_parser = subparsers.add_parser(
        "check-generated", help="fail when generated Markdown is missing or stale"
    )
    check_parser.add_argument(
        "--complete", action="store_true", help="also require the complete 200-entry corpus"
    )
    args = parser.parse_args(argv)

    if args.command == "validate":
        errors = validate_catalog(complete=args.complete)
        if errors:
            print_errors(errors)
            return 1
        print("Catalog data is valid." + (" Complete corpus: 200 entries." if args.complete else ""))
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
    print("Generated Markdown is current." + (" Complete corpus: 200 entries." if args.complete else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

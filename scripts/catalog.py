#!/usr/bin/env python3
"""Validate Exempla catalog data and generate GitHub-native Markdown."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CATALOG_DIR = ROOT / "catalog"
LANGUAGES_DIR = ROOT / "languages"

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REPOSITORY_RE = re.compile(r"^[^/\s]+/[^/\s]+$")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
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
GLOBAL_EXCLUSIONS = (
    "tests and test fixtures",
    "vendored and generated source",
    "build output and caches",
    "documentation and static assets",
)


class CatalogError(Exception):
    """Raised when catalog files cannot be loaded safely."""


def load_json(path: Path) -> dict[str, Any]:
    if is_dotenv_name(path.name):
        raise CatalogError(f"refusing to inspect dotenv-like path: {path}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise CatalogError(f"missing file: {path.relative_to(ROOT)}") from error
    except json.JSONDecodeError as error:
        raise CatalogError(
            f"invalid JSON in {path.relative_to(ROOT)}: {error.msg} at line {error.lineno}"
        ) from error
    if not isinstance(value, dict):
        raise CatalogError(f"top level must be an object: {path.relative_to(ROOT)}")
    return value


def is_dotenv_name(name: str) -> bool:
    """Return True for .env, *.env, and dotted dotenv variants."""
    lowered = name.lower()
    return lowered == ".env" or lowered.endswith(".env") or ".env." in lowered


def is_safe_relative_path(value: str) -> bool:
    path = PurePosixPath(value)
    return (
        bool(value)
        and not path.is_absolute()
        and ".." not in path.parts
        and not any(is_dotenv_name(part) for part in path.parts)
    )


def size_score(loc: int) -> int:
    if loc <= 2_000:
        return 1
    if loc <= 10_000:
        return 2
    if loc <= 50_000:
        return 3
    if loc <= 200_000:
        return 4
    return 5


def combined_level(size: int, difficulty: int, complexity: int) -> int:
    total = size + difficulty + complexity
    level = (total + 1) // 3
    if difficulty == 5 or complexity == 5:
        level = max(level, 4)
    if sum(score == 5 for score in (size, difficulty, complexity)) >= 2:
        level = 5
    return level


def calculate_learning_level(
    language: int, behavior: int, design: int, constraints: int
) -> int:
    """Calculate the public learner level from four path-centered scores."""
    scores = (language, behavior, design, constraints)
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


def require_keys(
    value: dict[str, Any], required: tuple[str, ...], path: str, errors: list[str]
) -> None:
    missing = [key for key in required if key not in value]
    if missing:
        errors.append(f"{path}: missing fields {', '.join(missing)}")


def require_exact_keys(
    value: dict[str, Any], required: tuple[str, ...], path: str, errors: list[str]
) -> None:
    """Require all named fields and reject unrecognized structured data."""
    require_keys(value, required, path, errors)
    unexpected = sorted(set(value) - set(required))
    if unexpected:
        errors.append(f"{path}: unexpected fields {', '.join(unexpected)}")


def require_text(value: Any, path: str, errors: list[str], minimum: int = 1) -> str:
    if not isinstance(value, str) or len(value.strip()) < minimum:
        errors.append(f"{path}: expected at least {minimum} non-whitespace characters")
        return ""
    return value.strip()


def require_text_list(
    value: Any, path: str, errors: list[str], minimum_items: int = 1
) -> list[str]:
    if not isinstance(value, list) or len(value) < minimum_items:
        errors.append(f"{path}: expected at least {minimum_items} text item(s)")
        return []
    result: list[str] = []
    for index, item in enumerate(value):
        text = require_text(item, f"{path}[{index}]", errors)
        if text:
            result.append(text)
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
    errors: list[str] = []
    prefix = f"catalog/{language['slug']}.json repositories[{index}]"
    item = require_object(entry, prefix, errors)
    required = (
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
        "start_here",
        "sdc",
        "quality",
        "inspection",
        "license",
        "github",
    )
    require_keys(item, required, prefix, errors)

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
    require_text(item.get("language_evidence"), f"{prefix}.language_evidence", errors, minimum=20)

    for field in ("description", "real_world_evidence", "why_study"):
        require_text(item.get(field), f"{prefix}.{field}", errors, minimum=20)
    require_text_list(item.get("learn"), f"{prefix}.learn", errors)
    require_text_list(item.get("prerequisites"), f"{prefix}.prerequisites", errors)

    start_here = require_object(item.get("start_here"), f"{prefix}.start_here", errors)
    require_keys(start_here, ("path", "reason"), f"{prefix}.start_here", errors)
    start_path = require_text(start_here.get("path"), f"{prefix}.start_here.path", errors)
    require_text(start_here.get("reason"), f"{prefix}.start_here.reason", errors, minimum=20)
    if start_path and not is_safe_relative_path(start_path):
        errors.append(f"{prefix}.start_here.path: expected safe non-dotenv relative path")

    sdc = require_object(item.get("sdc"), f"{prefix}.sdc", errors)
    require_keys(sdc, ("level", "size", "difficulty", "complexity", "placement"), f"{prefix}.sdc", errors)
    level = require_score(sdc.get("level"), f"{prefix}.sdc.level", errors)
    size = require_object(sdc.get("size"), f"{prefix}.sdc.size", errors)
    require_keys(size, ("score", "loc", "tool", "measured_at", "exclusions", "notes"), f"{prefix}.sdc.size", errors)
    s_score = require_score(size.get("score"), f"{prefix}.sdc.size.score", errors)
    loc = size.get("loc")
    if type(loc) is not int or loc < 1:
        errors.append(f"{prefix}.sdc.size.loc: expected positive integer")
        loc = None
    require_text(size.get("tool"), f"{prefix}.sdc.size.tool", errors)
    require_date(size.get("measured_at"), f"{prefix}.sdc.size.measured_at", errors)
    exclusions = size.get("exclusions")
    if not isinstance(exclusions, list):
        errors.append(f"{prefix}.sdc.size.exclusions: expected list")
    else:
        for exclusion_index, exclusion in enumerate(exclusions):
            require_text(exclusion, f"{prefix}.sdc.size.exclusions[{exclusion_index}]", errors)
    require_text(size.get("notes"), f"{prefix}.sdc.size.notes", errors, minimum=10)
    if loc is not None and s_score is not None and size_score(loc) != s_score:
        errors.append(
            f"{prefix}.sdc.size.score: LOC {loc} requires S{size_score(loc)}, not S{s_score}"
        )

    judgments: dict[str, int | None] = {}
    for dimension in ("difficulty", "complexity"):
        judgment = require_object(sdc.get(dimension), f"{prefix}.sdc.{dimension}", errors)
        require_keys(judgment, ("score", "signals", "reason"), f"{prefix}.sdc.{dimension}", errors)
        judgments[dimension] = require_score(
            judgment.get("score"), f"{prefix}.sdc.{dimension}.score", errors
        )
        require_text_list(judgment.get("signals"), f"{prefix}.sdc.{dimension}.signals", errors)
        require_text(judgment.get("reason"), f"{prefix}.sdc.{dimension}.reason", errors, minimum=20)
    require_text(sdc.get("placement"), f"{prefix}.sdc.placement", errors, minimum=20)
    if None not in (level, s_score, judgments.get("difficulty"), judgments.get("complexity")):
        expected_level = combined_level(
            s_score, judgments["difficulty"], judgments["complexity"]  # type: ignore[arg-type]
        )
        if level != expected_level:
            errors.append(
                f"{prefix}.sdc.level: S{s_score}/D{judgments['difficulty']}/C{judgments['complexity']} requires SDC {expected_level}, not {level}"
            )

    quality = require_object(item.get("quality"), f"{prefix}.quality", errors)
    require_keys(quality, QUALITY_FIELDS, f"{prefix}.quality", errors)
    for field in QUALITY_FIELDS:
        require_text(quality.get(field), f"{prefix}.quality.{field}", errors, minimum=20)

    inspection = require_object(item.get("inspection"), f"{prefix}.inspection", errors)
    require_keys(inspection, ("commit", "inspected_at", "reviewers", "files"), f"{prefix}.inspection", errors)
    commit = require_text(inspection.get("commit"), f"{prefix}.inspection.commit", errors)
    if commit and not COMMIT_RE.fullmatch(commit):
        errors.append(f"{prefix}.inspection.commit: expected 40 lowercase hexadecimal characters")
    require_date(inspection.get("inspected_at"), f"{prefix}.inspection.inspected_at", errors)
    require_text_list(inspection.get("reviewers"), f"{prefix}.inspection.reviewers", errors)
    files = require_text_list(inspection.get("files"), f"{prefix}.inspection.files", errors, minimum_items=3)
    for file_index, file_path in enumerate(files):
        if not is_safe_relative_path(file_path):
            errors.append(
                f"{prefix}.inspection.files[{file_index}]: expected safe non-dotenv relative path"
            )

    license_info = require_object(item.get("license"), f"{prefix}.license", errors)
    require_keys(license_info, ("spdx", "url"), f"{prefix}.license", errors)
    require_text(license_info.get("spdx"), f"{prefix}.license.spdx", errors)
    license_url = require_text(license_info.get("url"), f"{prefix}.license.url", errors)
    if license_url and repository and not license_url.startswith(expected_url + "/"):
        errors.append(f"{prefix}.license.url: expected a URL inside {expected_url}")

    github = require_object(item.get("github"), f"{prefix}.github", errors)
    require_keys(github, ("primary_language", "archived", "metadata_checked_at"), f"{prefix}.github", errors)
    github_language = require_text(
        github.get("primary_language"), f"{prefix}.github.primary_language", errors
    )
    if type(github.get("archived")) is not bool:
        errors.append(f"{prefix}.github.archived: expected boolean")
    require_date(github.get("metadata_checked_at"), f"{prefix}.github.metadata_checked_at", errors)
    return errors


def validate_repository_v2(
    entry: Any,
    language: dict[str, Any],
    index: int,
    seen_repositories: set[str],
    seen_slugs: set[str],
) -> list[str]:
    """Validate one path-centered schema-version-2 repository record."""
    errors: list[str] = []
    prefix = f"catalog/{language['slug']}.json repositories[{index}]"
    item = require_object(entry, prefix, errors)
    required = (
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
    require_exact_keys(item, required, prefix, errors)

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
    require_text(
        item.get("language_evidence"),
        f"{prefix}.language_evidence",
        errors,
        minimum=20,
    )
    for field in ("description", "real_world_evidence", "why_study"):
        require_text(item.get(field), f"{prefix}.{field}", errors, minimum=20)
    require_text_list(item.get("learn"), f"{prefix}.learn", errors)
    require_text_list(item.get("prerequisites"), f"{prefix}.prerequisites", errors)

    coding_relevance = require_object(
        item.get("coding_relevance"), f"{prefix}.coding_relevance", errors
    )
    require_exact_keys(
        coding_relevance,
        ("gate", "domain_context", "reason"),
        f"{prefix}.coding_relevance",
        errors,
    )
    gate = require_text(
        coding_relevance.get("gate"), f"{prefix}.coding_relevance.gate", errors
    )
    if gate and gate != "pass":
        errors.append(f"{prefix}.coding_relevance.gate: expected constant pass")
    require_text_list(
        coding_relevance.get("domain_context"),
        f"{prefix}.coding_relevance.domain_context",
        errors,
        minimum_items=0,
    )
    require_text(
        coding_relevance.get("reason"),
        f"{prefix}.coding_relevance.reason",
        errors,
        minimum=20,
    )

    learning_path = require_object(
        item.get("learning_path"), f"{prefix}.learning_path", errors
    )
    require_exact_keys(
        learning_path,
        ("goal", "start_here", "supporting_files", "trace"),
        f"{prefix}.learning_path",
        errors,
    )
    require_text(
        learning_path.get("goal"), f"{prefix}.learning_path.goal", errors, minimum=20
    )
    start_here = require_object(
        learning_path.get("start_here"), f"{prefix}.learning_path.start_here", errors
    )
    require_exact_keys(
        start_here,
        ("path", "reason"),
        f"{prefix}.learning_path.start_here",
        errors,
    )
    start_path = require_text(
        start_here.get("path"), f"{prefix}.learning_path.start_here.path", errors
    )
    require_text(
        start_here.get("reason"),
        f"{prefix}.learning_path.start_here.reason",
        errors,
        minimum=20,
    )
    if start_path and not is_safe_relative_path(start_path):
        errors.append(
            f"{prefix}.learning_path.start_here.path: expected safe non-dotenv relative path"
        )
    supporting_files = require_text_list(
        learning_path.get("supporting_files"),
        f"{prefix}.learning_path.supporting_files",
        errors,
    )
    for file_index, file_path in enumerate(supporting_files):
        if not is_safe_relative_path(file_path):
            errors.append(
                f"{prefix}.learning_path.supporting_files[{file_index}]: expected safe non-dotenv relative path"
            )
    if start_path and start_path in supporting_files:
        errors.append(
            f"{prefix}.learning_path.supporting_files: must contain paths in addition to start_here.path"
        )
    if len(set(supporting_files)) != len(supporting_files):
        errors.append(f"{prefix}.learning_path.supporting_files: duplicate path")
    require_text(
        learning_path.get("trace"),
        f"{prefix}.learning_path.trace",
        errors,
        minimum=20,
    )

    learning_level = require_object(
        item.get("learning_level"), f"{prefix}.learning_level", errors
    )
    dimension_names = (
        "language_technique",
        "behavioral_reasoning",
        "design_span",
        "constraint_burden",
    )
    require_exact_keys(
        learning_level,
        ("level", *dimension_names, "placement"),
        f"{prefix}.learning_level",
        errors,
    )
    level = require_score(
        learning_level.get("level"), f"{prefix}.learning_level.level", errors
    )
    scores: dict[str, int | None] = {}
    for dimension in dimension_names:
        judgment = require_object(
            learning_level.get(dimension),
            f"{prefix}.learning_level.{dimension}",
            errors,
        )
        require_exact_keys(
            judgment,
            ("score", "signals", "reason"),
            f"{prefix}.learning_level.{dimension}",
            errors,
        )
        scores[dimension] = require_score(
            judgment.get("score"),
            f"{prefix}.learning_level.{dimension}.score",
            errors,
        )
        require_text_list(
            judgment.get("signals"),
            f"{prefix}.learning_level.{dimension}.signals",
            errors,
        )
        require_text(
            judgment.get("reason"),
            f"{prefix}.learning_level.{dimension}.reason",
            errors,
            minimum=20,
        )
    require_text(
        learning_level.get("placement"),
        f"{prefix}.learning_level.placement",
        errors,
        minimum=20,
    )
    ordered_scores = tuple(scores[name] for name in dimension_names)
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
        require_text(quality.get(field), f"{prefix}.quality.{field}", errors, minimum=20)

    inspection = require_object(item.get("inspection"), f"{prefix}.inspection", errors)
    require_exact_keys(
        inspection,
        ("commit", "inspected_at", "reviewers", "files"),
        f"{prefix}.inspection",
        errors,
    )
    commit = require_text(inspection.get("commit"), f"{prefix}.inspection.commit", errors)
    if commit and not COMMIT_RE.fullmatch(commit):
        errors.append(
            f"{prefix}.inspection.commit: expected 40 lowercase hexadecimal characters"
        )
    require_date(inspection.get("inspected_at"), f"{prefix}.inspection.inspected_at", errors)
    require_text_list(inspection.get("reviewers"), f"{prefix}.inspection.reviewers", errors)
    files = require_text_list(
        inspection.get("files"), f"{prefix}.inspection.files", errors, minimum_items=3
    )
    for file_index, file_path in enumerate(files):
        if not is_safe_relative_path(file_path):
            errors.append(
                f"{prefix}.inspection.files[{file_index}]: expected safe non-dotenv relative path"
            )
    for path_name, path_value in [
        ("start_here.path", start_path),
        *((f"supporting_files[{index}]", value) for index, value in enumerate(supporting_files)),
    ]:
        if path_value and path_value not in files:
            errors.append(
                f"{prefix}.learning_path.{path_name}: must also appear in inspection.files"
            )

    license_info = require_object(item.get("license"), f"{prefix}.license", errors)
    require_exact_keys(license_info, ("spdx", "url"), f"{prefix}.license", errors)
    require_text(license_info.get("spdx"), f"{prefix}.license.spdx", errors)
    license_url = require_text(license_info.get("url"), f"{prefix}.license.url", errors)
    if license_url and repository and not license_url.startswith(expected_url + "/"):
        errors.append(f"{prefix}.license.url: expected a URL inside {expected_url}")

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
    require_date(
        github.get("metadata_checked_at"), f"{prefix}.github.metadata_checked_at", errors
    )
    return errors


def validate_languages(data: dict[str, Any]) -> tuple[list[dict[str, Any]], list[str]]:
    errors: list[str] = []
    if data.get("schema_version") != 1:
        errors.append("catalog/languages.json schema_version: expected 1")
    require_date(data.get("selected_at"), "catalog/languages.json selected_at", errors)
    baseline = require_object(data.get("baseline"), "catalog/languages.json baseline", errors)
    require_keys(baseline, ("name", "url", "published_at", "rule"), "catalog/languages.json baseline", errors)
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
        require_keys(language, ("order", "slug", "name", "source", "source_rank"), prefix, errors)
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


def validate_catalog(root: Path = ROOT, complete: bool = False) -> list[str]:
    global ROOT, CATALOG_DIR, LANGUAGES_DIR
    original = (ROOT, CATALOG_DIR, LANGUAGES_DIR)
    ROOT = root
    CATALOG_DIR = root / "catalog"
    LANGUAGES_DIR = root / "languages"
    try:
        language_data = load_json(CATALOG_DIR / "languages.json")
        languages, errors = validate_languages(language_data)
        seen_repositories: set[str] = set()
        total = 0
        for language in languages:
            path = CATALOG_DIR / f"{language['slug']}.json"
            try:
                data = load_json(path)
            except CatalogError as error:
                errors.append(str(error))
                continue
            schema_version = data.get("schema_version")
            if schema_version not in (1, 2):
                errors.append(
                    f"catalog/{language['slug']}.json schema_version: expected 1 or 2"
                )
            if data.get("language_slug") != language["slug"]:
                errors.append(
                    f"catalog/{language['slug']}.json language_slug: expected {language['slug']}"
                )
            repositories = data.get("repositories")
            if not isinstance(repositories, list):
                errors.append(f"catalog/{language['slug']}.json repositories: expected list")
                continue
            total += len(repositories)
            seen_slugs: set[str] = set()
            for index, entry in enumerate(repositories):
                validator = validate_repository_v2 if schema_version == 2 else validate_repository
                errors.extend(validator(entry, language, index, seen_repositories, seen_slugs))
            level_key = "learning_level" if schema_version == 2 else "sdc"
            level_label = "Level" if schema_version == 2 else "SDC"
            levels = Counter(
                entry.get(level_key, {}).get("level")
                for entry in repositories
                if isinstance(entry, dict) and isinstance(entry.get(level_key), dict)
            )
            for level in range(1, 6):
                count = levels[level]
                if count > 2:
                    errors.append(
                        f"catalog/{language['slug']}.json: {level_label} {level} has {count} entries; maximum is 2"
                    )
                if complete and count != 2:
                    errors.append(
                        f"catalog/{language['slug']}.json: {level_label} {level} requires 2 entries; found {count}"
                    )
        if complete and total != 200:
            errors.append(f"complete catalog requires 200 repositories; found {total}")
        return errors
    except CatalogError as error:
        return [str(error)]
    finally:
        ROOT, CATALOG_DIR, LANGUAGES_DIR = original


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def render_index(languages: list[dict[str, Any]], catalogs: dict[str, dict[str, Any]]) -> str:
    total = sum(len(catalogs[language["slug"]]["repositories"]) for language in languages)
    versions = {catalogs[language["slug"]].get("schema_version") for language in languages}
    if len(versions) != 1:
        raise CatalogError("cannot generate a partially migrated catalog")
    version = versions.pop()
    if version not in (1, 2):
        raise CatalogError(f"cannot generate unsupported catalog schema version {version}")
    level_label = "Level" if version == 2 else "SDC"
    level_key = "learning_level" if version == 2 else "sdc"
    rubric_link = (
        "../docs/learning-levels.md" if version == 2 else "../docs/sdc.md"
    )
    rubric_name = "how learning levels work" if version == 2 else "how SDC works"
    lines = [
        "# Languages",
        "",
        f"Choose a language, then browse from {level_label} 1 (most approachable) through {level_label} 5 (most demanding).",
        "",
        f"The catalog currently contains **{total} repositories across {len(languages)} languages**.",
        "",
        f"| Language | Entries | {level_label} 1 | {level_label} 2 | {level_label} 3 | {level_label} 4 | {level_label} 5 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for language in languages:
        repositories = catalogs[language["slug"]]["repositories"]
        counts = Counter(entry[level_key]["level"] for entry in repositories)
        lines.append(
            f"| [{markdown_escape(language['name'])}]({language['slug']}/README.md) | "
            + f"{len(repositories)} | "
            + " | ".join(str(counts[level]) for level in range(1, 6))
            + " |"
        )
    lines.extend(
        [
            "",
            f"Read [{rubric_name}]({rubric_link}), the [quality gate](../docs/qualification.md), "
            "or the [language selection rationale](../docs/language-selection.md).",
            "",
            "_Generated by `python3 scripts/catalog.py generate`; do not edit by hand._",
            "",
        ]
    )
    return "\n".join(lines)


def render_repository_v1(entry: dict[str, Any]) -> list[str]:
    sdc = entry["sdc"]
    size = sdc["size"]
    difficulty = sdc["difficulty"]
    complexity = sdc["complexity"]
    inspection = entry["inspection"]
    start_url = f"{entry['url']}/blob/{inspection['commit']}/{entry['start_here']['path']}"
    license_info = entry["license"]
    lines = [
        f"### [{entry['repository']}]({entry['url']})",
        "",
        f"**S{size['score']} / D{difficulty['score']} / C{complexity['score']} → SDC {sdc['level']}**",
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
    lines.extend(
        [
            "",
            f"**Start here:** [`{entry['start_here']['path']}`]({start_url}) — {entry['start_here']['reason']}",
            "",
            "**Why this level:**",
            "",
            f"- **S{size['score']}:** {size['loc']:,} meaningful implementation LOC measured with {size['tool']}. {size['notes']}",
            f"- **D{difficulty['score']}:** {difficulty['reason']}",
            f"- **C{complexity['score']}:** {complexity['reason']}",
            f"- **Placement:** {sdc['placement']}",
            "",
            "**Quality-gate evidence:**",
            "",
        ]
    )
    quality_labels = {
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
        f"- **{quality_labels[field]}:** {entry['quality'][field]}" for field in QUALITY_FIELDS
    )
    reviewed_files = ", ".join(f"`{path}`" for path in inspection["files"])
    exclusions = ", ".join(size["exclusions"] or GLOBAL_EXCLUSIONS)
    archive_note = " Archived repository." if entry["github"]["archived"] else ""
    github_language = entry["github"]["primary_language"]
    lines.extend(
        [
            "",
            f"**Inspection record:** commit `{inspection['commit']}`, reviewed {inspection['inspected_at']} by {', '.join(inspection['reviewers'])}. Files sampled: {reviewed_files}. GitHub Linguist label: {github_language}. LOC exclusions: {exclusions}.{archive_note}",
            "",
            f"**License:** [{license_info['spdx']}]({license_info['url']})",
            "",
        ]
    )
    return lines


def render_repository_v2(entry: dict[str, Any]) -> list[str]:
    learning_level = entry["learning_level"]
    language = learning_level["language_technique"]
    behavior = learning_level["behavioral_reasoning"]
    design = learning_level["design_span"]
    constraints = learning_level["constraint_burden"]
    learning_path = entry["learning_path"]
    inspection = entry["inspection"]
    start_here = learning_path["start_here"]
    start_url = f"{entry['url']}/blob/{inspection['commit']}/{start_here['path']}"
    license_info = entry["license"]
    lines = [
        f"### [{entry['repository']}]({entry['url']})",
        "",
        f"**Language {language['score']} / Behavior {behavior['score']} / Design {design['score']} / Constraints {constraints['score']} → Level {learning_level['level']}**",
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
    lines.extend(
        [
            "",
            "**Coding relevance:**",
            "",
            entry["coding_relevance"]["reason"],
            "",
        ]
    )
    domain_context = entry["coding_relevance"]["domain_context"]
    if domain_context:
        lines.extend(["Required domain context:", ""])
        lines.extend(f"- {item}" for item in domain_context)
        lines.append("")
    else:
        lines.extend(["No specialist domain context is required.", ""])
    lines.extend(
        [
            "**Learning path:**",
            "",
            f"- **Goal:** {learning_path['goal']}",
            f"- **Start here:** [`{start_here['path']}`]({start_url}) — {start_here['reason']}",
            "- **Then read:**",
        ]
    )
    for file_path in learning_path["supporting_files"]:
        file_url = f"{entry['url']}/blob/{inspection['commit']}/{file_path}"
        lines.append(f"  - [`{file_path}`]({file_url})")
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
            f"- **Placement:** {learning_level['placement']}",
            "",
            "**Quality-gate evidence:**",
            "",
        ]
    )
    quality_labels = {
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
        f"- **{quality_labels[field]}:** {entry['quality'][field]}" for field in QUALITY_FIELDS
    )
    reviewed_files = ", ".join(f"`{path}`" for path in inspection["files"])
    archive_note = " Archived repository." if entry["github"]["archived"] else ""
    github_language = entry["github"]["primary_language"]
    lines.extend(
        [
            "",
            f"**Inspection record:** commit `{inspection['commit']}`, reviewed {inspection['inspected_at']} by {', '.join(inspection['reviewers'])}. Files sampled: {reviewed_files}. GitHub Linguist label: {github_language}.{archive_note}",
            "",
            f"**License:** [{license_info['spdx']}]({license_info['url']})",
            "",
        ]
    )
    return lines


def render_repository(entry: dict[str, Any]) -> list[str]:
    if "learning_level" in entry:
        return render_repository_v2(entry)
    return render_repository_v1(entry)


def render_language(language: dict[str, Any], data: dict[str, Any]) -> str:
    version = data.get("schema_version")
    if version not in (1, 2):
        raise CatalogError(f"cannot generate unsupported catalog schema version {version}")
    level_key = "learning_level" if version == 2 else "sdc"
    level_label = "Level" if version == 2 else "SDC"
    rubric_name = "learning-level rubric" if version == 2 else "SDC rubric"
    rubric_path = "../../docs/learning-levels.md" if version == 2 else "../../docs/sdc.md"
    repositories = sorted(
        data["repositories"],
        key=lambda entry: (entry[level_key]["level"], entry["repository"].lower()),
    )
    lines = [
        f"# {language['name']}",
        "",
        f"{len(repositories)} qualified repositories. Scores assume the learner described in [the {rubric_name}]({rubric_path}).",
        "",
        "[← All languages](../README.md)",
        "",
    ]
    for level in range(1, 6):
        lines.extend([f"## {level_label} {level}", ""])
        entries = [entry for entry in repositories if entry[level_key]["level"] == level]
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
            "_Generated from `catalog/" + language["slug"] + ".json`; do not edit by hand._",
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
    errors: list[str] = []
    try:
        expected = generated_files(root)
    except CatalogError as error:
        return [str(error)]
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
    validate_parser.add_argument("--complete", action="store_true", help="require 200 entries: two per level and language")
    subparsers.add_parser("generate", help="regenerate learner-facing Markdown")
    check_parser = subparsers.add_parser("check-generated", help="fail when generated Markdown is missing or stale")
    check_parser.add_argument("--complete", action="store_true", help="also require the complete 200-entry corpus")
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

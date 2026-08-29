from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("catalog_tool", ROOT / "scripts" / "catalog.py")
assert SPEC and SPEC.loader
catalog_tool = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(catalog_tool)


def valid_entry() -> dict:
    repository = "example/real-tool"
    commit = "a" * 40
    return {
        "slug": "real-tool",
        "repository": repository,
        "url": f"https://github.com/{repository}",
        "primary_language": "Python",
        "language_evidence": "The src directory contains the first-party Python implementation.",
        "description": "A real command-line tool that performs useful production work.",
        "real_world_evidence": "Published releases are used as a command-line utility by real users.",
        "why_study": "The small implementation has explicit boundaries and behavior-focused tests.",
        "learn": ["How a command-line request flows into a focused domain function."],
        "prerequisites": ["Basic Python functions, modules, and exceptions."],
        "start_here": {
            "path": "src/tool.py",
            "reason": "This module connects the public command to the core transformation.",
        },
        "sdc": {
            "level": 1,
            "size": {
                "score": 1,
                "loc": 500,
                "tool": "tokei 14.0.0",
                "measured_at": "2026-08-28",
                "exclusions": ["tests"],
                "notes": "The count covers first-party implementation source only.",
            },
            "difficulty": {
                "score": 1,
                "signals": ["direct control flow"],
                "reason": "The implementation uses direct control flow and ordinary data structures.",
            },
            "complexity": {
                "score": 1,
                "signals": ["one process"],
                "reason": "One process and two focused modules contain the important behavior.",
            },
            "placement": "All three dimensions fit the most approachable published band.",
        },
        "quality": {
            "source_quality": "Functions are short, direct, and free of unexplained cleverness.",
            "architecture": "The command adapter and domain transformation have a clear boundary.",
            "naming_and_idiom": "Names expose intent and use conventional Python structure.",
            "tests": "Behavior tests cover the normal request and a representative error.",
            "documentation": "The README explains purpose, installation, and supported behavior.",
            "traceability": "A command can be followed through one adapter into its tested function.",
            "maintainability": "The modules have narrow responsibilities and explicit error handling.",
            "educational_value": "It demonstrates a complete small utility without teaching scaffolding.",
        },
        "inspection": {
            "commit": commit,
            "inspected_at": "2026-08-28",
            "reviewers": ["Codex"],
            "files": ["README.md", "src/tool.py", "tests/test_tool.py"],
        },
        "license": {
            "spdx": "MIT",
            "url": f"https://github.com/{repository}/blob/{commit}/LICENSE",
        },
        "github": {
            "primary_language": "Python",
            "archived": False,
            "metadata_checked_at": "2026-08-28",
        },
    }


def valid_v2_entry() -> dict:
    entry = valid_entry()
    start_here = entry.pop("start_here")
    entry.pop("sdc")
    entry["coding_relevance"] = {
        "gate": "pass",
        "domain_context": [],
        "reason": "The path teaches reusable request validation and transformation without specialist domain knowledge.",
    }
    entry["learning_path"] = {
        "goal": "Understand how a command request is validated and transformed into its observable result.",
        "start_here": start_here,
        "supporting_files": ["tests/test_tool.py"],
        "trace": "Start at the command adapter, follow its validation into the transformation, then confirm both success and error behavior in the focused test.",
    }
    entry["learning_level"] = {
        "level": 1,
        "language_technique": {
            "score": 1,
            "signals": ["direct functions and ordinary modules"],
            "reason": "Direct functions, ordinary modules, and basic exceptions contain the selected path.",
        },
        "behavioral_reasoning": {
            "score": 1,
            "signals": ["local synchronous data flow"],
            "reason": "The request follows local synchronous data flow with one explicit error path.",
        },
        "design_span": {
            "score": 1,
            "signals": ["one focused component"],
            "reason": "The command adapter and transformation form one focused component across a few functions.",
        },
        "constraint_burden": {
            "score": 1,
            "signals": ["ordinary output correctness"],
            "reason": "The main guarantee is the small transformation contract and its expected output.",
        },
        "placement": "All four observed dimensions fit Level 1 and the formula returns that level.",
    }
    return entry


class ScoreTests(unittest.TestCase):
    def test_learning_level_examples_and_guardrails(self) -> None:
        cases = {
            (1, 1, 1, 1): 1,
            (2, 2, 1, 1): 2,
            (3, 3, 2, 2): 3,
            (4, 4, 3, 3): 4,
            (5, 2, 2, 2): 4,
            (5, 5, 1, 1): 4,
            (5, 5, 4, 4): 5,
        }
        for scores, expected in cases.items():
            with self.subTest(scores=scores):
                self.assertEqual(catalog_tool.calculate_learning_level(*scores), expected)

    def test_size_boundaries(self) -> None:
        cases = {
            1: 1,
            2_000: 1,
            2_001: 2,
            10_000: 2,
            10_001: 3,
            50_000: 3,
            50_001: 4,
            200_000: 4,
            200_001: 5,
        }
        for loc, expected in cases.items():
            with self.subTest(loc=loc):
                self.assertEqual(catalog_tool.size_score(loc), expected)

    def test_combination_examples_and_guardrails(self) -> None:
        cases = {
            (1, 1, 1): 1,
            (2, 3, 2): 2,
            (1, 5, 2): 4,
            (5, 2, 3): 3,
            (5, 5, 4): 5,
            (1, 1, 5): 4,
            (1, 5, 5): 5,
        }
        for scores, expected in cases.items():
            with self.subTest(scores=scores):
                self.assertEqual(catalog_tool.combined_level(*scores), expected)


class RecordValidationTests(unittest.TestCase):
    language = {"slug": "python", "name": "Python"}

    def validate(self, entry: dict, seen: set[str] | None = None) -> list[str]:
        return catalog_tool.validate_repository(
            entry, self.language, 0, seen if seen is not None else set(), set()
        )

    def test_valid_record_passes(self) -> None:
        self.assertEqual(self.validate(valid_entry()), [])

    def test_missing_field_fails(self) -> None:
        entry = valid_entry()
        del entry["description"]
        errors = self.validate(entry)
        self.assertTrue(any("missing fields description" in error for error in errors))

    def test_duplicate_repository_fails(self) -> None:
        seen: set[str] = set()
        self.assertEqual(self.validate(valid_entry(), seen), [])
        errors = self.validate(valid_entry(), seen)
        self.assertTrue(any("duplicate across catalog" in error for error in errors))

    def test_invalid_score_and_formula_fail(self) -> None:
        entry = valid_entry()
        entry["sdc"]["level"] = 3
        errors = self.validate(entry)
        self.assertTrue(any("requires SDC 1, not 3" in error for error in errors))
        entry["sdc"]["difficulty"]["score"] = 6
        errors = self.validate(entry)
        self.assertTrue(any("expected integer from 1 through 5" in error for error in errors))

    def test_unsafe_slug_and_bad_url_fail(self) -> None:
        entry = valid_entry()
        entry["slug"] = "Bad Slug"
        entry["url"] = "http://example.com/not-github"
        errors = self.validate(entry)
        self.assertTrue(any("single hyphens" in error for error in errors))
        self.assertTrue(any("expected https://github.com" in error for error in errors))

    def test_dotenv_inspection_path_is_rejected(self) -> None:
        entry = valid_entry()
        entry["inspection"]["files"][1] = "config/service.env.production"
        errors = self.validate(entry)
        self.assertTrue(any("non-dotenv relative path" in error for error in errors))

    def test_github_linguist_label_may_differ_with_source_evidence(self) -> None:
        entry = valid_entry()
        entry["github"]["primary_language"] = "Jupyter Notebook"
        self.assertEqual(self.validate(entry), [])

    def test_loc_must_match_size_band(self) -> None:
        entry = valid_entry()
        entry["sdc"]["size"]["loc"] = 2_001
        errors = self.validate(entry)
        self.assertTrue(any("requires S2, not S1" in error for error in errors))


class VersionTwoRecordValidationTests(unittest.TestCase):
    language = {"slug": "python", "name": "Python"}

    def validate(self, entry: dict, seen: set[str] | None = None) -> list[str]:
        return catalog_tool.validate_repository_v2(
            entry, self.language, 0, seen if seen is not None else set(), set()
        )

    def test_valid_record_passes_and_renders_learning_evidence(self) -> None:
        entry = valid_v2_entry()
        self.assertEqual(self.validate(entry), [])
        rendered = "\n".join(catalog_tool.render_repository_v2(entry))
        self.assertIn("Language 1 / Behavior 1 / Design 1 / Constraints 1 → Level 1", rendered)
        self.assertIn("**Coding relevance:**", rendered)
        self.assertIn("**Learning path:**", rendered)
        self.assertIn("tests/test_tool.py", rendered)

    def test_stored_level_must_match_formula(self) -> None:
        entry = valid_v2_entry()
        entry["learning_level"]["level"] = 3
        errors = self.validate(entry)
        self.assertTrue(any("require Level 1, not 3" in error for error in errors))

    def test_each_dimension_rejects_scores_outside_one_through_five(self) -> None:
        dimensions = (
            "language_technique",
            "behavioral_reasoning",
            "design_span",
            "constraint_burden",
        )
        for dimension, invalid in zip(dimensions, (0, 6, 1.5, True), strict=True):
            with self.subTest(dimension=dimension, invalid=invalid):
                entry = valid_v2_entry()
                entry["learning_level"][dimension]["score"] = invalid
                errors = self.validate(entry)
                self.assertTrue(
                    any(
                        f"learning_level.{dimension}.score: expected integer from 1 through 5"
                        in error
                        for error in errors
                    )
                )

    def test_coding_relevance_gate_is_required_and_must_pass(self) -> None:
        missing = valid_v2_entry()
        del missing["coding_relevance"]["gate"]
        self.assertTrue(
            any("missing fields gate" in error for error in self.validate(missing))
        )

        failed = valid_v2_entry()
        failed["coding_relevance"]["gate"] = "fail"
        self.assertTrue(
            any("expected constant pass" in error for error in self.validate(failed))
        )

    def test_learning_path_requires_goal_trace_start_and_supporting_files(self) -> None:
        cases = (
            ("goal",),
            ("trace",),
            ("start_here",),
            ("supporting_files",),
            ("start_here", "path"),
        )
        for path in cases:
            with self.subTest(path=path):
                entry = valid_v2_entry()
                target = entry["learning_path"]
                for part in path[:-1]:
                    target = target[part]
                del target[path[-1]]
                errors = self.validate(entry)
                self.assertTrue(any("missing fields" in error for error in errors))

    def test_every_learning_path_file_must_be_inspected(self) -> None:
        entry = valid_v2_entry()
        entry["inspection"]["files"].remove("tests/test_tool.py")
        errors = self.validate(entry)
        self.assertTrue(any("must also appear in inspection.files" in error for error in errors))

    def test_dotenv_like_learning_and_inspection_paths_are_rejected(self) -> None:
        for field in ("start", "supporting", "inspection"):
            with self.subTest(field=field):
                entry = valid_v2_entry()
                if field == "start":
                    entry["learning_path"]["start_here"]["path"] = ".env.local"
                elif field == "supporting":
                    entry["learning_path"]["supporting_files"][0] = "config/service.env"
                else:
                    entry["inspection"]["files"][0] = "nested/secrets.env.production"
                errors = self.validate(entry)
                self.assertTrue(any("non-dotenv relative path" in error for error in errors))

    def test_obsolete_or_unrecognized_fields_are_rejected(self) -> None:
        entry = valid_v2_entry()
        entry["sdc"] = {"level": 1}
        errors = self.validate(entry)
        self.assertTrue(any("unexpected fields sdc" in error for error in errors))

    def test_supporting_file_is_distinct_and_unique(self) -> None:
        entry = valid_v2_entry()
        entry["learning_path"]["supporting_files"] = [
            "src/tool.py",
            "tests/test_tool.py",
            "tests/test_tool.py",
        ]
        errors = self.validate(entry)
        self.assertTrue(any("in addition to start_here.path" in error for error in errors))
        self.assertTrue(any("duplicate path" in error for error in errors))


class CatalogIntegrationTests(unittest.TestCase):
    def make_root(self, *, empty: bool = False, schema_version: int = 1) -> Path:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        catalog = root / "catalog"
        catalog.mkdir()
        language_data = json.loads((ROOT / "catalog" / "languages.json").read_text())
        (catalog / "languages.json").write_text(
            json.dumps(language_data, indent=2) + "\n", encoding="utf-8"
        )
        for language in language_data["languages"]:
            source = ROOT / "catalog" / f"{language['slug']}.json"
            destination = catalog / source.name
            if empty:
                content = {
                    "schema_version": schema_version,
                    "language_slug": language["slug"],
                    "repositories": [],
                }
                destination.write_text(
                    json.dumps(content, indent=2) + "\n", encoding="utf-8"
                )
            else:
                destination.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
        return root

    def test_complete_mode_catches_missing_corpus(self) -> None:
        errors = catalog_tool.validate_catalog(self.make_root(empty=True), complete=True)
        self.assertTrue(any("requires 200 repositories; found 0" in error for error in errors))
        self.assertTrue(any("SDC 1 requires 2 entries" in error for error in errors))

    def test_version_two_incomplete_catalog_is_valid_but_not_complete(self) -> None:
        root = self.make_root(empty=True, schema_version=2)
        self.assertEqual(catalog_tool.validate_catalog(root), [])
        errors = catalog_tool.validate_catalog(root, complete=True)
        self.assertTrue(any("requires 200 repositories; found 0" in error for error in errors))
        self.assertTrue(any("Level 1 requires 2 entries" in error for error in errors))

    def test_stale_generated_markdown_is_detected(self) -> None:
        root = self.make_root()
        catalog_tool.write_generated(root)
        self.assertEqual(catalog_tool.check_generated(root), [])
        index = root / "languages" / "README.md"
        index.write_text("stale\n", encoding="utf-8")
        self.assertIn("stale generated file: languages/README.md", catalog_tool.check_generated(root))

    def test_generation_is_deterministic(self) -> None:
        root = self.make_root()
        first = catalog_tool.generated_files(root)
        second = catalog_tool.generated_files(root)
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()

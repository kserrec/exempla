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


class ScoreTests(unittest.TestCase):
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

    def test_loc_must_match_size_band(self) -> None:
        entry = valid_entry()
        entry["sdc"]["size"]["loc"] = 2_001
        errors = self.validate(entry)
        self.assertTrue(any("requires S2, not S1" in error for error in errors))


class CatalogIntegrationTests(unittest.TestCase):
    def make_root(self) -> Path:
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
            destination.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
        return root

    def test_complete_mode_catches_missing_corpus(self) -> None:
        errors = catalog_tool.validate_catalog(self.make_root(), complete=True)
        self.assertTrue(any("requires 200 repositories; found 0" in error for error in errors))
        self.assertTrue(any("SDC 1 requires 2 entries" in error for error in errors))

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

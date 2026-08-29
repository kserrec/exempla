from __future__ import annotations

import importlib.util
import json
import re
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
        "why_study": "The path demonstrates a complete request, validation, and transformation boundary.",
        "learn": ["Understand how a command request becomes a tested observable result."],
        "prerequisites": ["Basic Python functions, modules, collections, and exceptions."],
        "coding_relevance": {
            "gate": "pass",
            "domain_context": [],
            "reason": "The path teaches reusable request validation and transformation without specialist domain knowledge.",
        },
        "learning_path": {
            "goal": "Understand how a command request is validated and transformed into its observable result.",
            "start_here": {
                "path": "src/tool.py",
                "reason": "This module connects the public command to the core transformation.",
            },
            "supporting_files": ["tests/test_tool.py"],
            "trace": "Start at the command adapter, follow validation into the transformation, then confirm success and error behavior in the focused test.",
        },
        "learning_level": {
            "level": 1,
            "language_technique": {
                "score": 1,
                "signals": ["direct functions and ordinary modules"],
                "reason": "Direct functions, ordinary modules, and basic exceptions contain the path.",
            },
            "behavioral_reasoning": {
                "score": 1,
                "signals": ["local synchronous data flow"],
                "reason": "The request follows local synchronous data flow with one explicit error path.",
            },
            "design_span": {
                "score": 1,
                "signals": ["one focused component"],
                "reason": "The command adapter and transformation form one focused component.",
            },
            "constraint_burden": {
                "score": 1,
                "signals": ["ordinary output correctness"],
                "reason": "The main guarantee is the small transformation contract and expected output.",
            },
            "placement": "All four observed dimensions fit Level 1 and the formula returns that level.",
        },
        "quality": {
            "source_quality": "Functions are short, direct, and free of unexplained cleverness.",
            "architecture": "The command adapter and transformation have one clear boundary.",
            "naming_and_idiom": "Names expose intent and use conventional Python structure.",
            "tests": "Behavior tests cover the normal request and a representative error.",
            "documentation": "The README explains purpose, installation, and supported behavior.",
            "traceability": "A command can be followed through one adapter into its tested function.",
            "maintainability": "Modules have narrow responsibilities and explicit error handling.",
            "educational_value": "The path demonstrates a complete utility without teaching scaffolding.",
        },
        "inspection": {
            "commit": commit,
            "inspected_at": "2026-08-29",
            "reviewers": ["Codex", "independent Codex reviewer"],
            "files": ["README.md", "src/tool.py", "tests/test_tool.py", "LICENSE"],
        },
        "license": {
            "spdx": "MIT",
            "urls": [f"https://github.com/{repository}/blob/{commit}/LICENSE"],
        },
        "github": {
            "primary_language": "Python",
            "archived": False,
            "metadata_checked_at": "2026-08-28",
        },
    }


class ScoreTests(unittest.TestCase):
    def test_required_examples_and_guardrails(self) -> None:
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

    def test_invalid_inputs_are_rejected(self) -> None:
        for scores in ((0, 1, 1, 1), (1, 6, 1, 1), (1, 1.5, 1, 1), (True, 1, 1, 1)):
            with self.subTest(scores=scores):
                with self.assertRaisesRegex(ValueError, "integers from 1 through 5"):
                    catalog_tool.calculate_learning_level(*scores)


class RecordValidationTests(unittest.TestCase):
    language = {"slug": "python", "name": "Python"}

    def validate(self, entry: dict, seen: set[str] | None = None) -> list[str]:
        return catalog_tool.validate_repository(
            entry, self.language, 0, seen if seen is not None else set(), set()
        )

    def test_valid_record_passes_and_renders_learning_evidence(self) -> None:
        entry = valid_entry()
        self.assertEqual(self.validate(entry), [])
        rendered = "\n".join(catalog_tool.render_repository(entry))
        self.assertIn("Language 1 / Behavior 1 / Design 1 / Constraints 1 → Level 1", rendered)
        self.assertIn("**Coding relevance:**", rendered)
        self.assertIn("**Learning path:**", rendered)
        self.assertIn("tests/test_tool.py", rendered)

    def test_missing_and_obsolete_fields_fail(self) -> None:
        missing = valid_entry()
        del missing["description"]
        self.assertTrue(any("missing fields description" in error for error in self.validate(missing)))
        obsolete = valid_entry()
        obsolete["sdc"] = {"level": 1}
        self.assertTrue(any("unexpected fields sdc" in error for error in self.validate(obsolete)))

    def test_duplicate_repository_fails(self) -> None:
        seen: set[str] = set()
        self.assertEqual(self.validate(valid_entry(), seen), [])
        self.assertTrue(any("duplicate across catalog" in error for error in self.validate(valid_entry(), seen)))

    def test_score_range_and_formula_are_enforced(self) -> None:
        invalid = valid_entry()
        invalid["learning_level"]["language_technique"]["score"] = 6
        self.assertTrue(any("integer from 1 through 5" in error for error in self.validate(invalid)))
        mismatch = valid_entry()
        mismatch["learning_level"]["level"] = 3
        self.assertTrue(any("require Level 1, not 3" in error for error in self.validate(mismatch)))

    def test_coding_relevance_gate_is_required_and_must_pass(self) -> None:
        missing = valid_entry()
        del missing["coding_relevance"]["gate"]
        self.assertTrue(any("missing fields gate" in error for error in self.validate(missing)))
        failed = valid_entry()
        failed["coding_relevance"]["gate"] = "fail"
        self.assertTrue(any("expected constant pass" in error for error in self.validate(failed)))

    def test_learning_path_requires_goal_start_support_and_trace(self) -> None:
        cases = (("goal",), ("trace",), ("start_here",), ("supporting_files",), ("start_here", "path"))
        for path in cases:
            with self.subTest(path=path):
                entry = valid_entry()
                target = entry["learning_path"]
                for part in path[:-1]:
                    target = target[part]
                del target[path[-1]]
                self.assertTrue(any("missing fields" in error for error in self.validate(entry)))

    def test_learning_and_license_paths_must_be_inspected(self) -> None:
        learning = valid_entry()
        learning["inspection"]["files"].remove("tests/test_tool.py")
        self.assertTrue(any("must also appear" in error for error in self.validate(learning)))
        license_entry = valid_entry()
        license_entry["inspection"]["files"].remove("LICENSE")
        self.assertTrue(any("license path must appear" in error for error in self.validate(license_entry)))

    def test_dotenv_variants_are_rejected_everywhere(self) -> None:
        names = (
            ".env",
            "service.env",
            ".env.local",
            "service.env.production",
            ".ENV",
            "SERVICE.ENV.production",
        )
        for name in names:
            for field in ("start", "supporting", "inspection"):
                with self.subTest(name=name, field=field):
                    entry = valid_entry()
                    value = f"config/{name}"
                    if field == "start":
                        entry["learning_path"]["start_here"]["path"] = value
                    elif field == "supporting":
                        entry["learning_path"]["supporting_files"][0] = value
                    else:
                        entry["inspection"]["files"][0] = value
                    self.assertTrue(any("non-dotenv" in error for error in self.validate(entry)))

    def test_paths_must_be_canonical_relative_and_unique(self) -> None:
        for invalid_path in ("/src/tool.py", "../src/tool.py", "src//tool.py", "src/./tool.py", "src\\tool.py"):
            with self.subTest(path=invalid_path):
                entry = valid_entry()
                entry["learning_path"]["start_here"]["path"] = invalid_path
                self.assertTrue(any("canonical safe" in error for error in self.validate(entry)))
        duplicate_support = valid_entry()
        duplicate_support["learning_path"]["supporting_files"] *= 2
        self.assertTrue(any("duplicate value" in error for error in self.validate(duplicate_support)))
        duplicate_inspection = valid_entry()
        duplicate_inspection["inspection"]["files"].append("README.md")
        self.assertTrue(any("duplicate value" in error for error in self.validate(duplicate_inspection)))

    def test_repository_url_commit_date_language_and_prose_are_checked(self) -> None:
        entry = valid_entry()
        entry["url"] = "https://example.com/not-github"
        entry["inspection"]["commit"] = "bad"
        entry["inspection"]["inspected_at"] = "2026-99-99"
        entry["primary_language"] = "Ruby"
        entry["why_study"] = "short"
        errors = self.validate(entry)
        for fragment in ("expected https://github.com", "40 lowercase", "ISO date", "expected catalog language", "at least 20"):
            self.assertTrue(any(fragment in error for error in errors), fragment)

    def test_license_urls_are_unique_and_pinned_to_the_inspection(self) -> None:
        wrong_commit = valid_entry()
        wrong_commit["license"]["urls"][0] = "https://github.com/example/real-tool/blob/" + "b" * 40 + "/LICENSE"
        self.assertTrue(any("expected URL pinned" in error for error in self.validate(wrong_commit)))
        duplicate = valid_entry()
        duplicate["license"]["urls"] *= 2
        self.assertTrue(any("duplicate value" in error for error in self.validate(duplicate)))

    def test_github_linguist_label_may_differ_with_source_evidence(self) -> None:
        entry = valid_entry()
        entry["github"]["primary_language"] = "Jupyter Notebook"
        self.assertEqual(self.validate(entry), [])


class CatalogIntegrationTests(unittest.TestCase):
    def make_root(self, *, empty: bool = False, schema_version: int = 2) -> Path:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        catalog = root / "catalog"
        catalog.mkdir()
        for name in ("languages.json", "schema.json"):
            (catalog / name).write_text((ROOT / "catalog" / name).read_text(encoding="utf-8"), encoding="utf-8")
        language_data = json.loads((catalog / "languages.json").read_text(encoding="utf-8"))
        for language in language_data["languages"]:
            source = ROOT / "catalog" / f"{language['slug']}.json"
            destination = catalog / source.name
            if empty:
                content = {"schema_version": schema_version, "language_slug": language["slug"], "repositories": []}
                destination.write_text(json.dumps(content, indent=2) + "\n", encoding="utf-8")
            else:
                destination.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
        return root

    def add_research(self, root: Path) -> None:
        research = root / "research"
        research.mkdir()
        for name in (
            "learner-centered-rebuild.json",
            "learner-centered-gap-research.json",
            "rejections.json",
        ):
            (research / name).write_text(
                (ROOT / "research" / name).read_text(encoding="utf-8"),
                encoding="utf-8",
            )

    def test_current_catalog_schema_and_rebuild_audit_reconcile(self) -> None:
        self.assertEqual(catalog_tool.validate_catalog(ROOT), [])

    def test_gap_research_requires_diligent_channels_and_reconciles_acceptance(self) -> None:
        root = self.make_root()
        self.add_research(root)
        self.assertEqual(catalog_tool.validate_catalog(root), [])
        gap_path = root / "research" / "learner-centered-gap-research.json"
        audit = json.loads(gap_path.read_text(encoding="utf-8"))
        audit["languages"][0]["discovery_channels"] = audit["languages"][0][
            "discovery_channels"
        ][:2]
        gap_path.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
        self.assertTrue(
            any(
                "expected at least 3 channels" in error
                for error in catalog_tool.validate_catalog(root)
            )
        )

    def test_later_reconsideration_may_follow_the_ordered_cutover_rejections(self) -> None:
        root = self.make_root()
        self.add_research(root)
        rejection_path = root / "research" / "rejections.json"
        rejection_data = json.loads(rejection_path.read_text(encoding="utf-8"))
        reconsidered = dict(rejection_data["rejections"][45])
        reconsidered["evidence"] = "A later independent research pass reached a new evidence-backed rejection."
        rejection_data["rejections"].append(reconsidered)
        rejection_path.write_text(
            json.dumps(rejection_data, indent=2) + "\n", encoding="utf-8"
        )
        self.assertEqual(catalog_tool.validate_catalog(root), [])

    def test_schema_version_one_is_rejected(self) -> None:
        root = self.make_root(empty=True, schema_version=1)
        errors = catalog_tool.validate_catalog(root)
        self.assertTrue(any("schema_version: expected 2" in error for error in errors))

    def test_incomplete_catalog_is_valid_but_not_complete(self) -> None:
        root = self.make_root(empty=True)
        self.assertEqual(catalog_tool.validate_catalog(root), [])
        errors = catalog_tool.validate_catalog(root, complete=True)
        self.assertTrue(any("complete catalog requires 200 repositories; found 0" in error for error in errors))
        self.assertTrue(any("Level 1 requires 2 entries" in error for error in errors))

    def test_schema_and_manual_validator_stay_aligned(self) -> None:
        self.assertEqual(catalog_tool.validate_schema(ROOT), [])
        published_schema = json.loads(
            (ROOT / "catalog" / "schema.json").read_text(encoding="utf-8")
        )
        published_path_pattern = re.compile(
            published_schema["$defs"]["safePath"]["pattern"]
        )
        for invalid_path in (
            ".env",
            "config/SERVICE.ENV.production",
            "src/./tool.py",
            "src/",
            "README.md/",
            "../src/tool.py",
            "src//tool.py",
            "src\\tool.py",
        ):
            with self.subTest(invalid_path=invalid_path):
                self.assertIsNone(published_path_pattern.fullmatch(invalid_path))
        root = self.make_root(empty=True)
        schema_path = root / "catalog" / "schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        schema["$defs"]["repository"]["required"].remove("learning_path")
        schema_path.write_text(json.dumps(schema, indent=2) + "\n", encoding="utf-8")
        self.assertTrue(any("required fields differ" in error for error in catalog_tool.validate_schema(root)))
        schema = json.loads(
            (ROOT / "catalog" / "schema.json").read_text(encoding="utf-8")
        )
        schema["$defs"]["safePath"]["pattern"] = r".+"
        schema_path.write_text(json.dumps(schema, indent=2) + "\n", encoding="utf-8")
        self.assertTrue(
            any(
                "safePath pattern differs" in error
                for error in catalog_tool.validate_schema(root)
            )
        )

    def test_generated_markdown_is_deterministic_and_staleness_is_detected(self) -> None:
        root = self.make_root()
        first = catalog_tool.generated_files(root)
        second = catalog_tool.generated_files(root)
        self.assertEqual(first, second)
        catalog_tool.write_generated(root)
        self.assertEqual(catalog_tool.check_generated(root), [])
        index = root / "languages" / "README.md"
        index.write_text("stale\n", encoding="utf-8")
        self.assertIn("stale generated file: languages/README.md", catalog_tool.check_generated(root))

    def test_no_active_entry_contains_sdc_or_top_level_start_here(self) -> None:
        languages = json.loads((ROOT / "catalog" / "languages.json").read_text(encoding="utf-8"))["languages"]
        for language in languages:
            data = json.loads((ROOT / "catalog" / f"{language['slug']}.json").read_text(encoding="utf-8"))
            self.assertEqual(data["schema_version"], 2)
            for entry in data["repositories"]:
                self.assertNotIn("sdc", entry)
                self.assertNotIn("start_here", entry)

    def test_multi_license_evidence_is_representable(self) -> None:
        shelf = json.loads((ROOT / "catalog" / "dart.json").read_text(encoding="utf-8"))
        entry = next(item for item in shelf["repositories"] if item["repository"] == "dart-lang/shelf")
        self.assertEqual(entry["license"]["spdx"], "Apache-2.0 AND BSD-3-Clause")
        self.assertGreaterEqual(len(entry["license"]["urls"]), 2)


if __name__ == "__main__":
    unittest.main()

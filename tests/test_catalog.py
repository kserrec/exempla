from __future__ import annotations

import importlib.util
import json
import re
import tempfile
import unittest
from collections import Counter
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
        "path_slug": "request-transformation",
        "repository": repository,
        "url": f"https://github.com/{repository}",
        "primary_language": "Python",
        "language_evidence": "The src directory contains the first-party Python implementation.",
        "description": "A real command-line tool that performs useful production work.",
        "source_kind": "production",
        "purpose_evidence": "Published releases are used as a command-line utility by real users.",
        "why_study": "The path demonstrates a complete request, validation, and transformation boundary.",
        "learn": ["Understand how a command request becomes a tested observable result."],
        "prerequisites": ["Basic Python functions, modules, collections, and exceptions."],
        "concepts_developed": [
            "Explicit request validation and transformation boundaries."
        ],
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
        "novice_accessibility": {
            "floor": 1,
            "central_concepts": ["Direct request validation and transformation."],
            "incidental_concepts": ["The command adapter around the focused function."],
            "reason": "All central ideas are in the novice baseline and the local adapter needs only a short explanation.",
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
            (4, 1, 1, 1): 3,
            (4, 2, 1, 2): 3,
            (4, 4, 1, 1): 3,
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

    def test_required_accessibility_floor_examples(self) -> None:
        cases = {
            (1, 1): 1,
            (1, 2): 2,
            (1, 3): 3,
            (2, 1): 2,
            (2, 2): 2,
            (2, 3): 3,
        }
        for inputs, expected in cases.items():
            with self.subTest(inputs=inputs):
                self.assertEqual(
                    catalog_tool.calculate_published_level(*inputs), expected
                )

    def test_invalid_accessibility_floor_inputs_are_rejected(self) -> None:
        for inputs in ((0, 1), (6, 1), (1, 0), (1, 4), (1, 1.5), (1, True)):
            with self.subTest(inputs=inputs):
                with self.assertRaises(ValueError):
                    catalog_tool.calculate_published_level(*inputs)


class RecordValidationTests(unittest.TestCase):
    language = {"slug": "python", "name": "Python"}

    def validate(
        self,
        entry: dict,
        seen_paths: set[tuple[str, str]] | None = None,
        repository_counts: Counter[str] | None = None,
        seen_buckets: set[tuple[str, int, str]] | None = None,
        seen_slugs: set[str] | None = None,
    ) -> list[str]:
        return catalog_tool.validate_repository(
            entry,
            self.language,
            0,
            seen_paths if seen_paths is not None else set(),
            repository_counts if repository_counts is not None else Counter(),
            seen_buckets if seen_buckets is not None else set(),
            seen_slugs if seen_slugs is not None else set(),
        )

    def test_valid_record_passes_and_renders_learning_evidence(self) -> None:
        entry = valid_entry()
        entry["coding_relevance"]["domain_context"] = [
            "A command adapter turns user input into a request for the focused function."
        ]
        self.assertEqual(self.validate(entry), [])
        rendered = "\n".join(catalog_tool.render_repository(entry))
        self.assertIn("Language 1 / Behavior 1 / Design 1 / Constraints 1 → Level 1", rendered)
        self.assertIn("**Source:** Production software", rendered)
        self.assertIn("**Purpose evidence:**", rendered)
        self.assertIn("**Coding relevance:**", rendered)
        self.assertIn("**Concepts this path develops:**", rendered)
        self.assertIn("**Learning path:**", rendered)
        self.assertIn("**Short context:**", rendered)
        self.assertIn("**Novice accessibility floor 1:**", rendered)
        self.assertIn("**Central concepts:**", rendered)
        self.assertIn("**Incidental concepts:**", rendered)
        self.assertIn("<details>", rendered)
        self.assertIn("<summary>Quality and review evidence</summary>", rendered)
        self.assertIn("tests/test_tool.py", rendered)

    def test_level_two_renders_an_understandable_accessibility_explanation(self) -> None:
        entry = valid_entry()
        for dimension in catalog_tool.DIMENSION_FIELDS:
            entry["learning_level"][dimension]["score"] = 2
        entry["learning_level"]["level"] = 2
        entry["novice_accessibility"] = {
            "floor": 2,
            "central_concepts": ["A callback-based request boundary."],
            "incidental_concepts": ["One dictionary comprehension."],
            "reason": "The callback is a common professional concept and the entry primer is enough to trace it.",
        }
        self.assertEqual(self.validate(entry), [])
        rendered = "\n".join(catalog_tool.render_repository(entry))
        self.assertIn("**Novice accessibility floor 2:**", rendered)
        self.assertIn("A callback-based request boundary.", rendered)
        self.assertIn("One dictionary comprehension.", rendered)

    def test_missing_and_obsolete_fields_fail(self) -> None:
        missing = valid_entry()
        del missing["description"]
        self.assertTrue(any("missing fields description" in error for error in self.validate(missing)))
        obsolete = valid_entry()
        obsolete["sdc"] = {"level": 1}
        self.assertTrue(any("unexpected fields sdc" in error for error in self.validate(obsolete)))

    def test_source_kind_and_purpose_evidence_are_required(self) -> None:
        missing_kind = valid_entry()
        del missing_kind["source_kind"]
        self.assertTrue(
            any("missing fields source_kind" in error for error in self.validate(missing_kind))
        )
        invalid_kind = valid_entry()
        invalid_kind["source_kind"] = "tutorial"
        self.assertTrue(
            any(
                "expected production or educational-exemplar" in error
                for error in self.validate(invalid_kind)
            )
        )
        missing_purpose = valid_entry()
        del missing_purpose["purpose_evidence"]
        self.assertTrue(
            any(
                "missing fields purpose_evidence" in error
                for error in self.validate(missing_purpose)
            )
        )
        obsolete = valid_entry()
        obsolete["real_world_evidence"] = obsolete.pop("purpose_evidence")
        errors = self.validate(obsolete)
        self.assertTrue(any("missing fields purpose_evidence" in error for error in errors))
        self.assertTrue(any("unexpected fields real_world_evidence" in error for error in errors))

    def test_educational_exemplar_is_allowed_only_at_levels_one_and_two(self) -> None:
        for level in range(1, 6):
            with self.subTest(level=level):
                entry = valid_entry()
                entry["source_kind"] = "educational-exemplar"
                for dimension in catalog_tool.DIMENSION_FIELDS:
                    entry["learning_level"][dimension]["score"] = level
                entry["learning_level"]["level"] = level
                if level <= 2:
                    entry["novice_accessibility"]["floor"] = level
                else:
                    del entry["novice_accessibility"]
                errors = self.validate(entry)
                if level <= 2:
                    self.assertEqual(errors, [])
                    rendered = "\n".join(catalog_tool.render_repository(entry))
                    self.assertIn("**Source:** Educational exemplar", rendered)
                    self.assertIn("gentler path", rendered)
                else:
                    self.assertTrue(
                        any(
                            f"may publish only at Level 1 or 2, not Level {level}" in error
                            for error in errors
                        )
                    )

    def test_production_source_is_allowed_at_every_level(self) -> None:
        for level in range(1, 6):
            with self.subTest(level=level):
                entry = valid_entry()
                for dimension in catalog_tool.DIMENSION_FIELDS:
                    entry["learning_level"][dimension]["score"] = level
                entry["learning_level"]["level"] = level
                if level <= 2:
                    entry["novice_accessibility"]["floor"] = level
                else:
                    del entry["novice_accessibility"]
                self.assertEqual(self.validate(entry), [])

    def test_path_slug_is_required_and_must_be_canonical(self) -> None:
        missing = valid_entry()
        del missing["path_slug"]
        self.assertTrue(any("missing fields path_slug" in error for error in self.validate(missing)))
        invalid = valid_entry()
        invalid["path_slug"] = "Not Stable"
        self.assertTrue(any("path_slug: use lowercase" in error for error in self.validate(invalid)))

    def test_duplicate_repository_and_path_slug_fails(self) -> None:
        seen_paths: set[tuple[str, str]] = set()
        repository_counts: Counter[str] = Counter()
        seen_buckets: set[tuple[str, int, str]] = set()
        seen_slugs: set[str] = set()
        self.assertEqual(
            self.validate(
                valid_entry(), seen_paths, repository_counts, seen_buckets, seen_slugs
            ),
            [],
        )
        duplicate = valid_entry()
        duplicate["slug"] = "real-tool-duplicate"
        errors = self.validate(
            duplicate, seen_paths, repository_counts, seen_buckets, seen_slugs
        )
        self.assertTrue(any("duplicate catalog path" in error for error in errors))

    def test_same_repository_may_supply_two_paths_at_different_levels(self) -> None:
        seen_paths: set[tuple[str, str]] = set()
        repository_counts: Counter[str] = Counter()
        seen_buckets: set[tuple[str, int, str]] = set()
        seen_slugs: set[str] = set()
        first = valid_entry()
        second = valid_entry()
        second["slug"] = "real-tool-advanced"
        second["path_slug"] = "advanced-request-lifecycle"
        for dimension in catalog_tool.DIMENSION_FIELDS:
            second["learning_level"][dimension]["score"] = 2
        second["learning_level"]["level"] = 2
        for entry in (first, second):
            self.assertEqual(
                self.validate(
                    entry, seen_paths, repository_counts, seen_buckets, seen_slugs
                ),
                [],
            )

    def test_third_path_from_one_repository_fails(self) -> None:
        seen_paths: set[tuple[str, str]] = set()
        repository_counts: Counter[str] = Counter()
        seen_buckets: set[tuple[str, int, str]] = set()
        seen_slugs: set[str] = set()
        for level in (1, 2, 3):
            entry = valid_entry()
            entry["slug"] = f"real-tool-{level}"
            entry["path_slug"] = f"request-path-{level}"
            for dimension in catalog_tool.DIMENSION_FIELDS:
                entry["learning_level"][dimension]["score"] = level
            entry["learning_level"]["level"] = level
            errors = self.validate(
                entry, seen_paths, repository_counts, seen_buckets, seen_slugs
            )
        self.assertTrue(any("exceeds the two-path" in error for error in errors))

    def test_same_repository_twice_in_one_language_level_fails(self) -> None:
        seen_paths: set[tuple[str, str]] = set()
        repository_counts: Counter[str] = Counter()
        seen_buckets: set[tuple[str, int, str]] = set()
        seen_slugs: set[str] = set()
        self.assertEqual(
            self.validate(
                valid_entry(), seen_paths, repository_counts, seen_buckets, seen_slugs
            ),
            [],
        )
        second = valid_entry()
        second["slug"] = "real-tool-second"
        second["path_slug"] = "second-request-path"
        errors = self.validate(
            second, seen_paths, repository_counts, seen_buckets, seen_slugs
        )
        self.assertTrue(any("appears twice in Python Level 1" in error for error in errors))

    def test_concepts_developed_are_required_and_distinct(self) -> None:
        missing = valid_entry()
        del missing["concepts_developed"]
        self.assertTrue(
            any("missing fields concepts_developed" in error for error in self.validate(missing))
        )
        overlap = valid_entry()
        overlap["concepts_developed"] = [overlap["prerequisites"][0]]
        self.assertTrue(
            any("duplicates a prerequisite" in error for error in self.validate(overlap))
        )

    def test_score_range_and_formula_are_enforced(self) -> None:
        invalid = valid_entry()
        invalid["learning_level"]["language_technique"]["score"] = 6
        self.assertTrue(any("integer from 1 through 5" in error for error in self.validate(invalid)))
        mismatch = valid_entry()
        mismatch["learning_level"]["level"] = 3
        self.assertTrue(any("require Level 1, not 3" in error for error in self.validate(mismatch)))

    def test_low_rubric_level_requires_accessibility_evidence(self) -> None:
        entry = valid_entry()
        del entry["novice_accessibility"]
        self.assertTrue(
            any(
                "novice_accessibility: required when rubric Level is 1" in error
                for error in self.validate(entry)
            )
        )

    def test_structural_level_three_does_not_require_accessibility_evidence(self) -> None:
        entry = valid_entry()
        del entry["novice_accessibility"]
        for dimension in catalog_tool.DIMENSION_FIELDS:
            entry["learning_level"][dimension]["score"] = 3
        entry["learning_level"]["level"] = 3
        self.assertEqual(self.validate(entry), [])

    def test_accessibility_floor_shape_and_range_are_enforced(self) -> None:
        for floor in (0, 4, 1.5, True):
            with self.subTest(floor=floor):
                entry = valid_entry()
                entry["novice_accessibility"]["floor"] = floor
                self.assertTrue(
                    any("expected integer from 1 through 3" in error for error in self.validate(entry))
                )

        missing = valid_entry()
        del missing["novice_accessibility"]["reason"]
        self.assertTrue(any("missing fields reason" in error for error in self.validate(missing)))

        malformed = valid_entry()
        malformed["novice_accessibility"]["central_concepts"] = "validation"
        self.assertTrue(any("expected at least 0 text item" in error for error in self.validate(malformed)))

    def test_published_level_must_equal_rubric_level_or_accessibility_floor(self) -> None:
        promoted = valid_entry()
        promoted["novice_accessibility"]["floor"] = 3
        promoted["learning_level"]["level"] = 3
        self.assertEqual(self.validate(promoted), [])

        contradicted = valid_entry()
        contradicted["novice_accessibility"]["floor"] = 3
        self.assertTrue(
            any(
                "rubric Level 1 and accessibility floor 3 require Level 3, not 1"
                in error
                for error in self.validate(contradicted)
            )
        )

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
    def make_root(self, *, empty: bool = False, schema_version: int = 5) -> Path:
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
            "learner-centered-remediation.json",
            "lower-level-expansion.json",
            "lower-level-expansion-audit.json",
            "novice-accessibility-audit.json",
            "rejections.json",
        ):
            (research / name).write_text(
                (ROOT / "research" / name).read_text(encoding="utf-8"),
                encoding="utf-8",
            )

    def test_current_catalog_schema_and_rebuild_audit_reconcile(self) -> None:
        self.assertEqual(catalog_tool.validate_catalog(ROOT), [])

    def test_lower_level_expansion_audit_reconciles_counts_and_educational_gate(self) -> None:
        root = self.make_root()
        self.add_research(root)
        audit_path = root / "research" / "lower-level-expansion-audit.json"
        audit = json.loads(audit_path.read_text(encoding="utf-8"))
        audit["after"]["accepted_paths"] += 1
        audit_path.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
        self.assertTrue(
            any(
                ".after: does not match the canonical catalog" in error
                for error in catalog_tool.validate_catalog(root)
            )
        )

        audit = json.loads(
            (ROOT / "research" / "lower-level-expansion-audit.json").read_text(
                encoding="utf-8"
            )
        )
        audit["educational_exemplars"][0]["qualification"]["complete_artifact"][
            "pass"
        ] = False
        audit_path.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
        self.assertTrue(
            any(
                "every educational gate must pass" in error
                for error in catalog_tool.validate_catalog(root)
            )
        )

    def test_historical_lower_gap_counts_are_not_coupled_to_later_additions(self) -> None:
        root = self.make_root()
        self.add_research(root)
        novice_audit = json.loads(
            (root / "research" / "novice-accessibility-audit.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(
            novice_audit["replacement_research"][0]["open_levels_after"],
            {"1": 1, "2": 2},
        )
        current_javascript = json.loads(
            (root / "catalog" / "javascript.json").read_text(encoding="utf-8")
        )
        current_gaps = {
            str(level): 3
            - sum(
                entry["learning_level"]["level"] == level
                for entry in current_javascript["repositories"]
            )
            for level in (1, 2)
        }
        self.assertEqual(current_gaps, {"1": 1, "2": 1})
        self.assertEqual(catalog_tool.validate_catalog(root), [])

        novice_audit["replacement_research"][0]["open_levels_after"] = current_gaps
        novice_path = root / "research" / "novice-accessibility-audit.json"
        novice_path.write_text(
            json.dumps(novice_audit, indent=2) + "\n", encoding="utf-8"
        )
        self.assertTrue(
            any(
                "differs from historical audited outcomes" in error
                for error in catalog_tool.validate_catalog(root)
            )
        )

    def test_distinct_later_path_in_a_removed_repository_is_allowed(self) -> None:
        root = self.make_root()
        self.add_research(root)
        self.assertEqual(catalog_tool.validate_catalog(root), [])

        path = root / "catalog" / "javascript.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        express = next(
            entry
            for entry in data["repositories"]
            if entry["repository"] == "expressjs/express"
        )
        express["learning_path"]["start_here"]["path"] = "lib/application.js"
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        self.assertTrue(
            any(
                "removed repository path is still accepted: expressjs/express" in error
                for error in catalog_tool.validate_catalog(root)
            )
        )

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

    def test_gap_candidate_evidence_fields_are_validated(self) -> None:
        mutations = (
            ("missing inspection files", lambda candidate: candidate.pop("inspection_files"), "missing fields inspection_files"),
            ("invalid pin", lambda candidate: candidate.__setitem__("pinned_commit", "main"), "40 lowercase hexadecimal"),
            ("dotenv inspection", lambda candidate: candidate["inspection_files"].append("config/.env.local"), "canonical safe non-dotenv"),
            ("unknown channel", lambda candidate: candidate["discovered_via"].append("invented-channel"), "unknown channel id"),
            ("invalid coding gate", lambda candidate: candidate.__setitem__("coding_relevance_status", "unknown"), "coding_relevance_status: expected pass or fail"),
            ("invalid quality gate", lambda candidate: candidate.__setitem__("quality_status", "unknown"), "quality_status: expected pass or fail"),
            ("missing second review", lambda candidate: candidate.pop("second_review"), "missing fields second_review"),
        )
        for label, mutate, expected in mutations:
            with self.subTest(label=label):
                root = self.make_root()
                self.add_research(root)
                gap_path = root / "research" / "learner-centered-gap-research.json"
                audit = json.loads(gap_path.read_text(encoding="utf-8"))
                mutate(audit["languages"][1]["candidates"][0])
                gap_path.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
                self.assertTrue(
                    any(expected in error for error in catalog_tool.validate_catalog(root)),
                    expected,
                )

    def test_hard_gate_rejection_is_unscored_but_qualified_candidate_is_scored(self) -> None:
        root = self.make_root()
        self.add_research(root)
        gap_path = root / "research" / "learner-centered-gap-research.json"
        audit = json.loads(gap_path.read_text(encoding="utf-8"))
        candidate = audit["languages"][1]["candidates"][0]
        candidate["coding_relevance_status"] = "fail"
        candidate.pop("scores")
        candidate.pop("calculated_level")
        gap_path.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
        self.assertEqual(catalog_tool.validate_catalog(root), [])

        candidate["coding_relevance_status"] = "pass"
        gap_path.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
        self.assertTrue(
            any(
                "missing fields scores, calculated_level" in error
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

    def test_novice_audit_reconciles_levels_capacity_and_safe_source_paths(self) -> None:
        root = self.make_root()
        self.add_research(root)
        audit_path = root / "research" / "novice-accessibility-audit.json"
        audit = json.loads(audit_path.read_text(encoding="utf-8"))

        audit["records"][0]["final_level"] = 1
        audit_path.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
        self.assertTrue(
            any(
                "must equal max(rubric level, floor)" in error
                for error in catalog_tool.validate_catalog(root)
            )
        )

        audit = json.loads(
            (ROOT / "research" / "novice-accessibility-audit.json").read_text(
                encoding="utf-8"
            )
        )
        audit["records"][0]["source_files_inspected"].append("config/.env.local")
        audit_path.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
        self.assertTrue(
            any(
                "expected canonical safe non-dotenv relative path" in error
                for error in catalog_tool.validate_catalog(root)
            )
        )

    def test_schema_version_four_is_rejected(self) -> None:
        root = self.make_root(empty=True, schema_version=4)
        errors = catalog_tool.validate_catalog(root)
        self.assertTrue(any("schema_version: expected 5" in error for error in errors))

    def test_incomplete_catalog_is_valid_but_not_complete(self) -> None:
        root = self.make_root(empty=True)
        self.assertEqual(catalog_tool.validate_catalog(root), [])
        errors = catalog_tool.validate_catalog(root, complete=True)
        self.assertTrue(any("complete catalog requires 240 learning paths; found 0" in error for error in errors))
        self.assertTrue(any("Level 1 requires 3 entries" in error for error in errors))
        self.assertTrue(any("Level 2 requires 3 entries" in error for error in errors))
        self.assertTrue(any("Level 3 requires 2 entries" in error for error in errors))

    def test_capacity_map_is_enforced(self) -> None:
        self.assertEqual(catalog_tool.LEVEL_CAPACITY, {1: 3, 2: 3, 3: 2, 4: 2, 5: 2})
        for level, capacity in catalog_tool.LEVEL_CAPACITY.items():
            with self.subTest(level=level):
                root = self.make_root(empty=True)
                entries = []
                for index in range(capacity + 1):
                    entry = valid_entry()
                    repository = f"example/level-{level}-tool-{index}"
                    entry["slug"] = f"level-{level}-tool-{index}"
                    entry["path_slug"] = f"level-{level}-path-{index}"
                    entry["repository"] = repository
                    entry["url"] = f"https://github.com/{repository}"
                    entry["license"]["urls"] = [
                        f"https://github.com/{repository}/blob/{entry['inspection']['commit']}/LICENSE"
                    ]
                    for dimension in catalog_tool.DIMENSION_FIELDS:
                        entry["learning_level"][dimension]["score"] = level
                    entry["learning_level"]["level"] = level
                    if level <= 2:
                        entry["novice_accessibility"]["floor"] = level
                    else:
                        del entry["novice_accessibility"]
                    entries.append(entry)
                path = root / "catalog" / "python.json"
                data = json.loads(path.read_text(encoding="utf-8"))
                data["repositories"] = entries[:capacity]
                path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
                self.assertEqual(catalog_tool.validate_catalog(root), [])
                data["repositories"] = entries
                path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
                self.assertTrue(
                    any(
                        f"Level {level} has {capacity + 1} entries; maximum is {capacity}"
                        in error
                        for error in catalog_tool.validate_catalog(root)
                    )
                )

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
        schema["$defs"]["repository"]["required"].remove("path_slug")
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

    def test_active_entries_use_current_schema_and_baseline_paths_stay_production(self) -> None:
        languages = json.loads((ROOT / "catalog" / "languages.json").read_text(encoding="utf-8"))["languages"]
        expansion = json.loads(
            (ROOT / "research" / "lower-level-expansion-audit.json").read_text(
                encoding="utf-8"
            )
        )
        added_paths = {
            (record["repository"].lower(), record["path_slug"])
            for record in expansion["additions"]["paths"]
        }
        educational_additions = {
            (record["repository"].lower(), record["path_slug"])
            for record in expansion["additions"]["paths"]
            if record["source_kind"] == "educational-exemplar"
        }
        for language in languages:
            data = json.loads((ROOT / "catalog" / f"{language['slug']}.json").read_text(encoding="utf-8"))
            self.assertEqual(data["schema_version"], 5)
            for entry in data["repositories"]:
                self.assertNotIn("sdc", entry)
                self.assertNotIn("start_here", entry)
                self.assertIn("purpose_evidence", entry)
                self.assertNotIn("real_world_evidence", entry)
                key = (entry["repository"].lower(), entry["path_slug"])
                if key not in added_paths:
                    self.assertEqual(entry["source_kind"], "production")
                if entry["source_kind"] == "educational-exemplar":
                    self.assertIn(key, educational_additions)
                    self.assertLessEqual(entry["learning_level"]["level"], 2)

    def test_multi_license_evidence_is_representable(self) -> None:
        shelf = json.loads((ROOT / "catalog" / "dart.json").read_text(encoding="utf-8"))
        entry = next(item for item in shelf["repositories"] if item["repository"] == "dart-lang/shelf")
        self.assertEqual(entry["license"]["spdx"], "Apache-2.0 AND BSD-3-Clause")
        self.assertGreaterEqual(len(entry["license"]["urls"]), 2)


if __name__ == "__main__":
    unittest.main()

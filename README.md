# Exempla

[![Validate catalog](https://github.com/kserrec/exempla/actions/workflows/validate.yml/badge.svg)](https://github.com/kserrec/exempla/actions/workflows/validate.yml)

Learn programming from real examples at your level.

Pick a language, choose Level 1 through 5 (novice to advanced), and follow one
small reviewed path through exact implementation lines and focused tests. Level
1 is for someone who has completed an introductory tutorial and written small
programs; Level 5 reaches expert production systems.

**[Choose a language and start here.](languages/README.md)** On its language
page, begin with the entry marked **Recommended first path**.

**You are not expected to understand the whole repository.** Each entry gives
you one bounded behavior, exact starting lines, and the relevant tests. The rest
of the codebase can wait.

Exempla is a curated, GitHub-native catalog of public open-source software. It
currently has
**158 qualified learning paths from 148 public repositories across 20
languages**. Its **82 open slots are honest research gaps** under the expanded
3/3/2/2/2 capacity map, including 42 Level 1 gaps and 34 Level 2 gaps after the
completed production and educational-exemplar research passes. Seventeen of 20
languages now have at least one qualified path at each of Levels 1 and 2. No
gate or score is lowered to preserve an arbitrary count.

Levels 1 and 2 may include carefully selected educational exemplars. Real
production code often assumes professional concepts before a novice has had a
chance to learn them, so requiring production use at every Level left the
beginning of the ladder nearly empty. Exempla keeps the same strict difficulty
and novice-accessibility standards while allowing complete, high-quality
teaching artifacts to bridge that gap. Every entry visibly identifies its
source type. From Level 3 onward, every path is production software.

## Browse the catalog

[Choose a language](languages/README.md). Every Level 1 and Level 2 entry puts
the first action before the research detail:

- whether the source is production software or an educational exemplar;
- a concise **Just start** instruction;
- the exact pinned source lines to open and their initial line count;
- the bounded behavior, prerequisites, concepts developed, focused tests, and
  an entry-to-result trace;
- a concise Level explanation and license; and
- collapsed scoring, coding-relevance, source-quality, inspection, and license
  evidence for readers who want to audit the decision.

Exempla links to upstream projects; it does not copy their source. Path and
license links are pinned so the review stays reproducible when a default branch
moves.

## How levels work

Exempla ranks the transferable programming skill needed to understand the
published path—not repository size, popularity, product importance, or outside
subject-matter prestige.

- **Language technique:** fluency beyond basic syntax.
- **Behavioral reasoning:** control flow, state, time, failure, and resources.
- **Design span:** how many meaningful boundaries the path crosses.
- **Constraint burden:** the guarantees a correct change must preserve.

Each dimension is an integer from 1 through 5. Their arithmetic mean rounds
halves upward. One score of 4 forces at least Level 3, one score of 5 forces at
least Level 4, and Level 5 requires a rounded mean of 5 plus at least two scores
of 5. This produces the rubric Level. When it is 1 or 2, a separate
novice-accessibility floor prevents a mechanically small path from hiding a
large conceptual prerequisite; the published Level is the higher result. The
floor is not averaged into the four scores. The complete anchors,
accessibility tests, and coding-relevance gate are in the
[learning-level rubric](docs/learning-levels.md). Repository quality remains a
separate [pass/fail gate](docs/qualification.md).

The learner-facing rungs are **Level 1 — First real code**, **Level 2 — Guided
real-world patterns**, **Level 3 — Intermediate production software**, **Level
4 — Advanced**, and **Level 5 — Expert**.

## How to study an entry

1. Follow **Just start** and open the exact pinned source lines.
2. Predict what the bounded behavior will do before reading the focused tests.
3. Use the goal, prerequisites, and trace only when you need orientation.
4. Use the quality evidence as review questions: are responsibilities clear,
   failures explicit, and contracts protected?
5. Move upward when the current Level feels navigable; Levels guide learning,
   not prestige.

## Trust and transparency

- [Language selection](docs/language-selection.md) records the dated scope.
- [Candidate research](docs/research-process.md) requires three independent
  discovery channels and pinned-source inspection before scoring.
- [Learning-level calibration](docs/learning-level-calibration.md) records the
  smoke test and completed corpus-wide consistency pass.
- [The v1 re-review](research/learner-centered-rebuild.json) preserves all 200
  retain/remove decisions and their recorded review passes.
- [The remediation record](research/learner-centered-remediation.json) preserves
  the verified 150-path baseline, the concurrent APISIX result, 56 targeted
  claim-to-source checks, and the Level 1 follow-up for every affected language.
- [The current corpus audit](research/learner-centered-audit.json) reconciles
  counts, identities, guardrails, metadata, licenses, generated pages, source
  claims, and neighboring-level comparisons.
- [The novice-accessibility audit](research/novice-accessibility-audit.json)
  records every starting Level 1 and Level 2 judgment, all five accessibility
  tests, capacity alternates, conditional replacement passes, and progression
  sanity checks.
- [The lower-level expansion audit](research/lower-level-expansion-audit.json)
  reconciles the 125-path baseline, 27 accepted additions, all 20 language
  passes, educational qualification, serious rejections, progression, source-
  class leakage, and 82 remaining lower-level gaps.
- [The learner-usability audit](research/learner-usability-audit.json) records
  the pre-polish first-click baseline, every lower-level range, simulated novice
  journeys, progression checks, narrow-width review, and after-state findings.
- [Rejected candidates](research/rejections.json) are append-only.
- [`research/audit.json`](research/audit.json) is the historical v1 corpus
  audit; it is no longer the active consistency record.
- Canonical schema-version-5 JSON under [`catalog/`](catalog/README.md)
  deterministically generates every language page.

Automation validates local structure, formulas, reconciliation, and generated
output. Source inspection and admission, rejection, and scoring judgments are
AI-assisted in the current corpus; the project owner directed the process and
accepted the resulting catalog. Inspection records name the actual review
passes, and no independent human review is implied.

## Current learner-centered expansion

The prior lower-rung review inspected all 3 starting Level 1 paths and all 35
starting Level 2 paths at their exact pins. The educational-exemplar expansion
preserves that strict learner baseline and accessibility floor while opening a
third target slot at Levels 1 and 2. Educational source must pass its own
complete-artifact gate and may never publish above Level 2.

## Contributing

Corrections, inspected candidates, and maintenance improvements are welcome.
Read [CONTRIBUTING.md](CONTRIBUTING.md) or use the
[structured issue chooser](https://github.com/kserrec/exempla/issues/new/choose).

Validation and generation use only Python's standard library. Continuous
integration runs tests, gap-tolerant catalog validation, and generated-output
checks. `--complete` remains available and is used only when every one of the
240 possible slots is genuinely filled.

## License

Exempla's original catalog text and tooling are released under the
[MIT License](LICENSE). Each linked repository remains governed by the license
recorded at its inspected revision.

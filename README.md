# Exempla

[![Validate catalog](https://github.com/kserrec/exempla/actions/workflows/validate.yml/badge.svg)](https://github.com/kserrec/exempla/actions/workflows/validate.yml)

Learn transferable programming skills from exemplary real-world source code.

Exempla is a curated, GitHub-native catalog of public open-source software.
Choose a language and a learner Level from 1 through 5, then follow one concrete
path through production implementation and tests. The catalog currently has
**125 qualified learning paths from 124 public repositories across 20
languages**. Its **75 open slots are honest research gaps** after the completed
learner-centered re-review, novice-accessibility audit, and documented gap
research. No gate or score is lowered to preserve an arbitrary count.

If you can write small programs in the language, **Level 1 — First real code**
is designed to be your first comfortable step into production source. An empty
Level 1 does not mean you should simply jump to Level 2; it means Exempla has
not yet found a path gentle enough to publish there.

## Browse the catalog

[Choose a language](languages/README.md). Each entry records:

- the real behavior the learner will understand;
- the first source file to open, supporting implementation and test files, and
  an entry-to-result trace;
- prerequisites, concepts developed by the path, and any short domain context;
- the coding-relevance and eight-part repository-quality evidence;
- four path-centered scores and the resulting Level;
- for structurally low-level paths, the central and incidental concepts plus a
  novice-accessibility judgment;
- the exact inspected commit and files; and
- one or more pinned license-evidence links.

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
real-world code**, **Level 3 — Intermediate**, **Level 4 — Advanced**, and
**Level 5 — Expert**.

## How to study an entry

1. Read the goal, prerequisites, and short domain context.
2. Open the pinned **Start here** file.
3. Follow the published trace through its supporting implementation and tests.
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
- [Rejected candidates](research/rejections.json) are append-only.
- [`research/audit.json`](research/audit.json) is the historical v1 corpus
  audit; it is no longer the active consistency record.
- Canonical schema-version-4 JSON under [`catalog/`](catalog/README.md)
  deterministically generates every language page.

Automation validates local structure, formulas, reconciliation, and generated
output. Source inspection and admission, rejection, and scoring judgments are
AI-assisted in the current corpus; the project owner directed the process and
accepted the resulting catalog. Inspection records name the actual review
passes, and no independent human review is implied.

## Current learner-centered refinement

The lower-rung review inspected all 3 starting Level 1 paths and all 35
starting Level 2 paths at their exact pins. It retained the four structural
scores, added a separate novice-accessibility floor, promoted 29 concept-heavy
paths to Level 3, and resolved Level 3 capacity only after those judgments were
fixed. Twenty-eight qualified overflow paths remain preserved as restorable
capacity alternates. Current exact-pin gap evidence yielded two honest Level 2
replacements—Humanizer string truncation for C# and inih's line-oriented parser
for C—while every other lower-level gap remains visible.

## Contributing

Corrections, inspected candidates, and maintenance improvements are welcome.
Read [CONTRIBUTING.md](CONTRIBUTING.md) or use the
[structured issue chooser](https://github.com/kserrec/exempla/issues/new/choose).

Validation and generation use only Python's standard library. Continuous
integration runs tests, gap-tolerant catalog validation, and generated-output
checks. `--complete` remains available and is used only when every one of the
200 possible slots is genuinely filled.

## License

Exempla's original catalog text and tooling are released under the
[MIT License](LICENSE). Each linked repository remains governed by the license
recorded at its inspected revision.

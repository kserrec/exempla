# Exempla

[![Validate catalog](https://github.com/kserrec/exempla/actions/workflows/validate.yml/badge.svg)](https://github.com/kserrec/exempla/actions/workflows/validate.yml)

Learn transferable programming skills from exemplary real-world source code.

Exempla is a curated, GitHub-native catalog of public open-source software.
Choose a language and a learner Level from 1 through 5, then follow one concrete
path through production implementation and tests. The catalog currently has
**138 qualified repositories across 20 languages**. Its **62 open slots are
honest research gaps** after the learner-centered re-review and the completed
JavaScript, Python, Java, PHP, and C# replacement-research passes; no standard
is lowered to preserve an arbitrary count.

## Browse the catalog

[Choose a language](languages/README.md). Each entry records:

- the real behavior the learner will understand;
- the first source file to open, supporting implementation and test files, and
  an entry-to-result trace;
- prerequisites and any short domain context;
- the coding-relevance and eight-part repository-quality evidence;
- four path-centered scores and the resulting Level;
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
halves upward; one score of 5 forces at least Level 4, and Level 5 requires a
rounded mean of 5 plus at least two scores of 5. The complete anchors and
coding-relevance gate are in the [learning-level rubric](docs/learning-levels.md).
Repository quality remains a separate [pass/fail gate](docs/qualification.md).

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
  discovery channels and human inspection before scoring.
- [Learning-level calibration](docs/learning-level-calibration.md) records the
  smoke test and final consistency method.
- [The v1 re-review](research/learner-centered-rebuild.json) preserves all 200
  retain/remove decisions and their independent reviews.
- [Rejected candidates](research/rejections.json) are append-only.
- [`research/audit.json`](research/audit.json) is the historical v1 corpus
  audit; a final learner-centered audit will replace its active role after gap
  research.
- Canonical schema-version-2 JSON under [`catalog/`](catalog/README.md)
  deterministically generates every language page.

Automation validates local structure, formulas, reconciliation, and generated
output. Human inspection establishes public facts and makes admission,
rejection, and scoring decisions.

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

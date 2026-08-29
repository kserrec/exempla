# Exempla

[![Validate catalog](https://github.com/kserrec/exempla/actions/workflows/validate.yml/badge.svg)](https://github.com/kserrec/exempla/actions/workflows/validate.yml)

Learn programming from exemplary real-world source code.

Exempla is a curated, GitHub-native catalog of public open-source software.
Choose a programming language, choose an SDC difficulty level, and find two
codebases worth reading at that stage of your learning. The initial catalog
contains **200 repositories across 20 languages**.

## Browse the catalog

[Choose a language](languages/README.md), then work from SDC 1 toward SDC 5 at
the pace that fits you. Every entry explains:

- what the software does and why it is real-world software;
- what its source can teach you;
- what you should know first;
- the file where reading should begin;
- why its size, code difficulty, and system complexity produce that level;
- the source, architecture, test, documentation, traceability, maintenance, and
  educational evidence behind its admission; and
- the exact commit, sampled files, LOC exclusions, and license reviewed.

Exempla links to upstream projects; it does not copy or mirror their source.
Start and license links are pinned to the inspected commit so the written
reasoning remains reproducible when an upstream default branch changes.

## How SDC works

SDC keeps three different questions visible:

- **S — Size:** how much meaningful first-party implementation code must be
  navigated?
- **D — Difficulty:** how demanding is the code itself to understand?
- **C — Complexity:** how demanding is the software as a whole system?

The three integer scores produce one broad learner-facing level from SDC 1
through SDC 5. Size is measured; difficulty and complexity are evidence-backed
expert judgments. The formula and its two guardrails are deliberately simple
and public in the [SDC rubric](docs/sdc.md).

Difficulty is not quality. A repository is scored only after it passes the
separate [qualification gate](docs/qualification.md). Empty catalog slots never
justify lowering either standard.

## How to study an entry

1. Read the prerequisites and the entry's short description.
2. Open the pinned **Start here** file and trace the behavior named in its
   explanation.
3. Follow that behavior into the sampled implementation and test files.
4. Use the quality evidence as questions to ask while reading: where are the
   boundaries, how are failures represented, and which tests define the
   contract?
5. Move upward only when the current level feels navigable; SDC is a guide, not
   a contest.

## Trust and transparency

The catalog is designed to be auditable without a website or opaque ranking
service:

- [Language selection](docs/language-selection.md) records the dated scope and
  replacement rule.
- [Candidate research](docs/research-process.md) defines discovery, source
  inspection, measurement, review, and refreshes.
- [Calibration](docs/calibration.md) records the initial sample and the final
  200-entry consistency pass.
- [Rejected candidates](research/rejections.json) preserve evidence for
  decisions that did not become entries.
- [The corpus audit](research/audit.json) records live repository, pinned path,
  license, duplication, distribution, navigation, and clean-snapshot results.
- Canonical JSON under [`catalog/`](catalog/README.md) generates every
  learner-facing language page deterministically.

GitHub metadata and automation can verify facts; they never decide whether code
is good or what level it deserves.

## Contributing

Corrections, well-researched candidates, and maintenance improvements are
welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before editing catalog data.
The complete ownership and refresh procedure is in
[docs/maintenance.md](docs/maintenance.md).

The project uses only Python's standard library for validation and generation.
Continuous integration runs the unit tests, requires the complete 200-entry
corpus, and rejects stale generated Markdown.

## License

Exempla's original catalog text and tooling are released under the
[MIT License](LICENSE). Each linked repository remains governed by its own
license, recorded on its entry at the inspected revision.

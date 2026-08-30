# Exempla current plan

Exempla is a learner-centered catalog of pinned real-world source paths. This
is the only current implementation plan; the original Size / Difficulty /
Complexity release plan is historical.

## Current state

- The canonical schema is version 3.
- The catalog contains 150 qualified learning paths from 149 public
  repositories across 20 languages.
- The 200-path grid has 50 documented research gaps. Ordinary validation
  accepts honest gaps; `--complete` is reserved for a genuinely full grid.
- A path is identified by `(repository, path_slug)`. One repository may supply
  at most two materially distinct paths and never two paths in the same
  language/Level bucket.
- Levels come from four path-centered scores. A score of 4 forces at least
  Level 3, a score of 5 forces at least Level 4, and Level 5 requires a rounded
  mean of 5 with at least two scores of 5.
- Prerequisites name prior knowledge; `concepts_developed` names what the path
  teaches.
- The active corpus audit is
  [`research/learner-centered-audit.json`](research/learner-centered-audit.json)
  and currently ends `pass-with-documented-gaps`.

## Completed learner-centered remediation

- [x] Record the verified 150-path starting state and preserve all remediation
  decisions in
  [`research/learner-centered-remediation.json`](research/learner-centered-remediation.json).
- [x] Migrate every accepted entry to stable path identity and enforce global
  uniqueness, repository diversity, and same-bucket rules.
- [x] Add the score-4 floor and tests for every formula guardrail.
- [x] Separate prerequisites from concepts developed across the corpus.
- [x] Correct `r-lib/pkgconfig`, rescore Swift Tagged, and run targeted pinned-
  source claim checks for 55 higher-risk paths.
- [x] Re-research every affected Level 1 gap without lowering admission or
  scoring standards.
- [x] Run live metadata, license, generated-output, distribution, and cross-
  level consistency checks and publish the active audit.
- [x] Make AI-assisted review provenance explicit and collapse detailed audit
  evidence on generated learner pages.
- [x] Replace current-facing Size / Difficulty / Complexity terminology and
  synchronize contributor and maintenance documentation.
- [x] Rerun the final supported test, validation, and generated-output gates
  after documentation synchronization: 30 tests, ordinary validation, and the
  generated-output check all passed on 2026-08-29.

## Ongoing maintenance

1. Correct factual drift only from direct evidence at the exact path and pin.
2. Research open slots through the documented multi-channel process; preserve
   qualified capacity alternates and evidence-backed rejections.
3. Recheck repository status, language labels, pins, paths, and license evidence
   when refreshing an entry or preparing a release.
4. Regenerate language pages with canonical JSON changes and run the ordinary
   verification gates. Use `--complete` only when all 200 paths exist.
5. Treat source quality and pedagogy as review judgments. Name model and human
   review passes literally; automation checks structure and formulas only.
6. Commit, push, tag, or publish only when those release actions are explicitly
   requested.

## Historical record

The `v1.0.0` tag and Git history preserve the original implementation plan and
Size / Difficulty / Complexity methodology. The surviving historical documents
are explicitly labeled by their own context, including [`docs/sdc.md`](docs/sdc.md),
[`docs/calibration.md`](docs/calibration.md), and
[`research/audit.json`](research/audit.json). The learner-centered transition is
specified in
[`LEARNER_CENTERED_REBUILD_SPEC.md`](LEARNER_CENTERED_REBUILD_SPEC.md), with its
decisions preserved under [`research/`](research/README.md).

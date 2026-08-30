# Exempla current plan

Exempla is a learner-centered catalog of pinned exemplary source paths. This
is the only current implementation plan; earlier release and remediation plans
are historical.

## Current state

- The canonical schema is version 5.
- The preserved pre-expansion baseline contains 125 qualified learning paths
  from 124 public repositories across 20 languages.
- The completed expansion catalog plus the follow-up Level 1 and Level 2 breadth
  batches contains 158 paths from 148 repositories: 153 production paths and 5
  educational exemplars. The 240-path 3/3/2/2/2 grid has 82 honest open slots,
  including 42 Level 1 and 34 Level 2 gaps. Seventeen of 20 languages have at
  least one qualified path at each of Levels 1 and 2.
  Ordinary validation accepts those gaps; `--complete` is reserved for a
  genuinely full grid.
- Every accepted path declares `source_kind` and `purpose_evidence`. Production
  software may publish at Levels 1–5; qualified educational exemplars may
  publish only at Levels 1–2.
- A path is identified by `(repository, path_slug)`. One repository may supply
  at most two materially distinct paths and never two paths in the same
  language/Level bucket.
- The four-score rubric, guardrails, novice learner baseline, accessibility
  floor, and five accessibility tests are unchanged.
- [`research/lower-level-expansion.json`](research/lower-level-expansion.json)
  preserves the exact before-state. The completed pass is reconciled in
  [`research/lower-level-expansion-audit.json`](research/lower-level-expansion-audit.json);
  older audits remain historical.

## Active lower-level educational-exemplar expansion

### Phase 1 — Record the new baseline

- [x] Snapshot commit, validation, totals, lower-level counts, gaps, capacity,
  and novice-accessibility policy.

### Phase 2 — Introduce explicit source classes

- [x] Require `source_kind` on every accepted entry.
- [x] Replace `real_world_evidence` with generalized `purpose_evidence`.

### Phase 3 — Define source qualification

- [x] Preserve the production gate.
- [x] Add the ten-part educational-exemplar gate.

### Phase 4 — Update coding relevance

- [x] Admit genuine production behavior or complete intentional lower-level
  educational behavior without weakening the domain gate.

### Phase 5 — Expand capacity

- [x] Implement 3/3/2/2/2 target capacity, repository diversity, and 240-path
  completeness semantics.

### Phase 6 — Update schema, tooling, rendering, and tests

- [x] Migrate every existing accepted path to schema version 5 and
  `source_kind = production` without reclassifying historical entries.
- [x] Enforce source-kind Level restrictions and visibly render provenance.
- [x] Add focused source-kind, migration, and capacity tests.

### Phase 7 — Update methodology and product explanation

- [x] Update current-facing source policy, rubric, research, contribution,
  maintenance, issue, pull-request, and catalog documentation.

### Phase 8 — Define educational discovery and triage

- [x] Add official-example, respected-teaching, small-reference, curated-list,
  and GitHub discovery channels plus explicit early rejections.

### Phase 9 — Run 20 language research passes in catalog order

- [x] JavaScript
- [x] Python
- [x] Java
- [x] PHP
- [x] C#
- [x] TypeScript
- [x] C++
- [x] Ruby
- [x] C
- [x] Swift
- [x] Go
- [x] R
- [x] Shell
- [x] Kotlin
- [x] Scala
- [x] PowerShell
- [x] Dart
- [x] Objective-C
- [x] Rust
- [x] Lua

### Phase 10 — Curate the lower-level ladders

- [x] Order Level 1 and Level 2 paths from gentlest to most demanding.
- [x] Check each available Level 2 → Level 3 handoff without globally
  re-grading Level 3.

### Phase 11 — Audit the expansion

- [x] Publish before/after totals, source-class results, every serious
  rejection, unresolved-gap stopping evidence, leakage checks, and sampled
  source-quality checks.

### Phase 12 — Finish learner-facing polish

- [x] Reconcile literal counts and expose the concise source legend and policy
  explanation on generated navigation and current documentation.

### Phase 13 — Validate and release-ready check

- [x] Regenerate all learner pages; run unit tests, ordinary validation,
  generated-output checks, source-class leakage checks, and the final diff
  audit. Run `--complete` only if all 240 slots genuinely qualify.

## Completed Level 1 language-breadth target

This was intentionally an oversized research phase whose Steps were the
single-pass execution units. The verified starting state is 7 of 20 languages
with at least one qualified Level 1 path. Completion required at least 17 of 20
without lowering source qualification, scoring, novice accessibility, evidence,
or verification standards.

### Phase 14 — Reach at least 85% Level 1 language coverage

- [x] Step 1 — Research Dart, C++, Lua, Shell, and Swift at pinned revisions;
  integrate every genuinely qualified Level 1 path and record serious failures.
- [x] Step 2 — Research TypeScript, C, R, PowerShell, and Rust at pinned
  revisions; integrate every genuinely qualified Level 1 path and record serious
  failures.
- [x] Step 3 — If fewer than 17 languages are covered, research Kotlin, Scala,
  and Objective-C as the fallback pool until the threshold is met or every
  remaining language has evidence-backed stopping evidence.
- [x] Step 4 — Reconcile the active audit, literal counts, progression order,
  generated pages, and the final Level 1 coverage result; run the full supported
  verification gates.

## Completed Level 2 language-breadth target

The verified starting state was 11 of 20 languages with at least one qualified
Level 2 path. Completion required at least 17 of 20 without lowering source
qualification, scoring, novice accessibility, evidence, or verification
standards.

### Phase 15 — Reach at least 85% Level 2 language coverage

- [x] Research TypeScript, Swift, and R at pinned revisions; integrate every
  genuinely qualified Level 2 path and preserve materially distinct paths when
  a repository already supplies Level 1.
- [x] Research Shell, Kotlin, and Rust at pinned revisions; integrate every
  genuinely qualified Level 2 path and record serious failures, including the
  rejected bats-file size assertion whose promised diagnostic was neither
  implemented nor directly tested and bats-assert's rejected `assert_failure`
  path whose source header inverted its implementation's return contract.
- [x] If fewer than 17 languages are covered, research Objective-C, PowerShell,
  and Scala as the fallback pool until the threshold is met or every remaining
  language has evidence-backed stopping evidence. The six primary languages all
  qualified, so this fallback was not needed.
- [x] Reconcile the active audit, literal counts, progression order, generated
  pages, and the final 17-of-20 Level 2 coverage result; run the full supported
  verification gates.

## Active learner usability and launch polish

This phase implements `EXEMPLA_LEARNER_USABILITY_AND_LAUNCH_POLISH_SPEC.md`
without changing the ranking algorithm, capacity, or accepted corpus.

### Phase 16 — Make every lower-level first click bounded and obvious

- [x] Step 1 — Record the clean-commit learner-facing baseline, public GitHub
  description, lower-level source-file sizes, and pre-change verification in
  `research/learner-usability-audit.json`.
- [x] Step 2 — Extend schema, validation, rendering, and tests so every Level 1
  and Level 2 path requires a concise `quick_start` and a valid exact initial
  source range while Levels 3–5 remain compatible.
- [x] Step 3 — Inspect all 44 populated Level 1 and Level 2 paths at their
  pinned revisions; add accurate ranges and quick starts, with evidence-backed
  exceptions for any initial range above the soft Level limit.
- [x] Step 4 — Reorder low-level presentation, mark recommended first paths and
  same-Level progression, improve README and index onboarding, add novice
  difficulty feedback, review narrow-width readability, and correct the public
  repository description.
- [ ] Step 5 — Simulate every populated Level 1 journey, every available Level
  1-to-2 transition, and at least ten Level 2-to-3 transitions; publish the
  before/after audit, regenerate, and pass every required verification gate.
  The simulations, audit, and all local workflow-equivalent gates pass; GitHub
  Actions remains pending until an explicitly authorized commit and push.

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
- [x] Preserve the concurrently completed APISIX Level 5 path and its Lua
  candidate evidence, migrate it to schema version 3, and recompute the final
  corpus as 151 paths with 49 documented gaps.
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
   verification gates. Use `--complete` only when all 240 paths exist.
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

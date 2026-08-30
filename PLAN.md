# Exempla current plan

Exempla is a learner-centered catalog of pinned real-world source paths. This
is the only current implementation plan; the original Size / Difficulty /
Complexity release plan is historical.

## Current state

- The canonical schema is version 4.
- The catalog contains 125 qualified learning paths from 124 public
  repositories across 20 languages.
- The 200-path grid has 75 documented research gaps. Ordinary validation
  accepts honest gaps; `--complete` is reserved for a genuinely full grid.
- A path is identified by `(repository, path_slug)`. One repository may supply
  at most two materially distinct paths and never two paths in the same
  language/Level bucket.
- The rubric Level still comes from four path-centered scores and their existing
  guardrails. Rubric Levels 1 and 2 also require a novice-accessibility floor;
  the published Level is the greater of the rubric Level and that floor.
- Prerequisites name prior knowledge; `concepts_developed` names what the path
  teaches.
- The active lower-rung audit is
  [`research/novice-accessibility-audit.json`](research/novice-accessibility-audit.json).
  It preserves all 38 starting low-level decisions, 28 qualified capacity
  alternates, 20 conditional gap passes, two replacements, and six progression
  sanity checks.

## Active novice-accessibility remediation

The novice-to-advanced progression review preserves the four path-centered
scores and adds a separate accessibility floor for structurally low-level
paths. The supplied specification describes eight phases and, despite calling
them 20 required steps, enumerates 25 named steps; all 25 remain in scope.

### Phase 1 — Define the novice learner precisely

- [x] Step 1.1: Rewrite the learner baseline.
- [x] Step 1.2: Give Levels 1 and 2 explicit pedagogical meanings.

### Phase 2 — Add a novice-accessibility floor to the algorithm

- [x] Step 2.1: Define central versus incidental concepts.
- [x] Step 2.2: Define `novice_accessibility` for low structural levels.
- [x] Step 2.3: Add five accessibility tests to candidate review.

### Phase 3 — Calibrate the revised low-level algorithm

- [x] Step 3.1: Recalibrate the required representative paths from pinned
  implementation and test evidence.
- [x] Step 3.2: Freeze the revised lower-level rules before the corpus audit.

### Phase 4 — Implement schema, tooling, rendering, and tests

- [x] Step 4.1: Implement machine-checkable accessibility-floor behavior.
- [x] Step 4.2: Test the required formula cases and known failure modes.

### Phase 5 — Audit all current Level 1 entries

- [x] Step 5.1: Audit every current Level 1 path from pinned implementation
  and tests, including all three required special reviews.

### Phase 6 — Audit all current Level 2 entries

- [x] Step 6.1: Audit JavaScript and Python.
- [x] Step 6.2: Audit Java and PHP.
- [x] Step 6.3: Audit C# and TypeScript.
- [x] Step 6.4: Audit C++ and Ruby.
- [x] Step 6.5: Audit C and Swift.
- [x] Step 6.6: Audit Go and R.
- [x] Step 6.7: Audit Shell and Kotlin.
- [x] Step 6.8: Audit Scala and PowerShell.
- [x] Step 6.9: Audit Dart and Objective-C.
- [x] Step 6.10: Audit Rust and Lua.

### Phase 7 — Reconcile movement and repair lower-level gaps

- [x] Step 7.1: Reconcile Levels and capacity without scoring to fit slots.
- [x] Run conditional replacement research only for newly open or clearly
  sparse lower-level language buckets.

### Phase 8 — Make the learner-facing experience explicitly gentle

- [x] Step 8.1: Rewrite low-level presentation rules and affected entries.
- [x] Step 8.2: Improve Level labels and onboarding text.
- [x] Step 8.3: Publish the complete lower-level pedagogy audit.
- [x] Step 8.4: Sanity-check at least five Level 1 → Level 2 → Level 3
  progressions, including JavaScript and PHP.
- [x] Run generation, tests, ordinary validation, generated-output checks, and
  a final approved-boundary diff audit: 38 tests pass, catalog validation
  passes, generated Markdown is current, and the diff remains within the
  novice-progression specification.

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

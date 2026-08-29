# Exempla implementation plan

This is the durable execution plan for the first complete release. Because the
project is unusually large, each numbered step is one focused, independently
verifiable pass. A checked box means its completion criteria were met.

## Phase 1 — Foundation

### Step 1.1 — Establish the repository and product contract

- [x] **Objective:** Create a public-repository-ready foundation with a clear
  purpose, name, license, constraints, and execution plan.
- **Work:** Initialize `main`; write the introductory README, license, ignore
  rules, and this plan; record that the catalog is GitHub-native and that SDC
  difficulty is separate from the admission quality gate.
- **Artifacts:** `README.md`, `LICENSE`, `.gitignore`, `PLAN.md`.
- **Complete when:** A fresh reader can state what Exempla is, what it excludes,
  and where implementation progress is tracked.
- **Dependencies:** None.

## Phase 2 — Methodology

### Step 2.1 — Specify the deliberately simple SDC rubric

- [x] **Objective:** Make S, D, C, and the final level reproducible without
  turning the rubric into a research project.
- **Work:** Define the assumed learner; implementation-LOC exclusions and five
  size bands; short D and C judgment checklists; the combination rule,
  guardrail, evidence requirements, borderline handling, revision pinning, and
  recalculation procedure.
- **Artifacts:** `docs/sdc.md`.
- **Complete when:** Two reviewers can score the same inspected repository and
  explain any disagreement using the written rubric.
- **Dependencies:** Step 1.1.

### Step 2.2 — Calibrate on a varied 10–15 repository sample

- [x] **Objective:** Remove obvious scoring absurdities before cataloging 200
  repositories.
- **Work:** Score repositories spanning tiny/large, conventional/systems,
  straightforward/algorithmic, and simple/interconnected designs; record the
  observed ordering and only the minimum rubric adjustments it requires.
- **Artifacts:** `docs/calibration.md`, revisions to `docs/sdc.md` if justified.
- **Complete when:** The sample ordering is broadly sensible, no dimension
  dominates accidentally, and any threshold change has a written reason.
- **Dependencies:** Step 2.1.

## Phase 3 — Curation rules and scope

### Step 3.1 — Define the repository quality gate

- [x] **Objective:** Ensure SDC measures difficulty while a separate gate
  decides whether a repository is worth learning from.
- **Work:** Define mandatory checks for genuine purpose, meaningful language
  use, source quality, architecture, naming, idiom, tests, documentation,
  traceability, maintainability, licensing, and educational value; define hard
  exclusions and the accepted/rejected evidence record.
- **Artifacts:** `docs/qualification.md`, `research/rejections.json`.
- **Complete when:** Every acceptance criterion is observable and a failed hard
  requirement necessarily rejects the candidate.
- **Dependencies:** Step 1.1.

### Step 3.2 — Select and document the initial 20 languages

- [x] **Objective:** Choose a current, defensible scope without pretending one
  popularity measure is universal.
- **Work:** Record the ranking source, snapshot date, selection rule, and
  treatment of CSS/HTML, SQL, shell languages, families, and ecosystems whose
  difficulty bands may be sparse.
- **Artifacts:** `docs/language-selection.md`, `catalog/languages.json`.
- **Complete when:** The exact 20 languages and every inclusion/exclusion are
  reproducible from cited sources and explicit rules.
- **Dependencies:** Step 1.1.

### Step 3.3 — Define systematic candidate research

- [x] **Objective:** Find strong small and less-famous projects as well as
  prominent ones, then preserve the evidence behind every decision.
- **Work:** Define multiple discovery channels, inspection depth, revision
  pinning, source files to sample, LOC measurement, quality review, scoring,
  rejection recording, conflict resolution, and later refreshes.
- **Artifacts:** `docs/research-process.md`, `research/README.md`.
- **Complete when:** A new curator can repeat a candidate review without hidden
  context or special infrastructure.
- **Dependencies:** Steps 2.1 and 3.1.

## Phase 4 — Data and validation tooling

### Step 4.1 — Define the catalog schema and authoring conventions

- [x] **Objective:** Keep one machine-checkable source of truth while serving
  readable Markdown to GitHub visitors.
- **Work:** Define language and repository records, evidence fields, inspection
  metadata, score consistency, stable slugs, and ordering rules in JSON Schema.
- **Artifacts:** `catalog/schema.json`, example/initial catalog data.
- **Complete when:** All required learner-facing and reproducibility metadata
  is represented without duplicated hand-authored prose.
- **Dependencies:** Steps 2.1, 3.1, and 3.2.

### Step 4.2 — Implement the standard-library catalog tool

- [x] **Objective:** Validate source data and generate deterministic
  learner-facing Markdown with no installed package dependency.
- **Work:** Implement `validate`, `generate`, and `check-generated` commands;
  check counts, uniqueness, URLs, score ranges/formula, evidence, revisions,
  licenses, file paths, language mapping, and generated-file freshness.
- **Artifacts:** `scripts/catalog.py`, generated `languages/**/README.md` files.
- **Complete when:** One documented command validates data and a second
  deterministically regenerates navigation and catalog pages.
- **Dependencies:** Step 4.1.

### Step 4.3 — Test validation and generation behavior

- [x] **Objective:** Prove checks fail for the mistakes they claim to catch.
- **Work:** Add focused standard-library tests for valid data, missing fields,
  duplicates, invalid scores, formula violations, unsafe slugs, incorrect
  counts, bad URLs, and stale generated output; add CI.
- **Artifacts:** `tests/test_catalog.py`, `.github/workflows/validate.yml`.
- **Complete when:** Tests pass locally, deliberate invalid fixtures fail for
  the expected reason, and CI runs the same supported commands.
- **Dependencies:** Step 4.2.

## Phase 5 — Curate the initial corpus

Every language step uses the same acceptance boundary: inspect actual source at
a pinned revision; record reviewed files and quality evidence; measure or
defensibly estimate meaningful implementation LOC; assign S/D/C independently;
apply the published formula; and add two accepted repositories at each level.
Standards are never lowered to fill a slot: a documented gap is preferable.

### Step 5.1 — JavaScript

- [x] **Objective:** Curate the JavaScript SDC 1–5 catalog.
- **Work:** Discover, inspect, qualify, score, and document up to ten projects.
- **Artifacts:** `catalog/javascript.json`, `languages/javascript/README.md`,
  JavaScript rejection records.
- **Complete when:** Each level has two qualified entries or an explicit gap,
  with all schema and generated-output checks passing.
- **Dependencies:** Phase 4.

### Step 5.2 — Python

- [x] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/python.json`, `languages/python/README.md`, rejection
  records.

### Step 5.3 — Java

- [x] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/java.json`, `languages/java/README.md`, rejection
  records.

### Step 5.4 — PHP

- [x] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/php.json`, `languages/php/README.md`, rejection records.

### Step 5.5 — C#

- [x] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/c-sharp.json`, `languages/c-sharp/README.md`, rejection
  records.

### Step 5.6 — TypeScript

- [x] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/typescript.json`, `languages/typescript/README.md`,
  rejection records.

### Step 5.7 — C++

- [x] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/cpp.json`, `languages/cpp/README.md`, rejection records.

### Step 5.8 — Ruby

- [x] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/ruby.json`, `languages/ruby/README.md`, rejection records.

### Step 5.9 — C

- [x] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/c.json`, `languages/c/README.md`, rejection records.

### Step 5.10 — Swift

- [x] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/swift.json`, `languages/swift/README.md`, rejection records.

### Step 5.11 — Go

- [x] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/go.json`, `languages/go/README.md`, rejection records.

### Step 5.12 — R

- [x] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/r.json`, `languages/r/README.md`, rejection records.

### Step 5.13 — Shell

- [x] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/shell.json`, `languages/shell/README.md`, rejection records.

### Step 5.14 — Kotlin

- [ ] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/kotlin.json`, `languages/kotlin/README.md`, rejection records.

### Step 5.15 — Scala

- [ ] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/scala.json`, `languages/scala/README.md`, rejection records.

### Step 5.16 — PowerShell

- [ ] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/powershell.json`, `languages/powershell/README.md`,
  rejection records.

### Step 5.17 — Dart

- [ ] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/dart.json`, `languages/dart/README.md`, rejection records.

### Step 5.18 — Objective-C

- [ ] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/objective-c.json`, `languages/objective-c/README.md`,
  rejection records.

### Step 5.19 — Rust

- [ ] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/rust.json`, `languages/rust/README.md`, rejection records.

### Step 5.20 — Lua

- [ ] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/lua.json`, `languages/lua/README.md`, rejection records.

## Phase 6 — Corpus-wide audit and recalibration

### Step 6.1 — Verify live repository facts

- [ ] **Objective:** Catch catalog drift and factual metadata errors.
- **Work:** Check that every URL resolves publicly; the pinned revision exists;
  the license permits source inspection; the primary-language classification
  is sensible; and no repository is duplicated inappropriately.
- **Artifacts:** `research/audit.json`, corrected catalog records.
- **Complete when:** Every accepted entry has a dated pass result or is removed.
- **Dependencies:** Phase 5.

### Step 6.2 — Cross-check the SDC distribution

- [ ] **Objective:** Use the full corpus to find obvious cross-language grading
  inconsistencies without statistical overengineering.
- **Work:** Compare neighboring levels and repositories with similar S/D/C
  profiles; identify absurd ordering, dimension dominance, and misplaced size
  bands; make only explainable corrections and regenerate pages.
- **Artifacts:** Final section in `docs/calibration.md`, corrected records.
- **Complete when:** No known repository is wildly easier or harder than its
  published level suggests and every correction is recorded.
- **Dependencies:** Step 6.1.

### Step 6.3 — Run learner-navigation and quality-gate audit

- [ ] **Objective:** Prove the finished repository delivers its promise to a
  GitHub visitor.
- **Work:** Traverse README → language → level → repository; verify required
  prose and prerequisites; recheck each quality-gate pass; run all validation,
  generation, and tests from a clean checkout.
- **Artifacts:** Final `research/audit.json`, any navigation/data corrections.
- **Complete when:** All 200 accepted entries pass, all links and generated pages
  are consistent, and no entry relies on popularity as its admission evidence.
- **Dependencies:** Step 6.2.

## Phase 7 — Contributor and maintainer documentation

### Step 7.1 — Document contribution and maintenance workflows

- [ ] **Objective:** Let another developer safely own and extend Exempla.
- **Work:** Document setup, validation, generation, candidate review, refreshes,
  scoring disputes, rejected-candidate records, language additions, and the
  no-lowered-standards rule.
- **Artifacts:** `CONTRIBUTING.md`, `docs/maintenance.md`, final README.
- **Complete when:** A fresh clone contains every command and decision rule
  required to propose and verify an entry.
- **Dependencies:** Phase 6.

## Phase 8 — Public release

### Step 8.1 — Publish the repository

- [ ] **Objective:** Release the verified initial catalog as a public GitHub
  repository.
- **Work:** Confirm tests and clean Git state, create `kserrec/exempla` publicly,
  push `main`, add a concise description and topics, then verify the public URL.
- **Artifacts:** Public GitHub repository and remote configuration.
- **Complete when:** Anonymous access succeeds and local `main` matches
  `origin/main` with no uncommitted recognized changes.
- **Dependencies:** Phase 7.

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

- [x] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/kotlin.json`, `languages/kotlin/README.md`, rejection records.

### Step 5.15 — Scala

- [x] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/scala.json`, `languages/scala/README.md`, rejection records.

### Step 5.16 — PowerShell

- [x] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/powershell.json`, `languages/powershell/README.md`,
  rejection records.

### Step 5.17 — Dart

- [x] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/dart.json`, `languages/dart/README.md`, rejection records.

### Step 5.18 — Objective-C

- [x] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/objective-c.json`, `languages/objective-c/README.md`,
  rejection records.

### Step 5.19 — Rust

- [x] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/rust.json`, `languages/rust/README.md`, rejection records.

### Step 5.20 — Lua

- [x] Same objective, work, completion criteria, and dependencies as Step 5.1.
- **Artifacts:** `catalog/lua.json`, `languages/lua/README.md`, rejection records.

## Phase 6 — Corpus-wide audit and recalibration

### Step 6.1 — Verify live repository facts

- [x] **Objective:** Catch catalog drift and factual metadata errors.
- **Work:** Check that every URL resolves publicly; the pinned revision exists;
  the license permits source inspection; the primary-language classification
  is sensible; and no repository is duplicated inappropriately.
- **Artifacts:** `research/audit.json`, corrected catalog records.
- **Complete when:** Every accepted entry has a dated pass result or is removed.
- **Dependencies:** Phase 5.

### Step 6.2 — Cross-check the SDC distribution

- [x] **Objective:** Use the full corpus to find obvious cross-language grading
  inconsistencies without statistical overengineering.
- **Work:** Compare neighboring levels and repositories with similar S/D/C
  profiles; identify absurd ordering, dimension dominance, and misplaced size
  bands; make only explainable corrections and regenerate pages.
- **Artifacts:** Final section in `docs/calibration.md`, corrected records.
- **Complete when:** No known repository is wildly easier or harder than its
  published level suggests and every correction is recorded.
- **Dependencies:** Step 6.1.

### Step 6.3 — Run learner-navigation and quality-gate audit

- [x] **Objective:** Prove the finished repository delivers its promise to a
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

- [x] **Objective:** Let another developer safely own and extend Exempla.
- **Work:** Document setup, validation, generation, candidate review, refreshes,
  scoring disputes, rejected-candidate records, language additions, and the
  no-lowered-standards rule.
- **Artifacts:** `CONTRIBUTING.md`, `docs/maintenance.md`, final README.
- **Complete when:** A fresh clone contains every command and decision rule
  required to propose and verify an entry.
- **Dependencies:** Phase 6.

## Phase 8 — Public release

### Step 8.1 — Publish the repository

- [x] **Objective:** Release the verified initial catalog as a public GitHub
  repository.
- **Work:** Confirm tests and clean Git state, create `kserrec/exempla` publicly,
  push `main`, add a concise description and topics, then verify the public URL.
- **Artifacts:** Public GitHub repository and remote configuration.
- **Complete when:** Anonymous access succeeds and local `main` matches
  `origin/main` with no uncommitted recognized changes.
- **Dependencies:** Phase 7.

## Phase 9 — Public collaboration readiness

### Step 9.1 — Guide issues and pull requests into the evidence workflow

- [x] **Objective:** Make the public GitHub contribution surfaces enforce the
  same evidence standards as the repository documentation.
- **Work:** Add focused issue forms for repository candidates, factual
  corrections, SDC disputes, and maintenance problems; disable unstructured
  public issues; add a pull-request template that distinguishes observed facts
  from proposed changes and carries the relevant release checks; document how
  contributors should choose among those entry points.
- **Artifacts:** `.github/ISSUE_TEMPLATE/*.yml`,
  `.github/pull_request_template.md`, updates to `CONTRIBUTING.md`.
- **Complete when:** The forms and pull-request template are present on `main`,
  the form and chooser definitions pass their published schemas, GitHub reports
  the pull-request template, and all existing catalog checks still pass.
- **Dependencies:** Phase 8.

## Phase 10 — Versioned initial release

### Step 10.1 — Publish the verified corpus as v1.0.0

- [x] **Objective:** Give the finished initial catalog a permanent, citable
  version on GitHub.
- **Work:** Run the complete release gate; create and push an annotated
  `v1.0.0` tag at the verified catalog snapshot; publish concise GitHub release
  notes describing the corpus, methodology, tooling, and contribution paths;
  verify anonymous release metadata and source archive links.
- **Artifacts:** Git tag `v1.0.0`, GitHub release `Exempla v1.0.0`.
- **Complete when:** GitHub reports a public, non-draft, non-prerelease
  `v1.0.0` release; its tag resolves to the tested commit; both generated source
  archives resolve; and local `main` remains clean and synchronized.
- **Dependencies:** Phase 9.

## Phase 11 — CI action runtime refresh

This maintenance phase remains pending, but the explicitly requested
learner-centered rebuild in Phases 12–16 takes priority. Complete Phase 11
after the rebuild rather than mixing an unrelated action-runtime change into
the catalog migration.

### Step 11.1 — Remove the Node.js 20 action deprecation warning

- [ ] **Objective:** Keep the GitHub release gate on supported action runtimes
  without changing the commands it verifies.
- **Work:** Confirm the official successor releases for `actions/checkout@v4`
  and `actions/setup-python@v5`; update only their workflow references; run the
  complete local gate and inspect the resulting GitHub Actions annotations.
- **Artifacts:** `.github/workflows/validate.yml`.
- **Complete when:** The exact workflow still passes all three project checks
  and GitHub no longer reports that either action targets Node.js 20.
- **Dependencies:** Phase 10.

## Phase 12 — Learner-centered ranking foundation

### Step 12.1 — Implement and smoke-test the simple learning-level mechanism

- [x] **Objective:** Replace repository-wide SDC ranking with a path-centered,
  four-dimension measure of transferable programming growth.
- **Work:** Write the short public rubric; add the pure four-score formula and
  focused unit cases; define schema-version-2 learning-path, coding-relevance,
  and score evidence; update validation and generation; score 10–15 varied
  existing paths as a smoke test; record only the minimum wording correction
  needed to remove an obvious calibration failure.
- **Artifacts:** `docs/learning-levels.md`,
  `docs/learning-level-calibration.md`, the version-2 contract and rendering in
  `scripts/catalog.py` and `tests/test_catalog.py`; canonical
  `catalog/schema.json` activation remains part of the all-at-once Phase 14
  cutover required by the rebuild specification.
- **Complete when:** The formula examples, input validation, path
  relationships, gap-tolerant mode, deterministic generation, and learner
  rendering pass focused tests without adding a dependency or an automated
  scoring mechanism.
- **Dependencies:** Phases 2–4 and the learner-centered rebuild specification.

## Phase 13 — Re-review the v1.0.0 catalog

Each step reviews the ten existing entries for one language in canonical
catalog order. Source, tests, documentation, license, pinned commit, quality,
domain relevance, learning path, score evidence, and formula are inspected
before a retain/remove decision. A second reviewer checks every decision.
Replacement research does not begin until all 200 decisions are recorded.

### Steps 13.1–13.20 — Review every existing language catalog

- [x] **13.1 JavaScript**
- [x] **13.2 Python**
- [x] **13.3 Java**
- [x] **13.4 PHP**
- [x] **13.5 C#**
- [x] **13.6 TypeScript**
- [x] **13.7 C++**
- [x] **13.8 Ruby**
- [x] **13.9 C**
- [x] **13.10 Swift**
- [x] **13.11 Go**
- [x] **13.12 R**
- [ ] **13.13 Shell**
- [ ] **13.14 Kotlin**
- [ ] **13.15 Scala**
- [ ] **13.16 PowerShell**
- [ ] **13.17 Dart**
- [ ] **13.18 Objective-C**
- [ ] **13.19 Rust**
- [ ] **13.20 Lua**
- **Artifact:** `research/learner-centered-rebuild.json`.
- **Complete when:** Every one of the 200 prior entries has an evidence-backed,
  independently reviewed decision and the audit summaries reconcile exactly.
- **Dependencies:** Step 12.1.

## Phase 14 — Schema-version-2 cutover

### Step 14.1 — Publish the reviewed retained corpus and honest gaps

- [ ] **Objective:** Make the learner-centered model the only active catalog
  model without retaining entries merely to preserve counts.
- **Work:** Review the complete audit; convert retained entries; remove failed
  entries; append removal evidence without erasing history; regenerate all
  language pages; update the README to literal counts; switch CI to ordinary
  validation while gaps exist.
- **Artifacts:** `catalog/*.json`, `research/rejections.json`,
  `languages/**/README.md`, `README.md`, `.github/workflows/validate.yml`.
- **Complete when:** Every canonical file uses schema version 2, no accepted
  entry contains SDC data, all retained entries match reviewed evidence, and
  ordinary validation and generated-output checks pass.
- **Dependencies:** Phase 13.

## Phase 15 — Gap research and replacement curation

### Steps 15.1–15.20 — Research each language in canonical order

- [ ] **15.1 JavaScript**
- [ ] **15.2 Python**
- [ ] **15.3 Java**
- [ ] **15.4 PHP**
- [ ] **15.5 C#**
- [ ] **15.6 TypeScript**
- [ ] **15.7 C++**
- [ ] **15.8 Ruby**
- [ ] **15.9 C**
- [ ] **15.10 Swift**
- [ ] **15.11 Go**
- [ ] **15.12 R**
- [ ] **15.13 Shell**
- [ ] **15.14 Kotlin**
- [ ] **15.15 Scala**
- [ ] **15.16 PowerShell**
- [ ] **15.17 Dart**
- [ ] **15.18 Objective-C**
- [ ] **15.19 Rust**
- [ ] **15.20 Lua**
- **Work:** Calculate real gaps, use at least three independent discovery
  channels per language, inspect pinned implementation/tests/docs, record every
  serious rejection and reconsideration condition, score before consulting the
  open bucket, and accept at most the strongest two entries per level.
- **Artifacts:** Canonical and generated catalog files,
  `research/rejections.json`, and rebuild-audit research summaries.
- **Complete when:** Each slot contains two qualified repositories or records
  the channels and plausible candidates behind an honest unresolved gap.
- **Dependencies:** Phase 14.

## Phase 16 — Consistency audit, public workflow, and release

### Step 16.1 — Audit the finished corpus and replace every active SDC workflow

- [ ] **Objective:** Make the public repository deliver its learner-centered
  promise consistently from navigation through contribution and maintenance.
- **Work:** Compare neighboring levels and score profiles; recheck domain and
  quality gates, paths, links, commits, licenses, languages, duplicates, counts,
  gaps, and navigation; replace current SDC documentation and issue workflows;
  keep `docs/sdc.md` only as a historical notice; run the applicable release
  gate; publish a new major-version release without moving `v1.0.0`.
- **Artifacts:** `README.md`, `CONTRIBUTING.md`, `docs/**`, `catalog/README.md`,
  issue and pull-request templates, `research/**`, generated pages, final Git
  commit/tag/release.
- **Complete when:** All completion criteria in the rebuild specification are
  evidenced, current docs contain no active SDC method, CI matches the README's
  honest completeness claim, tests and applicable validation pass, the remote
  release is verified, and Git is clean and synchronized.
- **Dependencies:** Phase 15.

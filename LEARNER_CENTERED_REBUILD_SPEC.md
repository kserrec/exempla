# Exempla learner-centered ranking and catalog rebuild specification

> **LOCAL-ONLY HANDOFF DOCUMENT**
>
> Do not stage, commit, or push this file. It is an instruction artifact for a
> new implementation agent, not a public project document. Implementation files
> created or changed under this specification may follow the project's normal
> commit workflow, but this file itself must remain local and untracked.

## 1. Purpose

Replace Exempla's current Size / Difficulty / Complexity (SDC) ranking with a
small learner-centered heuristic that answers this question:

> How advanced are the transferable programming skills required to understand
> one carefully chosen learning path through this real-world repository?

The replacement must rank programming difficulty, not arbitrary subject-matter
difficulty. A repository whose main challenge is advanced mathematics, a
specialized scientific discipline, niche business rules, or another difficult
external subject does not belong in Exempla, even at Level 5.

After implementing the new ranking:

1. re-review every repository in the existing 200-entry catalog;
2. remove every repository that fails the new coding-relevance gate, the
   existing quality gate, or the new path-centered ranking requirements;
3. preserve an evidence-backed audit record for every retain/remove decision;
4. calculate every gap left by those removals;
5. search again and fill those gaps with newly inspected repositories that
   genuinely satisfy the new rules; and
6. leave an honest gap when diligent research cannot find two qualified
   repositories for a language and level.

Almost every current entry may be removed. That is acceptable. Existing
membership and existing SDC placement provide no presumption of acceptance.

## 2. Authority and starting state

This document is the controlling specification for the rebuild. Where it
conflicts with the current SDC-specific parts of `docs/sdc.md`,
`docs/calibration.md`, `docs/research-process.md`, `docs/maintenance.md`,
`CONTRIBUTING.md`, `catalog/schema.json`, `scripts/catalog.py`, generated
language pages, issue forms, or `PLAN.md`, this specification takes precedence
for the rebuild.

Verified starting state when this specification was written:

- the public `v1.0.0` tag preserves the original SDC catalog;
- 20 languages are defined in `catalog/languages.json`;
- the 20 `catalog/<language>.json` files contain 200 accepted repositories;
- every accepted entry uses schema version 1 and an `sdc` object;
- `scripts/catalog.py` validates canonical JSON and generates Markdown using
  only the Python standard library;
- `tests/test_catalog.py` contains 13 tests for current validation and
  generation behavior;
- `languages/README.md` and `languages/*/README.md` are generated, not canonical;
- `research/rejections.json` preserves rejected-candidate evidence;
- `research/audit.json` records the completed SDC corpus audit; and
- Phase 11 in `PLAN.md` is unrelated CI maintenance. This explicitly named
  rebuild takes priority when handed to an agent; preserve that maintenance
  work as a later task rather than silently deleting it.

Never rewrite, move, or retag `v1.0.0`. Git history is the archive of the old
method and old catalog.

## 3. Product boundary

Exempla is for learning transferable programming and software-engineering
skills by reading good real-world source. It is not a catalog of every kind of
intellectually difficult software.

### 3.1 Assumed learner

The learner:

- knows the cataloged language's basic syntax, control flow, functions, common
  data structures, modules, and ordinary standard-library use;
- has written small programs;
- can clone a repository, navigate files, and run documented tests; and
- is not assumed to know advanced language features, production architecture,
  concurrency, systems techniques, or a specialized external domain.

The levels describe the programming growth required beyond that baseline.

### 3.2 Unit being ranked

Rank one explicit **learning path**, not the repository as an undifferentiated
whole.

Every accepted entry must define:

- one concrete programming behavior or feature the learner will understand;
- the first source file to open;
- the supporting implementation and test files needed for the trace;
- the path from entry point or public API through implementation to a test or
  observable result; and
- the reusable programming lessons demonstrated by that path.

A very large repository may qualify at a low or middle level when it contains a
small, coherent, genuinely representative learning path. A small repository may
rank highly when its chosen path requires advanced programming techniques.
Repository-wide lines of code must not enter the level calculation.

### 3.3 What remains separate from level

The existing repository quality gate remains pass/fail. Readability,
architecture, naming, idiom, tests, documentation, traceability,
maintainability, and educational value determine whether a repository is worth
studying; they do not numerically inflate its level.

Popularity, stars, downloads, maintainer reputation, and `good first issue`
labels remain discovery signals at most. They never admit or grade a project.

## 4. Hard coding-relevance and domain gate

Apply this gate before assigning any dimension score. A failure rejects the
candidate; there is no domain-difficulty score and no Level 5 exception.

### 4.1 Required pass conditions

An accepted learning path must satisfy all of these:

1. Its main lessons transfer to other programs: language technique, control and
   data flow, state management, API design, modular design, testing, error
   handling, concurrency, resource management, compatibility, portability, or
   comparable software-engineering practice.
2. Its purpose and the selected behavior can be explained without teaching an
   advanced external discipline first.
3. A generally capable programmer can obtain the necessary context from the
   repository's own documentation plus a short prerequisites paragraph.
4. The reason the path is challenging is primarily how the software is built,
   not the specialized theory, rules, or subject matter it encodes.
5. The selected behavior is real and representative of the production
   software; it is not a trivial wrapper chosen solely to make a difficult
   project appear approachable.

### 4.2 Mandatory rejection signals

Reject when understanding the selected path materially depends on expertise
such as:

- advanced mathematics or mathematical proofs;
- specialized scientific, medical, financial, legal, tax, or regulatory
  knowledge;
- research-paper theory that the repository assumes rather than teaches;
- cryptographic theory required to judge or follow a primitive's implementation;
- a niche hardware, protocol, or industry specification that dominates the
  program logic; or
- any similarly narrow subject whose mastery would explain the difficulty
  better than programming skill would.

Do not reject merely because a repository concerns a domain. A scheduling
tool, HTTP client, parser, database client, or signing API may qualify when the
chosen path is self-contained and teaches broadly reusable programming. The
test is what knowledge is required to understand the actual path, not the
repository topic or name.

General computer-science topics are not automatically admitted. A compiler,
database engine, operating-system component, machine-learning framework, or
cryptography project qualifies only when the selected path is understandable
without specialist theory and its main lessons are transferable programming.

### 4.3 Domain-gate evidence

Every accepted entry must record:

- any domain context the learner actually needs;
- why that context is short, self-contained, and subordinate to the coding
  lesson; and
- why the hard parts of the selected path teach transferable programming.

Every rejected current entry or candidate must record the exact failed
condition, observed evidence, and a literal condition for reconsideration.

## 5. The four ranking dimensions

Each dimension is a whole integer from 1 through 5. Score only recurring or
essential signals in the selected learning path. An isolated advanced helper
outside that path does not raise the score.

Write the observed signals and prose reason before calculating the final level.
When a path sits between anchors, use the lower score unless the higher anchor
recurs in the main trace.

### 5.1 Language technique depth

This measures how much language fluency beyond the assumed baseline is needed
to read the path.

- **1 — Basic:** Direct functions, ordinary collections, simple classes or
  records, basic exceptions, and conventional module use.
- **2 — Common professional idioms:** Clear interfaces, callbacks, composition,
  iterators, ordinary object-oriented or functional patterns, and standard
  ecosystem conventions.
- **3 — Substantial abstraction:** Generics, protocols or traits, higher-order
  composition, nontrivial type modeling, decorators or annotations, or
  framework idioms materially shape the path.
- **4 — Advanced language machinery:** Advanced type-system features, macros,
  reflection, metaprogramming, code generation, unsafe or low-level facilities,
  or similarly implicit mechanisms recur in important behavior.
- **5 — Expert language fluency:** Multiple advanced mechanisms interact
  pervasively; understanding the path requires expert command of the language
  rather than one isolated advanced construct.

### 5.2 Behavioral reasoning

This measures how hard it is to mentally follow what the program does over
time, including control flow, state, failure, and resources.

- **1 — Local and direct:** Synchronous, mostly stateless behavior with obvious
  data flow and local errors.
- **2 — Modest state and branching:** Several meaningful branches, localized
  mutable state, validation, error paths, or a simple lifecycle remain easy to
  trace.
- **3 — Nontrivial behavior:** Asynchronous work, persistence, caching, events,
  retries, state transitions, or resource lifecycles materially affect the
  trace.
- **4 — Advanced nonlocal reasoning:** Concurrency, state machines, scheduling,
  event propagation, resource ownership, recovery, or cross-cutting invariants
  recur and must be held together.
- **5 — Expert behavioral reasoning:** Several advanced concerns interact
  pervasively—for example concurrent state plus scheduling, recovery, resource
  lifetimes, or distributed coordination—and nonlocal reasoning is unavoidable.

### 5.3 Design span

This measures how much structural context a learner must hold to understand and
modify the selected behavior. It is about the path's span, not total repository
size or file count.

- **1 — One focused unit:** The path stays within a few functions or files and
  one clear component.
- **2 — A few clear modules:** One process and a small number of explicit
  boundaries contain the behavior.
- **3 — Several meaningful boundaries:** The trace crosses layers, subsystems,
  adapters, or interfaces, but their responsibilities remain locally
  understandable.
- **4 — Broad architecture:** Many modules, extension points, execution modes,
  integrations, or cross-cutting policies contribute to the path.
- **5 — Platform-scale span:** Understanding the path requires coordinating
  several major subsystems, processes, runtimes, or pervasive extension and
  policy mechanisms.

### 5.4 Constraint burden

This measures how many software guarantees a correct change must preserve. It
captures advanced engineering demands that are neither language syntax nor
architecture size.

- **1 — Ordinary correctness:** A small local contract and ordinary expected
  output dominate.
- **2 — Routine production safeguards:** Input validation, explicit errors,
  cleanup, basic tests, or a small stable API must be preserved.
- **3 — Several material guarantees:** Persistence or serialization contracts,
  compatibility, portability, performance, reliability, or security boundaries
  influence normal implementation decisions.
- **4 — Interacting strict constraints:** Multiple guarantees—such as backward
  compatibility, thread safety, resource bounds, performance, recovery, or
  cross-platform behavior—recur across the path.
- **5 — Expert change discipline:** Several system-wide guarantees interact so
  that a locally plausible change can violate correctness, safety,
  compatibility, performance, or reliability elsewhere in the selected path.

## 6. Final level calculation

The calculation must remain one small pure function with no dependencies.

Inputs, in this order:

1. language technique depth;
2. behavioral reasoning;
3. design span; and
4. constraint burden.

Algorithm:

```python
def calculate_learning_level(language, behavior, design, constraints):
    scores = (language, behavior, design, constraints)
    level = (sum(scores) + 2) // 4  # arithmetic mean, halves upward
    if 5 in scores:
        level = max(level, 4)
    if level == 5 and sum(score == 5 for score in scores) < 2:
        level = 4
    return level
```

The first guardrail prevents one expert-level programming burden from being
published as beginner or intermediate. The second states the Level 5 contract
explicitly: a path is highly advanced only when its rounded mean reaches 5 and
at least two dimensions are themselves expert-level.

Required examples:

- `1 / 1 / 1 / 1` → **Level 1**
- `2 / 2 / 1 / 1` → mean 1.50 → **Level 2**
- `3 / 3 / 2 / 2` → mean 2.50 → **Level 3**
- `4 / 4 / 3 / 3` → mean 3.50 → **Level 4**
- `5 / 2 / 2 / 2` → mean 2.75, expert guardrail → **Level 4**
- `5 / 5 / 1 / 1` → mean 3.00, expert guardrail → **Level 4**
- `5 / 5 / 4 / 4` → mean 4.50 → **Level 5**

Public pages show only integer Level 1 through Level 5. Do not display decimal
rankings.

## 7. Meaning of the five public levels

- **Level 1 — Beginner real-world code:** Basic language features, direct
  behavior, one focused design unit, and ordinary correctness constraints.
- **Level 2 — Early real-world code:** Common professional idioms, modest state
  and error handling, a few clear modules, and routine production safeguards.
- **Level 3 — Intermediate:** Substantial abstraction, meaningful state or
  asynchronous behavior, several boundaries, and multiple material guarantees.
- **Level 4 — Advanced:** At least one expert-level burden or a broadly advanced
  combination of language, behavioral, architectural, and constraint demands.
- **Level 5 — Highly advanced programming:** Multiple expert programming
  burdens interact across an exceptionally demanding but still
  programming-centered learning path. Specialized external subject matter may
  never be the reason for this level.

The levels are not prestige labels and do not describe product importance.

## 8. Simplicity and implementation budget

The scoring mechanism itself must be implementable by a capable agent in one
focused pass of less than roughly 30 minutes. The full 200-entry review and
replacement search are separate research work and will take many passes.

The algorithm implementation is finished when it has:

- the four written anchors above;
- the pure calculation function above;
- integer validation for four scores;
- concise evidence fields for each score;
- approximately ten focused unit cases covering rounding, invalid scores, and
  the expert guardrail; and
- learner-facing rendering of the four scores and final level.

Do not build or add:

- static-analysis engines;
- abstract-syntax-tree or call-graph scoring;
- machine-learning or language-model ranking pipelines;
- repository-wide dependency analysis;
- statistical fitting or learner prediction models;
- language-specific scoring plugins or normalization tables;
- weighted coefficients, scoring configuration languages, or private overrides;
- a database, website, service, crawler, or queue;
- automatic admission, rejection, or score assignment; or
- any new package dependency merely to implement this rubric.

Automation may validate structure, calculate the formula from human-entered
scores, generate Markdown, and check public metadata. Human source inspection
remains the ranking mechanism.

If implementing the formula or its validator starts becoming a project of its
own, stop and simplify it back to this section.

## 9. Target catalog schema version 2

Bump each per-language catalog file to schema version 2. Retain the existing
repository identity, language, description, real-world evidence, study value,
prerequisites, quality, inspection, license, and GitHub metadata fields where
their evidence survives re-review.

Remove the `sdc` object completely. Do not retain aliases such as `size_score`,
`difficulty`, `complexity`, or `sdc_level` in current canonical entries.
Historical SDC data remains available at `v1.0.0` and in Git history.

Replace top-level `start_here` and `sdc` with these three objects:

```json
{
  "coding_relevance": {
    "gate": "pass",
    "domain_context": [
      "Short, self-contained context actually required by this path."
    ],
    "reason": "Why the path primarily teaches transferable programming rather than specialist subject matter."
  },
  "learning_path": {
    "goal": "The concrete behavior or feature the learner will understand.",
    "start_here": {
      "path": "src/example.py",
      "reason": "Why reading begins here."
    },
    "supporting_files": [
      "src/support.py",
      "tests/test_example.py"
    ],
    "trace": "How to follow the behavior from entry point through implementation to a test or observable result."
  },
  "learning_level": {
    "level": 3,
    "language_technique": {
      "score": 3,
      "signals": ["observed recurring language mechanism"],
      "reason": "Why the selected path meets the published anchor."
    },
    "behavioral_reasoning": {
      "score": 3,
      "signals": ["observed recurring state or control-flow mechanism"],
      "reason": "Why the selected path meets the published anchor."
    },
    "design_span": {
      "score": 2,
      "signals": ["observed modules and boundaries in the trace"],
      "reason": "Why the selected path meets the published anchor."
    },
    "constraint_burden": {
      "score": 2,
      "signals": ["observed guarantees the implementation preserves"],
      "reason": "Why the selected path meets the published anchor."
    },
    "placement": "Why these four dimensions produce the published learner level."
  }
}
```

Schema requirements:

- `coding_relevance.gate` is the constant string `pass` for accepted entries;
- `domain_context` may be empty but must be an array of nonempty strings when
  context exists;
- `learning_path.supporting_files` contains at least one implementation or test
  path in addition to `start_here.path`;
- every learning-path path is a safe relative path and may not be a dotenv file
  or dotenv naming variant;
- learning-path files must be included in `inspection.files`;
- all four judgment objects require `score`, `signals`, and `reason`;
- the stored `level` must exactly equal `calculate_learning_level(...)`;
- repository lines of code are not required, scored, or rendered by schema
  version 2; and
- `additionalProperties` remains false for structured objects.

Keep the existing top-level `learn` list. Its contents must now be plainly
transferable programming lessons and must agree with `coding_relevance` and the
selected path.

## 10. Tooling and generated-output changes

Update `scripts/catalog.py` without adding a dependency:

1. remove `size_score` and the three-input `combined_level`;
2. add the exact four-input `calculate_learning_level` function;
3. validate the version-2 objects and their path relationships;
4. remove LOC-to-score validation;
5. count and group entries by `learning_level.level`;
6. render headings as `Level 1` through `Level 5`, not `SDC 1` through `SDC 5`;
7. render the four named dimension scores, their reasons, the explicit learning
   path, and the coding-relevance explanation;
8. preserve honest empty-level text;
9. preserve deterministic generation; and
10. retain ordinary and `--complete` validation modes.

Update `tests/test_catalog.py` to prove:

- every required formula example in Section 6;
- rejection of scores outside 1–5;
- rejection of a stored level inconsistent with the formula;
- rejection of a missing coding-relevance gate or any value other than `pass`;
- rejection of missing path goal, trace, start file, or supporting files;
- rejection of learning-path files absent from `inspection.files`;
- continued rejection of dotenv-like inspection or path names;
- continued duplicate, URL, commit, date, language, license, and required-prose
  validation;
- incomplete catalogs can contain honest gaps;
- complete mode still requires two repositories per language and level; and
- generation remains deterministic and stale output is detected.

During the rebuild, CI may temporarily run ordinary `validate` and
`check-generated` rather than `--complete`, because removals must be allowed to
create honest gaps. The README must state that the catalog is being rebuilt and
must show the actual accepted count. Restore `--complete` in CI only if every
slot is genuinely filled again.

## 11. Current-catalog re-review

Review all 200 current entries before searching for replacements. Do not
grandfather an entry, mechanically translate its old D/C scores, or assume its
old level predicts its new level.

### 11.1 Review source and order

Work in the order defined by `catalog/languages.json`, one language per focused
pass:

1. JavaScript
2. Python
3. Java
4. PHP
5. C#
6. TypeScript
7. C++
8. Ruby
9. C
10. Swift
11. Go
12. R
13. Shell
14. Kotlin
15. Scala
16. PowerShell
17. Dart
18. Objective-C
19. Rust
20. Lua

For every existing entry:

1. establish the exact current catalog record and pinned revision;
2. confirm the repository, commit, license, cataloged language, and selected
   source paths still resolve;
3. inspect the actual pinned source, tests, and relevant documentation;
4. identify the best honest learning path, if one exists;
5. apply the coding-relevance/domain gate;
6. reapply every existing quality requirement;
7. if both gates pass, score all four new dimensions from observed path evidence;
8. calculate the new level without considering which bucket needs an entry;
9. choose `retain` or `remove` and record the exact reason; and
10. have a second reviewer check the gate decision, path, anchor evidence, and
    formula before finalizing that entry.

An old entry may be retained at a different level. It may also be removed even
when its source is excellent, because the new product boundary is narrower.

### 11.2 Rebuild audit record

Create `research/learner-centered-rebuild.json` as the durable audit. Its
top-level record must contain:

- schema version;
- review start and completion dates;
- source catalog release (`v1.0.0`);
- source catalog commit;
- current language and entry totals;
- per-entry decisions; and
- summary counts by language, old level, new level, and removal reason.

Each prior entry records at least:

```json
{
  "repository": "owner/name",
  "language": "Python",
  "prior_level": 2,
  "pinned_commit": "40 lowercase hexadecimal characters",
  "decision": "retain",
  "coding_relevance": {
    "status": "pass",
    "domain_context": [],
    "evidence": "Observed reason the selected path teaches transferable programming."
  },
  "quality_status": "pass",
  "learning_path": {
    "goal": "Concrete behavior",
    "start_path": "src/example.py",
    "supporting_files": ["src/support.py", "tests/test_example.py"],
    "trace": "Entry-to-result trace"
  },
  "new_scores": {
    "language_technique": 2,
    "behavioral_reasoning": 3,
    "design_span": 2,
    "constraint_burden": 2
  },
  "new_level": 2,
  "evidence": "Concise retain/remove rationale grounded in inspected source.",
  "reconsider": "Literal condition that would justify a different decision."
}
```

For a removal, use `decision: "remove"`, set the failed gate literally, omit
new scores when scoring would be misleading, and state the removal reason.

Commit the growing audit after each completed language, but do not change the
public catalog during this audit phase. That keeps the old and new systems from
being partially mixed and lets reviewers inspect all 200 decisions before the
cutover.

### 11.3 Cutover after all 200 decisions

Only after every current entry has a reviewed decision:

1. bump the canonical schema to version 2;
2. replace SDC tooling and tests with the learner-centered implementation;
3. convert retained records using their reviewed evidence;
4. remove every failed record from canonical catalogs;
5. append removal evidence to `research/rejections.json` without erasing older
   rejection history;
6. regenerate every language page;
7. update the README to the actual retained count and rebuild status;
8. switch CI to gap-tolerant validation when gaps exist; and
9. run the full non-complete validation gate from a clean committed snapshot.

Do not keep an entry merely to avoid a dramatic count reduction. The cutover
may produce a mostly empty catalog.

## 12. Gap calculation and replacement research

After the cutover, calculate the exact missing slots for each
`(language, Level 1–5)` pair. The target remains at most two accepted
repositories per slot.

Research one language per focused pass, again in `catalog/languages.json`
order. For each language:

1. list its current retained entries and missing levels;
2. consult `research/rejections.json` and the rebuild audit before rediscovering
   candidates;
3. discover candidates through at least three independent channels from the
   existing research process;
4. deliberately include smaller and less-famous real software;
5. triage public status, genuine purpose, meaningful language use, license, and
   obvious domain-gate failures before deep inspection;
6. pin a full commit before judging source;
7. inspect the actual implementation, tests, documentation, and path;
8. apply the domain gate and quality gate before scoring;
9. score the four dimensions before looking at the missing bucket it might
   fill;
10. accept it only into the level produced by the formula;
11. record every serious rejection with observed evidence and a reconsideration
    condition;
12. regenerate and validate after each accepted batch; and
13. commit canonical JSON and generated Markdown together.

Never search for “a Level 3 repository” and then work backward to a Level 3
score. Search for good programming-learning repositories, score them honestly,
and see which gaps they fill.

Do not move a qualified candidate to a neighboring level merely because its
true slot is already full. Keep the stronger two entries using educational
quality and path clarity, record the other qualified candidate as an alternate,
and leave unrelated gaps honest.

Before declaring a gap unresolved, record the discovery channels used and the
plausible candidates inspected. There is no arbitrary star threshold or
candidate quota, but a superficial single search is not diligent research.

## 13. Documentation replacement

Create `docs/learning-levels.md` as the canonical public rubric. Keep it much
shorter than this execution specification: learner baseline, domain gate, four
anchors, formula, guardrail, path-centered unit, borderline rule, and one or
two examples.

Update every live reference and workflow:

- `README.md`;
- `CONTRIBUTING.md`;
- `docs/qualification.md`;
- `docs/research-process.md`;
- `docs/maintenance.md`;
- `catalog/README.md`;
- `PLAN.md`;
- `.github/ISSUE_TEMPLATE/01-repository-candidate.yml`;
- `.github/ISSUE_TEMPLATE/03-sdc-dispute.yml` (rename it to a learning-level
  dispute form);
- `.github/pull_request_template.md`;
- `research/README.md`;
- generated `languages/README.md` and `languages/*/README.md`; and
- audit/calibration records.

`docs/sdc.md` must no longer present a current algorithm. Replace it with a
short historical notice linking to `v1.0.0` and the new rubric, or remove it
only after updating every live link. Preserve the original document in Git
history rather than copying its obsolete method into current docs.

Create a short `docs/learning-level-calibration.md` that records the initial
smoke test and final corpus consistency pass. Do not preserve LOC monotonicity
as a success criterion; size is no longer a ranking dimension.

Use plain “Level 1” through “Level 5” language. Do not create another opaque
acronym unless the user explicitly requests a name.

## 14. Calibration and final corpus audit

### 14.1 Small pre-audit smoke test

Before reviewing all 200 entries, score 10–15 deliberately varied existing
paths. Include:

- direct beginner code;
- ordinary production libraries and tools;
- asynchronous or stateful applications;
- advanced language mechanisms;
- broad modular architectures;
- strict compatibility or performance constraints; and
- at least two candidates likely to fail the domain gate.

Ask only:

- Do the anchors distinguish programming growth sensibly?
- Does one dimension swallow the others?
- Does any specialist-domain project incorrectly survive?
- Does a single advanced feature produce an absurd public level?
- Are Levels 1 and 5 both realistically reachable?

Make at most the minimum wording or guardrail correction required to remove an
obvious failure, record it, and stop. Do not statistically tune the rubric or
optimize it to preserve existing entries.

### 14.2 Final consistency pass

After replacement research finishes:

- compare neighboring levels within and across languages;
- compare entries with similar four-score profiles;
- verify Level 5 difficulty comes from programming rather than outside subject
  matter;
- confirm every entry's published path is the path actually scored;
- recheck the quality and domain gates;
- verify all public links, pinned commits, licenses, paths, and language
  classifications;
- check duplicates and generated navigation;
- report retained, removed, newly accepted, rejected, and remaining-gap counts;
- explain every score or placement correction; and
- do not force a balanced score distribution as evidence of success.

The target is two qualified entries per language and level, but truth outranks
the 200-entry target. If gaps remain after diligent research, publish the gaps
and the evidence instead of weakening the gate or changing scores.

## 15. Required validation and release behavior

At every implementation or catalog pass, run the proportionate focused tests.
Before a final release, run:

```console
python3 -m unittest discover -s tests -v
python3 scripts/catalog.py validate --complete
python3 scripts/catalog.py check-generated --complete
```

Use `--complete` only when there really are two qualified entries at every
level for every language. Otherwise run the same two catalog commands without
that flag, make the incomplete state explicit, and do not claim completion of
the 200-entry target.

Final verification must prove:

- all canonical files use schema version 2;
- no accepted entry contains an `sdc` object;
- every stored final level follows the four-score formula;
- every accepted entry passes the coding-relevance and quality gates;
- every learning-path file is safe, inspected, and public at the pinned commit;
- all accepted licenses permit public source inspection;
- no repository is duplicated inappropriately;
- generated Markdown is deterministic and current;
- learner navigation works from root README to language, level, repository,
  path, and upstream pinned source;
- current docs do not describe SDC as active;
- catalog counts and gaps are literal; and
- CI runs the same gate the README claims.

Any recursive listing, search, snapshot, archive, or bulk-content operation
must explicitly exclude `.env`, names ending in `.env`, `.env.*`, and
`*.env.*`. Dotenv files are opaque secrets and must never be opened, searched,
printed, parsed, sourced, diffed, or delegated for inspection.

## 16. Execution plan for the new agent

Record this work in `PLAN.md` as single-pass phases and steps before broad
implementation. The local-only specification file must not be added to that
commit.

### Phase A — Implement the simple learner-level mechanism

- Write the short public rubric.
- Add the pure four-score calculation and unit cases.
- Define schema-version-2 fields and generator output.
- Perform the 10–15-path smoke test.
- Stop improving the algorithm once the simple stop conditions pass.

This is the only phase whose scoring mechanism should take roughly 30 minutes
to build. Do not confuse that budget with the research work below.

### Phase B — Re-review the existing catalog

- Complete one language per step in the exact 20-language order.
- Inspect all ten current entries for that language.
- Record every retain/remove decision in the rebuild audit.
- Do not search replacements yet.

### Phase C — Cut over to schema version 2

- Review the complete 200-entry audit for missing or unsupported decisions.
- Replace the schema, validation, generation, and canonical data together.
- Remove every failed entry.
- Publish honest gaps and actual counts.

### Phase D — Research and refill gaps

- Complete one language per step in catalog order.
- Research all missing levels for that language.
- Accept only candidates that independently pass and land in a genuine gap.
- Preserve rejection evidence and regenerate after each accepted batch.

### Phase E — Cross-corpus audit and documentation

- Run the final consistency, live-fact, quality, domain, path, and navigation
  audits.
- Finish public docs and contributor workflows.
- Restore complete-mode CI only if the corpus is actually complete.
- Publish a new major-version release rather than moving `v1.0.0`.

Each completed language, cutover, or audit phase should end with focused tests,
an explicit diff review, a small coherent commit, and a push only when the
user's active instructions authorize pushing implementation work.

## 17. Agent reporting contract

After each focused pass, report:

- exact entries inspected;
- retained, removed, accepted, and rejected counts;
- each evidence-backed domain-gate failure;
- new four-score profiles and resulting levels;
- gaps opened or filled;
- canonical, generated, test, and documentation files changed separately;
- verification commands and results;
- the next unfinished language or phase; and
- any action only the user can perform, stated literally with its consequence.

Do not describe a missing component as broken, a new field as a fix, or an
unverified upstream fact as current.

## 18. Completion criteria

The rebuild is complete when:

1. the old SDC algorithm is no longer active anywhere in current catalog data,
   tooling, generated pages, or contributor workflows;
2. the new algorithm remains exactly the simple four-dimension heuristic in
   this specification;
3. all 200 prior entries have explicit evidence-backed retain/remove decisions;
4. every retained and new entry passes the coding-relevance and quality gates;
5. every accepted entry has a concrete scored learning path;
6. every removal and serious rejected candidate has a durable record;
7. every gap has either two qualified entries or documented diligent research;
8. current counts and incomplete states are reported honestly;
9. all applicable tests, validation, generation, live-fact, and navigation
   checks pass; and
10. the final public documentation promises learning transferable programming,
    not learning arbitrary difficult subject matter.

The algorithm is successful when it is quick to understand, quick to apply,
and usually produces sensible learner progression. It is not required to be a
scientifically validated model, an objective truth about repositories, or a
perfect predictor for every learner.

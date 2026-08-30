# Candidate research process

This process is repeatable but keeps source inspection and judgment at its
center. Automation may validate facts and formulas; it may not admit, reject,
or score a repository.

## 1. Calculate the real gaps

List accepted entries and open slots for one language. Read the rebuild audit
and existing rejection history before rediscovering candidates. Gaps direct
research effort, but they never determine a candidate's score.

## 2. Discover through at least three channels

Use at least three independent sources such as:

- official language, foundation, or ecosystem organizations;
- official language, framework, and tool sample repositories with complete
  checked-in behavior;
- package registries and reverse-dependency evidence;
- GitHub language and topic search across varied project sizes;
- software named in production documentation or real workflows;
- respected maintainers' smaller libraries and tools; and
- completed companion code from respected books, courses, workshops, or public
  university materials;
- small complete reference implementations, games, command-line applications,
  data transformers, and deliberately minimal libraries; and
- curated ecosystem or beginner-project lists used only as leads.

For Level 1 and Level 2 research, actually search both production and
educational-exemplar channels. Deliberately include smaller and less-famous
software. Do not search for a desired score, treat a "beginner" label as
qualification evidence, or sort only by stars. Discover first, inspect second,
score third.

## 3. Triage before deep review

Record canonical URL, public status, source kind, purpose, license, archive
state, GitHub language label, meaningful first-party language paths, and a full
pinned commit. Reject incomplete work, exercise-only material, unlicensed
source, snippet and solution collections, materially obsolete instruction,
generated-code-dominated projects, intentionally bad examples, templates,
mirrors, incidental-language candidates, and artifacts with no coherent
behavior.

Do not reject teaching purpose by itself at Levels 1 and 2. A plausible
educational exemplar proceeds to the separate complete-artifact qualification
gate. Educational source is ineligible at Levels 3 through 5.

GitHub Linguist is evidence, not authority. Generated or vendored files can
dominate its label; explicit first-party path evidence may support a different
catalog classification.

## 4. Inspect one representative learning path

At the pin, review:

1. repository purpose and orientation documentation;
2. one concrete production behavior or, for a lower-level educational
   exemplar, one complete intentional teaching behavior;
3. the public entry point or first source file;
4. the implementation modules and meaningful boundaries in its trace;
5. tests covering the behavior and an important failure or edge case;
6. architecture or developer material needed to understand the boundaries;
7. language-classification evidence; and
8. every file needed to prove the selected-path license expression.

Rank this bounded path, not the whole repository. A large repository does not
require a broad subsystem survey when a smaller representative path is
complete, and total lines of code never enter the calculation.

Dotenv files (`.env`, names ending in `.env`, `.env.*`, and `*.env.*`) are opaque
secrets. Never open, search, print, diff, parse, or source them. Explicitly
exclude all four patterns from every recursive operation.

## 5. Apply both gates

Classify the candidate as production or educational before admission. Apply
the applicable source-qualification gate, the
[coding-relevance gate and eight quality findings](qualification.md) before
scoring. A failed gate rejects even when the corresponding catalog slot is
empty. Record the exact failed condition, evidence, and reconsideration
condition immediately.

## 6. Write path and score evidence

For a passing candidate, record:

- `source_kind` and `purpose_evidence` appropriate to that class;
- a stable `path_slug` that names this learning path inside the repository;
- concrete goal;
- start path and why reading begins there;
- supporting implementation, tests, and documentation;
- entry-to-result trace;
- short prerequisites, distinct concepts developed, and any subordinate domain
  context;
- transferable lessons that follow from those developed concepts;
- recurring signals and reasons for language technique, behavioral reasoning,
  design span, and constraint burden; and
- the pre-accessibility rubric Level from the published formula and
  guardrails.

Write signals and reasons before calculating. Do not inspect the open slot and
work backward to a desired result.

When that rubric Level is 1 or 2, identify central and incidental concepts and
record a `novice_accessibility` floor from 1 through 3. Apply the five-minute
orientation, no-hidden-course, prediction, jargon, and prerequisite-stack
tests in [the learning-level rubric](learning-levels.md). The published Level
is the higher of the rubric Level and accessibility floor. The floor is a
lower-rung guardrail, not a fifth weighted score.

Only after the final Level is known, apply the source restriction. An
educational exemplar at final Level 3 or higher is rejected under the
educational exception unless the same repository independently passes the
production gate and is truthfully reclassified as `production`.

## 7. Resolve capacity honestly

A repository may contribute at most two materially distinct learning paths
across the catalog and may not appear twice in the same `(language, Level)`
bucket. Level 1 and Level 2 each hold at most three paths per language; Levels
3–5 each hold at most two. Three lower-level slots are target capacity, not an
admission quota.

When more candidates qualify than fit, prefer novice accessibility and clarity,
educational value, source quality and correctness, diversity of lessons, then
repository and author diversity. At Levels 1–2, production provenance is only
a tie-breaker. Record other qualified candidates as capacity alternates. Never
move a candidate to a neighboring Level.

## 8. Verification pass and recording

A separate review pass checks both gates, selected path, every score anchor,
formula, low-level accessibility evidence when required, final Level, capacity
result, language, commit, file paths, quality findings, and license evidence.
Record whether a person or a model performed each pass; never turn a model
cross-check into a claim of independent human inspection. Resolve
disagreements against source and the public anchors before acceptance.

Accepted records go in `catalog/<language>.json`; serious failures and
alternates are appended to `research/rejections.json` and the active expansion
audit. Order multiple Level 1 and Level 2 entries from gentlest to most
demanding so each bucket forms a small learning progression. Regenerate and
validate canonical and learner-facing files together.

The current corpus was curated through AI-assisted source inspection and Codex
verification passes under the project owner's direction and acceptance.
Automation checks the schema, paths, formulas, capacity, reconciliation, and
generated output, but source-quality and pedagogical judgments remain review
judgments. Pinned community corrections are welcome.

## 9. Declaring an unresolved gap

A lower-level gap may remain only after recording at least three distinct
discovery channels, serious inspection of multiple plausible candidates,
reconsideration of prior lower-level alternates and rejections, and an actual
educational-exemplar search. Record the result as "unresolved after production
and educational-exemplar research"; do not claim that no suitable project
exists anywhere. A superficial single search is not diligent research. Truth
outranks a full grid.

## 10. Refresh

Automated checks may report dead links, metadata changes, or generated drift.
Changing a pin, gate, path, quality finding, or Level requires a new source
review by a human or an explicitly identified model. Automation never
auto-regrades an entry.

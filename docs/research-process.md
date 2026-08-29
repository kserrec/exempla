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
- package registries and reverse-dependency evidence;
- GitHub language and topic search across varied project sizes;
- software named in production documentation or real workflows;
- respected maintainers' smaller libraries and tools; and
- curated ecosystem lists used only as leads.

Deliberately include smaller and less-famous real software. Do not search for a
desired Level or sort only by stars.

## 3. Triage before deep review

Record canonical URL, public status, genuine purpose, license, archive state,
GitHub language label, meaningful first-party language paths, and a full pinned
commit. Reject tutorials, examples, generated artifacts, mirrors, templates,
incidental-language candidates, and obvious domain-gate failures early.

GitHub Linguist is evidence, not authority. Generated or vendored files can
dominate its label; explicit first-party path evidence may support a different
catalog classification.

## 4. Inspect one representative learning path

At the pin, review:

1. repository purpose and orientation documentation;
2. one concrete production behavior;
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

Apply the [coding-relevance gate and eight quality findings](qualification.md)
before scoring. A failed gate rejects even when the corresponding catalog slot
is empty. Record the exact failed condition, evidence, and reconsideration
condition immediately.

## 6. Write path and score evidence

For a passing candidate, record:

- concrete goal;
- start path and why reading begins there;
- supporting implementation, tests, and documentation;
- entry-to-result trace;
- short prerequisites and any subordinate domain context;
- transferable lessons;
- recurring signals and reasons for language technique, behavioral reasoning,
  design span, and constraint burden; and
- final Level from the published formula and guardrails.

Write signals and reasons before calculating. Do not inspect the open slot and
work backward to a desired result.

## 7. Resolve capacity honestly

At most two repositories may occupy one `(language, Level)` slot. When three or
more qualify, compare educational clarity and path quality, retain the strongest
two, and record the others as qualified capacity alternates. Never move a
candidate to a neighboring Level.

## 8. Independent review and recording

A second reviewer checks both gates, selected path, every score anchor, formula,
capacity result, language, commit, file paths, quality findings, and license
evidence. Resolve disagreements against source and the public anchors before
acceptance.

Accepted records go in `catalog/<language>.json`; serious failures and
alternates are appended to `research/rejections.json`. Regenerate and validate
canonical and learner-facing files together.

## 9. Declaring an unresolved gap

A gap may remain only after recording the three or more discovery channels and
the plausible candidates inspected. A superficial single search is not
diligent research. Truth outranks a full grid.

## 10. Refresh

Automated checks may report dead links, metadata changes, or generated drift.
Changing a pin, gate, path, quality finding, or Level requires a new human
source review. Automation never auto-regrades an entry.

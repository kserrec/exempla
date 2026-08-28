# Candidate research process

This process is systematic enough to be repeatable and deliberately small
enough to keep human source review at its center.

## 1. Discover a varied candidate pool

For one language and one tentative difficulty band, gather candidates from at
least three of these channels:

- official language, foundation, or major ecosystem organizations;
- package registries and reverse-dependency signals;
- GitHub language/topic search across several repository-size ranges;
- software named in production documentation or real user workflows;
- respected maintainers' smaller libraries and tools;
- curated ecosystem lists used only as leads, never as admission evidence.

Include smaller, less-famous projects deliberately. Do not sort only by stars,
and do not use `good first issue` as a discovery or quality criterion.

## 2. Triage eligibility before deep review

Record the canonical URL, public status, default branch, license, archive state,
GitHub language breakdown, project purpose, and a pinned commit. Reject obvious
tutorials, examples, generated artifacts, mirrors, templates, or projects whose
cataloged language is incidental.

GitHub Linguist's top label is evidence, not a verdict. Generated files,
fixtures, embedded intermediate representations, or documentation can dominate
that label. When it differs from the catalog language, record the exact
first-party implementation paths that justify classification; reject the
candidate if the catalog language is not substantial in the real software.

Repository discovery and metadata APIs may automate this triage. They may not
decide quality or SDC level.

## 3. Inspect actual source

At the pinned revision, review enough of the artifact to cover:

1. the top-level structure and documented purpose;
2. a primary entry point or public API;
3. the core implementation behind one meaningful behavior;
4. at least one boundary such as persistence, network, filesystem, process,
   plugin, or platform integration when present;
5. tests that exercise the chosen behavior and an important edge case;
6. architecture/developer documentation and the relevant build manifest.

For a small repository, read most implementation files. For a large repository,
sample at least two major subsystems and trace one behavior end-to-end; do not
pretend that sampling is an exhaustive whole-repository review.

Dotenv files (`.env`, names ending in `.env`, and variants such as `.env.local`
or `service.env.production`) are opaque secrets: never open, search, print,
diff, parse, or source them. Every recursive operation must exclude them.

## 4. Measure S

Run `tokei` against the pinned checkout with the global exclusions in
[`sdc.md`](sdc.md) plus recorded repository-specific generated/vendor/fixture
paths. Store the resulting meaningful implementation LOC, tool version, commit,
date, and exclusions. The reviewer checks that the count represents the code a
learner would actually navigate.

## 5. Apply the quality gate

Write observed evidence for all eight dimensions in
[`qualification.md`](qualification.md). Reject a failed hard requirement even
if the repository would fill an empty SDC slot. Add the reason to
`research/rejections.json`.

## 6. Score D and C independently

Use the anchors and short signal checklists in [`sdc.md`](sdc.md). Write D and C
evidence before calculating the final level. This prevents a desired level from
back-propagating into the dimensions.

## 7. Write the learner path

For accepted candidates, state:

- what the software does and the evidence that it is real-world software;
- why this source is worth studying, not merely why the product is notable;
- concrete concepts a learner can learn;
- prerequisites beyond the assumed learner baseline;
- a suggested starting file or directory and a traceable behavior;
- why S, D, and C produce this placement.

## 8. Review and record

A second review checks the source evidence, hard qualification gate, level, and
language classification. Disagreements cite a rubric anchor and are resolved
before acceptance. The catalog records reviewer identifiers and inspection
date; Git history preserves later changes.

## 9. Refresh

Automated maintenance may detect dead links, changed default revisions, missing
licenses, or generated-page drift. A human repeats source inspection and
scoring before changing quality or difficulty claims. Automation never
auto-admits or auto-regrades a repository.

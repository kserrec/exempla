# Contributing to Exempla

Exempla accepts evidence-backed improvements to a learning catalog. A
repository does not qualify because it is famous, convenient, or needed to
fill a slot. Its selected path must teach transferable programming, pass the
applicable production or educational-exemplar gate, pass the source-quality
gate, and earn its Level from observed evidence.

## Start here

- [Learning levels](docs/learning-levels.md) defines the learner baseline,
  coding-relevance gate, four score dimensions, formula, and guardrails.
- [Repository qualification](docs/qualification.md) defines hard eligibility
  and the eight quality findings.
- [Candidate research](docs/research-process.md) defines discovery, inspection,
  review, and rejection evidence.
- [Catalog source data](catalog/README.md) explains canonical and generated
  files.

Never hand-edit `languages/`; those pages are generated from `catalog/`.

## Choose the right contribution path

- [Propose a repository](https://github.com/kserrec/exempla/issues/new?template=01-repository-candidate.yml)
  after inspecting a pinned learning path and applying both gates and all four
  scores.
- [Report a catalog correction](https://github.com/kserrec/exempla/issues/new?template=02-catalog-correction.yml)
  when direct evidence proves a current fact wrong or outdated.
- [Dispute a learning-level placement](https://github.com/kserrec/exempla/issues/new?template=03-learning-level-dispute.yml)
  when recurring path evidence supports a different rubric anchor.
- [Report a maintenance problem](https://github.com/kserrec/exempla/issues/new?template=04-maintenance-problem.yml)
  for validation, generation, navigation, or workflow defects.

An issue proposes review; it does not pre-approve a repository.

## Local setup

Git and Python 3.12 or newer are sufficient. There are no package dependencies.

```console
git clone https://github.com/kserrec/exempla.git
cd exempla
python3 -m unittest discover -s tests -v
python3 scripts/catalog.py validate
python3 scripts/catalog.py check-generated
```

## Changes we accept

### Correct an existing entry

Verify the exact pinned commit, field, path, and behavior before calling
anything wrong or outdated. Explain the observed discrepancy, make the
smallest supported canonical change, and regenerate Markdown.

### Add or replace a repository

Use the full candidate workflow below. A removal may leave a visible gap.
Never alter a gate or score to preserve a full grid.

### Refresh an accepted repository

A moving default branch does not make pinned evidence stale. Move an entry to
a new commit only after repeating the coding-relevance review, path inspection,
eight quality findings, four scores, language classification, and license
review. Update the inspection date and files as one evidence unit.

### Change the language scope

The 20-language list is a dated product decision. Follow the annual procedure
in [docs/maintenance.md](docs/maintenance.md), preserve the prior basis in Git
history, and update the language registry, rationale, canonical files, tests,
and generated navigation together.

## Candidate workflow

1. **Classify and triage eligibility.** Record `source_kind` and
   `purpose_evidence`. Confirm public source, meaningful first-party code in
   the cataloged language, inspectable license terms, and either genuine
   non-teaching production purpose or every educational-exemplar requirement.
2. **Pin the revision.** Record a full 40-character commit before judging
   source. Do not use a floating branch as evidence.
3. **Choose a representative path.** Assign a stable `path_slug`; name one real
   behavior, its first source file, supporting implementation and tests, and
   an entry-to-result trace. Separate prior knowledge in `prerequisites` from
   the skills taught in `concepts_developed`.
4. **Apply the coding-relevance gate.** Reject paths whose difficulty depends
   primarily on specialist mathematics, science, medicine, finance, law,
   regulation, cryptography, hardware, protocols, or comparable outside
   expertise. Record short subordinate domain context when it is genuinely
   needed.
5. **Apply the quality gate.** Record all eight findings for this exact path.
   A material failure rejects the candidate even when a slot is empty.
6. **Score before consulting gaps.** Record recurring signals and reasons for
   language technique, behavioral reasoning, design span, and constraint
   burden. Calculate the pre-accessibility rubric Level exactly; never work
   backward from a desired slot.
7. **Review novice accessibility at low rubric Levels.** For rubric Level 1 or
   2, identify central and incidental concepts, apply all five accessibility
   tests, and record a floor from 1 through 3. The final Level is the higher of
   the rubric Level and accessibility floor. Do not average the floor with the
   four scores or lower it to fit a slot.
   An educational exemplar whose published result is Level 3 or higher is
   rejected unless it independently qualifies as production software and is
   reclassified truthfully.
8. **Resolve path and slot capacity.** A repository may contribute at most two
   materially distinct paths across the entire catalog and may not appear
   twice in one language/Level bucket. Levels 1 and 2 each hold at most three
   paths; Levels 3–5 each hold at most two. Keep the clearest learning sequence
   and record other qualified candidates as capacity alternates.
9. **Record the decision.** Accepted entries go in
   `catalog/<language>.json`; serious rejections go in
   `research/rejections.json` with evidence and a literal reconsideration
   condition.
10. **Record a separate verification pass.** Name the actual person or model
   that cross-checked both gates, the selected path, each anchor, formula,
   capacity result, language, pin, and license. Never imply independent human
   inspection when a model performed the verification.

Discovery must use at least three independent channels and deliberately include
smaller production projects. Lower-level research must also search official
examples, respected completed teaching artifacts, and small coherent reference
implementations. Stars, downloads, reputation, and beginner labels are leads
at most, never admission evidence.

The current catalog was curated with AI-assisted source inspection and
cross-checking under the project owner's direction and acceptance. Automated
validation proves structural and formula invariants; it cannot independently
prove source quality, educational value, or scoring judgment. Community
corrections with pinned evidence are welcome.

## Canonical entry format

[`catalog/schema.json`](catalog/schema.json) defines schema version 5 and
[`scripts/catalog.py`](scripts/catalog.py) enforces semantic relationships:
safe paths, inspection membership, pinned license URL arrays, formula and score
floors, the novice-accessibility floor for structural Levels 1 and 2,
`(repository, path_slug)` identity, repository and bucket capacity,
prerequisite/concept separation, order, and research reconciliation.

Keep these terms literal:

- `wrong` or `broken`: an existing component was inspected and directly shown
  to behave incorrectly;
- `outdated`: an existing fact no longer matches a stated requirement;
- `missing`: the component does not exist, so creating it is new work; and
- `unverified`: the exact source or behavior has not been checked.

## Generate and verify

Run the ordinary gate while honest gaps remain:

```console
python3 scripts/catalog.py generate
python3 -m unittest discover -s tests -v
python3 scripts/catalog.py validate
python3 scripts/catalog.py check-generated
```

Use `--complete` on both catalog commands only when every language has three
qualified entries at Levels 1 and 2 and two at Levels 3–5. Canonical JSON and
generated Markdown belong in the same commit.

## Scoring disagreements

Name the disputed dimension, cite its published anchor, and point to recurring
evidence in the selected path. All four dimensions are whole integers.
Reviewers resolve the supported anchor rather than averaging scores. Use the
lower anchor when a higher-level signal is isolated or outside the main trace.

## Pull request checklist

- The exact starting state and pinned revision are identified.
- The selected path passes the coding-relevance and quality gates.
- `source_kind` and `purpose_evidence` truthfully establish production or
  educational-exemplar eligibility; educational source is confined to Levels
  1 and 2.
- Stable path slug, goal, start reason, supporting files, trace, prerequisites,
  concepts developed, and domain context describe the path actually scored.
- All four scores cite observed recurring signals and the formula is exact.
- Every rubric-Level-1 or rubric-Level-2 path identifies central and incidental
  concepts, passes the five accessibility tests at its recorded floor, and
  publishes at `max(rubric level, accessibility floor)`.
- Inspection files contain every learning-path and license-evidence path.
- The repository contributes no more than two catalog paths and does not appear
  twice in the same language/Level bucket.
- Accepted and rejected decisions are recorded in the correct canonical files.
- Generated Markdown is current and the applicable ordinary or complete gate
  passes.
- No dotenv file or dotenv naming variant was opened, searched, printed,
  parsed, sourced, diffed, or included in output.

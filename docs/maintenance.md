# Maintaining Exempla

This is the ownership guide for keeping the catalog accurate without turning
its evidence-backed judgments into an automated popularity ranking.

## Source-of-truth map

- `catalog/languages.json` defines the ordered language scope and its source.
- `catalog/<language>.json` is the canonical accepted-entry data.
- `catalog/schema.json` defines the serialized entry shape.
- `scripts/catalog.py` enforces semantic rules and generates learner pages.
- `languages/README.md` and `languages/*/README.md` are generated; never edit
  them directly.
- `research/rejections.json` prevents rejected candidates from being
  rediscovered without new evidence.
- `research/audit.json` records the latest whole-corpus verification.
- `docs/sdc.md`, `docs/qualification.md`, and `docs/research-process.md` define
  the human judgment rules.
- `tests/test_catalog.py` protects validation, scoring boundaries, dotenv-path
  rejection, complete-corpus rules, and deterministic generation.
- `.github/workflows/validate.yml` applies the release gate to pushes and pull
  requests.

The repository has no runtime service and no third-party Python dependencies.
Its product is the reviewed data and the Markdown generated from it.

## Routine verification

Run the complete gate before every release and after any canonical catalog or
generator change:

```console
python3 -m unittest discover -s tests -v
python3 scripts/catalog.py validate --complete
python3 scripts/catalog.py check-generated --complete
```

Run generation only after editing canonical JSON:

```console
python3 scripts/catalog.py generate
```

Generated output and canonical input belong in the same commit. If
`check-generated` reports a stale file, diagnose whether canonical data or the
generator changed before regenerating; do not hand-patch the Markdown.

## Refreshing an accepted entry

1. Establish the verified starting state: exact catalog file, repository,
   pinned commit, start path, sampled files, LOC, S/D/C, license, and GitHub
   metadata.
2. Confirm the pinned repository, commit, start path, and license target still
   resolve publicly. A default-branch move alone does not invalidate pinned
   evidence.
3. Decide whether a refresh is warranted. Use a newer commit only for a factual
   correction, a material upstream change, or an intentional periodic review;
   never silently replace the evidence base.
4. Inspect the new revision from scratch: purpose, entry point, core behavior,
   boundaries, tests, architecture, language classification, and license.
5. Recount meaningful implementation LOC with the global and repository-specific
   exclusions. Reassign S from the count, then judge D and C independently.
6. Reapply all eight quality dimensions and rewrite claims that changed. Do not
   preserve prose merely to minimize the diff.
7. Update the full commit, inspection date, reviewers, sampled files, metadata
   date, start link, license link, LOC evidence, and placement explanation as
   one review unit.
8. Regenerate, verify, and compare the diff with the intended boundary.

If the refreshed revision no longer qualifies, remove the entry and record the
reason in `research/rejections.json`. An honest gap is preferable to retaining
an unsupported recommendation.

## Repository, link, and license drift

- **Renamed or transferred repository:** verify the GitHub redirect and new
  canonical owner/name. Update every canonical URL only if the pinned commit and
  paths resolve under the new location.
- **Deleted or private repository:** remove it; public source inspection is a
  hard requirement. Do not substitute an unverified fork.
- **Archived repository:** archival is not automatic rejection. Reapply the
  archived-project rule in `docs/qualification.md` and disclose the state.
- **Missing pinned commit:** determine whether history was rewritten or the
  repository moved. A replacement commit requires a full source refresh.
- **License changed:** the accepted evidence remains pinned, but moving to a new
  revision requires reviewing its current terms. Preserve compound,
  package-specific, exception, and third-party-notice expressions rather than
  flattening them into a simpler label.
- **GitHub language label changed:** inspect the actual first-party paths.
  Linguist is evidence, not authority, and generated or vendored source can
  dominate it.

## SDC review and disputes

S is mechanical once the meaningful source boundary is correct. D and C are
expert judgments constrained by public anchors.

- Compare disputed entries to neighboring projects with similar S/D/C profiles,
  not merely to projects in the desired slot.
- Cite the exact recurring source signal that supports the higher D or C anchor.
- Use the lower anchor when the higher signal is isolated or outside the main
  learner path.
- Keep whole-number dimensions; never publish decimal repository rankings.
- Apply the arithmetic formula and two guardrails exactly. Do not add a private
  override for one awkward project.
- Resolve disagreement through review and record the reason in prose; do not
  average reviewers' scores.

Corpus-wide changes require a new dated section in `docs/calibration.md` and an
updated `research/audit.json` explaining every measurement or placement change.

## Rejected candidates

Before researching a candidate, search `research/rejections.json`. Reconsider
it only when the recorded condition is now true or the proposed learning track
has materially changed. Add a new dated record rather than erasing the old
decision; Git history should show why the conclusion changed.

A rejection needs a concrete failed requirement and observed evidence. “Not
good enough” and “found a better project” are not reviewable explanations.

## Adding, removing, or replacing a language

Review the language scope annually or when a clearly newer source ranking is
available. A scope change must:

1. preserve the previous source and date in Git history;
2. update `docs/language-selection.md` with the new rule and ambiguous cases;
3. update the order and evidence in `catalog/languages.json`;
4. add or remove the matching canonical language JSON;
5. curate up to two qualified entries for every level without lowered
   standards;
6. update the current 20-language and 200-entry expectations in
   `scripts/catalog.py` and their tests when the scope size changes;
7. regenerate every learner page and repeat the live-facts, distribution, and
   navigation audits; and
8. update the README counts and audit record.

Do not silently swap one language to preserve a fixed count. The selection rule
is part of the public methodology.

## Whole-corpus audit

Repeat the audit before a tagged release and after a material scope change.
For every accepted entry, verify:

- canonical repository and public visibility;
- archive state and sensible language classification;
- exact pinned commit, start path, and license target;
- license terms permitting public source inspection;
- no inappropriate duplicate repository;
- required learner prose, prerequisites, and all eight quality findings;
- correct size band, formula, and guardrails;
- current generated Markdown and root-to-entry navigation; and
- no admission rationale that substitutes stars, downloads, or reputation for
  source evidence.

Record the date, checked commit, method, totals, failures, corrections, and the
literal repository set in `research/audit.json`. Run the final tests from an
isolated committed snapshot, with every dotenv naming variant explicitly
excluded from the snapshot operation.

## Dotenv and secret boundary

Dotenv files are opaque secrets. Never open, read, search, print, diff, parse,
source, or otherwise inspect `.env`, names ending in `.env`, `.env.*`, or
`*.env.*`. Every recursive listing, search, archive, and bulk-content operation
must explicitly exclude those patterns. If maintenance appears to require a
value from one, stop and ask the file's owner to handle it without pasting the
secret into an issue or pull request.

## Release checklist

- Canonical data validates as a complete corpus.
- Unit tests pass on the supported Python version.
- Generated Markdown is current and has no manual edits.
- The live-facts and navigation audits are dated and pass.
- README counts, project status, and maintenance links are current.
- The repository is public and the default branch is `main`.
- GitHub Actions passes on `main`.
- Local `main` matches `origin/main` and the recognized working tree is clean.

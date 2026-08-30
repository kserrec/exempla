# Maintaining Exempla

This is the ownership guide for preserving an evidence-backed learning catalog
without turning judgment into an automated popularity ranking.

## Source-of-truth map

- `catalog/languages.json` is the ordered language-scope registry.
- `catalog/<language>.json` contains accepted schema-version-3 learning paths.
- `catalog/schema.json` publishes the serialized contract.
- `scripts/catalog.py` enforces semantic rules and generates Markdown.
- `languages/**/README.md` is generated and must not be hand-edited.
- `research/learner-centered-rebuild.json` preserves all v1 re-review decisions.
- `research/learner-centered-remediation.json` preserves the 150-path baseline,
  path migration, targeted source checks, capacity decisions, and Level 1 gap
  research from the post-rerun refinement.
- `research/learner-centered-audit.json` is the active learner-centered corpus
  consistency audit.
- `research/rejections.json` is append-only rejection and alternate evidence.
- `research/audit.json` is the historical v1 Size / Difficulty / Complexity
  audit and is not the active consistency record.
- `docs/learning-levels.md`, `docs/qualification.md`, and
  `docs/research-process.md` define source inspection and review judgment.
- `tests/test_catalog.py` protects the formula, gates, paths, licenses,
  reconciliation, gaps, and deterministic generation.
- `.github/workflows/validate.yml` runs the same ordinary gate the README
  claims while gaps exist.

The repository has no runtime service or third-party Python dependency. Its
product is reviewed canonical data and generated Markdown. The current corpus
uses named AI-assisted source-inspection and verification passes under the
project owner's direction and acceptance; automation does not independently
prove source-quality or pedagogical judgments.

## Routine verification

```console
python3 -m unittest discover -s tests -v
python3 scripts/catalog.py validate
python3 scripts/catalog.py check-generated
```

After canonical changes:

```console
python3 scripts/catalog.py generate
```

Use `--complete` on validation and generated checks only when every language
has two qualified learning paths at every Level. Commit canonical input and
generated output together.

## Refreshing an accepted entry

1. Establish the exact catalog file, `(repository, path_slug)` identity, pin,
   learning path, prerequisites, concepts developed, four scores, quality
   findings, inspection files, language evidence, and license URLs.
2. Verify that the pinned repository, commit, every path, and every license
   target remain public. A default-branch move alone does not invalidate them.
3. Move to a new commit only for a factual correction, material upstream
   change, or intentional periodic review.
4. Reinspect the new revision: purpose, selected behavior, implementation,
   tests, boundaries, documentation, language classification, and license.
5. Reapply coding relevance and all eight quality findings.
6. Record recurring evidence for all four dimensions before calculating the
   Level. Repository size remains irrelevant.
7. Update the commit, date, named review passes, inspected files, path, domain
   context, prerequisites, concepts developed, learner prose, scores, metadata,
   and license URLs as one evidence unit.
8. Regenerate, verify, and compare the diff with the intended boundary.

If the refresh no longer qualifies, remove the entry and append the reason. An
honest gap is preferable to unsupported retention.

## Repository, path, and license drift

- **Rename or transfer:** verify the redirect and that the pin and paths resolve
  under the canonical location before changing URLs.
- **Deleted or private:** remove the entry; never substitute an unreviewed fork.
- **Archived:** reapply the archived-project rule and disclose the state;
  archival alone is not rejection.
- **Missing pin:** determine whether history moved. A replacement pin requires a
  full refresh.
- **Changed license:** preserve exact compound, package-specific, exception, and
  third-party-notice terms. Every expression component needs pinned evidence.
- **Changed GitHub language label:** inspect first-party paths. Linguist is
  evidence, not authority.

## Learning-level review and disputes

- Compare the selected paths and their four-score profiles, not repository
  prestige or a desired slot.
- Cite recurring evidence for the disputed anchor.
- Use the lower anchor when the higher signal is isolated or outside the trace.
- Keep whole-number dimensions and apply the public formula exactly.
- Apply the score-4 Level-3 floor, score-5 Level-4 floor, and Level-5 guardrail.
- Do not add private overrides or average reviewer scores; resolve the supported
  anchor in prose.

Corpus-wide corrections belong in `docs/learning-level-calibration.md` and the
current audit with every placement change explained.

## Rejected candidates

Search `research/rejections.json` before reviewing. Reconsider a record only
when its literal condition is now true or the proposed path materially differs.
Append a new dated decision; never erase history. “Not good enough” is not a
reviewable failed requirement.

## Adding, removing, or replacing a language

Review scope annually or when a clearly newer ranking is available. A scope
change must:

1. preserve the prior source and date in Git history;
2. update `docs/language-selection.md` and `catalog/languages.json`;
3. add or remove the matching canonical file;
4. research up to two qualified learning paths per Level without lowered
   standards;
5. update language-count expectations in the validator and tests;
6. regenerate navigation and repeat the live-fact and consistency audits; and
7. update literal counts and gaps in public documentation.

Do not swap a language merely to preserve a fixed total.

## Whole-corpus audit

Before a tagged release and after material scope changes, verify for every
accepted entry:

- public repository, archive state, language classification, globally unique
  `(repository, path_slug)` identity, and the two-path repository cap;
- exact pin and every safe learning-path and inspection path;
- coding-relevance and all eight quality findings;
- four scores, formula and all score floors, bucket capacity, prerequisites,
  concepts developed, their separation, and domain context;
- exact SPDX expression and all pinned license evidence;
- literal counts, honest gaps, generated navigation, and root-to-source links;
  and
- no popularity signal substituted for source inspection.

Record date, checked commit, method, totals, failures, corrections, accepted
set, rejected set, review provenance, and remaining gaps in the current audit.
Run the final gate from an isolated committed snapshot that explicitly excludes
all dotenv naming variants.

## Dotenv and secret boundary

Never open, read, search, print, diff, parse, source, or inspect `.env`, names
ending in `.env`, `.env.*`, or `*.env.*`. Explicitly exclude all four patterns
from every recursive listing, search, archive, and bulk-content operation. If
maintenance seems to require one, the file owner must handle it without pasting
its contents into an issue or pull request.

## Release checklist

- Ordinary validation passes; complete validation also passes only when no gap
  remains.
- Unit tests pass on the supported Python version.
- Generated Markdown is current and unmodified by hand.
- Live-fact, license, path, and navigation audits are dated and pass.
- README counts, project status, and maintenance links are literal.
- GitHub Actions passes on `main`.
- Local and remote `main` agree, and the recognized working tree is clean.

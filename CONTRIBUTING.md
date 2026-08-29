# Contributing to Exempla

Exempla accepts evidence-backed improvements to a curated learning catalog. A
candidate does not qualify because it is famous, convenient, or needed to fill
a slot. Real software, a coherent source-reading path, the full quality gate,
and an honest SDC placement are required every time.

## Start here

Read these documents before proposing a catalog change:

- [Repository qualification](docs/qualification.md) defines hard eligibility
  and the eight pass/fail quality dimensions.
- [SDC difficulty rubric](docs/sdc.md) defines size, code difficulty, system
  complexity, the formula, and guardrails.
- [Candidate research process](docs/research-process.md) defines the evidence
  expected from discovery through review.
- [Catalog source data](catalog/README.md) explains the canonical/generated
  boundary.

Do not hand-edit anything under `languages/`. Those pages are generated from
the JSON under `catalog/`.

## Choose the right contribution path

Use the focused GitHub form that matches the evidence you have:

- [Propose a repository](https://github.com/kserrec/exempla/issues/new?template=01-repository-candidate.yml)
  after inspecting a pinned revision and completing the qualification and SDC
  work. This proposes a review; it does not pre-approve the candidate.
- [Report a catalog correction](https://github.com/kserrec/exempla/issues/new?template=02-catalog-correction.yml)
  when a specific existing fact is demonstrably incorrect at the revision the
  entry records.
- [Dispute an SDC placement](https://github.com/kserrec/exempla/issues/new?template=03-sdc-dispute.yml)
  when observed source signals support a different published rubric anchor.
- [Report a maintenance problem](https://github.com/kserrec/exempla/issues/new?template=04-maintenance-problem.yml)
  for reproducible faults in validation, generation, tests, navigation, or
  contributor documentation.

Blank public issues are disabled so that every report arrives with the minimum
information needed to evaluate it. Maintainers can still open a blank issue
when an unusual case does not fit a form.

If you already have a complete, evidence-backed change, you may open a pull
request directly. GitHub will load the repository's checklist automatically;
answer every applicable section and write `Not applicable` for the others.

## Local setup

You need Git and Python 3.12 or newer. Validation and generation use only the
Python standard library; there is no package installation step.

```console
git clone https://github.com/kserrec/exempla.git
cd exempla
python3 -m unittest discover -s tests -v
python3 scripts/catalog.py validate --complete
python3 scripts/catalog.py check-generated --complete
```

Use `tokei 14.0.0` when measuring a candidate. Its installation is intentionally
not automated by this repository because reviewers may work on different
platforms; record the tool version, exact source scope, and exclusions in the
entry.

## Changes we accept

### Correct an existing entry

Verify the exact pinned commit, field, source path, and behavior before calling
anything wrong or outdated. Explain the observed discrepancy, update the
canonical JSON, regenerate Markdown, and keep the change no broader than the
evidence supports.

### Add or replace a repository

Use the complete candidate workflow below. If removing an entry temporarily
leaves a language or level with fewer than two repositories, leave the honest
gap visible until another candidate passes. Never alter S, D, C, or the quality
gate to preserve a full grid.

### Refresh an accepted repository

A moving default branch does not make the recorded entry stale by itself: its
links and claims are pinned. Move an entry to a newer commit only after
repeating source inspection, meaningful LOC measurement, every quality
judgment, language classification, license review, and SDC scoring. Update the
inspection date and sampled files together.

### Change the language scope

The 20-language list is a dated product decision, not a casual catalog edit.
Follow the annual scope procedure in [docs/maintenance.md](docs/maintenance.md),
update the language-selection rationale and validator expectations, and make
the addition, removal, or replacement explicit.

## Candidate workflow

1. **Triage eligibility.** Confirm the repository is public, the software has a
   genuine purpose, the cataloged language contains meaningful first-party
   implementation, and a pinned license permits source inspection.
2. **Pin the revision.** Record a full 40-character commit before inspecting or
   measuring. Evidence must describe that revision, not a floating branch.
3. **Inspect source.** Review the documented purpose, an entry point, core
   behavior, relevant boundaries, meaningful tests, and architecture or build
   material. Large repositories require representative subsystem sampling and
   one end-to-end trace, not a claim of exhaustive review.
4. **Measure S.** Count first-party implementation with `tokei 14.0.0`. Exclude
   tests, fixtures, benchmarks, examples, vendored, copied, generated or
   minified source, build output, caches, documentation, static assets,
   lockfiles, dumps, and large data. Record repository-specific exclusions.
5. **Apply the quality gate.** Write observed evidence for all eight dimensions.
   A material failure rejects the candidate even when the target slot is empty.
6. **Score D and C independently.** Use the published anchors before calculating
   the final level. Do not choose a desired level and work backward.
7. **Write the learner path.** State what the code teaches, its prerequisites,
   the concrete starting path, and a behavior that can be traced into tests or
   an observable result.
8. **Record the decision.** Add an accepted candidate to the appropriate
   `catalog/<language>.json`. Add a rejected candidate to
   `research/rejections.json` with the failed requirement, evidence, and a
   literal reconsideration condition.
9. **Seek an independent review.** The reviewer checks the source evidence,
   license, language classification, quality gate, LOC scope, D/C anchors, and
   formula. Disputes are resolved before acceptance.

Never use star counts, download counts, reputation, or beginner-labeled issues
as a substitute for inspecting source.

## Canonical entry format

[`catalog/schema.json`](catalog/schema.json) defines the serialized contract and
[`scripts/catalog.py`](scripts/catalog.py) enforces its semantic rules. The best
template is an existing entry in the same language, but every value must be
rewritten from evidence; copying another entry's rationale is not review.

Keep these distinctions literal:

- `wrong` or `broken` means the exact existing behavior was inspected and shown
  to be incorrect;
- `outdated` means an existing fact no longer matches a stated requirement;
- `missing` means the component does not exist; creating it is new work; and
- `unverified` means the exact source or behavior has not been checked yet.

## Generate and verify

During an incomplete replacement, ordinary validation can report record errors
without requiring all 200 entries:

```console
python3 scripts/catalog.py validate
```

Once the canonical JSON is ready, regenerate and run the complete release gate:

```console
python3 scripts/catalog.py generate
python3 -m unittest discover -s tests -v
python3 scripts/catalog.py validate --complete
python3 scripts/catalog.py check-generated --complete
```

Commit canonical JSON and its generated Markdown together. A generated-only
change is not a valid catalog update.

## Scoring disagreements

State which dimension is disputed, quote the relevant rubric anchor, and point
to the observed source signal. S, D, and C remain whole integers. Reviewers do
not average competing scores; they resolve which anchor the evidence supports.
When the higher anchor is uncertain, the rubric requires the lower score unless
the higher-level signal recurs in the main learning path.

## Pull request checklist

- The exact starting state and pinned revision are identified.
- The repository passes every hard qualification requirement.
- Source, tests, boundaries, documentation, language relevance, and license were
  inspected rather than inferred from metadata.
- Meaningful LOC and every exclusion are reproducible.
- D and C cite observed signals and the final level follows the published
  formula and guardrails.
- The learner path names prerequisites, a starting file, and a traceable
  behavior.
- Accepted and rejected decisions are recorded in the correct canonical files.
- Generated Markdown is current and all complete-corpus checks pass.
- No dotenv file or dotenv naming variant was opened, searched, printed,
  parsed, sourced, or included in review output.

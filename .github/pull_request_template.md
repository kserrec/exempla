## Summary

<!-- What does this change do, and why is it needed? -->

## Verified starting state

- Existing file, entry, claim, or behavior:
- Directly observed evidence:
- What this pull request modifies:
- What this pull request creates:
- What remains behaviorally unchanged:

## Change type

- [ ] Catalog candidate, replacement, or refresh
- [ ] Factual catalog correction
- [ ] Learning-level scoring correction
- [ ] Validation or generation tooling
- [ ] Documentation or maintenance only

## Catalog evidence

<!-- Complete this section for catalog changes; otherwise write "Not applicable." -->

- Pinned 40-character revision:
- Coding-relevance evidence and required domain context:
- Stable path slug, learning goal, start path and reason, supporting files, and trace:
- Prerequisites and distinct concepts developed:
- Eight path-specific quality findings:
- Language technique score, recurring signals, and reason:
- Behavioral reasoning score, recurring signals, and reason:
- Design span score, recurring signals, and reason:
- Constraint burden score, recurring signals, and reason:
- Formula result, score-4/score-5/Level-5 guardrails, and transferable lessons:
- Exact SPDX expression and pinned license evidence URL(s):

## Verification

<!-- Paste concise command results. Do not include secrets or dotenv contents. -->

- [ ] `python3 -m unittest discover -s tests -v`
- [ ] `python3 scripts/catalog.py validate`
- [ ] `python3 scripts/catalog.py check-generated`
- [ ] `--complete` was also run only if every catalog slot is genuinely filled.
- [ ] Canonical JSON and generated Markdown changed together, or neither needed regeneration.
- [ ] No catalog standard was lowered to fill a slot.
- [ ] `(repository, path_slug)` is unique; the repository stays within its two-path maximum and does not repeat inside one language/Level bucket.
- [ ] Review-pass labels accurately identify people or models and do not imply unperformed human inspection.
- [ ] Submitted text and output contain no credentials, private data, or dotenv contents.

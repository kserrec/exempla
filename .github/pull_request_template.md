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
- [ ] SDC scoring correction
- [ ] Validation or generation tooling
- [ ] Documentation or maintenance only

## Catalog evidence

<!-- Complete this section for catalog changes; otherwise write "Not applicable." -->

- Pinned 40-character revision:
- Inspected source, test, boundary, and architecture/build paths:
- Meaningful implementation LOC, tool version, scope, and exclusions:
- Qualification evidence:
- S, D, C, final level, and rubric anchors:
- Prerequisites, starting file, and traceable learner behavior:
- License evidence:

## Verification

<!-- Paste concise command results. Do not include secrets or dotenv contents. -->

- [ ] `python3 -m unittest discover -s tests -v`
- [ ] `python3 scripts/catalog.py validate --complete`
- [ ] `python3 scripts/catalog.py check-generated --complete`
- [ ] Canonical JSON and generated Markdown changed together, or neither needed regeneration.
- [ ] No catalog standard was lowered to fill a slot.
- [ ] Submitted text and output contain no credentials, private data, or dotenv contents.

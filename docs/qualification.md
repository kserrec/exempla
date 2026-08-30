# Repository qualification

An accepted entry must pass two independent gates at one pinned public
revision. Coding relevance asks whether the selected path belongs in Exempla;
repository quality asks whether that source is worth learning from. Neither
gate raises or lowers the numerical Level.

## Coding-relevance gate

Apply this gate before scoring. The selected path must:

1. teach transferable programming or software-engineering practice;
2. be explainable from repository documentation plus short prerequisites;
3. derive its difficulty primarily from how the software is built; and
4. represent real production behavior, not a trivial wrapper selected to hide
   the repository's actual difficulty.

Reject when advanced mathematics, scientific, medical, financial, legal, tax,
regulatory, cryptographic, hardware, protocol, or comparable specialist
knowledge explains the path's difficulty better than programming skill does.
A repository may concern a domain when its required context is short,
self-contained, and subordinate to the coding lesson.

## Hard repository eligibility

Every accepted repository must:

1. contain software used for a genuine purpose;
2. expose meaningful first-party implementation in the cataloged language;
3. be publicly readable with license terms permitting source inspection;
4. provide stable implementation, tests, and documentation for review;
5. offer a coherent implementation-to-test learning path; and
6. pass all eight quality findings below without a material red flag.

Reject tutorials, exercises, kata collections, teaching-first projects,
starter templates, contrived examples, source dumps, generated SDKs,
dependency mirrors, and projects selected merely for popularity. Archived
software may qualify when it served a genuine purpose, remains instructive,
has a stable inspectable revision, and is disclosed as archived.

## Eight quality findings

| Finding | Pass condition |
| --- | --- |
| Source quality | Main-path code is readable, intentional, and not dominated by unexplained cleverness or duplication. |
| Architecture | Responsibilities and boundaries in the selected path are recognizable and coherent. |
| Naming and idiom | Names communicate intent and the path demonstrates sound language and ecosystem practice. |
| Tests | Tests reveal behavior, edge cases, or integration contracts rather than superficial coverage. |
| Documentation | Purpose and setup are documented, with enough code or architecture guidance to orient the path. |
| Traceability | The named behavior can be followed from its entry point through implementation to a test or result. |
| Maintainability | The revision is internally consistent and does not teach plainly hazardous maintenance practice as normal design. |
| Educational value | The path teaches identifiable transferable lessons appropriate to its prerequisites and calculated Level. |

A disclosed weakness is acceptable only when it does not undermine the path.
A material failure in source quality, language relevance, genuine purpose, or
educational value always rejects.

## Required accepted evidence

Each canonical entry records:

- repository identity, catalog language evidence, and real-world purpose;
- a stable `path_slug` so the learning path, rather than only the repository,
  has a durable identity;
- the exact commit, review date, reviewers, and inspected files;
- coding-relevance result, short domain context, and transfer reason;
- goal, starting path and reason, supporting implementation and tests, and a
  complete trace;
- prior knowledge in prerequisites, distinct concepts developed by the path,
  and plainly transferable lessons;
- a score, recurring signals, and reason for all four learning dimensions;
- the formula-supported Level and placement explanation;
- one explicit finding for each quality dimension; and
- the exact SPDX expression and every pinned license-evidence URL required to
  prove it.

Stars, downloads, reputation, and beginner labels may support discovery but
cannot substitute for inspected source.

## Rejection record

Every serious rejection is appended to `research/rejections.json` with the
repository, language, review date, exact failed requirement, observed evidence,
and a literal reconsideration condition. Older decisions are never erased.

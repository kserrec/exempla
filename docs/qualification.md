# Source qualification

An accepted entry must pass two independent gates at one pinned public
revision. Coding relevance asks whether the selected path belongs in Exempla;
source quality asks whether the code is worth learning from. Neither gate
raises or lowers the numerical Level.

Every entry declares one `source_kind`:

- `production` — software built primarily for real users, applications,
  libraries, infrastructure, or other software; allowed at Levels 1–5; or
- `educational-exemplar` — a complete software artifact built primarily or
  substantially to teach or demonstrate a programming idea; allowed only at
  Levels 1 and 2.

Teaching purpose is not a difficulty score. An educational exemplar that
calculates to Level 3 or higher is rejected under this exception unless it
independently meets the production-software gate and is truthfully classified
as `production`.

## Coding-relevance gate

Apply this gate before scoring. The selected path must:

1. teach transferable programming or software-engineering practice;
2. be explainable from source documentation plus short prerequisites;
3. derive its difficulty primarily from how the software is built; and
4. represent either genuine production behavior or, at Levels 1–2, complete
   intentional educational behavior in a qualified educational exemplar.

In either source class, the path must be coherent and meaningful. Reject a
trivial wrapper or arbitrary helper chosen to hide the artifact's actual
conceptual burden. Specialist domain knowledge must remain short,
self-contained, and subordinate to the coding lesson.

Reject when advanced mathematics, scientific, medical, financial, legal, tax,
regulatory, cryptographic, hardware, protocol, or comparable specialist
knowledge explains the path's difficulty better than programming skill does.

## Production-software gate

Production source must:

1. perform a genuine non-teaching function;
2. expose meaningful first-party implementation in the cataloged language;
3. be publicly readable with license terms permitting source inspection;
4. provide stable implementation, tests, and documentation for review;
5. offer a coherent implementation-to-test learning path; and
6. pass all eight quality findings below without a material red flag.

Archived production software may qualify when it served a genuine purpose,
remains instructive, has a stable inspectable revision, and is disclosed as
archived.

## Educational-exemplar gate

An educational exemplar must satisfy every condition below.

1. **Complete artifact.** It is a finished small application, library, game,
   utility, reference implementation, completed tutorial application, or
   official example with real behavior. Starter repositories, skeletons,
   TODO-driven exercises, answer keys, and solution collections fail.
2. **Clear educational purpose.** A learner can understand what the artifact
   exists to teach or demonstrate before reading its implementation.
3. **Exemplary source quality.** Direct naming, understandable control flow,
   reasonable decomposition, idiomatic language use, and explicit errors teach
   good habits for the Level. Toy-sized is acceptable; toy-quality is not.
4. **Verifiable behavior.** Prefer automated tests. For a very small artifact,
   deterministic executable examples or golden-output checks may qualify when
   formal tests would add little. Prose alone is insufficient.
5. **Useful documentation.** The project explains what it does, how to run or
   inspect it, and enough context to orient the selected path.
6. **Stable inspectable revision.** The exact revision is pinned. An inactive
   project may qualify only when the code remains runnable or meaningfully
   inspectable and does not present materially obsolete or dangerous practice
   as current good practice.
7. **Public source and license.** The source is publicly inspectable with terms
   that permit source inspection.
8. **Genuine learning value.** The path teaches a coherent transferable lesson
   appropriate to its Level.
9. **Novice-accessibility compliance.** The unchanged novice baseline, floor,
   and all five accessibility tests remain mandatory.
10. **No Level gaming.** The path represents meaningful behavior of the
    exemplar, not an arbitrary low-scoring helper.

Exclude disconnected snippets, gist-like collections, kata, LeetCode,
Codewars, Advent of Code, incomplete scaffolds, generated-code dumps, and
"many examples" repositories whose files do not form coherent software.

## Eight quality findings

| Finding | Pass condition |
| --- | --- |
| Source quality | Main-path code is readable, intentional, and not dominated by unexplained cleverness or duplication. |
| Architecture | Responsibilities and boundaries in the selected path are recognizable and coherent. |
| Naming and idiom | Names communicate intent and the path demonstrates sound language and ecosystem practice. |
| Tests | Tests or deterministic verification reveal behavior, edge cases, or integration contracts rather than superficial coverage. |
| Documentation | Purpose and setup are documented, with enough code or architecture guidance to orient the path. |
| Traceability | The named behavior can be followed from its entry point through implementation to a test or result. |
| Maintainability | The revision is internally consistent and does not teach plainly hazardous maintenance practice as normal design. |
| Educational value | The path teaches identifiable transferable lessons appropriate to its prerequisites and calculated Level. |

A disclosed weakness is acceptable only when it does not undermine the path.
A material failure in source quality, language relevance, truthful purpose, or
educational value always rejects.

## Required accepted evidence

Each canonical entry records:

- `source_kind` and generalized `purpose_evidence` proving either genuine
  non-teaching purpose or the educational exemplar's creator, teaching intent,
  completeness, and credibility;
- repository identity, catalog-language evidence, and a stable `path_slug`;
- the exact commit, review date, reviewers, and inspected files;
- coding-relevance result, short domain context, and transfer reason;
- goal, starting path and reason, supporting implementation and verification,
  and a complete trace;
- prior knowledge in prerequisites, distinct concepts developed by the path,
  and plainly transferable lessons;
- a score, recurring signals, and reason for all four learning dimensions;
- the formula-supported Level and placement explanation;
- low-rubric novice-accessibility evidence;
- one explicit finding for each quality dimension; and
- the exact SPDX expression and every pinned license-evidence URL required to
  prove it.

Stars, downloads, reputation, official status, and beginner labels may support
discovery but cannot substitute for inspected source.

## Rejection record

Every serious rejection is appended to `research/rejections.json` with the
repository, language, review date, exact failed requirement, observed evidence,
and a literal reconsideration condition. Older decisions are never erased.

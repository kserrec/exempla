# Repository qualification

SDC describes difficulty only. A repository enters Exempla only after passing
this separate quality gate at a pinned public revision.

## Hard eligibility requirements

Every accepted repository must:

1. contain software used for a genuine purpose: an application, library, tool,
   runtime, database, compiler, infrastructure system, or comparable artifact;
2. expose meaningful first-party implementation code in the cataloged language;
3. be publicly readable and carry a license that permits source inspection;
4. provide enough stable source, tests, history, and documentation for a
   reviewer to make an evidence-backed judgment;
5. offer a coherent learning path through at least one important behavior; and
6. pass every quality dimension below without a material red flag.

Reject tutorials, exercises, kata collections, “build X to learn Y” projects,
starter templates, contrived examples, source dumps, generated SDKs, dependency
mirrors, abandoned experiments without real use, and projects selected merely
for popularity or beginner-labeled issues.

Archived software may qualify when it served a genuine purpose, remains useful
to study, has an inspectable stable revision, and the entry says plainly that
maintenance ended.

## Quality dimensions

The reviewer records concise evidence for all eight dimensions. These are
pass/fail judgments, not another numerical score.

| Dimension | Pass condition |
| --- | --- |
| Source quality | Main-path code is readable, intentional, and not dominated by cleverness, duplication, or unexplained workarounds. |
| Coherence and architecture | Responsibilities and boundaries are recognizable; organization helps rather than obstructs understanding. |
| Naming and idiom | Names communicate intent and the implementation demonstrates generally sound use of its language/ecosystem. |
| Tests | Meaningful behavior has tests that reveal contracts, edge cases, or integration boundaries rather than only superficial coverage. |
| Documentation | The project explains its purpose and setup; code-level or architectural guidance is sufficient to orient a reader. |
| Traceability | A learner can follow at least one useful behavior from an entry point through implementation to a test or observable result. |
| Maintainability | The studied revision is internally consistent and does not teach plainly hazardous maintenance practices as normal design. |
| Educational value | The repository teaches identifiable techniques or design lessons appropriate to its prerequisites and SDC level. |

A weakness can be disclosed without rejection only when it does not undermine
the main learning path. For example, sparse architecture prose may be offset by
exceptionally clear boundaries and tests. A material failure in source quality,
language relevance, genuine purpose, or educational value always rejects.

## Required evidence

An accepted entry records:

- the pinned commit and inspection date;
- the files or directories sampled for entry points, core behavior, boundaries,
  and corresponding tests;
- evidence of genuine use, preferably the project's own release, adoption, or
  production-purpose documentation;
- one concise finding for each quality dimension;
- what the learner can study, prerequisites, and a concrete suggested starting
  path;
- S/D/C evidence and the final placement explanation;
- license identifier, public URL, and measured primary-language evidence.

Evidence must describe what the reviewer observed. Star counts, download
counts, reputation, and “widely used” claims may corroborate real-world use but
cannot substitute for source inspection.

## Rejection record

Rejected candidates are kept in `research/rejections.json` with repository URL,
language, pinned revision when inspected, date, failed requirement, concise
evidence, and whether a future revision could justify reconsideration. This
prevents repeated low-value review and makes selection bias visible.

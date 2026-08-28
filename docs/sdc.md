# SDC difficulty rubric

SDC answers one question: **how difficult will this repository be to
understand?** It does not decide whether the repository is good learning
material. Admission is governed separately by the
[quality gate](qualification.md).

The rubric is a deliberately broad heuristic. Its success condition is that
experienced programmers generally find the ordering sensible and that few
repositories are wildly easier or harder than their published level suggests.

## Assumed learner

The learner:

- knows the language's syntax, core control flow, common data structures, and
  basic standard library;
- can clone a repository, navigate files, run documented tests, and follow a
  function call across modules;
- has built small programs but is not assumed to know the repository's domain,
  framework, advanced language features, or production architecture.

SDC therefore does not measure the difficulty of learning basic syntax. A
learner missing the stated prerequisites should expect the repository to feel
harder than its level.

## S — Size

S measures the amount of meaningful implementation code a learner may need to
navigate. It is based on code lines reported by
[`tokei`](https://github.com/XAMPPRocky/tokei) at the pinned revision.

| Score | Meaningful implementation LOC |
| --- | ---: |
| S1 | up to 2,000 |
| S2 | 2,001–10,000 |
| S3 | 10,001–50,000 |
| S4 | 50,001–200,000 |
| S5 | more than 200,000 |

The count includes first-party source needed to understand the software even
when it spans multiple languages. It excludes, where present:

- tests, snapshots, test fixtures, benchmarks, and fuzz corpora;
- vendored, copied, or generated source;
- minified files, compiled output, build directories, caches, and coverage;
- documentation, examples written primarily for users, and static assets;
- dependency lockfiles and package-manager contents;
- database dumps and large data files;
- dotenv files and every dotenv naming variant, which are treated as opaque
  secrets and are never opened or searched.

Every entry records the integer LOC, tool, pinned commit, measurement date, and
any repository-specific excluded paths. A measurement is reproducible at that
revision even after the default branch changes.

### Language normalization

There is no default language multiplier. D and C already absorb most meaningful
differences in expressiveness and ecosystem style. If the completed corpus
exposes an obviously unreasonable size placement for a language, a small,
documented language-specific threshold may be added during calibration. No
such exception may be invented for a single repository.

## D — Difficulty

D measures how hard the code itself is to understand after basic language
fluency. The reviewer inspects actual implementation files and uses this short
signal checklist:

- sophisticated algorithms, data structures, mathematics, or domain theory;
- concurrency, parallelism, materially tangled asynchronous flow, or shared
  mutable state;
- advanced types, macros, metaprogramming, reflection, code generation, or
  unusually implicit control flow;
- low-level memory, resource, binary, protocol, or platform management;
- unusually abstract, dense, clever, or non-idiomatic implementation.

The checklist informs one expert judgment; signals are not assigned weights.

| Score | Anchor |
| --- | --- |
| D1 | Direct, idiomatic code using basic language features and little domain knowledge. |
| D2 | Common abstractions or one modest technical concern; local behavior remains easy to trace. |
| D3 | One substantial advanced concern or several moderate ones; prerequisites materially help. |
| D4 | Several advanced concerns, deep domain knowledge, or low-level/implicit behavior recur. |
| D5 | Expert-level implementation such as a compiler, database core, runtime, kernel, or dense concurrent/algorithmic system. |

Every entry names the observed signals and explains the score in prose.

## C — Complexity

C measures how hard the software is to understand as a system. The reviewer
uses this signal checklist:

- number of meaningful components, layers, and cross-module interactions;
- persistence, networking, external services, integrations, or shared state;
- plugins, extension points, multiple execution modes, or cross-cutting logic;
- multi-process or distributed topology and nontrivial build/runtime topology;
- how much of the repository must be understood to trace an important behavior.

Again, the checklist informs one expert judgment rather than a weighted sum.

| Score | Anchor |
| --- | --- |
| C1 | One component; an important behavior can be traced through a few files. |
| C2 | A few clear modules in one process with limited boundaries or integrations. |
| C3 | Several layers or subsystems; tracing behavior crosses meaningful boundaries. |
| C4 | Many interacting components, modes, integrations, or cross-cutting concerns. |
| C5 | A platform-scale, distributed, operating-system, compiler, runtime, or similarly interconnected architecture. |

Every entry names the observed signals and explains the score in prose.

## Final SDC level

1. Compute the arithmetic mean of S, D, and C.
2. Round to the nearest integer, with exact halves rounded upward.
3. If D5 or C5 would otherwise produce SDC 1–3, raise the result to SDC 4.
4. If at least two dimensions are 5, the result is SDC 5.

Examples:

- `S1 / D1 / C1` → mean 1.00 → **SDC 1**
- `S2 / D3 / C2` → mean 2.33 → **SDC 2**
- `S1 / D5 / C2` → mean 2.67, D5 guardrail → **SDC 4**
- `S5 / D2 / C3` → mean 3.33 → **SDC 3**
- `S5 / D5 / C4` → mean 4.67 → **SDC 5**

The guardrail exists because extreme code or system difficulty must not be
hidden by small size. There are no other weights or exceptions.

## Borderline cases and disagreement

- Reviewers assign whole-number S, D, and C scores; half scores are forbidden.
- A score must follow the evidence at the pinned revision, not the desired
  catalog slot.
- When a D or C score sits between two anchors, use the lower score unless the
  higher-level signals recur in the main learning path.
- A second reviewer resolves a disputed dimension by comparing evidence to the
  anchors. The resolution and reason are recorded; scores are never averaged.
- If no qualified repository fits a language/level honestly, the catalog shows
  a gap instead of distorting the rubric.

## Recalculation

Scores describe a pinned commit. A maintenance review first checks whether the
default branch moved materially. If it did, the reviewer repeats the LOC count,
source inspection, D/C judgments, and quality gate at the new commit. Generated
pages are then rebuilt. Historic reasoning remains available in Git history.

# Learning levels

Exempla's levels answer one question: **how advanced are the transferable
programming skills needed to understand one carefully chosen path through this
repository?** The repository's total size, popularity, and subject-matter
prestige do not determine its level.

## Learner baseline

The assumed learner knows the cataloged language's basic syntax, control flow,
functions, common data structures, modules, and ordinary standard-library use.
They have written small programs and can clone a repository, navigate files,
and run documented tests. Advanced language features, production architecture,
concurrency, systems techniques, and specialist subject knowledge are not
assumed.

## Rank a learning path, not a whole repository

Every entry identifies one concrete behavior, the first source file to open,
the supporting implementation and test files, and a trace from entry point or
public API to a test or observable result. Only mechanisms that recur in or are
essential to that path affect its scores. Repository-wide lines of code are not
part of the calculation.

## Coding-relevance gate

Before scoring, the path must primarily teach transferable programming or
software-engineering practice. Its purpose must be understandable from the
repository's documentation plus a short prerequisites paragraph, and any
domain context must remain short and subordinate to the coding lesson.

A path is rejected when advanced mathematics, scientific, medical, financial,
legal, tax, regulatory, cryptographic, hardware, protocol, or comparable niche
expertise explains its difficulty better than programming skill does. A
repository may concern a domain and still qualify when its selected behavior is
self-contained and broadly useful to programmers.

The separate [repository quality gate](qualification.md) remains pass/fail.
Readability, architecture, tests, documentation, traceability,
maintainability, and educational value decide whether a repository is worth
studying; they do not inflate its level.

## Four dimensions

Each dimension receives one whole-number score from 1 through 5.

### Language technique depth

- **1 — Basic:** Direct functions, ordinary collections, simple classes or
  records, basic exceptions, and conventional modules.
- **2 — Common professional idioms:** Interfaces, callbacks, composition,
  iterators, ordinary object-oriented or functional patterns, and standard
  ecosystem conventions.
- **3 — Substantial abstraction:** Generics, protocols or traits, higher-order
  composition, nontrivial type modeling, decorators or annotations, or
  framework idioms materially shape the path.
- **4 — Advanced language machinery:** Advanced type-system features, macros,
  reflection, metaprogramming, code generation, unsafe or low-level facilities,
  or similarly implicit mechanisms recur in important behavior.
- **5 — Expert language fluency:** Multiple advanced mechanisms interact
  pervasively and require expert command of the language.

### Behavioral reasoning

- **1 — Local and direct:** Synchronous, mostly stateless behavior with obvious
  data flow and local errors.
- **2 — Modest state and branching:** Meaningful branches, localized mutable
  state, validation, error paths, or a simple lifecycle remain easy to trace.
- **3 — Nontrivial behavior:** Asynchronous work, persistence, caching, events,
  retries, state transitions, or resource lifecycles materially affect the
  trace.
- **4 — Advanced nonlocal reasoning:** Concurrency, state machines, scheduling,
  event propagation, resource ownership, recovery, or cross-cutting invariants
  recur and must be held together.
- **5 — Expert behavioral reasoning:** Several advanced concerns interact
  pervasively and nonlocal reasoning is unavoidable.

### Design span

- **1 — One focused unit:** The path stays within a few functions or files and
  one clear component.
- **2 — A few clear modules:** One process and a small number of explicit
  boundaries contain the behavior.
- **3 — Several meaningful boundaries:** The trace crosses layers, subsystems,
  adapters, or interfaces whose responsibilities remain locally understandable.
- **4 — Broad architecture:** Many modules, extension points, execution modes,
  integrations, or cross-cutting policies contribute to the path.
- **5 — Platform-scale span:** The path coordinates several major subsystems,
  processes, runtimes, or pervasive extension and policy mechanisms.

### Constraint burden

- **1 — Ordinary correctness:** A small local contract and expected output
  dominate.
- **2 — Routine production safeguards:** Input validation, explicit errors,
  cleanup, basic tests, or a small stable API must be preserved.
- **3 — Several material guarantees:** Persistence or serialization contracts,
  compatibility, portability, performance, reliability, or security boundaries
  influence normal decisions.
- **4 — Interacting strict constraints:** Multiple guarantees such as backward
  compatibility, thread safety, resource bounds, performance, recovery, or
  cross-platform behavior recur across the path.
- **5 — Expert change discipline:** Several system-wide guarantees interact so
  that a locally plausible change can violate correctness, safety,
  compatibility, performance, or reliability elsewhere in the path.

## Final level

Take the arithmetic mean of language technique, behavioral reasoning, design
span, and constraint burden, then round exact halves upward. If any dimension
is 4, the published level is at least 3. If any dimension is 5, the published
level is at least 4. A path reaches Level 5 only when its rounded mean is 5 and
at least two dimensions are themselves 5.

For example, `3 / 3 / 2 / 2` has a mean of 2.50 and becomes **Level 3**.
`4 / 1 / 1 / 1` has a mean of 1.75 but becomes **Level 3** because advanced
machinery in one dimension is not a beginner or intermediate learning burden.
`5 / 2 / 2 / 2` has a mean of 2.75 but becomes **Level 4** because one expert
burden may not be published as beginner or intermediate. `5 / 5 / 4 / 4` has a
mean of 4.50 and becomes **Level 5**.

When a path sits between two anchors, use the lower score unless the higher
anchor recurs in the main trace. Scores follow the inspected evidence at the
pinned revision, never the catalog slot that happens to be open. Public pages
show only integer Level 1 through Level 5.

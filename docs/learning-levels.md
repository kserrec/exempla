# Learning levels

Exempla's levels answer one question: **how advanced are the transferable
programming skills needed to understand one carefully chosen path through this
repository?** The repository's total size, popularity, and subject-matter
prestige do not determine its level.

## Learner baseline

The assumed learner has completed an introductory tutorial in the cataloged
language. They know basic syntax; variables and values; conditionals and loops
where applicable; functions; ordinary strings and common collections; basic
modules, imports, or packages; and basic exceptions or error returns. They
also know simple classes, structs, records, or equivalent fundamentals when
those are part of introductory use in that language. They have written small
exercises or personal programs, can open files in a repository, and can run
documented tests.

Professional experience is not part of the baseline. Unless a concept is
genuinely introductory in the language, the learner is not assumed to know:

- regular-expression grammar, metacharacters, or escaping rules;
- asynchronous scheduling, event loops, concurrency, threads, locks, channels,
  or more than basic exposure to promises and futures;
- advanced generics, type-system machinery, decorators, annotations, macros,
  reflection, or metaprogramming;
- parsers, lexers, abstract syntax trees, compilers, or interpreters;
- cryptographic protocols, networking protocols, or persistence internals;
- Unicode edge cases, operating-system-specific APIs, build systems, bundlers,
  resource-ownership internals, unsafe memory techniques, or framework
  lifecycles; or
- advanced algorithmic theory or specialized domain theory.

These are warning signs, not automatic Level assignments. Do not penalize
fundamentals that a learner must meet while learning the language itself. For
example, basic ownership and borrowing can be introductory Rust, pattern
matching can be introductory in a functional language, and classes can be
introductory Java while irrelevant to C. Record any such language-specific
exception when it materially changes a Level 1 or Level 2 decision.

## Source types across the ladder

Levels 1 and 2 may use production software or a qualified educational
exemplar. Production software is built primarily for real users or systems. An
educational exemplar is a complete, coherent, licensed, verifiable software
artifact intentionally chosen for teaching clarity; exercises, starters,
answer dumps, and disconnected snippets do not qualify.

This is deliberate curriculum design. Real production code commonly assumes
professional concepts before a novice has learned them, and a production-only
rule left the entry ramp too sparse. The four-score formula, guardrails,
learner baseline, novice-accessibility floor, and five tests are unchanged.
Every entry discloses its source type. Level 3 is the explicit transition to
production-only source. Teaching intent never lowers a score: an educational
exemplar whose evidence produces Level 3 or higher is rejected unless it also
independently qualifies and is truthfully classified as production software.

## Level meanings

- **Level 1 — First real code:** The central programming ideas are already in
  the learner baseline. Unfamiliar context is incidental and explainable in
  one or two plain sentences; control flow is local and predictable; and the
  learner does not need to study another topic before understanding why the
  path works. This rung should be a comfortable first serious source-code
  reading.
- **Level 2 — Guided real-world patterns:** One or a few common professional
  concepts may be central, but a short inline primer is enough to begin. The
  path remains locally traceable, prerequisites beyond the baseline are short
  and specific, and unrelated unfamiliar concepts do not pile up.
- **Level 3 — Intermediate production software:** Source is production-only.
  A substantial grammar, theory, lifecycle, protocol, or mental model is
  central; several post-baseline concepts interact; significant ecosystem
  knowledge is required; or the learner needs a separate tutorial before the
  path becomes intelligible.
- **Level 4 — Advanced:** Advanced machinery, architecture, state,
  constraints, or systems reasoning dominates the path.
- **Level 5 — Expert:** Several expert-level burdens interact pervasively.

If you can write small programs in the language, Level 1 is designed to be
your first comfortable step into serious source. An empty Level 1 does not
mean learners should simply jump to Level 2; it means Exempla has not yet found
a path gentle enough to publish there.

## Rank a learning path, not a whole repository

Every entry identifies one concrete behavior, the first source file to open,
the supporting implementation and test files, and a trace from entry point or
public API to a test or observable result. Only mechanisms that recur in or are
essential to that path affect its scores. Repository-wide lines of code are not
part of the calculation.

## Central and incidental concepts

A concept is **central** when it appears in the goal, explains the selected
behavior, is needed to understand why the main transformation or control flow
is correct, recurs in the source trace, determines important tests, or could
not be removed without changing the essential lesson.

A concept is **incidental** when it is one local implementation tool, can be
treated as one understandable operation after a one- or two-sentence
explanation, is not what the path teaches, and does not require its wider
grammar, theory, or ecosystem.

For `sindresorhus/escape-string-regexp`, regular-expression metacharacters and
escaping semantics are central, so its one-function implementation does not by
itself qualify for Level 1. For `sindresorhus/slash`, the local explanation
“this pattern means every backslash” can make its regular-expression literal
incidental because path-separator conversion, not regular-expression grammar,
is the lesson. The latter can still qualify for Level 1 when the rest of its
evidence fits.

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

## Rubric level

Take the arithmetic mean of language technique, behavioral reasoning, design
span, and constraint burden, then round exact halves upward. If any dimension
is 4, this result is at least 3. If any dimension is 5, this result is at least
4. The result reaches 5 only when its rounded mean is 5 and at least two
dimensions are themselves 5. This pre-accessibility result is the **rubric
level**.

For example, `3 / 3 / 2 / 2` has a mean of 2.50 and produces rubric Level 3.
`4 / 1 / 1 / 1` has a mean of 1.75 but produces rubric Level 3 because advanced
machinery in one dimension is not a Level 1 or Level 2 learning burden.
`5 / 2 / 2 / 2` has a mean of 2.75 but produces rubric Level 4 because one
expert burden may not be published as beginner or intermediate. `5 / 5 / 4 /
4` has a mean of 4.50 and produces rubric Level 5.

When a path sits between two anchors, use the lower score unless the higher
anchor recurs in the main trace. Scores follow the inspected evidence at the
pinned revision, never the catalog slot that happens to be open.

## Novice-accessibility floor

When the rubric level is 1 or 2, record a separate
`novice_accessibility` review with central concepts, incidental concepts, a
plain-language reason, and one integer floor:

- **Floor 1:** All central concepts are within the learner baseline;
  unfamiliar concepts are incidental and locally explainable; the path is
  suitable as a first serious source-code reading.
- **Floor 2:** One or a few common professional concepts are central, but a
  short in-entry primer is sufficient for a novice who has already read some
  real code.
- **Floor 3:** One central concept needs meaningful separate background,
  several post-baseline concepts interact, or the learner would probably stop
  to study another subject before continuing.

The published Level is `max(rubric level, accessibility floor)`. The floor is
capped at 3 and is not a fifth score: do not average it with the four
dimensions or assign decimals. Paths whose rubric level is already 3 or above
do not need this lower-rung guardrail.

## Five accessibility tests

Apply all five tests whenever the rubric level is 1 or 2:

1. **Five-minute orientation:** After the title, description, “Why study it?”,
   prerequisites, and short context note, can the learner explain what the
   code will do? If not, Level 1 is impossible and Level 2 is suspect.
2. **No hidden course:** Must the learner first study another topic—such as
   regular-expression grammar, key derivation, parser theory, event-loop
   scheduling, advanced type classes, or memory-ownership internals? If so,
   use at least floor 3 unless the relevant subset is genuinely introductory
   or fully taught in the short introduction.
3. **Prediction:** After the primer, can the learner predict representative
   inputs or test results and explain why they are correct? Mechanical syntax
   tracing alone is insufficient for Level 1.
4. **Jargon:** Level 1 introductions contain no unexplained specialist jargon.
   Level 2 introductions define every unfamiliar term immediately and simply.
5. **Prerequisite stack:** If the effective instruction is “learn A, then B,
   then C, then return,” the path is at least Level 3.

Reviewers resolve Level disputes against both the recurring structural
evidence and these tests. Public pages show only integer Level 1 through Level
5, while low-level entries also explain their accessibility judgment.

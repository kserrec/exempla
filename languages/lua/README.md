# Lua

8 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

**Source legend:** Production software is built primarily for real users or systems. Educational exemplars are complete teaching-oriented software and may appear only at Levels 1 and 2.

**You are not expected to understand the whole repository.** Follow the exact starting lines and focused tests in one entry; everything else can wait.

[← All languages](../README.md)

## Level 1 — First real code

### [rxi/lume](https://github.com/rxi/lume)

**Recommended first path**

**Source:** Production software

Lume's production utility library keeps a number inside a caller-supplied minimum and maximum.

**Just start:** Read lines 82–84 of `lume.lua`, then compare them with `test.lua`.

**Start with: 3 lines of source.** [Open `lume.lua`, lines 82–84.](https://github.com/rxi/lume/blob/98847e7812cf28d3d64b289b03fad71dc704547d/lume.lua#L82-L84)

**Why study it:** Read one transparent expression that returns the lower bound, upper bound, or original value, then verify ordinary, negative, and collapsed ranges.

**Prerequisites:**

- The global novice Lua baseline: functions, local values, comparisons, boolean operators, modules, and direct tests.
- In Lua, `a and b or c` selects b when a is true and otherwise c; here every selected numeric value is truthy.

**Concepts this path develops:**

- Constraining one numeric value to inclusive bounds.
- Expressing three local outcomes with ordered comparisons.
- Testing values below, inside, above, and at a collapsed range.

**Learning path:**

- **Goal:** Understand how lume.clamp returns the nearest inclusive bound or preserves an in-range number.
- **Start here:** [`lume.lua`, lines 82–84](https://github.com/rxi/lume/blob/98847e7812cf28d3d64b289b03fad71dc704547d/lume.lua#L82-L84) — The clamp function contains the complete lower, upper, and in-range decision in one readable expression.
- **Then read:**
  - [`test/test.lua`](https://github.com/rxi/lume/blob/98847e7812cf28d3d64b289b03fad71dc704547d/test/test.lua)
  - [`README.md`](https://github.com/rxi/lume/blob/98847e7812cf28d3d64b289b03fad71dc704547d/README.md)
- **Trace:** Compare x with min, return min when it is lower, otherwise compare x with max and return max or x, then follow the seven direct rows covering inside, outside, negative, and equal-bound cases.

**Why this level:**

**Level 1:** The central lesson is ordinary conditional selection, and one sentence about Lua's expression idiom makes all seven outcomes predictable.

**License:** MIT ([evidence 1](https://github.com/rxi/lume/blob/98847e7812cf28d3d64b289b03fad71dc704547d/LICENSE))

<details>
<summary>Detailed Level, learning, quality, and review evidence</summary>

**What you can learn:**

- Compare the input with the lower bound first.
- Compare with the upper bound only when the lower check did not select a result.
- See why equal bounds always produce that one bound.

**Language 1 / Behavior 1 / Design 1 / Constraints 1 → Level 1**

- **Language technique 1:** The implementation uses introductory Lua function, comparison, and boolean-expression syntax.
- **Behavioral reasoning 1:** The synchronous data flow is visible from left to right in one expression.
- **Design span 1:** The selected contract stays inside one function and seven nearby assertions.
- **Constraint burden 1:** A small local numeric contract and expected outputs dominate the path.
- **Novice accessibility floor 1:** The central lesson is ordinary conditional selection, and one sentence about Lua's expression idiom makes all seven outcomes predictable.
  - **Central concepts:** numeric comparisons; choosing the nearest bound
  - **Incidental concepts:** Lua's `and`/`or` selection idiom
- **Placement:** The four scores 1/1/1/1 produce rubric Level 1. Novice accessibility floor 1 preserves published Level 1.

**Purpose evidence:** Lume is a documented reusable Lua utility library for applications and games, distributed as one importable module with a direct test suite.

**Language evidence:** The complete utility library, clamp implementation, and direct test rows are first-party Lua; GitHub labels the repository Lua.

**Coding relevance:**

Boundary checks, ordered selection, and direct edge-case tests are broadly transferable programming practices.

No specialist domain context is required.

**Eight-part quality gate:**

- **Source quality:** The complete algorithm is a single named expression with no state, allocation, or hidden helper behavior.
- **Architecture:** A focused utility function lives in the library's single documented module beside its direct tests.
- **Naming and idiom:** clamp, x, min, and max state the contract directly using conventional Lua expression style.
- **Tests:** Seven passing direct assertions cover in-range, both bounds, negative ranges, and equal bounds.
- **Documentation:** The README presents Lume as a reusable utility library and documents clamp among its public functions.
- **Traceability:** Every test result follows one of the expression's three visible outcomes.
- **Maintainability:** The one-function contract and broad small boundary matrix make regressions easy to isolate.
- **Educational value:** The path is a comfortable first production reading in Lua with complete behavior and verification.

**Inspection record:** commit `98847e7812cf28d3d64b289b03fad71dc704547d`, inspected 2026-08-30. Review passes: Codex Level 1 language-breadth pass. Files inspected: `lume.lua`, `test/test.lua`, `README.md`, `LICENSE`. GitHub Linguist label: Lua.

</details>

## Level 2 — Guided real-world patterns

### [lunarmodules/say](https://github.com/lunarmodules/say)

**Source:** Production software

A small Lua module that stores named messages, falls back to another namespace, and inserts values into the selected text.

**Just start:** Read lines 1–65 of `init.lua`, then compare them with `say_spec.lua`.

**Start with: 65 lines of source.** [Open `say/init.lua`, lines 1–65.](https://github.com/lunarmodules/say/blob/fe1475fe2acaf844bd030c2ff998bc99ed8930ed/src/say/init.lua#L1-L65)

**Why study it:** Trace one in-memory registry from message storage through active-namespace lookup, fallback lookup, argument checking, and formatted output.

**Short context:**

- A namespaced message registry looks up a string in the active namespace, falls back to another namespace, and substitutes positional values.

**Prerequisites:**

- The global novice Lua baseline, including tables, functions, modules, strings, errors, and focused tests.
- A metatable can make a table callable and define fallback indexing; this module uses one small example of each behavior.

**Concepts this path develops:**

- Storing values under a namespace and key.
- Trying the active namespace before a fallback namespace.
- Using a small metatable to present a callable lookup API.

**Learning path:**

- **Goal:** Understand how a compact Lua module stores namespaced messages, falls back across namespaces, validates interpolation values, and exposes a callable lookup API.
- **Start here:** [`say/init.lua`, lines 1–65](https://github.com/lunarmodules/say/blob/fe1475fe2acaf844bd030c2ff998bc99ed8930ed/src/say/init.lua#L1-L65) — The only production module contains the complete data model and lookup path, so it can be read end to end before its specification.
- **Then read:**
  - [`spec/say_spec.lua`](https://github.com/lunarmodules/say/blob/fe1475fe2acaf844bd030c2ff998bc99ed8930ed/spec/say_spec.lua)
  - [`README.md`](https://github.com/lunarmodules/say/blob/fe1475fe2acaf844bd030c2ff998bc99ed8930ed/README.md)
  - [`LICENSE`](https://github.com/lunarmodules/say/blob/fe1475fe2acaf844bd030c2ff998bc99ed8930ed/LICENSE)
- **Trace:** Read set_namespace, set_fallback, and set to see registry mutation, then follow the __call metamethod through argument validation, active and fallback namespace lookup, string conversion, explicit or inferred argument count, and formatting; finish with __index registry access and the direct specification cases.

**Why this level:**

**Level 2:** One short metatable primer explains the API; registry state, fallback order, validation, and formatting then remain local and directly tested.

**License:** MIT ([evidence 1](https://github.com/lunarmodules/say/blob/fe1475fe2acaf844bd030c2ff998bc99ed8930ed/LICENSE))

<details>
<summary>Detailed Level, learning, quality, and review evidence</summary>

**What you can learn:**

- Trace message storage and lookup through one module-local registry.
- Compare active, fallback, and missing-key results.
- Use tests to understand substitution, nil values, and invalid argument types.

**Language 2 / Behavior 2 / Design 1 / Constraints 2 → Level 2**

- **Language technique 2:** Common professional Lua idioms shape the API without advanced metaprogramming.
- **Behavioral reasoning 2:** Meaningful state and branching remain synchronous, local, and direct.
- **Design span 1:** One focused unit contains the complete behavior.
- **Constraint burden 2:** The path carries routine validation and small stable-API safeguards rather than several material guarantees.
- **Novice accessibility floor 2:** One short metatable primer explains the API; registry state, fallback order, validation, and formatting then remain local and directly tested.
  - **Central concepts:** namespaced message lookup; fallback lookup and positional substitution; callable and indexable metatable behavior
  - **Incidental concepts:** table.unpack compatibility fallback; explicit table length for nil values
- **Placement:** The four structural scores 2/2/1/2 produce rubric Level 2 under the documented formula and guardrails. Novice accessibility floor 2 produces published Level 2.

**Purpose evidence:** Lua developers use the maintained LuaRocks module as the message and localization layer underneath tools including Luassert and Busted.

**Language evidence:** The message registry, namespace fallback, positional substitution, callable interface, and behavior tests are implemented in Lua.

**Coding relevance:**

That short localization vocabulary is subordinate to transferable lessons in table-backed state, metatable call and index behavior, validation, fallback lookup, deterministic formatting, compatibility, and focused specification tests.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The registry, namespace walk, fallback choice, substitutions, and error cases are direct and visible without framework indirection.
- **Architecture:** One private table holds messages while a small module API owns insertion, lookup, fallback selection, and callable dispatch.
- **Naming and idiom:** set, fallback, key, namespace, replacements, and the callable module table describe the mechanism in ordinary Lua vocabulary.
- **Tests:** The specification covers values, namespaces, arguments, nils, fallback behavior, missing keys, type errors, and replacement-count errors.
- **Documentation:** The README shows installation, registration, namespaces, retrieval, interpolation, fallback, and the callable shorthand with runnable examples.
- **Traceability:** A dotted key can be followed from insertion through namespace tables, fallback selection, substitution, and the returned string or error.
- **Maintainability:** A tiny API, no runtime dependencies, explicit validation, and a focused specification keep every behavior locally reviewable.
- **Educational value:** It is an unusually compact example of turning plain tables and metatables into a complete, useful library contract.

**Inspection record:** commit `fe1475fe2acaf844bd030c2ff998bc99ed8930ed`, inspected 2026-08-30. Review passes: Codex primary pass; independent Codex verification pass; Codex novice-accessibility audit. Files inspected: `src/say/init.lua`, `spec/say_spec.lua`, `README.md`, `LICENSE`. GitHub Linguist label: Lua.

</details>

## Level 3 — Intermediate production software

_Ordered from gentler to more demanding within this Level._

### [kikito/middleclass](https://github.com/kikito/middleclass)

**Language 4 / Behavior 3 / Design 1 / Constraints 3 → Level 3**

**Source:** Production software

A compact object-oriented library providing classes, inheritance, instances, mixins, static members, and metamethod support.

**Why study it:** It turns tables and metatables into a recognizable object model while keeping class construction, inheritance, allocation, mixins, and special metamethod handling visible in one file.

**Short context:**

- The library implements classes, instances, inheritance, static members, mixins, and metamethods on top of Lua tables and metatables.

**Prerequisites:**

- Basic Lua tables and functions, metatables and metamethods, colon-method syntax, module loading, inheritance concepts, and Busted-style tests.

**Concepts this path develops:**

- Interacting class, instance, static, and custom-index metatables.
- Recursive propagation through a live subclass hierarchy.
- Declared, inherited, overridden, and removed methods must propagate without clobbering subclass declarations.

**What you can learn:**

- Prototype relationships, metatables, class and instance lookup, inheritance, allocation versus initialization, mixins, static members, metamethod forwarding, and version-sensitive tests.

**Learning path:**

- **Goal:** Understand how a single Lua module builds classes and inheritance by translating method declarations into metatable-backed instance and subclass behavior.
- **Start here:** [`middleclass.lua`](https://github.com/kikito/middleclass/blob/359f0e2742f51ca77801b513ec91eb9029de8de4/middleclass.lua) — The single implementation file builds the class model from the bottom up and exposes every public operation without generated layers.
- **Then read:**
  - [`spec/classes_spec.lua`](https://github.com/kikito/middleclass/blob/359f0e2742f51ca77801b513ec91eb9029de8de4/spec/classes_spec.lua)
  - [`spec/instances_spec.lua`](https://github.com/kikito/middleclass/blob/359f0e2742f51ca77801b513ec91eb9029de8de4/spec/instances_spec.lua)
  - [`spec/mixins_spec.lua`](https://github.com/kikito/middleclass/blob/359f0e2742f51ca77801b513ec91eb9029de8de4/spec/mixins_spec.lua)
  - [`spec/metamethods_spec.lua`](https://github.com/kikito/middleclass/blob/359f0e2742f51ca77801b513ec91eb9029de8de4/spec/metamethods_spec.lua)
  - [`README.md`](https://github.com/kikito/middleclass/blob/359f0e2742f51ca77801b513ec91eb9029de8de4/README.md)
  - [`MIT-LICENSE.txt`](https://github.com/kikito/middleclass/blob/359f0e2742f51ca77801b513ec91eb9029de8de4/MIT-LICENSE.txt)
- **Trace:** Start with _createClass and its class, static, and instance metatables; follow __newindex into _declareInstanceMethod and recursive _propagateInstanceMethod, then trace subclass allocation, inherited initialization, static lookup, custom __index wrapping, mixin inclusion, and metamethod dispatch into the four focused specifications.

**Why this level:**

- **Language technique 4:** Advanced Lua metaprogramming machinery recurs throughout every central behavior.
- **Behavioral reasoning 3:** Nontrivial mutable class relationships must be followed across declarations, subclasses, and instances.
- **Design span 1:** The entire path remains one focused unit despite dense internals.
- **Constraint burden 3:** Several material dispatch, identity, inheritance, and compatibility guarantees influence ordinary changes.
- **Placement:** The four scores 4/3/1/3 sum to 11; their arithmetic mean is 2.75 and rounds half-up to Level 3. The published result is Level 3.

**License:** MIT ([evidence 1](https://github.com/kikito/middleclass/blob/359f0e2742f51ca77801b513ec91eb9029de8de4/MIT-LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The maintained LuaRocks library is used by applications and games that want a small conventional class abstraction without a framework.

**Language evidence:** Class creation, inheritance, allocation, mixins, metamethod propagation, and the complete test suite are handwritten Lua.

**Coding relevance:**

The path is entirely transferable language and library engineering: dynamic dispatch, method declaration and propagation, inheritance, allocation, mixin composition, weak subclass tracking, custom indexing, and behavioral self-tests.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Class construction, lookup chains, allocation, subclass tracking, mixin inclusion, and metamethod copying are small explicit functions.
- **Architecture:** One file separates instance behavior, class behavior, static lookup, subclass creation, and mixin inclusion through named internal tables.
- **Naming and idiom:** class, subclass, allocate, initialize, include, isInstanceOf, isSubclassOf, __instanceDict, and static expose the object model clearly.
- **Tests:** Eight focused specifications cover classes, instances, default methods, inheritance, mixins, ordinary metamethods, and Lua version differences.
- **Documentation:** The README explains class creation, constructors, inheritance, class variables, identity checks, mixins, metamethods, and performance boundaries.
- **Traceability:** A class definition can be followed through its instance dictionary and metatables into subclassing, allocation, initialization, lookup, and assertions.
- **Maintainability:** A stable small surface, dependency-free implementation, deliberate compatibility logic, and focused tests make semantic changes easy to review.
- **Educational value:** It demonstrates how a familiar abstraction can be built honestly from a language's native object primitives rather than hidden machinery.

**Inspection record:** commit `359f0e2742f51ca77801b513ec91eb9029de8de4`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `middleclass.lua`, `spec/classes_spec.lua`, `spec/instances_spec.lua`, `spec/mixins_spec.lua`, `spec/metamethods_spec.lua`, `README.md`, `MIT-LICENSE.txt`. GitHub Linguist label: Lua.

</details>

### [openresty/lua-resty-lrucache](https://github.com/openresty/lua-resty-lrucache)

**Language 4 / Behavior 3 / Design 2 / Constraints 4 → Level 3**

**Source:** Production software

An in-process least-recently-used cache for OpenResty with expiry, stale reads, user flags, bounded capacity, and table-backed or pure-FFI storage.

**Why study it:** Two implementations preserve one contract while exposing hash lookup, a doubly linked recency queue, expiration semantics, stale recovery, FFI memory layouts, and capacity tradeoffs.

**Short context:**

- A bounded least-recently-used cache promotes reads, evicts the least recent entry at capacity, and can expire entries by time-to-live.

**Prerequisites:**

- Comfortable Lua tables and modules, linked lists and hash maps, cache terminology, timestamps, LuaJIT FFI basics, and OpenResty request phases.

**Concepts this path develops:**

- LuaJIT FFI cdefs, arrays, structs, pointer arithmetic, casts, and memory fill.
- Promotion, replacement, eviction, expiration, deletion, and flush transitions.
- Queue links, sentinels, pointer identity, key-node maps, counts, and capacity must remain mutually consistent.

**What you can learn:**

- LRU invariants, hash-table and linked-list coordination, TTL expiration, stale reads, user flags, LuaJIT FFI structures, capacity accounting, cache flushing, and Nginx integration tests.

**Learning path:**

- **Goal:** Understand how an OpenResty Lua cache maintains bounded LRU order, expiration, flags, and constant-time lookup across its FFI-backed representations.
- **Start here:** [`resty/lrucache.lua`](https://github.com/openresty/lua-resty-lrucache/blob/ad373f457a091ffa85de984938f948bc1721d922/lib/resty/lrucache.lua) — The table-backed implementation presents the public API and recency invariants most directly before the equivalent pure-FFI representation.
- **Then read:**
  - [`lib/resty/lrucache/pureffi.lua`](https://github.com/openresty/lua-resty-lrucache/blob/ad373f457a091ffa85de984938f948bc1721d922/lib/resty/lrucache/pureffi.lua)
  - [`t/001-sanity.t`](https://github.com/openresty/lua-resty-lrucache/blob/ad373f457a091ffa85de984938f948bc1721d922/t/001-sanity.t)
  - [`t/100-pureffi/001-sanity.t`](https://github.com/openresty/lua-resty-lrucache/blob/ad373f457a091ffa85de984938f948bc1721d922/t/100-pureffi/001-sanity.t)
  - [`t/008-user-flags.t`](https://github.com/openresty/lua-resty-lrucache/blob/ad373f457a091ffa85de984938f948bc1721d922/t/008-user-flags.t)
  - [`README.markdown`](https://github.com/openresty/lua-resty-lrucache/blob/ad373f457a091ffa85de984938f948bc1721d922/README.markdown)
- **Trace:** Start with queue cdefs, allocation, pointer conversion, and new; follow set through free-node acquisition or tail eviction, bidirectional map updates, queue removal and head insertion, TTL and flags; follow get promotion and stale reporting, then delete and flush recycling; compare pureffi's representation and close equivalent behavior in both sanity suites and the flag suite.

**Why this level:**

- **Language technique 4:** Advanced low-level LuaJIT and representation machinery recurs throughout cache operations.
- **Behavioral reasoning 3:** Nontrivial mutable cache state spans several linked representations but remains within one object.
- **Design span 2:** A few clear modules and representations contain the behavior.
- **Constraint burden 4:** Multiple strict memory, representation, performance, lifecycle, and compatibility guarantees interact.
- **Placement:** The four scores 4/3/2/4 sum to 13; their arithmetic mean is 3.25 and rounds half-up to Level 3. The published result is Level 3.

**License:** BSD-2-Clause ([evidence 1](https://github.com/openresty/lua-resty-lrucache/blob/ad373f457a091ffa85de984938f948bc1721d922/README.markdown))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** OpenResty maintains the library for production Nginx and LuaJIT applications that need per-worker caching without shared-memory serialization overhead.

**Language evidence:** Both the table-backed and pure-FFI cache implementations, queue management, expiry logic, flags, and OpenResty tests are Lua.

**Coding relevance:**

That standard data-structure context is subordinate to transferable lessons in LuaJIT FFI structs and pointers, intrusive queues, bidirectional key-node indexes, bounded allocation, eviction, expiration, flags, representation parity, and invariant-focused tests.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Queue mutations, hash entries, expiration checks, stale returns, flag handling, capacity enforcement, and FFI allocations are explicit and localized.
- **Architecture:** A conventional table implementation and a pure-FFI implementation expose the same cache API while isolating their storage mechanics.
- **Naming and idiom:** get, set, delete, flush_all, get_keys, capacity, count, queue, free_queue, key2node, and node2key reveal contract and representation.
- **Tests:** Parallel Test::Nginx suites exercise construction, hits, misses, false values, eviction, expiration, stale values, flushing, capacity, counts, keys, flags, and mixed workloads.
- **Documentation:** The README explains per-worker scope, performance rationale, installation, every method, stale semantics, FFI constraints, and the BSD license.
- **Traceability:** A write can be followed into a hash entry and queue node, then through lookup, expiry, recency promotion, eviction, deletion, or stale return.
- **Maintainability:** A shared public contract, mirrored integration suites, explicit invariants, and separation between table and FFI storage contain low-level risk.
- **Educational value:** It is a concise bridge from textbook LRU behavior to the memory and expiry details required by a production runtime.

**Inspection record:** commit `ad373f457a091ffa85de984938f948bc1721d922`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `lib/resty/lrucache.lua`, `lib/resty/lrucache/pureffi.lua`, `t/001-sanity.t`, `t/100-pureffi/001-sanity.t`, `t/008-user-flags.t`, `README.markdown`. GitHub Linguist label: Lua.

</details>

## Level 4 — Advanced

_Ordered from gentler to more demanding within this Level._

### [lunarmodules/busted](https://github.com/lunarmodules/busted)

**Language 4 / Behavior 4 / Design 3 / Constraints 4 → Level 4**

**Source:** Production software

A full testing framework with nested contexts, hooks, asynchronous completion, filtering, randomized execution, multiple source loaders, and pluggable reporters.

**Why study it:** Busted's synchronous core shows how a dynamic Lua DSL becomes a nested block tree and executes with exact hooks, events, failures, pending state, and cleanup order.

**Short context:**

- A test framework registers nested describe and it blocks, runs setup and teardown hooks in defined order, and reports pass, fail, pending, and error results.

**Prerequisites:**

- Readers should know Lua tables, metatables, closures, varargs, protected calls, environment scoping, recursive trees, and basic test-framework hooks and result states.

**Concepts this path develops:**

- Dynamic describe, it, hook, and pending DSL injection.
- Separate discovery and execution over a nested block tree.
- Discovery must not accidentally execute test bodies and nested order must remain exact.

**What you can learn:**

- Trace describe, it, hook, and pending registration into block nodes, then through discovery, environment scoping, recursive execution, protected callbacks, teardown, cleanup, and results.

**Learning path:**

- **Goal:** Understand how Busted builds a nested test block tree from its DSL and executes it synchronously with correct hook, event, error, pending, and cleanup order.
- **Start here:** [`busted/core.lua`](https://github.com/lunarmodules/busted/blob/22f8089f461a563fb9553ab56f926c6805850833/busted/core.lua) — The reviewed trace begins in busted/core.lua because Core constructs the public DSL and registers each block, test, hook, tag, and pending case into the execution tree.
- **Then read:**
  - [`busted/block.lua`](https://github.com/lunarmodules/busted/blob/22f8089f461a563fb9553ab56f926c6805850833/busted/block.lua)
  - [`busted/environment.lua`](https://github.com/lunarmodules/busted/blob/22f8089f461a563fb9553ab56f926c6805850833/busted/environment.lua)
  - [`busted/execute.lua`](https://github.com/lunarmodules/busted/blob/22f8089f461a563fb9553ab56f926c6805850833/busted/execute.lua)
  - [`busted/runner.lua`](https://github.com/lunarmodules/busted/blob/22f8089f461a563fb9553ab56f926c6805850833/busted/runner.lua)
  - [`busted/modules/test_file_loader.lua`](https://github.com/lunarmodules/busted/blob/22f8089f461a563fb9553ab56f926c6805850833/busted/modules/test_file_loader.lua)
  - [`spec/core_spec.lua`](https://github.com/lunarmodules/busted/blob/22f8089f461a563fb9553ab56f926c6805850833/spec/core_spec.lua)
  - [`spec/execution_order_sync_spec.lua`](https://github.com/lunarmodules/busted/blob/22f8089f461a563fb9553ab56f926c6805850833/spec/execution_order_sync_spec.lua)
  - [`README.md`](https://github.com/lunarmodules/busted/blob/22f8089f461a563fb9553ab56f926c6805850833/README.md)
  - [`LICENSE`](https://github.com/lunarmodules/busted/blob/22f8089f461a563fb9553ab56f926c6805850833/LICENSE)
- **Trace:** Start with Core registering describe, it, hooks, pending, and tags into Block nodes, follow Environment and the test-file loader through discovery, then trace Runner and Execute recursively through setup, child execution, event emission, protected errors, pending state, teardown, cleanup, and results; close the exact synchronous order in core_spec and execution_order_sync_spec. Do not use the pending async specification as evidence.

**Why this level:**

- **Language technique 4:** Advanced dynamic-language and environment machinery recurs across registration and execution.
- **Behavioral reasoning 4:** Advanced nonlocal lifecycle and recovery reasoning recurs across nested callbacks and state.
- **Design span 3:** Several meaningful framework boundaries cooperate while the broader output and pending async surfaces are excluded.
- **Constraint burden 4:** Multiple strict lifecycle, isolation, recovery, extension, and compatibility guarantees interact.
- **Placement:** The four scores 4/4/3/4 sum to 15; their arithmetic mean is 3.75 and rounds half-up to Level 4. The published result is Level 4.

**License:** MIT ([evidence 1](https://github.com/lunarmodules/busted/blob/22f8089f461a563fb9553ab56f926c6805850833/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The maintained LuaRocks tool runs real project suites from the command line and provides the standard framework around Luassert assertions.

**Language evidence:** Test-tree construction, hooks, execution, filtering, loaders, configuration, status reporting, output handlers, and self-tests are Lua.

**Coding relevance:**

That standard testing vocabulary is subordinate to transferable lessons in dynamic DSL construction, block trees, event publication, environment scoping, recursive synchronous execution, hook ordering, failure recovery, filtering, result state, and self-hosting tests.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** core.lua and block.lua expose DSL registration and tree structure, while environment.lua, runner.lua, execute.lua, and the file loader separate discovery, scope, and execution.
- **Architecture:** A dynamically installed DSL builds nested Block nodes during discovery, and Runner plus Execute recursively apply hooks, callbacks, events, errors, pending state, cleanup, and results.
- **Naming and idiom:** Core, Block, Environment, Runner, Execute, describe, it, setup, teardown, pending, and events mirror the test lifecycle through idiomatic Lua tables and callbacks.
- **Tests:** core_spec.lua and execution_order_sync_spec.lua directly cover nesting, registration, hook order, failures, pending cases, cleanup, and synchronous lifecycle behavior.
- **Documentation:** README.md documents the DSL, hooks, pending tests, and execution model used by the selected path.
- **Traceability:** A describe or it call can be followed into a Block node, through scoped recursive execution and event publication, and into exact order assertions in the synchronous specifications.
- **Maintainability:** Registration, environment control, file loading, running, and execution are separated, and the selected evidence explicitly excludes pending asynchronous examples.
- **Educational value:** The path demonstrates how a concise dynamic testing DSL depends on a carefully ordered and recoverable execution lifecycle.

**Inspection record:** commit `22f8089f461a563fb9553ab56f926c6805850833`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `busted/core.lua`, `busted/block.lua`, `busted/environment.lua`, `busted/execute.lua`, `busted/runner.lua`, `busted/modules/test_file_loader.lua`, `spec/core_spec.lua`, `spec/execution_order_sync_spec.lua`, `README.md`, `LICENSE`. GitHub Linguist label: Lua.

</details>

### [lunarmodules/luacheck](https://github.com/lunarmodules/luacheck)

**Language 3 / Behavior 5 / Design 4 / Constraints 5 → Level 4**

**Source:** Production software

A static analyzer and command-line linter that reports globals, unused values, control-flow mistakes, whitespace problems, complexity, and configuration-sensitive warnings.

**Why study it:** The selected Luacheck path exposes a complete static-analysis trace from source tokens and syntax nodes through control-flow linearization, lexical-scope resolution, unused-local detection, and final warning filtering.

**Short context:**

- A static analyzer tokenizes and parses Lua source, resolves scopes and control flow, detects warnings, and filters them through configuration.

**Prerequisites:**

- Working familiarity with Lua functions, tables, modules, metatables at a basic level, protected calls, and unit tests, plus experience tracing behavior across several production files.

**Concepts this path develops:**

- Closure-based lexer and recursive-descent parser machinery.
- Lexical position, token, syntax, control-flow, scope, definition, access, value, mutation, and warning state interact.
- Every Lua syntax and dialect form must preserve exact token, source-range, scope, control-flow, definition, use, mutation, and closure semantics.

**What you can learn:**

- Use `src/luacheck/check.lua` to study lexing, parsing, syntax-tree normalization, control-flow linearization, nested lexical scopes, definition and access tracking, unused-local analysis, warning locations, option filtering, and focused end-to-end specifications.

**Learning path:**

- **Goal:** Understand how Luacheck turns Lua source into scoped analysis facts and then emits and filters warnings without losing source locations or control-flow meaning.
- **Start here:** [`luacheck/check.lua`](https://github.com/lunarmodules/luacheck/blob/2f764bdcabe8b7c19deadf0e9bb2adc19df1a4c5/src/luacheck/check.lua) — check.lua lists the exact parse-to-warning stage sequence and gives the selected lexer, parser, linearizer, resolver, detector, and filter modules a clear orchestration point.
- **Then read:**
  - [`src/luacheck/lexer.lua`](https://github.com/lunarmodules/luacheck/blob/2f764bdcabe8b7c19deadf0e9bb2adc19df1a4c5/src/luacheck/lexer.lua)
  - [`src/luacheck/parser.lua`](https://github.com/lunarmodules/luacheck/blob/2f764bdcabe8b7c19deadf0e9bb2adc19df1a4c5/src/luacheck/parser.lua)
  - [`src/luacheck/stages/linearize.lua`](https://github.com/lunarmodules/luacheck/blob/2f764bdcabe8b7c19deadf0e9bb2adc19df1a4c5/src/luacheck/stages/linearize.lua)
  - [`src/luacheck/stages/resolve_locals.lua`](https://github.com/lunarmodules/luacheck/blob/2f764bdcabe8b7c19deadf0e9bb2adc19df1a4c5/src/luacheck/stages/resolve_locals.lua)
  - [`src/luacheck/stages/detect_unused_locals.lua`](https://github.com/lunarmodules/luacheck/blob/2f764bdcabe8b7c19deadf0e9bb2adc19df1a4c5/src/luacheck/stages/detect_unused_locals.lua)
  - [`src/luacheck/filter.lua`](https://github.com/lunarmodules/luacheck/blob/2f764bdcabe8b7c19deadf0e9bb2adc19df1a4c5/src/luacheck/filter.lua)
  - [`spec/check_spec.lua`](https://github.com/lunarmodules/luacheck/blob/2f764bdcabe8b7c19deadf0e9bb2adc19df1a4c5/spec/check_spec.lua)
  - [`spec/resolve_locals_spec.lua`](https://github.com/lunarmodules/luacheck/blob/2f764bdcabe8b7c19deadf0e9bb2adc19df1a4c5/spec/resolve_locals_spec.lua)
  - [`README.md`](https://github.com/lunarmodules/luacheck/blob/2f764bdcabe8b7c19deadf0e9bb2adc19df1a4c5/README.md)
  - [`LICENSE`](https://github.com/lunarmodules/luacheck/blob/2f764bdcabe8b7c19deadf0e9bb2adc19df1a4c5/LICENSE)
- **Trace:** Begin with check.lua's exact stage sequence, follow tokens and locations from lexer into parser syntax nodes, then trace linearize's control-flow representation, resolve_locals' nested scopes, definitions, accesses and values, detect_unused_locals' cross-scope warning decisions, and final option filtering; close end-to-end and local-resolution contracts in the two direct specifications.

**Why this level:**

- **Language technique 3:** Substantial Lua abstractions materially shape the analyzer, but advanced metaprogramming is not pervasive.
- **Behavioral reasoning 5:** Several advanced analysis concerns interact pervasively, so expert nonlocal reasoning across stages is unavoidable.
- **Design span 4:** A broad but explicit analyzer architecture contributes to the selected source-to-warning path.
- **Constraint burden 5:** Several system-wide semantic, diagnostic, compatibility, determinism, and performance guarantees require expert change discipline.
- **Placement:** The four scores 3/5/4/5 sum to 17; their arithmetic mean is 4.25 and rounds half-up to Level 4. The published result is Level 4.

**License:** MIT ([evidence 1](https://github.com/lunarmodules/luacheck/blob/2f764bdcabe8b7c19deadf0e9bb2adc19df1a4c5/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The maintained LuaRocks and command-line tool checks applications and libraries locally and in continuous integration across configurable language standards.

**Language evidence:** Lexing, parsing, AST passes, control-flow linearization, local resolution, warning detectors, configuration, filtering, caching, CLI behavior, and tests are Lua.

**Coding relevance:**

The path is transferable compiler and tooling engineering: lexing, parsing, intermediate representation, staged analysis, scope and data-flow state, warning construction, filtering, configuration, diagnostics, and direct stage tests.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The selected modules keep tokens, syntax nodes, linear instructions, scopes, definitions, accesses, warning codes, source locations, and suppression decisions explicit.
- **Architecture:** The lexer and parser feed ordered linearization, local-resolution, and unused-local stages before check.lua applies options and the filter module selects warnings.
- **Naming and idiom:** lexer, parser, linearize, resolve_locals, detect_unused_locals, filter, definitions, accesses, and warnings expose the selected compiler roles.
- **Tests:** check_spec and resolve_locals_spec close end-to-end checking, source-location behavior, nested scope resolution, definitions, accesses, and local-warning cases used by this path.
- **Documentation:** The README explains Luacheck's warning model, codes, inline and configured options, and filtering behavior needed to understand the selected analysis result.
- **Traceability:** A source token can be followed into a syntax node, through linearization and nested-scope resolution, into unused-local detection and filtering, then matched to focused check or resolver assertions.
- **Maintainability:** Ordered stages, explicit intermediate representations, numbered warnings, and focused resolver specifications localize semantic changes in the selected analysis path.
- **Educational value:** This path presents a demanding but inspectable compiler-style pipeline without claiming uninspected caching, concurrency, formatter, or command-line subsystems.

**Inspection record:** commit `2f764bdcabe8b7c19deadf0e9bb2adc19df1a4c5`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/luacheck/check.lua`, `src/luacheck/lexer.lua`, `src/luacheck/parser.lua`, `src/luacheck/stages/linearize.lua`, `src/luacheck/stages/resolve_locals.lua`, `src/luacheck/stages/detect_unused_locals.lua`, `src/luacheck/filter.lua`, `spec/check_spec.lua`, `spec/resolve_locals_spec.lua`, `README.md`, `LICENSE`. GitHub Linguist label: Lua.

</details>

## Level 5 — Expert

_Ordered from gentler to more demanding within this Level._

### [apache/apisix](https://github.com/apache/apisix)

**Language 4 / Behavior 5 / Design 5 / Constraints 5 → Level 5**

**Source:** Production software

A cloud-native API and AI gateway with dynamic routing, load balancing, policy plugins, observability, standalone and distributed configuration modes, and HTTP, stream, and extensible runtime paths.

**Why study it:** APISIX's API-driven standalone configuration path is an expert trace through validation, monotonic resource versions, shared memory, subsystem-specific events, per-worker polling, hot route rebuilds, and safe traffic handling before the first configuration arrives.

**Short context:**

- API-driven standalone mode accepts a complete gateway configuration through an Admin API, stores it in shared memory, and hot-updates each worker without restarting the gateway.
- OpenResty's HTTP and stream subsystems use separate Lua virtual machines and event sockets, so stream workers poll shared state even when HTTP workers can receive an event directly.

**Prerequisites:**

- Comfort with Lua modules, tables, metatables, closures, protected calls, and callback-based code.
- Familiarity with HTTP requests, JSON documents, validation, and the idea that multiple server processes may handle requests concurrently.
- Basic knowledge that APISIX and OpenResty run Lua handlers inside Nginx worker phases; the required project-specific worker model is summarized below.

**Concepts this path develops:**

- Atomic full-configuration validation and publication with digest idempotence and monotonic resource versions.
- Cross-worker convergence through shared dictionaries, direct events, and polling across separate Lua virtual machines.
- Hot router reconstruction and safe empty-startup behavior while live traffic continues.

**What you can learn:**

- Trace a full configuration update from the Admin API through validation, version and digest decisions, shared-memory publication, HTTP and stream worker synchronization, per-resource cache mutation, route rebuild, and request behavior before and after configuration arrives.

**Learning path:**

- **Goal:** Understand how APISIX validates and distributes an API-driven standalone configuration across HTTP and stream workers while preserving version order, idempotence, hot routing, and safe behavior before the first update.
- **Start here:** [`admin/standalone.lua`](https://github.com/apache/apisix/blob/a64f2baa06b1c7d55e53051f3430f39bf9f4024c/apisix/admin/standalone.lua) — The reviewed trace begins in standalone.lua because its update handler owns request parsing, digest idempotence, full-resource version decisions, shared-memory publication, worker notification, and the cross-subsystem polling fallback.
- **Then read:**
  - [`apisix/admin/config_validate.lua`](https://github.com/apache/apisix/blob/a64f2baa06b1c7d55e53051f3430f39bf9f4024c/apisix/admin/config_validate.lua)
  - [`apisix/core/config_yaml.lua`](https://github.com/apache/apisix/blob/a64f2baa06b1c7d55e53051f3430f39bf9f4024c/apisix/core/config_yaml.lua)
  - [`apisix/events.lua`](https://github.com/apache/apisix/blob/a64f2baa06b1c7d55e53051f3430f39bf9f4024c/apisix/events.lua)
  - [`apisix/router.lua`](https://github.com/apache/apisix/blob/a64f2baa06b1c7d55e53051f3430f39bf9f4024c/apisix/router.lua)
  - [`apisix/stream/router/ip_port.lua`](https://github.com/apache/apisix/blob/a64f2baa06b1c7d55e53051f3430f39bf9f4024c/apisix/stream/router/ip_port.lua)
  - [`apisix/init.lua`](https://github.com/apache/apisix/blob/a64f2baa06b1c7d55e53051f3430f39bf9f4024c/apisix/init.lua)
  - [`t/admin/standalone.t`](https://github.com/apache/apisix/blob/a64f2baa06b1c7d55e53051f3430f39bf9f4024c/t/admin/standalone.t)
  - [`t/admin/standalone-stream.t`](https://github.com/apache/apisix/blob/a64f2baa06b1c7d55e53051f3430f39bf9f4024c/t/admin/standalone-stream.t)
  - [`t/admin/standalone.spec.ts`](https://github.com/apache/apisix/blob/a64f2baa06b1c7d55e53051f3430f39bf9f4024c/t/admin/standalone.spec.ts)
  - [`docs/en/latest/deployment-modes.md`](https://github.com/apache/apisix/blob/a64f2baa06b1c7d55e53051f3430f39bf9f4024c/docs/en/latest/deployment-modes.md)
  - [`README.md`](https://github.com/apache/apisix/blob/a64f2baa06b1c7d55e53051f3430f39bf9f4024c/README.md)
  - [`LICENSE`](https://github.com/apache/apisix/blob/a64f2baa06b1c7d55e53051f3430f39bf9f4024c/LICENSE)
- **Trace:** Start in the Standalone Admin API update handler and follow body parsing into batch schema and duplicate validation, digest idempotence, per-resource monotonic version checks, final-config construction, JSON publication in the standalone shared dictionary, and worker-event posting; continue through subsystem-specific event setup and the stream polling fallback into config_yaml's per-worker update and resource sync, then follow stream router version detection and empty-startup handling into stream_preread_phase matching; close the path with the Jest API contract, Test::Nginx hot-update and version cases, and the exact regression for a connection arriving before the first configuration.

**Why this level:**

- **Language technique 4:** Advanced Lua and OpenResty runtime machinery recurs across the main trace, but one bounded path does not require multiple pervasive expert-level language mechanisms beyond that framework fluency.
- **Behavioral reasoning 5:** Expert nonlocal reasoning across asynchronous publication, per-worker state, scheduling, failures, initialization, and live traffic is unavoidable throughout the selected behavior.
- **Design span 5:** Understanding the behavior requires coordinating several major control, storage, process, runtime, routing, and test subsystems rather than one local component.
- **Constraint burden 5:** Several system-wide correctness, ordering, availability, security, recovery, compatibility, and performance guarantees interact so a locally plausible change can reject valid state, publish stale state, strand workers, or abort live traffic.
- **Placement:** The four scores 4/5/5/5 sum to 19; their arithmetic mean is 4.75 and rounds half-up to Level 5. The published result is Level 5.

**License:** Apache-2.0 ([evidence 1](https://github.com/apache/apisix/blob/a64f2baa06b1c7d55e53051f3430f39bf9f4024c/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The Apache Software Foundation actively maintains and releases APISIX for production traffic management, and the project documents installation, deployment modes, gateway operation, extension points, upgrades, and contribution workflows.

**Language evidence:** Lua implements the Standalone Admin API, configuration validation and propagation, OpenResty worker events and timers, per-resource hot-reload state, stream routing, request phases, and the production gateway runtime; the selected integration suites exercise that Lua behavior.

**Coding relevance:**

That short gateway and worker-model primer is documented in the selected files. Transferable validation, versioned state replacement, idempotence, shared-memory publication, event and polling coordination, hot reload, availability during initialization, fault isolation, and integration testing explain the path's difficulty.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The selected modules make validation, version decisions, publication, event and polling coordination, cache mutation, router rebuild, empty startup, and request failure paths explicit.
- **Architecture:** The Admin handler, validator, shared dictionary, event adapter, configuration provider, per-worker resource objects, router, and request phase have recognizable responsibilities and boundaries.
- **Naming and idiom:** update_and_broadcast_config, validate_configuration, conf_version, sync_data, _automatic_fetch, stream_init_worker, create_router, and matched_route communicate the live configuration lifecycle in idiomatic OpenResty Lua.
- **Tests:** Forty Jest cases and seventeen Test::Nginx cases cover JSON and YAML updates, digests, versions, modified indexes, validation, duplicates, additions, deletion, routes and stream routes; a focused regression protects a stream connection before the first configuration.
- **Documentation:** The deployment-mode guide explains file-driven and API-driven standalone operation, full updates, version rules, digests, security requirements, hot reload, and empty startup; README.md provides gateway orientation.
- **Traceability:** A configuration can be followed from one HTTP update through validation and publication into worker-local resource state, route reconstruction, live request behavior, and direct integration assertions.
- **Maintainability:** Version, validation, publication, resource synchronization, and routing responsibilities are separated, and layered direct suites protect both API contracts and cross-worker runtime behavior.
- **Educational value:** The path joins a familiar configuration API to the exact concurrency, lifecycle, and consistency mechanisms needed to hot-update a production event-driven gateway safely.

**Inspection record:** commit `a64f2baa06b1c7d55e53051f3430f39bf9f4024c`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `apisix/admin/standalone.lua`, `apisix/admin/config_validate.lua`, `apisix/core/config_yaml.lua`, `apisix/events.lua`, `apisix/router.lua`, `apisix/stream/router/ip_port.lua`, `apisix/init.lua`, `t/admin/standalone.t`, `t/admin/standalone-stream.t`, `t/admin/standalone.spec.ts`, `docs/en/latest/deployment-modes.md`, `README.md`, `LICENSE`. GitHub Linguist label: Lua.

</details>

### [Kong/kong](https://github.com/Kong/kong)

**Language 3 / Behavior 5 / Design 5 / Constraints 5 → Level 5**

**Source:** Production software

A production API, AI, and MCP gateway supporting traffic routing, load balancing, authentication, policy plugins, observability, databases or declarative operation, and hybrid control and data planes.

**Why study it:** Kong's cluster-events subsystem is an expert Lua path through durable publication, polling, shared-memory cursors, deduplication, delayed delivery, callback isolation, and recovery across nodes and workers.

**Short context:**

- Cluster events propagate invalidation or coordination messages among Kong nodes by persisting events, polling them, deduplicating delivery, and invoking channel subscribers.

**Prerequisites:**

- Readers should know advanced Lua, OpenResty timers and shared dictionaries, database transactions and pagination, locks, callbacks, distributed node identity, clocks, deduplication, and failure recovery.

**Concepts this path develops:**

- Metatable modules and strategy polymorphism.
- Durable publish, recurring poll, shared cursor, lookback, pagination, deduplication, delayed delivery, callback, and cleanup state interact.
- Events must not be lost, replayed incorrectly, delivered to the publishing node, duplicated across workers, or observed before not-before time.

**What you can learn:**

- Trace broadcast into durable storage, then follow locked paged polling, lookback cursors, same-node suppression, shared-memory deduplication, not-before delays, protected callbacks, cleanup, and timer rescheduling.

**Learning path:**

- **Goal:** Understand how Kong durably broadcasts a cluster event and delivers it once to remote-node subscribers despite polling intervals, delays, pagination, worker concurrency, and failures.
- **Start here:** [`cluster_events/init.lua`](https://github.com/Kong/kong/blob/fa9c3b695af72668f135cb17bbb84a8b4dc511d2/kong/cluster_events/init.lua) — The reviewed trace begins in cluster_events/init.lua because it selects the strategy and owns broadcast, subscription, shared state, polling, delivery, error handling, and recurring scheduling.
- **Then read:**
  - [`kong/cluster_events/strategies/postgres.lua`](https://github.com/Kong/kong/blob/fa9c3b695af72668f135cb17bbb84a8b4dc511d2/kong/cluster_events/strategies/postgres.lua)
  - [`kong/cluster_events/strategies/off.lua`](https://github.com/Kong/kong/blob/fa9c3b695af72668f135cb17bbb84a8b4dc511d2/kong/cluster_events/strategies/off.lua)
  - [`kong/concurrency.lua`](https://github.com/Kong/kong/blob/fa9c3b695af72668f135cb17bbb84a8b4dc511d2/kong/concurrency.lua)
  - [`kong/tools/time.lua`](https://github.com/Kong/kong/blob/fa9c3b695af72668f135cb17bbb84a8b4dc511d2/kong/tools/time.lua)
  - [`spec/02-integration/06-invalidations/01-cluster_events_spec.lua`](https://github.com/Kong/kong/blob/fa9c3b695af72668f135cb17bbb84a8b4dc511d2/spec/02-integration/06-invalidations/01-cluster_events_spec.lua)
  - [`README.md`](https://github.com/Kong/kong/blob/fa9c3b695af72668f135cb17bbb84a8b4dc511d2/README.md)
  - [`DEVELOPER.md`](https://github.com/Kong/kong/blob/fa9c3b695af72668f135cb17bbb84a8b4dc511d2/DEVELOPER.md)
  - [`LICENSE`](https://github.com/Kong/kong/blob/fa9c3b695af72668f135cb17bbb84a8b4dc511d2/LICENSE)
- **Trace:** Start with new selecting a strategy, server-time cursor, node identity and shared-memory state; follow broadcast into durable insertion, subscribe into polling startup, then poll through concurrency locks, lookback cursor, paged database selection, cursor advancement, same-node suppression, shared-memory deduplication, not-before delay, protected callbacks, error handling, cleanup, and recurring timer scheduling; close the lifecycle in the dedicated cluster-events integration suite.

**Why this level:**

- **Language technique 3:** Substantial framework and runtime abstractions shape the path without pervasive expert Lua metaprogramming.
- **Behavioral reasoning 5:** Several advanced distributed, concurrent, scheduled, persistent, and recovery concerns interact pervasively.
- **Design span 5:** The selected behavior coordinates several major runtime, persistence, process, and platform subsystems.
- **Constraint burden 5:** Several system-wide correctness, liveness, durability, timing, recovery, compatibility, and performance guarantees require expert change discipline.
- **Placement:** The four scores 3/5/5/5 sum to 18; their arithmetic mean is 4.50 and rounds half-up to Level 5. The published result is Level 5.

**License:** Apache-2.0 ([evidence 1](https://github.com/Kong/kong/blob/fa9c3b695af72668f135cb17bbb84a8b4dc511d2/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** Kong maintains and ships the gateway for real network traffic, with documented deployment, upgrade, plugin-development, database, DB-less, and hybrid-cluster modes.

**Language evidence:** Lua implements the gateway lifecycle, routing, load balancing, plugins, policy enforcement, data models, declarative configuration, clustering, control and data planes, PDK, observability, vaults, migrations, and tests on OpenResty.

**Coding relevance:**

That short distributed-event context is subordinate to transferable expert engineering in database-backed pub/sub, shared-memory cursors and deduplication, timers, locks, delayed delivery, pagination, node identity, callback isolation, failure recovery, cross-worker coordination, and integration testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** cluster_events/init.lua keeps validation, strategy selection, cursors, locks, pagination, lookback, suppression, deduplication, delays, callbacks, cleanup, and timer recovery explicit.
- **Architecture:** The public cluster-events API composes a persistence strategy with database time, shared worker state, concurrency locks, recurring timers, channel subscribers, and protected callback delivery.
- **Naming and idiom:** cluster_events, broadcast, subscribe, poll, postgres and off strategies, node identity, lookback, not-before time, and shared cursors make distributed lifecycle intent visible.
- **Tests:** 01-cluster_events_spec.lua covers singleton construction, node identity, polling startup, broadcast, remote delivery, same-node suppression, lookback, pagination, callback errors, and delay.
- **Documentation:** README.md and DEVELOPER.md orient Kong's node and development environment sufficiently for the bounded cluster-events subsystem.
- **Traceability:** An event can be followed from broadcast and database insertion through a locked polling page, cursor and deduplication checks, delayed callback, and dedicated integration assertions.
- **Maintainability:** Persistence strategies, concurrency helpers, and time helpers isolate runtime contracts, while one direct integration suite protects cross-node and cross-worker behavior.
- **Educational value:** The path provides a representative production lesson in distributed event delivery without requiring Kong's proxy, router, plugin, and PDK breadth.

**Inspection record:** commit `fa9c3b695af72668f135cb17bbb84a8b4dc511d2`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `kong/cluster_events/init.lua`, `kong/cluster_events/strategies/postgres.lua`, `kong/cluster_events/strategies/off.lua`, `kong/concurrency.lua`, `kong/tools/time.lua`, `spec/02-integration/06-invalidations/01-cluster_events_spec.lua`, `README.md`, `DEVELOPER.md`, `LICENSE`. GitHub Linguist label: Lua.

</details>

_Generated from `catalog/lua.json`; do not edit by hand._

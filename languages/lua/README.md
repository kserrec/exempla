# Lua

10 qualified repositories. Scores assume the learner described in [the SDC rubric](../../docs/sdc.md).

[← All languages](../README.md)

## SDC 1

### [kikito/middleclass](https://github.com/kikito/middleclass)

**S1 / D2 / C1 → SDC 1**

A compact object-oriented library providing classes, inheritance, instances, mixins, static members, and metamethod support.

**Real-world evidence:** The maintained LuaRocks library is used by applications and games that want a small conventional class abstraction without a framework.

**Language evidence:** Class creation, inheritance, allocation, mixins, metamethod propagation, and the complete test suite are handwritten Lua.

**Why study it:** It turns tables and metatables into a recognizable object model while keeping class construction, inheritance, allocation, mixins, and special metamethod handling visible in one file.

**What you can learn:**

- Prototype relationships, metatables, class and instance lookup, inheritance, allocation versus initialization, mixins, static members, metamethod forwarding, and version-sensitive tests.

**Prerequisites:**

- Basic Lua tables and functions, metatables and metamethods, colon-method syntax, module loading, inheritance concepts, and Busted-style tests.

**Start here:** [`middleclass.lua`](https://github.com/kikito/middleclass/blob/359f0e2742f51ca77801b513ec91eb9029de8de4/middleclass.lua) — The single implementation file builds the class model from the bottom up and exposes every public operation without generated layers.

**Why this level:**

- **S1:** 155 meaningful implementation LOC measured with tokei 14.0.0. Count covers the complete production implementation in middleclass.lua.
- **D2:** The project requires a solid mental model of Lua metatables, but its implementation remains compact and self-contained.
- **C1:** All behavior is synchronous and in memory, with no integration, persistence, networking, or concurrency.
- **Placement:** S1/D2/C1 averages to 1.33, making middleclass an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** Class construction, lookup chains, allocation, subclass tracking, mixin inclusion, and metamethod copying are small explicit functions.
- **Architecture:** One file separates instance behavior, class behavior, static lookup, subclass creation, and mixin inclusion through named internal tables.
- **Naming and idiom:** class, subclass, allocate, initialize, include, isInstanceOf, isSubclassOf, __instanceDict, and static expose the object model clearly.
- **Tests:** Eight focused specifications cover classes, instances, default methods, inheritance, mixins, ordinary metamethods, and Lua version differences.
- **Documentation:** The README explains class creation, constructors, inheritance, class variables, identity checks, mixins, metamethods, and performance boundaries.
- **Traceability:** A class definition can be followed through its instance dictionary and metatables into subclassing, allocation, initialization, lookup, and assertions.
- **Maintainability:** A stable small surface, dependency-free implementation, deliberate compatibility logic, and focused tests make semantic changes easy to review.
- **Educational value:** It demonstrates how a familiar abstraction can be built honestly from a language's native object primitives rather than hidden machinery.

**Inspection record:** commit `359f0e2742f51ca77801b513ec91eb9029de8de4`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `middleclass.lua`, `spec/classes_spec.lua`, `spec/instances_spec.lua`, `spec/mixins_spec.lua`, `spec/metamethods_spec.lua`, `MIT-LICENSE.txt`. GitHub Linguist label: Lua. LOC exclusions: specifications, rockspecs, documentation, and license text.

**License:** [MIT](https://github.com/kikito/middleclass/blob/359f0e2742f51ca77801b513ec91eb9029de8de4/MIT-LICENSE.txt)

### [lunarmodules/say](https://github.com/lunarmodules/say)

**S1 / D1 / C1 → SDC 1**

A tiny namespaced message store with fallback lookup, formatted substitution, and a callable retrieval interface.

**Real-world evidence:** Lua developers use the maintained LuaRocks module as the message and localization layer underneath tools including Luassert and Busted.

**Language evidence:** The message registry, namespace fallback, positional substitution, callable interface, and behavior tests are implemented in Lua.

**Why study it:** Fifty production lines expose a complete contract: nested key storage, locale-style fallback, argument validation, substitution, missing-key behavior, and a metatable call API.

**What you can learn:**

- Nested tables, dotted namespace traversal, metatable call syntax, fallback lookup, positional substitution, input validation, module state, and compact behavior tests.

**Prerequisites:**

- Basic Lua tables, functions, modules, strings, varargs, metatables, error handling, and unit-test assertions.

**Start here:** [`src/say/init.lua`](https://github.com/lunarmodules/say/blob/fe1475fe2acaf844bd030c2ff998bc99ed8930ed/src/say/init.lua) — The only production module contains the complete data model and lookup path, so it can be read end to end before its specification.

**Why this level:**

- **S1:** 50 meaningful implementation LOC measured with tokei 14.0.0. Count covers the complete production Lua implementation in src/say/init.lua.
- **D1:** Every operation uses core Lua constructs and the entire state transition fits in one short module.
- **C1:** There are no external services, asynchronous paths, persistence layers, plugins, or process boundaries.
- **Placement:** S1/D1/C1 averages to 1.00, making say an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** The registry, namespace walk, fallback choice, substitutions, and error cases are direct and visible without framework indirection.
- **Architecture:** One private table holds messages while a small module API owns insertion, lookup, fallback selection, and callable dispatch.
- **Naming and idiom:** set, fallback, key, namespace, replacements, and the callable module table describe the mechanism in ordinary Lua vocabulary.
- **Tests:** The specification covers values, namespaces, arguments, nils, fallback behavior, missing keys, type errors, and replacement-count errors.
- **Documentation:** The README shows installation, registration, namespaces, retrieval, interpolation, fallback, and the callable shorthand with runnable examples.
- **Traceability:** A dotted key can be followed from insertion through namespace tables, fallback selection, substitution, and the returned string or error.
- **Maintainability:** A tiny API, no runtime dependencies, explicit validation, and a focused specification keep every behavior locally reviewable.
- **Educational value:** It is an unusually compact example of turning plain tables and metatables into a complete, useful library contract.

**Inspection record:** commit `fe1475fe2acaf844bd030c2ff998bc99ed8930ed`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/say/init.lua`, `spec/say_spec.lua`, `LICENSE`. GitHub Linguist label: Lua. LOC exclusions: specifications, localization data, rockspecs, and documentation.

**License:** [MIT](https://github.com/lunarmodules/say/blob/fe1475fe2acaf844bd030c2ff998bc99ed8930ed/LICENSE)

## SDC 2

### [lunarmodules/luassert](https://github.com/lunarmodules/luassert)

**S1 / D3 / C2 → SDC 2**

A fluent assertion and test-double library with extensible namespaces, snapshots, modifiers, matchers, rich formatting, spies, stubs, and mocks.

**Real-world evidence:** The maintained LuaRocks package supplies the assertion layer used by Busted and can also be embedded directly in other Lua test environments.

**Language evidence:** The fluent assertion state machine, assertions, modifiers, matchers, formatting, spies, stubs, mocks, and specifications are Lua.

**Why study it:** A familiar assertion API opens into metatable chaining, reversible registration, weakly tracked test-double state, deep comparison, diagnostic formatting, and composable matchers.

**What you can learn:**

- Fluent APIs through metatables, assertion state, namespaces, reversible registration, modifiers and matchers, deep equality, diagnostic formatting, spies, stubs, mocks, snapshots, and failure-message design.

**Prerequisites:**

- Comfortable Lua tables, functions, closures, varargs and metatables, unit-testing concepts, equality semantics, weak tables, and higher-order functions.

**Start here:** [`src/assert.lua`](https://github.com/lunarmodules/luassert/blob/a1c4902b0528d90f04214e2f334a01c2fb747bce/src/assert.lua) — The public assertion object shows how chained names resolve into modifiers or assertions and how state becomes a formatted pass or failure.

**Why this level:**

- **S1:** 1,658 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production Lua under src after removing message-only translations.
- **D3:** Extension, chaining, matching, and reversible state require precise dynamic-language reasoning beneath a simple public API.
- **C2:** Several cooperating modules serve one in-process testing concern without external systems or asynchronous orchestration.
- **Placement:** S1/D3/C2 averages to 2.00, making Luassert an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** Assertion dispatch, parameters, negation, deep comparison, formatter selection, call recording, replacement, and restoration are separated into readable operations.
- **Architecture:** A central state and namespace registry coordinate core assertions, modifiers, matchers, formatters, spies, stubs, mocks, and compatibility helpers.
- **Naming and idiom:** assertions, modifiers, matchers, snapshot, revert, spy, stub, mock, called_with, same, and near match the vocabulary users see in tests.
- **Tests:** Nine specifications cover outcomes and messages, snapshots, spies, stubs, mocks, matchers, formatters, output, modifiers, registration, and edge cases.
- **Documentation:** The README documents standalone use, chaining, negation, equality choices, errors, matchers, spies, stubs, mocks, customization, and localization.
- **Traceability:** An expression can be followed through metatable lookup, namespace resolution, state updates, the predicate, argument formatting, and the final message.
- **Maintainability:** Extension points are registered explicitly, snapshots undo shared mutations, formatting is isolated, and focused specifications protect each public family.
- **Educational value:** It shows how to design an expressive dynamic-language DSL without losing a traceable internal execution model.

**Inspection record:** commit `a1c4902b0528d90f04214e2f334a01c2fb747bce`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/assert.lua`, `src/assertions.lua`, `src/state.lua`, `src/modifiers.lua`, `src/match.lua`, `src/spy.lua`, `src/stub.lua`, `src/formatters/init.lua`, `spec/assertions_spec.lua`, `spec/spies_spec.lua`, `LICENSE`. GitHub Linguist label: Lua. LOC exclusions: specifications, localization tables under src/languages, rockspecs, and documentation.

**License:** [MIT](https://github.com/lunarmodules/luassert/blob/a1c4902b0528d90f04214e2f334a01c2fb747bce/LICENSE)

### [openresty/lua-resty-lrucache](https://github.com/openresty/lua-resty-lrucache)

**S1 / D3 / C2 → SDC 2**

An in-process least-recently-used cache for OpenResty with expiry, stale reads, user flags, bounded capacity, and table-backed or pure-FFI storage.

**Real-world evidence:** OpenResty maintains the library for production Nginx and LuaJIT applications that need per-worker caching without shared-memory serialization overhead.

**Language evidence:** Both the table-backed and pure-FFI cache implementations, queue management, expiry logic, flags, and OpenResty tests are Lua.

**Why study it:** Two implementations preserve one contract while exposing hash lookup, a doubly linked recency queue, expiration semantics, stale recovery, FFI memory layouts, and capacity tradeoffs.

**What you can learn:**

- LRU invariants, hash-table and linked-list coordination, TTL expiration, stale reads, user flags, LuaJIT FFI structures, capacity accounting, cache flushing, and Nginx integration tests.

**Prerequisites:**

- Comfortable Lua tables and modules, linked lists and hash maps, cache terminology, timestamps, LuaJIT FFI basics, and OpenResty request phases.

**Start here:** [`lib/resty/lrucache.lua`](https://github.com/openresty/lua-resty-lrucache/blob/ad373f457a091ffa85de984938f948bc1721d922/lib/resty/lrucache.lua) — The table-backed implementation presents the public API and recency invariants most directly before the equivalent pure-FFI representation.

**Why this level:**

- **S1:** 599 meaningful implementation LOC measured with tokei 14.0.0. Count covers both production Lua implementations under lib/resty.
- **D3:** Correct eviction and pointer manipulation demand careful invariant reasoning even though the public contract is bounded.
- **C2:** Several coordinated paths implement one in-process cache, with no distributed coherence or persistent service boundary.
- **Placement:** S1/D3/C2 averages to 2.00, making lua-resty-lrucache an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** Queue mutations, hash entries, expiration checks, stale returns, flag handling, capacity enforcement, and FFI allocations are explicit and localized.
- **Architecture:** A conventional table implementation and a pure-FFI implementation expose the same cache API while isolating their storage mechanics.
- **Naming and idiom:** get, set, delete, flush_all, get_keys, capacity, count, queue, free_queue, key2node, and node2key reveal contract and representation.
- **Tests:** Parallel Test::Nginx suites exercise construction, hits, misses, false values, eviction, expiration, stale values, flushing, capacity, counts, keys, flags, and mixed workloads.
- **Documentation:** The README explains per-worker scope, performance rationale, installation, every method, stale semantics, FFI constraints, and the BSD license.
- **Traceability:** A write can be followed into a hash entry and queue node, then through lookup, expiry, recency promotion, eviction, deletion, or stale return.
- **Maintainability:** A shared public contract, mirrored integration suites, explicit invariants, and separation between table and FFI storage contain low-level risk.
- **Educational value:** It is a concise bridge from textbook LRU behavior to the memory and expiry details required by a production runtime.

**Inspection record:** commit `ad373f457a091ffa85de984938f948bc1721d922`, reviewed 2026-08-28 by Codex. Files sampled: `README.markdown`, `lib/resty/lrucache.lua`, `lib/resty/lrucache/pureffi.lua`, `t/001-sanity.t`, `t/100-pureffi/001-sanity.t`, `t/008-user-flags.t`. GitHub Linguist label: Lua. LOC exclusions: Test::Nginx cases, Perl test helper, build metadata, and documentation.

**License:** [BSD-2-Clause](https://github.com/openresty/lua-resty-lrucache/blob/ad373f457a091ffa85de984938f948bc1721d922/README.markdown#copyright-and-license)

## SDC 3

### [lunarmodules/busted](https://github.com/lunarmodules/busted)

**S2 / D3 / C3 → SDC 3**

A full testing framework with nested contexts, hooks, asynchronous completion, filtering, randomized execution, multiple source loaders, and pluggable reporters.

**Real-world evidence:** The maintained LuaRocks tool runs real project suites from the command line and provides the standard framework around Luassert assertions.

**Language evidence:** Test-tree construction, hooks, execution, filtering, loaders, configuration, status reporting, output handlers, and self-tests are Lua.

**Why study it:** It turns declarative test blocks into an event-driven tree, schedules hooks safely, isolates failures and traces, loads multiple source languages, filters runs, and emits terminal or machine-readable reports.

**What you can learn:**

- Test-tree construction, context inheritance, setup and teardown ordering, event mediation, synchronous and asynchronous execution, error capture, filters and tags, randomized runs, source loaders, configuration, and report formats.

**Prerequisites:**

- Comfortable Lua modules, closures and tables, test-runner concepts, command-line parsing, callback-style asynchrony, stack traces, events, and plugin interfaces.

**Start here:** [`busted/core.lua`](https://github.com/lunarmodules/busted/blob/22f8089f461a563fb9553ab56f926c6805850833/busted/core.lua) — The core shows how describe and test declarations become blocks, how hooks attach, and how events connect construction to execution.

**Why this level:**

- **S2:** 3,048 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production Lua in busted plus its command-line modules.
- **D3:** A learner must reason about lifecycle ordering and failure containment across nested test contexts.
- **C3:** Many extensible subsystems cooperate across declaration, discovery, execution, and reporting within one local tool.
- **Placement:** S2/D3/C3 averages to 2.67, making Busted an SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** Block state, hook inheritance, event emission, safe calls, completion status, file loading, filtering, and output selection are expressed in focused modules.
- **Architecture:** The core builds a block tree; environment and runner modules discover files; executors traverse lifecycle hooks; loaders and reporters use explicit interfaces.
- **Naming and idiom:** describe, it, setup, teardown, lazy_setup, pending, block, environment, executor, file_loader, output_handler, and status mirror testing concepts.
- **Tests:** The self-hosted suite covers trees, hooks, execution order, async behavior, randomization, isolation, filters, tags, CLI failures, loaders, configuration, reporters, strict globals, and LuaJIT.
- **Documentation:** The README and command help explain installation, syntax, hooks, asynchronous tests, tags, filtering, randomization, configuration, loaders, reporters, and CI use.
- **Traceability:** A declared test can be followed into a block, through inherited hooks and protected execution, into status events and a selected report line.
- **Maintainability:** Lifecycle stages and plugin seams are separated, failures become explicit statuses, and the project exercises its own runner across success and failure fixtures.
- **Educational value:** It provides a readable implementation of infrastructure developers ordinarily consume without seeing: the test framework itself.

**Inspection record:** commit `22f8089f461a563fb9553ab56f926c6805850833`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `busted/core.lua`, `busted/block.lua`, `busted/environment.lua`, `busted/runner.lua`, `busted/execute.lua`, `busted/modules/test_file_loader.lua`, `busted/modules/files/lua.lua`, `busted/outputHandlers/junit.lua`, `spec/core_spec.lua`, `spec/execution_order_sync_spec.lua`, `spec/async_spec.lua`, `LICENSE`. GitHub Linguist label: Lua. LOC exclusions: specifications and fixtures, localization tables under busted/languages, documentation, and rockspecs.

**License:** [MIT](https://github.com/lunarmodules/busted/blob/22f8089f461a563fb9553ab56f926c6805850833/LICENSE)

### [lunarmodules/luacheck](https://github.com/lunarmodules/luacheck)

**S2 / D4 / C3 → SDC 3**

A static analyzer and command-line linter that reports globals, unused values, control-flow mistakes, whitespace problems, complexity, and configuration-sensitive warnings.

**Real-world evidence:** The maintained LuaRocks and command-line tool checks applications and libraries locally and in continuous integration across configurable language standards.

**Language evidence:** Lexing, parsing, AST passes, control-flow linearization, local resolution, warning detectors, configuration, filtering, caching, CLI behavior, and tests are Lua.

**Why study it:** It exposes a full pipeline from tokens and syntax trees through normalization, control-flow linearization, name resolution, warning passes, standards, inline options, filtering, caching, formatting, and exit codes.

**What you can learn:**

- Lexers and parsers, AST normalization, control-flow linearization, lexical scope resolution, data-flow warnings, cyclomatic complexity, inline directives, standards and configuration, caching, multithreading, formatters, and CLI contracts.

**Prerequisites:**

- Strong Lua syntax and semantics, tree traversal, lexical scope, control flow and data flow, command-line tools, configuration files, serialization, and behavior-driven tests.

**Start here:** [`src/luacheck/check.lua`](https://github.com/lunarmodules/luacheck/blob/2f764bdcabe8b7c19deadf0e9bb2adc19df1a4c5/src/luacheck/check.lua) — The orchestration module shows the parse-to-warning pipeline and gives every deeper lexer, parser, stage, option, and filter module a clear place.

**Why this level:**

- **S2:** 8,401 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production Lua under src/luacheck after removing vendor and generated data modules.
- **D4:** Understanding correctness requires compiler-style reasoning about syntax, bindings, reachability, mutation, and warning precedence.
- **C3:** Several substantial subsystems cooperate, but they form one local static-analysis product without a distributed runtime.
- **Placement:** S2/D4/C3 averages to 3.00, making Luacheck an SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** Tokens, parse nodes, transformations, linear instructions, scopes, warning codes, suppression decisions, and user diagnostics remain explicit at each stage.
- **Architecture:** Lexer and parser feed ordered analysis stages; the checker applies options and standards; filtering, configuration, caching, formatting, and the CLI wrap the core.
- **Naming and idiom:** lexer, parser, linearize, resolve_locals, detect_unused_locals, detect_unreachable_code, standards, filter, check_state, and warnings expose compiler roles.
- **Tests:** The broad suite covers parsing, scopes, globals, unused and uninitialized values, reachability, assignments, whitespace, options, directives, standards, config, globbing, cache, serialization, files, and formatters.
- **Documentation:** The README and command documentation explain warning families, codes, configuration hierarchy, standards, inline options, filtering, formatters, caching, and editor or CI use.
- **Traceability:** A source token can be followed into an AST, through normalization and scope resolution, into a detector, filter decision, formatted warning, and asserted output.
- **Maintainability:** Numbered warning contracts, isolated detector stages, explicit standards, stable configuration merging, and dense regressions localize semantic changes.
- **Educational value:** It is a full but approachable compiler-adjacent codebase where every analysis phase produces concepts a learner can inspect and test.

**Inspection record:** commit `2f764bdcabe8b7c19deadf0e9bb2adc19df1a4c5`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/luacheck/check.lua`, `src/luacheck/lexer.lua`, `src/luacheck/parser.lua`, `src/luacheck/stages/linearize.lua`, `src/luacheck/stages/resolve_locals.lua`, `src/luacheck/stages/detect_unused_locals.lua`, `src/luacheck/filter.lua`, `src/luacheck/config.lua`, `src/luacheck/main.lua`, `spec/check_spec.lua`, `spec/resolve_locals_spec.lua`, `LICENSE`. GitHub Linguist label: Lua. LOC exclusions: specifications and fixtures, vendored SHA-1 implementation, autogenerated Unicode boundary table, documentation, and package metadata.

**License:** [MIT](https://github.com/lunarmodules/luacheck/blob/2f764bdcabe8b7c19deadf0e9bb2adc19df1a4c5/LICENSE)

## SDC 4

### [CorsixTH/CorsixTH](https://github.com/CorsixTH/CorsixTH)

**S4 / D4 / C4 → SDC 4**

A cross-platform reimplementation of Theme Hospital with a complete campaign, simulation, custom levels, save games, localization, and native graphics, audio, and input integration.

**Real-world evidence:** The maintained desktop game is distributed for players on Windows, macOS, Linux, BSD, and other platforms and uses original game data for its full campaign.

**Language evidence:** Lua implements the application lifecycle and most game logic, including simulation, hospitals, rooms, entities, actions, diseases, events, research, interfaces, saves, and campaigns; C++ supplies the native bridge.

**Why study it:** It exposes a mature real-time game's Lua-dominant simulation and interface alongside a narrow C++ boundary for SDL, rendering, audio, filesystems, maps, and pathfinding.

**What you can learn:**

- Game loops and events, simulation time, world and hospital state, entity and action systems, rooms and objects, diseases and research, campaign progression, UI dialogs, save compatibility, localization, Lua and C++ bindings, and cross-platform builds.

**Prerequisites:**

- Strong Lua object and module patterns, event-driven state machines, game-loop concepts, spatial simulation, persistence and versioning, user-interface architecture, C++ interoperation, and native build systems.

**Start here:** [`CorsixTH/Lua/app.lua`](https://github.com/CorsixTH/CorsixTH/blob/c3ebe5d79e34ea0fef83d099be28a43ee01fa992/CorsixTH/Lua/app.lua) — The application object initializes subsystems and dispatches top-level events, mapping the game, UI, configuration, campaign, and native layers.

**Why this level:**

- **S4:** 120,339 meaningful implementation LOC measured with tokei 14.0.0. Count covers 105,298 production Lua lines, 14,935 production C++ lines, and 106 production C lines in the game and native bridge.
- **D4:** Many domain invariants and lifecycle transitions must remain correct across a long-running interactive simulation.
- **C4:** A large set of stateful game subsystems interacts with native platform services, but it remains one desktop product.
- **Placement:** S4/D4/C4 averages to 4.00, making CorsixTH an SDC 4 project.

**Quality-gate evidence:**

- **Source quality:** Application events, simulation objects, entity actions, room behavior, UI transitions, save versions, and native bindings are organized around concrete game responsibilities.
- **Architecture:** Lua owns application and game-domain behavior while C++ exposes SDL-based platform, graphics, audio, filesystem, map, pathfinding, and scripting services through a defined bridge.
- **Naming and idiom:** App, World, Hospital, Humanoid, Room, Action, Disease, Research, GameUI, Savegame, th_lua, and map expose the simulation and engine layers.
- **Tests:** Busted specifications cover utility, classes, dates, announcers, dialogs, humanoids, doctors, VIPs, machines, and objects; Catch2 tests cover the Lua bridge, maps, UI bindings, strings, and native components.
- **Documentation:** The README, contributor material, build instructions, code comments, test guides, and project wiki explain setup, supported platforms, original assets, gameplay scope, and development paths.
- **Traceability:** A player event can be followed through App dispatch, UI or world state, an entity or room action, simulation updates, and a Lua-to-C++ rendering or input call.
- **Maintainability:** Domain modules mirror game concepts, the native boundary is explicit, save versions are tracked, platform concerns are separated, and both language layers have targeted tests.
- **Educational value:** It offers a rare readable path through a complete desktop game where most high-level behavior is authored in Lua and the engine boundary is inspectable.

**Inspection record:** commit `c3ebe5d79e34ea0fef83d099be28a43ee01fa992`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `CorsixTH/Lua/app.lua`, `CorsixTH/Lua/world.lua`, `CorsixTH/Lua/entities/humanoid.lua`, `CorsixTH/Lua/room.lua`, `CorsixTH/Lua/game_ui.lua`, `CorsixTH/Lua/persistance.lua`, `CorsixTH/Src/main.cpp`, `CorsixTH/Src/th_lua.cpp`, `CorsixTH/Luatest/spec/entities/humanoid_spec.lua`, `CorsixTH/CppTest/test_th_lua.cpp`, `LICENSE.txt`. GitHub Linguist label: Lua. LOC exclusions: Lua and C++ test suites, third-party libraries, generated build files, original-game data, graphics, audio, maps, localization assets, documentation, and tooling.

**License:** [MIT](https://github.com/CorsixTH/CorsixTH/blob/c3ebe5d79e34ea0fef83d099be28a43ee01fa992/LICENSE.txt)

### [nvim-telescope/telescope.nvim](https://github.com/nvim-telescope/telescope.nvim)

**S3 / D4 / C4 → SDC 4**

An extensible fuzzy finder for Neovim with asynchronous sources, sorting, live previews, configurable layouts, composable actions, built-in searches, and extensions.

**Real-world evidence:** The maintained plugin is used interactively to find files, grep text, inspect Git and LSP data, browse buffers and diagnostics, and host third-party extensions.

**Language evidence:** Picker lifecycle, asynchronous finders, entry management, sorting, previews, actions, layouts, built-ins, extensions, configuration, and automated tests are Lua.

**Why study it:** It coordinates an event-driven terminal UI with asynchronous jobs, incremental results, scoring, preview lifecycles, mappings, actions, layout strategies, configuration, built-in domains, and extensions.

**What you can learn:**

- Neovim Lua APIs, asynchronous jobs, event-driven picker state, prompt and result windows, entry normalization, fuzzy scoring, previews, action composition, mappings, layouts, configuration resolution, built-ins, and extensions.

**Prerequisites:**

- Strong Lua modules and metatables, Neovim buffers and windows, callbacks and asynchronous processes, terminal user interfaces, iterators, sorting algorithms, configuration layering, and integration testing.

**Start here:** [`lua/telescope/pickers.lua`](https://github.com/nvim-telescope/telescope.nvim/blob/40aedd8a68c78a656a10a8d62d80c54af59420fb/lua/telescope/pickers.lua) — The picker owns the central lifecycle and ties together finders, sorters, entry managers, previewers, windows, mappings, actions, and completion.

**Why this level:**

- **S3:** 14,002 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production Lua under lua/telescope.
- **D4:** Correct behavior depends on timing, editor state, cancellation, selection, rendering, and user input across many extension seams.
- **C4:** Numerous stateful subsystems and integration boundaries interact during every live picker session.
- **Placement:** S3/D4/C4 averages to 3.67, making telescope.nvim an SDC 4 project.

**Quality-gate evidence:**

- **Source quality:** Picker phases, job callbacks, entry insertion, scoring, selection, window transitions, action dispatch, and cleanup are separated around observable UI behavior.
- **Architecture:** A picker composes a finder, sorter, entry manager and previewer; action, mapping, layout, configuration, built-in, and extension modules surround that protocol.
- **Naming and idiom:** Picker, Finder, Sorter, Previewer, entry_manager, refresh, find, prompt_bufnr, selection, attach_mappings, layout_strategy, and extensions match the domain.
- **Tests:** Automated suites cover actions, commands, diagnostics, entry display and management, layouts, linked lists, file finding, live grep, previewers, resolvers, scrollers, sorters, configuration, paths, and utilities.
- **Documentation:** The README, help documentation, developer guide, defaults, and extension guidance explain installation, dependencies, configuration, mappings, pickers, sorters, previewers, layouts, and customization.
- **Traceability:** A keystroke can be followed from mapping to action, picker state, finder results, sorting, insertion, selection, preview refresh, and an editor effect.
- **Maintainability:** Core roles have explicit interfaces, built-ins reuse shared machinery, extension loading is isolated, cleanup belongs to lifecycle paths, and integration-sensitive behavior has automated coverage.
- **Educational value:** It is a substantial plugin whose asynchronous architecture remains visible in ordinary Lua rather than a hidden graphical framework.

**Inspection record:** commit `40aedd8a68c78a656a10a8d62d80c54af59420fb`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `lua/telescope/init.lua`, `lua/telescope/pickers.lua`, `lua/telescope/finders.lua`, `lua/telescope/entry_manager.lua`, `lua/telescope/sorters.lua`, `lua/telescope/previewers/init.lua`, `lua/telescope/actions/init.lua`, `lua/telescope/config.lua`, `lua/telescope/_extensions/init.lua`, `lua/tests/automated/entry_manager_spec.lua`, `lua/tests/automated/pickers/live_grep_spec.lua`, `LICENSE`. GitHub Linguist label: Lua. LOC exclusions: automated tests and fixtures under lua/tests, internal test harness under lua/telescope/testharness, documentation, examples, and package metadata.

**License:** [MIT](https://github.com/nvim-telescope/telescope.nvim/blob/40aedd8a68c78a656a10a8d62d80c54af59420fb/LICENSE)

## SDC 5

### [Kong/kong](https://github.com/Kong/kong)

**S4 / D5 / C5 → SDC 5**

A production API, AI, and MCP gateway supporting traffic routing, load balancing, authentication, policy plugins, observability, databases or declarative operation, and hybrid control and data planes.

**Real-world evidence:** Kong maintains and ships the gateway for real network traffic, with documented deployment, upgrade, plugin-development, database, DB-less, and hybrid-cluster modes.

**Language evidence:** Lua implements the gateway lifecycle, routing, load balancing, plugins, policy enforcement, data models, declarative configuration, clustering, control and data planes, PDK, observability, vaults, migrations, and tests on OpenResty.

**Why study it:** It coordinates Nginx phases, routers and balancers, a plugin protocol, data access and migrations, caches, clustering, external plugin processes, telemetry, secrets, and many application protocols at an untrusted network boundary.

**What you can learn:**

- OpenResty and Nginx phases, HTTP and stream proxying, route matching, load balancing and health, plugin iteration, authentication and rate limiting, PDK design, database and declarative models, migrations, cache invalidation, hybrid control and data planes, RPC, external plugin servers, observability, vaults, and CLI operations.

**Prerequisites:**

- Expert Lua and LuaJIT, HTTP, TLS, DNS and proxy semantics, Nginx and OpenResty phases, databases and migrations, caching, distributed systems, authentication and security boundaries, concurrency, observability, and production operations.

**Start here:** [`kong/runloop/handler.lua`](https://github.com/Kong/kong/blob/fa9c3b695af72668f135cb17bbb84a8b4dc511d2/kong/runloop/handler.lua) — The run-loop handler maps Nginx phases to gateway work and leads into routing, balancing, plugins, caching, clustering, logging, and request state.

**Why this level:**

- **S4:** 77,326 meaningful implementation LOC measured with tokei 14.0.0. Count covers conservative first-party production Lua under kong after removing attributed, copied, protocol-definition, and test material.
- **D5:** Failures can affect authentication, traffic isolation, availability, configuration consistency, upgrades, or data-plane behavior under production load.
- **C5:** Many extensible subsystems cross process, network, persistence, security, and lifecycle boundaries in one operational platform.
- **Placement:** S4/D5/C5 averages to 4.67 and two dimensions score 5, making Kong an SDC 5 project.

**Quality-gate evidence:**

- **Source quality:** Gateway phases, plugin iteration, route selection, balancer state, DAO operations, cluster messages, cache invalidation, migrations, and failures are separated into explicit units.
- **Architecture:** OpenResty hosts a Lua run loop over routers, balancers, plugins and the PDK, backed by database or declarative state, caches, clustering services, control and data planes, observability, vaults, and CLI operations.
- **Naming and idiom:** runloop, access, rewrite, balancer, plugins_iterator, router, DAO, schema, migration, control_plane, data_plane, PDK, vault, and clustering identify gateway roles.
- **Tests:** Thousands of unit, integration, plugin, migration, hybrid-mode, protocol, database, performance, upgrade, and third-party compatibility cases exercise success and failure behavior.
- **Documentation:** The README, developer guide, security policy, migration guides, PDK and plugin documentation, configuration reference, and operational manuals support deployment and study.
- **Traceability:** A request can be followed from an Nginx phase through route match, service selection, plugin iteration, policy, balancing, upstream I/O, logging, metrics, and persisted or clustered state.
- **Maintainability:** Lifecycle phases, public plugin contracts, schema-driven data access, versioned migrations, compatibility layers, test helpers, and extensive integration suites constrain changes.
- **Educational value:** It is a demanding but unusually rich example of Lua as the control plane for a security-sensitive distributed production system.

**Inspection record:** commit `fa9c3b695af72668f135cb17bbb84a8b4dc511d2`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `DEVELOPER.md`, `SECURITY.md`, `kong/init.lua`, `kong/runloop/handler.lua`, `kong/runloop/plugins_iterator.lua`, `kong/router/atc.lua`, `kong/db/init.lua`, `kong/db/dao/init.lua`, `kong/clustering/control_plane.lua`, `kong/clustering/data_plane.lua`, `kong/pdk/init.lua`, `kong/cache/init.lua`, `kong/cmd/start.lua`, `spec/01-unit/01-db/01-schema/01-schema_spec.lua`, `spec/02-integration/05-proxy/01-proxy_spec.lua`, `LICENSE`. GitHub Linguist label: Lua. LOC exclusions: specifications and fixtures, bundled resty modules, external OpenTelemetry protocol definitions, adapted ljsyscall helper, copied Prometheus module, generated runtime configuration output, documentation, build files, and package metadata.

**License:** [Apache-2.0](https://github.com/Kong/kong/blob/fa9c3b695af72668f135cb17bbb84a8b4dc511d2/LICENSE)

### [LuaLS/lua-language-server](https://github.com/LuaLS/lua-language-server)

**S3 / D5 / C5 → SDC 5**

A production Language Server Protocol implementation with parsing integration, type inference, diagnostics, completion, navigation, annotations, formatting, workspace libraries, and editor clients.

**Real-world evidence:** The maintained server powers Lua development in Visual Studio Code, Neovim, and other LSP clients and reports nearly a million Visual Studio Code installations.

**Language evidence:** Lua implements startup, JSON-RPC and LSP dispatch, workspaces, file state, semantic compilation, type inference, diagnostics, completion, navigation, configuration, plugins, concurrency, and tests.

**Why study it:** It combines a stateful editor protocol server, asynchronous scheduling, workspace and file models, a semantic VM, cross-file inference, diagnostics, completion, refactoring, configuration scopes, plugins, native dependencies, and a large suite.

**What you can learn:**

- Language Server Protocol and JSON-RPC, cancellation, asynchronous tasks, workspace discovery, file versions and text edits, parser integration, semantic graphs, type inference, diagnostics, completion, hover, references, rename, semantic tokens, configuration scopes, plugins, native modules, and cross-file testing.

**Prerequisites:**

- Expert Lua, compiler front ends and abstract syntax trees, static analysis and type inference, Language Server Protocol, JSON-RPC, editor document models, Unicode offsets, asynchronous concurrency, caching, filesystem watching, configuration layering, and native modules.

**Start here:** [`script/provider/provider.lua`](https://github.com/LuaLS/lua-language-server/blob/7a73c7889c1ec981dfd76fba38f5096379f62f99/script/provider/provider.lua) — The provider registers LSP methods and connects client capabilities, workspaces, configuration, files, protocol transport, and each user-facing language feature.

**Why this level:**

- **S3:** 37,979 meaningful implementation LOC measured with tokei 14.0.0. Count covers conservative first-party production Lua in main.lua and script after removing credited embedded components and metadata-only definitions.
- **D5:** Correctness spans language semantics, incremental editor state, asynchronous requests, cross-file caches, native services, and a broad compatibility surface.
- **C5:** Many stateful subsystems and user-facing features share evolving semantic data while responding concurrently to an external editor protocol.
- **Placement:** S3/D5/C5 would average to 4.33, but two dimensions score 5, so the SDC override places lua-language-server at level 5.

**Quality-gate evidence:**

- **Source quality:** Protocol messages, workspace scopes, file versions, semantic nodes, inference caches, diagnostic passes, completion candidates, edits, cancellation, and errors are represented explicitly.
- **Architecture:** A service loop and JSON-RPC transport feed registered providers; workspaces and files feed parser and semantic VM layers; feature modules produce diagnostics, navigation, completion, edits, and tokens.
- **Naming and idiom:** service, proto, provider, workspace, files, vm, compiler, infer, diagnostic, completion, references, rename, semantic_tokens, scope, and capability mirror server responsibilities.
- **Tests:** The runner exercises parsing, inference, definitions, implementations, references, hover, completion, diagnostics, cross-file behavior, highlighting, inlay hints, rename, signatures, commands, symbols, code actions, plugins, CLI behavior, file watching, and full clients.
- **Documentation:** The README, website, configuration reference, annotations guide, changelog, contribution guide, command help, and inline type annotations cover operation and extension.
- **Traceability:** An editor request can be followed from JSON-RPC decoding and provider dispatch through workspace and file state, semantic analysis and a feature module, then back through position conversion to an LSP response.
- **Maintainability:** Protocol handlers, semantic stages, feature modules, configuration scopes, caches, native interfaces, and tests are separated; embedded dependencies remain identifiable in review metrics.
- **Educational value:** It is an advanced reference for how a dynamic language can implement industrial editor intelligence in Lua while keeping protocol and semantic layers inspectable.

**Inspection record:** commit `7a73c7889c1ec981dfd76fba38f5096379f62f99`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `CONTRIBUTING.md`, `main.lua`, `script/service/service.lua`, `script/proto/proto.lua`, `script/provider/provider.lua`, `script/workspace/workspace.lua`, `script/files.lua`, `script/vm/compiler.lua`, `script/vm/infer.lua`, `script/core/completion/completion.lua`, `script/core/diagnostics/init.lua`, `test.lua`, `test/crossfile/init.lua`, `test/diagnostics/init.lua`, `test/completion/init.lua`, `LICENSE`. GitHub Linguist label: Lua. LOC exclusions: tests and fixtures, native dependencies under 3rd, generated or static metadata, locales, documentation, credited embedded LuaParser, lua-glob, utility, json.lua and inspect.lua sources, and the attributed FFI C parser.

**License:** [MIT](https://github.com/LuaLS/lua-language-server/blob/7a73c7889c1ec981dfd76fba38f5096379f62f99/LICENSE)

_Generated from `catalog/lua.json`; do not edit by hand._

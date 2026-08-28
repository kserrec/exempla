# JavaScript

10 qualified repositories. Scores assume the learner described in [the SDC rubric](../../docs/sdc.md).

[← All languages](../README.md)

## SDC 1

### [mafintosh/pump](https://github.com/mafintosh/pump)

**S1 / D2 / C1 → SDC 1**

A stream piping utility that destroys an entire Node.js pipeline when any component closes or fails.

**Real-world evidence:** The repository publishes an npm stream utility designed to prevent resource leaks in real Node.js pipelines.

**Language evidence:** index.js contains the complete Node.js and browser stream-pipeline implementation in JavaScript.

**Why study it:** Its tiny implementation captures a subtle production concern: coordinating completion, errors, and cleanup across heterogeneous streams.

**What you can learn:**

- Node.js stream lifecycle handling, once-only callbacks, error fan-out, and compatibility boundaries.

**Prerequisites:**

- CommonJS modules, callbacks, Node.js readable and writable streams, and event emitters.

**Start here:** [`index.js`](https://github.com/mafintosh/pump/blob/714c0a70a8199104bf65a57582009d42f81d8d94/index.js) — The destroyer helper and final pump reduction expose the whole lifecycle algorithm in one place.

**Why this level:**

- **S1:** 161 meaningful implementation LOC measured with tokei 14.0.0. Count covers the runtime module and browser shim, excluding the two integration test scripts.
- **D2:** Close/error ordering and old stream variants are subtle, but the algorithm is direct and fully contained.
- **C1:** The software coordinates one list of streams with no wider component topology or configuration system.
- **Placement:** A complete real utility in 161 lines makes this SDC 1 despite the care required around stream termination.

**Quality-gate evidence:**

- **Source quality:** Cleanup guards prevent duplicate destruction and preserve the first pipeline error without unnecessary abstraction.
- **Architecture:** A focused destroyer helper composes into one exported pipeline function with no hidden global state.
- **Naming and idiom:** Short names follow the older Node.js style while stream roles and lifecycle flags remain understandable.
- **Tests:** Node and browser integration scripts exercise closure, destruction, callback completion, and returned-stream behavior.
- **Documentation:** The README explains the leak it prevents, callback contract, array form, and concrete stream usage.
- **Traceability:** A stream error flows through end-of-stream, destroyer, sibling cleanup, and the final callback in one file.
- **Maintainability:** The small surface and explicit compatibility checks isolate the few platform-dependent behaviors.
- **Educational value:** It shows why a tiny production library can encode important lifecycle knowledge absent from naive piping.

**Inspection record:** commit `714c0a70a8199104bf65a57582009d42f81d8d94`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `index.js`, `test-node.js`, `test-browser.js`. GitHub Linguist label: JavaScript. LOC exclusions: tests and test fixtures, vendored and generated source, build output and caches, documentation and static assets.

**License:** [MIT](https://github.com/mafintosh/pump/blob/714c0a70a8199104bf65a57582009d42f81d8d94/LICENSE)

### [sindresorhus/p-limit](https://github.com/sindresorhus/p-limit)

**S1 / D2 / C1 → SDC 1**

A small promise-concurrency limiter that queues asynchronous functions and caps how many run simultaneously.

**Real-world evidence:** The repository publishes the p-limit npm library as a reusable concurrency control primitive for production JavaScript programs.

**Language evidence:** The public limiter and all runtime behavior are implemented in index.js; TypeScript supplies declarations only.

**Why study it:** One file demonstrates a complete, useful abstraction with careful promise timing, queue state, error propagation, and a compact public API.

**What you can learn:**

- FIFO work scheduling, promise adoption, asynchronous context preservation, and observable queue state.

**Prerequisites:**

- Promises, async functions, closures, and JavaScript property descriptors.

**Start here:** [`index.js`](https://github.com/sindresorhus/p-limit/blob/df476048d023ff868cd45b35ee47f5fb0ca2b25a/index.js) — The entire runtime contract, queue, transitions, and public API are visible in this one implementation file.

**Why this level:**

- **S1:** 745 meaningful implementation LOC measured with tokei 14.0.0. Count includes runtime JavaScript and TypeScript declarations while excluding tests, recipes, and benchmarks.
- **D2:** Promise adoption and microtask ordering require attention, but state transitions remain short, named, and local.
- **C1:** One factory owns one queue and exposes counters without services, persistence, plugins, or architectural layers.
- **Placement:** The small single-module design outweighs its modest asynchronous nuance, yielding an approachable SDC 1 reading project.

**Quality-gate evidence:**

- **Source quality:** Queue transitions are compact, explicit, and guarded against both synchronous throws and rejected promises.
- **Architecture:** A single factory cleanly contains scheduling state and returns one callable public abstraction.
- **Naming and idiom:** Names such as activeCount, pendingCount, resumeNext, and clearQueue state the contract directly.
- **Tests:** AVA tests cover concurrency limits, thrown errors, queue clearing, dynamic limits, and asynchronous context propagation.
- **Documentation:** The README documents the API, counters, mapping helper, mutable concurrency, and usage examples.
- **Traceability:** A call can be followed through generator, enqueue, run, next, and its matching tests in minutes.
- **Maintainability:** The narrow API, isolated validation, and visible state invariants make changes reviewable.
- **Educational value:** It teaches production promise coordination without framework scaffolding or irrelevant repository machinery.

**Inspection record:** commit `df476048d023ff868cd45b35ee47f5fb0ca2b25a`, reviewed 2026-08-28 by Codex. Files sampled: `readme.md`, `index.js`, `index.d.ts`, `test.js`. GitHub Linguist label: JavaScript. LOC exclusions: tests and test fixtures, vendored and generated source, build output and caches, documentation and static assets.

**License:** [MIT](https://github.com/sindresorhus/p-limit/blob/df476048d023ff868cd45b35ee47f5fb0ca2b25a/license)

## SDC 2

### [ai/nanoid](https://github.com/ai/nanoid)

**S1 / D3 / C2 → SDC 2**

A compact secure unique-ID generator for JavaScript runtimes with customizable alphabets and output lengths.

**Real-world evidence:** The repository ships Nano ID for Node.js, browsers, and package ecosystems as a production identifier library.

**Language evidence:** Node and browser generators, alphabets, and public entry points are first-party JavaScript with declaration files alongside them.

**Why study it:** A small surface demonstrates cryptographic randomness, unbiased alphabet mapping, performance-conscious pooling, and cross-runtime packaging.

**What you can learn:**

- Rejection sampling, entropy preservation, typed-array operations, runtime-specific entry points, and property-focused tests.

**Prerequisites:**

- Typed arrays, bitwise operations, cryptographic random APIs, modules, and elementary probability.

**Start here:** [`index.js`](https://github.com/ai/nanoid/blob/07a39d62d84c21af5046fe6b2ef7b3e36ee557db/index.js) — The secure generator explains modulo bias, fast paths, pooling, and the customizable public API together.

**Why this level:**

- **S1:** 265 meaningful implementation LOC measured with tokei 14.0.0. Count includes Node/browser JavaScript and declarations, excluding tests, benchmarks, and translated documentation.
- **D3:** Correct uniform sampling and optimized byte/string pools require probability and low-level representation reasoning.
- **C2:** Several runtime builds share one concept, but the architecture remains a small family of focused modules.
- **Placement:** Very small size is balanced by substantive randomness and optimization concerns, producing SDC 2.

**Quality-gate evidence:**

- **Source quality:** The implementation explains every non-obvious constant and separates generic randomness from optimized alphabet paths.
- **Architecture:** Runtime-specific entry points reuse a small core instead of duplicating the public generator model.
- **Naming and idiom:** Names expose entropy cutoffs, masks, pools, and offsets while modern modules keep boundaries explicit.
- **Tests:** Tests cover distribution, collision resistance, invalid sizes, huge buffers, custom alphabets, and browser behavior.
- **Documentation:** The README explains security, collision probability, APIs, runtime usage, and performance tradeoffs.
- **Traceability:** A nanoid call can be followed from the export through pooled random bytes to the flat-distribution tests.
- **Maintainability:** Fast and generic paths are separated, documented, and exercised against adversarial input conversions.
- **Educational value:** It makes a security-sensitive algorithm readable without pretending secure IDs are just random string concatenation.

**Inspection record:** commit `07a39d62d84c21af5046fe6b2ef7b3e36ee557db`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `index.js`, `index.browser.js`, `test/index.test.js`. GitHub Linguist label: JavaScript. LOC exclusions: tests and test fixtures, vendored and generated source, build output and caches, documentation and static assets.

**License:** [MIT](https://github.com/ai/nanoid/blob/07a39d62d84c21af5046fe6b2ef7b3e36ee557db/LICENSE)

### [expressjs/express](https://github.com/expressjs/express)

**S1 / D3 / C3 → SDC 2**

A minimalist Node.js web framework providing middleware composition, routing integration, HTTP helpers, and view rendering.

**Real-world evidence:** Express is released as a deployable web framework whose repository maintains the runtime used by Node.js applications.

**Language evidence:** The application, request, response, view, and utility layers under lib are implemented in JavaScript.

**Why study it:** Its relatively small core reveals how a mature framework extends native HTTP objects and composes middleware without hiding the flow.

**What you can learn:**

- Middleware pipelines, prototype extension, request/response adaptation, application settings, and error finalization.

**Prerequisites:**

- Node.js HTTP servers, callbacks, prototypes, CommonJS modules, and middleware concepts.

**Start here:** [`lib/application.js`](https://github.com/expressjs/express/blob/023767fe9872e029271df1418f73401bff20ff40/lib/application.js) — Application initialization, middleware registration, dispatch, settings, and mounting converge in this central module.

**Why this level:**

- **S1:** 1,139 meaningful implementation LOC measured with tokei 14.0.0. Count covers lib runtime JavaScript, excluding tests, examples, documentation, and dependency code.
- **D3:** Native HTTP mutation and callback/error semantics require framework knowledge even though individual functions are readable.
- **C3:** Meaningful behavior crosses application, router dependency, request, response, settings, and final-handler boundaries.
- **Placement:** Compact size keeps a mature multi-layer web framework at SDC 2 rather than overstating it based on reputation.

**Quality-gate evidence:**

- **Source quality:** The core favors small functions and delegates security-sensitive encoding, sending, and finalization to focused libraries.
- **Architecture:** Application, request, response, view, and utilities have recognizable roles around a middleware router.
- **Naming and idiom:** Long-standing public methods and private helpers consistently match familiar HTTP and middleware vocabulary.
- **Tests:** The test suite covers mounting, configuration, routing, HTTP semantics, error paths, and regression behavior.
- **Documentation:** The README and linked API guides explain installation, routing, middleware, and application behavior.
- **Traceability:** A request enters app.handle, receives adapted prototypes and locals, reaches the router, then uses response helpers.
- **Maintainability:** Compatibility behavior is explicit, public surfaces are stable, and responsibilities remain split into a few modules.
- **Educational value:** Learners can see a real framework core without first navigating a large plugin or build infrastructure.

**Inspection record:** commit `023767fe9872e029271df1418f73401bff20ff40`, reviewed 2026-08-28 by Codex. Files sampled: `Readme.md`, `lib/application.js`, `lib/response.js`, `test/app.js`. GitHub Linguist label: JavaScript. LOC exclusions: tests and test fixtures, vendored and generated source, build output and caches, documentation and static assets.

**License:** [MIT](https://github.com/expressjs/express/blob/023767fe9872e029271df1418f73401bff20ff40/LICENSE)

## SDC 3

### [axios/axios](https://github.com/axios/axios)

**S2 / D3 / C3 → SDC 3**

A promise-based HTTP client that presents one request API across browsers, Node.js, and multiple transport adapters.

**Real-world evidence:** The project publishes a production HTTP client with browser and Node transports, releases, and maintained compatibility behavior.

**Language evidence:** The client core, adapters, helpers, cancellation, transforms, and platform implementations are JavaScript under lib.

**Why study it:** It shows how a portable library normalizes configuration, headers, errors, cancellation, proxying, streams, and adapters behind one API.

**What you can learn:**

- Adapter architecture, interceptor chains, configuration merging, HTTP/TLS proxy behavior, cancellation, and cross-runtime boundaries.

**Prerequisites:**

- Promises, HTTP, Node.js streams, browser requests, modules, and object configuration patterns.

**Start here:** [`lib/core/Axios.js`](https://github.com/axios/axios/blob/fede1d1562e308077da7994305d63fb7722b66ac/lib/core/Axios.js) — The request method assembles configuration, interceptors, dispatch, and response flow before handing off to adapters.

**Why this level:**

- **S2:** 7,769 meaningful implementation LOC measured with tokei 14.0.0. Count includes JavaScript runtime and declarations, excluding tests, examples, distributions, and generated artifacts.
- **D3:** The core is conventional, while Node transport, redirects, proxy tunneling, streaming, and cancellation add recurring technical depth.
- **C3:** A request crosses defaults, merge logic, interceptors, dispatch, an environment adapter, transforms, and structured errors.
- **Placement:** Moderate size plus multiple runtime and protocol boundaries make Axios a balanced SDC 3 codebase.

**Quality-gate evidence:**

- **Source quality:** Core orchestration is separated from transport-specific detail, with defensive error decoration and option normalization.
- **Architecture:** Core, adapters, helpers, cancellation, defaults, and platform directories form a clear portability boundary.
- **Naming and idiom:** Request, dispatch, adapter, interceptor, headers, and transform vocabulary follows the HTTP client model.
- **Tests:** Unit and integration suites exercise configuration, adapters, proxies, headers, cancellation, errors, and runtime regressions.
- **Documentation:** The README documents requests, instances, interceptors, cancellation, configuration, errors, and environment support.
- **Traceability:** A request can be traced from Axios.request through interceptor chains and dispatchRequest into the chosen adapter.
- **Maintainability:** Environment-specific branches live behind adapters and helpers instead of contaminating the central request abstraction.
- **Educational value:** It provides a concrete study of portable networking code at a size where the entire request lifecycle remains approachable.

**Inspection record:** commit `fede1d1562e308077da7994305d63fb7722b66ac`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `lib/core/Axios.js`, `lib/adapters/http.js`, `tests/unit/core/Axios.test.js`. GitHub Linguist label: JavaScript. LOC exclusions: tests and test fixtures, vendored and generated source, build output and caches, documentation and static assets.

**License:** [MIT](https://github.com/axios/axios/blob/fede1d1562e308077da7994305d63fb7722b66ac/LICENSE)

### [jquery/jquery](https://github.com/jquery/jquery)

**S2 / D4 / C3 → SDC 3**

A browser library that normalizes DOM traversal, manipulation, events, Ajax, data, and effects behind a chainable API.

**Real-world evidence:** The repository builds and releases the jQuery browser library as real compatibility software, not an instructional implementation.

**Language evidence:** The modular DOM, events, data, Ajax, traversal, and effects implementation is JavaScript under src.

**Why study it:** Its modules expose years of browser-platform edge cases, extensible transports, deferred flow, and a durable chainable object model.

**What you can learn:**

- DOM abstraction, prototype-based fluent APIs, feature detection, Ajax prefilters/transports, events, and compatibility engineering.

**Prerequisites:**

- Browser DOM APIs, prototypes, callbacks and promises, HTTP/Ajax, and regular expressions.

**Start here:** [`src/core.js`](https://github.com/jquery/jquery/blob/71c0dd14927c41d1aab5ce5ef2687d7808a4186b/src/core.js) — The central constructor, prototype, extension mechanism, collection operations, and shared utilities define the library model.

**Why this level:**

- **S2:** 7,166 meaningful implementation LOC measured with tokei 14.0.0. Count covers modular source JavaScript, excluding QUnit tests, build tooling, distributions, and vendor material.
- **D4:** Host-object quirks, feature detection, callbacks/deferreds, selector behavior, and legacy compatibility recur across core paths.
- **C3:** Core collections connect selectors, DOM manipulation, events, data, effects, serialization, and Ajax modules.
- **Placement:** A modest codebase with unusually demanding platform knowledge and several connected subsystems fits SDC 3.

**Quality-gate evidence:**

- **Source quality:** Compatibility branches are purposeful, security-sensitive merges reject prototype pollution, and modules isolate browser concerns.
- **Architecture:** A small core and explicit feature modules build into selectable distributions without obscuring shared behavior.
- **Naming and idiom:** Long-lived names consistently distinguish collections, elements, transports, prefilters, converters, and deferred state.
- **Tests:** Extensive QUnit suites encode DOM, Ajax, selector, event, manipulation, and historical regression contracts.
- **Documentation:** The README covers building and contribution while the public API documentation is linked and maintained separately.
- **Traceability:** A jQuery collection begins in core, gains module methods, and reaches focused unit suites for each browser behavior.
- **Maintainability:** Modular builds and dedicated compatibility tests preserve a difficult browser contract without a monolithic source file.
- **Educational value:** It teaches mature compatibility engineering and the reasons real browser abstractions contain seemingly unusual branches.

**Inspection record:** commit `71c0dd14927c41d1aab5ce5ef2687d7808a4186b`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/core.js`, `src/ajax.js`, `test/unit/core.js`. GitHub Linguist label: JavaScript. LOC exclusions: tests and test fixtures, vendored and generated source, build output and caches, documentation and static assets.

**License:** [MIT](https://github.com/jquery/jquery/blob/71c0dd14927c41d1aab5ce5ef2687d7808a4186b/LICENSE.txt)

## SDC 4

### [eslint/eslint](https://github.com/eslint/eslint)

**S4 / D4 / C4 → SDC 4**

A configurable static-analysis engine and CLI for identifying and automatically fixing JavaScript problems.

**Real-world evidence:** The repository publishes ESLint as an extensible linter used in development and continuous-integration workflows.

**Language evidence:** The linter engine, configuration loaders, rule traversal, fixes, CLI engine, and services are JavaScript under lib.

**Why study it:** It demonstrates AST traversal, plugin rules, configuration resolution, safe autofixes, caching, parallel work, and stable diagnostics.

**What you can learn:**

- Static analysis, visitor dispatch, configuration merging, plugin systems, source ranges, autofix conflict handling, and CLI orchestration.

**Prerequisites:**

- JavaScript ASTs, modules, asynchronous filesystem work, configuration systems, and command-line tools.

**Start here:** [`lib/linter/linter.js`](https://github.com/eslint/eslint/blob/5634542be580750ffb1a5766470f9e9c72719696/lib/linter/linter.js) — The linter connects parsing, rule listeners, traversal, diagnostics, inline configuration, and iterative fixes.

**Why this level:**

- **S4:** 71,101 meaningful implementation LOC measured with tokei 14.0.0. Count includes production JavaScript and declarations, excluding tests, fixtures, docs, benchmarks, and generated output.
- **D4:** Parsing services, scoped traversal, dynamic plugins, suppression, and multipass fixes create recurring advanced behavior.
- **C4:** Linting crosses file discovery, config loading, parsers, plugins, traversal, fixes, suppression, caching, and output services.
- **Placement:** All three dimensions independently land in the fourth band, making ESLint a clear SDC 4 project.

**Quality-gate evidence:**

- **Source quality:** Large orchestration functions are supported by focused helpers, explicit types in comments, invariants, and structured result objects.
- **Architecture:** Public ESLint orchestration, the Linter engine, config loaders, services, rules, and formatters have distinct responsibilities.
- **Naming and idiom:** Rule, source-code, config, suppression, fix, and diagnostic vocabulary is consistent across public and internal APIs.
- **Tests:** Extensive unit and integration suites cover parsers, rules, configuration, fixes, caching, workers, and regressions.
- **Documentation:** User, rule-author, plugin, parser, formatter, integration, and contributor documentation covers each extension surface.
- **Traceability:** A lint request can be followed from ESLint.lintFiles into configuration, Linter verification, rule listeners, and diagnostics.
- **Maintainability:** Extension contracts and service boundaries prevent the configurable analysis engine from collapsing into rule-specific conditionals.
- **Educational value:** It is a substantial but navigable example of how a real static-analysis platform contains third-party code safely.

**Inspection record:** commit `5634542be580750ffb1a5766470f9e9c72719696`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `lib/eslint/eslint.js`, `lib/linter/linter.js`, `tests/lib/linter/linter.js`. GitHub Linguist label: JavaScript. LOC exclusions: tests and test fixtures, vendored and generated source, build output and caches, documentation and static assets.

**License:** [MIT](https://github.com/eslint/eslint/blob/5634542be580750ffb1a5766470f9e9c72719696/LICENSE)

### [prettier/prettier](https://github.com/prettier/prettier)

**S3 / D5 / C4 → SDC 4**

An opinionated source-code formatter that parses many languages, builds a document representation, and prints stable layouts.

**Real-world evidence:** The repository releases a formatter CLI, library, standalone browser builds, and editor-facing plugins used on real codebases.

**Language evidence:** The formatter core, document intermediate representation, printers, parser adapters, and plugins are JavaScript under src.

**Why study it:** It is a strong example of compiler-shaped software: parse, normalize, attach comments, build documents, and render under width constraints.

**What you can learn:**

- AST adaptation, pretty-printing algorithms, document IR, comment attachment, plugin boundaries, snapshots, and cursor preservation.

**Prerequisites:**

- Abstract syntax trees, parsing concepts, recursion, immutable transformations, modules, and basic compiler pipelines.

**Start here:** [`src/main/core.js`](https://github.com/prettier/prettier/blob/0283c8848ecb541c7ea0601ff274799bce1b39e5/src/main/core.js) — The core formatting path connects parser resolution, AST-to-document conversion, printing, ranges, comments, and cursor mapping.

**Why this level:**

- **S3:** 47,162 meaningful implementation LOC measured with tokei 14.0.0. Count includes formatter JavaScript and declarations, excluding tests, fixtures, generated distributions, and documentation.
- **D5:** Correct stable printing across many syntaxes requires recursive algorithms, parser recovery, comment placement, and layout optimization.
- **C4:** Core formatting coordinates parser adapters, language printers, options, plugins, document rendering, ranges, and standalone builds.
- **Placement:** Expert code difficulty triggers the guardrail and the broad formatter architecture confirms an SDC 4 placement.

**Quality-gate evidence:**

- **Source quality:** Pipeline stages and utility boundaries keep difficult formatting algorithms readable and reduce language-plugin duplication.
- **Architecture:** Parser adapters, AST normalization, document builders, printers, and core rendering form a recognizable compiler-style pipeline.
- **Naming and idiom:** Names such as printAstToDoc, normalizeFormatOptions, attachComments, and printDocToString expose each transformation.
- **Tests:** A large fixture and snapshot system covers languages, syntax proposals, options, cursor placement, ranges, and regressions.
- **Documentation:** Contributor and plugin documentation explain architecture, testing, debugging, options, and supported language behavior.
- **Traceability:** A format call can be traced through coreFormat, parsing, AST-to-doc, document printing, and a focused fixture snapshot.
- **Maintainability:** Shared document primitives and plugin contracts constrain a large compatibility matrix behind stable interfaces.
- **Educational value:** It offers a production-grade introduction to formatting and compiler pipelines with unusually strong executable examples.

**Inspection record:** commit `0283c8848ecb541c7ea0601ff274799bce1b39e5`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/main/core.js`, `src/language-js/parse/babel.js`, `tests/config/format-test/run-format-test.js`. GitHub Linguist label: JavaScript. LOC exclusions: tests and test fixtures, vendored and generated source, build output and caches, documentation and static assets.

**License:** [MIT](https://github.com/prettier/prettier/blob/0283c8848ecb541c7ea0601ff274799bce1b39e5/LICENSE)

## SDC 5

### [nodejs/node](https://github.com/nodejs/node)

**S5 / D5 / C5 → SDC 5**

The Node.js runtime, standard library, module loaders, native bindings, event loop integration, diagnostics, and tooling.

**Real-world evidence:** This repository builds the released Node.js executable and standard library used to run server, command-line, and tooling workloads.

**Language evidence:** JavaScript implements the standard-library and internal runtime layers, with substantial first-party C++ and C bindings beneath them.

**Why study it:** It connects high-level JavaScript APIs to native runtime machinery, operating systems, V8, libuv, networking, modules, and diagnostics.

**What you can learn:**

- Runtime bootstrapping, CommonJS/ESM loading, native bindings, event loops, filesystem and network APIs, workers, diagnostics, and compatibility.

**Prerequisites:**

- Expert JavaScript, C++, operating-system APIs, event loops, compilers/runtimes, networking, and concurrent systems.

**Start here:** [`lib/internal/modules/cjs/loader.js`](https://github.com/nodejs/node/blob/4215cc35e25c44f9f4fea5a4541afc862db7ef0a/lib/internal/modules/cjs/loader.js) — The CommonJS loader exposes resolution, caching, cycles, compilation, ESM interoperation, hooks, and internal bindings in a familiar feature.

**Why this level:**

- **S5:** 300,560 meaningful implementation LOC measured with tokei 14.0.0. Count includes first-party JavaScript, TypeScript, C, C headers, and C++ while excluding tests, deps, docs, fixtures, and build output.
- **D5:** Loaders, V8 contexts, native resources, async hooks, workers, crypto, and platform APIs repeatedly require expert runtime knowledge.
- **C5:** Bootstrap, modules, JS libraries, native bindings, V8, libuv, crypto, networking, workers, diagnostics, and tooling interact across the system.
- **Placement:** A large expert runtime with platform-scale architecture reaches SDC 5 on every independent dimension.

**Quality-gate evidence:**

- **Source quality:** Internal modules use hardened primordials, explicit validation, structured errors, and comments around compatibility-sensitive behavior.
- **Architecture:** JavaScript libraries, internal modules, native source, bindings, dependencies, tests, and tooling have established boundaries.
- **Naming and idiom:** Runtime concepts such as contexts, isolates, modules, bindings, handles, hooks, and resources are used consistently.
- **Tests:** Large parallel, sequential, internet, addon, benchmark, and subsystem suites encode API and platform contracts.
- **Documentation:** API documentation, contributor guides, architecture notes, and source comments cover both users and runtime developers.
- **Traceability:** A familiar API such as file opening or require can be traced from JavaScript validation through internal bindings to native code and tests.
- **Maintainability:** Stable internal conventions, subsystem ownership, error codes, and exhaustive regression tests support a long-lived runtime.
- **Educational value:** It lets advanced learners connect JavaScript semantics and APIs to the concrete machinery of a production runtime.

**Inspection record:** commit `4215cc35e25c44f9f4fea5a4541afc862db7ef0a`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `lib/internal/modules/cjs/loader.js`, `src/node.cc`, `test/parallel/test-fs-open.js`. GitHub Linguist label: JavaScript. LOC exclusions: tests and test fixtures, vendored and generated source, build output and caches, documentation and static assets.

**License:** [MIT](https://github.com/nodejs/node/blob/4215cc35e25c44f9f4fea5a4541afc862db7ef0a/LICENSE)

### [react/react](https://github.com/react/react)

**S5 / D5 / C5 → SDC 5**

A component runtime and rendering platform spanning reconciliation, scheduling, server rendering, native/web renderers, and a compiler.

**Real-world evidence:** The repository produces React runtime packages and renderer integrations used to build and operate real user interfaces.

**Language evidence:** JavaScript implements the public packages, reconciler, scheduler integration, renderers, server components, and runtime; Rust supports the compiler.

**Why study it:** It exposes the internals of cooperative scheduling, persistent update queues, fiber reconciliation, rendering phases, hydration, and compilation.

**What you can learn:**

- Fiber data structures, priority lanes, interruptible rendering, commit phases, renderer abstraction, hydration, server components, and compiler analysis.

**Prerequisites:**

- Advanced JavaScript, trees and graph algorithms, scheduling, concurrent state machines, compilers, and browser rendering.

**Start here:** [`packages/react-reconciler/src/ReactFiberWorkLoop.js`](https://github.com/react/react/blob/2dc7da790d6388b95b83198ca9b588b2ad5f5c0b/packages/react-reconciler/src/ReactFiberWorkLoop.js) — The work loop coordinates priorities, render phases, suspension, retries, errors, and commits at the heart of React.

**Why this level:**

- **S5:** 338,536 meaningful implementation LOC measured with tokei 14.0.0. Count includes production JavaScript, TypeScript, and Rust compiler code while excluding tests, fixtures, generated builds, and docs.
- **D5:** Priority lanes, resumable work, effect ordering, suspension, hydration, server protocols, and compiler transforms are expert-level code.
- **C5:** The platform connects public APIs, reconciler, scheduler, DOM/native renderers, server components, hydration, devtools, and compiler packages.
- **Placement:** Every dimension reaches the highest band, so React is unambiguously SDC 5.

**Quality-gate evidence:**

- **Source quality:** Difficult state machines use explicit phase, lane, fiber, and feature-flag vocabulary with extensive invariants and comments.
- **Architecture:** Package boundaries separate public APIs, reconciliation, scheduling, renderers, server behavior, shared utilities, and compiler code.
- **Naming and idiom:** Domain terminology is consistent enough to trace priorities, roots, fibers, updates, effects, and commits across subsystems.
- **Tests:** Specialized renderers and scheduler logs test ordering, interruption, retries, effects, hydration, errors, and compatibility contracts.
- **Documentation:** Public documentation is extensive, while repository READMEs and source comments orient contributors to internal packages.
- **Traceability:** A state update can be followed through queues, lanes, the fiber work loop, completion, commit, and priority-order tests.
- **Maintainability:** Shared reconciler contracts let multiple renderers reuse hard logic while feature flags isolate staged behavior.
- **Educational value:** For prepared readers, it is a rare public implementation of a mature cooperative rendering runtime and compiler ecosystem.

**Inspection record:** commit `2dc7da790d6388b95b83198ca9b588b2ad5f5c0b`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `packages/react/src/ReactClient.js`, `packages/react-reconciler/src/ReactFiberWorkLoop.js`, `packages/react-reconciler/src/__tests__/ReactIncrementalUpdates-test.js`. GitHub Linguist label: JavaScript. LOC exclusions: tests and test fixtures, vendored and generated source, build output and caches, documentation and static assets.

**License:** [MIT](https://github.com/react/react/blob/2dc7da790d6388b95b83198ca9b588b2ad5f5c0b/LICENSE)

_Generated from `catalog/javascript.json`; do not edit by hand._

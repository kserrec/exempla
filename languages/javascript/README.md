# JavaScript

10 qualified repositories. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

[← All languages](../README.md)

## Level 1

### [sindresorhus/escape-string-regexp](https://github.com/sindresorhus/escape-string-regexp)

**Language 1 / Behavior 1 / Design 1 / Constraints 2 → Level 1**

A focused npm utility that escapes regular-expression metacharacters in strings.

**Real-world evidence:** npm published version 5.0.0 without a deprecation notice, and the public registry reported 361,397,477 downloads for 2026-08-22 through 2026-08-28.

**Language evidence:** The first-party runtime is exported from index.js as an ES module and its direct runtime suite is JavaScript; GitHub also labels the repository JavaScript at the metadata check.

**Why study it:** One short function demonstrates how input validation, staged transformation, compatibility-driven representation, tests, and explicit API limits fit into production utility code.

**What you can learn:**

- Use `index.js` to study narrow input contracts, staged string replacement, compatibility-driven escaping choices, boundary-focused tests, and documented safety limits.

**Prerequisites:**

- Before reading `index.js`, be familiar with JavaScript functions, strings, regular-expression literals, replacement strings, exceptions, and the idea that some characters have special meaning in a regular expression.

**Coding relevance:**

The hard part is a transferable programming decision: enforce a small API contract, choose representations that preserve compatibility, test the boundaries, and state where the abstraction does not apply.

Required domain context:

- The path requires only the README's short explanation that regular expressions reserve metacharacters and that a hyphen needs a hexadecimal form for PCRE and Unicode-pattern compatibility in this utility.

**Learning path:**

- **Goal:** Understand how a small JavaScript utility validates a string and escapes regular-expression metacharacters while preserving its stated PCRE and Unicode-pattern compatibility for hyphens.
- **Start here:** [`index.js`](https://github.com/sindresorhus/escape-string-regexp/blob/cbc42403142c96923b482604e1f3d627b1956aff/index.js) — The file contains the entire production contract: the input guard and both escaping passes, including the comment that explains the non-obvious hexadecimal hyphen representation.
- **Then read:**
  - [`test.js`](https://github.com/sindresorhus/escape-string-regexp/blob/cbc42403142c96923b482604e1f3d627b1956aff/test.js)
  - [`readme.md`](https://github.com/sindresorhus/escape-string-regexp/blob/cbc42403142c96923b482604e1f3d627b1956aff/readme.md)
- **Trace:** Enter escapeStringRegexp, reject a non-string, backslash-escape the ordinary metacharacter set with the replacement token, encode each hyphen as a hexadecimal escape, then close the shipped behavior with the complete metacharacter output and both PCRE- and Unicode-compatible hyphen cases in test.js.

**Why this level:**

- **Language technique 1:** A learner needs only basic functions, strings, a type check, regular-expression literals, and replace calls to read the entire path.
- **Behavioral reasoning 1:** The input either fails one immediate guard or flows locally through two deterministic replacements to the returned string.
- **Design span 1:** One focused implementation unit and its direct tests contain the complete selected behavior.
- **Constraint burden 2:** Input validation, exact output, localized compatibility, and explicit safety limits are routine production safeguards rather than interacting advanced constraints.
- **Placement:** The 1/1/1/2 profile sums to 5, so the published formula yields Level 1; the localized compatibility safeguard does not make the direct path structurally or behaviorally advanced.

**Quality-gate evidence:**

- **Source quality:** The short implementation is intentional, and its comment explains why the second replacement uses a hexadecimal escape instead of a simpler form.
- **Architecture:** A single-purpose exported function and one direct runtime suite are a coherent structure for the complete selected behavior.
- **Naming and idiom:** escapeStringRegexp states the contract directly, and the implementation uses conventional ES-module export, validation, and string replacement.
- **Tests:** The shipped AVA cases cover the complete ordinary metacharacter set and both stated PCRE- and Unicode-compatible hyphen outcomes; they do not claim direct coverage of the TypeError branch.
- **Documentation:** The README explains installation, basic use, the native alternative, minimal escaping, and the interpolation positions where this utility is not sufficient.
- **Traceability:** Every shipped transformation can be followed from the exported call through one of two replace operations into an exact assertion or successful Unicode-regex construction.
- **Maintainability:** The two-stage implementation, explicit compatibility comment, and narrow contract keep changes local and reviewable.
- **Educational value:** The path turns a tiny utility into a concrete lesson about contracts, representation choices, compatibility, tests, and honest abstraction boundaries.

**Inspection record:** commit `cbc42403142c96923b482604e1f3d627b1956aff`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `index.js`, `test.js`, `readme.md`, `package.json`, `license`. GitHub Linguist label: JavaScript.

**License:** MIT ([evidence 1](https://github.com/sindresorhus/escape-string-regexp/blob/cbc42403142c96923b482604e1f3d627b1956aff/license))

### [sindresorhus/slash](https://github.com/sindresorhus/slash)

**Language 1 / Behavior 1 / Design 1 / Constraints 2 → Level 1**

A focused npm utility that converts Windows path separators while preserving extended-length paths.

**Real-world evidence:** npm published version 5.1.0 without a deprecation notice, and the public registry reported 140,366,022 downloads for 2026-08-22 through 2026-08-28.

**Language evidence:** The first-party runtime is exported from index.js as an ES module and its direct runtime suite is JavaScript; GitHub also labels the repository JavaScript at the metadata check.

**Why study it:** A guard and one lexical transformation show how small production utilities make a portability exception explicit and prove both the common and protected cases.

**What you can learn:**

- Use `index.js` to study a small compatibility guard, lexical transformation, Unicode-transparent string handling, explicit exceptions, and boundary-focused tests.

**Prerequisites:**

- Before reading `index.js`, be familiar with JavaScript functions, strings, startsWith, regular-expression replacement, and the distinction between ordinary Windows paths and extended-length paths.

**Coding relevance:**

The selected behavior primarily teaches reusable compatibility engineering: isolate an exception, preserve it exactly, transform only the ordinary case, and test the boundary.

Required domain context:

- The path requires only the README and test explanation that ordinary Windows paths may use backslashes while paths beginning with the extended-length prefix must remain untouched.

**Learning path:**

- **Goal:** Understand how a small JavaScript utility converts Windows separators lexically while preserving extended-length paths whose namespace syntax must remain untouched.
- **Start here:** [`index.js`](https://github.com/sindresorhus/slash/blob/98b618f5a3bfcb5dd374b204868818845b87bb2f/index.js) — The file contains the complete guard-and-transform behavior, so a learner can see the compatibility exception before the ordinary replacement.
- **Then read:**
  - [`test.js`](https://github.com/sindresorhus/slash/blob/98b618f5a3bfcb5dd374b204868818845b87bb2f/test.js)
  - [`readme.md`](https://github.com/sindresorhus/slash/blob/98b618f5a3bfcb5dd374b204868818845b87bb2f/readme.md)
- **Trace:** Enter slash, detect the extended-length prefix and return that input unchanged; otherwise replace every backslash with a forward slash, then close mixed separators, a Windows drive path, Unicode content, and the protected prefix in test.js.

**Why this level:**

- **Language technique 1:** The complete path uses only a direct function, a string-prefix check, a local branch, and a basic replacement.
- **Behavioral reasoning 1:** The function either preserves one protected input class or performs one deterministic lexical transformation.
- **Design span 1:** One focused source unit and its direct tests contain the complete selected contract.
- **Constraint burden 2:** The stable API and one portability exception are routine production safeguards, not several interacting guarantees.
- **Placement:** The 1/1/1/2 profile sums to 5, so the published formula yields Level 1; one compatibility guard does not raise the otherwise direct path.

**Quality-gate evidence:**

- **Source quality:** The implementation exposes its one protected case and ordinary transformation without indirection or hidden state.
- **Architecture:** One exported function and one direct runtime suite are proportionate to this single lexical responsibility.
- **Naming and idiom:** slash and isExtendedLengthPath state the public transformation and its exception directly using conventional JavaScript string operations.
- **Tests:** The shipped AVA cases cover mixed separators, Windows drive syntax, Unicode content, and exact preservation of the extended-length prefix.
- **Documentation:** The README states the portability problem, installation, a cross-platform example, and the exact string-to-string API.
- **Traceability:** Each input follows either the startsWith guard or the replace call and lands in a directly corresponding assertion.
- **Maintainability:** The narrow API, one named compatibility decision, and direct boundary cases make future changes easy to bound.
- **Educational value:** The path is a clear first example of production code that remains simple while preserving a real platform-specific exception.

**Inspection record:** commit `98b618f5a3bfcb5dd374b204868818845b87bb2f`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `index.js`, `test.js`, `readme.md`, `package.json`, `license`. GitHub Linguist label: JavaScript.

**License:** MIT ([evidence 1](https://github.com/sindresorhus/slash/blob/98b618f5a3bfcb5dd374b204868818845b87bb2f/license))

## Level 2

### [mafintosh/pump](https://github.com/mafintosh/pump)

**Language 2 / Behavior 3 / Design 1 / Constraints 3 → Level 2**

A stream piping utility that destroys an entire Node.js pipeline when any component closes or fails.

**Real-world evidence:** The repository publishes an npm stream utility designed to prevent resource leaks in real Node.js pipelines.

**Language evidence:** index.js contains the complete Node.js and browser stream-pipeline implementation in JavaScript.

**Why study it:** Its tiny implementation captures a subtle production concern: coordinating completion, errors, and cleanup across heterogeneous streams.

**What you can learn:**

- Node.js stream lifecycle handling, once-only callbacks, error fan-out, and compatibility boundaries.

**Prerequisites:**

- CommonJS modules, callbacks, Node.js readable and writable streams, and event emitters.

**Coding relevance:**

The short stream context is documented by the project; the path primarily teaches transferable lifecycle coordination, cleanup, and once-only completion.

Required domain context:

- A Node.js stream emits completion, close, and error events and may own an operating-system resource.

**Learning path:**

- **Goal:** Understand how pump tears down every stream and completes exactly once when a pipeline closes or fails.
- **Start here:** [`index.js`](https://github.com/mafintosh/pump/blob/714c0a70a8199104bf65a57582009d42f81d8d94/index.js) — The destroyer helper and final pump reduction expose the whole lifecycle algorithm in one place.
- **Then read:**
  - [`test-node.js`](https://github.com/mafintosh/pump/blob/714c0a70a8199104bf65a57582009d42f81d8d94/test-node.js)
  - [`test-browser.js`](https://github.com/mafintosh/pump/blob/714c0a70a8199104bf65a57582009d42f81d8d94/test-browser.js)
- **Trace:** Follow each stream through the destroyer helper and end-of-stream callback, then follow the pump reduction as an error fans cleanup across siblings and the final writable triggers the one callback; confirm closure and returned-stream behavior in both integration scripts.

**Why this level:**

- **Language technique 2:** Callbacks, event emitters, CommonJS modules, array reduction, and duck-typed stream operations are ordinary professional Node.js idioms.
- **Behavioral reasoning 3:** Several asynchronous lifecycle events may arrive in different orders, and local flags coordinate destruction, error preservation, and final completion.
- **Design span 1:** The whole production behavior fits in one module and one list of streams.
- **Constraint burden 3:** A correct change must avoid leaks and duplicate callbacks while preserving distinct cleanup behavior for filesystem streams, request streams, and older implementations.
- **Placement:** The four scores 2/3/1/3 sum to 9; their arithmetic mean is 2.25 and rounds half-up to Level 2. The published result is Level 2.

**Quality-gate evidence:**

- **Source quality:** Cleanup guards prevent duplicate destruction and preserve the first pipeline error without unnecessary abstraction.
- **Architecture:** A focused destroyer helper composes into one exported pipeline function with no hidden global state.
- **Naming and idiom:** Short names follow the older Node.js style while stream roles and lifecycle flags remain understandable.
- **Tests:** Node and browser integration scripts exercise closure, destruction, callback completion, and returned-stream behavior.
- **Documentation:** The README explains the leak it prevents, callback contract, array form, and concrete stream usage.
- **Traceability:** A stream error flows through end-of-stream, destroyer, sibling cleanup, and the final callback in one file.
- **Maintainability:** The small surface and explicit compatibility checks isolate the few platform-dependent behaviors.
- **Educational value:** It shows why a tiny production library can encode important lifecycle knowledge absent from naive piping.

**Inspection record:** commit `714c0a70a8199104bf65a57582009d42f81d8d94`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `index.js`, `test-node.js`, `test-browser.js`, `LICENSE`. GitHub Linguist label: JavaScript.

**License:** MIT ([evidence 1](https://github.com/mafintosh/pump/blob/714c0a70a8199104bf65a57582009d42f81d8d94/LICENSE))

### [sindresorhus/p-limit](https://github.com/sindresorhus/p-limit)

**Language 2 / Behavior 3 / Design 1 / Constraints 3 → Level 2**

A small promise-concurrency limiter that queues asynchronous functions and caps how many run simultaneously.

**Real-world evidence:** The repository publishes the p-limit npm library as a reusable concurrency control primitive for production JavaScript programs.

**Language evidence:** The public limiter and all runtime behavior are implemented in index.js; TypeScript supplies declarations only.

**Why study it:** One file demonstrates a complete, useful abstraction with careful promise timing, queue state, error propagation, and a compact public API.

**What you can learn:**

- FIFO work scheduling, promise adoption, asynchronous context preservation, and observable queue state.

**Prerequisites:**

- Promises, async functions, closures, and JavaScript property descriptors.

**Coding relevance:**

The selected path is entirely about transferable promise scheduling, bounded concurrency, state transitions, and error propagation.

No specialist domain context is required.

**Learning path:**

- **Goal:** Understand how p-limit admits, queues, runs, and completes promise-returning tasks while preserving a concurrency cap.
- **Start here:** [`index.js`](https://github.com/sindresorhus/p-limit/blob/df476048d023ff868cd45b35ee47f5fb0ca2b25a/index.js) — The entire runtime contract, queue, transitions, and public API are visible in this one implementation file.
- **Then read:**
  - [`test.js`](https://github.com/sindresorhus/p-limit/blob/df476048d023ff868cd45b35ee47f5fb0ca2b25a/test.js)
  - [`index.d.ts`](https://github.com/sindresorhus/p-limit/blob/df476048d023ff868cd45b35ee47f5fb0ca2b25a/index.d.ts)
- **Trace:** Call the returned generator, follow enqueue as it stores a runnable closure, resumeNext as it increments activeCount, run as it adopts success or failure, and next as it releases capacity; then correlate the concurrency, error, queue, and async-context tests.

**Why this level:**

- **Language technique 2:** The path uses common professional JavaScript idioms—closures, async functions, promise adoption, property descriptors, and bound callbacks—without expert language machinery.
- **Behavioral reasoning 3:** Admission, active and pending counts, microtask order, synchronous throws, rejected promises, and queue resumption materially affect the trace.
- **Design span 1:** The complete behavior remains in one factory and one source file, with the declaration and tests explaining its public boundary.
- **Constraint burden 3:** A correct change must preserve the concurrency ceiling, queue progress after failures, observable counts, result and rejection adoption, and asynchronous execution context.
- **Placement:** The four scores 2/3/1/3 sum to 9; their arithmetic mean is 2.25 and rounds half-up to Level 2. The published result is Level 2.

**Quality-gate evidence:**

- **Source quality:** Queue transitions are compact, explicit, and guarded against both synchronous throws and rejected promises.
- **Architecture:** A single factory cleanly contains scheduling state and returns one callable public abstraction.
- **Naming and idiom:** Names such as activeCount, pendingCount, resumeNext, and clearQueue state the contract directly.
- **Tests:** AVA tests cover concurrency limits, thrown errors, queue clearing, dynamic limits, and asynchronous context propagation.
- **Documentation:** The README documents the API, counters, mapping helper, mutable concurrency, and usage examples.
- **Traceability:** A call can be followed through generator, enqueue, run, next, and its matching tests in minutes.
- **Maintainability:** The narrow API, isolated validation, and visible state invariants make changes reviewable.
- **Educational value:** It teaches production promise coordination without framework scaffolding or irrelevant repository machinery.

**Inspection record:** commit `df476048d023ff868cd45b35ee47f5fb0ca2b25a`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `index.js`, `test.js`, `index.d.ts`, `license`. GitHub Linguist label: JavaScript.

**License:** MIT ([evidence 1](https://github.com/sindresorhus/p-limit/blob/df476048d023ff868cd45b35ee47f5fb0ca2b25a/license))

## Level 3

### [ai/nanoid](https://github.com/ai/nanoid)

**Language 2 / Behavior 2 / Design 2 / Constraints 4 → Level 3**

A compact secure unique-ID generator for JavaScript runtimes with customizable alphabets and output lengths.

**Real-world evidence:** The repository ships Nano ID for Node.js, browsers, and package ecosystems as a production identifier library.

**Language evidence:** Node and browser generators, alphabets, and public entry points are first-party JavaScript with declaration files alongside them.

**Why study it:** A small surface demonstrates cryptographic randomness, unbiased alphabet mapping, performance-conscious pooling, and cross-runtime packaging.

**What you can learn:**

- Rejection sampling, entropy preservation, typed-array operations, runtime-specific entry points, and property-focused tests.

**Prerequisites:**

- Typed arrays, bitwise operations, cryptographic random APIs, modules, and elementary probability.

**Coding relevance:**

The required probability is elementary and self-contained in source comments; the path mainly teaches secure API use, rejection sampling, typed arrays, validation, portability, and performance-conscious implementation.

Required domain context:

- Mapping random bytes to an alphabet is uniform only when remainder values that would bias a symbol are rejected; the implementation explains this with a concrete 17-symbol example.

**Learning path:**

- **Goal:** Understand how Nano ID converts cryptographically random bytes into uniformly distributed custom-alphabet identifiers without runtime-size or modulo-bias errors.
- **Start here:** [`index.js`](https://github.com/ai/nanoid/blob/07a39d62d84c21af5046fe6b2ef7b3e36ee557db/index.js) — The secure generator explains modulo bias, fast paths, pooling, and the customizable public API together.
- **Then read:**
  - [`index.browser.js`](https://github.com/ai/nanoid/blob/07a39d62d84c21af5046fe6b2ef7b3e36ee557db/index.browser.js)
  - [`test/index.test.js`](https://github.com/ai/nanoid/blob/07a39d62d84c21af5046fe6b2ef7b3e36ee557db/test/index.test.js)
- **Trace:** Start with customRandom's cutoff and power-of-two fast path, follow rejected bytes and size validation into the returned generator, compare the browser variant's random source, and verify length, bounds, custom alphabet, and flat-distribution tests.

**Why this level:**

- **Language technique 2:** The path uses common professional typed-array, closure, module, and bitwise idioms rather than metaprogramming or expert language machinery.
- **Behavioral reasoning 2:** Several branches and a small retry lifecycle matter, but the state remains local and directly visible.
- **Design span 2:** A few explicit runtime modules implement the same small public abstraction.
- **Constraint burden 4:** Security, distribution correctness, hostile size conversion, browser random-byte limits, cross-runtime equivalence, collision properties, and hot-path performance interact throughout the selected generator.
- **Placement:** The four scores 2/2/2/4 sum to 10; their arithmetic mean is 2.50 and rounds half-up to Level 3. The published result is Level 3.

**Quality-gate evidence:**

- **Source quality:** The implementation explains every non-obvious constant and separates generic randomness from optimized alphabet paths.
- **Architecture:** Runtime-specific entry points reuse a small core instead of duplicating the public generator model.
- **Naming and idiom:** Names expose entropy cutoffs, masks, pools, and offsets while modern modules keep boundaries explicit.
- **Tests:** Tests cover distribution, collision resistance, invalid sizes, huge buffers, custom alphabets, and browser behavior.
- **Documentation:** The README explains security, collision probability, APIs, runtime usage, and performance tradeoffs.
- **Traceability:** A nanoid call can be followed from the export through pooled random bytes to the flat-distribution tests.
- **Maintainability:** Fast and generic paths are separated, documented, and exercised against adversarial input conversions.
- **Educational value:** It makes a security-sensitive algorithm readable without pretending secure IDs are just random string concatenation.

**Inspection record:** commit `07a39d62d84c21af5046fe6b2ef7b3e36ee557db`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `index.js`, `index.browser.js`, `test/index.test.js`, `LICENSE`. GitHub Linguist label: JavaScript.

**License:** MIT ([evidence 1](https://github.com/ai/nanoid/blob/07a39d62d84c21af5046fe6b2ef7b3e36ee557db/LICENSE))

### [jquery/jquery](https://github.com/jquery/jquery)

**Language 3 / Behavior 2 / Design 2 / Constraints 4 → Level 3**

A browser library that normalizes DOM traversal, manipulation, events, Ajax, data, and effects behind a chainable API.

**Real-world evidence:** The repository builds and releases the jQuery browser library as real compatibility software, not an instructional implementation.

**Language evidence:** The modular DOM, events, data, Ajax, traversal, and effects implementation is JavaScript under src.

**Why study it:** The core factory path shows how jQuery turns varied selector inputs into one array-like, chainable collection while preserving deep-extension compatibility and prototype-pollution defenses.

**What you can learn:**

- Use `src/core.js` to study the following transferable techniques and behaviors: Prototype-based fluent objects, constructor indirection, selector-input classification, array-like collections, shallow and deep extension, document-ready callbacks, and prototype-pollution prevention.

**Prerequisites:**

- Before reading `src/core.js`, be familiar with the following concepts: JavaScript prototypes, constructor functions, array-like objects, browser DOM nodes, callbacks, recursion, and object-property copying.

**Coding relevance:**

The short DOM context is sufficient; collection construction, prototype design, recursive extension, input classification, compatibility, and security hardening are transferable programming lessons.

Required domain context:

- A DOM element is a browser object, and a jQuery collection wraps zero or more elements behind a chainable API.

**Learning path:**

- **Goal:** Understand how jQuery constructs an array-like chainable collection from different selector inputs and extends its shared prototype safely.
- **Start here:** [`src/core.js`](https://github.com/jquery/jquery/blob/71c0dd14927c41d1aab5ce5ef2687d7808a4186b/src/core.js) — src/core.js defines the jQuery factory, shared prototype, and extend operation before src/core/init.js classifies empty values, DOM nodes, callbacks, IDs, and HTML inputs.
- **Then read:**
  - [`src/core/init.js`](https://github.com/jquery/jquery/blob/71c0dd14927c41d1aab5ce5ef2687d7808a4186b/src/core/init.js)
  - [`test/unit/core.js`](https://github.com/jquery/jquery/blob/71c0dd14927c41d1aab5ce5ef2687d7808a4186b/test/unit/core.js)
- **Trace:** Start at the jQuery factory and prototype, follow init as it classifies empty values, DOM nodes, callbacks, IDs, and HTML, then follow extend's shallow and deep copy rules; correlate constructor, extension, recursion, and security cases in the core tests.

**Why this level:**

- **Language technique 3:** Prototype aliasing, constructor indirection, dynamic input classification, array-like collections, and recursive extension materially shape the path.
- **Behavioral reasoning 2:** Input kind and context select explicit synchronous branches, while recursive merge and ready callbacks remain localized rather than forming a distributed state machine.
- **Design span 2:** The selected behavior stays within a few closely related core modules and their focused tests.
- **Constraint burden 4:** DOM quirks, accepted selector forms, deep-copy semantics, prototype safety, modular builds, performance, and decades of compatibility interact in the core path.
- **Placement:** The four scores 3/2/2/4 sum to 11; their arithmetic mean is 2.75 and rounds half-up to Level 3. The published result is Level 3.

**Quality-gate evidence:**

- **Source quality:** The factory, prototype, and extension logic use explicit branches, while src/core/init.js isolates the input-classification behavior that constructs each collection.
- **Architecture:** The selected path stays within the core factory, the init constructor, one shared collection prototype, and their focused core tests.
- **Naming and idiom:** jQuery, fn, init, extend, pushStack, selector, context, and ready consistently describe construction and fluent collection behavior.
- **Tests:** test/unit/core.js covers constructor inputs, prototype extension, recursive copying, and security cases such as `__proto__` pollution.
- **Documentation:** The README and maintained public API documentation provide the collection-construction and extension context needed to follow `src/core.js`.
- **Traceability:** A call to jQuery can be followed from the factory into init's input branches and back through the shared prototype, while extend can be traced independently into the core tests.
- **Maintainability:** A shared prototype and separate input constructor localize the historical API, browser-compatibility, deep-copy, and prototype-safety constraints.
- **Educational value:** The path demonstrates how a mature JavaScript library builds a compact fluent object model without hiding its compatibility and security obligations.

**Inspection record:** commit `71c0dd14927c41d1aab5ce5ef2687d7808a4186b`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `src/core.js`, `src/core/init.js`, `test/unit/core.js`, `LICENSE.txt`. GitHub Linguist label: JavaScript.

**License:** MIT ([evidence 1](https://github.com/jquery/jquery/blob/71c0dd14927c41d1aab5ce5ef2687d7808a4186b/LICENSE.txt))

## Level 4

### [eslint/eslint](https://github.com/eslint/eslint)

**Language 3 / Behavior 4 / Design 4 / Constraints 4 → Level 4**

A configurable static-analysis engine and CLI for identifying and automatically fixing JavaScript problems.

**Real-world evidence:** The repository publishes ESLint as an extensible linter used in development and continuous-integration workflows.

**Language evidence:** The linter engine, configuration loaders, rule traversal, fixes, CLI engine, and services are JavaScript under lib.

**Why study it:** Starting at the public lintText entry point reveals the full analysis lifecycle: configuration lookup, parser and rule isolation, event-driven traversal, diagnostic suppression, and conflict-safe iterative fixes.

**What you can learn:**

- Use `lib/eslint/eslint.js` to study the following transferable techniques and behaviors: Public API orchestration, abstract-syntax-tree traversal, visitor dispatch, plugin isolation, configuration resolution, stable diagnostics, suppression accounting, and multipass autofix handling.

**Prerequisites:**

- Before reading `lib/eslint/eslint.js`, be familiar with the following concepts: JavaScript modules and callbacks, abstract syntax trees, visitor traversal, configuration objects, source ranges, and ordinary linter concepts.

**Coding relevance:**

The short static-analysis context is documented; the selected path teaches transferable visitor dispatch, extension isolation, configuration, diagnostics, suppression, conflict-safe fixes, caching, and error handling.

Required domain context:

- A linter parses source into an abstract syntax tree and invokes configured rule listeners as that tree is traversed.

**Learning path:**

- **Goal:** Understand how ESLint parses one source file, creates isolated rule listeners, traverses the source, reports and suppresses diagnostics, and applies safe iterative fixes.
- **Start here:** [`lib/eslint/eslint.js`](https://github.com/eslint/eslint/blob/5634542be580750ffb1a5766470f9e9c72719696/lib/eslint/eslint.js) — ESLint.lintText is the learner-facing entry point that assembles configuration and result handling before delegating to the linter engine, so it exposes the selected end-to-end path without beginning inside an internal subsystem.
- **Then read:**
  - [`lib/eslint/eslint-helpers.js`](https://github.com/eslint/eslint/blob/5634542be580750ffb1a5766470f9e9c72719696/lib/eslint/eslint-helpers.js)
  - [`lib/linter/linter.js`](https://github.com/eslint/eslint/blob/5634542be580750ffb1a5766470f9e9c72719696/lib/linter/linter.js)
  - [`lib/linter/source-code-fixer.js`](https://github.com/eslint/eslint/blob/5634542be580750ffb1a5766470f9e9c72719696/lib/linter/source-code-fixer.js)
  - [`tests/lib/linter/linter.js`](https://github.com/eslint/eslint/blob/5634542be580750ffb1a5766470f9e9c72719696/tests/lib/linter/linter.js)
- **Trace:** Enter through ESLint.lintText and its configuration and result helpers, continue into Linter verification, parser and SourceCode creation, runRules, rule-context creation, and visitor dispatch, then follow reports through suppression and source-code-fixer passes; confirm message ordering, rule failures, suppression, and autofix behavior in the linter tests.

**Why this level:**

- **Language technique 3:** Visitor callbacks, dynamic rule contexts, plugin interfaces, private state, and structured AST/source models materially shape the path.
- **Behavioral reasoning 4:** Rule listeners, traversal order, processor blocks, inline directives, suppression accounting, fix conflicts, repeated verification, and plugin failures interact nonlocally.
- **Design span 4:** One lint request crosses many extension points, services, representation boundaries, and cross-cutting diagnostic policies.
- **Constraint burden 4:** Correctness, deterministic diagnostics, safe fixes, plugin errors, source ranges, configuration semantics, and compatibility recur throughout the path.
- **Placement:** The four scores 3/4/4/4 sum to 15; their arithmetic mean is 3.75 and rounds half-up to Level 4. The published result is Level 4.

**Quality-gate evidence:**

- **Source quality:** The public lintText orchestration delegates configuration, source verification, suppression, and fixing to named helpers with explicit result and failure paths.
- **Architecture:** ESLint orchestration, configuration helpers, the Linter engine, parser and SourceCode creation, rule listeners, and the source-code fixer have distinct responsibilities.
- **Naming and idiom:** lintText, runRules, SourceCode, rule listeners, suppressions, messages, and fixes consistently describe each stage of one lint request.
- **Tests:** The selected linter tests exercise message ordering, rule failures, suppression behavior, fix conflicts, repeated fix passes, parser behavior, and extension errors.
- **Documentation:** User and extension documentation explains configuration, rules, parsers, plugins, diagnostics, and fixes needed to follow the selected linting path.
- **Traceability:** A learner can follow lintText through configuration and verification into visitor dispatch, reported messages, suppression accounting, and source-code-fixer passes, then match each outcome to focused tests.
- **Maintainability:** Stable public orchestration and explicit parser, rule, source, and fixer boundaries keep third-party extension behavior out of unrelated control flow.
- **Educational value:** This path shows how a production static-analysis platform turns configurable third-party visitors into deterministic diagnostics and safe edits.

**Inspection record:** commit `5634542be580750ffb1a5766470f9e9c72719696`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `lib/eslint/eslint.js`, `lib/eslint/eslint-helpers.js`, `lib/linter/linter.js`, `lib/linter/source-code-fixer.js`, `tests/lib/linter/linter.js`, `LICENSE`. GitHub Linguist label: JavaScript.

**License:** MIT ([evidence 1](https://github.com/eslint/eslint/blob/5634542be580750ffb1a5766470f9e9c72719696/LICENSE))

### [prettier/prettier](https://github.com/prettier/prettier)

**Language 3 / Behavior 4 / Design 4 / Constraints 4 → Level 4**

An opinionated source-code formatter that parses many languages, builds a document representation, and prints stable layouts.

**Real-world evidence:** The repository releases a formatter CLI, library, standalone browser builds, and editor-facing plugins used on real codebases.

**Language evidence:** The formatter core, document intermediate representation, printers, parser adapters, and plugins are JavaScript under src.

**Why study it:** The core formatting path makes a production pretty-printer concrete by connecting parsing, abstract-syntax-tree conversion, document layout, comment handling, and cursor preservation.

**What you can learn:**

- Use `src/main/core.js` to study the following transferable techniques and behaviors: Parser-plugin resolution, abstract-syntax-tree modeling, document intermediate representations, constrained layout, comment attachment, line-ending normalization, cursor relocation, and snapshot testing.

**Prerequisites:**

- Before reading `src/main/core.js`, be familiar with the following concepts: JavaScript modules and asynchronous functions, abstract syntax trees, recursive tree traversal, immutable transformations, parsing, and basic compiler pipelines.

**Coding relevance:**

The repository documents the compiler-shaped pipeline, and its hard parts teach transferable parsing adapters, staged transformations, immutable layout representations, deterministic output, and compatibility engineering.

Required domain context:

- A formatter parses source into an abstract syntax tree, converts it to a layout document, and prints that document under width and option constraints.

**Learning path:**

- **Goal:** Understand how Prettier formats source through parsing, AST-to-document conversion, document printing, and cursor preservation.
- **Start here:** [`src/main/core.js`](https://github.com/prettier/prettier/blob/0283c8848ecb541c7ea0601ff274799bce1b39e5/src/main/core.js) — src/main/core.js coordinates parser selection, parseText, printAstToDoc, document rendering, line endings, and cursor relocation, so it exposes the complete selected formatting request.
- **Then read:**
  - [`src/language-js/parse/babel.js`](https://github.com/prettier/prettier/blob/0283c8848ecb541c7ea0601ff274799bce1b39e5/src/language-js/parse/babel.js)
  - [`src/main/ast-to-doc.js`](https://github.com/prettier/prettier/blob/0283c8848ecb541c7ea0601ff274799bce1b39e5/src/main/ast-to-doc.js)
  - [`src/document/printer/printer.js`](https://github.com/prettier/prettier/blob/0283c8848ecb541c7ea0601ff274799bce1b39e5/src/document/printer/printer.js)
  - [`src/main/get-cursor-node.js`](https://github.com/prettier/prettier/blob/0283c8848ecb541c7ea0601ff274799bce1b39e5/src/main/get-cursor-node.js)
  - [`tests/format/js/arrays/format.test.js`](https://github.com/prettier/prettier/blob/0283c8848ecb541c7ea0601ff274799bce1b39e5/tests/format/js/arrays/format.test.js)
  - [`tests/format/js/arrays/__snapshots__/format.test.js.snap`](https://github.com/prettier/prettier/blob/0283c8848ecb541c7ea0601ff274799bce1b39e5/tests/format/js/arrays/__snapshots__/format.test.js.snap)
  - [`tests/integration/__tests__/cursor-offset.js`](https://github.com/prettier/prettier/blob/0283c8848ecb541c7ea0601ff274799bce1b39e5/tests/integration/__tests__/cursor-offset.js)
- **Trace:** Follow coreFormat into parser resolution and parseText, then through printAstToDoc and the document printer; continue through line-ending, comment, and cursor-node relocation handling, and finish with a concrete JavaScript arrays fixture, its expected snapshot, and cursor-offset integration tests.

**Why this level:**

- **Language technique 3:** Higher-order composition, parser plugins, AST and document modeling, and asynchronous stages materially shape the path without pervasive expert JavaScript machinery.
- **Behavioral reasoning 4:** Parsing, comment attachment, document layout, cursor-node tracking, diff-based relocation, and error recovery create recurring nonlocal invariants.
- **Design span 4:** Many modules, language plugins, intermediate representations, option policies, and test fixtures contribute to one formatting request.
- **Constraint burden 4:** A locally plausible change can alter syntax coverage, comments, formatting stability, cursor positions, line endings, plugin behavior, or performance across languages.
- **Placement:** The four scores 3/4/4/4 sum to 15; their arithmetic mean is 3.75 and rounds half-up to Level 4. The published result is Level 4.

**Quality-gate evidence:**

- **Source quality:** Named stages in core.js, ast-to-doc.js, and the document printer separate parsing, intermediate representation construction, layout, and result adjustment.
- **Architecture:** The path crosses an explicit parser-plugin boundary, an AST-to-document stage, a document renderer, and narrow cursor-mapping helpers.
- **Naming and idiom:** coreFormat, parseText, printAstToDoc, printDocToString, getCursorNode, and cursorOffset state each transformation and observable result directly.
- **Tests:** The selected JavaScript array fixture and snapshot prove formatted output, while cursor-offset integration tests exercise relocation across formatting changes.
- **Documentation:** Contributor and plugin documentation explains Prettier's parser, printer, document, option, and fixture contracts needed to follow this path.
- **Traceability:** A format request can be followed from coreFormat through Babel parsing, AST-to-document conversion, document rendering, and cursor relocation into one concrete fixture, snapshot, and integration suite.
- **Maintainability:** Stable parser and printer contracts plus deterministic fixtures constrain changes across language syntax, comments, layout, line endings, and cursor behavior.
- **Educational value:** The path provides an evidence-backed view of compiler-shaped JavaScript software whose intermediate representation and output constraints are visible end to end.

**Inspection record:** commit `0283c8848ecb541c7ea0601ff274799bce1b39e5`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `src/main/core.js`, `src/language-js/parse/babel.js`, `src/main/ast-to-doc.js`, `src/document/printer/printer.js`, `src/main/get-cursor-node.js`, `tests/format/js/arrays/format.test.js`, `tests/format/js/arrays/__snapshots__/format.test.js.snap`, `tests/integration/__tests__/cursor-offset.js`, `LICENSE`. GitHub Linguist label: JavaScript.

**License:** MIT ([evidence 1](https://github.com/prettier/prettier/blob/0283c8848ecb541c7ea0601ff274799bce1b39e5/LICENSE))

## Level 5

### [nodejs/node](https://github.com/nodejs/node)

**Language 4 / Behavior 5 / Design 5 / Constraints 5 → Level 5**

The Node.js runtime, standard library, module loaders, native bindings, event loop integration, diagnostics, and tooling.

**Real-world evidence:** This repository builds the released Node.js executable and standard library used to run server, command-line, and tooling workloads.

**Language evidence:** JavaScript implements the standard-library and internal runtime layers, with substantial first-party C++ and C bindings beneath them.

**Why study it:** The CommonJS loader path connects require to resolution, caching, circular dependencies, wrapper compilation, extension handling, and failure cleanup inside a production runtime.

**What you can learn:**

- Use `lib/internal/modules/cjs/loader.js` to study the following transferable techniques and behaviors: Module resolution, cache identity, circular exports, built-in modules, extension dispatch, source wrapping, dynamic compilation, parent-child relationships, and failed-load cleanup.

**Prerequisites:**

- Before reading `lib/internal/modules/cjs/loader.js`, be familiar with the following concepts: Expert JavaScript, CommonJS modules, filesystem paths, package resolution, caches, dynamic compilation, and basic runtime internals.

**Coding relevance:**

The documented module model is sufficient context; the selected path's difficulty is transferable runtime, cache, resolution, compilation, compatibility, security, and error-recovery engineering.

Required domain context:

- CommonJS require resolves a module specifier, caches module instances to support reuse and cycles, wraps source with module variables, and executes it in the runtime.

**Learning path:**

- **Goal:** Understand how Node.js resolves, caches, loads, compiles, and returns a classic CommonJS module while handling built-ins, cycles, extensions, and failures.
- **Start here:** [`lib/internal/modules/cjs/loader.js`](https://github.com/nodejs/node/blob/4215cc35e25c44f9f4fea5a4541afc862db7ef0a/lib/internal/modules/cjs/loader.js) — lib/internal/modules/cjs/loader.js contains Module._load, Module._resolveFilename, Module.prototype._compile, wrapper execution, caches, and extension dispatch for the selected classic CommonJS trace.
- **Then read:**
  - [`doc/api/modules.md`](https://github.com/nodejs/node/blob/4215cc35e25c44f9f4fea5a4541afc862db7ef0a/doc/api/modules.md)
  - [`test/sequential/test-module-loading.js`](https://github.com/nodejs/node/blob/4215cc35e25c44f9f4fea5a4541afc862db7ef0a/test/sequential/test-module-loading.js)
  - [`test/parallel/test-module-cache.js`](https://github.com/nodejs/node/blob/4215cc35e25c44f9f4fea5a4541afc862db7ef0a/test/parallel/test-module-cache.js)
- **Trace:** Start with the documented CommonJS loading model and Module._load, follow relative and module-cache fast paths, circular-export handling, Module._resolveFilename, instance creation, then Module.prototype._compile and wrapSafe; correlate main-module, extension, path, cache, cycle, load-error, and failed-resolution invalidation cases in the module-loading tests.

**Why this level:**

- **Language technique 4:** Dynamic compilation, proxy behavior, symbol-keyed internal state, hardened built-ins, format detection, and native runtime interfaces recur throughout the loader.
- **Behavioral reasoning 5:** Caches, parent-child relationships, cycles, rollback, format detection, resolution, extensions, and compilation interact pervasively.
- **Design span 5:** The familiar require path coordinates several major runtime subsystems and pervasive policy mechanisms.
- **Constraint burden 5:** A loader change can break security boundaries, cache identity, cycles, package resolution, built-ins, source maps, performance, diagnostics, or long-standing cross-platform compatibility.
- **Placement:** The four scores 4/5/5/5 sum to 19; their arithmetic mean is 4.75 and rounds half-up to Level 5. The published result is Level 5.

**Quality-gate evidence:**

- **Source quality:** The loader uses hardened primordial operations, structured errors, explicit cache transitions, and detailed comments around circular and compatibility-sensitive cases.
- **Architecture:** Resolution, module and path caches, built-ins, wrapper compilation, filesystem access, and extension handlers meet at named loader boundaries.
- **Naming and idiom:** Module._load, Module._resolveFilename, Module._compile, wrapSafe, _cache, _pathCache, loaded, parent, and children expose the loader lifecycle.
- **Tests:** The selected module-loading and cache suites cover main modules, paths, extensions, cycles, load failures, and invalidation after failed resolution.
- **Documentation:** doc/api/modules.md documents the CommonJS wrapper, resolution algorithm, cache, cycles, main module, and extension behavior followed in source.
- **Traceability:** A require call can be followed through Module._load, cache and cycle branches, filename resolution, module construction, source compilation, and the selected module tests.
- **Maintainability:** Stable internal conventions, structured error codes, explicit caches, and broad loader regressions protect long-standing package and platform compatibility.
- **Educational value:** The path lets advanced learners connect a familiar JavaScript API to the runtime machinery that preserves identity, cycles, compilation, and recovery.

**Inspection record:** commit `4215cc35e25c44f9f4fea5a4541afc862db7ef0a`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `lib/internal/modules/cjs/loader.js`, `doc/api/modules.md`, `test/sequential/test-module-loading.js`, `test/parallel/test-module-cache.js`, `LICENSE`. GitHub Linguist label: JavaScript.

**License:** MIT ([evidence 1](https://github.com/nodejs/node/blob/4215cc35e25c44f9f4fea5a4541afc862db7ef0a/LICENSE))

### [react/react](https://github.com/react/react)

**Language 3 / Behavior 5 / Design 5 / Constraints 5 → Level 5**

A component runtime and rendering platform spanning reconciliation, scheduling, server rendering, native/web renderers, and a compiler.

**Real-world evidence:** The repository produces React runtime packages and renderer integrations used to build and operate real user interfaces.

**Language evidence:** JavaScript implements the public packages, reconciler, scheduler integration, renderers, server components, and runtime; Rust supports the compiler.

**Why study it:** The reconciler work-loop path shows how React assigns a state update to priority lanes, performs interruptible fiber work, rebases deferred updates, and commits effects in order.

**What you can learn:**

- Use `packages/react-reconciler/src/ReactFiberWorkLoop.js` to study the following transferable techniques and behaviors: Fiber update queues, priority lanes, root scheduling, synchronous and concurrent rendering, interruption, rebasing, effect collection, and commit ordering.

**Prerequisites:**

- Before reading `packages/react-reconciler/src/ReactFiberWorkLoop.js`, be familiar with the following concepts: Advanced JavaScript, recursive trees, queues, cooperative scheduling, priority systems, persistent state, and concurrent state-machine reasoning.

**Coding relevance:**

The repository's tests and source vocabulary make the rendering model learnable; the difficulty comes from transferable scheduling, persistent queues, state machines, interruption, recovery, and side-effect ordering rather than an external specialist discipline.

Required domain context:

- A component update is represented as work on a fiber tree and assigned a priority lane before rendering and committing observable effects.

**Learning path:**

- **Goal:** Understand how React schedules a state update by lane, performs interruptible work on the fiber root, and commits effects in the required order.
- **Start here:** [`packages/react-reconciler/src/ReactFiberWorkLoop.js`](https://github.com/react/react/blob/2dc7da790d6388b95b83198ca9b588b2ad5f5c0b/packages/react-reconciler/src/ReactFiberWorkLoop.js) — ReactFiberWorkLoop.js coordinates scheduled root work, render phases, interruption, completion, and commits after an update enters through the reconciler and class update queue.
- **Then read:**
  - [`packages/react-reconciler/src/ReactFiberReconciler.js`](https://github.com/react/react/blob/2dc7da790d6388b95b83198ca9b588b2ad5f5c0b/packages/react-reconciler/src/ReactFiberReconciler.js)
  - [`packages/react-reconciler/src/ReactFiberClassUpdateQueue.js`](https://github.com/react/react/blob/2dc7da790d6388b95b83198ca9b588b2ad5f5c0b/packages/react-reconciler/src/ReactFiberClassUpdateQueue.js)
  - [`packages/react-reconciler/src/ReactFiberRootScheduler.js`](https://github.com/react/react/blob/2dc7da790d6388b95b83198ca9b588b2ad5f5c0b/packages/react-reconciler/src/ReactFiberRootScheduler.js)
  - [`packages/react-reconciler/src/ReactFiberCommitWork.js`](https://github.com/react/react/blob/2dc7da790d6388b95b83198ca9b588b2ad5f5c0b/packages/react-reconciler/src/ReactFiberCommitWork.js)
  - [`packages/react-reconciler/src/__tests__/ReactIncrementalUpdates-test.js`](https://github.com/react/react/blob/2dc7da790d6388b95b83198ca9b588b2ad5f5c0b/packages/react-reconciler/src/__tests__/ReactIncrementalUpdates-test.js)
- **Trace:** Enter through updateContainer and its queued update, follow scheduleUpdateOnFiber as it marks lanes, continue through root scheduling and concurrent or synchronous rendering, then through commitRoot and priority, interruption, rebasing, and commit-order tests using the no-op renderer and scheduler log.

**Why this level:**

- **Language technique 3:** Substantial type modeling, higher-order APIs, recursive fiber structures, and framework conventions shape the path, while the hardest burdens are behavioral and architectural rather than JavaScript metaprogramming.
- **Behavioral reasoning 5:** Concurrent state, priority, starvation prevention, interruption, rebasing, deferred work, effects, and commit ordering interact pervasively and require expert nonlocal reasoning.
- **Design span 5:** Understanding the chosen update path requires coordinating major reconciler subsystems, execution modes, renderer contracts, and pervasive scheduling and commit policies.
- **Constraint burden 5:** Locally plausible changes can violate rendering consistency, update ordering, effects, scheduling fairness, rebasing, compatibility, memory, or performance elsewhere in the path.
- **Placement:** The four scores 3/5/5/5 sum to 18; their arithmetic mean is 4.50 and rounds half-up to Level 5. The published result is Level 5.

**Quality-gate evidence:**

- **Source quality:** Explicit fiber, lane, render-phase, and commit-phase vocabulary makes the selected scheduling state machine inspectable despite its breadth.
- **Architecture:** ReactFiberReconciler, ReactFiberClassUpdateQueue, ReactFiberRootScheduler, ReactFiberWorkLoop, and ReactFiberCommitWork divide update creation, prioritization, rendering, and effects.
- **Naming and idiom:** updateContainer, enqueueUpdate, scheduleUpdateOnFiber, renderRootConcurrent, commitRoot, lanes, fibers, and effects preserve one scheduling vocabulary across files.
- **Tests:** ReactIncrementalUpdates-test.js uses the no-op renderer and scheduler log to cover priority, interruption, rebasing, deferred work, and observable commit order.
- **Documentation:** Inline invariants, source comments, and repository package documentation explain the phase, lane, update, and commit contracts used by the selected reconciler path.
- **Traceability:** An update can be followed from updateContainer into the queue, through lane assignment and root scheduling, across render work, and into commit order asserted by scheduler logs.
- **Maintainability:** Named subsystem boundaries, pervasive invariants, feature gates, and ordering tests constrain changes to the reconciler's shared concurrency rules.
- **Educational value:** For prepared learners, the path exposes a production cooperative renderer as concrete queues, priorities, interruptions, and ordered effects rather than as framework magic.

**Inspection record:** commit `2dc7da790d6388b95b83198ca9b588b2ad5f5c0b`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `packages/react-reconciler/src/ReactFiberWorkLoop.js`, `packages/react-reconciler/src/ReactFiberReconciler.js`, `packages/react-reconciler/src/ReactFiberClassUpdateQueue.js`, `packages/react-reconciler/src/ReactFiberRootScheduler.js`, `packages/react-reconciler/src/ReactFiberCommitWork.js`, `packages/react-reconciler/src/__tests__/ReactIncrementalUpdates-test.js`, `LICENSE`. GitHub Linguist label: JavaScript.

**License:** MIT ([evidence 1](https://github.com/react/react/blob/2dc7da790d6388b95b83198ca9b588b2ad5f5c0b/LICENSE))

_Generated from `catalog/javascript.json`; do not edit by hand._

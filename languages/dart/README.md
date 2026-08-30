# Dart

6 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

[← All languages](../README.md)

## Level 1 — First real code

No qualified learning path has been published at this level. An empty Level 1 means Exempla has not yet found a path gentle enough to publish here; learners are not being told to jump to Level 2.

## Level 2 — Guided real-world code

### [VeryGoodOpenSource/formz](https://github.com/VeryGoodOpenSource/formz)

**Language 3 / Behavior 2 / Design 1 / Constraints 2 → Level 2**

A small Dart model for form values, validation errors, untouched inputs, modified inputs, and submission state.

**Why study it:** See how one file gives form inputs explicit value, interaction, error, and validation state, then combines several inputs into a whole-form answer.

**Short context:**

- A form input can distinguish an untouched value from a modified value and expose a typed validation error.

**Prerequisites:**

- The global novice Dart baseline, including classes, simple generics, enums, null safety, and focused tests.
- A pure input is untouched; a dirty input has been modified. A validator returns null for success or a typed error for failure.

**Concepts this path develops:**

- Modeling a value and its possible validation error with generic types.
- Separating untouched input state from modified input state.
- Combining local validation results into whole-form validity.

**What you can learn:**

- Trace how pure and dirty inputs expose validation and display errors.
- See how an optional mixin caches one validation result.
- Use focused tests to compare valid, invalid, untouched, and modified inputs.

**Learning path:**

- **Goal:** Understand how a small Dart model makes input interaction state, typed validation, cached errors, and aggregate form validity explicit.
- **Start here:** [`lib/formz.dart`](https://github.com/VeryGoodOpenSource/formz/blob/57a4e1e7efb13eb1fea614158ccdd1fc52d4f969/lib/formz.dart) — The sole production file contains the entire model from submission status and typed inputs through cached errors and aggregate FormzMixin queries, with no framework layer to cross.
- **Then read:**
  - [`test/formz_test.dart`](https://github.com/VeryGoodOpenSource/formz/blob/57a4e1e7efb13eb1fea614158ccdd1fc52d4f969/test/formz_test.dart)
  - [`test/helpers/name_input.dart`](https://github.com/VeryGoodOpenSource/formz/blob/57a4e1e7efb13eb1fea614158ccdd1fc52d4f969/test/helpers/name_input.dart)
  - [`README.md`](https://github.com/VeryGoodOpenSource/formz/blob/57a4e1e7efb13eb1fea614158ccdd1fc52d4f969/README.md)
  - [`LICENSE`](https://github.com/VeryGoodOpenSource/formz/blob/57a4e1e7efb13eb1fea614158ccdd1fc52d4f969/LICENSE)
- **Trace:** Begin with FormzInput.pure and dirty, follow value and status through validator, error, displayError, equality, and FormzInputErrorCacheMixin, then aggregate several inputs through Formz and FormzMixin validity and submission predicates and close the behavior in formz_test.dart.

**Why this level:**

- **Language technique 3:** Generics and compositional language abstractions materially shape the model, reaching the substantial-abstraction anchor.
- **Behavioral reasoning 2:** State and caching are meaningful but remain local and deterministic.
- **Design span 1:** The full path stays inside one focused component.
- **Constraint burden 2:** The path carries routine production safeguards and a small stable API rather than interacting strict constraints.
- **Novice accessibility floor 2:** The form-state vocabulary and conventional Dart abstractions form one cohesive professional lesson that can be explained locally and traced in one file.
  - **Central concepts:** typed form values and errors; untouched versus modified input state; local validation and cached results
  - **Incidental concepts:** enum convenience extensions; value equality
- **Placement:** The four structural scores 3/2/1/2 produce rubric Level 2 under the documented formula and guardrails. Novice accessibility floor 2 produces published Level 2.

**License:** MIT ([evidence 1](https://github.com/VeryGoodOpenSource/formz/blob/57a4e1e7efb13eb1fea614158ccdd1fc52d4f969/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Formz is published on pub.dev and its README documents integration with Dart and Flutter form-state architectures.

**Language evidence:** Typed form-input state, validation, error caching, aggregate form status, value semantics, and tests are implemented in one Dart library and its Dart test fixtures.

**Coding relevance:**

That familiar context is subordinate to transferable lessons in generic modeling, immutable state, validation, lazy memoization, aggregate predicates, enum extensions, value semantics, and direct unit tests.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Constructors distinguish untouched and modified values, validation remains user-supplied and typed, and the optional cache changes performance without changing the contract.
- **Architecture:** FormzInput models one field, FormzInputErrorCacheMixin memoizes validation, Formz aggregates fields, and FormzMixin projects those queries onto a form state.
- **Naming and idiom:** pure, dirty, isValid, displayError, validator, inputs, and FormzSubmissionStatus state the domain directly.
- **Tests:** Tests cover validity, error display, pure and dirty state, caching exactly once, equality, hashes, string output, aggregate inputs, and every submission-status predicate.
- **Documentation:** The README and API comments show custom typed inputs, validation, Flutter integration, caching, and form-level composition.
- **Traceability:** An input value can be followed through its validator into error, displayError, aggregate validity, and a focused fixture assertion.
- **Maintainability:** The domain has no hidden state, extensions are additive, the cache is isolated in a mixin, and the complete behavior suite is short enough to audit.
- **Educational value:** It is a strong first example of using a few language abstractions to replace loosely coupled booleans and nullable strings with an explicit domain model.

**Inspection record:** commit `57a4e1e7efb13eb1fea614158ccdd1fc52d4f969`, inspected 2026-08-30. Review passes: Codex primary pass; independent Codex verification pass; Codex novice-accessibility audit. Files inspected: `lib/formz.dart`, `test/formz_test.dart`, `test/helpers/name_input.dart`, `README.md`, `LICENSE`. GitHub Linguist label: Dart.

</details>

## Level 3 — Intermediate

### [dart-lang/sdk](https://github.com/dart-lang/sdk)

**Language 3 / Behavior 4 / Design 2 / Constraints 4 → Level 3**

The Dart language platform: common front end, analyzers and language server, intermediate representation, native and web compilers, virtual machine, JIT and AOT runtimes, garbage collector, core libraries, debugger services, command-line tools, and platform ports.

**Why study it:** Future.wait is a bounded standard-library implementation that combines concurrency, input ordering, error policy, cleanup ownership, malformed protocol handling, and type soundness.

**Short context:**

- Future.wait combines several asynchronous results into one ordered result and defines how errors and successful values are handled.

**Prerequisites:**

- Readers should know Dart Futures, closures, generic lists, errors and stack traces, zones at a high level, and the difference between eager and deferred failure.

**Concepts this path develops:**

- Generic Future<List<T>> construction.
- Concurrent out-of-order completion with ordered output.
- Input ordering, result types, first-error identity, and stack traces must remain exact.

**What you can learn:**

- Trace concurrent Future completions through position capture, shared remaining state, first-error handling, eager or deferred failure, cleanup, and ordered result construction.

**Learning path:**

- **Goal:** Understand how Future.wait preserves input order while coordinating concurrent completions, first-error policy, optional eager failure, and cleanup of successful values.
- **Start here:** [`sdk/lib/async/future.dart`](https://github.com/dart-lang/sdk/blob/967bed205c83cba3ac05b0f8d084d11291e93ff1/sdk/lib/async/future.dart) — The reviewed trace begins in future.dart at Future.wait because the full ordering, error, cleanup, and completion policy is documented and implemented there.
- **Then read:**
  - [`sdk/lib/async/future_impl.dart`](https://github.com/dart-lang/sdk/blob/967bed205c83cba3ac05b0f8d084d11291e93ff1/sdk/lib/async/future_impl.dart)
  - [`tests/lib/async/future_test.dart`](https://github.com/dart-lang/sdk/blob/967bed205c83cba3ac05b0f8d084d11291e93ff1/tests/lib/async/future_test.dart)
  - [`tests/lib/async/futures_test.dart`](https://github.com/dart-lang/sdk/blob/967bed205c83cba3ac05b0f8d084d11291e93ff1/tests/lib/async/futures_test.dart)
  - [`README.md`](https://github.com/dart-lang/sdk/blob/967bed205c83cba3ac05b0f8d084d11291e93ff1/README.md)
  - [`LICENSE`](https://github.com/dart-lang/sdk/blob/967bed205c83cba3ac05b0f8d084d11291e93ff1/LICENSE)
- **Trace:** Start at Future.wait, follow iteration and position capture into shared remaining and values state, then trace successful completions, first-error sentinel transition, eager or deferred failure, cleanup of values received before and after the error through Future.sync, protocol-breach handling, and final typed result construction; close ordering, timing, cleanup, error, stack, zone, and empty-input behavior in the direct suites.

**Why this level:**

- **Language technique 3:** Substantial generic and asynchronous library abstractions materially shape the path without advanced language machinery.
- **Behavioral reasoning 4:** Advanced nonlocal completion, error, cleanup, and timing reasoning recurs across callbacks.
- **Design span 2:** A few clear units contain the complete behavior.
- **Constraint burden 4:** Multiple strict concurrency, cleanup, type, error, compatibility, and performance guarantees recur.
- **Placement:** The four scores 3/4/2/4 sum to 13; their arithmetic mean is 3.25 and rounds half-up to Level 3. The published result is Level 3.

**License:** BSD-3-Clause ([evidence 1](https://github.com/dart-lang/sdk/blob/967bed205c83cba3ac05b0f8d084d11291e93ff1/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** This repository is the upstream source for official Dart SDK releases and the compiler, runtime, libraries, analyzer, and tools used by Dart and Flutter developers.

**Language evidence:** The analyzer, common front end, kernel IR, dart2js, development compiler, WebAssembly compiler, analysis server, package tools, debugger services, and core libraries are Dart, while the first-party VM, garbage collector, JIT, AOT backend, runtime and native platform layers are C++ and related native code.

**Coding relevance:**

The path is entirely transferable asynchronous-library engineering: completion ordering, shared state, eager and deferred error policy, cleanup ownership, error zones, protocol breaches, type soundness, and focused standard-library tests.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Future.wait keeps position capture, completion counting, the first-error sentinel, cleanup of prior and later successes, and malformed Future handling in one documented implementation.
- **Architecture:** The public combinator registers completion callbacks, coordinates shared values and remaining count, delegates underlying completion mechanics to future_impl.dart, and returns one typed Future.
- **Naming and idiom:** Future.wait, remaining, values, eagerError, cleanUp, Future.sync, and completion callbacks state the protocol and use Dart's asynchronous library idioms directly.
- **Tests:** future_test.dart and futures_test.dart cover ordering permutations, timing, empty inputs, one or several errors, eager errors, cleanup values and failures, stack traces, zones, and malformed inputs.
- **Documentation:** The API documentation beside Future.wait defines the selected ordering, error, and cleanup contract; README.md orients the SDK source tree.
- **Traceability:** Each input Future callback can be followed through shared state to ordered success or first-error completion and matched with direct async-library test cases.
- **Maintainability:** The bounded implementation has explicit invariants and exhaustive direct tests, avoiding the unrelated compiler and runtime breadth of the repository.
- **Educational value:** The path shows how a familiar combinator must account for ordering, ownership, errors, and even protocol breaches under concurrency.

**Inspection record:** commit `967bed205c83cba3ac05b0f8d084d11291e93ff1`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `sdk/lib/async/future.dart`, `sdk/lib/async/future_impl.dart`, `tests/lib/async/future_test.dart`, `tests/lib/async/futures_test.dart`, `README.md`, `LICENSE`. GitHub Linguist label: Dart.

</details>

### [dart-lang/shelf](https://github.com/dart-lang/shelf)

**Language 3 / Behavior 3 / Design 3 / Constraints 3 → Level 3**

Dart's composable web-server middleware ecosystem, with immutable requests and responses, streaming bodies, pipelines, routing, static files, proxies, WebSockets, and HTTP compliance checks.

**Why study it:** Shelf Router is a coherent Dart path from declarative route patterns through trie indexing, ordered matching, request updates, middleware, and handler dispatch.

**Short context:**

- An HTTP router associates a method and path pattern with a handler and exposes matched path parameters to the request.

**Prerequisites:**

- Readers should know Dart classes, regular expressions, immutable object updates, FutureOr, middleware functions, and basic HTTP methods, routes, requests, and path parameters.

**Concepts this path develops:**

- Higher-order Handler and Middleware composition.
- Stateful route registration and ordered lookup.
- Method, HEAD, route order, parameter, and trailing-slash semantics must remain stable.

**What you can learn:**

- Trace route registration into a trie, then follow candidate ordering, method and HEAD policy, parameter extraction, mounted paths, middleware, and FutureOr dispatch.

**Learning path:**

- **Goal:** Understand how Shelf Router registers path patterns, narrows ordered candidates through a trie, extracts parameters, updates a request, applies middleware, and dispatches a handler.
- **Start here:** [`pkgs/shelf_router/lib/src/router.dart`](https://github.com/dart-lang/shelf/blob/3dbf65bedad2f1d97c5bae227b68a4ed1551a320/pkgs/shelf_router/lib/src/router.dart) — The reviewed trace begins in shelf_router's router.dart because Router.add parses and registers the patterns later resolved and dispatched by the same subsystem.
- **Then read:**
  - [`pkgs/shelf_router/lib/src/trie.dart`](https://github.com/dart-lang/shelf/blob/3dbf65bedad2f1d97c5bae227b68a4ed1551a320/pkgs/shelf_router/lib/src/trie.dart)
  - [`pkgs/shelf_router/lib/src/router_entry.dart`](https://github.com/dart-lang/shelf/blob/3dbf65bedad2f1d97c5bae227b68a4ed1551a320/pkgs/shelf_router/lib/src/router_entry.dart)
  - [`pkgs/shelf/lib/src/request.dart`](https://github.com/dart-lang/shelf/blob/3dbf65bedad2f1d97c5bae227b68a4ed1551a320/pkgs/shelf/lib/src/request.dart)
  - [`pkgs/shelf_router/test/router_test.dart`](https://github.com/dart-lang/shelf/blob/3dbf65bedad2f1d97c5bae227b68a4ed1551a320/pkgs/shelf_router/test/router_test.dart)
  - [`pkgs/shelf_router/README.md`](https://github.com/dart-lang/shelf/blob/3dbf65bedad2f1d97c5bae227b68a4ed1551a320/pkgs/shelf_router/README.md)
  - [`pkgs/shelf_router/LICENSE`](https://github.com/dart-lang/shelf/blob/3dbf65bedad2f1d97c5bae227b68a4ed1551a320/pkgs/shelf_router/LICENSE)
  - [`LICENSE`](https://github.com/dart-lang/shelf/blob/3dbf65bedad2f1d97c5bae227b68a4ed1551a320/LICENSE)
- **Trace:** Start with Router.add and route-pattern parsing, follow trie insertion and ordered candidate lookup into RouterEntry matching, method and HEAD handling, parameter extraction, request context and path updates, mounted middleware, and synchronous or asynchronous handler dispatch, then close priority, parameters, mounts, trailing-slash, middleware, response, and failure behavior in router_test.dart.

**Why this level:**

- **Language technique 3:** Substantial framework and composition idioms materially shape routing without advanced language machinery.
- **Behavioral reasoning 3:** Several nontrivial behaviors cross the trace, but they remain locally understandable and do not require advanced recovery or concurrency.
- **Design span 3:** Several meaningful package and adapter boundaries contribute to one coherent dispatch path.
- **Constraint burden 3:** Several routing, composition, compatibility, and distribution guarantees influence ordinary changes.
- **Placement:** The four scores 3/3/3/3 sum to 12; their arithmetic mean is 3.00 and rounds half-up to Level 3. The published result is Level 3.

**License:** Apache-2.0 AND BSD-3-Clause ([evidence 1](https://github.com/dart-lang/shelf/blob/3dbf65bedad2f1d97c5bae227b68a4ed1551a320/pkgs/shelf_router/LICENSE), [evidence 2](https://github.com/dart-lang/shelf/blob/3dbf65bedad2f1d97c5bae227b68a4ed1551a320/pkgs/shelf/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The repository publishes the shelf family of packages used to build Dart HTTP servers and middleware, and maintains protocol-compliance reports against its server adapter.

**Language evidence:** HTTP request and response models, body and header handling, middleware composition, I/O adapters, routing tries, static and proxy handlers, WebSocket support, generators, and tests are Dart.

**Coding relevance:**

That short routing vocabulary is subordinate to transferable lessons in trie indexing, ordered matching, regular-expression parameters, immutable request updates, middleware composition, synchronous or asynchronous dispatch, and direct contract testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** router.dart keeps registration and dispatch explicit, while trie.dart and router_entry.dart isolate candidate indexing and pattern matching and Request supplies immutable updates.
- **Architecture:** Router inserts parsed entries into a trie, retrieves ordered candidates, applies method and path policy, updates the Request, composes middleware, and calls a handler.
- **Naming and idiom:** Router, Trie, RouterEntry, Request, mount, parameters, and handler reveal the flow and use Dart's FutureOr and immutable request conventions clearly.
- **Tests:** router_test.dart covers methods, HEAD, candidate order, parameters, mounts, trailing slashes, middleware, synchronous and asynchronous handlers, responses, and failures.
- **Documentation:** The shelf_router README documents registration, parameters, mounts, and middleware for the selected package path.
- **Traceability:** A route added in router.dart can be followed through trie and entry matching into a modified Request and then closed by direct router tests.
- **Maintainability:** Parsing, indexing, entry matching, request state, and dispatch have distinct boundaries, with one focused suite protecting their integration.
- **Educational value:** The path demonstrates practical indexing and dispatch design while remaining small enough to trace end to end.

**Inspection record:** commit `3dbf65bedad2f1d97c5bae227b68a4ed1551a320`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `pkgs/shelf_router/lib/src/router.dart`, `pkgs/shelf_router/lib/src/trie.dart`, `pkgs/shelf_router/lib/src/router_entry.dart`, `pkgs/shelf/lib/src/request.dart`, `pkgs/shelf_router/test/router_test.dart`, `pkgs/shelf_router/README.md`, `pkgs/shelf_router/LICENSE`, `LICENSE`, `pkgs/shelf/LICENSE`. GitHub Linguist label: Dart.

</details>

## Level 4 — Advanced

### [felangel/mocktail](https://github.com/felangel/mocktail)

**Language 4 / Behavior 4 / Design 2 / Constraints 4 → Level 4**

A null-safe Dart mocking library that intercepts invocations at runtime and supports stubbing, argument matching, capture, verification, and asynchronous call observation without code generation.

**Why study it:** Mocktail makes Dart's runtime mocking mechanics inspectable by connecting noSuchMethod interception to matcher reconstruction, fallback values, stubbing, call history, and verification.

**Short context:**

- A mocking library records method invocations, returns configured responses, and later verifies calls made by a test.

**Prerequisites:**

- Readers should know Dart classes, generics, null safety, noSuchMethod, closures, Futures and Streams, and basic stubbing and verification concepts.

**Concepts this path develops:**

- NoSuchMethod and runtime Invocation interception.
- Global stubbing, verification, waiting, and ordinary-call modes.
- Sound null safety and generic return fallback must remain valid.

**What you can learn:**

- Trace an intercepted invocation through recording mode, argument matcher registration, invocation matching, canned responses, call capture, verification, and reset.

**Learning path:**

- **Goal:** Understand how a null-safe Dart mocking library intercepts a call, reconstructs its matchers, selects a stubbed response, records history, and verifies the invocation.
- **Start here:** [`packages/mocktail/lib/src/mocktail.dart`](https://github.com/felangel/mocktail/blob/d6a96e15b9203d33af61083e02e8c40ac07192d6/packages/mocktail/lib/src/mocktail.dart) — The reviewed trace begins in mocktail.dart because Mock.noSuchMethod owns the mode switch between stubbing, verification, until-called observation, and ordinary calls.
- **Then read:**
  - [`packages/mocktail/lib/src/_register_matcher.dart`](https://github.com/felangel/mocktail/blob/d6a96e15b9203d33af61083e02e8c40ac07192d6/packages/mocktail/lib/src/_register_matcher.dart)
  - [`packages/mocktail/lib/src/_invocation_matcher.dart`](https://github.com/felangel/mocktail/blob/d6a96e15b9203d33af61083e02e8c40ac07192d6/packages/mocktail/lib/src/_invocation_matcher.dart)
  - [`packages/mocktail/test/mocktail_test.dart`](https://github.com/felangel/mocktail/blob/d6a96e15b9203d33af61083e02e8c40ac07192d6/packages/mocktail/test/mocktail_test.dart)
  - [`packages/mocktail/README.md`](https://github.com/felangel/mocktail/blob/d6a96e15b9203d33af61083e02e8c40ac07192d6/packages/mocktail/README.md)
  - [`LICENSE`](https://github.com/felangel/mocktail/blob/d6a96e15b9203d33af61083e02e8c40ac07192d6/LICENSE)
- **Trace:** Begin at Mock.noSuchMethod and its recording-mode switch, follow matcher registration and Invocation reconstruction into expectation selection, fallback handling, a canned response or real-call record, capture and verification, then close generic, null-safe, asynchronous, ordering, count, error, and reset behavior in the package self-tests.

**Why this level:**

- **Language technique 4:** Advanced Dart runtime and type-system machinery recurs throughout the central call path.
- **Behavioral reasoning 4:** Several nonlocal modes and histories must remain coherent across calls and asynchronous observation.
- **Design span 2:** A few explicit modules inside one test-library runtime contain the behavior.
- **Constraint burden 4:** Multiple strict type, state, asynchronous, diagnostic, and compatibility guarantees recur across the path.
- **Placement:** The four scores 4/4/2/4 sum to 14; their arithmetic mean is 3.50 and rounds half-up to Level 4. The published result is Level 4.

**License:** MIT ([evidence 1](https://github.com/felangel/mocktail/blob/d6a96e15b9203d33af61083e02e8c40ac07192d6/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Mocktail is released on pub.dev and its README documents use as a test dependency in Dart and Flutter projects.

**Language evidence:** Runtime method interception, stubbing, invocation and argument matching, capture, verification, fallback values, call history, timing, and the test suite are Dart.

**Coding relevance:**

That standard testing vocabulary is subordinate to transferable lessons in runtime interception, generic fallback handling, matcher reconstruction, global recording modes, call history, asynchronous observation, diagnostics, and state reset.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** mocktail.dart keeps interception and recording modes visible, while _register_matcher.dart and _invocation_matcher.dart isolate argument reconstruction and comparison.
- **Architecture:** Runtime interception records an Invocation, matcher helpers reconstruct expectations, a matching stub returns a response, and history supports later verification.
- **Naming and idiom:** Mock, noSuchMethod, registerMatcher, InvocationMatcher, verify, capture, and reset mirror test intent and use Dart's dynamic interception and null-safety mechanisms directly.
- **Tests:** mocktail_test.dart covers methods, accessors, generics, named and positional matchers, captures, fallback values, asynchronous results, errors, counts, order, waiting, and reset.
- **Documentation:** The package README documents the fluent API, fallback registration, and null-safety constraints.
- **Traceability:** A mocked method call can be followed from Mock.noSuchMethod through matcher reconstruction and response selection into verification assertions in the package self-suite.
- **Maintainability:** Matcher registration and comparison are separated from the central mode switch, and broad direct tests protect global recording-state transitions.
- **Educational value:** The path shows the concrete runtime machinery behind a familiar testing API and why null-safe fallback handling is part of correctness.

**Inspection record:** commit `d6a96e15b9203d33af61083e02e8c40ac07192d6`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `packages/mocktail/lib/src/mocktail.dart`, `packages/mocktail/lib/src/_register_matcher.dart`, `packages/mocktail/lib/src/_invocation_matcher.dart`, `packages/mocktail/test/mocktail_test.dart`, `packages/mocktail/README.md`, `LICENSE`. GitHub Linguist label: Dart.

</details>

### [google/json_serializable.dart](https://github.com/google/json_serializable.dart)

**Language 4 / Behavior 3 / Design 3 / Constraints 4 → Level 4**

A source generator and annotation suite that derives typed Dart JSON codecs, validation helpers, field metadata, enums, converters, generics, and JSON Schema from class declarations.

**Why study it:** json_serializable's generic-factory path shows how analyzer metadata becomes generated callback parameters and nested conversion code with checked-in, executable evidence.

**Short context:**

- Generic JSON serialization supplies conversion callbacks for type parameters that cannot be inferred or instantiated directly at runtime.

**Prerequisites:**

- Readers should know Dart generics and annotations, JSON conversion, source generation, analyzer elements at a high level, callbacks, and generated-code tests.

**Concepts this path develops:**

- Analyzer element and annotation inspection.
- Configuration-dependent field and constructor selection.
- Generic callback signatures and nested type arguments must remain type-correct.

**What you can learn:**

- Follow an annotated generic class through configuration and field analysis into generated fromJson and toJson callbacks, nested type arguments, emitted source, and runtime tests.

**Learning path:**

- **Goal:** Understand how json_serializable generates fromJson and toJson callback parameters for a generic annotated class and threads those callbacks through nested fields.
- **Start here:** [`json_serializable/lib/src/generator_helper.dart`](https://github.com/google/json_serializable.dart/blob/9ccf5da684914cc332b60d5e030f9288aa29ac62/json_serializable/lib/src/generator_helper.dart) — The reviewed trace begins in generator_helper.dart because GeneratorHelper validates the annotated class and assembles the generated members that the direction-specific helpers produce.
- **Then read:**
  - [`json_serializable/lib/src/decode_helper.dart`](https://github.com/google/json_serializable.dart/blob/9ccf5da684914cc332b60d5e030f9288aa29ac62/json_serializable/lib/src/decode_helper.dart)
  - [`json_serializable/lib/src/encoder_helper.dart`](https://github.com/google/json_serializable.dart/blob/9ccf5da684914cc332b60d5e030f9288aa29ac62/json_serializable/lib/src/encoder_helper.dart)
  - [`json_serializable/lib/src/type_helper.dart`](https://github.com/google/json_serializable.dart/blob/9ccf5da684914cc332b60d5e030f9288aa29ac62/json_serializable/lib/src/type_helper.dart)
  - [`json_serializable/test/generic_files/generic_argument_factories.dart`](https://github.com/google/json_serializable.dart/blob/9ccf5da684914cc332b60d5e030f9288aa29ac62/json_serializable/test/generic_files/generic_argument_factories.dart)
  - [`json_serializable/test/generic_files/generic_argument_factories.g.dart`](https://github.com/google/json_serializable.dart/blob/9ccf5da684914cc332b60d5e030f9288aa29ac62/json_serializable/test/generic_files/generic_argument_factories.g.dart)
  - [`json_serializable/test/generic_files/generic_test.dart`](https://github.com/google/json_serializable.dart/blob/9ccf5da684914cc332b60d5e030f9288aa29ac62/json_serializable/test/generic_files/generic_test.dart)
  - [`json_serializable/README.md`](https://github.com/google/json_serializable.dart/blob/9ccf5da684914cc332b60d5e030f9288aa29ac62/json_serializable/README.md)
  - [`LICENSE`](https://github.com/google/json_serializable.dart/blob/9ccf5da684914cc332b60d5e030f9288aa29ac62/LICENSE)
- **Trace:** Start with GeneratorHelper reading class configuration and accessible fields, follow genericArgumentFactories into generated fromJson and toJson callback parameters, then trace decode and encode helper selection through nested type arguments and compare emitted source and runtime behavior with the generic fixture, checked-in generated file, and direct test.

**Why this level:**

- **Language technique 4:** Advanced reflection-like analyzer APIs, generics, annotations, and generated code recur throughout the path.
- **Behavioral reasoning 3:** Nontrivial transformation and error behavior spans several stages without advanced nonlocal lifecycle reasoning.
- **Design span 3:** Several meaningful layers cooperate while remaining locally understandable.
- **Constraint burden 4:** Multiple strict type, configuration, generated-output, and compatibility guarantees interact.
- **Placement:** The four scores 4/3/3/4 sum to 14; their arithmetic mean is 3.50 and rounds half-up to Level 4. The published result is Level 4.

**License:** BSD-3-Clause ([evidence 1](https://github.com/google/json_serializable.dart/blob/9ccf5da684914cc332b60d5e030f9288aa29ac62/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The repository publishes json_serializable, json_annotation, and checked_yaml packages used in Dart build_runner workflows and generated model layers.

**Language evidence:** Annotations, analyzer-driven model inspection, serialization and deserialization generation, type-helper dispatch, schema output, checked runtime helpers, YAML support, and tests are Dart.

**Coding relevance:**

That short serialization context is subordinate to transferable lessons in analyzer-driven metadata inspection, generic API design, code generation, staged source construction, configuration, error reporting, and generated-contract testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** GeneratorHelper makes class validation, field selection, ordering, accessibility, constructor handling, and member assembly explicit; decode, encode, and type helpers have separate roles.
- **Architecture:** Analyzer metadata and class configuration feed direction-specific helpers, which thread generic conversion callbacks into emitted fromJson and toJson functions.
- **Naming and idiom:** GeneratorHelper, DecodeHelper, EncoderHelper, TypeHelper, genericArgumentFactories, fromJson, and toJson expose both generator phases and the generated API.
- **Tests:** generic_argument_factories.dart, its checked-in generated file, and generic_test.dart compare callback signatures, nested conversions, emitted source, and runtime behavior.
- **Documentation:** The package README explains genericArgumentFactories and the callback contract used by the selected fixture.
- **Traceability:** The annotated generic fixture can be followed through GeneratorHelper and direction-specific helpers to exact generated text and direct runtime assertions.
- **Maintainability:** Analysis, directional generation, and type dispatch are separated, while golden generated output and runtime tests catch contract drift.
- **Educational value:** The path connects abstract analyzer and code-generation concepts to a small feature whose generated API and behavior are both observable.

**Inspection record:** commit `9ccf5da684914cc332b60d5e030f9288aa29ac62`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `json_serializable/lib/src/generator_helper.dart`, `json_serializable/lib/src/decode_helper.dart`, `json_serializable/lib/src/encoder_helper.dart`, `json_serializable/lib/src/type_helper.dart`, `json_serializable/test/generic_files/generic_argument_factories.dart`, `json_serializable/test/generic_files/generic_argument_factories.g.dart`, `json_serializable/test/generic_files/generic_test.dart`, `json_serializable/README.md`, `LICENSE`. GitHub Linguist label: Dart.

</details>

## Level 5 — Expert

### [dart-lang/build](https://github.com/dart-lang/build)

**Language 4 / Behavior 5 / Design 5 / Constraints 5 → Level 5**

Dart's modular code-generation toolkit and build runner, including incremental planning, dependency tracking, builder execution, and persistent build state.

**Why study it:** Understand how build_runner turns sources and configured builder phases into an incremental execution plan, reuses compatible cached state, invalidates changed dependency paths, runs concurrent build actions, and persists the next build's state. The code-generation vocabulary needs only a short primer; the path teaches transferable graph planning, content-addressed change detection, lifecycle state, concurrency, failure recovery, caching, and adversarial testing.

**Short context:**

- A builder maps primary input assets to declared output assets in ordered phases; build_runner records input and output dependencies so later runs can skip unaffected work and rebuild invalidated paths.

**Prerequisites:**

- Be fluent with Dart futures, streams, generics, collections, exceptions, filesystem I/O, package layouts, hashing, immutable value objects, and asynchronous tests.
- A builder maps primary input assets to declared output assets in ordered phases; build_runner records input and output dependencies so later runs can skip unaffected work and rebuild invalidated paths.

**Concepts this path develops:**

- Asynchronous filesystem and builder execution with futures, zones, and completers.
- Clean, compatible incremental, changed, deleted, missing, retained, invalid, skipped, failed, and successful states.
- Compatible-state and content-digest correctness across repeated builds.

**What you can learn:**

- Study these advanced Dart mechanisms in `build_runner/lib/src/build_plan/build_plan.dart`: asynchronous filesystem inspection, immutable built_value plans, typed AssetId maps and sets, content digests, phase-indexed build steps, and clean-versus-incremental construction.
- Trace source creation, update, deletion, generated-output modification, lazy build demand, transitive invalidation, builder failure, resource disposal, and successful-state persistence through BuildPlan, BuildStepPlan, Build, BuildState, AssetContent, and InputTracker.
- Identify these architectural responsibilities: configuration and phase planning, source and declared-output indexing, previous-build compatibility, mutable execution state, builder-facing filesystem access, dependency tracking, resolver reuse, and direct unit, integration, and randomized stress verification.
- Study these change constraints: only compatible cached state may be reused; content digests rather than timestamps determine changes; deleted inputs invalidate transitive declared outputs; externally modified outputs obey the chosen strategy; phases serialize while actions within a phase may run concurrently; resources close after all work; and failures must not publish invalid success state.

**Learning path:**

- **Goal:** Understand how build_runner plans and executes a compatible incremental build while preserving dependency, output, concurrency, failure, and resource-lifecycle guarantees.
- **Start here:** [`build_runner/lib/src/build_plan/build_plan.dart`](https://github.com/dart-lang/build/blob/c25d2e1e41e463bcdd9282146c0cd4c9dfadc909/build_runner/lib/src/build_plan/build_plan.dart) — Begin with BuildPlan.load because it finds present and previous assets, chooses clean or compatible incremental planning, compares persisted digests, classifies source and output changes, and computes the BuildStepPlan consumed by execution.
- **Then read:**
  - [`build_runner/lib/src/build_plan/build_step_plan.dart`](https://github.com/dart-lang/build/blob/c25d2e1e41e463bcdd9282146c0cd4c9dfadc909/build_runner/lib/src/build_plan/build_step_plan.dart)
  - [`build_runner/lib/src/build_plan/previous_build.dart`](https://github.com/dart-lang/build/blob/c25d2e1e41e463bcdd9282146c0cd4c9dfadc909/build_runner/lib/src/build_plan/previous_build.dart)
  - [`build_runner/lib/src/build/build.dart`](https://github.com/dart-lang/build/blob/c25d2e1e41e463bcdd9282146c0cd4c9dfadc909/build_runner/lib/src/build/build.dart)
  - [`build_runner/lib/src/build/asset_content.dart`](https://github.com/dart-lang/build/blob/c25d2e1e41e463bcdd9282146c0cd4c9dfadc909/build_runner/lib/src/build/asset_content.dart)
  - [`build_runner/lib/src/build/build_state/build_state.dart`](https://github.com/dart-lang/build/blob/c25d2e1e41e463bcdd9282146c0cd4c9dfadc909/build_runner/lib/src/build/build_state/build_state.dart)
  - [`build_runner/lib/src/build/input_tracker.dart`](https://github.com/dart-lang/build/blob/c25d2e1e41e463bcdd9282146c0cd4c9dfadc909/build_runner/lib/src/build/input_tracker.dart)
  - [`build_runner/test/build/build_test.dart`](https://github.com/dart-lang/build/blob/c25d2e1e41e463bcdd9282146c0cd4c9dfadc909/build_runner/test/build/build_test.dart)
  - [`build_runner/test/build/build_state/build_state_test.dart`](https://github.com/dart-lang/build/blob/c25d2e1e41e463bcdd9282146c0cd4c9dfadc909/build_runner/test/build/build_state/build_state_test.dart)
  - [`build_runner/test/invalidation/asset_input_invalidation_test.dart`](https://github.com/dart-lang/build/blob/c25d2e1e41e463bcdd9282146c0cd4c9dfadc909/build_runner/test/invalidation/asset_input_invalidation_test.dart)
  - [`build_runner/test/invalidation/invalidation_stress_test.dart`](https://github.com/dart-lang/build/blob/c25d2e1e41e463bcdd9282146c0cd4c9dfadc909/build_runner/test/invalidation/invalidation_stress_test.dart)
  - [`build_runner/test/integration_tests/build_command_invalidation_test.dart`](https://github.com/dart-lang/build/blob/c25d2e1e41e463bcdd9282146c0cd4c9dfadc909/build_runner/test/integration_tests/build_command_invalidation_test.dart)
  - [`build_runner/test/build/deferred_writes_test.dart`](https://github.com/dart-lang/build/blob/c25d2e1e41e463bcdd9282146c0cd4c9dfadc909/build_runner/test/build/deferred_writes_test.dart)
  - [`build_runner/README.md`](https://github.com/dart-lang/build/blob/c25d2e1e41e463bcdd9282146c0cd4c9dfadc909/build_runner/README.md)
  - [`LICENSE`](https://github.com/dart-lang/build/blob/c25d2e1e41e463bcdd9282146c0cd4c9dfadc909/LICENSE)
- **Trace:** Start with BuildPlan loading previous state and discovering current sources and cache files; follow clean or incremental classification through digest comparison, output strategy, source additions and deletions, transitive declared-output invalidation, and BuildStepPlan recomputation; then follow Build through phase scheduling, lazy work, builder-facing reads and writes, dependency recording, failure handling, resource disposal, resolver reset, and finished-state persistence; close with direct no-change, changed-input, deleted-input, generated-input, external-output, concurrent-phase, failure, deferred-write, transitive-graph, command, and randomized invalidation tests.

**Why this level:**

- **Language technique 4:** Advanced asynchronous, generic, immutable-state, collection, hashing, and error-handling techniques recur throughout the selected path.
- **Behavioral reasoning 5:** Several coupled graph, filesystem, cache, execution, failure, and lifecycle state machines interact nonlocally across successive builds.
- **Design span 5:** The learning trace crosses many substantial planning, I/O, graph, execution, lifecycle, persistence, and verification boundaries while remaining inside build_runner's incremental core.
- **Constraint burden 5:** Interacting graph, cache, filesystem, concurrency, failure, lifecycle, performance, and compatibility guarantees constrain every stage of the path.
- **Placement:** The four scores 4/5/5/5 sum to 19; their arithmetic mean is 4.75 and rounds half-up to Level 5, with three dimensions scored 5. The published result is Level 5.

**License:** BSD-3-Clause ([evidence 1](https://github.com/dart-lang/build/blob/c25d2e1e41e463bcdd9282146c0cd4c9dfadc909/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The Dart team publishes build_runner on pub.dev as the standard command-line entry point used by Dart and Flutter code generators such as json_serializable, built_value, Mockito, and Freezed.

**Language evidence:** The selected build planning, incremental state, dependency invalidation, execution, resource lifecycle, and direct unit, integration, and stress suites are handwritten first-party Dart under build_runner.

**Coding relevance:**

The code-generation vocabulary needs only a short primer; the path teaches transferable graph planning, content-addressed change detection, lifecycle state, concurrency, failure recovery, caching, and adversarial testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** BuildPlan, BuildStepPlan, Build, BuildState, AssetContent, and InputTracker state their roles and keep change classification, planning, execution, content, and dependency operations in focused types and methods.
- **Architecture:** BuildPlan combines configuration, previous state, and filesystem observations into a BuildStepPlan and BuildInputs; Build executes that plan through a builder filesystem while BuildState records contents and results for the next run.
- **Naming and idiom:** BuildPlan, PreviousBuild, BuildInputs, BuildStepPlan, BuildState, AssetContent, InputTracker, invalidOutputs, retainedOutputContents, and transitiveDeclaredOutputsOf expose the model in idiomatic Dart.
- **Tests:** The selected suites exercise phase concurrency, lazy actions, generated and hidden inputs, cached reads, unchanged and changed builds, deletion cleanup, output modification, transitive invalidation graphs, deferred writes, command behavior, regression cases, and randomized stress sequences.
- **Documentation:** build_runner/README.md documents builders, phases from a user perspective, build and watch operation, output and internal files, workspace behavior, and configuration; source comments document the selected planner and state contracts.
- **Traceability:** A discovered asset can be followed through digest comparison and change classification into a planned build step, builder execution and dependency reads, recorded output content, direct assertions, and serialized follow-on state.
- **Maintainability:** Planning and execution are separated, compatibility and change rules are centralized, generated value support is distinct from handwritten logic, and layered deterministic plus stress tests protect the dangerous incremental boundaries.
- **Educational value:** The path exposes the real machinery behind an everyday Dart command and ties advanced graph, cache, asynchronous, resource, and failure concepts to observable rebuild decisions.

**Inspection record:** commit `c25d2e1e41e463bcdd9282146c0cd4c9dfadc909`, inspected 2026-08-29. Review passes: Codex primary pass; Codex cold verification pass. Files inspected: `build_runner/lib/src/build_plan/build_plan.dart`, `build_runner/lib/src/build_plan/build_step_plan.dart`, `build_runner/lib/src/build_plan/previous_build.dart`, `build_runner/lib/src/build/build.dart`, `build_runner/lib/src/build/asset_content.dart`, `build_runner/lib/src/build/build_state/build_state.dart`, `build_runner/lib/src/build/input_tracker.dart`, `build_runner/test/build/build_test.dart`, `build_runner/test/build/build_state/build_state_test.dart`, `build_runner/test/invalidation/asset_input_invalidation_test.dart`, `build_runner/test/invalidation/invalidation_stress_test.dart`, `build_runner/test/integration_tests/build_command_invalidation_test.dart`, `build_runner/test/build/deferred_writes_test.dart`, `build_runner/README.md`, `LICENSE`. GitHub Linguist label: Dart.

</details>

_Generated from `catalog/dart.json`; do not edit by hand._

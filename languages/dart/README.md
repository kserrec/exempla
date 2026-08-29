# Dart

6 qualified repositories. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

[← All languages](../README.md)

## Level 1

No qualified repository has been published at this level. Standards are not lowered to fill a slot.

## Level 2

### [felangel/equatable](https://github.com/felangel/equatable)

**Language 2 / Behavior 2 / Design 1 / Constraints 3 → Level 2**

A compact Dart package that gives immutable objects value equality and stable hashing from an explicit list of properties.

**Real-world evidence:** Equatable is distributed as a versioned pub.dev package and its README documents use in ordinary Dart and Flutter domain models.

**Language evidence:** Value equality, recursive collection comparison, hashing, stringification, configuration, and the behavior tests are implemented in Dart under lib and test.

**Why study it:** Its tiny public contract exposes the complete mechanics behind value objects: runtime-type checks, property traversal, nested collection equality, hash combination, and diagnostic string output.

**What you can learn:**

- Dart equality and hashCode contracts, immutable value objects, recursive iterable, map, and set comparison, mixins, global and local configuration, stringification, and focused unit tests.

**Prerequisites:**

- Dart classes, getters, operator overloading, generics, iterables, maps and sets, null safety, and basic unit testing.

**Coding relevance:**

That short vocabulary is subordinate to transferable lessons in operator contracts, immutable data, recursive collection comparison, hashing, runtime-type checks, configuration, and focused unit testing.

Required domain context:

- A value object defines equality and hashing from the properties that constitute its value.

**Learning path:**

- **Goal:** Understand how a Dart value object derives consistent equality, hashing, and diagnostic output from an explicit property list.
- **Start here:** [`lib/src/equatable.dart`](https://github.com/felangel/equatable/blob/f98a58960545ba72b51d0eacf746af393a0c6b24/lib/src/equatable.dart) — The base class shows the whole user contract—props, equality, hashing, and stringification—while equatable_utils.dart supplies the recursive comparison and hash mechanics beneath it.
- **Then read:**
  - [`lib/src/equatable_utils.dart`](https://github.com/felangel/equatable/blob/f98a58960545ba72b51d0eacf746af393a0c6b24/lib/src/equatable_utils.dart)
  - [`test/equatable_test.dart`](https://github.com/felangel/equatable/blob/f98a58960545ba72b51d0eacf746af393a0c6b24/test/equatable_test.dart)
  - [`test/equatable_utils_test.dart`](https://github.com/felangel/equatable/blob/f98a58960545ba72b51d0eacf746af393a0c6b24/test/equatable_utils_test.dart)
  - [`README.md`](https://github.com/felangel/equatable/blob/f98a58960545ba72b51d0eacf746af393a0c6b24/README.md)
  - [`LICENSE`](https://github.com/felangel/equatable/blob/f98a58960545ba72b51d0eacf746af393a0c6b24/LICENSE)
- **Trace:** Start with Equatable.props, operator ==, hashCode, and stringify; follow the shared utilities through runtime-type checks, recursive iterable, map, and set comparison, order-sensitive and order-insensitive behavior, hash combination, and diagnostics; then close each contract in the two direct unit suites.

**Why this level:**

- **Language technique 2:** Common professional Dart idioms shape the path without advanced type or runtime machinery.
- **Behavioral reasoning 2:** Meaningful branching and recursion remain synchronous, stateless, and easy to trace.
- **Design span 1:** One focused component contains the complete behavior.
- **Constraint burden 3:** Several material semantic and compatibility guarantees constrain otherwise local code.
- **Placement:** The four scores 2/2/1/3 sum to 8; their arithmetic mean is 2.00 and rounds half-up to Level 2. The published result is Level 2.

**Quality-gate evidence:**

- **Source quality:** The implementation is small, null-safe, explicit about runtime type, and keeps equality and hashing over the same props representation.
- **Architecture:** Equatable and EquatableMixin define the public contract; EquatableConfig controls default display behavior; utilities own recursive equality and hash combination.
- **Naming and idiom:** props, stringify, equals, iterableEquals, mapEquals, setEquals, and mapPropsToHashCode make the value-object model discoverable.
- **Tests:** Unit suites cover identity, runtime types, nulls, nested iterables, sets, maps, numbers, hashes, mixins, configuration, string output, and regressions.
- **Documentation:** The README explains installation, props, nullable properties, mixins, stringification, immutability, and common usage patterns.
- **Traceability:** A model's props can be followed directly through operator== or hashCode into one utility branch and an exact assertion.
- **Maintainability:** The public surface is narrow, shared mechanics are centralized, and edge cases are represented in small targeted tests.
- **Educational value:** It turns a language feature often treated as boilerplate into a complete, approachable study of behavioral contracts.

**Inspection record:** commit `f98a58960545ba72b51d0eacf746af393a0c6b24`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `lib/src/equatable.dart`, `lib/src/equatable_utils.dart`, `test/equatable_test.dart`, `test/equatable_utils_test.dart`, `README.md`, `LICENSE`. GitHub Linguist label: Dart.

**License:** MIT ([evidence 1](https://github.com/felangel/equatable/blob/f98a58960545ba72b51d0eacf746af393a0c6b24/LICENSE))

### [VeryGoodOpenSource/formz](https://github.com/VeryGoodOpenSource/formz)

**Language 3 / Behavior 2 / Design 1 / Constraints 2 → Level 2**

A minimal typed model for pure and modified form inputs, validation errors, aggregate validity, and submission state.

**Real-world evidence:** Formz is published on pub.dev and its README documents integration with Dart and Flutter form-state architectures.

**Language evidence:** Typed form-input state, validation, error caching, aggregate form status, value semantics, and tests are implemented in one Dart library and its Dart test fixtures.

**Why study it:** One file demonstrates how a tiny generic domain model can make input value, interaction state, validation error, display policy, caching, equality, and whole-form queries explicit.

**What you can learn:**

- Generic abstract classes, sealed state through constructors, typed validation errors, pure versus dirty input state, lazy caching with mixins, aggregate predicates, enum extensions, immutability, equality, and unit tests.

**Prerequisites:**

- Dart generics, abstract classes, mixins, enums and extensions, null safety, immutable objects, and basic form validation.

**Coding relevance:**

That familiar context is subordinate to transferable lessons in generic modeling, immutable state, validation, lazy memoization, aggregate predicates, enum extensions, value semantics, and direct unit tests.

Required domain context:

- A form input can distinguish an untouched value from a modified value and expose a typed validation error.

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
- **Placement:** The four scores 3/2/1/2 sum to 8; their arithmetic mean is 2.00 and rounds half-up to Level 2. The published result is Level 2.

**Quality-gate evidence:**

- **Source quality:** Constructors distinguish untouched and modified values, validation remains user-supplied and typed, and the optional cache changes performance without changing the contract.
- **Architecture:** FormzInput models one field, FormzInputErrorCacheMixin memoizes validation, Formz aggregates fields, and FormzMixin projects those queries onto a form state.
- **Naming and idiom:** pure, dirty, isValid, displayError, validator, inputs, and FormzSubmissionStatus state the domain directly.
- **Tests:** Tests cover validity, error display, pure and dirty state, caching exactly once, equality, hashes, string output, aggregate inputs, and every submission-status predicate.
- **Documentation:** The README and API comments show custom typed inputs, validation, Flutter integration, caching, and form-level composition.
- **Traceability:** An input value can be followed through its validator into error, displayError, aggregate validity, and a focused fixture assertion.
- **Maintainability:** The domain has no hidden state, extensions are additive, the cache is isolated in a mixin, and the complete behavior suite is short enough to audit.
- **Educational value:** It is a strong first example of using a few language abstractions to replace loosely coupled booleans and nullable strings with an explicit domain model.

**Inspection record:** commit `57a4e1e7efb13eb1fea614158ccdd1fc52d4f969`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `lib/formz.dart`, `test/formz_test.dart`, `test/helpers/name_input.dart`, `README.md`, `LICENSE`. GitHub Linguist label: Dart.

**License:** MIT ([evidence 1](https://github.com/VeryGoodOpenSource/formz/blob/57a4e1e7efb13eb1fea614158ccdd1fc52d4f969/LICENSE))

## Level 3

### [dart-lang/sdk](https://github.com/dart-lang/sdk)

**Language 3 / Behavior 4 / Design 2 / Constraints 4 → Level 3**

The Dart language platform: common front end, analyzers and language server, intermediate representation, native and web compilers, virtual machine, JIT and AOT runtimes, garbage collector, core libraries, debugger services, command-line tools, and platform ports.

**Real-world evidence:** This repository is the upstream source for official Dart SDK releases and the compiler, runtime, libraries, analyzer, and tools used by Dart and Flutter developers.

**Language evidence:** The analyzer, common front end, kernel IR, dart2js, development compiler, WebAssembly compiler, analysis server, package tools, debugger services, and core libraries are Dart, while the first-party VM, garbage collector, JIT, AOT backend, runtime and native platform layers are C++ and related native code.

**Why study it:** Future.wait is a bounded standard-library implementation that combines concurrency, input ordering, error policy, cleanup ownership, malformed protocol handling, and type soundness.

**What you can learn:**

- Trace concurrent Future completions through position capture, shared remaining state, first-error handling, eager or deferred failure, cleanup, and ordered result construction.

**Prerequisites:**

- Readers should know Dart Futures, closures, generic lists, errors and stack traces, zones at a high level, and the difference between eager and deferred failure.

**Coding relevance:**

The path is entirely transferable asynchronous-library engineering: completion ordering, shared state, eager and deferred error policy, cleanup ownership, error zones, protocol breaches, type soundness, and focused standard-library tests.

Required domain context:

- Future.wait combines several asynchronous results into one ordered result and defines how errors and successful values are handled.

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

**Quality-gate evidence:**

- **Source quality:** Future.wait keeps position capture, completion counting, the first-error sentinel, cleanup of prior and later successes, and malformed Future handling in one documented implementation.
- **Architecture:** The public combinator registers completion callbacks, coordinates shared values and remaining count, delegates underlying completion mechanics to future_impl.dart, and returns one typed Future.
- **Naming and idiom:** Future.wait, remaining, values, eagerError, cleanUp, Future.sync, and completion callbacks state the protocol and use Dart's asynchronous library idioms directly.
- **Tests:** future_test.dart and futures_test.dart cover ordering permutations, timing, empty inputs, one or several errors, eager errors, cleanup values and failures, stack traces, zones, and malformed inputs.
- **Documentation:** The API documentation beside Future.wait defines the selected ordering, error, and cleanup contract; README.md orients the SDK source tree.
- **Traceability:** Each input Future callback can be followed through shared state to ordered success or first-error completion and matched with direct async-library test cases.
- **Maintainability:** The bounded implementation has explicit invariants and exhaustive direct tests, avoiding the unrelated compiler and runtime breadth of the repository.
- **Educational value:** The path shows how a familiar combinator must account for ordering, ownership, errors, and even protocol breaches under concurrency.

**Inspection record:** commit `967bed205c83cba3ac05b0f8d084d11291e93ff1`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `sdk/lib/async/future.dart`, `sdk/lib/async/future_impl.dart`, `tests/lib/async/future_test.dart`, `tests/lib/async/futures_test.dart`, `README.md`, `LICENSE`. GitHub Linguist label: Dart.

**License:** BSD-3-Clause ([evidence 1](https://github.com/dart-lang/sdk/blob/967bed205c83cba3ac05b0f8d084d11291e93ff1/LICENSE))

### [dart-lang/shelf](https://github.com/dart-lang/shelf)

**Language 3 / Behavior 3 / Design 3 / Constraints 3 → Level 3**

Dart's composable web-server middleware ecosystem, with immutable requests and responses, streaming bodies, pipelines, routing, static files, proxies, WebSockets, and HTTP compliance checks.

**Real-world evidence:** The repository publishes the shelf family of packages used to build Dart HTTP servers and middleware, and maintains protocol-compliance reports against its server adapter.

**Language evidence:** HTTP request and response models, body and header handling, middleware composition, I/O adapters, routing tries, static and proxy handlers, WebSocket support, generators, and tests are Dart.

**Why study it:** Shelf Router is a coherent Dart path from declarative route patterns through trie indexing, ordered matching, request updates, middleware, and handler dispatch.

**What you can learn:**

- Trace route registration into a trie, then follow candidate ordering, method and HEAD policy, parameter extraction, mounted paths, middleware, and FutureOr dispatch.

**Prerequisites:**

- Readers should know Dart classes, regular expressions, immutable object updates, FutureOr, middleware functions, and basic HTTP methods, routes, requests, and path parameters.

**Coding relevance:**

That short routing vocabulary is subordinate to transferable lessons in trie indexing, ordered matching, regular-expression parameters, immutable request updates, middleware composition, synchronous or asynchronous dispatch, and direct contract testing.

Required domain context:

- An HTTP router associates a method and path pattern with a handler and exposes matched path parameters to the request.

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

**Quality-gate evidence:**

- **Source quality:** router.dart keeps registration and dispatch explicit, while trie.dart and router_entry.dart isolate candidate indexing and pattern matching and Request supplies immutable updates.
- **Architecture:** Router inserts parsed entries into a trie, retrieves ordered candidates, applies method and path policy, updates the Request, composes middleware, and calls a handler.
- **Naming and idiom:** Router, Trie, RouterEntry, Request, mount, parameters, and handler reveal the flow and use Dart's FutureOr and immutable request conventions clearly.
- **Tests:** router_test.dart covers methods, HEAD, candidate order, parameters, mounts, trailing slashes, middleware, synchronous and asynchronous handlers, responses, and failures.
- **Documentation:** The shelf_router README documents registration, parameters, mounts, and middleware for the selected package path.
- **Traceability:** A route added in router.dart can be followed through trie and entry matching into a modified Request and then closed by direct router tests.
- **Maintainability:** Parsing, indexing, entry matching, request state, and dispatch have distinct boundaries, with one focused suite protecting their integration.
- **Educational value:** The path demonstrates practical indexing and dispatch design while remaining small enough to trace end to end.

**Inspection record:** commit `3dbf65bedad2f1d97c5bae227b68a4ed1551a320`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `pkgs/shelf_router/lib/src/router.dart`, `pkgs/shelf_router/lib/src/trie.dart`, `pkgs/shelf_router/lib/src/router_entry.dart`, `pkgs/shelf/lib/src/request.dart`, `pkgs/shelf_router/test/router_test.dart`, `pkgs/shelf_router/README.md`, `pkgs/shelf_router/LICENSE`, `LICENSE`, `pkgs/shelf/LICENSE`. GitHub Linguist label: Dart.

**License:** Apache-2.0 AND BSD-3-Clause ([evidence 1](https://github.com/dart-lang/shelf/blob/3dbf65bedad2f1d97c5bae227b68a4ed1551a320/pkgs/shelf_router/LICENSE), [evidence 2](https://github.com/dart-lang/shelf/blob/3dbf65bedad2f1d97c5bae227b68a4ed1551a320/pkgs/shelf/LICENSE))

## Level 4

### [felangel/mocktail](https://github.com/felangel/mocktail)

**Language 4 / Behavior 4 / Design 2 / Constraints 4 → Level 4**

A null-safe Dart mocking library that intercepts invocations at runtime and supports stubbing, argument matching, capture, verification, and asynchronous call observation without code generation.

**Real-world evidence:** Mocktail is released on pub.dev and its README documents use as a test dependency in Dart and Flutter projects.

**Language evidence:** Runtime method interception, stubbing, invocation and argument matching, capture, verification, fallback values, call history, timing, and the test suite are Dart.

**Why study it:** Mocktail makes Dart's runtime mocking mechanics inspectable by connecting noSuchMethod interception to matcher reconstruction, fallback values, stubbing, call history, and verification.

**What you can learn:**

- Trace an intercepted invocation through recording mode, argument matcher registration, invocation matching, canned responses, call capture, verification, and reset.

**Prerequisites:**

- Readers should know Dart classes, generics, null safety, noSuchMethod, closures, Futures and Streams, and basic stubbing and verification concepts.

**Coding relevance:**

That standard testing vocabulary is subordinate to transferable lessons in runtime interception, generic fallback handling, matcher reconstruction, global recording modes, call history, asynchronous observation, diagnostics, and state reset.

Required domain context:

- A mocking library records method invocations, returns configured responses, and later verifies calls made by a test.

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

**Quality-gate evidence:**

- **Source quality:** mocktail.dart keeps interception and recording modes visible, while _register_matcher.dart and _invocation_matcher.dart isolate argument reconstruction and comparison.
- **Architecture:** Runtime interception records an Invocation, matcher helpers reconstruct expectations, a matching stub returns a response, and history supports later verification.
- **Naming and idiom:** Mock, noSuchMethod, registerMatcher, InvocationMatcher, verify, capture, and reset mirror test intent and use Dart's dynamic interception and null-safety mechanisms directly.
- **Tests:** mocktail_test.dart covers methods, accessors, generics, named and positional matchers, captures, fallback values, asynchronous results, errors, counts, order, waiting, and reset.
- **Documentation:** The package README documents the fluent API, fallback registration, and null-safety constraints.
- **Traceability:** A mocked method call can be followed from Mock.noSuchMethod through matcher reconstruction and response selection into verification assertions in the package self-suite.
- **Maintainability:** Matcher registration and comparison are separated from the central mode switch, and broad direct tests protect global recording-state transitions.
- **Educational value:** The path shows the concrete runtime machinery behind a familiar testing API and why null-safe fallback handling is part of correctness.

**Inspection record:** commit `d6a96e15b9203d33af61083e02e8c40ac07192d6`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `packages/mocktail/lib/src/mocktail.dart`, `packages/mocktail/lib/src/_register_matcher.dart`, `packages/mocktail/lib/src/_invocation_matcher.dart`, `packages/mocktail/test/mocktail_test.dart`, `packages/mocktail/README.md`, `LICENSE`. GitHub Linguist label: Dart.

**License:** MIT ([evidence 1](https://github.com/felangel/mocktail/blob/d6a96e15b9203d33af61083e02e8c40ac07192d6/LICENSE))

### [google/json_serializable.dart](https://github.com/google/json_serializable.dart)

**Language 4 / Behavior 3 / Design 3 / Constraints 4 → Level 4**

A source generator and annotation suite that derives typed Dart JSON codecs, validation helpers, field metadata, enums, converters, generics, and JSON Schema from class declarations.

**Real-world evidence:** The repository publishes json_serializable, json_annotation, and checked_yaml packages used in Dart build_runner workflows and generated model layers.

**Language evidence:** Annotations, analyzer-driven model inspection, serialization and deserialization generation, type-helper dispatch, schema output, checked runtime helpers, YAML support, and tests are Dart.

**Why study it:** json_serializable's generic-factory path shows how analyzer metadata becomes generated callback parameters and nested conversion code with checked-in, executable evidence.

**What you can learn:**

- Follow an annotated generic class through configuration and field analysis into generated fromJson and toJson callbacks, nested type arguments, emitted source, and runtime tests.

**Prerequisites:**

- Readers should know Dart generics and annotations, JSON conversion, source generation, analyzer elements at a high level, callbacks, and generated-code tests.

**Coding relevance:**

That short serialization context is subordinate to transferable lessons in analyzer-driven metadata inspection, generic API design, code generation, staged source construction, configuration, error reporting, and generated-contract testing.

Required domain context:

- Generic JSON serialization supplies conversion callbacks for type parameters that cannot be inferred or instantiated directly at runtime.

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

**Quality-gate evidence:**

- **Source quality:** GeneratorHelper makes class validation, field selection, ordering, accessibility, constructor handling, and member assembly explicit; decode, encode, and type helpers have separate roles.
- **Architecture:** Analyzer metadata and class configuration feed direction-specific helpers, which thread generic conversion callbacks into emitted fromJson and toJson functions.
- **Naming and idiom:** GeneratorHelper, DecodeHelper, EncoderHelper, TypeHelper, genericArgumentFactories, fromJson, and toJson expose both generator phases and the generated API.
- **Tests:** generic_argument_factories.dart, its checked-in generated file, and generic_test.dart compare callback signatures, nested conversions, emitted source, and runtime behavior.
- **Documentation:** The package README explains genericArgumentFactories and the callback contract used by the selected fixture.
- **Traceability:** The annotated generic fixture can be followed through GeneratorHelper and direction-specific helpers to exact generated text and direct runtime assertions.
- **Maintainability:** Analysis, directional generation, and type dispatch are separated, while golden generated output and runtime tests catch contract drift.
- **Educational value:** The path connects abstract analyzer and code-generation concepts to a small feature whose generated API and behavior are both observable.

**Inspection record:** commit `9ccf5da684914cc332b60d5e030f9288aa29ac62`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `json_serializable/lib/src/generator_helper.dart`, `json_serializable/lib/src/decode_helper.dart`, `json_serializable/lib/src/encoder_helper.dart`, `json_serializable/lib/src/type_helper.dart`, `json_serializable/test/generic_files/generic_argument_factories.dart`, `json_serializable/test/generic_files/generic_argument_factories.g.dart`, `json_serializable/test/generic_files/generic_test.dart`, `json_serializable/README.md`, `LICENSE`. GitHub Linguist label: Dart.

**License:** BSD-3-Clause ([evidence 1](https://github.com/google/json_serializable.dart/blob/9ccf5da684914cc332b60d5e030f9288aa29ac62/LICENSE))

## Level 5

No qualified repository has been published at this level. Standards are not lowered to fill a slot.

_Generated from `catalog/dart.json`; do not edit by hand._

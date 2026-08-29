# Dart

10 qualified repositories. Scores assume the learner described in [the SDC rubric](../../docs/sdc.md).

[← All languages](../README.md)

## SDC 1

### [felangel/equatable](https://github.com/felangel/equatable)

**S1 / D2 / C1 → SDC 1**

A compact Dart package that gives immutable objects value equality and stable hashing from an explicit list of properties.

**Real-world evidence:** Equatable is distributed as a versioned pub.dev package and its README documents use in ordinary Dart and Flutter domain models.

**Language evidence:** Value equality, recursive collection comparison, hashing, stringification, configuration, and the behavior tests are implemented in Dart under lib and test.

**Why study it:** Its tiny public contract exposes the complete mechanics behind value objects: runtime-type checks, property traversal, nested collection equality, hash combination, and diagnostic string output.

**What you can learn:**

- Dart equality and hashCode contracts, immutable value objects, recursive iterable, map, and set comparison, mixins, global and local configuration, stringification, and focused unit tests.

**Prerequisites:**

- Dart classes, getters, operator overloading, generics, iterables, maps and sets, null safety, and basic unit testing.

**Start here:** [`lib/src/equatable.dart`](https://github.com/felangel/equatable/blob/f98a58960545ba72b51d0eacf746af393a0c6b24/lib/src/equatable.dart) — The base class shows the whole user contract—props, equality, hashing, and stringification—while equatable_utils.dart supplies the recursive comparison and hash mechanics beneath it.

**Why this level:**

- **S1:** 165 meaningful implementation LOC measured with tokei 14.0.0. Count covers all production Dart under lib and excludes tests, examples, benchmarks, documentation, and package metadata.
- **D2:** Correct equality has subtle contracts and nested-container cases, but the implementation uses direct, bounded algorithms and familiar Dart types.
- **C1:** The package has one cohesive responsibility and a short call path from props to comparison, hashing, or display.
- **Placement:** S1/D2/C1 averages to 1.33, making Equatable an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** The implementation is small, null-safe, explicit about runtime type, and keeps equality and hashing over the same props representation.
- **Architecture:** Equatable and EquatableMixin define the public contract; EquatableConfig controls default display behavior; utilities own recursive equality and hash combination.
- **Naming and idiom:** props, stringify, equals, iterableEquals, mapEquals, setEquals, and mapPropsToHashCode make the value-object model discoverable.
- **Tests:** Unit suites cover identity, runtime types, nulls, nested iterables, sets, maps, numbers, hashes, mixins, configuration, string output, and regressions.
- **Documentation:** The README explains installation, props, nullable properties, mixins, stringification, immutability, and common usage patterns.
- **Traceability:** A model's props can be followed directly through operator== or hashCode into one utility branch and an exact assertion.
- **Maintainability:** The public surface is narrow, shared mechanics are centralized, and edge cases are represented in small targeted tests.
- **Educational value:** It turns a language feature often treated as boilerplate into a complete, approachable study of behavioral contracts.

**Inspection record:** commit `f98a58960545ba72b51d0eacf746af393a0c6b24`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `lib/src/equatable.dart`, `lib/src/equatable_utils.dart`, `test/equatable_test.dart`, `test/equatable_utils_test.dart`, `LICENSE`. GitHub Linguist label: Dart. LOC exclusions: test/, example/, benchmarks, documentation and package metadata.

**License:** [MIT](https://github.com/felangel/equatable/blob/f98a58960545ba72b51d0eacf746af393a0c6b24/LICENSE)

### [VeryGoodOpenSource/formz](https://github.com/VeryGoodOpenSource/formz)

**S1 / D2 / C1 → SDC 1**

A minimal typed model for pure and modified form inputs, validation errors, aggregate validity, and submission state.

**Real-world evidence:** Formz is published on pub.dev and its README documents integration with Dart and Flutter form-state architectures.

**Language evidence:** Typed form-input state, validation, error caching, aggregate form status, value semantics, and tests are implemented in one Dart library and its Dart test fixtures.

**Why study it:** One file demonstrates how a tiny generic domain model can make input value, interaction state, validation error, display policy, caching, equality, and whole-form queries explicit.

**What you can learn:**

- Generic abstract classes, sealed state through constructors, typed validation errors, pure versus dirty input state, lazy caching with mixins, aggregate predicates, enum extensions, immutability, equality, and unit tests.

**Prerequisites:**

- Dart generics, abstract classes, mixins, enums and extensions, null safety, immutable objects, and basic form validation.

**Start here:** [`lib/formz.dart`](https://github.com/VeryGoodOpenSource/formz/blob/57a4e1e7efb13eb1fea614158ccdd1fc52d4f969/lib/formz.dart) — The sole production file contains the entire model from submission status and typed inputs through cached errors and aggregate FormzMixin queries, with no framework layer to cross.

**Why this level:**

- **S1:** 66 meaningful implementation LOC measured with tokei 14.0.0. Count covers the complete production library in lib/formz.dart and excludes its Flutter example, tests, documentation, and package metadata.
- **D2:** The design combines several form-state invariants, but each operation is a direct predicate or immutable value transformation.
- **C1:** All behavior belongs to a single typed form model with no subsystem or lifecycle graph.
- **Placement:** S1/D2/C1 averages to 1.33, making Formz an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** Constructors distinguish untouched and modified values, validation remains user-supplied and typed, and the optional cache changes performance without changing the contract.
- **Architecture:** FormzInput models one field, FormzInputErrorCacheMixin memoizes validation, Formz aggregates fields, and FormzMixin projects those queries onto a form state.
- **Naming and idiom:** pure, dirty, isValid, displayError, validator, inputs, and FormzSubmissionStatus state the domain directly.
- **Tests:** Tests cover validity, error display, pure and dirty state, caching exactly once, equality, hashes, string output, aggregate inputs, and every submission-status predicate.
- **Documentation:** The README and API comments show custom typed inputs, validation, Flutter integration, caching, and form-level composition.
- **Traceability:** An input value can be followed through its validator into error, displayError, aggregate validity, and a focused fixture assertion.
- **Maintainability:** The domain has no hidden state, extensions are additive, the cache is isolated in a mixin, and the complete behavior suite is short enough to audit.
- **Educational value:** It is a strong first example of using a few language abstractions to replace loosely coupled booleans and nullable strings with an explicit domain model.

**Inspection record:** commit `57a4e1e7efb13eb1fea614158ccdd1fc52d4f969`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `lib/formz.dart`, `test/formz_test.dart`, `test/helpers/name_input.dart`, `LICENSE`. GitHub Linguist label: Dart. LOC exclusions: test/, example/, documentation and package metadata.

**License:** [MIT](https://github.com/VeryGoodOpenSource/formz/blob/57a4e1e7efb13eb1fea614158ccdd1fc52d4f969/LICENSE)

## SDC 2

### [felangel/mocktail](https://github.com/felangel/mocktail)

**S1 / D4 / C2 → SDC 2**

A null-safe Dart mocking library that intercepts invocations at runtime and supports stubbing, argument matching, capture, verification, and asynchronous call observation without code generation.

**Real-world evidence:** Mocktail is released on pub.dev and its README documents use as a test dependency in Dart and Flutter projects.

**Language evidence:** Runtime method interception, stubbing, invocation and argument matching, capture, verification, fallback values, call history, timing, and the test suite are Dart.

**Why study it:** It reveals the machinery behind a fluent mocking API: noSuchMethod interception, global recording modes, typed fallback values, invocation reconstruction, matcher evaluation, captured arguments, call history, verification, and reset behavior.

**What you can learn:**

- noSuchMethod and Invocation, runtime interception, generic fallback values under sound null safety, argument matchers, named and positional argument reconstruction, canned responses, call recording, verification counts, capture, streams, timestamps, errors, and framework self-tests.

**Prerequisites:**

- Advanced Dart classes and generics, noSuchMethod, closures, streams and futures, matcher libraries, null safety, test doubles, and mocking semantics.

**Start here:** [`packages/mocktail/lib/src/mocktail.dart`](https://github.com/felangel/mocktail/blob/d6a96e15b9203d33af61083e02e8c40ac07192d6/packages/mocktail/lib/src/mocktail.dart) — Mock.noSuchMethod shows the central mode switch among stubbing, verification, waiting, and real calls; the part files then explain matcher registration and invocation comparison.

**Why this level:**

- **S1:** 982 meaningful implementation LOC measured with tokei 14.0.0. Count covers the complete production mocktail package under packages/mocktail/lib and excludes tests, companion workspace packages, examples, documentation, and package metadata.
- **D4:** The implementation depends on subtle Dart runtime and type-system behavior and must distinguish several global recording modes without corrupting later calls.
- **C2:** Several interacting mechanisms share invocation state, but they remain inside one test-library runtime and a small file set.
- **Placement:** S1/D4/C2 averages to 2.33, making Mocktail an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** Recording modes, fallback errors, invocation matching, call history, and verification failures are explicit and report actionable context.
- **Architecture:** Mock intercepts calls; matcher registration reconstructs invocations; Expectation objects pair invocation predicates with responses; RealCall and VerifyCall own history and verification state.
- **Naming and idiom:** when, thenReturn, verify, captureAny, registerFallbackValue, RealCall, InvocationMatcher, and MissingStubError mirror testing intent.
- **Tests:** A broad self-test suite covers getters, setters, methods, generics, named and positional matchers, captures, fallback values, futures, streams, throws, resets, call counts, ordering, waiting, errors, and regressions.
- **Documentation:** The README explains setup, stubbing, verification, argument matching, captures, async behavior, fallback registration, FAQs, and migration concerns.
- **Traceability:** A mocked method can be followed from noSuchMethod through reconstructed Invocation arguments, matcher selection, canned response or call record, and an exact verification assertion.
- **Maintainability:** Runtime responsibilities are partitioned into part files, state reset is public and tested, and diagnostic paths guard invalid API combinations early.
- **Educational value:** It is a compact advanced example of building a language-native testing DSL over runtime interception rather than generated proxies.

**Inspection record:** commit `d6a96e15b9203d33af61083e02e8c40ac07192d6`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `packages/mocktail/lib/src/mocktail.dart`, `packages/mocktail/lib/src/_register_matcher.dart`, `packages/mocktail/lib/src/_invocation_matcher.dart`, `packages/mocktail/test/mocktail_test.dart`, `LICENSE`. GitHub Linguist label: Dart. LOC exclusions: packages/mocktail/test/, other workspace packages, examples, documentation, and package metadata.

**License:** [MIT](https://github.com/felangel/mocktail/blob/d6a96e15b9203d33af61083e02e8c40ac07192d6/LICENSE)

### [felangel/web_socket_client](https://github.com/felangel/web_socket_client)

**S1 / D3 / C2 → SDC 2**

A cross-platform WebSocket client with observable connection states, automatic reconnection, configurable backoff and timeout policy, message streams, and explicit shutdown.

**Real-world evidence:** The project is published as the web_socket_client package on pub.dev and documents Dart use across browser, desktop, mobile, and server runtimes.

**Language evidence:** Connection state, socket lifecycle, platform adapters, retry scheduling, backoff strategies, message streams, and integration tests are implemented in Dart.

**Why study it:** A small codebase makes asynchronous lifecycle behavior visible: platform-conditioned connection adapters, connection-state transitions, stream subscriptions, failure recovery, cumulative backoff, timeout closure, messages, and resource cleanup.

**What you can learn:**

- Futures, streams, broadcast controllers, subscriptions, timers, connection state machines, WebSocket channels, conditional imports, automatic reconnection, constant, linear, and exponential backoff, timeouts, idempotent shutdown, and socket integration tests.

**Prerequisites:**

- Dart asynchronous programming, streams and subscriptions, timers, sealed state objects, WebSocket concepts, conditional imports, and integration testing.

**Start here:** [`lib/src/web_socket.dart`](https://github.com/felangel/web_socket_client/blob/a1111df94451261b19f69bfa0cef17ba1e179c40/lib/src/web_socket.dart) — WebSocket owns the complete connection lifecycle from constructor-triggered connect through failure, reconnection, state publication, message forwarding, sending, timeout, and close.

**Why this level:**

- **S1:** 389 meaningful implementation LOC measured with tokei 14.0.0. Count covers all production Dart under lib and excludes tests, the example client, documentation, and package metadata.
- **D3:** Correctness depends on asynchronous ordering and resource lifecycle across platforms, though protocol framing itself is delegated to the WebSocket channel implementation.
- **C2:** Several components cooperate around one connection, but the topology remains a single client rather than a network service.
- **Placement:** S1/D3/C2 averages to 2.00, making WebSocket Client an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** State guards prevent duplicate connection and close work, timers and subscriptions are canceled explicitly, and failures retain errors and stack traces.
- **Architecture:** WebSocket owns orchestration; ConnectionController publishes state; Backoff implementations encapsulate retry timing; conditional adapters isolate browser and dart:io APIs.
- **Naming and idiom:** Connecting, Connected, Reconnecting, Reconnected, Disconnecting, Disconnected, Backoff, next, reset, send, and close expose lifecycle intent.
- **Tests:** Tests run real local WebSocket servers and verify failed connects, retries, recovery, timeouts, selected protocols, message flow, sends, close codes, state sequences, backoff progressions, resets, and value semantics.
- **Documentation:** The README covers connection, reconnection policy, all built-in backoffs, observable states, messages, binary browser data, timeouts, and closing.
- **Traceability:** A dropped socket can be followed from stream onDone into Disconnected and Reconnecting states, a scheduled attempt, Reconnected, and a real-server assertion.
- **Maintainability:** Platform differences and retry policies are separate from orchestration, state values are immutable, and lifecycle regressions are exercised through public behavior.
- **Educational value:** It is a bounded introduction to reliable asynchronous clients and the state ownership that a happy-path WebSocket example omits.

**Inspection record:** commit `a1111df94451261b19f69bfa0cef17ba1e179c40`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `lib/src/web_socket.dart`, `lib/src/connection.dart`, `lib/src/backoff/binary_exponential_backoff.dart`, `test/src/web_socket_test.dart`, `test/src/backoff/binary_exponential_backoff_test.dart`, `LICENSE`. GitHub Linguist label: Dart. LOC exclusions: test/, example/, documentation and package metadata.

**License:** [MIT](https://github.com/felangel/web_socket_client/blob/a1111df94451261b19f69bfa0cef17ba1e179c40/LICENSE)

## SDC 3

### [dart-lang/shelf](https://github.com/dart-lang/shelf)

**S2 / D3 / C3 → SDC 3**

Dart's composable web-server middleware ecosystem, with immutable requests and responses, streaming bodies, pipelines, routing, static files, proxies, WebSockets, and HTTP compliance checks.

**Real-world evidence:** The repository publishes the shelf family of packages used to build Dart HTTP servers and middleware, and maintains protocol-compliance reports against its server adapter.

**Language evidence:** HTTP request and response models, body and header handling, middleware composition, I/O adapters, routing tries, static and proxy handlers, WebSocket support, generators, and tests are Dart.

**Why study it:** Shelf shows how a small Handler function becomes a practical web stack through immutable message models, streaming bodies, nested path ownership, middleware wrapping, trie routing, protocol adapters, and focused companion packages.

**What you can learn:**

- Functional middleware composition, immutable HTTP messages, case-insensitive multi-value headers, byte streams and encodings, request path mounting, response construction, socket hijacking, I/O adapters, route tries and parameters, static files, proxies, WebSockets, source generation, and HTTP hardening tests.

**Prerequisites:**

- Intermediate Dart, futures and streams, HTTP requests, responses, headers and status codes, URI paths, middleware, sockets, regular expressions, and integration testing.

**Start here:** [`pkgs/shelf/lib/src/message.dart`](https://github.com/dart-lang/shelf/blob/3dbf65bedad2f1d97c5bae227b68a4ed1551a320/pkgs/shelf/lib/src/message.dart) — Message defines the immutable headers, context, body stream, encoding, content length, and change semantics shared by every request, response, middleware, router, and adapter path.

**Why this level:**

- **S2:** 2,616 meaningful implementation LOC measured with tokei 14.0.0. Count covers production Dart in shelf, shelf_packages_handler, shelf_proxy, shelf_router, shelf_router_generator, shelf_static, and shelf_web_socket; test-only packages and harnesses, tests, examples, benchmarks, docs, and metadata are excluded.
- **D3:** The implementation must preserve HTTP, stream, and routing invariants across synchronous and asynchronous composition, while using established Dart I/O primitives.
- **C3:** Several independently publishable packages cooperate around one server contract, producing a meaningful subsystem graph without platform-scale deployment complexity.
- **Placement:** S2/D3/C3 averages to 2.67 and rounds upward, making Shelf an SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** Message invariants fail early, headers and context are immutable, streaming ownership is documented, and adapters make protocol translation visible.
- **Architecture:** Handler and Middleware are the stable core; Request and Response carry messages; Pipeline composes behavior; shelf_io adapts sockets; companion packages add routing and concrete handlers.
- **Naming and idiom:** Handler, Middleware, Pipeline, Request.change, handlerPath, Response, Router, Trie, createStaticHandler, and webSocketHandler express the web model.
- **Tests:** Package suites cover bodies, headers, encodings, request paths, responses, middleware order, adapters, hijacking, routing patterns and parameters, static files, proxies, WebSockets, generated routes, and HTTP compliance and hardening scenarios.
- **Documentation:** Repository and per-package READMEs explain the handler model, middleware composition, serving, routing, static content, proxies, WebSockets, examples, and publishing status.
- **Traceability:** A request can be followed from the I/O adapter into Request, through nested pipeline wrappers and trie matching, into a handler, and back through Response streaming and protocol tests.
- **Maintainability:** A deliberately small shared contract lets packages evolve separately, immutable messages constrain side effects, and compliance reports expose adapter behavior.
- **Educational value:** It is a clear bridge from small functional composition to a tested, extensible HTTP ecosystem.

**Inspection record:** commit `3dbf65bedad2f1d97c5bae227b68a4ed1551a320`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `pkgs/shelf/lib/src/message.dart`, `pkgs/shelf/lib/src/request.dart`, `pkgs/shelf/lib/src/pipeline.dart`, `pkgs/shelf_router/lib/src/router.dart`, `pkgs/shelf_router/lib/src/trie.dart`, `pkgs/shelf/test/pipeline_test.dart`, `pkgs/shelf_router/test/router_test.dart`, `pkgs/_shelf_compliance/test/compliance_test.dart`, `LICENSE`. GitHub Linguist label: Dart. LOC exclusions: all test/ directories, examples and benchmarks, _shelf_compliance harness, shelf_test_handler, documentation and package metadata.

**License:** [BSD-3-Clause](https://github.com/dart-lang/shelf/blob/3dbf65bedad2f1d97c5bae227b68a4ed1551a320/LICENSE)

### [google/json_serializable.dart](https://github.com/google/json_serializable.dart)

**S2 / D4 / C3 → SDC 3**

A source generator and annotation suite that derives typed Dart JSON codecs, validation helpers, field metadata, enums, converters, generics, and JSON Schema from class declarations.

**Real-world evidence:** The repository publishes json_serializable, json_annotation, and checked_yaml packages used in Dart build_runner workflows and generated model layers.

**Language evidence:** Annotations, analyzer-driven model inspection, serialization and deserialization generation, type-helper dispatch, schema output, checked runtime helpers, YAML support, and tests are Dart.

**Why study it:** It demonstrates production code generation from semantic elements: merge configuration, select accessible fields and constructors, dispatch by Dart type, preserve nullability and defaults, generate checked or direct code, report source errors, and verify emitted behavior.

**What you can learn:**

- Dart analyzer elements and types, source_gen builders, annotations and constant reading, code generation, constructor and field discovery, nullability, generic factories, type-helper chains, custom converters, enum and map-key handling, checked decoding, schema generation, golden sources, and round-trip integration tests.

**Prerequisites:**

- Advanced Dart types and null safety, annotations, constructors and fields, JSON encoding, build_runner and source generation, analyzer element APIs, generics, code emission, and test fixtures.

**Start here:** [`json_serializable/lib/src/generator_helper.dart`](https://github.com/google/json_serializable.dart/blob/9ccf5da684914cc332b60d5e030f9288aa29ac62/json_serializable/lib/src/generator_helper.dart) — GeneratorHelper merges configuration, discovers usable fields, invokes decoding and encoding helpers, detects duplicate keys, and assembles every optional generated member.

**Why this level:**

- **S2:** 4,567 meaningful implementation LOC measured with tokei 14.0.0. Count covers production Dart in checked_yaml/lib, json_annotation/lib, and json_serializable/lib; tests, fixtures, examples and their generated output, repository-maintenance tools, docs, and metadata are excluded.
- **D4:** Correct output depends on advanced type-system and analyzer knowledge across a large matrix of source shapes and configuration combinations.
- **C3:** Multiple packages and helper families cooperate around one generation pipeline, with emitted code forming a second runtime boundary.
- **Placement:** S2/D4/C3 averages to 3.00, making json_serializable an SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** Unsupported source shapes fail with element context, configuration is merged explicitly, generated expressions retain target types, and duplicate or unsafe keys are rejected.
- **Architecture:** Annotations define policy; GeneratorHelper coordinates; DecodeHelper and EncodeHelper emit functions; ordered TypeHelpers translate specific Dart types; checked helpers enforce runtime input contracts.
- **Naming and idiom:** JsonSerializableGenerator, GeneratorHelper, TypeHelper, createFactory, createToJson, jsonKeyFor, UnsupportedTypeError, and checkedConvert reveal generation stages.
- **Tests:** Annotated-source, field-matrix, kitchen-sink, integration, schema, converter, generic, enum, map-key, default-value, checked-mode, configuration, and round-trip suites cover both emitted text and runtime behavior.
- **Documentation:** The README and package guides explain setup, builders, annotations, configuration, converters, generics, supported types, enums, generated members, and troubleshooting.
- **Traceability:** A class field can be followed from analyzer discovery through JsonKey policy and a selected TypeHelper into emitted fromJson and toJson expressions and a round-trip assertion.
- **Maintainability:** Type-specific logic is extensible behind one helper protocol, generation stages are separated, and a large source matrix guards language and analyzer changes.
- **Educational value:** It is a practical intermediate-to-advanced study of compilers in miniature: semantic input becomes validated executable source.

**Inspection record:** commit `9ccf5da684914cc332b60d5e030f9288aa29ac62`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `json_serializable/lib/src/json_serializable_generator.dart`, `json_serializable/lib/src/generator_helper.dart`, `json_serializable/lib/src/decode_helper.dart`, `json_serializable/lib/src/encoder_helper.dart`, `json_serializable/lib/src/type_helpers/map_helper.dart`, `json_serializable/test/json_serializable_test.dart`, `json_serializable/test/integration/integration_test.dart`, `LICENSE`. GitHub Linguist label: Dart. LOC exclusions: all test/ directories, example/ and generated example outputs, tool/ generators for repository maintenance, shared_test and _test_yaml fixtures, documentation and package metadata.

**License:** [BSD-3-Clause](https://github.com/google/json_serializable.dart/blob/9ccf5da684914cc332b60d5e030f9288aa29ac62/LICENSE)

## SDC 4

### [dart-lang/pub](https://github.com/dart-lang/pub)

**S3 / D4 / C4 → SDC 4**

Dart's package manager, including dependency resolution, lockfiles and workspaces, hosted, Git and path sources, caching, publishing, authentication, package validation, and command-line workflows.

**Real-world evidence:** This repository supplies the pub implementation invoked by the Dart SDK for dependency acquisition, package publication, workspace management, and package commands.

**Language evidence:** Command dispatch, package and workspace models, PubGrub version solving, source adapters, caches, lockfiles, downloads, publishing, authentication, validation, diagnostics, and tests are Dart.

**Why study it:** Pub joins a documented conflict-driven dependency solver with real package sources, caches, archives, credentials, lockfiles, workspaces, command UX, and failure explanations, making abstract algorithms traceable into a production tool.

**What you can learn:**

- Package-manager architecture, semantic version ranges, PubGrub and conflict-driven clause learning, unit propagation, backjumping, derivation graphs, human-readable solver failures, lockfiles, workspace resolution, hosted and Git sources, HTTP caching, archives, publishing, authentication tokens, validation, command runners, and process-level tests.

**Prerequisites:**

- Advanced Dart, graph and set reasoning, semantic versioning, constraint solving, asynchronous I/O, HTTP, filesystems and archives, Git, command-line tools, credentials, package ecosystems, and integration testing.

**Start here:** [`lib/src/solver/version_solver.dart`](https://github.com/dart-lang/pub/blob/8be46bd8538d4763aabe93a47a242dd5a3b0d9f3/lib/src/solver/version_solver.dart) — VersionSolver contains PubGrub's central loop, unit propagation, conflict resolution and backjumping, version choice, lazy package incompatibilities, and final result construction, with doc/solver.md defining the model.

**Why this level:**

- **S3:** 25,113 meaningful implementation LOC measured with tokei 14.0.0. Count covers all production Dart under lib and bin, including commands, solver, sources, cache, publishing, authentication, validation, models, and utilities; tests, tools, docs, fixtures, goldens, and metadata are excluded.
- **D4:** The solver is an advanced search algorithm and its result must remain consistent with persistent package state and several failure-prone external systems.
- **C4:** Most user operations coordinate multiple durable and external subsystems through shared package and resolution models.
- **Placement:** S3/D4/C4 averages to 3.67 and rounds upward, making Pub an SDC 4 project.

**Quality-gate evidence:**

- **Source quality:** Solver state and incompatibilities are domain types, filesystem and network work is wrapped by source and cache abstractions, and failures retain actionable package context.
- **Architecture:** Commands enter through a shared runner; Entrypoint coordinates workspaces and lock state; VersionSolver resolves constraints; Source implementations fetch packages through SystemCache; validators and publisher own release policy.
- **Naming and idiom:** VersionSolver, Term, Incompatibility, PartialSolution, PackageLister, Entrypoint, LockFile, SystemCache, HostedSource, and LishCommand encode package-manager concepts.
- **Tests:** Extensive process and unit suites cover solver graphs and regressions, lockfiles, sources, workspaces, caches, offline behavior, commands, archives, credentials, validators, publishing protocols, errors, suggestions, and golden transcripts.
- **Documentation:** The README points users to official command documentation, while repository documents specify PubGrub, cache and tool layouts, hosted repositories, and contributor workflows.
- **Traceability:** A dependency constraint can be followed from pubspec parsing into PackageRange terms, propagation and conflicts, a selected PackageId, lockfile and cache work, or a derivation-graph failure explanation and exact integration test.
- **Maintainability:** Algorithmic state, package identity, sources, I/O, command policy, and diagnostics are separated, and end-to-end fixtures protect externally observable behavior.
- **Educational value:** It is an advanced but unusually well-explained example of combining a difficult algorithm with the operational details of a production developer tool.

**Inspection record:** commit `8be46bd8538d4763aabe93a47a242dd5a3b0d9f3`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `doc/solver.md`, `lib/src/solver/version_solver.dart`, `lib/src/solver/incompatibility.dart`, `lib/src/entrypoint.dart`, `lib/src/source/hosted.dart`, `test/version_solver_test.dart`, `LICENSE`. GitHub Linguist label: Dart. LOC exclusions: test/, tool/, doc/, generated test data and goldens, documentation and package metadata.

**License:** [BSD-3-Clause](https://github.com/dart-lang/pub/blob/8be46bd8538d4763aabe93a47a242dd5a3b0d9f3/LICENSE)

### [sass/dart-sass](https://github.com/sass/dart-sass)

**S3 / D5 / C4 → SDC 4**

The reference Sass compiler, with parsers for Sass syntaxes, a module-aware evaluator, selector extension, values and calculations, CSS serialization, import systems, embedded protocol, command-line tool, and host APIs.

**Real-world evidence:** Dart Sass is the primary maintained Sass implementation and this repository builds its command-line, JavaScript, Dart, and embedded compiler distributions.

**Language evidence:** SCSS, indented Sass and CSS parsing, ASTs, evaluation, modules, imports, selectors and extension, values and calculations, serialization, embedded protocol handling, JavaScript and Dart APIs, CLI behavior, and tests are predominantly Dart.

**Why study it:** It is a readable production language implementation: multiple concrete syntaxes become typed ASTs; the evaluator manages lexical and module state; selector algorithms implement @extend; values and calculations enforce semantics; serializers and host protocols emit results.

**What you can learn:**

- Lexer and recursive-descent parser design, source spans and diagnostics, AST hierarchies and visitors, lexical environments, user and built-in functions and mixins, modules and canonical imports, synchronous and asynchronous evaluation, selector unification and extension laws, Sass values and calculations, CSS serialization and source maps, deprecations, host APIs, embedded protocols, CLI behavior, and specification-driven tests.

**Prerequisites:**

- Advanced Dart, compiler and interpreter construction, parsing, AST visitors, language semantics and environments, graphs and modules, selector algebra, asynchronous APIs, source maps, protocols, and large test corpora.

**Start here:** [`lib/src/visitor/evaluate.dart`](https://github.com/sass/dart-sass/blob/62243d455aa1d2ac7462e4c0ddda964ffbc82363/lib/src/visitor/evaluate.dart) — EvaluateVisitor is the semantic center where parsed statements, expressions, modules, imports, environments, functions, mixins, extensions, warnings, source spans, and CSS output converge.

**Why this level:**

- **S3:** 43,504 meaningful implementation LOC measured with tokei 14.0.0. Count covers non-generated production Dart under lib, bin, pkg/sass_api/lib, and pkg/sass-parser/lib; tests, maintenance tools, analysis support, generated output, packaging artifacts, docs, and metadata are excluded.
- **D5:** Core paths require expert language-implementation and algorithmic knowledge, and must conform precisely to a rich evolving specification.
- **C4:** A compilation crosses many coordinated subsystems and host surfaces, while remaining a single compiler platform rather than a distributed system.
- **Placement:** S3/D5/C4 averages to 4.00; the D5 floor also prevents placement below level 4, making Dart Sass an SDC 4 project.

**Quality-gate evidence:**

- **Source quality:** Semantic state, source spans, importer ownership, module cycles, extension contexts, deprecations, and synchronous versus asynchronous behavior are represented explicitly and fail with Sass-specific diagnostics.
- **Architecture:** Syntax-specific parsers produce shared Sass ASTs; evaluator visitors resolve modules and values into CSS ASTs; ExtensionStore applies selector rules; serializers emit CSS; adapters expose CLI, Dart, JavaScript, and embedded APIs.
- **Naming and idiom:** StylesheetParser, EvaluateVisitor, Environment, Module, Importer, ExtensionStore, SassValue, Calculation, SerializeVisitor, and CompilationDispatcher expose compiler concepts.
- **Tests:** The repository combines API, CLI, parser, value, importer, protocol, source-map, regression, and specification suites, including synchronous and asynchronous host callbacks and externally maintained Sass spec cases.
- **Documentation:** The README, differences and performance guides, contributor docs, subsystem READMEs, API docs, language specification links, and host-package guides orient both users and implementers.
- **Traceability:** A source construct can be followed from a syntax parser into a typed AST visitor, environment and module operation, selector or value semantics, CSS serialization, and a spec or API assertion.
- **Maintainability:** Shared AST and visitor protocols isolate syntax and phase changes, import and host adapters are bounded, and specification tests constrain compatibility across releases.
- **Educational value:** It is a premier advanced Dart corpus for seeing an industrial language implementation without the additional runtime and machine-code layers of a general-purpose VM.

**Inspection record:** commit `62243d455aa1d2ac7462e4c0ddda964ffbc82363`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `lib/src/parse/stylesheet.dart`, `lib/src/visitor/evaluate.dart`, `lib/src/extend/extension_store.dart`, `lib/src/value.dart`, `lib/src/visitor/serialize.dart`, `test/dart_api/function_test.dart`, `LICENSE`. GitHub Linguist label: Dart. LOC exclusions: test/, tool/ and analysis/, generated .g.dart and protobuf output, package and npm build output, documentation and package metadata.

**License:** [MIT](https://github.com/sass/dart-sass/blob/62243d455aa1d2ac7462e4c0ddda964ffbc82363/LICENSE)

## SDC 5

### [dart-lang/sdk](https://github.com/dart-lang/sdk)

**S5 / D5 / C5 → SDC 5**

The Dart language platform: common front end, analyzers and language server, intermediate representation, native and web compilers, virtual machine, JIT and AOT runtimes, garbage collector, core libraries, debugger services, command-line tools, and platform ports.

**Real-world evidence:** This repository is the upstream source for official Dart SDK releases and the compiler, runtime, libraries, analyzer, and tools used by Dart and Flutter developers.

**Language evidence:** The analyzer, common front end, kernel IR, dart2js, development compiler, WebAssembly compiler, analysis server, package tools, debugger services, and core libraries are Dart, while the first-party VM, garbage collector, JIT, AOT backend, runtime and native platform layers are C++ and related native code.

**Why study it:** It is the complete path from source text and language rules through analysis, kernel IR, optimization and native, JavaScript, or WebAssembly code generation into VM execution, garbage collection, debugging, libraries, tools, and multi-platform releases.

**What you can learn:**

- Language front ends and diagnostics, parsing and static analysis, type inference and null safety, kernel intermediate representation, incremental compilation, dart2js and JavaScript optimization, WebAssembly code generation, VM bytecode and machine-code compilation, SSA and optimization passes, JIT and AOT execution, garbage collection and heap management, isolates and concurrency, snapshots and hot reload, core libraries, analysis protocols, debugging services, command tools, ABI and architecture ports, and toolchain testing.

**Prerequisites:**

- Expert Dart and C++, programming-language semantics, compiler construction and IR, static analysis and type systems, operating systems, virtual machines, garbage collection, concurrency and memory models, assembly and computer architecture, JavaScript and WebAssembly, protocols, performance engineering, and very large monorepo navigation.

**Start here:** [`pkg/front_end/lib/src/kernel_generator_impl.dart`](https://github.com/dart-lang/sdk/blob/967bed205c83cba3ac05b0f8d084d11291e93ff1/pkg/front_end/lib/src/kernel_generator_impl.dart) — generateKernel is a central bounded entry from validated compiler options and SDK summaries through outlines, source loading, precompilation, verification, transformations, and a Kernel Component consumed by multiple back ends.

**Why this level:**

- **S5:** 1,486,780 meaningful implementation LOC measured with tokei 14.0.0. Conservative count covers non-generated first-party Dart, C++, C and headers, GNU-style assembly, and Objective-C++ in selected production runtime and VM directories, sdk/lib, and the front end, analyzer, compiler, kernel, VM, dart2wasm, dartdev, DDS, DTD, and analysis-server libraries. Tests, generated code, examples, docs, tooling, and third-party material are excluded.
- **D5:** Expert language, compiler, runtime, operating-system, concurrency, memory, architecture, and performance knowledge recurs throughout every central path.
- **C5:** The SDK is a platform-scale language ecosystem whose independently deep components must agree on semantics, representations, protocols, runtime layouts, and compatibility.
- **Placement:** S5/D5/C5 averages to 5.00 and satisfies the two-dimensions-at-5 guardrail, making the Dart SDK an SDC 5 project.

**Quality-gate evidence:**

- **Source quality:** Compiler and runtime phases expose invariants, target and architecture distinctions are explicit, diagnostic context is preserved, and low-level layout checks fail fast when generated code and runtime disagree.
- **Architecture:** The shared front end emits Kernel IR for analyzer and compiler consumers; native, JavaScript and WebAssembly back ends transform it; the VM and runtime execute code; libraries and protocol services form the developer platform above them.
- **Naming and idiom:** CompilerContext, KernelTarget, Component, FlowGraph, CompilerPass, Isolate, Heap, Snapshot, Analyzer, AnalysisServer, DDS, and Dartdev maintain toolchain vocabulary.
- **Tests:** Language conformance, analyzer, front-end, kernel, compiler, VM unit, optimization, runtime, GC, hot-reload, service, protocol, library, architecture, web, Wasm, integration, performance, and platform builders protect the SDK.
- **Documentation:** Language specifications, SDK guides, architecture and subsystem notes, package READMEs, protocol specifications, build instructions, API references, and source comments cover use and implementation.
- **Traceability:** A Dart function can be followed from source loading and front-end outline/body construction into Kernel IR, a chosen backend and optimization pipeline, emitted code, VM runtime objects and scheduling, and focused compiler and runtime tests.
- **Maintainability:** Shared semantic and IR layers, explicit target interfaces, generated-code markers, platform build guards, layout verification, compatibility processes, and exhaustive builders constrain a self-hosting platform.
- **Educational value:** It is the definitive Dart capstone and a complete expert reference for how a modern language becomes analysis tools, several compilers, a virtual machine, libraries, and a portable SDK.

**Inspection record:** commit `967bed205c83cba3ac05b0f8d084d11291e93ff1`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `pkg/front_end/README.md`, `pkg/front_end/lib/src/kernel_generator_impl.dart`, `pkg/compiler/lib/src/compiler.dart`, `runtime/vm/compiler/compiler_pass.cc`, `runtime/vm/dart.cc`, `pkg/front_end/test/kernel_generator_test.dart`, `runtime/vm/compiler/backend/constant_propagator_test.cc`, `LICENSE`. GitHub Linguist label: Dart. LOC exclusions: all test and tests directories, *_test source files, generated directories, *.g.dart and generated_*.dart, runtime/bin/ffi_test, examples, benchmarks, documentation, build and release tooling, third-party and vendored code.

**License:** [BSD-3-Clause](https://github.com/dart-lang/sdk/blob/967bed205c83cba3ac05b0f8d084d11291e93ff1/LICENSE)

### [flutter/flutter](https://github.com/flutter/flutter)

**S5 / D5 / C5 → SDC 5**

The Flutter application framework and SDK tooling for building reactive mobile, web, and desktop interfaces, including widgets, rendering, painting, gestures, semantics, platform services, design systems, testing, builds, devices, hot reload, localization, and integration infrastructure.

**Real-world evidence:** This repository builds the Flutter framework and command-line SDK distributed for production applications across Android, iOS, web, Windows, macOS, Linux, and embedded targets.

**Language evidence:** The widget, rendering, painting, animation, gesture, semantics, Material and Cupertino frameworks, scheduler and services, test runtime, build and device tools, localizations, driver, integration support, and web-plugin APIs are implemented predominantly in Dart.

**Why study it:** Flutter shows Dart at product-platform scale: immutable widget descriptions reconcile into persistent element and render trees; scheduler phases coordinate work; rendering, compositing, input and semantics meet platform services; tooling builds, launches, reloads, tests and diagnoses applications across devices.

**What you can learn:**

- Reactive UI and immutable widgets, element reconciliation and keyed identity, state lifecycles and inherited dependencies, render trees and constraint layout, painting and compositing, frame scheduling, animations, gestures and hit testing, focus and keyboard input, accessibility semantics, Material and Cupertino systems, platform channels, restoration, localization, testing bindings and fakes, incremental build graphs, artifact and device discovery, hot reload and restart, compiler and engine orchestration, desktop, mobile and web targets, diagnostics, performance, and large-framework evolution.

**Prerequisites:**

- Expert Dart, reactive UI architecture, graphics and rendering pipelines, layout algorithms, event systems and gestures, accessibility, asynchronous scheduling, mobile, desktop and browser platforms, build systems, compilers and device tooling, testing frameworks, performance engineering, and very large monorepo navigation.

**Start here:** [`packages/flutter/lib/src/widgets/framework.dart`](https://github.com/flutter/flutter/blob/0116c837eb60174e7bd81c5b1dde6fc6990ccc81/packages/flutter/lib/src/widgets/framework.dart) — The widget framework defines Widget, Element, BuildContext, State, keys, reconciliation, inherited dependencies, lifecycle, mounting, updating and teardown—the central model connecting application declarations to rendering.

**Why this level:**

- **S5:** 471,362 meaningful implementation LOC measured with tokei 14.0.0. Count covers non-generated production Dart in flutter, flutter_driver, flutter_localizations, flutter_test, flutter_tools, flutter_web_plugins, fuchsia_remote_debug_protocol, and integration_test libraries. Tests, examples, benchmarks, generated sources, engine artifacts, docs, configuration, and metadata are excluded.
- **D5:** Expert UI framework, graphics, scheduler, accessibility, toolchain, platform, lifecycle, and performance knowledge recurs across core learning paths.
- **C5:** Flutter is a platform-scale SDK in which a deep UI framework and a deep multi-platform developer toolchain coordinate across many runtime and external boundaries.
- **Placement:** S5/D5/C5 averages to 5.00 and satisfies the two-dimensions-at-5 guardrail, making Flutter an SDC 5 project.

**Quality-gate evidence:**

- **Source quality:** Framework invariants use assertions and structured diagnostics, ownership and lifecycle are explicit, performance-sensitive layers avoid unnecessary abstraction, and tooling preserves detailed failure context.
- **Architecture:** Foundation and scheduler support gestures, rendering and widgets; Material and Cupertino compose the framework; services bridge platforms; flutter_test simulates runtime behavior; flutter_tools coordinates artifacts, builds, devices and compilers.
- **Naming and idiom:** Widget, Element, BuildContext, State, RenderObject, Constraints, PipelineOwner, SchedulerBinding, GestureArena, SemanticsNode, Target, Environment, Device, and Artifact expose the platform model.
- **Tests:** Large unit, widget, rendering, golden, semantics, gesture, platform, tooling, build-system, device, command, integration, performance, regression, and shard suites exercise public behavior and internal invariants across platforms.
- **Documentation:** The README, API docs, architectural overview, inside-Flutter guides, subsystem and contributor documents, design notes, breaking-change records, and extensive source comments orient users and framework contributors.
- **Traceability:** A widget update can be followed through key matching and Element.update, build scheduling, render-object mutation, layout and paint pipelines, compositing and semantics, then into widget and rendering tests; a run command can likewise be traced through target and device tooling.
- **Maintainability:** Layered libraries, binding interfaces, lifecycle assertions, diagnostics, generated-data boundaries, platform abstractions, ownership files, presubmit shards, goldens, and compatibility processes support many specialist teams.
- **Educational value:** It is the definitive Dart application-platform capstone, connecting language idioms to a production UI framework, testing runtime, and multi-platform SDK toolchain.

**Inspection record:** commit `0116c837eb60174e7bd81c5b1dde6fc6990ccc81`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `packages/flutter/lib/src/widgets/framework.dart`, `packages/flutter/lib/src/rendering/object.dart`, `packages/flutter/lib/src/scheduler/binding.dart`, `packages/flutter_tools/lib/src/build_system/build_system.dart`, `packages/flutter/test/widgets/framework_test.dart`, `packages/flutter_tools/test/general.shard/build_system/build_system_test.dart`, `LICENSE`. GitHub Linguist label: Dart. LOC exclusions: all test directories, examples and dev benchmarks, *.g.dart, generated directories and generated_*.dart localization outputs, engine and external artifacts, documentation, build configuration, and release metadata.

**License:** [BSD-3-Clause](https://github.com/flutter/flutter/blob/0116c837eb60174e7bd81c5b1dde6fc6990ccc81/LICENSE)

_Generated from `catalog/dart.json`; do not edit by hand._

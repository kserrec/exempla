# Scala

10 qualified repositories. Scores assume the learner described in [the SDC rubric](../../docs/sdc.md).

[← All languages](../README.md)

## SDC 1

### [softwaremill/retry](https://github.com/softwaremill/retry)

**S1 / D2 / C1 → SDC 1**

A compact library of composable retry policies for Scala Futures, including immediate, paused, exponential-backoff, jittered, conditional, and fail-fast strategies.

**Real-world evidence:** SoftwareMill maintains and publishes the versioned com.softwaremill.retry artifact, and the README documents application-facing policy configuration and timer integration.

**Language evidence:** Retry policies, success predicates, jitter algorithms, asynchronous scheduling, and the complete test suite are implemented in Scala under retry/src.

**Why study it:** Four production files show how a tiny public abstraction can capture several useful retry strategies while keeping asynchronous repetition non-blocking and testable.

**What you can learn:**

- Scala Futures, implicit type classes, partial functions, recursive asynchronous control flow, capped exponential backoff, jitter algorithms, policy decorators, and focused timing and failure tests.

**Prerequisites:**

- Scala traits and objects, generics, implicits, Futures, execution contexts, partial functions, finite durations, and basic asynchronous tests.

**Start here:** [`retry/src/main/scala/Policy.scala`](https://github.com/softwaremill/retry/blob/f5d887b23adb8c34b2dc891a4d25a6263e300c48/retry/src/main/scala/Policy.scala) — Policy.scala contains the common contract and every retry strategy, so a learner can trace one failed Future through success classification, delay scheduling, recursion, and the matching PolicySpec case.

**Why this level:**

- **S1:** 325 meaningful implementation LOC measured with tokei 14.0.0. Count covers all four production Scala files under retry/src/main and excludes tests, documentation, and build metadata.
- **D2:** Asynchrony and backoff arithmetic introduce modest technical concerns, but each policy is short, explicit, and built from familiar Future operations.
- **C1:** The project has no persistence, service topology, or plugin system; an important behavior is local to Policy.scala and one timer boundary.
- **Placement:** S1/D2/C1 averages to 1.33, making retry an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** Policies share small internal helpers, failure paths are explicit, and jitter arithmetic is isolated from Future orchestration.
- **Architecture:** A Policy accepts deferred Future work, Success classifies results, Timer schedules pauses, and Jitter supplies a replaceable delay calculation.
- **Naming and idiom:** Directly, Pause, Backoff, JitterBackoff, When, FailFast, countdown, and retry state the behavior rather than the implementation trick.
- **Tests:** Focused ScalaTest suites cover retry counts, by-name execution, failed Futures, success predicates, pauses, backoff, jitter bounds, overflow, conditional policies, and fail-fast behavior on JVM and Scala.js.
- **Documentation:** The README explains installation, the Success type class, timers, every policy, examples, and the intended client-configuration pattern.
- **Traceability:** A Backoff call can be followed through countdown and Delay into a repeated Future and then into exact attempt-count and elapsed-time assertions.
- **Maintainability:** The small interface, shared helpers, bounded responsibility, cross-platform tests, and current published artifact keep changes reviewable.
- **Educational value:** It is a concise introduction to designing asynchronous policy objects without hiding their control flow behind a framework.

**Inspection record:** commit `f5d887b23adb8c34b2dc891a4d25a6263e300c48`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `retry/src/main/scala/Policy.scala`, `retry/src/main/scala/Jitter.scala`, `retry/src/main/scala/Success.scala`, `retry/src/test/scala/PolicySpec.scala`, `retry/src/test/scala/JitterSpec.scala`, `LICENSE`. GitHub Linguist label: Scala. LOC exclusions: retry/src/test/, README.md, build files.

**License:** [MIT](https://github.com/softwaremill/retry/blob/f5d887b23adb8c34b2dc891a4d25a6263e300c48/LICENSE)

### [typelevel/case-insensitive](https://github.com/typelevel/case-insensitive)

**S1 / D2 / C1 → SDC 1**

Typelevel's small locale-independent case-insensitive string value with lawful equality, hashing, ordering, Cats instances, interpolation, and extraction.

**Real-world evidence:** Typelevel publishes the cross-version case-insensitive artifact used as a dedicated value type in Scala libraries and documents its Maven coordinates and microsite.

**Language evidence:** The CIString value type, interpolator compatibility layers, Cats instances, test generators, and property suites are Scala across the core, testing, and cross-platform test modules.

**Why study it:** The repository turns one deceptively subtle value-semantic requirement into a tiny implementation whose equality, hash, ordering, interpolation, and Unicode edge cases are all visible.

**What you can learn:**

- Value-object invariants, equals and hashCode contracts, locale-independent case folding, cached hashes, ordering, Cats type-class instances, string interpolators, cross-version compatibility, property testing, and Unicode edge cases.

**Prerequisites:**

- Scala classes and companion objects, equality and hashing, string operations, implicits or givens, algebraic type classes, property tests, and basic Unicode awareness.

**Start here:** [`core/src/main/scala/org/typelevel/ci/CIString.scala`](https://github.com/typelevel/case-insensitive/blob/2b28be5341a0f1c6bc5c00a8486622f26018ae9c/core/src/main/scala/org/typelevel/ci/CIString.scala) — CIString.scala states the equality contract, implements hashing and ordering, and supplies the algebraic instances exercised directly by CIStringSuite and TurkeySuite.

**Why this level:**

- **S1:** 209 meaningful implementation LOC measured with tokei 14.0.0. Count covers the core production value and Scala-version compatibility files and excludes the test-support artifact, test suites, benchmark, documentation, and build metadata.
- **D2:** Correct value semantics require care, but the implementation relies on standard String and Character operations and remains concentrated in one principal file.
- **C1:** The core has no I/O or runtime topology and its behavior can be understood from one class, its companion, and the compatibility shim.
- **Placement:** S1/D2/C1 averages to 1.33, making case-insensitive an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** The implementation documents its surprising substitutability caveat, keeps equality and hashing aligned, and uses direct loops where allocation-free behavior matters.
- **Architecture:** CIString owns value semantics, its companion supplies Cats instances, and version-specific compatibility files implement interpolation without contaminating the core.
- **Naming and idiom:** CIString, calculateHash, contains, catsInstancesForOrgTypelevelCIString, and the ci interpolator expose precise responsibilities.
- **Tests:** Property suites verify equality, ordering, hashing, algebraic laws, serialization, interpolation, containment, and the Turkish-I edge case across platforms.
- **Documentation:** The README gives installation and points to the microsite, while the primary type documents the exact equality rule and its observable caveat.
- **Traceability:** CIString equality can be followed into case-insensitive comparison and the matching normalized hash loop, then checked against property laws and TurkeySuite.
- **Maintainability:** The public surface is narrow, platform differences are isolated, algebraic laws guard refactors, and the project remains actively maintained.
- **Educational value:** It demonstrates why a seemingly tiny value type deserves explicit contracts and law-based tests.

**Inspection record:** commit `2b28be5341a0f1c6bc5c00a8486622f26018ae9c`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `core/src/main/scala/org/typelevel/ci/CIString.scala`, `core/src/main/scala/org/typelevel/ci/package.scala`, `core/src/main/scala-3/org/typelevel/ci/compat.scala`, `tests/shared/src/test/scala/org/typelevel/ci/CIStringSuite.scala`, `tests/shared/src/test/scala/org/typelevel/ci/TurkeySuite.scala`, `LICENSE`. GitHub Linguist label: Scala. LOC exclusions: tests/, testing/, bench/, README.md, build files.

**License:** [Apache-2.0](https://github.com/typelevel/case-insensitive/blob/2b28be5341a0f1c6bc5c00a8486622f26018ae9c/LICENSE)

## SDC 2

### [com-lihaoyi/requests-scala](https://github.com/com-lihaoyi/requests-scala)

**S1 / D3 / C2 → SDC 2**

A compact synchronous Scala HTTP client with sessions, streaming, redirects, cookies, authentication, compression, TLS, proxies, and multipart uploads.

**Real-world evidence:** Li Haoyi publishes requests-scala as a versioned library and documents it as the straightforward HTTP client used from Scala applications.

**Language evidence:** The request API, HTTP transport orchestration, sessions, cookies, request and response models, encoders, decompression, errors, and integration tests are Scala.

**Why study it:** Fewer than a thousand production lines expose the concrete work beneath a friendly HTTP call: URI construction, headers, bodies, Java HttpClient configuration, redirects, cookies, streams, decompression, and resource cleanup.

**What you can learn:**

- Facade API design, Java HttpClient integration, request models, URL encoding, redirects, cookie persistence, TLS and proxies, streaming bodies, compression, multipart data, resource ownership, and local integration tests.

**Prerequisites:**

- Scala classes and collections, Java interoperability, HTTP request and response semantics, streams, cookies, TLS basics, compression, and resource cleanup.

**Start here:** [`requests/src/requests/Requester.scala`](https://github.com/com-lihaoyi/requests-scala/blob/e3619c19ef551067d2979ced99b434d45bb60986/requests/src/requests/Requester.scala) — Requester.apply delegates to stream, where URL, headers, cookies, transport configuration, redirects, body handling, response construction, and cleanup form one visible end-to-end request path.

**Why this level:**

- **S1:** 902 meaningful implementation LOC measured with tokei 14.0.0. Count covers all seven production Scala files under requests/src and excludes integration tests, documentation, fixtures, and build metadata.
- **D3:** The code is short, but correct request behavior crosses several protocol and resource-management concerns, including a platform-specific cleanup fallback.
- **C2:** Several small pieces cooperate around one HTTP client, with no server, persistence layer, plugin system, or multi-process topology.
- **Placement:** S1/D3/C2 averages to 2.00, making requests-scala an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** The public convenience call delegates to one streaming implementation, protocol helpers stay separated, and resource cleanup is explicit even where the JDK API varies.
- **Architecture:** Package-level verbs create Requesters, Session supplies reusable defaults and transport state, request blobs encode uploads, and Response owns aggregated output.
- **Naming and idiom:** Requester.stream, BaseSession, RequestBlob, StreamHeaders, persistCookies, autoDecompress, and maxRedirects make behavior discoverable.
- **Tests:** A local httpbin-based suite exercises methods, parameters, multipart data, cookies, redirects, streaming, timeouts, certificate handling, compression, headers, failures, and resource leaks.
- **Documentation:** The generated project documentation and readme orient users to installation and a Python-Requests-like API, while source comments document every request option and streaming contract.
- **Traceability:** A GET call can be followed through the package facade, Requester, shared HttpClient selection, request construction, response stream and redirects into a local integration assertion.
- **Maintainability:** One transport path serves buffered and streaming calls, session defaults are overrideable in one place, and regression tests cover platform and lifecycle failures.
- **Educational value:** It offers a rare small but realistic tour of application-level HTTP client mechanics.

**Inspection record:** commit `e3619c19ef551067d2979ced99b434d45bb60986`, reviewed 2026-08-28 by Codex. Files sampled: `readme.md`, `requests/src/requests/package.scala`, `requests/src/requests/Requester.scala`, `requests/src/requests/Session.scala`, `requests/src/requests/Model.scala`, `requests/test/src/requests/RequestTests.scala`, `requests/test/src/requests/ResourceLeakTests.scala`, `LICENSE`. GitHub Linguist label: Scala. LOC exclusions: requests/test/, readme.md, documentation and build files.

**License:** [MIT](https://github.com/com-lihaoyi/requests-scala/blob/e3619c19ef551067d2979ced99b434d45bb60986/LICENSE)

### [scopt/scopt](https://github.com/scopt/scopt)

**S1 / D2 / C2 → SDC 2**

A small cross-platform command-line option parser for Scala with functional and object-oriented declaration styles and interceptable effects.

**Real-world evidence:** The project publishes scopt artifacts for Scala 2, Scala 3, JVM, Scala.js, and Scala Native and documents a mature application configuration API.

**Language evidence:** The option definitions, functional and object-oriented DSLs, parser runner, validation, rendering, effects, type readers, and platform adapters are Scala.

**Why study it:** Its source connects a typed declaration DSL to token matching, occurrence constraints, configuration updates, validation, usage rendering, and effect handling without a large framework.

**What you can learn:**

- Typed option readers, builder DSLs, immutable parser descriptions, token classification, commands and positionals, occurrence constraints, validation, effect separation, usage rendering, and cross-platform parsing.

**Prerequisites:**

- Scala generics, type classes, case classes, immutable collections, higher-order functions, command-line conventions, and basic cross-platform source layouts.

**Start here:** [`shared/src/main/scala/scopt/OParser.scala`](https://github.com/scopt/scopt/blob/f1906911a989320a87c0670fb2e654d48731747d/shared/src/main/scala/scopt/OParser.scala) — OParser builds the declarative option list and hands it to ORunner, providing the shortest path from user-facing DSL calls to token execution and parser effects.

**Why this level:**

- **S1:** 1,183 meaningful implementation LOC measured with tokei 14.0.0. Count covers shared production parsing plus the JVM, JS, and Native read adapters and excludes every test source set, build logic, documentation, and build metadata.
- **D2:** Generic readers and parser state require attention, but the grammar and transitions are conventional and represented with explicit data and branches.
- **C2:** Several clear layers cooperate in one small library, while platform-specific code remains limited to value readers.
- **Placement:** S1/D2/C2 averages to 1.67 and rounds upward, making scopt an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** Parser descriptions are immutable, effects are represented explicitly, and token, validation, and rendering responsibilities remain separated.
- **Architecture:** OParser builds OptionDefs, ORunner consumes arguments into configurations and OEffects, and a separate interpreter performs display or termination effects.
- **Naming and idiom:** OptionDefKind, minOccurs, validateConfig, runParser, runEffects, RenderingMode, and DefaultOEffectSetup reveal the parsing lifecycle.
- **Tests:** Shared and platform suites cover both APIs, option forms, grouped flags, commands, arguments, validation, fallback values, rendering, URI and platform readers, and regression cases.
- **Documentation:** The README supplies complete functional and object-oriented examples, generated usage output, supported readers, commands, validation, and effect interception.
- **Traceability:** A declared option can be followed from OParserBuilder into an OptionDef, ORunner's token match and action, an updated configuration, emitted effects, and ImmutableParserSpec.
- **Maintainability:** The dual APIs converge on one representation, platform dependencies stay at the edge, and behavior-focused suites cover the supported matrix.
- **Educational value:** It is a compact example of separating a declarative interface, a pure-ish execution result, and side-effect interpretation.

**Inspection record:** commit `f1906911a989320a87c0670fb2e654d48731747d`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `shared/src/main/scala/scopt/OParser.scala`, `shared/src/main/scala/scopt/ORunner.scala`, `shared/src/main/scala/scopt/OptionDef.scala`, `shared/src/main/scala/scopt/Read.scala`, `shared/src/test/scala/scopttest/ImmutableParserSpec.scala`, `shared/src/test/scala/scopttest/MonadicParserSpec.scala`, `LICENSE.md`. GitHub Linguist label: Scala. LOC exclusions: shared/src/test/, jvm/src/test/, js/src/test/, native/src/test/, project/, README.md, build files.

**License:** [MIT](https://github.com/scopt/scopt/blob/f1906911a989320a87c0670fb2e654d48731747d/LICENSE.md)

## SDC 3

### [circe/circe](https://github.com/circe/circe)

**S2 / D4 / C3 → SDC 3**

A modular functional JSON library for Scala with immutable values, typed codecs, cursor navigation, generic derivation, parsing integrations, literals, and JSON Pointer.

**Real-world evidence:** The circe organization publishes cross-platform modules and maintains versioned documentation for production JSON encoding and decoding across the Scala ecosystem.

**Language evidence:** The immutable JSON model, cursors, codecs, numeric representation, parser integrations, printing, generic derivation, literal macros, pointers, and platform modules are Scala.

**Why study it:** Circe separates JSON representation, navigation, error accumulation, parsing, printing, codecs, and derivation, making the tradeoffs of a strongly typed functional API inspectable across clear modules.

**What you can learn:**

- Algebraic JSON models, cursors and edit histories, type-class codecs, fail-fast and accumulating decoding, numeric preservation, parser and printer boundaries, generic product and coproduct derivation, literal macros, law testing, and cross-platform design.

**Prerequisites:**

- Advanced Scala types, Cats abstractions, Either and Validated, type classes, recursive algebraic data, JSON grammar, macros or derivation, and cross-platform modules.

**Start here:** [`modules/core/shared/src/main/scala/io/circe/Decoder.scala`](https://github.com/circe/circe/blob/2fb611bb49619e4287b6ac048d2283c2781f4943/modules/core/shared/src/main/scala/io/circe/Decoder.scala) — Decoder connects the public typed API to HCursor navigation, error histories, composition, accumulation, collection decoding, and the comprehensive DecoderSuite before generic derivation is introduced.

**Why this level:**

- **S2:** 8,270 meaningful implementation LOC measured with tokei 14.0.0. Count covers production Scala and Java in the core, numbers, generic, parser, literal, pointer, extras, shapes, scodec, and platform modules; test support, laws, benchmarks, rewrite rules, examples, tests, documentation, and build metadata are excluded.
- **D4:** Advanced types, functional error models, recursive structures, and compile-time derivation recur across the central codec path.
- **C3:** Several substantial library layers and extension modules interact, but all converge on stable in-process JSON and codec contracts.
- **Placement:** S2/D4/C3 averages to 3.00, making circe an SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** Core algebraic types and codec combinators are explicit, low-level number handling is isolated, and complex derivation machinery is kept out of the runtime model.
- **Architecture:** Json and JsonObject represent values; cursors navigate with histories; Encoder and Decoder map types; parsers and Printer handle syntax; derivation modules synthesize codecs.
- **Naming and idiom:** HCursor, ACursor, CursorOp, DecodingFailure, decodeAccumulating, JsonNumber, AsObjectEncoder, and DerivedDecoder state contracts precisely.
- **Tests:** Property laws and suites cover values, numbers, cursors, codecs, error accumulation, parsers, printers, derivation, literals, pointers, platform differences, compatibility, and regression cases.
- **Documentation:** The README gives purpose, installation, module links, examples, version support, and documentation routes; dedicated docs explain codecs and advanced usage.
- **Traceability:** A field decode can be traced from Decoder.forProduct through HCursor movement and history, into fail-fast or accumulating results, then through DecoderSuite properties and derived-codec suites.
- **Maintainability:** The immutable core is decoupled from syntax and derivation, modules make optional features explicit, and law suites guard compositional contracts across platforms.
- **Educational value:** It is a strong study of how functional API design can preserve precise errors and composition without merging representation, parsing, and object mapping.

**Inspection record:** commit `2fb611bb49619e4287b6ac048d2283c2781f4943`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `modules/core/shared/src/main/scala/io/circe/Json.scala`, `modules/core/shared/src/main/scala/io/circe/Decoder.scala`, `modules/core/shared/src/main/scala/io/circe/HCursor.scala`, `modules/generic/shared/src/main/scala-2/io/circe/generic/util/macros/DerivationMacros.scala`, `modules/jawn/shared/src/main/scala/io/circe/jawn/JawnParser.scala`, `modules/tests/shared/src/test/scala/io/circe/DecoderSuite.scala`, `LICENSE`. GitHub Linguist label: Scala. LOC exclusions: modules/tests/, modules/testing/, modules/laws/, modules/benchmark/, modules/numbers-testing/, modules/scalafix/, all src/test/ trees, examples/ and documentation.

**License:** [Apache-2.0](https://github.com/circe/circe/blob/2fb611bb49619e4287b6ac048d2283c2781f4943/LICENSE)

### [com-lihaoyi/upickle](https://github.com/com-lihaoyi/upickle)

**S2 / D4 / C3 → SDC 3**

A cross-platform Scala serialization family for typed objects, JSON, MessagePack, streaming visitors, and derived codecs.

**Real-world evidence:** The project publishes uPickle, uJson, and uPack artifacts and maintains user documentation for JSON and binary serialization in Scala applications.

**Language evidence:** The visitor protocol, JSON and MessagePack parsers and writers, object serializers, Scala 2 macros, Scala 3 derivation, format adapters, and schema support are implemented in Scala.

**Why study it:** It unifies text JSON, binary MessagePack, mutable JSON values, and typed object codecs behind one allocation-conscious visitor protocol, then shows both Scala 2 macro and Scala 3 Mirror-based derivation.

**What you can learn:**

- Visitor-based tree processing, JSON and MessagePack state machines, buffered input, typed readers and writers, recursive codecs, tagged sum types, Scala 2 macros, Scala 3 Mirrors and inline derivation, cross-platform adapters, and serialization failure paths.

**Prerequisites:**

- Advanced Scala generics and variance, type classes, binary and text serialization, byte buffers, state machines, macros or Mirrors, inline methods, and cross-platform source conventions.

**Start here:** [`upickle/core/src/upickle/core/Visitor.scala`](https://github.com/com-lihaoyi/upickle/blob/87e0b24b8c811e174ebd680839e4edf1e62abe71/upickle/core/src/upickle/core/Visitor.scala) — Visitor defines the shared event protocol; tracing it into ujson's parser, upack's MsgPackReader, and a derived ReadWriter reveals how all formats avoid an obligatory intermediate tree.

**Why this level:**

- **S2:** 7,550 meaningful implementation LOC measured with tokei 14.0.0. Count covers production Scala across uPickle, uJson, uPack, format adapters, JSON Schema, platform sources, and both Scala derivation implementations; tests, benchmarks, documentation generators, source templates, and build metadata are excluded.
- **D4:** Advanced parsing, binary encoding, type derivation, recursion, and performance concerns recur through the principal serialization path.
- **C3:** Several formats and execution modes meet at explicit visitor and reader/writer contracts, creating meaningful but bounded cross-module tracing.
- **Placement:** S2/D4/C3 averages to 3.00, making uPickle an SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** The visitor contract centralizes traversal, byte parsers make indices and buffer growth explicit, and derivation code is isolated by Scala version.
- **Architecture:** Parsers emit Visitor events; uJson or uPack materialize values, typed Readers consume events, Writers emit them, and derived codecs bridge Scala products and sums.
- **Naming and idiom:** Visitor, ObjVisitor, BufferingByteParser, MsgPackReader, CaseClassReader, ReadWriter, macroRW, and TraceVisitor expose each role.
- **Tests:** Format, primitive, macro, derivation, failure, large-input, streaming, schema, compatibility, and cross-platform suites exercise both happy paths and boundary behavior.
- **Documentation:** The readme links the maintained documentation and hands-on guide, while public protocol and parser types carry implementation-level explanations.
- **Traceability:** A case class can be followed from macroRW or Mirror derivation into a CaseClassReader, through Visitor callbacks driven by JSON or MessagePack bytes, and into round-trip and failure tests.
- **Maintainability:** Format-independent events reduce duplicated traversal, version-specific metaprogramming stays separate, and extensive format tests constrain low-level changes.
- **Educational value:** It shows how one carefully designed protocol can support multiple wire formats, ASTs, and derived object mappings efficiently.

**Inspection record:** commit `87e0b24b8c811e174ebd680839e4edf1e62abe71`, reviewed 2026-08-28 by Codex. Files sampled: `readme.md`, `upickle/core/src/upickle/core/Visitor.scala`, `ujson/src/ujson/ByteArrayParser.scala`, `upack/src/upack/MsgPackReader.scala`, `upickle/implicits/src/upickle/implicits/CaseClassReadWriters.scala`, `upickle/implicits/src-3/upickle/implicits/MacroImplicits.scala`, `upickle/test/src/upickletest/MacroTests.scala`, `LICENSE`. GitHub Linguist label: Scala. LOC exclusions: all test and testSlow modules, benchmarks, upickleReadme/, upickle/core/templates/, documentation and build files.

**License:** [MIT](https://github.com/com-lihaoyi/upickle/blob/87e0b24b8c811e174ebd680839e4edf1e62abe71/LICENSE)

## SDC 4

### [http4s/http4s](https://github.com/http4s/http4s)

**S3 / D4 / C4 → SDC 4**

A purely functional, streaming HTTP toolkit for Scala with protocol types, clients, servers, routing, middleware, codecs, and the Ember network implementation.

**Real-world evidence:** The http4s project publishes a versioned family of core, DSL, client, server, Ember, codec, and integration artifacts for production services on multiple Scala platforms.

**Language evidence:** The HTTP model, codecs, header parsers, routing DSL, client and server algebras, middleware, Ember HTTP/1 and HTTP/2 engine, WebSockets, TLS, and platform integrations are Scala.

**Why study it:** It connects precise HTTP data types and functional service composition to streaming bodies, parsers, sockets, TLS, connection pools, servers, clients, HTTP/2, WebSockets, middleware, and resource-safe shutdown.

**What you can learn:**

- HTTP message modeling, Kleisli and OptionT services, streaming entities, codecs and content negotiation, incremental protocol parsing, server and client resources, connection pooling, TLS, HTTP/2 framing, WebSockets, middleware, cancellation, and cross-platform networking.

**Prerequisites:**

- Advanced Scala, Cats Effect, fs2 streams, higher-kinded types, Resource, HTTP/1.1 and HTTP/2, sockets and TLS, parser state machines, concurrency, and functional service composition.

**Start here:** [`core/shared/src/main/scala/org/http4s/HttpApp.scala`](https://github.com/http4s/http4s/blob/a95ed19a5d377276d1eb98d93897cea45cbad921/core/shared/src/main/scala/org/http4s/HttpApp.scala) — HttpApp and HttpRoutes establish the service model; following a route into EmberServerBuilder and Ember's Parser connects the small functional abstraction to actual sockets, bytes, requests, responses, and lifecycle tests.

**Why this level:**

- **S3:** 28,756 meaningful implementation LOC measured with tokei 14.0.0. Count covers production Scala and Java across core, DSL, client, server, Ember, codecs, and integrations; it excludes tests and support, laws, benchmarks, examples, documentation, rewrite rules, build metadata, and the explicitly marked 7,876-line generated MimeDB.scala.
- **D4:** Advanced functional abstractions, streaming, concurrency, and protocol correctness recur across every server or client path.
- **C4:** Tracing a real request crosses many explicit components and resource boundaries, with shared concerns such as cancellation, logging, metrics, and headers.
- **Placement:** S3/D4/C4 averages to 3.67 and rounds upward, making http4s an SDC 4 project.

**Quality-gate evidence:**

- **Source quality:** Protocol models, service abstractions, parser internals, resource builders, and middleware are separated, with detailed comments at subtle streaming and RFC boundaries.
- **Architecture:** Core defines messages and services; DSL and codecs construct them; clients and servers define resources; Ember implements network protocols; middleware and integrations wrap stable interfaces.
- **Naming and idiom:** HttpApp, HttpRoutes, EntityDecoder, Request, Response, Client.run, EmberServerBuilder, Parser.Request, Shutdown, and WebSocketBuilder2 expose the end-to-end path.
- **Tests:** Protocol laws, header suites, parser chunk-boundary tests, client middleware, server lifecycle, TLS, HTTP/2, WebSocket, connection, resource, platform, and integration suites cover behavior deeply.
- **Documentation:** The README provides modules, supported platforms, setup, examples, version status, and links to extensive concepts, recipes, API, and migration documentation.
- **Traceability:** A request can be followed from HttpRoutes through an HttpApp, Ember server acquisition, incremental parsing, body streaming, response encoding, socket write, and the parser and server suites.
- **Maintainability:** Protocol and effect contracts are reusable, generated MIME data is labeled, optional integrations remain modular, and exhaustive tests isolate regressions at boundaries.
- **Educational value:** It demonstrates how small functional abstractions scale into a full protocol implementation without obscuring network and resource mechanics.

**Inspection record:** commit `a95ed19a5d377276d1eb98d93897cea45cbad921`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `core/shared/src/main/scala/org/http4s/HttpApp.scala`, `core/shared/src/main/scala/org/http4s/Message.scala`, `client/shared/src/main/scala/org/http4s/client/Client.scala`, `ember-core/shared/src/main/scala/org/http4s/ember/core/Parser.scala`, `ember-server/shared/src/main/scala/org/http4s/ember/server/EmberServerBuilder.scala`, `ember-core/shared/src/test/scala/org/http4s/ember/core/ParserSuite.scala`, `LICENSE`. GitHub Linguist label: Scala. LOC exclusions: all test, tests, testing, laws, and testkit modules and source trees, benchmarks, examples/, scalafix/, site and documentation, core/shared/src/main/scala/org/http4s/MimeDB.scala, build files.

**License:** [Apache-2.0](https://github.com/http4s/http4s/blob/a95ed19a5d377276d1eb98d93897cea45cbad921/LICENSE)

### [typelevel/cats-effect](https://github.com/typelevel/cats-effect)

**S3 / D5 / C4 → SDC 4**

Typelevel's pure asynchronous runtime and effect-kernel for resource-safe, cancelable, concurrent Scala applications.

**Real-world evidence:** Typelevel publishes the stable Cats Effect kernel, runtime, standard primitives, laws, and testkit that underpin production libraries and applications across JVM, Scala.js, and Native.

**Language evidence:** The effect type classes, IO algebra and interpreter, fibers, runtime, schedulers, queues, synchronization primitives, test control, metrics, and platform implementations are Scala.

**Why study it:** The repository exposes the machinery beneath IO: an immutable effect algebra, a stack-safe interpreter, cancellation masks, fibers, work-stealing execution, resource safety, structured concurrency, and deterministic testing.

**What you can learn:**

- Effect algebras, referential transparency, trampolining, fibers, structured concurrency, cancellation and finalization, asynchronous callbacks, runtime scheduling, work stealing, atomics, queues and semaphores, Resource, virtual time, laws, and platform runtimes.

**Prerequisites:**

- Expert Scala and functional programming, higher-kinded types, Cats type classes, concurrency, atomics and memory visibility, continuation interpreters, cancellation semantics, thread pools, and law-based testing.

**Start here:** [`core/shared/src/main/scala/cats/effect/IO.scala`](https://github.com/typelevel/cats-effect/blob/3d4486d47a22a40ba33f822cf4adb1eccfdb4feb/core/shared/src/main/scala/cats/effect/IO.scala) — IO defines the user-visible algebra and contracts; IOFiber.scala then interprets its tags, while IORuntime shows how schedulers and shutdown resources execute the resulting fibers.

**Why this level:**

- **S3:** 20,172 meaningful implementation LOC measured with tokei 14.0.0. Count covers production Scala and Java across kernel, core, standard primitives, testkit, platform runtimes, and runtime metrics; test applications, laws and generators, benchmarks, rewrite rules, tests, documentation, and build metadata are excluded.
- **D5:** Expert-level runtime, concurrent-algorithm, memory-model, and type-system concerns are central rather than peripheral.
- **C4:** Many interacting runtime pieces and platform adaptations share lifecycle contracts, though the repository remains one library family rather than a distributed platform.
- **Placement:** S3/D5/C4 averages to 4.00, making Cats Effect an SDC 4 project.

**Quality-gate evidence:**

- **Source quality:** Dense runtime paths document invariants and fast paths, algebra and interpreter concerns stay distinct, and unsafe operations are visibly contained.
- **Architecture:** Kernel type classes define capabilities, IO describes effects, IOFiber interprets them, IORuntime owns schedulers and shutdown, std builds coordination primitives, and testkit supplies controlled execution.
- **Naming and idiom:** IO, IOFiber, Outcome, CancelScope, uncancelable, evalOn, WorkStealingThreadPool, IORuntime, TestControl, Queue, and Supervisor expose operational meaning.
- **Tests:** Law suites, deterministic runtime suites, race and stress tests, platform tests, scheduler tests, primitive contracts, tracing checks, and virtual-time tests cover both semantics and concurrency failures.
- **Documentation:** The README explains the artifact family, IO execution model, resource and concurrency rules, compatibility, performance claims, architecture, and routes to guides and migration material.
- **Traceability:** An IO.flatMap chain can be followed from algebra nodes into IOFiber's run loop, scheduling and cancellation state, completion Outcome, and focused IOFiber and concurrency suites.
- **Maintainability:** Capability interfaces constrain implementations, platform code is partitioned, unsafe runtime ownership is explicit, and a deep law and stress-test matrix protects refactoring.
- **Educational value:** It is a rigorous view of how a high-level pure effect API becomes a practical concurrent runtime.

**Inspection record:** commit `3d4486d47a22a40ba33f822cf4adb1eccfdb4feb`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `core/shared/src/main/scala/cats/effect/IO.scala`, `core/shared/src/main/scala/cats/effect/IOFiber.scala`, `core/shared/src/main/scala/cats/effect/unsafe/IORuntime.scala`, `core/jvm/src/main/scala/cats/effect/unsafe/IORuntimeCompanionPlatform.scala`, `std/shared/src/main/scala/cats/effect/std/Queue.scala`, `tests/shared/src/test/scala/cats/effect/IOFiberSuite.scala`, `LICENSE.txt`. GitHub Linguist label: Scala. LOC exclusions: tests/, laws/, kernel-testkit/, benchmarks/, scalafix/, ioapp-tests/, all src/test/ trees, documentation and build files.

**License:** [Apache-2.0](https://github.com/typelevel/cats-effect/blob/3d4486d47a22a40ba33f822cf4adb1eccfdb4feb/LICENSE.txt)

## SDC 5

### [apache/spark](https://github.com/apache/spark)

**S5 / D5 / C5 → SDC 5**

Apache's unified distributed analytics engine for batch computation, SQL, structured streaming, machine learning, and graph processing.

**Real-world evidence:** The Apache Software Foundation ships Spark releases and documents Scala, Java, Python, and R APIs for production-scale data processing across standalone and cluster resource managers.

**Language evidence:** Spark's execution engine, RDD lineage, scheduling, SQL Catalyst analyzer and optimizer, query execution, streaming, MLlib, GraphX, resource-manager integrations, and connectors are predominantly Scala, with substantial first-party Java APIs and infrastructure.

**Why study it:** Spark exposes an entire distributed data platform: lazy lineage, DAG and task scheduling, shuffle, memory and storage management, fault recovery, query analysis and optimization, code generation, streaming state, cluster backends, and multiple domain libraries.

**What you can learn:**

- Lazy distributed collections, lineage and fault recovery, DAG scheduling, stages and tasks, shuffle and storage, executors, cluster resource managers, Catalyst trees and rules, cost and adaptive query optimization, code generation, streaming state, distributed ML, graph processing, RPC, and compatibility engineering.

**Prerequisites:**

- Expert Scala and Java, distributed systems, concurrency, networking and RPC, storage and serialization, query planning and optimization, JVM internals, fault tolerance, cluster schedulers, streaming semantics, and large multi-module builds.

**Start here:** [`core/src/main/scala/org/apache/spark/rdd/RDD.scala`](https://github.com/apache/spark/blob/024120dc960517021a887b51865220f544340362/core/src/main/scala/org/apache/spark/rdd/RDD.scala) — RDD defines lazy partitions, dependencies, transformations, and actions; following an action through SparkContext and DAGScheduler shows how lineage becomes stages, tasks, shuffle boundaries, execution, and recovery before Catalyst is studied separately.

**Why this level:**

- **S5:** 630,468 meaningful implementation LOC measured with tokei 14.0.0. Conservative count covers checked-in production Scala and Java under 45 non-example src/main roots across common infrastructure, core, SQL, streaming, MLlib, GraphX, connectors, cluster managers, launchers, REPL, and tools. It excludes other first-party language front ends, so the project remains well above S5 without relying on them.
- **D5:** Multiple expert domains are implemented in the main path, and correctness depends on distributed execution, recovery, optimization, storage, concurrency, and JVM behavior.
- **C5:** Spark is a platform-scale distributed system whose important behaviors cross process, network, storage, planning, scheduling, and cluster-manager boundaries.
- **Placement:** S5/D5/C5 triggers the two-dimensions-at-5 rule and makes Apache Spark an SDC 5 project.

**Quality-gate evidence:**

- **Source quality:** Core state machines and planners use explicit domain types and extensive comments; dense distributed paths document invariants, event ownership, and failure handling.
- **Architecture:** SparkContext coordinates driver services; RDD lineage feeds DAGScheduler and task scheduling; executors and storage run work; Catalyst analyzes and optimizes SQL; higher libraries build on the shared engine.
- **Naming and idiom:** RDD, Dependency, DAGScheduler, Stage, TaskSet, BlockManager, LogicalPlan, RuleExecutor, SparkPlan, StateStore, and ExecutorBackend map directly to the runtime model.
- **Tests:** Large unit, integration, distributed, SQL golden, streaming recovery, scheduler, shuffle, storage, connector, compatibility, and cluster-manager suites exercise normal, fault, race, and upgrade behavior.
- **Documentation:** The README routes readers to maintained programming, SQL, streaming, MLlib, deployment, configuration, operations, tuning, and contribution documentation.
- **Traceability:** An RDD action can be followed through SparkContext job submission, DAGScheduler's stage graph and event loop, task scheduling, executor computation and shuffle, completion events, and DAGSchedulerSuite failure scenarios.
- **Maintainability:** Subsystem boundaries, internal APIs, event-driven scheduling, compatibility policies, extensive diagnostics, and broad test matrices support coordinated changes at platform scale.
- **Educational value:** It is a canonical advanced study of how a distributed data abstraction is realized through scheduling, recovery, optimization, and cluster infrastructure.

**Inspection record:** commit `024120dc960517021a887b51865220f544340362`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `core/src/main/scala/org/apache/spark/rdd/RDD.scala`, `core/src/main/scala/org/apache/spark/SparkContext.scala`, `core/src/main/scala/org/apache/spark/scheduler/DAGScheduler.scala`, `sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/optimizer/Optimizer.scala`, `sql/core/src/main/scala/org/apache/spark/sql/classic/Dataset.scala`, `core/src/test/scala/org/apache/spark/scheduler/DAGSchedulerSuite.scala`, `sql/catalyst/src/test/scala/org/apache/spark/sql/catalyst/optimizer/OptimizerSuite.scala`, `LICENSE`. GitHub Linguist label: Scala. LOC exclusions: all src/test/ trees and test modules, examples/src/main/, Python and R front ends, documentation, benchmarks, fixtures, generated test sources, and build files.

**License:** [Apache-2.0](https://github.com/apache/spark/blob/024120dc960517021a887b51865220f544340362/LICENSE)

### [scala/scala3](https://github.com/scala/scala3)

**S5 / D5 / C5 → SDC 5**

The official Scala 3 compiler and language toolchain, including the type checker, transformation pipeline, backends, TASTy, libraries, REPL, documentation, and editor services.

**Real-world evidence:** The Scala organization ships Scala 3 language releases and the compiler, standard library, TASTy tools, REPL, Scaladoc, and presentation components used by the ecosystem.

**Language evidence:** The Scala 3 compiler, standard library additions, TASTy representation, REPL, presentation compiler, language server, Scaladoc, staging, and build bridges are implemented primarily in Scala 3, with small Java interfaces.

**Why study it:** The repository implements a modern language end to end: parsing, name resolution, rich types, inference, implicit search, staging, macros, typed trees, optimization and lowering phases, TASTy serialization, JVM and JavaScript backends, diagnostics, and tooling.

**What you can learn:**

- Compiler phase orchestration, parsing and syntax trees, contexts and symbols, advanced type representation and comparison, inference and implicit search, typed trees, macro staging, desugaring and lowering, phase fusion, TASTy serialization, JVM and JavaScript backends, REPL and editor services, and language conformance testing.

**Prerequisites:**

- Expert Scala 3, programming-language semantics, type theory and inference, compiler architecture, JVM bytecode, JavaScript backends, macros and staging, incremental tooling, serialization formats, and very large codebases.

**Start here:** [`compiler/src/dotty/tools/dotc/Compiler.scala`](https://github.com/scala/scala3/blob/2106c166d34e5451661d1ab812016cf7c9870c80/compiler/src/dotty/tools/dotc/Compiler.scala) — Compiler.scala names and orders the front-end, typing, transformation, serialization, and backend phases; Run.scala shows compilation-unit execution before deeper study of Typer, Types, MegaPhase, or TASTy.

**Why this level:**

- **S5:** 242,131 meaningful implementation LOC measured with tokei 14.0.0. Count covers production Scala and Java in compiler, libraries, TASTy, staging, interfaces, directives parser, REPL, Scaladoc, presentation compiler, language server, TASTy inspector, and sbt bridge; tests, testcases, benchmarks, community builds, scripted fixtures, documentation, and build metadata are excluded.
- **D5:** The main path is an expert compiler implementation whose correctness depends on language semantics, type theory, staging, transformations, serialization, and platform backends.
- **C5:** Scala 3 is a language platform and toolchain; even one compilation crosses many tightly coordinated subsystems and representation changes.
- **Placement:** S5/D5/C5 triggers the two-dimensions-at-5 rule and makes Scala 3 an SDC 5 project.

**Quality-gate evidence:**

- **Source quality:** Compiler phases, contexts, types, and trees have strong internal vocabulary; difficult algorithms carry design comments, invariants, and links to specifications or prior work.
- **Architecture:** Compiler and Run assemble phases; front-end parsing and Typer produce typed trees; mini-phases transform them; TASTy persists typed structure; backends emit code; tools reuse compiler services.
- **Naming and idiom:** Context, Symbol, Type, Denotation, Typer, ProtoType, Phase, MiniPhase, MegaPhase, TastyPickler, GenBCode, and InteractiveCompiler expose compiler concepts directly.
- **Tests:** Positive, negative, run, staging, TASTy, explicit-nulls, initialization, backend, presentation, REPL, documentation, compiler-unit, and regression suites exercise both accepted programs and diagnostics.
- **Documentation:** The README provides build, test, contribution, issue, release, and architecture routes, alongside the language reference, API, internals documentation, and contributor guidance.
- **Traceability:** A source unit can be followed through Compiler phase assembly, Run compilation, parsing and Typer, grouped MegaPhase transformations, TASTy pickling, backend emission, and CompilationTests plus focused conformance cases.
- **Maintainability:** Phase boundaries, explicit context threading, stable typed representations, compatibility tests, diagnostic tests, tooling modules, and a vast conformance corpus support language evolution.
- **Educational value:** It is an advanced reference for how a production language's semantics, compiler pipeline, binary interchange format, runtimes, and developer tools evolve together.

**Inspection record:** commit `2106c166d34e5451661d1ab812016cf7c9870c80`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `compiler/src/dotty/tools/dotc/Compiler.scala`, `compiler/src/dotty/tools/dotc/Run.scala`, `compiler/src/dotty/tools/dotc/typer/Typer.scala`, `compiler/src/dotty/tools/dotc/core/Types.scala`, `compiler/src/dotty/tools/dotc/transform/MegaPhase.scala`, `compiler/src/dotty/tools/dotc/core/tasty/TastyPickler.scala`, `compiler/test/dotty/tools/dotc/CompilationTests.scala`, `LICENSE`. GitHub Linguist label: Scala. LOC exclusions: all test and tests trees, scaladoc-testcases/, presentation-compiler-testcases/, benchmarks, community-build/, sbt scripted fixtures, documentation and build files.

**License:** [Apache-2.0](https://github.com/scala/scala3/blob/2106c166d34e5451661d1ab812016cf7c9870c80/LICENSE)

_Generated from `catalog/scala.json`; do not edit by hand._

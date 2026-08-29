# Swift

10 qualified repositories. Scores assume the learner described in [the SDC rubric](../../docs/sdc.md).

[← All languages](../README.md)

## SDC 1

### [JohnSundell/Files](https://github.com/JohnSundell/Files)

**S1 / D2 / C1 → SDC 1**

A small object-oriented filesystem library that wraps Foundation paths as File and Folder values.

**Real-world evidence:** The repository publishes Swift Package Manager and CocoaPods libraries used by macOS, iOS, Linux, tvOS, and watchOS code.

**Language evidence:** File and folder values, traversal, creation, copying, moving, renaming, deletion, attributes, and Foundation interoperation are implemented in Swift in Sources/Files.swift.

**Why study it:** It turns FileManager's string-heavy API into typed values and sequences while keeping filesystem effects, errors, traversal, and path relationships visible.

**What you can learn:**

- Value-oriented API design, filesystem traversal, Sequence conformance, path relationships, file operations, lazy properties, error modeling, Foundation bridging, and cross-platform conditions.

**Prerequisites:**

- Swift classes and protocols, sequences, optionals and errors, Foundation FileManager, paths, closures, and computed properties.

**Start here:** [`Sources/Files.swift`](https://github.com/JohnSundell/Files/blob/e85f2b4a8dfa0f242889f45236f3867d16e40480/Sources/Files.swift) — The complete implementation introduces shared location behavior before File and Folder specialize creation, traversal, mutation, and metadata.

**Why this level:**

- **S1:** 640 meaningful implementation LOC measured with tokei 14.0.0. Count covers the complete production source, excluding tests, configuration, project files, documentation, and packaging metadata.
- **D2:** Filesystem edge cases add care, but behavior is expressed through familiar Foundation calls and small typed wrappers.
- **C1:** Two related types and shared helpers cover one local filesystem concern without services or plugin boundaries.
- **Placement:** S1/D2/C1 averages to 1.33, placing Files at SDC 1.

**Quality-gate evidence:**

- **Source quality:** Path operations validate location kinds, make mutation explicit, preserve references after moves, and translate Foundation failures into domain errors.
- **Architecture:** A shared Location protocol and internal helpers support File and Folder classes plus sequence-based child traversal.
- **Naming and idiom:** File, Folder, path, name, extension, parent, subfolders, files, create, move, copy, and delete mirror user intent.
- **Tests:** The suite covers lookup, creation, traversal, paths, extensions, reads and writes, copy and move, rename, delete, attributes, errors, equality, and platform behavior.
- **Documentation:** The README teaches common and advanced operations, traversal, errors, testing, installation, and platform support through examples.
- **Traceability:** Creating and moving a file can be followed from Folder helpers through FileManager, path updates, returned values, and temporary-directory tests.
- **Maintainability:** The entire public model is visible in one source file and integration-style tests exercise actual filesystem effects.
- **Educational value:** It shows how a thin wrapper can materially improve domain clarity without hiding the underlying platform.

**Inspection record:** commit `e85f2b4a8dfa0f242889f45236f3867d16e40480`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Package.swift`, `Sources/Files.swift`, `Tests/FilesTests/FilesTests.swift`, `LICENSE`. GitHub Linguist label: Swift. LOC exclusions: Tests/, Configs/.

**License:** [MIT](https://github.com/JohnSundell/Files/blob/e85f2b4a8dfa0f242889f45236f3867d16e40480/LICENSE)

### [pointfreeco/swift-tagged](https://github.com/pointfreeco/swift-tagged)

**S1 / D2 / C1 → SDC 1**

A tiny generic wrapper that gives otherwise identical raw values distinct compile-time identities.

**Real-world evidence:** The repository publishes Swift packages used by applications to prevent identifier and domain-value mixups without runtime overhead.

**Language evidence:** The generic tag wrapper, conditional conformances, literal support, serialization, identifiers, money, and time helpers are implemented in Swift under Sources/.

**Why study it:** One struct demonstrates how Swift's type system, conditional conformances, dynamic members, literals, Codable, collections, and numeric protocols compose into a practical domain tool.

**What you can learn:**

- Phantom types, generic wrappers, conditional protocol conformance, dynamic member lookup, Codable forwarding, literal protocols, numeric protocols, and zero-cost domain modeling.

**Prerequisites:**

- Swift structs and generics, protocols and extensions, key paths, Codable, collections, numeric types, and basic domain modeling.

**Start here:** [`Sources/Tagged/Tagged.swift`](https://github.com/pointfreeco/swift-tagged/blob/6a8517578035408b6c14ccba00ee990a1435515c/Sources/Tagged/Tagged.swift) — The main file defines the wrapper and builds nearly every behavior through conditional conformance to the raw value's protocols.

**Why this level:**

- **S1:** 326 meaningful implementation LOC measured with tokei 14.0.0. Count covers all production package targets, excluding tests, the playground, documentation, and package metadata.
- **D2:** The type-system ideas are moderately unfamiliar, but each forwarding implementation is short and directly testable.
- **C1:** A single value abstraction and two tiny domain helpers have no I/O, services, or runtime coordination.
- **Placement:** S1/D2/C1 averages to 1.33, making Tagged an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** The wrapper stores one raw value, forwards only when constraints permit, and keeps conversions and unsafe coercion explicit.
- **Architecture:** A generic core type gains behavior through focused extensions, with optional money and time targets layered above it.
- **Naming and idiom:** Tagged, Tag, RawValue, rawValue, map, coerced, and conditional conformances state the type-level design plainly.
- **Tests:** Tests cover initialization, protocols, Codable strategies, literals, numeric behavior, dynamic members, optional values, identities, coercion, money, and time.
- **Documentation:** The README develops the motivating bugs, type solution, collisions, features, caveats, installation, and practical examples.
- **Traceability:** A typed identifier can be followed from its type alias into storage, protocol forwarding, encoding, comparison, and focused tests.
- **Maintainability:** One core representation and compiler-enforced conditional extensions keep behavior local and prevent unsupported operations from compiling.
- **Educational value:** It is a compact demonstration of using the compiler to eliminate an entire class of domain mistakes.

**Inspection record:** commit `6a8517578035408b6c14ccba00ee990a1435515c`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Package.swift`, `Sources/Tagged/Tagged.swift`, `Tests/TaggedTests/TaggedTests.swift`, `LICENSE`. GitHub Linguist label: Swift. LOC exclusions: Tests/, Tagged.playground/.

**License:** [MIT](https://github.com/pointfreeco/swift-tagged/blob/6a8517578035408b6c14ccba00ee990a1435515c/LICENSE)

## SDC 2

### [apple/swift-log](https://github.com/apple/swift-log)

**S2 / D2 / C2 → SDC 2**

The Swift server ecosystem's vendor-neutral logging API with pluggable backends and structured metadata.

**Real-world evidence:** The project publishes the Logging package used by Swift libraries and applications to share a stable logging abstraction across backend implementations.

**Language evidence:** Logger values, levels, messages, metadata, backend protocols, global bootstrap, multiplexing, streams, concurrency safety, and testing handlers are Swift under Sources/.

**Why study it:** A familiar Logger API demonstrates protocol-based backends, value semantics around mutable handlers, autoclosure performance, metadata composition, global one-time setup, task context, and concurrency.

**What you can learn:**

- Protocol-based adapters, copy-on-write style handler mutation, log filtering, lazy autoclosures, structured metadata, string interpolation, one-time global bootstrap, task-local context, locks, and Sendable design.

**Prerequisites:**

- Swift protocols and existentials, structs and value semantics, closures and autoclosures, generics, concurrency and Sendable, locks, and logging concepts.

**Start here:** [`Sources/Logging/Logger.swift`](https://github.com/apple/swift-log/blob/47a917767fde0cd7f5b5dfdabbec733d2cb2dd95/Sources/Logging/Logger.swift) — Logger connects levels, messages, metadata, convenience methods, filtering, backend ownership, and log-site calls before global setup is introduced.

**Why this level:**

- **S2:** 3,516 meaningful implementation LOC measured with tokei 14.0.0. Count covers production logging and in-memory logging targets, excluding tests, benchmarks, snippets, documentation, CMake support, and package metadata.
- **D2:** The API uses several modern Swift features, but the logging pipeline and synchronization rules are compact and clearly documented.
- **C2:** A few cohesive modules implement one logging abstraction and bounded extension surface.
- **Placement:** S2/D2/C2 is a balanced SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** Filtering occurs before message materialization, handler mutation is deliberate, bootstrap is guarded, and concurrency contracts are annotated and tested.
- **Architecture:** Logger is a value facade over LogHandler; LoggingSystem chooses a process-wide factory; handlers implement destinations and composition; metadata providers add context.
- **Naming and idiom:** Logger, LogHandler, Level, Message, Metadata, bootstrap, multiplex, label, metadataProvider, and logLevel define the domain.
- **Tests:** Tests cover filtering and laziness, metadata and interpolation, handler mutation, multiplexing, bootstrap rules, concurrency, task-local loggers, streams, no-op and in-memory handlers, and compatibility.
- **Documentation:** The README and generated API docs explain use, backend authoring, metadata, source information, global setup, concurrency, compatibility, and ecosystem packages.
- **Traceability:** An info call can be followed through level filtering, lazy message construction, metadata merge, handler dispatch, multiplexing, and history assertions.
- **Maintainability:** A deliberately small API, backend protocol, semantic-versioning policy, concurrency annotations, and focused tests keep ecosystem compatibility manageable.
- **Educational value:** It is a clean study of designing a shared abstraction whose main value is decoupling producers from implementations.

**Inspection record:** commit `47a917767fde0cd7f5b5dfdabbec733d2cb2dd95`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Package.swift`, `Sources/Logging/Logger.swift`, `Sources/Logging/LoggingSystem.swift`, `Tests/LoggingTests/LoggingTest.swift`, `LICENSE.txt`. GitHub Linguist label: Swift. LOC exclusions: Tests/, Benchmarks/, Snippets/.

**License:** [Apache-2.0](https://github.com/apple/swift-log/blob/47a917767fde0cd7f5b5dfdabbec733d2cb2dd95/LICENSE.txt)

### [apple/swift-system](https://github.com/apple/swift-system)

**S2 / D3 / C2 → SDC 2**

Idiomatic strongly typed Swift interfaces over low-level operating-system calls and currency types.

**Real-world evidence:** The project publishes SystemPackage for Swift libraries and applications that need direct, safer access to platform system interfaces.

**Language evidence:** Typed file descriptors, paths, system strings, errors, permissions, file operations, stat data, IO request types, and Darwin, POSIX, Windows, and WASI mappings are Swift under Sources/System.

**Why study it:** It shows how to wrap C and OS APIs without pretending platforms are identical, preserving raw semantics while adding types, ownership helpers, error mapping, and source-stable Swift interfaces.

**What you can learn:**

- System call wrappers, strongly typed flags and handles, errno mapping, EINTR retry, buffer lifetimes, filesystem paths and strings, platform conditional compilation, availability, ABI and source stability, and unsafe Swift boundaries.

**Prerequisites:**

- Comfortable Swift, C interoperation, pointers and buffers, POSIX and Windows file APIs, errors, option sets, generics, platform compilation, and systems concepts.

**Start here:** [`Sources/System/FileDescriptor.swift`](https://github.com/apple/swift-system/blob/1b452c2996c677d8e435bf0b766fc927176d8c77/Sources/System/FileDescriptor.swift) — FileDescriptor builds typed access modes and options around a raw handle before operation files connect them to system calls and lifetime helpers.

**Why this level:**

- **S2:** 8,797 meaningful implementation LOC measured with tokei 14.0.0. Count covers production SystemPackage and C shims, excluding tests, proposals, documentation, CMake support, and package metadata.
- **D3:** Low-level interfaces require precision, but wrappers are repetitive, documented, and organized by operating-system concept.
- **C2:** Several related modules expose one low-level system interface layer with no service orchestration.
- **Placement:** S2/D3/C2 averages to 2.33, placing Swift System at SDC 2.

**Quality-gate evidence:**

- **Source quality:** Raw values, platform constants, retry policy, ownership responsibility, availability, and unsafe buffer scopes are visible and extensively documented.
- **Architecture:** Strongly typed currency types and option sets wrap narrow C shims; operation files provide platform-specific calls while FilePath and SystemString own path representation.
- **Naming and idiom:** FileDescriptor, FilePath, Errno, FilePermissions, OpenOptions, retryOnInterrupt, closeAfter, read, writeAll, and Stat map directly to system concepts.
- **Tests:** Cross-platform tests cover paths and syntax, file operations, descriptors, permissions, errors, stat data, strings, mocking, temporary paths, Windows behavior, I/O requests, and visibility.
- **Documentation:** The README defines platform philosophy, usage, supported systems, source-stability rules, toolchains, branching, and API documentation.
- **Traceability:** Opening and writing a file can be followed from typed path and flags through platform constants and system-call wrappers, errno translation, lifetime cleanup, and operation tests.
- **Maintainability:** Generated availability, explicit platform branches, narrow C modules, source-stability rules, and multi-platform CI contain a difficult compatibility surface.
- **Educational value:** It teaches how to make unsafe platform power more expressive without erasing the semantics learners need to understand.

**Inspection record:** commit `1b452c2996c677d8e435bf0b766fc927176d8c77`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Package.swift`, `Sources/System/FileDescriptor.swift`, `Sources/System/FilePath/FilePath.swift`, `Tests/SystemTests/FileOperationsTest.swift`, `LICENSE.txt`. GitHub Linguist label: Swift. LOC exclusions: Tests/, Proposals/, cmake/.

**License:** [Apache-2.0 WITH Swift-exception](https://github.com/apple/swift-system/blob/1b452c2996c677d8e435bf0b766fc927176d8c77/LICENSE.txt)

## SDC 3

### [Alamofire/Alamofire](https://github.com/Alamofire/Alamofire)

**S2 / D3 / C3 → SDC 3**

An HTTP networking library for Apple platforms built over URLSession with fluent, async, Combine, streaming, and WebSocket APIs.

**Real-world evidence:** The repository releases Alamofire through Swift Package Manager and CocoaPods for production iOS, macOS, tvOS, watchOS, and visionOS applications.

**Language evidence:** Session management, requests, uploads, downloads, streams, WebSockets, serialization, validation, authentication, retries, trust evaluation, reachability, and event monitoring are Swift under Source/.

**Why study it:** It turns URLSession's delegate model into explicit request state, queues, serializers, validators, interceptors, authentication refresh, trust policy, retries, events, and several user-facing concurrency styles.

**What you can learn:**

- Request state machines, URLSession delegation, concurrency queues, async and await, Combine, serializers and validators, uploads and downloads, WebSockets and streams, retries, authentication, TLS trust, and event monitoring.

**Prerequisites:**

- Swift closures and generics, structured concurrency, Foundation URLSession, HTTP, TLS basics, state machines, dispatch queues, streams, and testing asynchronous code.

**Start here:** [`Source/Core/Session.swift`](https://github.com/Alamofire/Alamofire/blob/0455bfb650893e86ad07ace16e5f2d36dadf46f4/Source/Core/Session.swift) — Session owns URLSession, request creation, delegate routing, root queues, interceptors, trust, lifecycle events, cancellation, and cleanup.

**Why this level:**

- **S2:** 9,287 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production Swift under Source, excluding tests, examples, resources, generated documentation, project files, and packaging metadata.
- **D3:** Networking and concurrency rules recur, but URLSession provides the transport and the library names its state transitions clearly.
- **C3:** Several substantial features cooperate through a common request lifecycle within one library.
- **Placement:** S2/D3/C3 averages to 2.67, which rounds to SDC 3.

**Quality-gate evidence:**

- **Source quality:** Request states, protected mutation, queue boundaries, delegate ownership, retry decisions, serializer ordering, cancellation, and completion are explicit.
- **Architecture:** Session creates Request subclasses and maps URLSession tasks; delegates report transport events; serializers, validators, interceptors, monitors, trust evaluators, and reachability provide focused extensions.
- **Naming and idiom:** Session, Request, DataRequest, DownloadRequest, UploadRequest, DataStreamRequest, interceptor, retrier, serializer, validator, and event monitor form a coherent model.
- **Tests:** Extensive tests cover sessions, requests, delegates, uploads, downloads, streaming, WebSockets, serialization, validation, retries, authentication, trust, reachability, concurrency, memory leaks, and regressions.
- **Documentation:** The README, API docs, migration guides, usage guides, advanced examples, and release history explain architecture and every feature family.
- **Traceability:** A data request can be followed from Session construction through task mapping and delegate events, validation and serialization queues, retry or completion, async response delivery, and tests.
- **Maintainability:** Feature protocols and Request subclasses isolate concerns, while state protection and a broad asynchronous test suite guard the shared lifecycle.
- **Educational value:** It is a readable production example of converting callback-heavy platform APIs into a coherent modern Swift library.

**Inspection record:** commit `0455bfb650893e86ad07ace16e5f2d36dadf46f4`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Package.swift`, `Source/Core/Session.swift`, `Source/Core/Request.swift`, `Tests/SessionTests.swift`, `LICENSE`. GitHub Linguist label: Swift. LOC exclusions: Tests/, Example/, Documentation/, docs/.

**License:** [MIT](https://github.com/Alamofire/Alamofire/blob/0455bfb650893e86ad07ace16e5f2d36dadf46f4/LICENSE)

### [vapor/vapor](https://github.com/vapor/vapor)

**S3 / D3 / C3 → SDC 3**

A server-side Swift web framework built on SwiftNIO with routing, middleware, content, authentication, sessions, clients, and operational integrations.

**Real-world evidence:** The repository publishes the Vapor package used to build and run production HTTP and WebSocket services in Swift.

**Language evidence:** Application lifecycle, routing, requests and responses, middleware, content coding, authentication, sessions, clients, servers, WebSockets, validation, views, caching, tracing, metrics, and testing are Swift under Sources/.

**Why study it:** It shows how a framework composes a low-level evented network stack into application lifecycle, typed routing, requests, middleware, content, authentication, sessions, observability, and test ergonomics.

**What you can learn:**

- Framework application lifecycle, typed routing, middleware chains, HTTP request and response modeling, content negotiation, authentication, sessions, WebSockets, structured concurrency, dependency storage, logging, metrics, tracing, and testing.

**Prerequisites:**

- Comfortable Swift and concurrency, HTTP and WebSockets, SwiftNIO basics, Codable, dependency injection, middleware, authentication, sessions, and server application design.

**Start here:** [`Sources/Vapor/Application.swift`](https://github.com/vapor/vapor/blob/86ab4300efa1b3e270eeba2ca4b253998b734669/Sources/Vapor/Application.swift) — Application owns environment, event loops, storage, lifecycle, services, startup, running, and ordered shutdown, providing the framework map.

**Why this level:**

- **S3:** 13,509 meaningful implementation LOC measured with tokei 14.0.0. Count covers production framework, testing support, and macros, excluding tests, performance harnesses, development server examples, documentation, and package metadata.
- **D3:** Concurrency and framework contracts matter, while most transport depth is delegated to SwiftNIO and components are conventionally structured.
- **C3:** Many framework capabilities cooperate through one application container and request lifecycle.
- **Placement:** S3/D3/C3 makes Vapor a balanced SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** Lifecycle ownership, thread-safe storage, request mutation, body modes, async boundaries, route metadata, and shutdown order are explicit and documented.
- **Architecture:** Application stores configured providers and lifecycle handlers; routing and middleware turn NIO HTTP traffic into Request and Response values; focused modules add content, auth, sessions, clients, servers, views, caches, and telemetry.
- **Naming and idiom:** Application, Request, Response, Route, RoutesBuilder, Middleware, Content, Abort, LifecycleHandler, storage, and withApp expose framework roles.
- **Tests:** The suite covers routing, middleware, requests, responses, content, streams, servers, TLS, WebSockets, clients, auth, sessions, validation, caches, views, errors, observability, macros, and shutdown.
- **Documentation:** The README and maintained documentation cover setup, async APIs, routing, content, databases, authentication, middleware, testing, deployment, packages, and contributor workflows.
- **Traceability:** An HTTP route can be followed from registration through matcher parameters, middleware, Request storage and body handling, async handler, response encoding, NIO write, and route tests.
- **Maintainability:** Application storage keys and protocol-based providers isolate features, while lifecycle rules and full-stack tests protect framework integration.
- **Educational value:** It is a strong intermediate framework study because abstractions are rich but the full request path remains visible.

**Inspection record:** commit `86ab4300efa1b3e270eeba2ca4b253998b734669`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Package.swift`, `Sources/Vapor/Application.swift`, `Sources/Vapor/Request/Request.swift`, `Tests/VaporTests/RouteTests.swift`, `LICENSE`. GitHub Linguist label: Swift. LOC exclusions: Tests/, Performance/, Sources/Development/.

**License:** [MIT](https://github.com/vapor/vapor/blob/86ab4300efa1b3e270eeba2ca4b253998b734669/LICENSE)

## SDC 4

### [apple/swift-nio](https://github.com/apple/swift-nio)

**S4 / D4 / C4 → SDC 4**

A cross-platform high-performance event-driven networking framework for building protocol servers and clients in Swift.

**Real-world evidence:** The project publishes the core SwiftNIO packages that underpin production server frameworks, protocol libraries, and network clients across the Swift ecosystem.

**Language evidence:** Event loops, channels and pipelines, futures, byte buffers, sockets, selectors, bootstraps, HTTP/1, WebSockets, TLS abstractions, async sequences, and filesystem APIs are primarily Swift under Sources/.

**Why study it:** It makes asynchronous systems mechanics explicit: selector threads, event-loop confinement, channels, handler pipelines, byte buffers, promises, backpressure, bootstraps, protocol codecs, and modern async bridges.

**What you can learn:**

- Nonblocking I/O, event loops and thread confinement, channels and handler pipelines, futures and promises, byte buffers, backpressure, socket bootstraps, HTTP and WebSocket codecs, async sequences, filesystems, performance, and portability.

**Prerequisites:**

- Advanced Swift and generics, structured and callback concurrency, sockets and readiness APIs, protocol state machines, memory and buffer management, threads and atomics, HTTP, performance engineering, and large-library navigation.

**Start here:** [`Sources/NIOCore/Channel.swift`](https://github.com/apple/swift-nio/blob/a931f2c1de8dd49381ce3bf2e279d033f68d8865/Sources/NIOCore/Channel.swift) — Channel and ChannelPipeline define ownership and event flow; then EventLoop explains the execution model that makes handlers safe and nonblocking.

**Why this level:**

- **S4:** 88,031 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production Swift and native shims under Sources, excluding tests, integration and performance harnesses, snippets, development tools, documentation, generated files, and package metadata.
- **D4:** Concurrency, ownership, low-level networking, and performance invariants are pervasive across central abstractions.
- **C4:** Many interdependent library products form a networking platform, though deployment remains within client and server processes built by consumers.
- **Placement:** S4/D4/C4 makes SwiftNIO an SDC 4 project.

**Quality-gate evidence:**

- **Source quality:** Event-loop preconditions, ownership, Sendable boundaries, state machines, promises, buffer indices, backpressure, and performance-sensitive branches are explicit and asserted.
- **Architecture:** NIOCore defines abstractions; NIOPosix supplies selector-driven sockets; embedded implementations enable deterministic tests; protocol, TLS, concurrency, Foundation, and filesystem modules build on the core.
- **Naming and idiom:** EventLoop, Channel, ChannelPipeline, ChannelHandler, ByteBuffer, EventLoopFuture, EventLoopPromise, Bootstrap, Selector, and writability define the runtime model.
- **Tests:** Large unit, integration, allocation, performance, crash, concurrency, protocol, filesystem, sanitizer, and platform suites cover abstractions, transports, codecs, edge cases, and regressions.
- **Documentation:** The conceptual README, API docs, public-API policy, migration guides, performance guidance, examples, and ecosystem maps explain both use and internals.
- **Traceability:** A socket read can be followed from selector readiness through an EventLoop-owned Channel, inbound pipeline handlers and decoders, backpressure state, user callback or async sequence, and embedded or POSIX tests.
- **Maintainability:** Strict event-loop rules, protocol boundaries, embedded test doubles, compatibility contracts, allocation benchmarks, and modular packages constrain a performance-sensitive system.
- **Educational value:** It is an advanced source for understanding the execution machinery beneath modern Swift servers rather than only consuming async APIs.

**Inspection record:** commit `a931f2c1de8dd49381ce3bf2e279d033f68d8865`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Package.swift`, `Sources/NIOCore/Channel.swift`, `Sources/NIOCore/EventLoop.swift`, `Tests/NIOCoreTests/CustomChannelTests.swift`, `LICENSE.txt`. GitHub Linguist label: Swift. LOC exclusions: Tests/, IntegrationTests/, Benchmarks/, Snippets/, dev/, docs/.

**License:** [Apache-2.0](https://github.com/apple/swift-nio/blob/a931f2c1de8dd49381ce3bf2e279d033f68d8865/LICENSE.txt)

### [realm/SwiftLint](https://github.com/realm/SwiftLint)

**S4 / D3 / C4 → SDC 4**

A configurable Swift style and static-analysis tool with hundreds of rules, autocorrection, baselines, reporters, and build integrations.

**Real-world evidence:** The repository releases the SwiftLint command, frameworks, package plugins, and build-tool integrations used by Swift projects and CI systems.

**Language evidence:** Rule protocols and implementations, SwiftSyntax and SourceKit analysis, configuration, corrections, baselines, caching, reporters, file discovery, command execution, plugins, and macros are Swift under Source/ and Plugins/.

**Why study it:** It analyzes its own language using protocol-oriented rules, syntax trees, compiler services, configuration graphs, generated registries, corrections, caching, reporters, plugins, and a substantial CLI.

**What you can learn:**

- Static analysis, syntax visitors, SourceKit integration, rule protocols and registries, configuration merging, diagnostics and source locations, autocorrection, baselines, caching, reporters, package plugins, macros, and command-line architecture.

**Prerequisites:**

- Advanced Swift, SwiftSyntax and AST concepts, compiler tooling, protocols and generics, concurrency, YAML configuration, source ranges and rewriting, command-line tools, build plugins, and large-rule-set navigation.

**Start here:** [`Source/SwiftLintFramework/Models/Linter.swift`](https://github.com/realm/SwiftLint/blob/29d5c2b0484c9cf52d9745402160e59b7741b1db/Source/SwiftLintFramework/Models/Linter.swift) — Linter connects files and syntax, configured rule storage, collectors, corrections, violation production, command directives, and benchmark timing.

**Why this level:**

- **S4:** 61,065 meaningful implementation LOC measured with tokei 14.0.0. Count covers production frameworks, built-in rules, command, macros, and plugins, excluding tests and fixtures, platform packaging, assets, build tooling, generated test sources, documentation, and dependency metadata.
- **D3:** Compiler tooling is specialized, but rule implementations share well-defined protocols and reusable visitor and configuration machinery.
- **C4:** Many extensible subsystems and rules interact across analysis, correction, configuration, output, and delivery surfaces.
- **Placement:** S4/D3/C4 averages to 3.67, which rounds to SDC 4.

**Quality-gate evidence:**

- **Source quality:** Rule capabilities, correction modes, configuration state, source regions, syntax and SourceKit paths, cache keys, and concurrency boundaries use explicit types and protocols.
- **Architecture:** Core defines rules and models; Framework handles files, configuration, linting and correction; BuiltInRules supplies rule families; the command, reporters, plugins, macros, and analyzer extensions provide delivery surfaces.
- **Naming and idiom:** Rule, RuleRegistry, Linter, SwiftLintFile, StyleViolation, Correction, Configuration, Region, Reporter, baseline, and opt-in rule define the tool vocabulary.
- **Tests:** Large generated and focused suites cover every rule and correction, configuration, baselines, caching, file graphs, SourceKit failures, reporters, commands, plugins, macros, integration cases, and regressions.
- **Documentation:** The README, generated Rules reference, configuration examples, custom-rule guidance, baseline and analyzer docs, build integrations, changelog, and contributor guide are extensive.
- **Traceability:** A rule violation can be followed from configured registry through syntax collection and Linter dispatch, region and command filtering, severity and baseline handling, reporter output or correction, and rule tests.
- **Maintainability:** Protocol families, generated registries and docs, shared configurations, isolated rule tests, semantic versioning, and multiple integration suites contain a wide feature surface.
- **Educational value:** It is an advanced but approachable study of a language tool implemented in the language and tested rule by rule.

**Inspection record:** commit `29d5c2b0484c9cf52d9745402160e59b7741b1db`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Package.swift`, `Source/SwiftLintCore/Models/RuleRegistry.swift`, `Source/SwiftLintFramework/Models/Linter.swift`, `Tests/CoreTests/RuleTests.swift`, `LICENSE`. GitHub Linguist label: Swift. LOC exclusions: Tests/, Platforms/, assets/, bazel/, tools/.

**License:** [MIT](https://github.com/realm/SwiftLint/blob/29d5c2b0484c9cf52d9745402160e59b7741b1db/LICENSE)

## SDC 5

### [mozilla-mobile/firefox-ios](https://github.com/mozilla-mobile/firefox-ios)

**S5 / D4 / C5 → SDC 5**

The Firefox and Focus browser products for iOS, including tab management, synchronization, privacy features, browser UI, and reusable component packages.

**Real-world evidence:** The repository builds Mozilla's production Firefox and Focus applications distributed through Apple's App Store.

**Language evidence:** Browser lifecycle, tabs and windows, WebKit integration, navigation, accounts and sync, history, bookmarks, passwords, downloads, privacy, search, settings, telemetry, extensions, and shared component packages are primarily Swift.

**Why study it:** It exposes a large browser product within iOS constraints: WebKit lifecycle, multiwindow tab state, accounts and sync, history and passwords, downloads, privacy, experiments, telemetry, reusable packages, and two related apps.

**What you can learn:**

- Large iOS application architecture, WebKit embedding, tab and window state, coordinators and stores, browser navigation, accounts and sync, data persistence, privacy and content blocking, downloads, feature flags and experiments, telemetry, accessibility, and product modularization.

**Prerequisites:**

- Expert Swift and iOS, UIKit and WebKit, structured concurrency, state management, databases, networking, browser concepts, accounts and sync, privacy, accessibility, telemetry, testing, and very large monorepo navigation.

**Start here:** [`firefox-ios/Client/TabManagement/TabManagerImplementation.swift`](https://github.com/mozilla-mobile/firefox-ios/blob/b0799c34c313be9e832b749794f91277a9ce57eb/firefox-ios/Client/TabManagement/TabManagerImplementation.swift) — TabManagerImplementation connects windows, tabs, WebKit views, private state, persistence, restoration, downloads, delegates, telemetry, and selection behavior at the browser's center.

**Why this level:**

- **S5:** 255,137 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party Firefox, Focus, BrowserKit, and shared Swift packages, excluding tests and mocks, Rust component bindings, fixtures, archived scripts, assets, translations, large data files, documentation, generated content, and dependency metadata.
- **D4:** Many platform and product invariants recur, though core browser engine execution is delegated to WebKit and Rust components.
- **C5:** The monorepo coordinates many product surfaces and external systems across windows, extensions, application modes, and long-lived user data.
- **Placement:** S5/D4/C5 has two dimensions at 5 and therefore requires SDC 5.

**Quality-gate evidence:**

- **Source quality:** Window and tab ownership, main-actor boundaries, persistence, feature flags, privacy state, navigation decisions, telemetry, and lifecycle events use explicit protocols and domain types.
- **Architecture:** Application and scene lifecycles compose coordinators, store and middleware features, tab and window managers, BrowserKit packages, profile services, WebKit delegates, sync components, and reusable UI systems for Firefox and Focus.
- **Naming and idiom:** Tab, TabManager, WindowManager, BrowserCoordinator, Profile, BrowserViewController, feature flag, middleware, private mode, and restoration expose the browser domain.
- **Tests:** Large client, component, snapshot, UI, integration, middleware, tab, coordinator, account, sync, privacy, download, telemetry, and regression suites cover both products and shared packages.
- **Documentation:** The README, contributor setup, architecture decision records, package docs, testing guides, accessibility practices, security policy, and inline rationale support ownership.
- **Traceability:** Opening and selecting a tab can be followed from browser actions through coordinator and store or manager state, WebKit construction and navigation, persistence and restoration, UI updates, telemetry, and tab-manager tests.
- **Maintainability:** Protocol-driven services, coordinators, state stores and middleware, feature packages, window scoping, dependency containers, ADRs, and extensive tests contain product breadth.
- **Educational value:** It is an expert source for studying how a long-lived consumer app balances platform constraints, modularity, privacy, and rapid product change.

**Inspection record:** commit `b0799c34c313be9e832b749794f91277a9ce57eb`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Package.swift`, `firefox-ios/Client/Application/AppDelegate.swift`, `firefox-ios/Client/TabManagement/TabManagerImplementation.swift`, `firefox-ios/firefox-ios-tests/Tests/ClientTests/TabManagement/TabManagerTests.swift`, `LICENSE`. GitHub Linguist label: Swift. LOC exclusions: **/*test*, test-fixtures/, MozillaRustComponents/, archived-scripts/, docs/, *.xcassets, *.strings, *.json, Mocks/.

**License:** [MPL-2.0](https://github.com/mozilla-mobile/firefox-ios/blob/b0799c34c313be9e832b749794f91277a9ce57eb/LICENSE)

### [signalapp/Signal-iOS](https://github.com/signalapp/Signal-iOS)

**S5 / D5 / C5 → SDC 5**

The complete Signal private messenger for iPhone and iPad, including encrypted messages, calls, groups, media, backups, and platform integration.

**Real-world evidence:** The repository builds the production Signal iOS application distributed to users for private communication.

**Language evidence:** Application lifecycle, encrypted messaging, identity and key management, contacts, conversations, attachments, calls, groups, backups, storage, networking, notifications, UI, and extensions are principally Swift across Signal, SignalServiceKit, and SignalUI.

**Why study it:** It combines a security-critical messaging domain with key and identity lifecycle, durable local state, queued delivery, attachments, groups, calls, backups, push notifications, complex UI, migrations, and platform extensions.

**What you can learn:**

- Security-critical mobile architecture, encrypted messaging workflows, identity and key state, durable message queues, database transactions and migrations, attachments and backups, calling, groups, networking, push notifications, app lifecycle, extensions, concurrency, and privacy engineering.

**Prerequisites:**

- Expert Swift and iOS, cryptographic protocol concepts, databases and migrations, networking and queues, concurrency, UIKit, media and calling, background execution, secure storage, threat modeling, performance, and very large-codebase navigation.

**Start here:** [`SignalServiceKit/Messages/MessageSender.swift`](https://github.com/signalapp/Signal-iOS/blob/eec0a2f587b49082efdb5a4dc1e2a491fd52144f/SignalServiceKit/Messages/MessageSender.swift) — MessageSender connects persisted outgoing messages to recipient state, encryption, attachments, queues, network requests, retries, errors, and completion across the product.

**Why this level:**

- **S5:** 497,732 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party app, extensions, service kit, and UI implementation, excluding tests, CocoaPods, third-party code, generated protocol files, assets, translations, large data files, scripts, and project metadata.
- **D5:** Security and correctness depend on subtle interactions among untrusted networks, persistent state, cryptographic sessions, background execution, and user-visible lifecycle.
- **C5:** Many runtime components and external systems coordinate long-lived encrypted state across devices, accounts, groups, and application processes.
- **Placement:** S5/D5/C5 requires SDC 5.

**Quality-gate evidence:**

- **Source quality:** Security and state transitions use explicit transaction, recipient, job, request, and error types, with comments concentrated around protocol, privacy, recovery, and migration invariants.
- **Architecture:** The app and extensions build on SignalServiceKit for domain, storage, network, jobs, crypto bindings, backups, and notifications, while SignalUI and feature modules compose the iOS experience.
- **Naming and idiom:** TSMessage, SignalRecipient, MessageSender, job queue, thread, interaction, attachment, identity key, session, group, backup, and AppLaunch define the product model.
- **Tests:** Extensive unit and integration suites cover messaging, recipients, storage, migrations, networking, registration, groups, backups, attachments, calls, notifications, cryptographic integration, UI models, and regressions.
- **Documentation:** Build and maintenance guides, security policy, inline protocol commentary, architecture-oriented names, and linked Signal specifications provide essential context.
- **Traceability:** An outgoing message can be followed from UI and persisted interaction through job enqueue, attachment preparation, recipient and session lookup, encryption, network submission, retry or failure state, delivery updates, and tests.
- **Maintainability:** Transaction-scoped services, dependency shims, durable job records, migrations, feature modules, generated protocol boundaries, and broad regression suites support continuous security-sensitive evolution.
- **Educational value:** It is an expert study of a real privacy product where architecture must preserve trust across every layer.

**Inspection record:** commit `eec0a2f587b49082efdb5a4dc1e2a491fd52144f`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Podfile`, `Signal/AppLaunch/AppDelegate.swift`, `SignalServiceKit/Messages/MessageSender.swift`, `Signal/test/AppDelegateTest.swift`, `LICENSE`. GitHub Linguist label: Swift. LOC exclusions: Pods/, ThirdParty/, **/test/, **/tests/, Protos/, *.xcassets, *.strings, *.json.

**License:** [AGPL-3.0-only](https://github.com/signalapp/Signal-iOS/blob/eec0a2f587b49082efdb5a4dc1e2a491fd52144f/LICENSE)

_Generated from `catalog/swift.json`; do not edit by hand._

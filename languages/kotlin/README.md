# Kotlin

10 qualified repositories. Scores assume the learner described in [the SDC rubric](../../docs/sdc.md).

[← All languages](../README.md)

## SDC 1

### [JakeWharton/picnic](https://github.com/JakeWharton/picnic)

**S1 / D2 / C1 → SDC 1**

A compact Kotlin multiplatform library for building HTML-like tables and rendering them as aligned text.

**Real-world evidence:** The repository publishes versioned Picnic artifacts and documents both a Kotlin DSL and Java/Kotlin builder API for application output.

**Language evidence:** The table model, builder and Kotlin DSL, span-aware layout, border calculation, and text rendering are implemented in Kotlin under picnic/src/commonMain.

**Why study it:** Six production files connect a friendly type-safe DSL to a nontrivial but bounded layout problem involving styles, borders, padding, Unicode width, and row and column spans.

**What you can learn:**

- Kotlin DSL markers, receiver lambdas, builder APIs, interface delegation, immutable models, style inheritance, grid layout, span accounting, text alignment, and focused rendering tests.

**Prerequisites:**

- Kotlin classes and interfaces, lambdas with receivers, nullable values, collections, delegated interfaces, basic terminal text layout, and unit tests.

**Start here:** [`picnic/src/commonMain/kotlin/com/jakewharton/picnic/dsl.kt`](https://github.com/JakeWharton/picnic/blob/bc8832efb604ecdd80abedc0648fdb3ca813d714/picnic/src/commonMain/kotlin/com/jakewharton/picnic/dsl.kt) — The DSL turns nested table declarations into the model that textLayout.kt measures and renders, giving the shortest complete path from public API to output tests.

**Why this level:**

- **S1:** 1,012 meaningful implementation LOC measured with tokei 14.0.0. Count covers all production Kotlin under picnic/src/commonMain and excludes tests, the sample application, documentation, and build metadata.
- **D2:** Layout carries and inherited styles add real edge cases, but the algorithms are explicit and contained in a few well-named files.
- **C1:** There is no persistence, networking, plugin system, or process boundary; a render can be traced locally from DSL to model to canvas.
- **Placement:** S1/D2/C1 averages to 1.33, making Picnic an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** The DSL, model, layout, border, and rendering concerns are separated cleanly, with direct transformations and explicit invariants.
- **Architecture:** A small builder and DSL produce immutable table data, which layout objects measure before the text renderer draws borders and cell content.
- **Naming and idiom:** TableDsl, PositionedCell, SimpleLayout, canonicalStyle, measureWidth, and renderText reveal the pipeline while demonstrating idiomatic receiver lambdas and delegation.
- **Tests:** Common and JVM suites cover the DSL, Java builder, alignment, sizing, border combinations, row spans, column spans, holes, and representative complete tables.
- **Documentation:** The README develops the feature set through rendered examples and includes a realistic styled-table example, setup, and API links.
- **Traceability:** A cell declaration can be followed through CellDslImpl into positioned model data, width and height measurement, canvas drawing, and exact multiline assertions.
- **Maintainability:** The production surface is tiny, multiplatform logic is centralized, names mirror table concepts, and output-focused tests constrain layout regressions.
- **Educational value:** It is an approachable demonstration that a concise Kotlin DSL can front a complete, testable domain model rather than hide the implementation.

**Inspection record:** commit `bc8832efb604ecdd80abedc0648fdb3ca813d714`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `picnic/src/commonMain/kotlin/com/jakewharton/picnic/dsl.kt`, `picnic/src/commonMain/kotlin/com/jakewharton/picnic/model.kt`, `picnic/src/commonMain/kotlin/com/jakewharton/picnic/textLayout.kt`, `picnic/src/commonTest/kotlin/com/jakewharton/picnic/CellSpanTest.kt`, `picnic/src/commonTest/kotlin/com/jakewharton/picnic/DslTest.kt`, `LICENSE.txt`. GitHub Linguist label: Kotlin. LOC exclusions: picnic/src/commonTest/, picnic/src/jvmTest/, sample/, build and documentation files.

**License:** [Apache-2.0](https://github.com/JakeWharton/picnic/blob/bc8832efb604ecdd80abedc0648fdb3ca813d714/LICENSE.txt)

### [Kotlin/kotlinx-cli](https://github.com/Kotlin/kotlinx-cli)

**S1 / D2 / C1 → SDC 1**

JetBrains' compact multiplatform command-line parser, preserved as an explicitly obsolete but stable study of declarative CLI design.

**Real-world evidence:** The repository published kotlinx-cli artifacts for JVM, Native, and other Kotlin targets; its README now states plainly that the experimental library is obsolete and effectively unmaintained.

**Language evidence:** Option and argument descriptors, delegated values, parsing state, prefix styles, subcommands, help generation, and platform exits are implemented in Kotlin multiplatform source sets.

**Why study it:** Its small source makes option declaration, delegated result values, token scanning, subcommand recursion, defaults, validation, and help generation visible in one pass.

**What you can learn:**

- Property delegates, generic argument types, declarative option descriptors, prefix grammars, positional queues, subcommands, multiplatform expect/actual functions, parsing errors, and contract-oriented tests.

**Prerequisites:**

- Kotlin generics, property delegation, mutable collections, inheritance, arrays, command-line conventions, and basic multiplatform source sets.

**Start here:** [`core/commonMain/src/ArgParser.kt`](https://github.com/Kotlin/kotlinx-cli/blob/32112b630b3f1e01c2b446173410be895d456e5e/core/commonMain/src/ArgParser.kt) — ArgParser owns declarations, parsing state, option recognition, positional assignment, subcommand dispatch, validation, and help termination, so the library's full control flow is concentrated here.

**Why this level:**

- **S1:** 928 meaningful implementation LOC measured with tokei 14.0.0. Count covers common, JVM, JS, and Native production source sets in core and excludes tests, documentation, and build metadata.
- **D2:** The type transformations and parsing states require attention, but they use familiar collections and explicit branches without advanced algorithms or concurrency.
- **C1:** All behavior lives in one cohesive module and can be followed without external services, persistence, or runtime plugins.
- **Placement:** S1/D2/C1 averages to 1.33, making kotlinx-cli an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** Descriptors, option transformations, positional values, parser control flow, and platform exits are separated while keeping state changes explicit.
- **Architecture:** Common source defines the parser and value model; three tiny platform files supply process termination behavior.
- **Naming and idiom:** ArgParser, ArgumentsQueue, ParsingValue, ValueOrigin, declaredOptions, and strictSubcommandOptionsOrder make parser responsibilities and state visible.
- **Tests:** Focused suites cover options, positionals, GNU and JVM prefixes, defaults, required and repeated values, help, errors, and recursive subcommands.
- **Documentation:** The README explains the obsolete status first, then preserves setup, entity types, examples, generated help, and subcommand behavior.
- **Traceability:** A declared option can be followed through its descriptor, parser map, token match, typed conversion, delegated value, and a directly corresponding OptionsTests case.
- **Maintainability:** The inspected revision is internally coherent and broadly tested, but maintenance has ended; the entry recommends it for source study, not as a new production dependency.
- **Educational value:** It provides a compact historical example of a typed declarative parser while teaching learners to distinguish source-study value from dependency advice.

**Inspection record:** commit `32112b630b3f1e01c2b446173410be895d456e5e`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `core/commonMain/src/ArgParser.kt`, `core/commonMain/src/Options.kt`, `core/commonMain/src/ArgType.kt`, `core/commonTest/src/OptionsTests.kt`, `core/commonTest/src/SubcommandsTests.kt`, `LICENSE`. GitHub Linguist label: Kotlin. LOC exclusions: core/commonTest/, README.md, Gradle build files.

**License:** [Apache-2.0](https://github.com/Kotlin/kotlinx-cli/blob/32112b630b3f1e01c2b446173410be895d456e5e/LICENSE)

## SDC 2

### [cashapp/turbine](https://github.com/cashapp/turbine)

**S1 / D3 / C2 → SDC 2**

A small multiplatform testing library that turns Kotlin Flow emissions, completion, and failures into explicit ordered assertions.

**Real-world evidence:** Cash App publishes the versioned Turbine testing artifact and documents stable Flow-testing APIs used from ordinary coroutine test suites.

**Language evidence:** Flow collection, channel wrapping, event modeling, timeouts, cancellation, assertion reporting, and the public test DSL are implemented in common Kotlin.

**Why study it:** A very small codebase exposes the hard parts of asynchronous tests: collection startup, virtual time, cancellation, terminal events, unconsumed events, timeouts, and error preservation.

**What you can learn:**

- Flow collection, channels, structured concurrency, coroutine contexts, cancellation, virtual test dispatchers, sealed event models, timeout scopes, assertion design, and race-sensitive tests.

**Prerequisites:**

- Suspend functions, CoroutineScope and Job, Flow and Channel, cancellation exceptions, coroutine test scheduling, sealed types, and asynchronous test reasoning.

**Start here:** [`src/commonMain/kotlin/app/cash/turbine/flow.kt`](https://github.com/cashapp/turbine/blob/408104d0874678455ff997913bd3f698039f5c25/src/commonMain/kotlin/app/cash/turbine/flow.kt) — The test and testIn operators show how a Flow is launched into a channel-backed Turbine, registered with a scope, validated, canceled, and checked for unconsumed events.

**Why this level:**

- **S1:** 569 meaningful implementation LOC measured with tokei 14.0.0. Count covers the complete common production implementation and excludes all platform test source sets, documentation, API dumps, and build metadata.
- **D3:** The library is tiny, but correct behavior depends on coroutine scheduling, cancellation propagation, channel closure, and preserving causal exceptions across asynchronous boundaries.
- **C2:** Several tightly related pieces interact in one process, but there are no external services or broad subsystem boundaries.
- **Placement:** S1/D3/C2 averages to 2.00, making Turbine an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** Public contracts, channel adaptation, coroutine-scope setup, timeout handling, and error formatting remain separated despite delicate cancellation semantics.
- **Architecture:** Flow operators collect into channels, ChannelTurbine implements the assertion protocol, context elements carry registry and timeout state, and Event models terminal outcomes.
- **Naming and idiom:** awaitItem, ensureAllEventsConsumed, cancelAndIgnoreRemainingEvents, collectTurbineIn, TurbineRegistryElement, and Event.Error state behavior directly.
- **Tests:** Large common and platform suites exercise ordering, completion, exceptions, timeouts, virtual time, cancellation, multiple flows, standalone turbines, non-suspending APIs, and diagnostic messages.
- **Documentation:** The README explains the channel model, single and multiple Flow use, cleanup obligations, terminal events, timeouts, standalone fakes, and known unstable upstream dependency.
- **Traceability:** A Flow.test call can be followed through collection launch and channel closure into awaitItem or awaitError and then matched to exact failure-message assertions.
- **Maintainability:** The small API, explicit lifecycle operations, stable artifact policy, and exhaustive edge-case suite constrain changes to timing-sensitive behavior.
- **Educational value:** It demonstrates why concurrent code can be difficult even when short and provides a bounded place to study structured testing of asynchronous streams.

**Inspection record:** commit `408104d0874678455ff997913bd3f698039f5c25`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/commonMain/kotlin/app/cash/turbine/flow.kt`, `src/commonMain/kotlin/app/cash/turbine/Turbine.kt`, `src/commonMain/kotlin/app/cash/turbine/ReceiveTurbine.kt`, `src/commonTest/kotlin/app/cash/turbine/FlowTest.kt`, `src/commonTest/kotlin/app/cash/turbine/ChannelTest.kt`, `LICENSE.txt`. GitHub Linguist label: Kotlin. LOC exclusions: src/commonTest/, src/jvmTest/, src/nonJvmTest/, README.md, build files.

**License:** [Apache-2.0](https://github.com/cashapp/turbine/blob/408104d0874678455ff997913bd3f698039f5c25/LICENSE.txt)

### [oshai/kotlin-logging](https://github.com/oshai/kotlin-logging)

**S1 / D2 / C2 → SDC 2**

A lightweight Kotlin multiplatform logging facade with lazy messages and adapters for platform logging systems.

**Real-world evidence:** The project publishes current Maven artifacts, documents platform setup and runtime backend requirements, and lists production software that uses the facade.

**Language evidence:** The lazy logging facade, event builder, logger factories, SLF4J and JUL adapters, source-location preservation, and native, Android, JS, Wasm, and Darwin backends are Kotlin.

**Why study it:** The code shows how a narrow common API can preserve lazy evaluation, markers, structured payloads, caller location, and exceptions while adapting to very different platform loggers.

**What you can learn:**

- Lazy lambda APIs, facade and adapter design, multiplatform source sets, logger factories, fluent event builders, caller-boundary preservation, markers, MDC context, and platform contract tests.

**Prerequisites:**

- Kotlin interfaces and default methods, lambdas, delegation, multiplatform source organization, logging levels, SLF4J concepts, and coroutine context basics.

**Start here:** [`src/commonMain/kotlin/io/github/oshai/kotlinlogging/KLogger.kt`](https://github.com/oshai/kotlin-logging/blob/0aaa57ccef9e1cc619de0d30bd65cc0a7271332d/src/commonMain/kotlin/io/github/oshai/kotlinlogging/KLogger.kt) — KLogger defines the common lazy and fluent contract; LocationAwareKLogger then shows how that contract maps to SLF4J without losing the real caller.

**Why this level:**

- **S1:** 1,882 meaningful implementation LOC measured with tokei 14.0.0. Count covers common, Java, JVM, Android, JS, Native, Darwin, Wasm JS, and Wasm WASI production source sets and excludes every test source set, documentation, and build metadata.
- **D2:** The wrappers contain platform details and overload discipline, but data flow is direct and the common abstractions are conventional.
- **C2:** Several clear adapters implement one contract, without persistence, networking, or a service topology.
- **Placement:** S1/D2/C2 averages to 1.67 and rounds upward, making kotlin-logging an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** The common API centralizes overload semantics while backend files focus on translating events and preserving platform-specific metadata.
- **Architecture:** KLogger and event builders define the facade; configuration selects a factory; platform wrappers translate the same level, marker, cause, argument, and payload model.
- **Naming and idiom:** KLoggingEventBuilder, DelegatingKLogger, LocationAwareKLogger, loggerFactory, isLoggingEnabledFor, and callerBoundary reveal intent and ownership.
- **Tests:** Common and platform suites cover lazy invocation, payloads, markers, caller lines, name resolution, MDC propagation, startup configuration, and backend-specific formatting.
- **Documentation:** The README explains lazy messages, logger naming, exceptions, structured payloads, backend setup, compatibility changes, multiplatform status, and troubleshooting.
- **Traceability:** A logger.info lambda can be followed through the common level method, enabled check, event builder, selected wrapper, underlying backend call, and caller-location assertion.
- **Maintainability:** The facade isolates backend churn, platform behavior has targeted tests, and public compatibility changes are documented explicitly.
- **Educational value:** It is a manageable study of abstraction boundaries: convenience is added without pretending that all logging platforms expose identical capabilities.

**Inspection record:** commit `0aaa57ccef9e1cc619de0d30bd65cc0a7271332d`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/commonMain/kotlin/io/github/oshai/kotlinlogging/KotlinLogging.kt`, `src/commonMain/kotlin/io/github/oshai/kotlinlogging/KLogger.kt`, `src/javaMain/kotlin/io/github/oshai/kotlinlogging/slf4j/internal/LocationAwareKLogger.kt`, `src/commonTest/kotlin/io/github/oshai/kotlinlogging/SimpleTest.kt`, `src/jvmTest/kotlin/io/github/oshai/kotlinlogging/LoggingWithLocationTest.kt`, `LICENSE`. GitHub Linguist label: Kotlin. LOC exclusions: all test source sets under src/, docs/, README.md, build files.

**License:** [Apache-2.0](https://github.com/oshai/kotlin-logging/blob/0aaa57ccef9e1cc619de0d30bd65cc0a7271332d/LICENSE)

## SDC 3

### [ajalt/clikt](https://github.com/ajalt/clikt)

**S2 / D3 / C3 → SDC 3**

A multiplatform Kotlin framework for type-safe command-line applications with nested commands, composable parameters, generated help, and shell completion.

**Real-world evidence:** Clikt publishes current core, full, and Markdown artifacts on Maven Central and maintains documentation and sample applications for JVM, Node.js, and native targets.

**Language evidence:** Command modeling, tokenization and parsing, property-delegated parameters, transformations, validation, value sources, help formatting, completion generation, and platform types are Kotlin.

**Why study it:** Clikt shows how a polished declarative API is supported by a staged parser: invocation collection, eager handling, conversion, finalization, validation, command execution, help, and completion.

**What you can learn:**

- Property-delegate providers, typed transformation chains, command trees, parser staging, error aggregation, value sources and environment precedence, parameter groups, help formatting, shell completion, and multiplatform APIs.

**Prerequisites:**

- Comfortable Kotlin generics, variance, property delegates, extension functions, sealed errors, command-line parsing, nested commands, and validation pipelines.

**Start here:** [`clikt/src/commonMain/kotlin/com/github/ajalt/clikt/parsers/CommandLineParser.kt`](https://github.com/ajalt/clikt/blob/fa2e48c54995a88d492f05568a64889d99994877/clikt/src/commonMain/kotlin/com/github/ajalt/clikt/parsers/CommandLineParser.kt) — This file names the distinct parse, eager-finalization, value-finalization, validation, and run stages and connects them to command and parameter abstractions.

**Why this level:**

- **S2:** 5,249 meaningful implementation LOC measured with tokei 14.0.0. Count covers production source in clikt, clikt-mordant, and clikt-mordant-markdown, including JVM-specific types, and excludes tests, samples, documentation, API dumps, and build metadata.
- **D3:** Understanding a value requires following generic wrappers and lifecycle stages, while shell grammars, grouped constraints, and multiple sources add moderate domain depth.
- **C3:** An important option crosses several explicit layers and extension points, though everything remains an in-process library.
- **Placement:** S2/D3/C3 averages to 2.67, making Clikt an SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** Parsing, invocation records, value transformation, finalization, validation, formatting, and completion are decomposed into focused files with explicit stage boundaries.
- **Architecture:** Base commands own contexts and parameters; the parser builds invocation trees; finalizers derive typed values; output and completion layers consume the resulting command model.
- **Naming and idiom:** CommandInvocation, OptionInvocation, finalizeEagerOptions, finalizeCommand, TransformContext, ValueSource, and CompletionCandidates expose the lifecycle.
- **Tests:** Extensive common and JVM suites cover token forms, suggestions, nested commands, eager options, groups, sources, every common type, help output, completion scripts, and filesystem types.
- **Documentation:** The README orients quickly, while dedicated documentation explains command, option, argument, completion, testing, migration, and advanced extension behavior.
- **Traceability:** An option delegate can be followed from registration through argv invocation, source precedence, conversion, finalization, post-validation, property access, and targeted OptionTest cases.
- **Maintainability:** Core and rich-output integrations are separated, public APIs have dumps, transformations compose instead of duplicating parser branches, and tests mirror feature areas.
- **Educational value:** It is a strong intermediate study of the machinery required to make a declarative user API both type-safe and operationally precise.

**Inspection record:** commit `fa2e48c54995a88d492f05568a64889d99994877`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `clikt/src/commonMain/kotlin/com/github/ajalt/clikt/parsers/CommandLineParser.kt`, `clikt/src/commonMain/kotlin/com/github/ajalt/clikt/parsers/ParserInternals.kt`, `clikt/src/commonMain/kotlin/com/github/ajalt/clikt/parameters/options/Option.kt`, `test/src/commonTest/kotlin/com/github/ajalt/clikt/parameters/OptionTest.kt`, `test/src/commonTest/kotlin/com/github/ajalt/clikt/parameters/SubcommandTest.kt`, `LICENSE.txt`. GitHub Linguist label: Kotlin. LOC exclusions: test/, samples/, docs/, API dumps, build files.

**License:** [Apache-2.0](https://github.com/ajalt/clikt/blob/fa2e48c54995a88d492f05568a64889d99994877/LICENSE.txt)

### [square/moshi](https://github.com/square/moshi)

**S2 / D4 / C3 → SDC 3**

A modern JSON library for Kotlin and Java with streaming I/O, composable adapters, reflection support, and generated adapters through Kotlin Symbol Processing.

**Real-world evidence:** Square publishes Moshi runtime, Kotlin, adapter, and code-generation artifacts and documents stable use in Kotlin and Java applications.

**Language evidence:** The adapter registry, streaming UTF-8 reader and writer, Kotlin reflection integration, standard adapters, and KSP code generator are primarily Kotlin, with intentional Java interoperability and tests.

**Why study it:** Moshi connects a byte-level JSON state machine to a type-driven adapter registry and two Kotlin object-mapping strategies, making parsing, caching, reflection, and code generation comparable in one repository.

**What you can learn:**

- Streaming JSON tokenization, parser state stacks, buffered I/O, generic type resolution, adapter factories and caching, annotations, reflection, Kotlin metadata, KSP code generation, recursion handling, and exhaustive format tests.

**Prerequisites:**

- Advanced Kotlin and Java interoperability, generics and reflection, JSON grammar, buffered byte I/O, annotations, code generation, Kotlin metadata, and Gradle modules.

**Start here:** [`moshi/src/main/java/com/squareup/moshi/Moshi.kt`](https://github.com/square/moshi/blob/889013ec2edb8d8034902662a1dc8c4f3b3f8111/moshi/src/main/java/com/squareup/moshi/Moshi.kt) — Moshi.adapter shows factory lookup, recursive deferred adapters, qualifier and type handling, and cache publication before the reader or object-mapping details are explored.

**Why this level:**

- **S2:** 9,041 meaningful implementation LOC measured with tokei 14.0.0. Count covers production source in moshi, moshi-kotlin, moshi-adapters, and moshi-kotlin-codegen, including Kotlin and Java, and excludes tests, examples, dedicated test modules, documentation, and build metadata.
- **D4:** Several advanced concerns recur across the main path: correct JSON lexing, generic type construction, reflection, generated code, recursive types, and strict error locations.
- **C3:** Tracing object decoding crosses meaningful layers and sometimes build-time generation, but the architecture remains a bounded library rather than a platform.
- **Placement:** S2/D4/C3 averages to 3.00, making Moshi an SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** Parser states, adapter lookup, standard adapters, reflection, and generation are separated and heavily documented where contracts are subtle.
- **Architecture:** JsonReader and JsonWriter provide the streaming layer; Moshi resolves and caches JsonAdapters; reflection or KSP-generated adapters map Kotlin objects; optional factories extend behavior.
- **Naming and idiom:** peekedNumberLength, JsonScope, DeferredJsonAdapter, nextAdapter, KotlinJsonAdapterFactory, TargetType, and AdapterGenerator make state and extension roles explicit.
- **Tests:** Broad suites cover valid and invalid grammar, numeric boundaries, paths, recursion, factories, qualifiers, Kotlin defaults and nullability, reflection, generated adapters, dates, enums, and polymorphism.
- **Documentation:** The README explains the object model, adapter composition, Kotlin reflection versus code generation, custom adapters, platform requirements, and limitations.
- **Traceability:** A requested Kotlin type can be followed through factory selection and cache handling into a generated or reflective adapter, streaming token reads, object construction, and corresponding tests.
- **Maintainability:** Public extension points are narrow, recursion is handled explicitly, parser errors carry paths, compatibility tooling is present, and implementation areas have dedicated suites.
- **Educational value:** It teaches how production serialization spans syntax, bytes, types, reflection, generated code, and API design without collapsing those concerns into one opaque mapper.

**Inspection record:** commit `889013ec2edb8d8034902662a1dc8c4f3b3f8111`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `moshi/src/main/java/com/squareup/moshi/Moshi.kt`, `moshi/src/main/java/com/squareup/moshi/-JsonUtf8Reader.kt`, `moshi-kotlin/src/main/java/com/squareup/moshi/kotlin/reflect/KotlinJsonAdapterFactory.kt`, `moshi-kotlin-codegen/src/main/java/com/squareup/moshi/kotlin/codegen/api/AdapterGenerator.kt`, `moshi/src/test/java/com/squareup/moshi/MoshiTest.java`, `moshi-kotlin-codegen/src/test/java/com/squareup/moshi/kotlin/codegen/ksp/JsonClassSymbolProcessorTest.kt`, `LICENSE.txt`. GitHub Linguist label: Kotlin. LOC exclusions: all src/test/ trees, moshi-kotlin-tests/, examples/, records-tests/, build files and API reports.

**License:** [Apache-2.0](https://github.com/square/moshi/blob/889013ec2edb8d8034902662a1dc8c4f3b3f8111/LICENSE.txt)

## SDC 4

### [Kotlin/kotlinx.coroutines](https://github.com/Kotlin/kotlinx.coroutines)

**S3 / D5 / C4 → SDC 4**

Kotlin's official multiplatform library for structured concurrency, asynchronous streams, channels, scheduling, testing, debugging, and ecosystem integration.

**Real-world evidence:** JetBrains publishes stable core, test, debug, reactive, UI, and integration artifacts as the standard library companion for Kotlin coroutine applications.

**Language evidence:** Coroutine jobs, continuations, dispatchers, work-stealing scheduler, channels, flows, synchronization primitives, test scheduler, debug probes, reactive adapters, and platform integrations are Kotlin.

**Why study it:** The repository exposes the runtime machinery beneath friendly suspend APIs: lock-free job states, cancellation, continuation resumption, scheduling, channels, Flow operators, virtual time, and platform dispatchers.

**What you can learn:**

- Structured concurrency, coroutine contexts, state machines, atomic and lock-free algorithms, work stealing, cancellation races, continuations, channels, Flow backpressure, synchronization, virtual-time testing, debugger instrumentation, and platform adapters.

**Prerequisites:**

- Expert Kotlin, continuations and suspend lowering concepts, memory models, atomics, concurrent data structures, thread scheduling, reactive streams, cancellation semantics, and stress-test reasoning.

**Start here:** [`kotlinx-coroutines-core/common/src/JobSupport.kt`](https://github.com/Kotlin/kotlinx.coroutines/blob/f63a04bacb8beeafcc9d49199b1e4bb08931b7eb/kotlinx-coroutines-core/common/src/JobSupport.kt) — JobSupport documents and implements the central lifecycle state machine; its state-table tests provide an unusually direct bridge into the wider cancellation and child-job machinery.

**Why this level:**

- **S3:** 20,652 meaningful implementation LOC measured with tokei 14.0.0. Count covers production Kotlin and Java in source directories across core, test, debug, reactive, UI, and integration modules; test sources, benchmarks, integration harnesses, internal test utilities, build logic, documentation, and build metadata are excluded.
- **D5:** Expert-level concurrent algorithms recur in the main runtime, and correctness depends on atomic transitions, scheduling, cancellation, and platform memory behavior.
- **C4:** Many interacting components and integrations share core lifecycle contracts, although the project is still a library family rather than a distributed platform.
- **Placement:** S3/D5/C4 averages to 4.00, making kotlinx.coroutines an SDC 4 project.

**Quality-gate evidence:**

- **Source quality:** Dense concurrency code accompanies its atomic transitions with state tables, invariants, and comments explaining common-case optimizations and race handling.
- **Architecture:** Job and continuation lifecycles anchor builders and scopes; dispatchers schedule work; channels and Flow provide communication; test and debug modules observe the same runtime contracts.
- **Naming and idiom:** JobSupport, Finishing, CancellableContinuationImpl, CoroutineScheduler, parkedWorkersStack, SharedFlowImpl, and TestCoroutineScheduler expose concrete runtime roles.
- **Tests:** Deterministic lifecycle tests, platform suites, stress tests, Lincheck models, scheduler tests, Flow and channel contracts, virtual-time tests, integration tests, and debugger tests cover concurrency behavior deeply.
- **Documentation:** The README maps modules and concepts, links the coroutine guide and design proposal, documents platform support, compatibility, debugging, testing, and integration setup.
- **Traceability:** A launched child can be followed through JobSupport state transitions and continuation dispatch into a scheduler queue, cancellation propagation, and explicit state and stress tests.
- **Maintainability:** Internal APIs are marked, compatibility policy is documented, platform implementations share common contracts, invariants are stated, and specialized concurrency tests guard races.
- **Educational value:** It is a demanding but exemplary source for understanding how structured concurrency emerges from atomic lifecycle machinery rather than syntax alone.

**Inspection record:** commit `f63a04bacb8beeafcc9d49199b1e4bb08931b7eb`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `kotlinx-coroutines-core/common/src/JobSupport.kt`, `kotlinx-coroutines-core/common/src/CancellableContinuationImpl.kt`, `kotlinx-coroutines-core/jvm/src/scheduling/CoroutineScheduler.kt`, `kotlinx-coroutines-core/common/src/flow/SharedFlow.kt`, `kotlinx-coroutines-core/common/test/JobStatesTest.kt`, `kotlinx-coroutines-core/jvm/test/scheduling/CoroutineSchedulerTest.kt`, `LICENSE.txt`. GitHub Linguist label: Kotlin. LOC exclusions: all test source directories, all benchmark directories, integration-testing/, test-utils/, buildSrc/, docs/, build files.

**License:** [Apache-2.0](https://github.com/Kotlin/kotlinx.coroutines/blob/f63a04bacb8beeafcc9d49199b1e4bb08931b7eb/LICENSE.txt)

### [Kotlin/kotlinx.serialization](https://github.com/Kotlin/kotlinx.serialization)

**S3 / D4 / C4 → SDC 4**

Kotlin's multiplatform, multi-format, reflectionless serialization runtime and format libraries.

**Real-world evidence:** JetBrains publishes stable core and format artifacts coordinated with Kotlin's serialization compiler plugin and documents JVM, JS, Native, and Wasm use.

**Language evidence:** The format-independent serializer contracts and modules plus JSON, ProtoBuf, CBOR, Properties, and HOCON runtime implementations are Kotlin multiplatform code.

**Why study it:** The repository cleanly separates generated type knowledge from format encoders and decoders, then implements several text and binary protocols over the same descriptor contract.

**What you can learn:**

- Serializer and descriptor protocols, generated-code boundaries, encoder and decoder abstractions, polymorphic and contextual lookup, JSON lexing and modes, ProtoBuf and CBOR wire formats, schema behavior, multiplatform APIs, and conformance testing.

**Prerequisites:**

- Advanced Kotlin generics and annotations, compiler-plugin concepts, serialization theory, JSON and binary protocols, state machines, polymorphism, multiplatform source sets, and compatibility testing.

**Start here:** [`core/commonMain/src/kotlinx/serialization/KSerializer.kt`](https://github.com/Kotlin/kotlinx.serialization/blob/25c2a755cbe6926a63003f3a51527bb731e8cd14/core/commonMain/src/kotlinx/serialization/KSerializer.kt) — KSerializer documents the format-independent contract between generated serializers and encoders; Json.kt and StreamingJsonDecoder then show one substantial realization of that contract.

**Why this level:**

- **S3:** 13,771 meaningful implementation LOC measured with tokei 14.0.0. Count covers production Kotlin and Java in core and all format main source sets and excludes every test source set, dedicated test modules, benchmarks, guide examples, integration fixtures, build logic, documentation, and build metadata.
- **D4:** Advanced type, protocol, parser, and generated-code concerns recur throughout the runtime and require both language and serialization-domain knowledge.
- **C4:** A complete behavior crosses generated code, descriptors, modules, encoders, format internals, and platform-specific paths, with several formats sharing the same core.
- **Placement:** S3/D4/C4 averages to 3.67, making kotlinx.serialization an SDC 4 project.

**Quality-gate evidence:**

- **Source quality:** Core contracts are documented as protocols, format code isolates wire concerns, and error paths preserve positions and descriptor paths.
- **Architecture:** Generated serializers speak the KSerializer and descriptor protocol; modules resolve contextual and polymorphic types; each format supplies encoders, decoders, lexers or readers, and configuration.
- **Naming and idiom:** SerialDescriptor, SerializersModule, CompositeDecoder, StreamingJsonDecoder, WriteMode, ProtobufTaggedEncoder, and MissingFieldException reveal the data and control contracts.
- **Tests:** Core, format, cross-platform, compatibility, conformance, failure-mode, schema, polymorphism, numeric-boundary, and stress suites exercise both protocols and diagnostics.
- **Documentation:** The README and guides explain setup, compiler/runtime versioning, formats, generated serializers, customization, polymorphism, compatibility, and platform caveats.
- **Traceability:** A Serializable value can be followed from a generated serializer's descriptor calls through module lookup and a format encoder or decoder into JSON or binary tokens and targeted tests.
- **Maintainability:** Stable core contracts decouple formats, configurations are explicit, platform differences stay in source sets, compatibility policies are documented, and exhaustive tests bound protocol changes.
- **Educational value:** It is a rigorous study of designing one type-directed protocol that supports multiple encodings without reflection or format knowledge leaking into generated models.

**Inspection record:** commit `25c2a755cbe6926a63003f3a51527bb731e8cd14`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `core/commonMain/src/kotlinx/serialization/KSerializer.kt`, `core/commonMain/src/kotlinx/serialization/modules/SerializersModule.kt`, `formats/json/commonMain/src/kotlinx/serialization/json/Json.kt`, `formats/json/commonMain/src/kotlinx/serialization/json/internal/StreamingJsonDecoder.kt`, `formats/protobuf/commonMain/src/kotlinx/serialization/protobuf/internal/ProtobufEncoding.kt`, `formats/json-tests/commonTest/src/kotlinx/serialization/json/JsonParserFailureModesTest.kt`, `LICENSE.txt`. GitHub Linguist label: Kotlin. LOC exclusions: all test source sets under core/ and formats/, formats/json-tests/, benchmark/, guide/, integration-test/, buildSrc/, build files.

**License:** [Apache-2.0](https://github.com/Kotlin/kotlinx.serialization/blob/25c2a755cbe6926a63003f3a51527bb731e8cd14/LICENSE.txt)

## SDC 5

### [JetBrains/kotlin](https://github.com/JetBrains/kotlin)

**S5 / D5 / C5 → SDC 5**

The Kotlin programming language implementation, including its compiler frontends, intermediate representations, backends, tooling, libraries, and multiplatform infrastructure.

**Real-world evidence:** This official JetBrains repository builds the Kotlin compiler and language toolchain distributed for JVM, JavaScript, Wasm, Native, IDE, Gradle, Maven, and command-line workflows.

**Language evidence:** The compiler frontends, FIR semantic model, FIR-to-IR conversion, intermediate representations, lowering pipelines, JVM backend, command-line compiler, daemon, incremental compilation, and much supporting infrastructure are implemented primarily in Kotlin.

**Why study it:** The JVM path provides a complete compiler journey: command-line configuration, source environment, FIR analysis, FIR-to-IR conversion, lowering phases, bytecode generation, metadata, diagnostics, plugins, and deterministic output tests.

**What you can learn:**

- Compiler drivers, syntax and semantic analysis, symbol and type systems, FIR and IR design, lowering phases, expect/actual processing, plugin extension points, bytecode generation, incremental compilation, compiler daemons, diagnostics, metadata, and massive generated and integration test systems.

**Prerequisites:**

- Expert Kotlin and Java, compiler construction, parsing and semantic analysis, type systems, intermediate representations, JVM bytecode, build systems, concurrency, multiplatform compilation, and large-repository navigation.

**Start here:** [`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/K2JVMCompiler.kt`](https://github.com/JetBrains/kotlin/blob/893937b03bee8acd82c4c6201732d9e29cb3d932/compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/K2JVMCompiler.kt) — K2JVMCompiler is a concrete product entry point whose pipeline leads through environment setup, FIR analysis and conversion, JVM IR lowerings, bytecode generation, output writing, and integration tests.

**Why this level:**

- **S5:** 780,962 meaningful implementation LOC measured with tokei 14.0.0. A conservative count covers first-party Kotlin, Java, C, and C++ implementation under compiler/ and core/ only. Tests, fixtures, test data, generated files, benchmarks, build paths, documentation, and the repository's many libraries, plugins, IDE integrations, Native, JS, and Wasm areas are excluded; the measured slice alone remains S5.
- **D5:** The central code is expert compiler implementation requiring deep language, type-system, IR, platform, and performance knowledge.
- **C5:** A compilation crosses many major subsystems, and the full repository also serves numerous targets and tool integrations with shared language contracts.
- **Placement:** S5/D5/C5 averages to 5.00, making Kotlin an SDC 5 project.

**Quality-gate evidence:**

- **Source quality:** Complex compiler phases are represented by named pipeline objects, explicit result types, phase engines, symbol tables, diagnostics, and extensive internal contracts rather than an undifferentiated driver.
- **Architecture:** CLI and build-tool drivers configure environments; FIR performs frontend analysis; FIR-to-IR bridges semantic and backend models; target lowering phases prepare IR; backends emit artifacts and metadata.
- **Naming and idiom:** K2JVMCompiler, KotlinCoreEnvironment, JvmFir2IrPipelinePhase, Fir2IrConverter, JvmIrCodegenFactory, PhaseEngine, and DiagnosticReporter expose the compilation stages.
- **Tests:** Generated language tests, integration suites, diagnostics, IR dumps, bytecode listings, runtime boxes, incremental scenarios, daemon tests, compatibility suites, and deterministic JAR tests cover the toolchain at many boundaries.
- **Documentation:** The repository orients contributors, links language and build resources, documents code rules and security, and contains subsystem READMEs plus a precise license and third-party notice directory.
- **Traceability:** A JVM CLI invocation can be followed through K2JVMCompiler configuration and pipeline selection, FIR analysis, FIR-to-IR conversion, JVM lowerings, per-file code generation, output packaging, and JarOutputTest.
- **Maintainability:** Despite scale, stages and extension points are explicit, code ownership is modular, diagnostics and outputs have stable models, and layered generated, golden, integration, and compatibility tests constrain change.
- **Educational value:** It is a genuine capstone: learners can study a production language implementation end to end while choosing one bounded target pipeline instead of pretending the whole platform is a beginner reading exercise.

**Inspection record:** commit `893937b03bee8acd82c4c6201732d9e29cb3d932`, reviewed 2026-08-28 by Codex. Files sampled: `ReadMe.md`, `compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/K2JVMCompiler.kt`, `compiler/cli/cli-base/src/org/jetbrains/kotlin/cli/jvm/compiler/KotlinCoreEnvironment.kt`, `compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmFir2IrPipelinePhase.kt`, `compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/pipeline/convertToIr.kt`, `compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrConverter.kt`, `compiler/ir/backend.jvm/entrypoint/src/org/jetbrains/kotlin/backend/jvm/JvmIrCodegenFactory.kt`, `compiler/tests-integration/tests/org/jetbrains/kotlin/cli/JarOutputTest.kt`, `license/README.md`, `license/LICENSE.txt`. GitHub Linguist label: Kotlin. LOC exclusions: all test, testFixtures, and testData paths, generated source, benchmarks, build infrastructure, documentation, repository areas outside compiler/ and core/.

**License:** [Apache-2.0 AND LicenseRef-Third-Party-Notices](https://github.com/JetBrains/kotlin/blob/893937b03bee8acd82c4c6201732d9e29cb3d932/license/README.md)

### [ktorio/ktor](https://github.com/ktorio/ktor)

**S4 / D5 / C5 → SDC 5**

JetBrains' multiplatform asynchronous framework for HTTP clients, servers, microservices, WebSockets, streaming, and extensible application plugins.

**Real-world evidence:** Ktor is an official JetBrains product with published client, server, engine, protocol, plugin, and testing artifacts and maintained product documentation.

**Language evidence:** Server and client pipelines, routing, HTTP and WebSocket protocols, I/O channels, networking, engines, plugins, serialization adapters, test hosts, and multiplatform implementations are overwhelmingly Kotlin, with a small Rust WebRTC boundary.

**Why study it:** Ktor shows how a coroutine-based pipeline abstraction scales from request routing and plugins into clients, servers, network engines, protocols, serialization, testing, and multiple operating platforms.

**What you can learn:**

- Coroutine request lifecycles, phased pipelines, route trees and resolution, client and server plugin systems, HTTP parsing, streaming byte channels, sockets and TLS, engine adapters, WebSockets and SSE, serialization, multiplatform boundaries, and integration testing.

**Prerequisites:**

- Expert Kotlin and coroutines, HTTP semantics, asynchronous I/O, sockets and TLS, parser and routing concepts, plugin architecture, serialization, Gradle multiplatform builds, and server lifecycle operations.

**Start here:** [`ktor-server/ktor-server-core/common/src/io/ktor/server/application/ApplicationCallPipeline.kt`](https://github.com/ktorio/ktor/blob/6b20bd02a684a3543bf2e4d2fa2f9c83a83189e4/ktor-server/ktor-server-core/common/src/io/ktor/server/application/ApplicationCallPipeline.kt) — The call pipeline names the framework's execution phases; RoutingRoot then demonstrates how route resolution builds and executes merged receive, call, and response pipelines for one request.

**Why this level:**

- **S4:** 101,229 meaningful implementation LOC measured with tokei 14.0.0. Count covers production Kotlin, Java, Rust, C, and C++ under source and Rust implementation paths across the framework; tests, fixtures, test-support modules, samples, benchmarks, integration suites, build logic, documentation, and generated API dumps are excluded.
- **D5:** Expert-level concurrency, networking, protocol, compiler, and platform concerns recur throughout core framework paths rather than appearing in one isolated module.
- **C5:** Tracing a real request can cross routing, plugins, transformations, streaming channels, an engine, protocol parsing, and platform adapters inside a broad framework platform.
- **Placement:** S4/D5/C5 averages to 4.67 and has two dimensions at 5, making Ktor an SDC 5 project.

**Quality-gate evidence:**

- **Source quality:** Core lifecycle classes and protocol modules use explicit phases, capabilities, attributes, typed plugins, and coroutine ownership to bound otherwise broad behavior.
- **Architecture:** Shared I/O, network, HTTP, and utility modules support independent client and server stacks; engines adapt platforms; plugins intercept stable pipelines; test hosts exercise applications in process.
- **Naming and idiom:** ApplicationCallPipeline, RoutingResolveContext, RoutingPipelineCall, HttpClientEngine, HttpRequestPipeline, ByteReadChannel, and BaseApplicationPlugin reveal execution and extension boundaries.
- **Tests:** Unit, contract, engine, protocol, routing, plugin, test-host, platform, stress, and integration suites cover request lifecycles from parsing through responses across multiple engines.
- **Documentation:** The README states principles and a complete first server; product documentation covers clients, servers, engines, plugins, protocols, deployment, testing, and extension points.
- **Traceability:** A server call can be followed from an engine into ApplicationCallPipeline, RoutingRoot resolution, merged route and application pipelines, a handler response, and route or engine tests.
- **Maintainability:** Shared contracts isolate engines and platforms, public APIs are documented and dumped, plugins compose through named hooks, and subsystem-specific tests localize a very large surface.
- **Educational value:** It is a mature capstone for studying how small Kotlin abstractions such as receiver DSLs, coroutines, and pipelines scale into a full network framework.

**Inspection record:** commit `6b20bd02a684a3543bf2e4d2fa2f9c83a83189e4`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `ktor-server/ktor-server-core/common/src/io/ktor/server/application/ApplicationCallPipeline.kt`, `ktor-server/ktor-server-core/common/src/io/ktor/server/routing/RoutingRoot.kt`, `ktor-client/ktor-client-core/common/src/io/ktor/client/HttpClient.kt`, `ktor-utils/common/src/io/ktor/util/pipeline/Pipeline.kt`, `ktor-server/ktor-server-core/common/test/io/ktor/server/routing/RouteTest.kt`, `ktor-client/ktor-client-core/common/test/ClientPluginsTest.kt`, `LICENSE`. GitHub Linguist label: Kotlin. LOC exclusions: all test source trees and test-only modules, all testData trees, samples and examples, benchmarks, integration test suites, build-logic/, build-settings-logic/, documentation and build metadata.

**License:** [Apache-2.0](https://github.com/ktorio/ktor/blob/6b20bd02a684a3543bf2e4d2fa2f9c83a83189e4/LICENSE)

_Generated from `catalog/kotlin.json`; do not edit by hand._

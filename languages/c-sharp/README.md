# C#

10 qualified repositories. Scores assume the learner described in [the SDC rubric](../../docs/sdc.md).

[← All languages](../README.md)

## SDC 1

### [ardalis/GuardClauses](https://github.com/ardalis/GuardClauses)

**S1 / D1 / C1 → SDC 1**

A focused library of guard-clause extension methods for validating arguments and returning narrowed, usable values.

**Real-world evidence:** The repository publishes a NuGet package used to enforce method preconditions in production .NET applications.

**Language evidence:** The guard entry point and validation extension methods under src/GuardClauses are implemented in C#.

**Why study it:** A learner can read nearly all of it while seeing extension methods, nullable annotations, caller argument expressions, generic constraints, exception design, and disciplined tests.

**What you can learn:**

- Guard clauses, extension methods, nullable flow annotations, generic constraints, caller argument expressions, exceptions, and boundary testing.

**Prerequisites:**

- C# methods, generics, nullable reference types, extension methods, exceptions, and collections.

**Start here:** [`src/GuardClauses/GuardAgainstNullExtensions.cs`](https://github.com/ardalis/GuardClauses/blob/7d55fa5397d73c0fe4e86a2dcab0230d1db57870/src/GuardClauses/GuardAgainstNullExtensions.cs) — The null, empty, default, and predicate guards demonstrate the package's extension pattern and value-returning contract.

**Why this level:**

- **S1:** 1,374 meaningful implementation LOC measured with tokei 14.0.0. Calibration count covers production C# under src, excluding tests, samples, docs, and build metadata.
- **D1:** Behavior consists mostly of clear conditions and conventional exceptions using familiar language features.
- **C1:** Each guard is locally traceable through one static class family and the shared entry point.
- **Placement:** Small, direct, and locally testable production code makes GuardClauses SDC 1.

**Quality-gate evidence:**

- **Source quality:** Guards return validated inputs, use precise framework exceptions, and annotate nullability so runtime and compiler contracts agree.
- **Architecture:** A tiny Guard entry point is extended by partial static classes grouped by validation concern.
- **Naming and idiom:** Against, Null, NullOrEmpty, OutOfRange, InvalidInput, and CallerArgumentExpression read naturally at call sites.
- **Tests:** Focused xUnit suites cover valid returns, exception types, parameter names, messages, custom exceptions, generics, and edge values.
- **Documentation:** The README lists guards, extension guidance, package use, and concise examples.
- **Traceability:** A call such as Guard.Against.Null stays in one extension method before returning the input or throwing.
- **Maintainability:** Independent methods, partial files, and matching test classes keep additions isolated.
- **Educational value:** It demonstrates polished library fundamentals without domain or framework overhead.

**Inspection record:** commit `7d55fa5397d73c0fe4e86a2dcab0230d1db57870`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/GuardClauses/Guard.cs`, `src/GuardClauses/GuardAgainstNullExtensions.cs`, `test/GuardClauses.UnitTests/GuardAgainstNull.cs`. GitHub Linguist label: C#. LOC exclusions: tests, samples.

**License:** [MIT](https://github.com/ardalis/GuardClauses/blob/7d55fa5397d73c0fe4e86a2dcab0230d1db57870/LICENSE)

### [serilog/serilog-sinks-console](https://github.com/serilog/serilog-sinks-console)

**S1 / D2 / C1 → SDC 1**

A Serilog sink that renders structured log events as text or JSON to standard output or error with ANSI and Windows console themes.

**Real-world evidence:** Serilog publishes this NuGet package as the production console output adapter for structured .NET logging.

**Language evidence:** Console sink configuration, rendering, formatting, platform handling, and theme implementations under src are C#.

**Why study it:** A compact integration shows configuration extensions, thread-safe output, stream selection, token rendering, ANSI state, platform differences, and approval tests.

**What you can learn:**

- Adapter design, synchronized console I/O, structured-log rendering, format tokens, ANSI themes, platform fallbacks, and approval tests.

**Prerequisites:**

- C# interfaces, text writers, locking, structured logging, terminal escape sequences, and formatting.

**Start here:** [`src/Serilog.Sinks.Console/Sinks/SystemConsole/ConsoleSink.cs`](https://github.com/serilog/serilog-sinks-console/blob/9b75d510787f5d54cf76584a3c3341d7eab0ee0a/src/Serilog.Sinks.Console/Sinks/SystemConsole/ConsoleSink.cs) — The sink selects output, applies formatting and theme behavior, synchronizes writes, and flushes one complete event.

**Why this level:**

- **S1:** 1,630 meaningful implementation LOC measured with tokei 14.0.0. Count covers production C# under src, excluding tests, sample applications, visual assets, docs, and build support.
- **D2:** Rendering and platform nuances require attention, but they are isolated behind direct formatter and theme abstractions.
- **C1:** Configuration produces one sink whose output path crosses only formatter, theme, renderer, and console writer classes.
- **Placement:** The focused architecture keeps this real output integration at SDC 1 despite terminal-specific details.

**Quality-gate evidence:**

- **Source quality:** Writes are synchronized and flushed explicitly, platform setup is isolated, and renderers each own one token concern.
- **Architecture:** Configuration extensions construct a ConsoleSink using formatters, output-token renderers, and interchangeable console themes.
- **Naming and idiom:** ConsoleSink, OutputTemplateRenderer, LevelTokenRenderer, AnsiConsoleTheme, and standardErrorFromLevel state roles plainly.
- **Tests:** Unit and approval tests cover output templates, JSON and display values, themes, configuration, escaping, and stream choices.
- **Documentation:** README and examples document default output, templates, JSON, themes, standard error thresholds, and XML configuration.
- **Traceability:** A LogEvent can be followed through ConsoleSink, a formatter or template renderer, theme writes, and the selected TextWriter.
- **Maintainability:** Small renderers and theme interfaces isolate new tokens and terminal behavior from sink synchronization.
- **Educational value:** It teaches how a narrow production adapter handles formatting and platform edges cleanly.

**Inspection record:** commit `9b75d510787f5d54cf76584a3c3341d7eab0ee0a`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/Serilog.Sinks.Console/Sinks/SystemConsole/ConsoleSink.cs`, `src/Serilog.Sinks.Console/Sinks/SystemConsole/Themes/AnsiConsoleTheme.cs`, `test/Serilog.Sinks.Console.Tests/Output/OutputTemplateRendererTests.cs`. GitHub Linguist label: C#. LOC exclusions: tests, samples, assets.

**License:** [Apache-2.0](https://github.com/serilog/serilog-sinks-console/blob/9b75d510787f5d54cf76584a3c3341d7eab0ee0a/LICENSE)

## SDC 2

### [DapperLib/Dapper](https://github.com/DapperLib/Dapper)

**S2 / D3 / C2 → SDC 2**

A lightweight object mapper that extends database connections with fast SQL execution and row-to-object materialization.

**Real-world evidence:** Dapper is released as production data-access infrastructure and is used by large .NET applications, including its original Stack Overflow use case.

**Language evidence:** SQL execution, parameter handling, mapping, caching, async operations, type handlers, and AOT support are implemented in C#.

**Why study it:** It shows how a deliberately small public API uses reflection, generated IL, caches, dynamic rows, and asynchronous database contracts for performance.

**What you can learn:**

- ADO.NET extension APIs, reflection and IL emission, row mapping, parameter binding, caches, multi-mapping, buffered versus streamed results, and async I/O.

**Prerequisites:**

- ADO.NET, SQL, generics, reflection, delegates, async tasks, dynamic objects, and basic IL concepts.

**Start here:** [`Dapper/SqlMapper.cs`](https://github.com/DapperLib/Dapper/blob/6d48ef664acc7298c649e2d449d903b3360d5a90/Dapper/SqlMapper.cs) — The central partial class defines query/execute entry points, identity caches, deserializer generation, parameter binding, and mapping behavior.

**Why this level:**

- **S2:** 7,824 meaningful implementation LOC measured with tokei 14.0.0. Count covers production C# across Dapper libraries, excluding tests, benchmarks, samples, generated output, and build support.
- **D3:** Fast deserializer generation, cache identities, provider quirks, dynamic rows, and asynchronous readers require substantial .NET knowledge.
- **C2:** Most behavior flows through one central mapper and a few helper types into standard database interfaces.
- **Placement:** Compact architecture keeps advanced mapping internals at SDC 2 rather than overstating them.

**Quality-gate evidence:**

- **Source quality:** Performance paths are guarded by type and provider checks, cache keys are explicit, and resource disposal is visible in sync and async code.
- **Architecture:** A central SqlMapper partial class coordinates commands, parameters, deserializers, grids, dynamic rows, type handlers, and provider settings.
- **Naming and idiom:** CommandDefinition, DynamicParameters, GridReader, TypeHandler, Identity, Query, Execute, and multi-map describe data access directly.
- **Tests:** Large database-backed suites cover providers, parameters, mapping, buffering, async operations, type handlers, nulls, and regressions.
- **Documentation:** README, API examples, benchmarks, package docs, and tests explain common and advanced patterns.
- **Traceability:** A QueryAsync call can be followed through command setup, reader execution, cached deserializer selection, materialization, and disposal.
- **Maintainability:** Provider switches and mapping helpers live behind a small stable extension-method API and extensive regression coverage.
- **Educational value:** It demonstrates how a micro-ORM earns speed and convenience without becoming a full persistence framework.

**Inspection record:** commit `6d48ef664acc7298c649e2d449d903b3360d5a90`, reviewed 2026-08-28 by Codex. Files sampled: `Readme.md`, `Dapper/SqlMapper.cs`, `Dapper/SqlMapper.Async.cs`, `tests/Dapper.Tests/AsyncTests.cs`. GitHub Linguist label: C#. LOC exclusions: tests, benchmarks, samples, generated files.

**License:** [Apache-2.0](https://github.com/DapperLib/Dapper/blob/6d48ef664acc7298c649e2d449d903b3360d5a90/License.txt)

### [serilog/serilog](https://github.com/serilog/serilog)

**S2 / D2 / C2 → SDC 2**

A structured logging core that turns message templates and properties into immutable events routed through enrichers, filters, and sinks.

**Real-world evidence:** Serilog is released as widely used production logging infrastructure with a large sink and integration ecosystem.

**Language evidence:** Logger pipelines, structured events, message-template parsing, enrichment, filtering, sinks, configuration, and level switching are C#.

**Why study it:** Its compact core demonstrates immutable events, template parsing, pipeline composition, contextual enrichment, level control, failure isolation, and stable extension contracts.

**What you can learn:**

- Structured events, message-template parsing, immutable values, pipeline composition, filtering, enrichment, sinks, context propagation, and failure handling.

**Prerequisites:**

- Interfaces, delegates, immutable data, parsing basics, thread safety, logging concepts, and disposable resources.

**Start here:** [`src/Serilog/Core/Logger.cs`](https://github.com/serilog/serilog/blob/49b5339ce85385dc52d4d8e8f2b8308becf23506/src/Serilog/Core/Logger.cs) — Logger binds templates, constructs events, applies enrichment and filtering, dispatches sinks, and protects the application from logging failures.

**Why this level:**

- **S2:** 7,067 meaningful implementation LOC measured with tokei 14.0.0. Count covers production C# under src/Serilog, excluding tests, benchmarks, samples, assets, and build files.
- **D2:** Parsing and concurrent logging need care, but the core pipeline uses familiar interfaces and explicit immutable records.
- **C2:** Several components compose in one process along a clearly ordered event path.
- **Placement:** Moderate size and a cohesive structured-event pipeline make Serilog SDC 2.

**Quality-gate evidence:**

- **Source quality:** Logging failures are contained, events are immutable, hot paths avoid avoidable allocation, and pipeline order is explicit.
- **Architecture:** LoggerConfiguration builds a Logger from level controls, enrichers, filters, sinks, message-template processing, and audit paths.
- **Naming and idiom:** LogEvent, MessageTemplate, Enricher, Filter, Sink, LevelSwitch, ForContext, and WriteTo establish precise vocabulary.
- **Tests:** Focused suites cover parsing, binding, properties, context, filters, levels, sinks, disposal, concurrency, and failures.
- **Documentation:** README, wiki, configuration examples, API docs, and ecosystem links explain concepts and extension.
- **Traceability:** A Log.Information call can be followed through template binding, event construction, enrichment, filtering, and sink emission.
- **Maintainability:** Small public interfaces and immutable event/value types let external sinks and enrichers evolve independently.
- **Educational value:** It shows a clean production implementation of structured logging rather than simple string output.

**Inspection record:** commit `49b5339ce85385dc52d4d8e8f2b8308becf23506`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/Serilog/Core/Logger.cs`, `src/Serilog/LoggerConfiguration.cs`, `test/Serilog.Tests/Core/LoggerTests.cs`. GitHub Linguist label: C#. LOC exclusions: tests, benchmarks, samples.

**License:** [Apache-2.0](https://github.com/serilog/serilog/blob/49b5339ce85385dc52d4d8e8f2b8308becf23506/LICENSE)

## SDC 3

### [FluentValidation/FluentValidation](https://github.com/FluentValidation/FluentValidation)

**S3 / D3 / C3 → SDC 3**

A strongly typed validation framework that turns fluent expression-based rules into synchronous or asynchronous validation pipelines.

**Real-world evidence:** FluentValidation is released as production validation infrastructure used in .NET services and applications.

**Language evidence:** Validator composition, rule components, expression parsing, selectors, conditions, async execution, messages, and results are C#.

**Why study it:** It shows how expression trees and fluent builders become reusable rules with cascade modes, conditions, selectors, localization, async validators, and structured failures.

**What you can learn:**

- Fluent builders, expression trees, generic rule components, validation contexts, cascade control, async rules, localization, dependency injection, and test helpers.

**Prerequisites:**

- Generics, delegates, expression trees, async tasks, extension methods, validation patterns, and dependency injection.

**Start here:** [`src/FluentValidation/AbstractValidator.cs`](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/src/FluentValidation/AbstractValidator.cs) — The base validator registers expression-derived property rules and drives selection, execution, conditions, dependent rules, and results.

**Why this level:**

- **S3:** 16,382 meaningful implementation LOC measured with tokei 14.0.0. Count covers production C# in FluentValidation projects, excluding tests, docs, samples, and build support.
- **D3:** Expressions, generic builders, conditional and dependent rule execution, and async validators introduce recurring abstraction and lifecycle reasoning.
- **C3:** Validation crosses fluent construction, contexts, selectors, rules, validators, messages, conditions, and result aggregation.
- **Placement:** Mid-sized source with layered generic execution makes FluentValidation SDC 3.

**Quality-gate evidence:**

- **Source quality:** Rule construction and execution are separated, generic contracts preserve types, and cancellation and async boundaries are explicit.
- **Architecture:** Validators build property and collection rules composed from components, selectors, contexts, message formatters, and result objects.
- **Naming and idiom:** AbstractValidator, RuleFor, PropertyRule, ValidationContext, RuleComponent, CascadeMode, and ValidationFailure form a coherent model.
- **Tests:** Extensive tests cover validators, expressions, conditions, collections, async behavior, messages, selectors, inheritance, and regressions.
- **Documentation:** The versioned guide covers every validator, composition pattern, testing, localization, DI, async behavior, and upgrades.
- **Traceability:** A RuleFor call can be followed from expression parsing into a PropertyRule, its components, context execution, and failures.
- **Maintainability:** Interfaces and rule components isolate validators and integrations while compatibility is supported by broad behavioral tests.
- **Educational value:** It demonstrates how a readable fluent DSL is backed by explicit generic objects and execution policy.

**Inspection record:** commit `daa00b795450881c233253488e3ddeb362f59f56`, reviewed 2026-08-28 by Codex. Files sampled: `docs/index.rst`, `src/FluentValidation/AbstractValidator.cs`, `src/FluentValidation/Internal/PropertyRule.cs`, `src/FluentValidation.Tests/AbstractValidatorTester.cs`. GitHub Linguist label: C#. LOC exclusions: tests, documentation, build files.

**License:** [Apache-2.0](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/License.txt)

### [nodatime/nodatime](https://github.com/nodatime/nodatime)

**S3 / D4 / C3 → SDC 3**

A date and time library with precise immutable types for instants, durations, local values, calendars, time zones, periods, and parsing.

**Real-world evidence:** Noda Time is a released production library used when .NET applications need rigorous temporal modeling and time-zone behavior.

**Language evidence:** Temporal value types, calendars, time zones, parsers, patterns, providers, serialization, and utilities under src/NodaTime are C#.

**Why study it:** It makes difficult domain semantics explicit through immutable types, carefully separated timelines and calendars, generated time-zone data, parsers, and exhaustive invariants.

**What you can learn:**

- Temporal modeling, immutable value types, calendars, time-zone transitions, interval arithmetic, parsing patterns, nanosecond representation, caching, and specification tests.

**Prerequisites:**

- Advanced C#, value types and operators, calendar arithmetic, time zones, integer overflow, parsing, concurrency, and XML/JSON serialization.

**Start here:** [`src/NodaTime/Instant.cs`](https://github.com/nodatime/nodatime/blob/67f788570b9b5972f52aa316fa1cf32b73439eb6/src/NodaTime/Instant.cs) — Instant demonstrates the timeline model, trusted versus validated construction, nanosecond representation, arithmetic, conversions, and invariants.

**Why this level:**

- **S3:** 16,037 meaningful implementation LOC measured with tokei 14.0.0. Count covers production C# in src/NodaTime, excluding tests, generated data, benchmarks, tools, docs, and build support.
- **D4:** Correctness depends repeatedly on subtle temporal semantics, multiple calendars, ambiguous transitions, bounds, and representation conversions.
- **C3:** Several substantial subsystems interoperate around a coherent immutable temporal model without distributed or service topology.
- **Placement:** Deep domain difficulty raises this S3-sized, well-structured library to the upper end of SDC 3.

**Quality-gate evidence:**

- **Source quality:** Trusted and untrusted constructors, preconditions, immutable values, overflow checks, and detailed XML comments make invariants explicit.
- **Architecture:** Core values connect calendars, time zones, providers, text patterns, global utilities, and serialization adapters through narrow types.
- **Naming and idiom:** Instant, Duration, LocalDateTime, ZonedDateTime, DateTimeZone, Period, CalendarSystem, and Pattern distinguish semantics precisely.
- **Tests:** Extensive unit, data, compatibility, serialization, pattern, calendar, and time-zone tests cover difficult boundary behavior.
- **Documentation:** A comprehensive user guide, API docs, design notes, migration guides, and time-zone resources explain both model and use.
- **Traceability:** An instant conversion can be followed through duration representation, a zone provider and interval, calendar mapping, and tested output.
- **Maintainability:** Immutable domain types, explicit providers, generated-data boundaries, and exhaustive tests control change in a subtle domain.
- **Educational value:** It is a model case of using type design to make domain distinctions that ordinary date-time APIs blur.

**Inspection record:** commit `67f788570b9b5972f52aa316fa1cf32b73439eb6`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/NodaTime/Instant.cs`, `src/NodaTime/TimeZones/DateTimeZoneCache.cs`, `src/NodaTime.Test/InstantTest.cs`. GitHub Linguist label: C#. LOC exclusions: tests, generated time-zone data, benchmarks, tools.

**License:** [Apache-2.0](https://github.com/nodatime/nodatime/blob/67f788570b9b5972f52aa316fa1cf32b73439eb6/LICENSE.txt)

## SDC 4

### [dotnet/efcore](https://github.com/dotnet/efcore)

**S5 / D4 / C4 → SDC 4**

An object-database mapper that translates LINQ, tracks entity state, generates database updates and migrations, and supports provider extensions.

**Real-world evidence:** Microsoft releases EF Core as production data-access infrastructure for .NET applications and database providers.

**Language evidence:** DbContext, LINQ translation, metadata, change tracking, state management, updates, migrations, providers, and tooling are C#.

**Why study it:** It connects expression trees and metadata models to query compilation, identity maps, change detection, transactional updates, migrations, and provider-specific SQL.

**What you can learn:**

- LINQ expression translation, metadata models, identity maps, change tracking, unit-of-work state, query compilation, migrations, database providers, and diagnostics.

**Prerequisites:**

- Advanced C#, expression trees, databases and SQL, transactions, reflection, dependency injection, caching, and compiler-style pipelines.

**Start here:** [`src/EFCore/DbContext.cs`](https://github.com/dotnet/efcore/blob/8e66699fe92713d8cfa9f4b248c0f3711af88d34/src/EFCore/DbContext.cs) — DbContext exposes the unit-of-work boundary and connects sets, services, tracking, queries, change detection, saves, configuration, and disposal.

**Why this level:**

- **S5:** 301,586 meaningful implementation LOC measured with tokei 14.0.0. Count covers production C# under src, excluding tests, benchmarks, samples, generated source, docs, and build artifacts.
- **D4:** Type mapping, expression rewriting, relational semantics, state transitions, concurrency, migrations, and provider behavior recur across core paths.
- **C4:** A database operation crosses contexts, metadata, services, query compilation, materialization, tracking, update generation, transactions, and providers.
- **Placement:** EF Core's S5 source volume and advanced, multi-subsystem ORM behavior combine to SDC 4.

**Quality-gate evidence:**

- **Source quality:** State transitions, service dependencies, async restrictions, lifetimes, query caching, and provider contracts are explicitly documented and typed.
- **Architecture:** Core services connect metadata, queries, change tracking, updates, storage, diagnostics, migrations, design-time tooling, and providers.
- **Naming and idiom:** DbContext, EntityType, ChangeTracker, StateManager, QueryCompiler, ModificationCommand, Migration, and Provider express ORM roles.
- **Tests:** Large specification, provider, functional, unit, migration, query, update, concurrency, and compatibility suites exercise behavior.
- **Documentation:** Concept guides, API docs, provider writing, performance notes, migrations, samples, and breaking-change references are comprehensive.
- **Traceability:** A LINQ query can be followed through compilation and provider translation into materialization and identity tracking; SaveChanges follows a parallel update path.
- **Maintainability:** Service interfaces, provider specifications, convention pipelines, diagnostics, and cross-provider tests govern a large abstraction surface.
- **Educational value:** It provides a deep production study of translating object and language semantics into database operations.

**Inspection record:** commit `8e66699fe92713d8cfa9f4b248c0f3711af88d34`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/EFCore/DbContext.cs`, `src/EFCore/ChangeTracking/Internal/StateManager.cs`, `test/EFCore.Tests/DbContextTest.cs`. GitHub Linguist label: C#. LOC exclusions: tests, benchmarks, samples, generated code.

**License:** [MIT](https://github.com/dotnet/efcore/blob/8e66699fe92713d8cfa9f4b248c0f3711af88d34/LICENSE.txt)

### [dotnet/orleans](https://github.com/dotnet/orleans)

**S5 / D4 / C4 → SDC 4**

A distributed virtual-actor framework providing grains, durable identity, activation, placement, messaging, clustering, persistence, streams, and hosting.

**Real-world evidence:** Microsoft releases Orleans as a production cloud-native application framework used to build distributed .NET services.

**Language evidence:** Virtual-actor runtime, grain references, messaging, placement, membership, persistence, serialization, clustering, and hosting are predominantly C#.

**Why study it:** Its source makes actor identity and calls look local while exposing the distributed runtime that handles activation, routing, serialization, membership, failures, persistence, and rebalancing.

**What you can learn:**

- Virtual actors, distributed identity and messaging, serialization, placement, membership, activation lifecycles, persistence, streams, retries, and graceful shutdown.

**Prerequisites:**

- Advanced C#, async concurrency, distributed systems, serialization, dependency injection, networking, persistence, and cluster operations.

**Start here:** [`src/Orleans.Core.Abstractions/Runtime/GrainReference.cs`](https://github.com/dotnet/orleans/blob/137d9acc17830f15b13a4eb0058d6cee633cad5e/src/Orleans.Core.Abstractions/Runtime/GrainReference.cs) — GrainReference shows how typed remote identities are represented, serialized, copied, invoked, compared, and connected to runtime services.

**Why this level:**

- **S5:** 227,174 meaningful implementation LOC measured with tokei 14.0.0. Count covers production C#, JavaScript, and TypeScript under src, excluding tests, samples, benchmarks, generated code, docs, and build output.
- **D4:** Remote invocation, activation races, placement, membership, retries, persistence, and single-threaded actor guarantees require advanced distributed reasoning.
- **C4:** A grain call crosses generated references, serialization, messaging, routing, silo lifecycle, activation, storage, and cluster services.
- **Placement:** S5 breadth plus D4/C4 distributed-runtime mechanics place Orleans at SDC 4 under the simple average.

**Quality-gate evidence:**

- **Source quality:** Runtime state machines, cancellation, timeouts, activation ownership, serializer contracts, and cluster transitions are explicitly modeled.
- **Architecture:** Abstractions connect runtime, messaging, hosting, serialization, clustering, placement, persistence, streaming, transactions, and provider extensions.
- **Naming and idiom:** Grain, GrainReference, Silo, Activation, Placement, Membership, Stream, Reminder, and ClusterClient define the virtual-actor model.
- **Tests:** Unit, default-cluster, persistence, streaming, serialization, failure, compatibility, provider, and distributed suites cover runtime behavior.
- **Documentation:** Conceptual guides, tutorials, API references, hosting and deployment guidance, provider docs, and contributor material are extensive.
- **Traceability:** A typed grain call can be traced through a GrainReference and request serialization into messaging, placement, activation, dispatch, and response.
- **Maintainability:** Public abstractions, generated-code contracts, provider interfaces, lifecycle participants, and multi-layer tests constrain runtime change.
- **Educational value:** It is an unusually accessible production implementation of the virtual-actor model and its distributed machinery.

**Inspection record:** commit `137d9acc17830f15b13a4eb0058d6cee633cad5e`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/Orleans.Core.Abstractions/Runtime/GrainReference.cs`, `src/Orleans.Runtime/Silo/Silo.cs`, `test/Orleans.DefaultCluster.Tests/GrainReferenceTest.cs`. GitHub Linguist label: C#. LOC exclusions: tests, samples, benchmarks, generated code.

**License:** [MIT](https://github.com/dotnet/orleans/blob/137d9acc17830f15b13a4eb0058d6cee633cad5e/LICENSE)

## SDC 5

### [dotnet/aspnetcore](https://github.com/dotnet/aspnetcore)

**S5 / D4 / C5 → SDC 5**

The ASP.NET Core web platform, including HTTP servers, middleware, routing, hosting, MVC, Razor, Blazor, SignalR, security, and deployment integrations.

**Real-world evidence:** Microsoft ships ASP.NET Core as the production web framework and server stack for modern .NET applications.

**Language evidence:** HTTP abstractions, Kestrel, hosting, routing, middleware, MVC, Razor, Blazor, SignalR, authentication, and data protection are predominantly C# with first-party web client code.

**Why study it:** It connects low-level HTTP parsing and pipelines to application middleware, endpoints, controllers, real-time messaging, UI frameworks, security, diagnostics, and deployment.

**What you can learn:**

- HTTP protocol engines, pipelines and backpressure, middleware, routing, hosting, dependency injection, MVC, real-time messaging, rendering, authentication, data protection, and observability.

**Prerequisites:**

- Expert C#, async I/O, HTTP/1–3, networking, concurrency, web security, compilers/rendering, dependency injection, and distributed deployment.

**Start here:** [`src/Servers/Kestrel/Core/src/Internal/Http/HttpProtocol.cs`](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/src/Servers/Kestrel/Core/src/Internal/Http/HttpProtocol.cs) — The per-request protocol state connects parsed HTTP data, body pipes, response features, limits, timeouts, diagnostics, and application dispatch.

**Why this level:**

- **S5:** 666,450 meaningful implementation LOC measured with tokei 14.0.0. Count covers production C#, native code, JavaScript, TypeScript, and F# under src, excluding tests, samples, benchmarks, generated/built assets, docs, and artifacts.
- **D4:** Kestrel, pipelines, HTTP versions, rendering, SignalR, auth, cryptography, and framework activation repeatedly require advanced domain knowledge.
- **C5:** Requests cross servers, features, hosting, middleware, routing, endpoints, MVC or UI stacks, auth, diagnostics, and deployment integrations.
- **Placement:** S5 and C5 make the full ASP.NET Core platform SDC 5.

**Quality-gate evidence:**

- **Source quality:** Hot protocol paths document state and allocation choices, request features expose explicit contracts, and lifecycle cleanup is strongly tested.
- **Architecture:** Shared abstractions connect servers, HTTP features, hosting, middleware, routing, MVC, Razor, Blazor, SignalR, identity, data protection, and tools.
- **Naming and idiom:** HttpContext, FeatureCollection, RequestDelegate, Middleware, Endpoint, Kestrel, Hub, Razor, and Host define the platform model.
- **Tests:** Unit, functional, server, browser, interop, security, stress, performance, compatibility, and deployment suites cover the platform.
- **Documentation:** Product docs, API references, architecture notes, server guidance, security material, samples, and contributor docs are comprehensive.
- **Traceability:** A request can be followed from Kestrel protocol state through HttpContext features, middleware and routing into an endpoint and response pipeline.
- **Maintainability:** Feature interfaces, shared frameworks, subsystem directories, compatibility policy, generated-code boundaries, and broad matrices constrain change.
- **Educational value:** It is an advanced end-to-end study of how a production web platform spans sockets, protocols, frameworks, UI, and operations.

**Inspection record:** commit `8c1a406592b06b954acac509fa4725ca560b2e53`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/Http/Http/src/DefaultHttpContext.cs`, `src/Servers/Kestrel/Core/src/Internal/Http/HttpProtocol.cs`, `src/Http/Http/test/DefaultHttpContextTests.cs`. GitHub Linguist label: C#. LOC exclusions: tests, samples, benchmarks, generated and built assets.

**License:** [MIT](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/LICENSE.txt)

### [dotnet/runtime](https://github.com/dotnet/runtime)

**S5 / D5 / C5 → SDC 5**

The cross-platform .NET runtime, including the CLR, JIT, garbage collector, type system, core libraries, interop, diagnostics, and native hosting.

**Real-world evidence:** Microsoft ships this repository as the production runtime and standard libraries underlying .NET applications across operating systems and architectures.

**Language evidence:** Core libraries are C#, while the CLR, garbage collector, JIT, native hosting, interop, and platform layers use C++, C, and assembly as first-party runtime implementation.

**Why study it:** It exposes the entire managed execution stack from C# library contracts through object layouts, JIT compilation, garbage collection, exceptions, threading, interop, and operating-system ports.

**What you can learn:**

- Runtime type systems, JIT compilation, garbage collection, object layout, core libraries, interop and marshalling, threading, exceptions, diagnostics, native hosting, and portability.

**Prerequisites:**

- Expert C#, C++, C, assembly, compilers, operating systems, memory models, concurrency, ABIs, garbage collection, and CPU architecture.

**Start here:** [`src/libraries/System.Private.CoreLib/src/System/String.cs`](https://github.com/dotnet/runtime/blob/c4eee2b76e574b0dd6cfe3387220a905ba69aca6/src/libraries/System.Private.CoreLib/src/System/String.cs) — String shows the managed contract, intrinsic hooks, layout assumptions, spans, allocation, and the boundary between library source and runtime implementation.

**Why this level:**

- **S5:** 3,761,600 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party C#, C++, C, assembly, and supporting source under src, excluding tests, samples, benchmarks, generated code, reference-only source, docs, and artifacts.
- **D5:** Expert compiler, memory, concurrency, type-system, binary, platform, and performance reasoning is pervasive across central components.
- **C5:** Managed calls can cross libraries, intrinsics, the VM, JIT, GC, threading, diagnostics, interop, native hosting, and many OS/architecture ports.
- **Placement:** Millions of lines and D5/C5 runtime internals make dotnet/runtime definitively SDC 5.

**Quality-gate evidence:**

- **Source quality:** Performance and memory invariants, managed/native boundaries, platform conditions, contracts, and failure paths are documented and heavily tested.
- **Architecture:** CoreCLR, Mono, NativeAOT, libraries, JIT, GC, diagnostics, hosting, interop, installer, and platform abstractions have explicit ownership.
- **Naming and idiom:** MethodTable, Object, String, GCHeap, JIT, CoreLib, Interop, SafeHandle, and RuntimeType form the execution vocabulary.
- **Tests:** Runtime, library, JIT, GC, interop, diagnostics, stress, performance, compatibility, and platform matrices exercise the stack.
- **Documentation:** Design documents, coding guides, runtime notes, API docs, issue policies, build instructions, and performance material are extensive.
- **Traceability:** A managed operation can be followed from a core-library method through intrinsic or internal-call boundaries into VM/JIT/native implementation and architecture-specific tests.
- **Maintainability:** Subsystem boundaries, compatibility standards, code generation, platform abstractions, stress infrastructure, and enormous test matrices control risk.
- **Educational value:** It is a premier expert-level source for understanding how a modern managed language platform actually executes.

**Inspection record:** commit `c4eee2b76e574b0dd6cfe3387220a905ba69aca6`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/libraries/System.Private.CoreLib/src/System/String.cs`, `src/coreclr/vm/object.cpp`, `src/libraries/System.Runtime/tests/System.Runtime.Tests/System/StringTests.cs`. GitHub Linguist label: C#. LOC exclusions: tests, samples, benchmarks, generated code, reference assemblies.

**License:** [MIT](https://github.com/dotnet/runtime/blob/c4eee2b76e574b0dd6cfe3387220a905ba69aca6/LICENSE.TXT)

_Generated from `catalog/c-sharp.json`; do not edit by hand._

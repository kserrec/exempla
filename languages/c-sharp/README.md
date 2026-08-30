# C#

8 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

[← All languages](../README.md)

## Level 1

No qualified learning path has been published at this level. Standards are not lowered to fill a slot.

## Level 2

### [ardalis/GuardClauses](https://github.com/ardalis/GuardClauses)

**Language 3 / Behavior 2 / Design 1 / Constraints 2 → Level 2**

A focused library of guard-clause extension methods for validating arguments and returning narrowed, usable values.

**Why study it:** The null-guard path shows how a tiny C# API combines runtime validation with compiler flow narrowing, automatic caller-expression capture, generic overloads, and a stable exception contract.

**Prerequisites:**

- Basic familiarity with C# classes and interfaces, generics, delegates, nullable values, exceptions, asynchronous basics, and unit tests.

**Concepts this path develops:**

- Generic reference- and value-type overloads.
- Localized null and non-null branches.
- Stable parameter-name and exception contracts.

**What you can learn:**

- Use `src/GuardClauses/GuardAgainstNullExtensions.cs` to study the following transferable techniques and behaviors: Generic reference- and value-type overloads, nullable annotations, NotNull flow guarantees, CallerArgumentExpression, optional exception factories, ArgumentNullException construction, and value-returning guards.

**Learning path:**

- **Goal:** Understand how GuardClauses rejects null arguments while returning a compiler-narrowed value and preserving the caller's argument name and exception contract.
- **Start here:** [`src/GuardClauses/GuardAgainstNullExtensions.cs`](https://github.com/ardalis/GuardClauses/blob/7d55fa5397d73c0fe4e86a2dcab0230d1db57870/src/GuardClauses/GuardAgainstNullExtensions.cs) — src/GuardClauses/GuardAgainstNullExtensions.cs contains the reference- and value-type Null overloads and exposes every selected type-system and exception behavior directly.
- **Then read:**
  - [`src/GuardClauses/Guard.cs`](https://github.com/ardalis/GuardClauses/blob/7d55fa5397d73c0fe4e86a2dcab0230d1db57870/src/GuardClauses/Guard.cs)
  - [`test/GuardClauses.UnitTests/GuardAgainstNull.cs`](https://github.com/ardalis/GuardClauses/blob/7d55fa5397d73c0fe4e86a2dcab0230d1db57870/test/GuardClauses.UnitTests/GuardAgainstNull.cs)
- **Trace:** Begin with the reference- and value-type Null extension overloads, follow their generic constraints, nullable annotations, CallerArgumentExpression parameter capture, and optional exception factory into ArgumentNullException, then correlate default and custom names, messages, factories, non-null returns, and nullable value narrowing in GuardAgainstNull tests.

**Why this level:**

- **Language technique 3:** Generics, constraints, compiler flow annotations, and caller-expression capture materially shape the small public API.
- **Behavioral reasoning 2:** Validation and error behavior require care but remain synchronous and local to the guard call.
- **Design span 1:** The complete behavior remains in one focused unit with a minimal public marker boundary.
- **Constraint burden 2:** The path preserves routine public-API, diagnostic, and compiler-analysis safeguards without several interacting production constraints.
- **Placement:** The four scores 3/2/1/2 sum to 8; their arithmetic mean is 2.00 and rounds half-up to Level 2. The published result is Level 2.

**License:** MIT ([evidence 1](https://github.com/ardalis/GuardClauses/blob/7d55fa5397d73c0fe4e86a2dcab0230d1db57870/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The repository publishes a NuGet package used to enforce method preconditions in production .NET applications.

**Language evidence:** The guard entry point and validation extension methods under src/GuardClauses are implemented in C#.

**Coding relevance:**

The selected behavior is entirely about transferable argument validation, generic nullable-flow contracts, exception construction, and caller-expression capture.

No specialist domain context is required.

**Eight-part quality gate:**

- **Source quality:** The two overload families state their generic constraints, nullable contracts, captured argument name, optional message, custom factory, and return value explicitly.
- **Architecture:** A minimal Guard marker API hosts one focused extension unit, while the compiler and ArgumentNullException supply the flow and diagnostic boundaries.
- **Naming and idiom:** Guard, Against, Null, input, parameterName, message, exceptionCreator, NotNull, and CallerArgumentExpression state the guard contract directly.
- **Tests:** GuardAgainstNull tests cover null and non-null references and nullable values, default and custom names, messages, factories, returned values, and compiler narrowing.
- **Documentation:** XML documentation and the public guard-clause guidance explain the value-returning null contract, automatic parameter names, and customization points.
- **Traceability:** A Guard.Against.Null call can be followed through overload selection, compiler-supplied argument text, the null branch, optional exception factory, and focused assertions.
- **Maintainability:** The narrow extension surface and direct compiler-contract tests make changes to nullability, diagnostics, and exception compatibility easy to review.
- **Educational value:** The path demonstrates how a few modern C# features can make a conventional runtime guard improve static flow analysis and caller diagnostics.

**Inspection record:** commit `7d55fa5397d73c0fe4e86a2dcab0230d1db57870`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/GuardClauses/GuardAgainstNullExtensions.cs`, `src/GuardClauses/Guard.cs`, `test/GuardClauses.UnitTests/GuardAgainstNull.cs`, `LICENSE`. GitHub Linguist label: C#.

</details>

### [serilog/serilog-sinks-console](https://github.com/serilog/serilog-sinks-console)

**Language 2 / Behavior 2 / Design 2 / Constraints 3 → Level 2**

A Serilog sink that renders structured log events as text or JSON to standard output or error with ANSI and Windows console themes.

**Why study it:** The console-sink path shows how Serilog binds configuration to a renderer and emits every structured event as one synchronized write to standard output or standard error.

**Prerequisites:**

- Basic familiarity with C# classes and interfaces, generics, delegates, nullable values, exceptions, asynchronous basics, and unit tests.

**Concepts this path develops:**

- Formatter and theme interfaces.
- Localized buffered versus direct output branch.
- Atomic event output.

**What you can learn:**

- Use `src/Serilog.Sinks.Console/Sinks/SystemConsole/ConsoleSink.cs` to study the following transferable techniques and behaviors: Configuration extension methods, renderer and theme composition, output-template tokens, format providers, buffered themed output, stream selection, shared locking, and atomic event writes.

**Learning path:**

- **Goal:** Understand how the Serilog console sink configures a renderer and emits each formatted event as one synchronized console write.
- **Start here:** [`src/Serilog.Sinks.Console/Sinks/SystemConsole/ConsoleSink.cs`](https://github.com/serilog/serilog-sinks-console/blob/9b75d510787f5d54cf76584a3c3341d7eab0ee0a/src/Serilog.Sinks.Console/Sinks/SystemConsole/ConsoleSink.cs) — ConsoleSink.cs contains Emit, where stream selection, optional themed buffering, rendering, and the final shared-lock write meet for each event.
- **Then read:**
  - [`src/Serilog.Sinks.Console/ConsoleLoggerConfigurationExtensions.cs`](https://github.com/serilog/serilog-sinks-console/blob/9b75d510787f5d54cf76584a3c3341d7eab0ee0a/src/Serilog.Sinks.Console/ConsoleLoggerConfigurationExtensions.cs)
  - [`src/Serilog.Sinks.Console/Sinks/SystemConsole/Output/OutputTemplateRenderer.cs`](https://github.com/serilog/serilog-sinks-console/blob/9b75d510787f5d54cf76584a3c3341d7eab0ee0a/src/Serilog.Sinks.Console/Sinks/SystemConsole/Output/OutputTemplateRenderer.cs)
  - [`test/Serilog.Sinks.Console.Tests/Configuration/ConsoleLoggerConfigurationExtensionsTests.cs`](https://github.com/serilog/serilog-sinks-console/blob/9b75d510787f5d54cf76584a3c3341d7eab0ee0a/test/Serilog.Sinks.Console.Tests/Configuration/ConsoleLoggerConfigurationExtensionsTests.cs)
  - [`test/Serilog.Sinks.Console.Tests/Output/OutputTemplateRendererTests.cs`](https://github.com/serilog/serilog-sinks-console/blob/9b75d510787f5d54cf76584a3c3341d7eab0ee0a/test/Serilog.Sinks.Console.Tests/Output/OutputTemplateRendererTests.cs)
- **Trace:** Follow console configuration as it chooses a theme and constructs OutputTemplateRenderer and ConsoleSink, then follow Emit as it selects standard output or error, optionally buffers themed output, and protects the final write with the shared lock; correlate configuration output and token-rendering behavior in the focused tests.

**Why this level:**

- **Language technique 2:** Interfaces, callbacks, and ordinary composition shape the path without advanced C# machinery.
- **Behavioral reasoning 2:** The lock and output choice matter, but all mutable behavior remains localized in one short Emit method and does not require advanced concurrent-state reasoning.
- **Design span 2:** A few small modules contain the complete console-output behavior.
- **Constraint burden 3:** Several material reliability and compatibility contracts constrain changes even though the implementation remains compact.
- **Placement:** The four scores 2/2/2/3 sum to 9; their arithmetic mean is 2.25 and rounds half-up to Level 2. The published result is Level 2.

**License:** Apache-2.0 ([evidence 1](https://github.com/serilog/serilog-sinks-console/blob/9b75d510787f5d54cf76584a3c3341d7eab0ee0a/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Serilog publishes this NuGet package as the production console output adapter for structured .NET logging.

**Language evidence:** Console sink configuration, rendering, formatting, platform handling, and theme implementations under src are C#.

**Coding relevance:**

The logging vocabulary is familiar and short; the path primarily teaches interface composition, conditional buffering, localized synchronization, configuration defaults, and observable formatting.

Required domain context:

- A console sink formats each structured log event, optionally applies a theme, and writes it atomically to standard output or standard error.

**Eight-part quality gate:**

- **Source quality:** ConsoleSink.Emit expresses output selection, themed buffering, direct rendering, and synchronized final writing in a short explicit lifecycle.
- **Architecture:** ConsoleLoggerConfigurationExtensions constructs ConsoleSink with OutputTemplateRenderer and theme collaborators, while the sink owns only output coordination.
- **Naming and idiom:** ConsoleSink, Emit, OutputTemplateRenderer, theme, standardErrorFromLevel, output, syncRoot, and render state console behavior directly.
- **Tests:** The selected configuration and renderer suites cover output selection, themes, templates, format providers, properties, levels, timestamps, trace identifiers, and rendered text.
- **Documentation:** The sink README explains output templates, themes, standard-error routing, formatting, and configuration options used by this path.
- **Traceability:** A Console configuration call can be followed through renderer and sink construction into Emit's stream choice, rendering branch, shared lock, and exact output assertions.
- **Maintainability:** Separate configuration, rendering, theming, and output responsibilities plus focused text tests localize changes to a compact compatibility surface.
- **Educational value:** The path demonstrates how a small sink preserves event formatting and write atomicity under concurrent logging without introducing a large subsystem.

**Inspection record:** commit `9b75d510787f5d54cf76584a3c3341d7eab0ee0a`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/Serilog.Sinks.Console/Sinks/SystemConsole/ConsoleSink.cs`, `src/Serilog.Sinks.Console/ConsoleLoggerConfigurationExtensions.cs`, `src/Serilog.Sinks.Console/Sinks/SystemConsole/Output/OutputTemplateRenderer.cs`, `test/Serilog.Sinks.Console.Tests/Configuration/ConsoleLoggerConfigurationExtensionsTests.cs`, `test/Serilog.Sinks.Console.Tests/Output/OutputTemplateRendererTests.cs`, `LICENSE`. GitHub Linguist label: C#.

</details>

## Level 3

### [FluentValidation/FluentValidation](https://github.com/FluentValidation/FluentValidation)

**Language 4 / Behavior 3 / Design 3 / Constraints 3 → Level 3**

A strongly typed validation framework that turns fluent expression-based rules into synchronous or asynchronous validation pipelines.

**Why study it:** The validator path shows how a typed RuleFor expression becomes an authored asynchronous property-rule pipeline with conditions, cascades, dependent rules, cancellation, and structured failures.

**Prerequisites:**

- Basic familiarity with C# classes and interfaces, generics, delegates, nullable values, exceptions, asynchronous basics, and unit tests.

**Concepts this path develops:**

- Generic fluent rule-builder interfaces.
- Ordered async rule evaluation.
- Sync and async parity.

**What you can learn:**

- Use `src/FluentValidation/AbstractValidator.cs` to study the following transferable techniques and behaviors: Generic fluent builders, expression-tree property capture, cached accessors, validation contexts and selectors, ordered asynchronous components, conditions, class and rule cascades, dependent rules, cancellation, and sync-async parity.

**Learning path:**

- **Goal:** Understand how FluentValidation turns a typed RuleFor expression into an authored asynchronous property-rule pipeline with conditions, cascade behavior, dependent rules, cancellation, and failures.
- **Start here:** [`src/FluentValidation/AbstractValidator.cs`](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/src/FluentValidation/AbstractValidator.cs) — src/FluentValidation/AbstractValidator.cs contains RuleFor and ValidateInternalAsync, connecting typed rule declaration to selection, cancellation, class-level cascade, and rule execution.
- **Then read:**
  - [`src/FluentValidation/Internal/PropertyRule.cs`](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/src/FluentValidation/Internal/PropertyRule.cs)
  - [`src/FluentValidation/Internal/RuleBase.cs`](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/src/FluentValidation/Internal/RuleBase.cs)
  - [`src/FluentValidation/Internal/RuleBuilder.cs`](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/src/FluentValidation/Internal/RuleBuilder.cs)
  - [`src/FluentValidation.Tests/AbstractValidatorTester.cs`](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/src/FluentValidation.Tests/AbstractValidatorTester.cs)
  - [`src/FluentValidation.Tests/ConditionTests.cs`](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/src/FluentValidation.Tests/ConditionTests.cs)
  - [`src/FluentValidation.Tests/CascadingFailuresTester.cs`](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/src/FluentValidation.Tests/CascadingFailuresTester.cs)
  - [`src/FluentValidation.Tests/SyncAsyncParityTests.cs`](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/src/FluentValidation.Tests/SyncAsyncParityTests.cs)
- **Trace:** Follow RuleFor as it captures a typed expression and builds PropertyRule and RuleBuilder, then follow ValidateInternalAsync through cancellation and class-level cascade into PropertyRule.ValidateAsync, selector and condition checks, lazy accessor evaluation, validator components, failure creation, rule-level cascade, and dependent rules; use the focused tests to verify conditions, cascades, failures, and sync/async parity without treating generated output as the teaching source.

**Why this level:**

- **Language technique 4:** Expression processing and code generation materially shape the API and maintenance model alongside pervasive generic abstractions.
- **Behavioral reasoning 3:** Meaningful async, conditional, and cascade behavior recurs, but it remains a linear per-validation pipeline rather than an advanced distributed or concurrent state machine.
- **Design span 3:** Several meaningful framework boundaries contribute directly to one property validation.
- **Constraint burden 3:** Several material API, correctness, and reliability guarantees constrain changes, but they do not rise to interacting system-wide expert constraints in this bounded path.
- **Placement:** The four scores 4/3/3/3 sum to 13; their arithmetic mean is 3.25 and rounds half-up to Level 3. The published result is Level 3.

**License:** Apache-2.0 ([evidence 1](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/License.txt))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** FluentValidation is released as production validation infrastructure used in .NET services and applications.

**Language evidence:** Validator composition, rule components, expression parsing, selectors, conditions, async execution, messages, and results are C#.

**Coding relevance:**

The validation vocabulary is short and programming-led; the selected authored async path teaches expression-based APIs, generic fluent builders, cached accessors, callbacks, cancellation, conditions, and ordered rule composition.

Required domain context:

- A validator builds typed property rules, then evaluates their selectors, conditions, validator components, cascade policy, and dependent rules into validation failures.

**Eight-part quality gate:**

- **Source quality:** The authored asynchronous implementation explicitly separates validator orchestration, property rules, rule components, conditions, cascades, failures, and dependencies.
- **Architecture:** AbstractValidator owns the rule set, PropertyRule evaluates one property, RuleBase stores shared policy, RuleBuilder composes validators, and context and selector abstractions control execution.
- **Naming and idiom:** RuleFor, ValidateInternalAsync, PropertyRule, RuleBuilder, ValidationContext, selector, cascade, dependent rules, and ValidationFailure state pipeline intent.
- **Tests:** The selected validator, condition, cascade, and sync-async-parity suites cover selection, conditions, short circuits, dependencies, cancellation, failures, and generated counterpart agreement.
- **Documentation:** FluentValidation's rules, conditions, cascade, dependent-rule, asynchronous-validation, and error documentation explains the selected public and runtime contracts.
- **Traceability:** A RuleFor expression can be followed through PropertyRule and RuleBuilder construction into ValidateInternalAsync, selector and condition checks, component evaluation, failures, cascades, and dependencies.
- **Maintainability:** Strong generic boundaries, an inspectable authored async source, generated parity checks, and focused policy tests constrain changes across the fluent API.
- **Educational value:** The path shows how a declarative type-safe API becomes an ordered cancellable runtime without treating generated synchronous code as the teaching source.

**Inspection record:** commit `daa00b795450881c233253488e3ddeb362f59f56`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/FluentValidation/AbstractValidator.cs`, `src/FluentValidation/Internal/PropertyRule.cs`, `src/FluentValidation/Internal/RuleBase.cs`, `src/FluentValidation/Internal/RuleBuilder.cs`, `src/FluentValidation.Tests/AbstractValidatorTester.cs`, `src/FluentValidation.Tests/ConditionTests.cs`, `src/FluentValidation.Tests/CascadingFailuresTester.cs`, `src/FluentValidation.Tests/SyncAsyncParityTests.cs`, `License.txt`. GitHub Linguist label: C#.

</details>

### [serilog/serilog](https://github.com/serilog/serilog)

**Language 3 / Behavior 3 / Design 3 / Constraints 4 → Level 3**

A structured logging core that turns message templates and properties into immutable events routed through enrichers, filters, and sinks.

**Why study it:** The Logger path shows how Serilog parses and caches a message template, binds structured properties, enriches and filters one event, emits it to sinks, and contains extension failures.

**Prerequisites:**

- Basic familiarity with C# classes and interfaces, generics, delegates, nullable values, exceptions, asynchronous basics, and unit tests.

**Concepts this path develops:**

- Interface-composed enrichers, filters, and sinks.
- Message-template cache state.
- Stable message-template and property semantics.

**What you can learn:**

- Use `src/Serilog/Core/Logger.cs` to study the following transferable techniques and behaviors: Message-template tokenization, template caching, property binding, immutable log events, contextual enrichment, filtering, sink dispatch, dynamic levels, trace context, failure isolation, and synchronous and asynchronous disposal.

**Learning path:**

- **Goal:** Understand how Serilog parses and caches a message template, binds one structured event, enriches and filters it, emits it to sinks, and contains extension failures.
- **Start here:** [`src/Serilog/Core/Logger.cs`](https://github.com/serilog/serilog/blob/49b5339ce85385dc52d4d8e8f2b8308becf23506/src/Serilog/Core/Logger.cs) — src/Serilog/Core/Logger.cs owns Write, where level checks, message-template lookup, property binding, LogEvent creation, enrichment, filtering, and sink emission form one complete trace.
- **Then read:**
  - [`src/Serilog/LoggerConfiguration.cs`](https://github.com/serilog/serilog/blob/49b5339ce85385dc52d4d8e8f2b8308becf23506/src/Serilog/LoggerConfiguration.cs)
  - [`src/Serilog/Core/Pipeline/MessageTemplateCache.cs`](https://github.com/serilog/serilog/blob/49b5339ce85385dc52d4d8e8f2b8308becf23506/src/Serilog/Core/Pipeline/MessageTemplateCache.cs)
  - [`src/Serilog/Parsing/MessageTemplateParser.cs`](https://github.com/serilog/serilog/blob/49b5339ce85385dc52d4d8e8f2b8308becf23506/src/Serilog/Parsing/MessageTemplateParser.cs)
  - [`src/Serilog/Events/LogEvent.cs`](https://github.com/serilog/serilog/blob/49b5339ce85385dc52d4d8e8f2b8308becf23506/src/Serilog/Events/LogEvent.cs)
  - [`test/Serilog.Tests/Core/LoggerTests.cs`](https://github.com/serilog/serilog/blob/49b5339ce85385dc52d4d8e8f2b8308becf23506/test/Serilog.Tests/Core/LoggerTests.cs)
  - [`test/Serilog.Tests/Parsing/MessageTemplateParserTests.cs`](https://github.com/serilog/serilog/blob/49b5339ce85385dc52d4d8e8f2b8308becf23506/test/Serilog.Tests/Parsing/MessageTemplateParserTests.cs)
- **Trace:** Follow Logger.Write from level checking through MessageTemplateCache and MessageTemplateParser, property binding, LogEvent construction, enrichment, filtering, and sink emission; then correlate parser tokenization, property precedence, enricher-failure containment, dynamic level switches, trace context, binding, disposal, and async-disposal tests.

**Why this level:**

- **Language technique 3:** Substantial framework abstraction and typed pipeline idioms recur without reflection, unsafe code, or pervasive code generation.
- **Behavioral reasoning 3:** Caching, contextual state, events, failure paths, and cleanup materially affect the trace without expert concurrent scheduling.
- **Design span 3:** Several meaningful framework boundaries contribute directly to one structured event.
- **Constraint burden 4:** Several interacting compatibility, reliability, extension, and resource guarantees constrain pipeline changes.
- **Placement:** The four scores 3/3/3/4 sum to 13; their arithmetic mean is 3.25 and rounds half-up to Level 3. The published result is Level 3.

**License:** Apache-2.0 ([evidence 1](https://github.com/serilog/serilog/blob/49b5339ce85385dc52d4d8e8f2b8308becf23506/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Serilog is maintained and released as the core event pipeline for a production logging ecosystem of sinks and framework integrations.

**Language evidence:** Logger pipelines, structured events, message-template parsing, enrichment, filtering, sinks, configuration, and level switching are C#.

**Coding relevance:**

The logging model is concise and familiar; the path primarily teaches parser and cache design, interface-driven pipelines, contextual enrichment, fault containment, resource cleanup, and stable extension contracts.

Required domain context:

- A structured log event combines a parsed message template, bound properties, a level, timestamp, exception, and optional trace identifiers before enrichers, filters, and sinks process it.

**Eight-part quality gate:**

- **Source quality:** Logger.Write names each pipeline stage and makes disabled levels, binding failures, extension failures, filtering, and disposal behavior explicit.
- **Architecture:** LoggerConfiguration assembles the Logger, MessageTemplateCache and MessageTemplateParser produce templates, LogEvent carries data, and enricher, filter, and sink interfaces extend processing.
- **Naming and idiom:** Write, IsEnabled, MessageTemplateCache, MessageTemplateParser, BindMessageTemplate, LogEvent, Enrich, Filter, and sink preserve structured-logging vocabulary.
- **Tests:** LoggerTests and MessageTemplateParserTests cover tokenization, binding, cache-facing behavior, contextual properties, enrichers, filters, dynamic levels, trace capture, failures, and disposal.
- **Documentation:** Serilog's message-template, enrichment, filtering, sink, level, and lifecycle documentation explains the contracts implemented by this selected event path.
- **Traceability:** A Write call can be followed through level gating, cached parsing, property binding, LogEvent creation, enrichment, filtering, sink emission, and corresponding parser and logger assertions.
- **Maintainability:** Stable event and extension interfaces, a bounded template cache, explicit failure containment, and disposal tests localize pipeline changes.
- **Educational value:** The path demonstrates how a production structured logger turns text-like input into a typed extensible event while preserving reliability at every extension seam.

**Inspection record:** commit `49b5339ce85385dc52d4d8e8f2b8308becf23506`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/Serilog/Core/Logger.cs`, `src/Serilog/LoggerConfiguration.cs`, `src/Serilog/Core/Pipeline/MessageTemplateCache.cs`, `src/Serilog/Parsing/MessageTemplateParser.cs`, `src/Serilog/Events/LogEvent.cs`, `test/Serilog.Tests/Core/LoggerTests.cs`, `test/Serilog.Tests/Parsing/MessageTemplateParserTests.cs`, `LICENSE`. GitHub Linguist label: C#.

</details>

## Level 4

### [DapperLib/Dapper](https://github.com/DapperLib/Dapper)

**Language 4 / Behavior 3 / Design 3 / Constraints 4 → Level 4**

A lightweight object mapper that extends database connections with fast SQL execution and row-to-object materialization.

**Why study it:** The type-deserializer path shows how Dapper converts a data-reader row into a typed object by caching generated IL while preserving constructor, member, null, conversion, tuple, and type-handler contracts.

**Prerequisites:**

- Working familiarity with C# classes and interfaces, generics, delegates, nullable values, exceptions, asynchronous basics, and unit tests, plus experience tracing behavior across several production files.

**Concepts this path develops:**

- Reflection-driven constructor and member selection.
- Typed deserializer caching.
- Provider and runtime compatibility.

**What you can learn:**

- Use `Dapper/SqlMapper.TypeDeserializerCache.cs` to study the following transferable techniques and behaviors: Reflection-driven mapping, typed deserializer caches, DynamicMethod and ILGenerator, constructor selection, member binding, column conversion, null handling, tuple materialization, custom type handlers, and hot-path performance.

**Learning path:**

- **Goal:** Understand how Dapper converts one data-reader row into a typed object by caching a generated deserializer and honoring constructor, member, conversion, null, and type-handler contracts.
- **Start here:** [`Dapper/SqlMapper.TypeDeserializerCache.cs`](https://github.com/DapperLib/Dapper/blob/6d48ef664acc7298c649e2d449d903b3360d5a90/Dapper/SqlMapper.TypeDeserializerCache.cs) — Dapper/SqlMapper.TypeDeserializerCache.cs owns the row-shape and target-type cache that supplies generated materializer delegates, making it the clearest entrance before IL emission and type mapping.
- **Then read:**
  - [`Dapper/SqlMapper.cs`](https://github.com/DapperLib/Dapper/blob/6d48ef664acc7298c649e2d449d903b3360d5a90/Dapper/SqlMapper.cs)
  - [`Dapper/DefaultTypeMap.cs`](https://github.com/DapperLib/Dapper/blob/6d48ef664acc7298c649e2d449d903b3360d5a90/Dapper/DefaultTypeMap.cs)
  - [`tests/Dapper.Tests/ConstructorTests.cs`](https://github.com/DapperLib/Dapper/blob/6d48ef664acc7298c649e2d449d903b3360d5a90/tests/Dapper.Tests/ConstructorTests.cs)
  - [`tests/Dapper.Tests/TypeHandlerTests.cs`](https://github.com/DapperLib/Dapper/blob/6d48ef664acc7298c649e2d449d903b3360d5a90/tests/Dapper.Tests/TypeHandlerTests.cs)
- **Trace:** Follow TypeDeserializerCache as it keys and reuses row-reader delegates, then follow SqlMapper.GetTypeDeserializer and GenerateDeserializerFromMap as they inspect columns, select constructors or members through DefaultTypeMap, and emit conversion, null, tuple, and type-handler IL; correlate constructor selection and custom-handler behavior in the focused tests.

**Why this level:**

- **Language technique 4:** Reflection and runtime code generation are central rather than incidental to the materialization path.
- **Behavioral reasoning 3:** Cache state and numerous mapping branches materially affect behavior, but the bounded row conversion remains synchronous and lacks advanced nonlocal scheduling.
- **Design span 3:** Several meaningful framework boundaries contribute directly to one row materialization.
- **Constraint burden 4:** Several interacting correctness, compatibility, extensibility, and performance guarantees constrain changes to the emitted materializer.
- **Placement:** The four scores 4/3/3/4 sum to 14; their arithmetic mean is 3.50 and rounds half-up to Level 4. The published result is Level 4.

**License:** Apache-2.0 ([evidence 1](https://github.com/DapperLib/Dapper/blob/6d48ef664acc7298c649e2d449d903b3360d5a90/License.txt))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Dapper is released as production data-access infrastructure and is used by large .NET applications, including its original Stack Overflow use case.

**Language evidence:** SQL execution, parameter handling, mapping, caching, async operations, type handlers, and AOT support are implemented in C#.

**Coding relevance:**

This row-mapping context fits in a short paragraph; the selected path teaches reflection, dynamic IL generation, typed caches, constructor and member selection, conversion, null handling, and extensibility rather than database theory.

Required domain context:

- An ADO.NET data reader exposes typed columns for the current database row, which Dapper maps into a requested object constructor and members.

**Eight-part quality gate:**

- **Source quality:** The bounded materializer path names cache lookup, type-map selection, constructor and member branches, conversion, null handling, tuple logic, and type-handler emission despite intricate IL.
- **Architecture:** TypeDeserializerCache stores delegates, SqlMapper emits materializers, DefaultTypeMap selects constructors and members, and type handlers provide an explicit extension point.
- **Naming and idiom:** TypeDeserializerCache, GetReader, GetTypeDeserializer, GenerateDeserializerFromMap, DefaultTypeMap, FindConstructor, members, and type handlers expose row materialization.
- **Tests:** ConstructorTests and TypeHandlerTests cover constructor selection, member mapping, null and conversion behavior, custom handlers, error cases, and cache-facing compatibility.
- **Documentation:** The README, API examples, and package documentation provide the mapping and type-handler context needed to follow the selected generated materializer.
- **Traceability:** A reader shape can be followed through TypeDeserializerCache into GetTypeDeserializer, DefaultTypeMap selection, emitted load and conversion IL, and constructor or type-handler tests.
- **Maintainability:** Named cache and type-map seams plus compatibility tests constrain changes to generated code that sits on a performance-critical public boundary.
- **Educational value:** The path demonstrates how reflection and runtime code generation can produce a fast typed mapping API while retaining explicit extension and compatibility rules.

**Inspection record:** commit `6d48ef664acc7298c649e2d449d903b3360d5a90`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `Dapper/SqlMapper.TypeDeserializerCache.cs`, `Dapper/SqlMapper.cs`, `Dapper/DefaultTypeMap.cs`, `tests/Dapper.Tests/ConstructorTests.cs`, `tests/Dapper.Tests/TypeHandlerTests.cs`, `License.txt`. GitHub Linguist label: C#.

</details>

### [dotnet/aspnetcore](https://github.com/dotnet/aspnetcore)

**Language 4 / Behavior 3 / Design 3 / Constraints 4 → Level 4**

The ASP.NET Core web platform, including HTTP servers, middleware, routing, hosting, MVC, Razor, Blazor, SignalR, security, and deployment integrations.

**Why study it:** The ApplicationBuilder path shows how ASP.NET Core folds middleware into an ordered request-delegate pipeline and adapts both conventional and factory-created components with dependency injection and reliable release.

**Prerequisites:**

- Working familiarity with C# classes and interfaces, generics, delegates, nullable values, exceptions, asynchronous basics, and unit tests, plus experience tracing behavior across several production files.

**Concepts this path develops:**

- Higher-order RequestDelegate composition.
- Ordered nested async execution and short circuiting.
- Middleware signature and DI compatibility.

**What you can learn:**

- Use `src/Http/Http/src/Builder/ApplicationBuilder.cs` to study the following transferable techniques and behaviors: Higher-order RequestDelegate composition, reverse pipeline folding, asynchronous ordering and short circuits, reflection-based Invoke discovery, expression compilation, AOT-compatible fallback, injected and keyed services, per-request activation, and finally-based release.

**Learning path:**

- **Goal:** Understand how ASP.NET Core composes an ordered request-delegate pipeline and adapts conventional or factory-created middleware with dependency injection and reliable per-request release.
- **Start here:** [`src/Http/Http/src/Builder/ApplicationBuilder.cs`](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/src/Http/Http/src/Builder/ApplicationBuilder.cs) — ApplicationBuilder.cs contains Use and Build, which reveal how middleware factories are stored and folded around a terminal RequestDelegate before adaptation details are introduced.
- **Then read:**
  - [`src/Http/Http.Abstractions/src/IApplicationBuilder.cs`](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/src/Http/Http.Abstractions/src/IApplicationBuilder.cs)
  - [`src/Http/Http.Abstractions/src/Extensions/UseMiddlewareExtensions.cs`](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/src/Http/Http.Abstractions/src/Extensions/UseMiddlewareExtensions.cs)
  - [`src/Http/Http.Abstractions/src/IMiddleware.cs`](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/src/Http/Http.Abstractions/src/IMiddleware.cs)
  - [`src/Http/Http.Abstractions/src/IMiddlewareFactory.cs`](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/src/Http/Http.Abstractions/src/IMiddlewareFactory.cs)
  - [`src/Http/Http/src/MiddlewareFactory.cs`](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/src/Http/Http/src/MiddlewareFactory.cs)
  - [`src/Http/Http/test/ApplicationBuilderTests.cs`](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/src/Http/Http/test/ApplicationBuilderTests.cs)
  - [`src/Http/Http.Abstractions/test/UseMiddlewareTest.cs`](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/src/Http/Http.Abstractions/test/UseMiddlewareTest.cs)
- **Trace:** Follow ApplicationBuilder.Use as it stores middleware factories and Build as it folds them in reverse around the terminal delegate, then follow UseMiddlewareExtensions as it validates Invoke or InvokeAsync, chooses compiled-expression or reflection fallback service injection, or creates IMiddleware per request and releases it in finally; correlate ordering, terminal, endpoint, signature, service, factory, and release tests.

**Why this level:**

- **Language technique 4:** Reflection, expression compilation, and sophisticated delegate composition are central to middleware adaptation.
- **Behavioral reasoning 3:** Async ordering, lifecycle, and fallback behavior materially affect requests, but the bounded pipeline does not require advanced protocol or distributed state reasoning.
- **Design span 3:** Several meaningful framework boundaries contribute directly to one middleware invocation.
- **Constraint burden 4:** Several interacting compatibility, reliability, extensibility, and resource guarantees constrain the pipeline.
- **Placement:** The four scores 4/3/3/4 sum to 14; their arithmetic mean is 3.50 and rounds half-up to Level 4. The published result is Level 4.

**License:** MIT ([evidence 1](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Microsoft ships ASP.NET Core as the production web framework and server stack for modern .NET applications.

**Language evidence:** HTTP abstractions, Kestrel, hosting, routing, middleware, MVC, Razor, Blazor, SignalR, authentication, and data protection are predominantly C# with first-party web client code.

**Coding relevance:**

The middleware model fits in a short prerequisite paragraph; this corrected path teaches delegate composition, reflection and expression compilation, dependency injection, per-request activation and release, async control flow, and runtime fallback rather than HTTP protocol rules.

Required domain context:

- An ASP.NET Core request pipeline is an ordered nesting of middleware delegates; each component can perform work before and after calling the next component or short-circuit the request.

**Eight-part quality gate:**

- **Source quality:** ApplicationBuilder and UseMiddlewareExtensions make ordering, terminal behavior, signature validation, invocation branches, service resolution, and release paths explicit.
- **Architecture:** IApplicationBuilder defines composition, ApplicationBuilder builds delegates, UseMiddlewareExtensions supplies conventional and interface binders, and IMiddlewareFactory owns per-request activation and release.
- **Naming and idiom:** Use, Build, RequestDelegate, UseMiddleware, Invoke, InvokeAsync, IMiddleware, IMiddlewareFactory, Create, and Release expose the pipeline contract.
- **Tests:** ApplicationBuilderTests and UseMiddlewareTest cover ordering, terminal and endpoint mistakes, signature validation, dependency and keyed-service injection, dynamic-code fallback, factory failures, and release.
- **Documentation:** Source documentation for ApplicationBuilder, UseMiddlewareExtensions, the middleware interfaces, and MiddlewareFactory explains composition, invocation, dependency injection, activation, and release contracts.
- **Traceability:** A Use call can be followed into reverse Build folding, conventional reflection or compiled binding, interface-factory creation, asynchronous invocation, and finally release with direct tests.
- **Maintainability:** Stable delegate and factory interfaces, explicit binder branches, AOT fallback coverage, and lifecycle tests isolate middleware extensibility from pipeline composition.
- **Educational value:** The path demonstrates how a compact higher-order pipeline supports reflection, dependency injection, per-request ownership, and ahead-of-time constraints without losing traceability.

**Inspection record:** commit `8c1a406592b06b954acac509fa4725ca560b2e53`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/Http/Http/src/Builder/ApplicationBuilder.cs`, `src/Http/Http.Abstractions/src/IApplicationBuilder.cs`, `src/Http/Http.Abstractions/src/Extensions/UseMiddlewareExtensions.cs`, `src/Http/Http.Abstractions/src/IMiddleware.cs`, `src/Http/Http.Abstractions/src/IMiddlewareFactory.cs`, `src/Http/Http/src/MiddlewareFactory.cs`, `src/Http/Http/test/ApplicationBuilderTests.cs`, `src/Http/Http.Abstractions/test/UseMiddlewareTest.cs`, `LICENSE.txt`. GitHub Linguist label: C#.

</details>

## Level 5

### [dotnet/roslyn](https://github.com/dotnet/roslyn)

**Language 5 / Behavior 5 / Design 5 / Constraints 5 → Level 5**

The open-source C# and Visual Basic compiler platform that exposes syntax, semantic, diagnostic, compilation, and emit APIs used by the .NET toolchain.

**Why study it:** The compilation-to-emit path shows how a platform-scale C# system turns immutable syntax, references, and options into diagnostics or deterministic PE and PDB output while coordinating binding, flow analysis, concurrent method compilation, lowering, IL generation, metadata, compatibility, and cleanup.

**Prerequisites:**

- Strong working familiarity with C# classes and interfaces, generics, delegates, nullable values, exceptions, asynchronous basics, and unit tests, plus experience tracing state, resources, or asynchronous control flow across many production files.

**Concepts this path develops:**

- Recursive generic symbol, visitor, builder, and CCI adapter hierarchies.
- Staged parse, declaration, bind, flow, lower, codegen, and serialization state.
- C# language and CLR metadata correctness.

**What you can learn:**

- Use `src/Compilers/Core/Portable/Compilation/Compilation.cs` to study the following transferable techniques and behaviors: Public stream and option validation, immutable compilation snapshots, staged diagnostics, module-builder specialization, concurrent symbol traversal, binding and flow analysis, lowering and instrumentation, IL generation, entry-point selection, deterministic PE and PDB serialization, cancellation, pooled resources, and compatibility-preserving APIs.

**Learning path:**

- **Goal:** Understand how Roslyn validates an emit request and turns one immutable CSharpCompilation into either stable diagnostics or deterministic PE and PDB output.
- **Start here:** [`src/Compilers/Core/Portable/Compilation/Compilation.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/Core/Portable/Compilation/Compilation.cs) — Compilation.cs owns the public Emit boundary, validates streams and options, creates the language-specific module builder, invokes compilation, generates resources and documentation, gates serialization on diagnostics, and returns EmitResult.
- **Then read:**
  - [`src/Compilers/CSharp/Portable/Compilation/CSharpCompilation.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Portable/Compilation/CSharpCompilation.cs)
  - [`src/Compilers/CSharp/Portable/Compiler/MethodCompiler.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Portable/Compiler/MethodCompiler.cs)
  - [`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter.cs)
  - [`src/Compilers/CSharp/Portable/CodeGen/CodeGenerator.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Portable/CodeGen/CodeGenerator.cs)
  - [`src/Compilers/CSharp/Portable/Emitter/Model/PEModuleBuilder.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Portable/Emitter/Model/PEModuleBuilder.cs)
  - [`src/Compilers/Core/Portable/Emit/CommonPEModuleBuilder.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/Core/Portable/Emit/CommonPEModuleBuilder.cs)
  - [`src/Compilers/Core/Portable/PEWriter/PeWriter.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/Core/Portable/PEWriter/PeWriter.cs)
  - [`src/Compilers/CSharp/Test/Emit/Emit/CompilationEmitTests.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Test/Emit/Emit/CompilationEmitTests.cs)
  - [`src/Compilers/CSharp/Test/Emit/Emit/EntryPointTests.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Test/Emit/Emit/EntryPointTests.cs)
  - [`src/Compilers/CSharp/Test/Emit/Emit/DeterministicTests.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Test/Emit/Emit/DeterministicTests.cs)
  - [`src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncMainTests.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncMainTests.cs)
  - [`src/Compilers/CSharp/Test/Emit2/PDB/CSharpDeterministicBuildCompilationTests.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Test/Emit2/PDB/CSharpDeterministicBuildCompilationTests.cs)
  - [`docs/wiki/Roslyn-Overview.md`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/docs/wiki/Roslyn-Overview.md)
  - [`docs/compilers/README.md`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/docs/compilers/README.md)
- **Trace:** Follow Compilation.Emit through stream and option checks into CheckOptionsAndCreateModuleBuilder, then into CSharpCompilation.CreateModuleBuilder and CompileMethods; trace parse and declaration diagnostics into MethodCompiler's concurrent symbol traversal, binding, flow analysis, LocalRewriter transformations, CodeGenerator IL construction, async entry-point synthesis, and PEModuleBuilder metadata; follow stored method bodies and entry point through CommonPEModuleBuilder into PeWriter and return to Compilation.SerializeToPeStream for deterministic PE and optional PDB output, then correlate staged errors, entry-point rules, executed async Main, emitted artifacts, platform changes, and repeatable PE, MVID, and supported PDB data in the selected tests.

**Why this level:**

- **Language technique 5:** Several advanced C# mechanisms interact pervasively: recursive generic and visitor hierarchies, language-specific adapters, synthesized symbols, nullable and pattern-based modeling, task concurrency, pooled ownership, immutable snapshots, and low-level metadata and IL builders.
- **Behavioral reasoning 5:** Concurrency, staged transformation state, diagnostics, synthesized code, failure containment, cancellation, and resource lifecycles interact pervasively and require expert nonlocal reasoning.
- **Design span 5:** The representative behavior coordinates several major compiler and runtime-format subsystems through shared abstractions and language-specific implementations.
- **Constraint burden 5:** Language semantics, emitted-runtime correctness, stable diagnostics, concurrency, determinism, compatibility, performance, resources, and platform-specific output guarantees constrain changes across the entire path.
- **Placement:** The four scores 5/5/5/5 sum to 20; their arithmetic mean is 5.00. Four expert dimensions satisfy the Level 5 guardrail, so the published result is Level 5.

**License:** MIT ([evidence 1](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/License.txt))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Roslyn supplies the production C# and Visual Basic compilers and code-analysis APIs shipped through the .NET SDK, Visual Studio, and Microsoft.CodeAnalysis packages.

**Language evidence:** The selected public compilation API, C# compiler pipeline, lowering, IL generation, emitter model, and focused compiler tests are implemented in first-party C#; GitHub also reports C# as the repository's primary language.

**Coding relevance:**

The compiler vocabulary fits in a bounded primer and is documented by the project; the selected path primarily teaches transferable immutable modeling, staged pipelines, concurrency, diagnostics, transformation passes, serialization, deterministic builds, compatibility, and resource discipline.

Required domain context:

- A compiler parses source into syntax, declares and binds symbols, analyzes and lowers method bodies, generates intermediate-language instructions, and serializes an assembly plus optional debug information.

**Eight-part quality gate:**

- **Source quality:** The emit boundary, diagnostic stages, fork-join strategy, per-method failure isolation, lowering handoff, serialization gates, and cleanup are explicit and carry unusually detailed invariant comments.
- **Architecture:** Common Compilation orchestrates the lifecycle, CSharpCompilation specializes language diagnostics and module creation, MethodCompiler binds and lowers symbols, LocalRewriter transforms bound trees, CodeGenerator produces IL, and PEModuleBuilder exposes metadata to the serializer.
- **Naming and idiom:** Compilation, Emit, CreateModuleBuilder, CompileMethods, MethodCompiler, BindMethodBody, FlowAnalysisPass, LowerBodyOrInitializer, CodeGenerator, PEModuleBuilder, diagnostics, and EmitResult preserve compiler-stage vocabulary.
- **Tests:** CompilationEmitTests directly checks staged errors and emitted stream behavior, EntryPointTests exercises executable entry-point selection and diagnostics, CodeGenAsyncMainTests executes async entry points and verifies synthesized forwarding IL, DeterministicTests compares module identifiers and emitted bytes, and the deterministic-build PDB suite checks embedded PDB options and reference metadata. Coverage of the complete platform is intentionally distributed across many suites.
- **Documentation:** The repository overview, compiler support guide, and source documentation explain the public compiler pipeline, immutable compilation model, diagnostics, emit semantics, compatibility overloads, concurrency invariants, platform support, and major representation boundaries.
- **Traceability:** A public Emit call can be followed through option validation, language-specific module construction, diagnostics, method compilation, lowering, IL and metadata production, PE and PDB serialization, EmitResult, and end-to-end assertions.
- **Maintainability:** Stable phase boundaries, immutable public models, deterministic tests, per-method diagnostic bags, cancellation checks, pooled-resource cleanup, compatibility annotations, and explicit finish hooks make cross-cutting changes reviewable despite the platform scale.
- **Educational value:** The path is a rare production example of a complete compiler backend and public platform API in which concurrency, transformation passes, diagnostics, compatibility, deterministic output, and failure discipline remain observable.

**Inspection record:** commit `8323a94cb432bbffad016d4f6d7e04ee0f8419f2`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/Compilers/Core/Portable/Compilation/Compilation.cs`, `src/Compilers/CSharp/Portable/Compilation/CSharpCompilation.cs`, `src/Compilers/CSharp/Portable/Compiler/MethodCompiler.cs`, `src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter.cs`, `src/Compilers/CSharp/Portable/CodeGen/CodeGenerator.cs`, `src/Compilers/CSharp/Portable/Emitter/Model/PEModuleBuilder.cs`, `src/Compilers/Core/Portable/Emit/CommonPEModuleBuilder.cs`, `src/Compilers/Core/Portable/PEWriter/PeWriter.cs`, `src/Compilers/CSharp/Test/Emit/Emit/CompilationEmitTests.cs`, `src/Compilers/CSharp/Test/Emit/Emit/EntryPointTests.cs`, `src/Compilers/CSharp/Test/Emit/Emit/DeterministicTests.cs`, `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncMainTests.cs`, `src/Compilers/CSharp/Test/Emit2/PDB/CSharpDeterministicBuildCompilationTests.cs`, `docs/wiki/Roslyn-Overview.md`, `docs/compilers/README.md`, `README.md`, `License.txt`. GitHub Linguist label: C#.

</details>

### [dotnet/runtime](https://github.com/dotnet/runtime)

**Language 4 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

The cross-platform .NET runtime, including the CLR, JIT, garbage collector, type system, core libraries, interop, diagnostics, and native hosting.

**Why study it:** The TaskAwaiter path exposes how .NET registers and runs an await continuation while preserving contexts, scheduler policy, race safety, inlining rules, fault behavior, and forced asynchronous execution.

**Prerequisites:**

- Strong working familiarity with C# classes and interfaces, generics, delegates, nullable values, exceptions, asynchronous basics, and unit tests, plus experience tracing state, resources, or asynchronous control flow across many production files.

**Concepts this path develops:**

- Awaiter and async-state-machine interfaces.
- Lock-free registration versus completion races.
- Memory ordering and exactly-once continuation execution.

**What you can learn:**

- Use `src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/TaskAwaiter.cs` to study the following transferable techniques and behaviors: Awaiter and async-state-machine interfaces, Task continuation registration, SynchronizationContext and TaskScheduler capture, ExecutionContext flow, lock-free completion races, inline versus queued execution, ThreadPool scheduling, cancellation, faults, and exactly-once guarantees.

**Learning path:**

- **Goal:** Understand how an awaited Task registers and eventually runs a continuation while preserving execution context, scheduler and synchronization-context policy, race safety, inlining rules, and asynchronous-continuation guarantees.
- **Start here:** [`src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/TaskAwaiter.cs`](https://github.com/dotnet/runtime/blob/c4eee2b76e574b0dd6cfe3387220a905ba69aca6/src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/TaskAwaiter.cs) — TaskAwaiter.cs contains OnCompletedInternal, the compiler-facing handoff that turns an await into Task continuation registration with explicit context and scheduling policy.
- **Then read:**
  - [`src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/Task.cs`](https://github.com/dotnet/runtime/blob/c4eee2b76e574b0dd6cfe3387220a905ba69aca6/src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/Task.cs)
  - [`src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/TaskContinuation.cs`](https://github.com/dotnet/runtime/blob/c4eee2b76e574b0dd6cfe3387220a905ba69aca6/src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/TaskContinuation.cs)
  - [`src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/ThreadPoolTaskScheduler.cs`](https://github.com/dotnet/runtime/blob/c4eee2b76e574b0dd6cfe3387220a905ba69aca6/src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/ThreadPoolTaskScheduler.cs)
  - [`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/System.Runtime.CompilerServices/TaskAwaiterTests.cs`](https://github.com/dotnet/runtime/blob/c4eee2b76e574b0dd6cfe3387220a905ba69aca6/src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/System.Runtime.CompilerServices/TaskAwaiterTests.cs)
  - [`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/RunContinuationsAsynchronouslyTests.cs`](https://github.com/dotnet/runtime/blob/c4eee2b76e574b0dd6cfe3387220a905ba69aca6/src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/RunContinuationsAsynchronouslyTests.cs)
  - [`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/ExecutionContextFlowTest.cs`](https://github.com/dotnet/runtime/blob/c4eee2b76e574b0dd6cfe3387220a905ba69aca6/src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/ExecutionContextFlowTest.cs)
- **Trace:** Follow TaskAwaiter.OnCompletedInternal into Task.SetContinuationForAwait as it chooses a SynchronizationContext, non-default TaskScheduler, ExecutionContext-capturing continuation, or direct state-machine registration; follow AddTaskContinuation's completion race and FinishContinuations into AwaitTaskContinuation inlining or ThreadPoolTaskScheduler queuing, then correlate scheduler/context capture, ConfigureAwait, forced asynchronous continuations, execution-context lifetime, and race behavior in the focused tests.

**Why this level:**

- **Language technique 4:** Advanced async, generic, low-level synchronization, and runtime-specific C# techniques are central, while the bounded path does not require multiple pervasive Level 5 language mechanisms.
- **Behavioral reasoning 5:** Multiple expert concurrency, scheduling, lifecycle, and nonlocal state concerns are pervasive and tightly coupled.
- **Design span 4:** The trace crosses broad runtime architecture and many core subsystems while remaining bounded to continuation execution.
- **Constraint burden 5:** System-wide runtime safety, correctness, compatibility, observability, and performance guarantees interact throughout the path.
- **Placement:** The four scores 4/5/4/5 sum to 18; their arithmetic mean is 4.50 and rounds half-up to Level 5. The published result is Level 5.

**License:** MIT ([evidence 1](https://github.com/dotnet/runtime/blob/c4eee2b76e574b0dd6cfe3387220a905ba69aca6/LICENSE.TXT))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Microsoft ships this repository as the production runtime and standard libraries underlying .NET applications across operating systems and architectures.

**Language evidence:** Core libraries are C#, while the CLR, garbage collector, JIT, native hosting, interop, and platform layers use C++, C, and assembly as first-party runtime implementation.

**Coding relevance:**

The selected all-C# path is core transferable runtime programming: await continuation registration, captured execution context, synchronization and scheduler choice, lock-free completion, inlining, queuing, cancellation, and error behavior.

No specialist domain context is required.

**Eight-part quality gate:**

- **Source quality:** TaskAwaiter, Task, continuation, and scheduler code documents registration, completion races, context capture, inlining, queuing, cancellation, and debugger invariants extensively.
- **Architecture:** The compiler awaiter boundary delegates to Task state, specialized continuation objects, SynchronizationContext, TaskScheduler, ExecutionContext, and ThreadPoolTaskScheduler.
- **Naming and idiom:** OnCompletedInternal, SetContinuationForAwait, AddTaskContinuation, FinishContinuations, AwaitTaskContinuation, RunContinuationsAsynchronously, and scheduler names expose the lifecycle.
- **Tests:** The selected TaskAwaiter, RunContinuationsAsynchronously, and ExecutionContextFlow suites cover scheduler and context capture, ConfigureAwait, races, forced queuing, context lifetime, faults, and platform cases.
- **Documentation:** Extensive invariants in the TaskAwaiter, Task, continuation, and scheduler source comments document context capture, continuation scheduling, race handling, and exactly-once execution for this path.
- **Traceability:** An await can be followed from TaskAwaiter.OnCompletedInternal through continuation selection and race-safe registration into completion-time inlining or ThreadPoolTaskScheduler queuing and focused tests.
- **Maintainability:** Documented invariants, specialized continuation types, low-level synchronization boundaries, and targeted concurrency tests protect a performance-critical runtime contract.
- **Educational value:** The path gives expert learners a concrete account of async continuation semantics beneath the language syntax, including the races and context policies ordinary code depends on.

**Inspection record:** commit `c4eee2b76e574b0dd6cfe3387220a905ba69aca6`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/TaskAwaiter.cs`, `src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/Task.cs`, `src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/TaskContinuation.cs`, `src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/ThreadPoolTaskScheduler.cs`, `src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/System.Runtime.CompilerServices/TaskAwaiterTests.cs`, `src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/RunContinuationsAsynchronouslyTests.cs`, `src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/ExecutionContextFlowTest.cs`, `LICENSE.TXT`. GitHub Linguist label: C#.

</details>

_Generated from `catalog/c-sharp.json`; do not edit by hand._

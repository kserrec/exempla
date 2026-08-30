# Kotlin

7 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

**Source legend:** Production software is built primarily for real users or systems. Educational exemplars are complete teaching-oriented software and may appear only at Levels 1 and 2.

[← All languages](../README.md)

## Level 1 — First real code

### [JetBrains/kotlin](https://github.com/JetBrains/kotlin)

**Language 1 / Behavior 1 / Design 1 / Constraints 1 → Level 1**

**Source:** Production software

Kotlin's production standard library returns the text after the first string delimiter, the original string when it is missing, or a caller-supplied fallback.

**Why study it:** Follow one familiar string operation through delimiter search, a missing-result branch, substring boundaries, defaults, and direct examples.

**Prerequisites:**

- The global novice Kotlin baseline: functions, extension functions, parameters, default arguments, val, conditionals, string indices, indexOf, substring, and focused assertions.
- indexOf returns -1 when the delimiter is absent; a delimiter found at the end produces an empty suffix.

**Concepts this path develops:**

- Building a string helper from search and slicing primitives.
- Making missing-delimiter behavior configurable through a default parameter.
- Testing found, end-of-string, missing, and custom-fallback cases.

**What you can learn:**

- Find the first occurrence of a delimiter string.
- Return a fallback when the search reports no match.
- Start the result after the full delimiter and allow an empty suffix.

**Learning path:**

- **Goal:** Understand how Kotlin's standard library defines the result after a delimiter, including both forms of missing-delimiter behavior.
- **Start here:** [`libraries/stdlib/src/kotlin/text/Strings.kt`](https://github.com/JetBrains/kotlin/blob/b143655f3dca9afacf7ef5e10f40868cc7e28f43/libraries/stdlib/src/kotlin/text/Strings.kt) — The KDoc and complete string-delimiter overload of substringAfter appear together in this file.
- **Then read:**
  - [`libraries/stdlib/test/text/StringTest.kt`](https://github.com/JetBrains/kotlin/blob/b143655f3dca9afacf7ef5e10f40868cc7e28f43/libraries/stdlib/test/text/StringTest.kt)
  - [`ReadMe.md`](https://github.com/JetBrains/kotlin/blob/b143655f3dca9afacf7ef5e10f40868cc7e28f43/ReadMe.md)
  - [`license/README.md`](https://github.com/JetBrains/kotlin/blob/b143655f3dca9afacf7ef5e10f40868cc7e28f43/license/README.md)
  - [`license/LICENSE.txt`](https://github.com/JetBrains/kotlin/blob/b143655f3dca9afacf7ef5e10f40868cc7e28f43/license/LICENSE.txt)
- **Trace:** Call indexOf with the delimiter, return missingDelimiterValue when the result is -1, otherwise call substring from index plus delimiter length to the string length, then match the focused test's found, trailing, missing, and custom-fallback assertions.

**Why this level:**

- **Language technique 1:** The implementation uses introductory Kotlin function, value, conditional, and string operations.
- **Behavioral reasoning 1:** One local search result selects between a fallback and one substring calculation.
- **Design span 1:** One source function and one direct test section contain the complete selected contract.
- **Constraint burden 1:** The function has a small explicit string contract with locally tested edge cases.
- **Novice accessibility floor 1:** All behavior uses novice string and branch operations; extension syntax needs one local sentence and introduces no extra state or architecture.
  - **Central concepts:** string search; if expression; default argument; substring boundaries
  - **Incidental concepts:** extension-function receiver syntax
- **Placement:** The four scores 1/1/1/1 produce rubric Level 1. Novice accessibility floor 1 preserves published Level 1.

**License:** Apache-2.0 AND LicenseRef-Third-Party-Notices ([evidence 1](https://github.com/JetBrains/kotlin/blob/b143655f3dca9afacf7ef5e10f40868cc7e28f43/license/README.md), [evidence 2](https://github.com/JetBrains/kotlin/blob/b143655f3dca9afacf7ef5e10f40868cc7e28f43/license/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** This official repository builds Kotlin and its shipped standard library; substringAfter is a documented public kotlin.text extension used by Kotlin programs across supported platforms.

**Language evidence:** The standard-library substringAfter implementation, its KDoc, and its focused multiplatform tests are first-party Kotlin; GitHub labels the repository Kotlin.

**Coding relevance:**

String search, slicing, sentinel handling, default parameters, and edge-case tests transfer directly to everyday application code.

No specialist domain context is required.

**Eight-part quality gate:**

- **Source quality:** The handwritten standard-library function exposes its entire search, branch, and slice sequence in three statements.
- **Architecture:** The extension composes existing string primitives and stays beside the related before, last, and delimiter overloads.
- **Naming and idiom:** substringAfter, delimiter, and missingDelimiterValue state the operation and both outcomes using ordinary Kotlin conventions.
- **Tests:** substringDelimited directly covers a string delimiter, a delimiter at the end, a missing delimiter with the default original-string result, and a custom fallback.
- **Documentation:** The source KDoc defines first-occurrence, missing-delimiter, and fallback behavior, while the repository documentation establishes the official standard-library context.
- **Traceability:** Found assertions follow the substring branch; the two missing assertions distinguish the default and caller-supplied fallback paths.
- **Maintainability:** The implementation delegates search and slicing semantics to established string primitives while keeping policy in one branch.
- **Educational value:** The path turns familiar string operations into a complete, precisely tested public API contract.

**Inspection record:** commit `b143655f3dca9afacf7ef5e10f40868cc7e28f43`, inspected 2026-08-30. Review passes: Codex 85% Level 1 investigation; Codex resumed-session source verification. Files inspected: `libraries/stdlib/src/kotlin/text/Strings.kt`, `libraries/stdlib/test/text/StringTest.kt`, `ReadMe.md`, `license/README.md`, `license/LICENSE.txt`. GitHub Linguist label: Kotlin.

</details>

## Level 2 — Guided real-world patterns

No qualified learning path has been published at this level. Standards are not lowered to fill a slot.

## Level 3 — Intermediate production software

### [ajalt/clikt](https://github.com/ajalt/clikt)

**Language 3 / Behavior 3 / Design 3 / Constraints 4 → Level 3**

**Source:** Production software

A multiplatform Kotlin framework for type-safe command-line applications with nested commands, composable parameters, generated help, and shell completion.

**Why study it:** Starting at CommandLineParser shows how a declarative Kotlin command model becomes normalized tokens, recursive invocations, finalized option values, validation results, and executable subcommands.

**Short context:**

- A command-line parser maps option and argument tokens into typed command invocations, including nested subcommands.

**Prerequisites:**

- Basic familiarity with Kotlin classes and interfaces, generics, null safety, lambdas, coroutine basics, and unit tests.

**Concepts this path develops:**

- Generic command and invocation types.
- Mutable token-consumption state.
- Grouped, attached, transformed, and interspersed token forms.

**What you can learn:**

- Use `CommandLineParser.kt` to study property delegates, staged parsing, token normalization, alias and argument-file expansion, recursive command trees, typed option finalization, validation, and direct option and subcommand contracts.

**Learning path:**

- **Goal:** Understand how Clikt turns a delegated command DSL into recursively parsed, finalized, validated, and executable command invocations.
- **Start here:** [`clikt/src/commonMain/kotlin/com/github/ajalt/clikt/parsers/CommandLineParser.kt`](https://github.com/ajalt/clikt/blob/fa2e48c54995a88d492f05568a64889d99994877/clikt/src/commonMain/kotlin/com/github/ajalt/clikt/parsers/CommandLineParser.kt) — CommandLineParser names the tokenize, parse, eager-finalization, value-finalization, validation, and run stages and connects them to the selected command and option abstractions.
- **Then read:**
  - [`clikt/src/commonMain/kotlin/com/github/ajalt/clikt/parsers/ParserInternals.kt`](https://github.com/ajalt/clikt/blob/fa2e48c54995a88d492f05568a64889d99994877/clikt/src/commonMain/kotlin/com/github/ajalt/clikt/parsers/ParserInternals.kt)
  - [`clikt/src/commonMain/kotlin/com/github/ajalt/clikt/parameters/options/Option.kt`](https://github.com/ajalt/clikt/blob/fa2e48c54995a88d492f05568a64889d99994877/clikt/src/commonMain/kotlin/com/github/ajalt/clikt/parameters/options/Option.kt)
  - [`test/src/commonTest/kotlin/com/github/ajalt/clikt/parameters/OptionTest.kt`](https://github.com/ajalt/clikt/blob/fa2e48c54995a88d492f05568a64889d99994877/test/src/commonTest/kotlin/com/github/ajalt/clikt/parameters/OptionTest.kt)
  - [`test/src/commonTest/kotlin/com/github/ajalt/clikt/parameters/SubcommandTest.kt`](https://github.com/ajalt/clikt/blob/fa2e48c54995a88d492f05568a64889d99994877/test/src/commonTest/kotlin/com/github/ajalt/clikt/parameters/SubcommandTest.kt)
  - [`README.md`](https://github.com/ajalt/clikt/blob/fa2e48c54995a88d492f05568a64889d99994877/README.md)
  - [`LICENSE.txt`](https://github.com/ajalt/clikt/blob/fa2e48c54995a88d492f05568a64889d99994877/LICENSE.txt)
- **Trace:** Start with tokenize, parse, finalize, and run, follow CommandParser as it normalizes tokens, expands aliases and argument files, distinguishes long, short, numeric, argument, and subcommand cases, then trace option finalization and validation into the direct option and nested-subcommand tests.

**Why this level:**

- **Language technique 3:** Generics, delegates, and framework idioms materially shape the trace; the lower anchor controls because advanced type or implicit machinery does not recur pervasively.
- **Behavioral reasoning 3:** A nontrivial synchronous parser lifecycle materially affects the trace without advanced concurrent or recovery behavior.
- **Design span 3:** Several meaningful parsing, model, lifecycle, and verification boundaries cooperate.
- **Constraint burden 4:** Multiple grammar, extension, validation, portability, and compatibility guarantees interact throughout the parser.
- **Placement:** The four scores 3/3/3/4 sum to 13; their arithmetic mean is 3.25 and rounds half-up to Level 3. The published result is Level 3.

**License:** Apache-2.0 ([evidence 1](https://github.com/ajalt/clikt/blob/fa2e48c54995a88d492f05568a64889d99994877/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** Clikt publishes current core, full, and Markdown artifacts on Maven Central and maintains documentation and sample applications for JVM, Node.js, and native targets.

**Language evidence:** Command modeling, tokenization and parsing, property-delegated parameters, transformations, validation, value sources, help formatting, completion generation, and platform types are Kotlin.

**Coding relevance:**

The concise command-line vocabulary is subordinate to reusable lessons in delegated APIs, token-state machines, recursive parsing, extension boundaries, error aggregation, validation, and compatibility-oriented tests.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Token normalization, invocation records, option transformation, finalization, validation, and command execution are separated into named stages with explicit errors.
- **Architecture:** CommandLineParser coordinates ParserInternals, command invocation trees, and Option finalizers; the selected tests close option and nested-subcommand behavior.
- **Naming and idiom:** CommandInvocation, OptionInvocation, finalizeEagerOptions, finalizeCommand, TransformContext, and ValueSource expose the parser lifecycle.
- **Tests:** OptionTest and SubcommandTest exercise option conversion and validation, token forms, eager options, nested commands, command selection, and related failure cases used by this trace.
- **Documentation:** The README introduces the declarative command and option model, shows representative usage, and links the reference material a learner needs before entering the parser.
- **Traceability:** A command-line token can be followed through normalization and invocation collection into option finalization, validation, command selection, and the direct option or subcommand assertions.
- **Maintainability:** Parser stages, invocation data, command structure, and option transformations remain separate, so changes to one selected boundary do not require rewriting the whole trace.
- **Educational value:** This path demonstrates the machinery beneath a type-safe declarative API without requiring the unrelated help, rich-output, or completion subsystems.

**Inspection record:** commit `fa2e48c54995a88d492f05568a64889d99994877`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `clikt/src/commonMain/kotlin/com/github/ajalt/clikt/parsers/CommandLineParser.kt`, `clikt/src/commonMain/kotlin/com/github/ajalt/clikt/parsers/ParserInternals.kt`, `clikt/src/commonMain/kotlin/com/github/ajalt/clikt/parameters/options/Option.kt`, `test/src/commonTest/kotlin/com/github/ajalt/clikt/parameters/OptionTest.kt`, `test/src/commonTest/kotlin/com/github/ajalt/clikt/parameters/SubcommandTest.kt`, `README.md`, `LICENSE.txt`. GitHub Linguist label: Kotlin.

</details>

### [oshai/kotlin-logging](https://github.com/oshai/kotlin-logging)

**Language 3 / Behavior 2 / Design 3 / Constraints 4 → Level 3**

**Source:** Production software

A lightweight Kotlin multiplatform logging facade with lazy messages and adapters for platform logging systems.

**Why study it:** kotlin-logging shows how a multiplatform facade can keep logging lazy while preserving markers, payloads, causes, and the original call site through an SLF4J adapter.

**Short context:**

- A logging facade checks a level, lazily creates an event, and forwards it to a platform backend while preserving the caller location.

**Prerequisites:**

- Readers should know Kotlin interfaces, inline and lambda-based APIs, multiplatform source sets, and basic logging levels, markers, exceptions, and backend adapters.

**Concepts this path develops:**

- Receiver-lambda event builder.
- Level-enabled branch.
- Disabled messages must remain unevaluated.

**What you can learn:**

- Trace enabled checks and lazy event construction through the common logger contract into a location-aware JVM backend with exact caller metadata.

**Learning path:**

- **Goal:** Understand how a multiplatform Kotlin logging facade keeps messages lazy while preserving markers, payloads, causes, and the original source location through an SLF4J adapter.
- **Start here:** [`src/commonMain/kotlin/io/github/oshai/kotlinlogging/KLogger.kt`](https://github.com/oshai/kotlin-logging/blob/0aaa57ccef9e1cc619de0d30bd65cc0a7271332d/src/commonMain/kotlin/io/github/oshai/kotlinlogging/KLogger.kt) — The reviewed trace begins in KLogger.kt because it defines the level methods and lazy receiver-builder contract that every selected backend call implements.
- **Then read:**
  - [`src/commonMain/kotlin/io/github/oshai/kotlinlogging/KLoggingEventBuilder.kt`](https://github.com/oshai/kotlin-logging/blob/0aaa57ccef9e1cc619de0d30bd65cc0a7271332d/src/commonMain/kotlin/io/github/oshai/kotlinlogging/KLoggingEventBuilder.kt)
  - [`src/commonMain/kotlin/io/github/oshai/kotlinlogging/KotlinLogging.kt`](https://github.com/oshai/kotlin-logging/blob/0aaa57ccef9e1cc619de0d30bd65cc0a7271332d/src/commonMain/kotlin/io/github/oshai/kotlinlogging/KotlinLogging.kt)
  - [`src/javaMain/kotlin/io/github/oshai/kotlinlogging/slf4j/internal/LocationAwareKLogger.kt`](https://github.com/oshai/kotlin-logging/blob/0aaa57ccef9e1cc619de0d30bd65cc0a7271332d/src/javaMain/kotlin/io/github/oshai/kotlinlogging/slf4j/internal/LocationAwareKLogger.kt)
  - [`src/jvmTest/kotlin/io/github/oshai/kotlinlogging/LoggingWithLocationTest.kt`](https://github.com/oshai/kotlin-logging/blob/0aaa57ccef9e1cc619de0d30bd65cc0a7271332d/src/jvmTest/kotlin/io/github/oshai/kotlinlogging/LoggingWithLocationTest.kt)
  - [`README.md`](https://github.com/oshai/kotlin-logging/blob/0aaa57ccef9e1cc619de0d30bd65cc0a7271332d/README.md)
  - [`LICENSE`](https://github.com/oshai/kotlin-logging/blob/0aaa57ccef9e1cc619de0d30bd65cc0a7271332d/LICENSE)
- **Trace:** Start with KLogger level methods and the receiver event builder, follow enabled checks and lazy message, marker, cause, and payload collection into LocationAwareKLogger, then close with exact caller-class, method, and line assertions for ordinary, lazy, fluent, null, and entry/exit calls.

**Why this level:**

- **Language technique 3:** Higher-order facade abstractions materially shape the API without recurring reflection, code generation, or expert type machinery.
- **Behavioral reasoning 2:** Behavior has meaningful local branching but no nontrivial state machine or lifecycle.
- **Design span 3:** Several meaningful common, platform, backend, and verification boundaries cooperate.
- **Constraint burden 4:** Performance, source-location, payload, multiplatform, and backend-compatibility guarantees interact throughout the facade.
- **Placement:** The four scores 3/2/3/4 sum to 12; their arithmetic mean is 3.00 and rounds half-up to Level 3. The published result is Level 3.

**License:** Apache-2.0 ([evidence 1](https://github.com/oshai/kotlin-logging/blob/0aaa57ccef9e1cc619de0d30bd65cc0a7271332d/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The project publishes current Maven artifacts, documents platform setup and runtime backend requirements, and lists production software that uses the facade.

**Language evidence:** The lazy logging facade, event builder, logger factories, SLF4J and JUL adapters, source-location preservation, and native, Android, JS, Wasm, and Darwin backends are Kotlin.

**Coding relevance:**

Logging vocabulary is short and subordinate to transferable lessons in lazy APIs, receiver builders, common-to-platform adapters, compatibility facades, payload forwarding, and observability contracts.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** KLogger.kt, KLoggingEventBuilder.kt, KotlinLogging.kt, and LocationAwareKLogger.kt give the common contract, event state, entry point, and JVM adapter distinct roles.
- **Architecture:** Common logger methods collect a lazy event and forward it through a platform implementation that preserves the fully qualified caller boundary.
- **Naming and idiom:** KLogger, KLoggingEventBuilder, KotlinLogging, and LocationAwareKLogger make the facade and adapter layers explicit while using Kotlin receiver builders and lazy lambdas idiomatically.
- **Tests:** LoggingWithLocationTest.kt verifies class, method, and line attribution for ordinary, lazy, fluent, null-message, and entry or exit calls.
- **Documentation:** README.md documents lazy evaluation, supported backends, and the facade's intended usage.
- **Traceability:** A level call in KLogger.kt can be followed through event construction into LocationAwareKLogger.kt and closed by exact source-location assertions.
- **Maintainability:** The common contract and backend adapter are separated, and one focused test suite protects the subtle caller-location guarantee.
- **Educational value:** The path teaches that an ergonomic wrapper must preserve observability semantics, not merely forward message text.

**Inspection record:** commit `0aaa57ccef9e1cc619de0d30bd65cc0a7271332d`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/commonMain/kotlin/io/github/oshai/kotlinlogging/KLogger.kt`, `src/commonMain/kotlin/io/github/oshai/kotlinlogging/KLoggingEventBuilder.kt`, `src/commonMain/kotlin/io/github/oshai/kotlinlogging/KotlinLogging.kt`, `src/javaMain/kotlin/io/github/oshai/kotlinlogging/slf4j/internal/LocationAwareKLogger.kt`, `src/jvmTest/kotlin/io/github/oshai/kotlinlogging/LoggingWithLocationTest.kt`, `README.md`, `LICENSE`. GitHub Linguist label: Kotlin.

</details>

## Level 4 — Advanced

### [cashapp/turbine](https://github.com/cashapp/turbine)

**Language 3 / Behavior 4 / Design 3 / Constraints 4 → Level 4**

**Source:** Production software

A small multiplatform testing library that turns Kotlin Flow emissions, completion, and failures into explicit ordered assertions.

**Why study it:** Turbine makes concurrent Flow testing concrete by turning collection into an ordered event protocol with timeouts, cancellation, cleanup, and preserved failures.

**Short context:**

- A Flow test observes emitted items, normal completion, and errors through a channel-backed assertion API.

**Prerequisites:**

- Readers should know Kotlin coroutines, Flow, channels, structured cancellation, exceptions, and ordinary asynchronous unit tests.

**Concepts this path develops:**

- Generic suspend extension functions and receiver contexts.
- Concurrent Flow collection and channel delivery.
- Collection must start promptly without losing hot-flow events.

**What you can learn:**

- Follow Flow collection into channel-backed item, completion, and error events, then reason about timeout selection, cancellation, joining, and unconsumed-event reporting.

**Learning path:**

- **Goal:** Understand how Turbine turns concurrent Flow collection into an ordered, timeout-bounded assertion lifecycle with explicit cleanup and terminal events.
- **Start here:** [`src/commonMain/kotlin/app/cash/turbine/flow.kt`](https://github.com/cashapp/turbine/blob/408104d0874678455ff997913bd3f698039f5c25/src/commonMain/kotlin/app/cash/turbine/flow.kt) — The reviewed trace begins in flow.kt because Flow.test and testIn establish collection ownership and hand events to the assertion lifecycle.
- **Then read:**
  - [`src/commonMain/kotlin/app/cash/turbine/Turbine.kt`](https://github.com/cashapp/turbine/blob/408104d0874678455ff997913bd3f698039f5c25/src/commonMain/kotlin/app/cash/turbine/Turbine.kt)
  - [`src/commonMain/kotlin/app/cash/turbine/ReceiveTurbine.kt`](https://github.com/cashapp/turbine/blob/408104d0874678455ff997913bd3f698039f5c25/src/commonMain/kotlin/app/cash/turbine/ReceiveTurbine.kt)
  - [`src/commonMain/kotlin/app/cash/turbine/channel.kt`](https://github.com/cashapp/turbine/blob/408104d0874678455ff997913bd3f698039f5c25/src/commonMain/kotlin/app/cash/turbine/channel.kt)
  - [`src/commonMain/kotlin/app/cash/turbine/Event.kt`](https://github.com/cashapp/turbine/blob/408104d0874678455ff997913bd3f698039f5c25/src/commonMain/kotlin/app/cash/turbine/Event.kt)
  - [`src/commonMain/kotlin/app/cash/turbine/coroutines.kt`](https://github.com/cashapp/turbine/blob/408104d0874678455ff997913bd3f698039f5c25/src/commonMain/kotlin/app/cash/turbine/coroutines.kt)
  - [`src/commonTest/kotlin/app/cash/turbine/FlowTest.kt`](https://github.com/cashapp/turbine/blob/408104d0874678455ff997913bd3f698039f5c25/src/commonTest/kotlin/app/cash/turbine/FlowTest.kt)
  - [`src/commonTest/kotlin/app/cash/turbine/ChannelTest.kt`](https://github.com/cashapp/turbine/blob/408104d0874678455ff997913bd3f698039f5c25/src/commonTest/kotlin/app/cash/turbine/ChannelTest.kt)
  - [`README.md`](https://github.com/cashapp/turbine/blob/408104d0874678455ff997913bd3f698039f5c25/README.md)
  - [`LICENSE.txt`](https://github.com/cashapp/turbine/blob/408104d0874678455ff997913bd3f698039f5c25/LICENSE.txt)
- **Trace:** Start with Flow.test and testIn, follow undispatched collection into ChannelTurbine and item, completion, or error events, then trace timeout selection, cancellation and join, remaining-event reporting, and exception preservation into the direct Flow and Channel assertions.

**Why this level:**

- **Language technique 3:** Substantial coroutine and higher-order abstractions shape the path without manual continuations or multiple expert language mechanisms.
- **Behavioral reasoning 4:** Concurrency, cancellation, event propagation, and cleanup invariants recur and require advanced nonlocal reasoning.
- **Design span 3:** Several meaningful collection, assertion, lifecycle, and verification boundaries cooperate.
- **Constraint burden 4:** Concurrency, cleanup, timing, diagnostic, and test-determinism guarantees interact throughout the path.
- **Placement:** The four scores 3/4/3/4 sum to 14; their arithmetic mean is 3.50 and rounds half-up to Level 4. The published result is Level 4.

**License:** Apache-2.0 ([evidence 1](https://github.com/cashapp/turbine/blob/408104d0874678455ff997913bd3f698039f5c25/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** Cash App publishes the versioned Turbine testing artifact and documents stable Flow-testing APIs used from ordinary coroutine test suites.

**Language evidence:** Flow collection, channel wrapping, event modeling, timeouts, cancellation, assertion reporting, and the public test DSL are implemented in common Kotlin.

**Coding relevance:**

Coroutine and Flow vocabulary is programming subject matter; the path directly teaches concurrent collection, structured cancellation, terminal events, timeouts, cleanup, exception causality, and race-sensitive testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** flow.kt, Turbine.kt, ReceiveTurbine.kt, channel.kt, Event.kt, and coroutines.kt separate adaptation, event transport, assertions, and coroutine helpers.
- **Architecture:** An undispatched collector converts a Flow into channel events, ChannelTurbine exposes assertions, and cleanup cancels and joins the collection job.
- **Naming and idiom:** Flow.test, testIn, ChannelTurbine, ReceiveTurbine, and Event state the lifecycle directly and use structured coroutine APIs idiomatically.
- **Tests:** FlowTest.kt and ChannelTest.kt exercise item ordering, completion, errors, cancellation, timeouts, names, and leftover-event failures.
- **Documentation:** README.md explains the assertion lifecycle, cleanup obligation, and interaction with virtual time.
- **Traceability:** A Flow passed to test can be traced through collection and Event creation to receive assertions and the direct Flow and channel tests.
- **Maintainability:** Narrow interfaces isolate event transport from public assertions, while direct lifecycle tests constrain cancellation and timeout regressions.
- **Educational value:** The path is a bounded lesson in testing concurrent streams without losing ownership, terminal-state, or cleanup guarantees.

**Inspection record:** commit `408104d0874678455ff997913bd3f698039f5c25`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/commonMain/kotlin/app/cash/turbine/flow.kt`, `src/commonMain/kotlin/app/cash/turbine/Turbine.kt`, `src/commonMain/kotlin/app/cash/turbine/ReceiveTurbine.kt`, `src/commonMain/kotlin/app/cash/turbine/channel.kt`, `src/commonMain/kotlin/app/cash/turbine/Event.kt`, `src/commonMain/kotlin/app/cash/turbine/coroutines.kt`, `src/commonTest/kotlin/app/cash/turbine/FlowTest.kt`, `src/commonTest/kotlin/app/cash/turbine/ChannelTest.kt`, `README.md`, `LICENSE.txt`. GitHub Linguist label: Kotlin.

</details>

### [square/moshi](https://github.com/square/moshi)

**Language 4 / Behavior 4 / Design 3 / Constraints 4 → Level 4**

**Source:** Production software

A modern JSON library for Kotlin and Java with streaming I/O, composable adapters, reflection support, and generated adapters through Kotlin Symbol Processing.

**Why study it:** Moshi's adapter lookup is a focused study of recursive factory resolution, cycle breaking, deferred publication, and safe cache updates.

**Short context:**

- Moshi maps JSON values to and from Kotlin and Java object models through composable adapters.

**Prerequisites:**

- Readers should know Kotlin and Java generics, factories, reflection at a high level, thread-local state, maps, and the role of adapters in JSON serialization.

**Concepts this path develops:**

- Reified and KType-based adapter APIs.
- Ordered factory search and next-adapter continuation.
- Recursive types and circular adapter graphs.

**What you can learn:**

- Follow a generic adapter request through factory precedence, a thread-local lookup chain, deferred recursive adapters, and synchronized cache publication.

**Learning path:**

- **Goal:** Understand how Moshi resolves, constructs, temporarily defers, and safely caches recursive adapters without exposing incomplete adapters to callers.
- **Start here:** [`moshi/src/main/java/com/squareup/moshi/Moshi.kt`](https://github.com/square/moshi/blob/889013ec2edb8d8034902662a1dc8c4f3b3f8111/moshi/src/main/java/com/squareup/moshi/Moshi.kt) — The reviewed trace begins in Moshi.kt because Moshi.adapter owns the factory walk, recursive LookupChain, deferred adapter, and cache-publication behavior.
- **Then read:**
  - [`moshi-kotlin/src/main/java/com/squareup/moshi/kotlin/reflect/KotlinJsonAdapterFactory.kt`](https://github.com/square/moshi/blob/889013ec2edb8d8034902662a1dc8c4f3b3f8111/moshi-kotlin/src/main/java/com/squareup/moshi/kotlin/reflect/KotlinJsonAdapterFactory.kt)
  - [`moshi/src/test/java/com/squareup/moshi/CircularAdaptersTest.java`](https://github.com/square/moshi/blob/889013ec2edb8d8034902662a1dc8c4f3b3f8111/moshi/src/test/java/com/squareup/moshi/CircularAdaptersTest.java)
  - [`moshi/src/test/java/com/squareup/moshi/DeferredAdapterTest.java`](https://github.com/square/moshi/blob/889013ec2edb8d8034902662a1dc8c4f3b3f8111/moshi/src/test/java/com/squareup/moshi/DeferredAdapterTest.java)
  - [`moshi/src/test/java/com/squareup/moshi/MoshiTest.java`](https://github.com/square/moshi/blob/889013ec2edb8d8034902662a1dc8c4f3b3f8111/moshi/src/test/java/com/squareup/moshi/MoshiTest.java)
  - [`README.md`](https://github.com/square/moshi/blob/889013ec2edb8d8034902662a1dc8c4f3b3f8111/README.md)
  - [`LICENSE.txt`](https://github.com/square/moshi/blob/889013ec2edb8d8034902662a1dc8c4f3b3f8111/LICENSE.txt)
- **Trace:** Start at Moshi.adapter and its factory walk, follow the thread-local LookupChain as recursive requests receive deferred adapters and successful outermost lookup publishes a synchronized cache snapshot, inspect the Kotlin reflection factory as a concrete recursive boundary, then close the trace with the direct circular and deferred tests plus only MoshiTest's lookup-stack and factory-precedence cases.

**Why this level:**

- **Language technique 4:** Advanced generic and reflective techniques recur across lookup and concrete adapter construction, but the trace does not require pervasive compiler-level type machinery.
- **Behavioral reasoning 4:** Correctness depends on a nonlocal recursive construction lifecycle, reentrancy, cleanup, and publication across nested lookups, matching the advanced behavior anchor.
- **Design span 3:** Several meaningful implementation and verification boundaries cooperate, while the representative path remains one cohesive adapter-resolution subsystem.
- **Constraint burden 4:** Multiple interacting compatibility, concurrency, extension, recursion, and diagnostic guarantees constrain the lookup design.
- **Placement:** The four scores 4/4/3/4 sum to 15; their arithmetic mean is 3.75 and rounds half-up to Level 4. The published result is Level 4.

**License:** Apache-2.0 ([evidence 1](https://github.com/square/moshi/blob/889013ec2edb8d8034902662a1dc8c4f3b3f8111/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** Square publishes Moshi runtime, Kotlin, adapter, and code-generation artifacts and documents stable use in Kotlin and Java applications.

**Language evidence:** The adapter registry, streaming UTF-8 reader and writer, Kotlin reflection integration, standard adapters, and KSP code generator are primarily Kotlin, with intentional Java interoperability and tests.

**Coding relevance:**

The short serialization vocabulary is subordinate to transferable programming lessons in generic factory lookup, recursive construction, cycle breaking, cache publication, reentrancy, reflection boundaries, and focused contract tests.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Moshi.kt keeps adapter lookup and caching readable, while KotlinJsonAdapterFactory.kt isolates the reflection boundary used as a concrete recursive case.
- **Architecture:** A public lookup walks factories, a thread-local chain breaks recursive construction cycles, and the outermost successful lookup publishes a synchronized cache snapshot.
- **Naming and idiom:** Moshi.adapter, LookupChain, DeferredAdapter, and KotlinJsonAdapterFactory expose their responsibilities and use typed factories and localized synchronization clearly.
- **Tests:** CircularAdaptersTest.java and DeferredAdapterTest.java directly close recursion and publication behavior; focused MoshiTest.java cases cover lookup stacks and factory precedence.
- **Documentation:** README.md explains adapters and factories sufficiently to enter the selected implementation path.
- **Traceability:** An adapter request can be followed from Moshi.adapter through the factory chain and deferred placeholder to cache publication and the circular-adapter tests.
- **Maintainability:** Cycle handling is concentrated in the lookup chain, reflection stays behind a factory, and focused tests protect precedence and publication invariants.
- **Educational value:** The path turns a difficult recursive-cache problem into a bounded example with observable failure and success cases.

**Inspection record:** commit `889013ec2edb8d8034902662a1dc8c4f3b3f8111`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `moshi/src/main/java/com/squareup/moshi/Moshi.kt`, `moshi-kotlin/src/main/java/com/squareup/moshi/kotlin/reflect/KotlinJsonAdapterFactory.kt`, `moshi/src/test/java/com/squareup/moshi/CircularAdaptersTest.java`, `moshi/src/test/java/com/squareup/moshi/DeferredAdapterTest.java`, `moshi/src/test/java/com/squareup/moshi/MoshiTest.java`, `README.md`, `LICENSE.txt`. GitHub Linguist label: Kotlin.

</details>

## Level 5 — Expert

### [JetBrains/kotlin](https://github.com/JetBrains/kotlin)

**Language 5 / Behavior 5 / Design 5 / Constraints 5 → Level 5**

**Source:** Production software

The Kotlin programming language implementation, including its compiler frontends, intermediate representations, backends, tooling, libraries, and multiplatform infrastructure.

**Why study it:** Kotlin's JVM command-line compiler exposes an expert but unusually explicit staged path from configuration and frontend analysis through FIR, IR, backend code generation, and artifact output.

**Short context:**

- The selected JVM command-line compiler pipeline transforms Kotlin source through frontend analysis, FIR-to-IR conversion, backend code generation, and output writing.

**Prerequisites:**

- Readers should know advanced Kotlin, compiler frontends and intermediate representations, JVM bytecode at a high level, staged pipelines, diagnostics, and build artifacts.

**Concepts this path develops:**

- Strongly typed generic pipeline phases and artifacts.
- Multi-stage configuration and diagnostic lifecycle.
- Language semantic and diagnostic compatibility.

**What you can learn:**

- Follow source compilation through ordered pipeline phases, typed intermediate representations, backend generation, diagnostics, and safe JAR output.

**Learning path:**

- **Goal:** Understand how the Kotlin JVM command-line compiler coordinates configuration, frontend analysis, FIR-to-IR conversion, JVM backend generation, and safe artifact output as an explicit staged pipeline.
- **Start here:** [`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmCliPipeline.kt`](https://github.com/JetBrains/kotlin/blob/893937b03bee8acd82c4c6201732d9e29cb3d932/compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmCliPipeline.kt) — The reviewed trace begins in JvmCliPipeline.kt because it names and composes the exact frontend, FIR-to-IR, backend, and output phases selected for study.
- **Then read:**
  - [`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/K2JVMCompiler.kt`](https://github.com/JetBrains/kotlin/blob/893937b03bee8acd82c4c6201732d9e29cb3d932/compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/K2JVMCompiler.kt)
  - [`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmFrontendPipelinePhase.kt`](https://github.com/JetBrains/kotlin/blob/893937b03bee8acd82c4c6201732d9e29cb3d932/compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmFrontendPipelinePhase.kt)
  - [`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmFir2IrPipelinePhase.kt`](https://github.com/JetBrains/kotlin/blob/893937b03bee8acd82c4c6201732d9e29cb3d932/compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmFir2IrPipelinePhase.kt)
  - [`compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/pipeline/convertToIr.kt`](https://github.com/JetBrains/kotlin/blob/893937b03bee8acd82c4c6201732d9e29cb3d932/compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/pipeline/convertToIr.kt)
  - [`compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrConverter.kt`](https://github.com/JetBrains/kotlin/blob/893937b03bee8acd82c4c6201732d9e29cb3d932/compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrConverter.kt)
  - [`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmBackendPipelinePhase.kt`](https://github.com/JetBrains/kotlin/blob/893937b03bee8acd82c4c6201732d9e29cb3d932/compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmBackendPipelinePhase.kt)
  - [`compiler/ir/backend.jvm/entrypoint/src/org/jetbrains/kotlin/backend/jvm/JvmIrCodegenFactory.kt`](https://github.com/JetBrains/kotlin/blob/893937b03bee8acd82c4c6201732d9e29cb3d932/compiler/ir/backend.jvm/entrypoint/src/org/jetbrains/kotlin/backend/jvm/JvmIrCodegenFactory.kt)
  - [`compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmWriteOutputsPhase.kt`](https://github.com/JetBrains/kotlin/blob/893937b03bee8acd82c4c6201732d9e29cb3d932/compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmWriteOutputsPhase.kt)
  - [`compiler/tests-integration/tests/org/jetbrains/kotlin/cli/JarOutputTest.kt`](https://github.com/JetBrains/kotlin/blob/893937b03bee8acd82c4c6201732d9e29cb3d932/compiler/tests-integration/tests/org/jetbrains/kotlin/cli/JarOutputTest.kt)
  - [`ReadMe.md`](https://github.com/JetBrains/kotlin/blob/893937b03bee8acd82c4c6201732d9e29cb3d932/ReadMe.md)
  - [`license/README.md`](https://github.com/JetBrains/kotlin/blob/893937b03bee8acd82c4c6201732d9e29cb3d932/license/README.md)
  - [`license/LICENSE.txt`](https://github.com/JetBrains/kotlin/blob/893937b03bee8acd82c4c6201732d9e29cb3d932/license/LICENSE.txt)
- **Trace:** Start with JvmCliPipeline's ordered phase composition and K2JVMCompiler entry, follow frontend session and analysis output into JvmFir2IrPipelinePhase, convertToIr and Fir2IrConverter, continue through JvmBackendPipelinePhase and JvmIrCodegenFactory, then finish at JvmWriteOutputsPhase and JarOutputTest's artifact contracts; unrelated IDE, Native, JavaScript, build, and plugin subsystems are excluded.

**Why this level:**

- **Language technique 5:** Expert type, compiler, generic pipeline, representation, and code-generation techniques are pervasive across every stage.
- **Behavioral reasoning 5:** Correctness requires expert nonlocal reasoning across staged transformations, shared compiler state, diagnostics, failure policies, generated artifacts, and output finalization.
- **Design span 5:** The coherent source-to-jar trace necessarily spans many architecturally distinct compiler subsystems and integration boundaries.
- **Constraint burden 5:** Expert semantic, representation, extension, artifact, performance, and backward-compatibility guarantees interact pervasively across the pipeline.
- **Placement:** The four scores 5/5/5/5 sum to 20; their arithmetic mean is 5.00 and rounds half-up to Level 5. The published result is Level 5.

**License:** Apache-2.0 AND LicenseRef-Third-Party-Notices ([evidence 1](https://github.com/JetBrains/kotlin/blob/893937b03bee8acd82c4c6201732d9e29cb3d932/license/README.md), [evidence 2](https://github.com/JetBrains/kotlin/blob/893937b03bee8acd82c4c6201732d9e29cb3d932/license/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** This official JetBrains repository builds the Kotlin compiler and language toolchain distributed for JVM, JavaScript, Wasm, Native, IDE, Gradle, Maven, and command-line workflows.

**Language evidence:** The compiler frontends, FIR semantic model, FIR-to-IR conversion, intermediate representations, lowering pipelines, JVM backend, command-line compiler, daemon, incremental compilation, and much supporting infrastructure are implemented primarily in Kotlin.

**Coding relevance:**

Compiler construction is programming infrastructure rather than an external specialist domain, and the trace teaches transferable staged architecture, typed intermediate representations, diagnostics, extension coordination, code generation, lifecycle, and output-integrity reasoning.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** JvmCliPipeline.kt and its phase classes expose ordered boundaries, while convertToIr.kt, Fir2IrConverter.kt, and JvmIrCodegenFactory.kt make the central transformations inspectable.
- **Architecture:** K2JVMCompiler enters a typed pipeline whose frontend result feeds FIR-to-IR conversion, JVM backend generation, and a dedicated output phase.
- **Naming and idiom:** JvmFrontendPipelinePhase, JvmFir2IrPipelinePhase, JvmBackendPipelinePhase, and JvmWriteOutputsPhase make the compiler architecture literal and use typed phase composition consistently.
- **Tests:** JarOutputTest.kt closes the selected pipeline at the artifact boundary by exercising the compiler's JAR-output contracts.
- **Documentation:** ReadMe.md orients the repository, while the explicitly named pipeline and phase types provide a stage-by-stage implementation map from frontend analysis through JAR output.
- **Traceability:** A JVM CLI invocation can be followed from K2JVMCompiler through every named pipeline phase to JvmWriteOutputsPhase and the JAR integration test.
- **Maintainability:** Explicit phase inputs and outputs localize the selected compiler flow, and the bounded trace excludes IDE, Native, JavaScript, build, and plugin subsystems.
- **Educational value:** The path lets an advanced learner study a production compiler as a sequence of concrete transformations rather than an undifferentiated monorepo.

**Inspection record:** commit `893937b03bee8acd82c4c6201732d9e29cb3d932`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmCliPipeline.kt`, `compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/jvm/K2JVMCompiler.kt`, `compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmFrontendPipelinePhase.kt`, `compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmFir2IrPipelinePhase.kt`, `compiler/fir/entrypoint/src/org/jetbrains/kotlin/fir/pipeline/convertToIr.kt`, `compiler/fir/fir2ir/src/org/jetbrains/kotlin/fir/backend/Fir2IrConverter.kt`, `compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmBackendPipelinePhase.kt`, `compiler/ir/backend.jvm/entrypoint/src/org/jetbrains/kotlin/backend/jvm/JvmIrCodegenFactory.kt`, `compiler/cli/cli-jvm/src/org/jetbrains/kotlin/cli/pipeline/jvm/JvmWriteOutputsPhase.kt`, `compiler/tests-integration/tests/org/jetbrains/kotlin/cli/JarOutputTest.kt`, `ReadMe.md`, `license/README.md`, `license/LICENSE.txt`. GitHub Linguist label: Kotlin.

</details>

### [Kotlin/kotlinx.coroutines](https://github.com/Kotlin/kotlinx.coroutines)

**Language 5 / Behavior 5 / Design 3 / Constraints 5 → Level 5**

**Source:** Production software

Kotlin's official multiplatform library for structured concurrency, asynchronous streams, channels, scheduling, testing, debugging, and ecosystem integration.

**Why study it:** The kotlinx.coroutines Job implementation is a concentrated example of a thread-safe lifecycle state machine with cancellation, child ownership, callbacks, and exception aggregation.

**Short context:**

- The selected Job path coordinates structured coroutine lifetimes, cancellation, completion, and parent-child relationships.

**Prerequisites:**

- Readers should know advanced Kotlin, coroutines and structured concurrency, atomic compare-and-set loops, linked state structures, cancellation, and exception propagation.

**Concepts this path develops:**

- Atomicfu-backed compare-and-set loops.
- Multi-phase incomplete, finishing, completed, and cancelled states.
- Lock-free thread safety and linearizable state publication.

**What you can learn:**

- Trace Job activation, cancellation, make-completing transitions, child waiting, finalization, handler notification, and exception aggregation through atomic state changes.

**Learning path:**

- **Goal:** Understand how kotlinx.coroutines implements a thread-safe Job lifecycle across activation, completion, cancellation, child waiting, handler invocation, and exception aggregation.
- **Start here:** [`kotlinx-coroutines-core/common/src/JobSupport.kt`](https://github.com/Kotlin/kotlinx.coroutines/blob/f63a04bacb8beeafcc9d49199b1e4bb08931b7eb/kotlinx-coroutines-core/common/src/JobSupport.kt) — The reviewed trace begins in JobSupport.kt because it contains the state representation and transition loops that implement the public Job contract.
- **Then read:**
  - [`kotlinx-coroutines-core/common/src/Job.kt`](https://github.com/Kotlin/kotlinx.coroutines/blob/f63a04bacb8beeafcc9d49199b1e4bb08931b7eb/kotlinx-coroutines-core/common/src/Job.kt)
  - [`kotlinx-coroutines-core/common/test/JobStatesTest.kt`](https://github.com/Kotlin/kotlinx.coroutines/blob/f63a04bacb8beeafcc9d49199b1e4bb08931b7eb/kotlinx-coroutines-core/common/test/JobStatesTest.kt)
  - [`kotlinx-coroutines-core/common/test/JobTest.kt`](https://github.com/Kotlin/kotlinx.coroutines/blob/f63a04bacb8beeafcc9d49199b1e4bb08931b7eb/kotlinx-coroutines-core/common/test/JobTest.kt)
  - [`kotlinx-coroutines-core/common/test/ParentCancellationTest.kt`](https://github.com/Kotlin/kotlinx.coroutines/blob/f63a04bacb8beeafcc9d49199b1e4bb08931b7eb/kotlinx-coroutines-core/common/test/ParentCancellationTest.kt)
  - [`kotlinx-coroutines-core/common/test/CompletableJobTest.kt`](https://github.com/Kotlin/kotlinx.coroutines/blob/f63a04bacb8beeafcc9d49199b1e4bb08931b7eb/kotlinx-coroutines-core/common/test/CompletableJobTest.kt)
  - [`README.md`](https://github.com/Kotlin/kotlinx.coroutines/blob/f63a04bacb8beeafcc9d49199b1e4bb08931b7eb/README.md)
  - [`LICENSE.txt`](https://github.com/Kotlin/kotlinx.coroutines/blob/f63a04bacb8beeafcc9d49199b1e4bb08931b7eb/LICENSE.txt)
- **Trace:** Start with JobSupport's state representation and atomic transition loops, follow start, cancel, make-completing, child-wait, finalization, exception aggregation, and handler notification against the public Job lifecycle contract, then close each transition and parent-child edge with the focused state, cancellation, completion, and completable-job tests; unrelated scheduler, continuation, channel, and SharedFlow machinery is excluded.

**Why this level:**

- **Language technique 5:** Low-level atomic, lock-free, type-state, and performance techniques are pervasive across the selected lifecycle implementation.
- **Behavioral reasoning 5:** Correctness depends on expert nonlocal reasoning across concurrent state transitions, nested ownership, callbacks, and exceptional completion.
- **Design span 3:** Several meaningful contract, implementation, collaboration, and test boundaries cooperate, but the representative path deliberately remains one subsystem.
- **Constraint burden 5:** Expert concurrency, lifecycle, exception, compatibility, and performance guarantees interact pervasively throughout the path.
- **Placement:** The four scores 5/5/3/5 sum to 18; their arithmetic mean is 4.50 and rounds half-up to Level 5. The published result is Level 5.

**License:** Apache-2.0 ([evidence 1](https://github.com/Kotlin/kotlinx.coroutines/blob/f63a04bacb8beeafcc9d49199b1e4bb08931b7eb/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** JetBrains publishes stable core, test, debug, reactive, UI, and integration artifacts as the standard library companion for Kotlin coroutine applications.

**Language evidence:** Coroutine jobs, continuations, dispatchers, work-stealing scheduler, channels, flows, synchronization primitives, test scheduler, debug probes, reactive adapters, and platform integrations are Kotlin.

**Coding relevance:**

Coroutine vocabulary is programming-language and concurrency infrastructure, and the trace teaches transferable state-machine, lock-free transition, lifecycle, callback, ownership, exception, and concurrency reasoning without relying on an external specialist domain.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** JobSupport.kt names its states and transition phases explicitly, and Job.kt provides the public lifecycle contract against which the implementation can be read.
- **Architecture:** The public Job abstraction delegates lifecycle management to one atomic state machine that coordinates children, handlers, completion, cancellation, and failures.
- **Naming and idiom:** JobSupport, makeCompleting, finalization, child waiting, and handler nodes expose lifecycle intent while demonstrating advanced lock-free Kotlin patterns.
- **Tests:** JobStatesTest.kt, JobTest.kt, ParentCancellationTest.kt, and CompletableJobTest.kt exercise state transitions, parent-child cancellation, completion, and explicit completable jobs.
- **Documentation:** Job.kt documents the lifecycle contract, and README.md provides project and coroutine orientation for the bounded trace.
- **Traceability:** Each public lifecycle action in Job.kt can be followed into JobSupport.kt's atomic transitions and then matched to a focused state or cancellation test.
- **Maintainability:** The selected path excludes unrelated schedulers, channels, and flow machinery, leaving explicit invariants and direct regression suites around one lifecycle engine.
- **Educational value:** The path provides a rare, complete view of how structured-concurrency promises are enforced under races rather than merely described by an API.

**Inspection record:** commit `f63a04bacb8beeafcc9d49199b1e4bb08931b7eb`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `kotlinx-coroutines-core/common/src/JobSupport.kt`, `kotlinx-coroutines-core/common/src/Job.kt`, `kotlinx-coroutines-core/common/test/JobStatesTest.kt`, `kotlinx-coroutines-core/common/test/JobTest.kt`, `kotlinx-coroutines-core/common/test/ParentCancellationTest.kt`, `kotlinx-coroutines-core/common/test/CompletableJobTest.kt`, `README.md`, `LICENSE.txt`. GitHub Linguist label: Kotlin.

</details>

_Generated from `catalog/kotlin.json`; do not edit by hand._

# C++

7 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

[← All languages](../README.md)

## Level 1 — First real code

No qualified learning path has been published at this level. An empty Level 1 means Exempla has not yet found a path gentle enough to publish here; learners are not being told to jump to Level 2.

## Level 2 — Guided real-world code

### [microsoft/GSL](https://github.com/microsoft/GSL)

**Language 3 / Behavior 2 / Design 1 / Constraints 3 → Level 2**

A small C++ scope guard that runs a cleanup function when control leaves a block.

**Why study it:** Learn how one object owns a cleanup action, runs it during ordinary destruction, and transfers that responsibility safely when moved.

**Short context:**

- A scope guard owns a cleanup callback and invokes it when the guard leaves scope unless responsibility has been transferred to another guard.

**Prerequisites:**

- The global novice C++ baseline, including classes, templates, object lifetime, move construction, and focused tests.
- RAII means an object's destructor performs cleanup; moving this guard transfers which object will perform it.

**Concepts this path develops:**

- Owning cleanup with an object's lifetime.
- Making a moved-from guard inactive.
- Testing that ordinary scope exit runs the cleanup once.

**What you can learn:**

- Follow construction, move construction, and destruction through one small utility.
- See how moving transfers cleanup responsibility.
- Use lifecycle tests to distinguish active and inactive guards.

**Learning path:**

- **Goal:** Understand how final_action stores a cleanup callable, invokes it once at scope exit, and transfers that responsibility safely through move construction.
- **Start here:** [`include/gsl/util`](https://github.com/microsoft/GSL/blob/417ef685eafd626db765f0027b7fc5a0057e0770/include/gsl/util) — include/gsl/util contains the complete final_action class, its armed state, move-only ownership transfer, destructor, and finally factory.
- **Then read:**
  - [`tests/utils_tests.cpp`](https://github.com/microsoft/GSL/blob/417ef685eafd626db765f0027b7fc5a0057e0770/tests/utils_tests.cpp)
  - [`docs/headers.md`](https://github.com/microsoft/GSL/blob/417ef685eafd626db765f0027b7fc5a0057e0770/docs/headers.md)
- **Trace:** Start at finally's decay and forwarding into final_action, follow callable storage and the invoke flag through construction, move construction with std::exchange, and noexcept destruction, then close the path with the lambda, moved-guard, lvalue, and function-pointer tests and the public header contract.

**Why this level:**

- **Language technique 3:** Templates, forwarding, type transformation, and move-only RAII materially shape the tiny public utility, but remain localized and conventional.
- **Behavioral reasoning 2:** One small lifecycle and ownership transfer determine whether cleanup runs, with no asynchronous or distributed state.
- **Design span 1:** The complete behavior is one focused header component with direct tests and documentation.
- **Constraint burden 3:** Several ownership, exception-safety, and portability guarantees constrain an otherwise small implementation.
- **Novice accessibility floor 2:** One cohesive professional idea—an object owns cleanup until destruction or a move—can be taught in a short primer and then traced locally through direct tests.
  - **Central concepts:** scope-based cleanup (RAII); ownership transfer when a guard is moved; generic cleanup callables
  - **Incidental concepts:** std::exchange; noexcept spelling
- **Placement:** The four structural scores 3/2/1/3 produce rubric Level 2 under the documented formula and guardrails. Novice accessibility floor 2 produces published Level 2.

**License:** MIT ([evidence 1](https://github.com/microsoft/GSL/blob/417ef685eafd626db765f0027b7fc5a0057e0770/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The project ships a versioned, installable CMake package whose public headers implement the C++ Core Guidelines Support Library interfaces.

**Language evidence:** The final_action class, finally factory, move-only ownership transfer, and direct contract tests are implemented in C++ in include/gsl/util and tests/utils_tests.cpp.

**Coding relevance:**

Scope cleanup is a standard programming concern needing only one local definition; the path teaches transferable RAII, ownership transfer, generic callables, exception-safety policy, API design, and direct lifecycle testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The compact class makes callable ownership, the armed flag, move transfer, and destructor invocation explicit, with comments explaining its purpose and unavoidable padding.
- **Architecture:** final_action owns one callable and invocation flag, while finally provides deduction and forwarding; no unrelated subsystem is needed for the selected behavior.
- **Naming and idiom:** final_action, finally, invoke, std::decay_t, std::forward, std::move, and std::exchange directly express generic RAII ownership.
- **Tests:** tests/utils_tests.cpp covers scope-exit timing, one callback after moving, inert moved-from guards, const and mutable lvalue lambdas, lambdas, function pointers, and functions.
- **Documentation:** README.md and docs/headers.md document final_action, finally, move-only behavior, scope-exit invocation, and noexcept signatures.
- **Traceability:** A callback can be followed from finally through decay and construction, into move ownership or the original guard, and finally into one destructor call verified by direct counter assertions.
- **Maintainability:** A single data-bearing class, deleted copy and assignment operations, explicit move disarming, and focused lifecycle tests tightly constrain changes.
- **Educational value:** The path is a compact production example of generic RAII and single-owner cleanup. It has no explicit dismiss operation; moving is the only disarming mechanism, and a throwing callable copy, move, or invocation cannot escape the unconditional noexcept boundary.

**Inspection record:** commit `417ef685eafd626db765f0027b7fc5a0057e0770`, inspected 2026-08-30. Review passes: Codex primary pass; independent Codex verification pass; Codex novice-accessibility audit. Files inspected: `include/gsl/util`, `tests/utils_tests.cpp`, `docs/headers.md`, `README.md`, `LICENSE`. GitHub Linguist label: C++.

</details>

## Level 3 — Intermediate

### [CLIUtils/CLI11](https://github.com/CLIUtils/CLI11)

**Language 3 / Behavior 3 / Design 3 / Constraints 3 → Level 3**

A command-line parser supporting typed options, flags, subcommands, validation, configuration files, aliases, and rich help output.

**Why study it:** The CLI11 App path shows how command-line tokens become typed option and subcommand values while preserving validation, callbacks, fallthrough, remaining arguments, repetition, and structured errors.

**Short context:**

- A command-line parser assigns tokens to options and subcommands, converts values, validates relationships, and invokes callbacks or reports structured errors.

**Prerequisites:**

- Basic familiarity with C++ classes, templates, references, smart pointers, RAII, standard containers, exceptions, and unit tests.

**Concepts this path develops:**

- Generic typed option conversion.
- Token-consumption and parse state.
- Stable option and subcommand API behavior.

**What you can learn:**

- Use `include/CLI/App.hpp` to study the following transferable techniques and behaviors: Generic option conversion, traits for scalar and container inputs, overloads, callback and validator composition, token classification, option matching, arity, nested subcommands, fallthrough, requirements and exclusions, callback order, remaining tokens, repeated parsing, and errors.

**Learning path:**

- **Goal:** Understand how CLI11 maps command-line tokens into typed options and subcommands while preserving validation, callback, fallthrough, remaining-argument, and error contracts.
- **Start here:** [`include/CLI/App.hpp`](https://github.com/CLIUtils/CLI11/blob/c1cfe00d2f3d862aecfe6e69ec810414d5f4c906/include/CLI/App.hpp) — include/CLI/App.hpp defines the application, option, and subcommand model and leads into App_inl.hpp for the selected token-consumption and validation lifecycle.
- **Then read:**
  - [`include/CLI/impl/App_inl.hpp`](https://github.com/CLIUtils/CLI11/blob/c1cfe00d2f3d862aecfe6e69ec810414d5f4c906/include/CLI/impl/App_inl.hpp)
  - [`include/CLI/Option.hpp`](https://github.com/CLIUtils/CLI11/blob/c1cfe00d2f3d862aecfe6e69ec810414d5f4c906/include/CLI/Option.hpp)
  - [`include/CLI/impl/Option_inl.hpp`](https://github.com/CLIUtils/CLI11/blob/c1cfe00d2f3d862aecfe6e69ec810414d5f4c906/include/CLI/impl/Option_inl.hpp)
  - [`include/CLI/TypeTools.hpp`](https://github.com/CLIUtils/CLI11/blob/c1cfe00d2f3d862aecfe6e69ec810414d5f4c906/include/CLI/TypeTools.hpp)
  - [`tests/AppTest.cpp`](https://github.com/CLIUtils/CLI11/blob/c1cfe00d2f3d862aecfe6e69ec810414d5f4c906/tests/AppTest.cpp)
- **Trace:** Start with App's option and subcommand model, follow parse through token classification, option matching, value collection and conversion, subcommand and remaining-token handling, requirement and exclusion validation, callback ordering, and structured errors; connect Option and TypeTools behavior to the focused application tests.

**Why this level:**

- **Language technique 3:** Generics, traits, overloads, and higher-order composition materially shape the declarative parser API.
- **Behavioral reasoning 3:** State transitions, recursion, callbacks, and errors materially affect a parse without requiring advanced concurrency or resource reasoning.
- **Design span 3:** The trace crosses several meaningful library boundaries whose responsibilities remain locally understandable.
- **Constraint burden 3:** Several material API, compatibility, and correctness guarantees influence normal parser changes.
- **Placement:** The four scores 3/3/3/3 sum to 12; their arithmetic mean is 3.00 and rounds half-up to Level 3. The published result is Level 3.

**License:** BSD-3-Clause ([evidence 1](https://github.com/CLIUtils/CLI11/blob/c1cfe00d2f3d862aecfe6e69ec810414d5f4c906/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The repository ships a header-only, precompiled, and module-capable library through major C++ package systems.

**Language evidence:** Argument models, parsers, validators, config formats, help formatters, encoding, and public APIs are C++ under include/CLI.

**Coding relevance:**

Command-line concepts are familiar and documented locally; the selected path teaches transferable parser state, declarative APIs, type conversion, callbacks, validation, modular design, and error handling rather than a specialized command grammar.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** App, Option, implementation headers, and TypeTools separate declarative configuration, token parsing, typed conversion, validation, callbacks, and errors.
- **Architecture:** App owns parser and subcommand state, Option owns occurrence and value policy, TypeTools performs generic conversion, and validators and callbacks extend the lifecycle.
- **Naming and idiom:** App, Option, add_option, add_subcommand, parse, remaining, fallthrough, required, excludes, needs, callback, and ParseError expose command-line policy.
- **Tests:** AppTest.cpp covers parsing order, option values, subcommands, callbacks, requirements, exclusions, fallthrough, remaining arguments, errors, and repeated parsing.
- **Documentation:** CLI11's App, Option, subcommand, configuration, validation, callback, and parsing documentation explains the contracts exercised by this path.
- **Traceability:** A token vector can be followed through App parsing, option or subcommand matching, value collection and TypeTools conversion, validation, callback ordering, remaining handling, and focused tests.
- **Maintainability:** Separated declaration, implementation, conversion, and validation headers plus focused application tests constrain changes to a broad typed command-line API.
- **Educational value:** The path demonstrates how generic C++ abstractions support a fluent parser while leaving token state, conversion, callback, and error decisions inspectable.

**Inspection record:** commit `c1cfe00d2f3d862aecfe6e69ec810414d5f4c906`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `include/CLI/App.hpp`, `include/CLI/impl/App_inl.hpp`, `include/CLI/Option.hpp`, `include/CLI/impl/Option_inl.hpp`, `include/CLI/TypeTools.hpp`, `tests/AppTest.cpp`, `LICENSE`. GitHub Linguist label: C++.

</details>

### [kainjow/Mustache](https://github.com/kainjow/Mustache)

**Language 3 / Behavior 2 / Design 2 / Constraints 3 → Level 3**

A dependency-free, header-only Mustache template engine for STL-compatible narrow and wide string types.

**Why study it:** The single-header Mustache path shows how C++ parses templates and renders variables, sections, lambdas, and partials against a context stack while preserving escaping and specification compatibility.

**Short context:**

- A Mustache template contains variables, escaped or unescaped substitutions, sections that repeat or conditionally render, inverted sections, and partial templates.

**Prerequisites:**

- Basic familiarity with C++ classes, templates, references, smart pointers, RAII, standard containers, exceptions, and unit tests.

**Concepts this path develops:**

- Generic string and stream support.
- Localized token-parser state.
- Mustache delimiter, whitespace, section, and partial compatibility.

**What you can learn:**

- Use `mustache.hpp` to study the following transferable techniques and behaviors: Generic string and stream support, recursive template data, tokenization, delimiter changes, nested sections, stacked context lookup, scalar, list, object and lambda values, partials, HTML escaping, raw output, whitespace, and parse errors.

**Learning path:**

- **Goal:** Understand how a header-only C++ Mustache engine parses a template and renders variables and nested sections against a context stack while preserving escaping and template compatibility.
- **Start here:** [`mustache.hpp`](https://github.com/kainjow/Mustache/blob/3f654942a70c46a775070d7a09ca7acfa3e205b7/mustache.hpp) — mustache.hpp contains the entire public data model, token parser, context lookup, escaping, rendering, partial, lambda, and error behavior in one source.
- **Then read:**
  - [`tests/tests.cpp`](https://github.com/kainjow/Mustache/blob/3f654942a70c46a775070d7a09ca7acfa3e205b7/tests/tests.cpp)
- **Trace:** Follow template construction into token parsing, delimiter and section handling, then follow render through stacked context lookup, scalar, list, object and lambda data cases, escaped or raw output, partials, and errors; correlate each branch with the direct rendering and malformed-template tests.

**Why this level:**

- **Language technique 3:** Templates, recursive data modeling, and callable composition materially shape the path without requiring expert C++ machinery.
- **Behavioral reasoning 2:** Meaningful state and branches remain within a direct synchronous parse-and-render lifecycle.
- **Design span 2:** A few clear responsibilities inside one header and one test suite contain the behavior.
- **Constraint burden 3:** Several material compatibility, portability, and correctness guarantees influence ordinary parser and renderer changes.
- **Placement:** The four scores 3/2/2/3 sum to 10; their arithmetic mean is 2.50 and rounds half-up to Level 3. The published result is Level 3.

**License:** BSL-1.0 ([evidence 1](https://github.com/kainjow/Mustache/blob/3f654942a70c46a775070d7a09ca7acfa3e205b7/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The repository publishes an embeddable C++ library that implements the Mustache template specification for application use.

**Language evidence:** The complete template parser, data model, renderer, escaping, sections, lambdas, and partials are implemented in mustache.hpp.

**Coding relevance:**

The small documented template vocabulary is sufficient context; the path teaches transferable recursive parsing, variant-like data modeling, context lookup, callback rendering, escaping, error reporting, and compatibility testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The header separates template data, tokens, parsing, context lookup, escaping, and rendering into named types and functions despite its single-file distribution.
- **Architecture:** One header contains distinct parser and renderer boundaries plus data, context-stack, partial, lambda, escaping, and error collaborators.
- **Naming and idiom:** mustache, data, context, token, parse, render, section, partial, lambda, escape, error_message, and is_valid preserve template vocabulary.
- **Tests:** tests/tests.cpp covers variables, sections, inverted sections, lists, lambdas, partials, whitespace, delimiter changes, escaping, malformed templates, and specification examples.
- **Documentation:** The README provides runnable examples and explains template construction, data kinds, rendering, lambdas, partials, escaping, errors, and stream use needed for this path.
- **Traceability:** A template can be followed from construction through token parsing and nested section matching into stacked data lookup, rendering or escaping, partial expansion, and direct tests.
- **Maintainability:** Named responsibilities within the header and specification-oriented tests constrain parser and renderer changes without requiring a multi-library build.
- **Educational value:** The path provides a complete production parser-and-renderer study with generic C++ modeling, callbacks, compatibility rules, and security-sensitive escaping.

**Inspection record:** commit `3f654942a70c46a775070d7a09ca7acfa3e205b7`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `mustache.hpp`, `tests/tests.cpp`, `LICENSE`. GitHub Linguist label: C++.

</details>

## Level 4 — Advanced

### [catchorg/Catch2](https://github.com/catchorg/Catch2)

**Language 5 / Behavior 4 / Design 3 / Constraints 4 → Level 4**

A C++ testing framework with expressive assertions, matchers, generators, test discovery, filtering, reporters, and benchmarking.

**Why study it:** The assertion-macro path shows how Catch2 captures one C++ expression, decomposes operands without double evaluation, and reports faithful values through a managed assertion lifecycle.

**Short context:**

- An assertion framework evaluates a user's expression once and reports both the original expression and decomposed operand values when it fails.

**Prerequisites:**

- Working familiarity with C++ classes, templates, references, smart pointers, RAII, standard containers, exceptions, and unit tests, plus experience tracing behavior across several production files.

**Concepts this path develops:**

- Layered variadic preprocessor macros.
- Single expression evaluation with deferred reporting.
- Exactly-once evaluation and preserved operand values.

**What you can learn:**

- Use `src/catch2/catch_test_macros.hpp` to study the following transferable techniques and behaviors: Layered variadic macros, expression templates, operator-overload capture, forwarding and traits, unary and binary expression objects, exactly-once evaluation, operand stringification, negation, exception and fatal branches, assertion handlers, and compiler portability.

**Learning path:**

- **Goal:** Understand how a Catch2 assertion macro captures one C++ expression, decomposes its operands without double evaluation, and reports a faithful result through the assertion handler.
- **Start here:** [`src/catch2/catch_test_macros.hpp`](https://github.com/catchorg/Catch2/blob/317ac1ed4c0bb6e6b91eafc817e05c488feffcb3/src/catch2/catch_test_macros.hpp) — src/catch2/catch_test_macros.hpp defines the public REQUIRE and CHECK families that lead into internal expansion, Decomposer expression capture, and AssertionHandler reporting.
- **Then read:**
  - [`src/catch2/internal/catch_test_macro_impl.hpp`](https://github.com/catchorg/Catch2/blob/317ac1ed4c0bb6e6b91eafc817e05c488feffcb3/src/catch2/internal/catch_test_macro_impl.hpp)
  - [`src/catch2/internal/catch_decomposer.hpp`](https://github.com/catchorg/Catch2/blob/317ac1ed4c0bb6e6b91eafc817e05c488feffcb3/src/catch2/internal/catch_decomposer.hpp)
  - [`tests/SelfTest/IntrospectiveTests/AssertionHandler.tests.cpp`](https://github.com/catchorg/Catch2/blob/317ac1ed4c0bb6e6b91eafc817e05c488feffcb3/tests/SelfTest/IntrospectiveTests/AssertionHandler.tests.cpp)
  - [`tests/SelfTest/UsageTests/Decomposition.tests.cpp`](https://github.com/catchorg/Catch2/blob/317ac1ed4c0bb6e6b91eafc817e05c488feffcb3/tests/SelfTest/UsageTests/Decomposition.tests.cpp)
- **Trace:** Follow a public REQUIRE or CHECK macro through the internal assertion expansion and handler lifetime, then follow Decomposer's overloaded <= into unary or binary expression objects, result evaluation and reconstructed operand output; correlate handler state, exception, single-evaluation, operator, negation, and diagnostic tests.

**Why this level:**

- **Language technique 5:** Multiple advanced macro, template, overload, and value-category mechanisms interact pervasively and require expert C++ command.
- **Behavioral reasoning 4:** Evaluation state, exceptions, control-flow outcomes, and reporting invariants recur across macro and handler boundaries.
- **Design span 3:** The trace crosses several meaningful interfaces while remaining one assertion subsystem.
- **Constraint burden 4:** Multiple strict semantic, compatibility, diagnostic, and portability constraints interact throughout assertion decomposition.
- **Placement:** The four scores 5/4/3/4 sum to 16; their arithmetic mean is 4.00 and rounds half-up to Level 4. The published result is Level 4.

**License:** BSL-1.0 ([evidence 1](https://github.com/catchorg/Catch2/blob/317ac1ed4c0bb6e6b91eafc817e05c488feffcb3/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The repository releases libraries, a test runner, CMake discovery integration, and packages used to test C++ software.

**Language evidence:** Test registration, assertions, matchers, generators, reporters, command handling, execution, and discovery support are C++ under src/catch2.

**Coding relevance:**

Assertion semantics are familiar and locally documented; the path teaches transferable macro API design, expression templates, operator overloading, single-evaluation discipline, exception capture, diagnostic construction, and regression testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Public macros, internal expansion, decomposer expression types, evaluation, reconstructed diagnostics, and handler lifetime are separated despite intricate macro and template machinery.
- **Architecture:** catch_test_macros.hpp owns the public surface, catch_test_macro_impl.hpp expands control flow, catch_decomposer.hpp captures expressions, and AssertionHandler owns reporting state.
- **Naming and idiom:** REQUIRE, CHECK, INTERNAL_CATCH_TEST, AssertionHandler, Decomposer, BinaryExpr, UnaryExpr, ResultDisposition, completed, and handleException expose the assertion model.
- **Tests:** AssertionHandler.tests.cpp and Decomposition.tests.cpp cover evaluated values, unary and binary expressions, exceptions, messages, negation, short forms, operator behavior, and failure reporting.
- **Documentation:** Catch2's assertion, decomposition, exception, and macro documentation explains the public behavior and operator limitations represented by this path.
- **Traceability:** A REQUIRE or CHECK expression can be followed through macro expansion and handler construction into Decomposer's overloaded capture, result reconstruction, exception handling, and exact diagnostic tests.
- **Maintainability:** Layered boundaries, centralized decomposition, RAII handler state, and introspective compiler-sensitive tests constrain changes to a demanding portable macro API.
- **Educational value:** The path provides an expert study of how C++ language machinery can improve diagnostics while preserving evaluation semantics and broad user-type compatibility.

**Inspection record:** commit `317ac1ed4c0bb6e6b91eafc817e05c488feffcb3`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/catch2/catch_test_macros.hpp`, `src/catch2/internal/catch_test_macro_impl.hpp`, `src/catch2/internal/catch_decomposer.hpp`, `tests/SelfTest/IntrospectiveTests/AssertionHandler.tests.cpp`, `tests/SelfTest/UsageTests/Decomposition.tests.cpp`, `LICENSE.txt`. GitHub Linguist label: C++.

</details>

### [gabime/spdlog](https://github.com/gabime/spdlog)

**Language 3 / Behavior 4 / Design 3 / Constraints 4 → Level 4**

A high-performance logging library with synchronous and asynchronous loggers, formatters, registries, and many output sinks.

**Why study it:** The asynchronous logger path shows how spdlog hands messages to a bounded queue and worker threads while preserving overflow, ordering, flush, ownership, exceptions, and shutdown contracts.

**Short context:**

- An asynchronous logger queues prepared log messages for a background worker; its overflow policy either blocks producers or discards an older message when the bounded queue is full.

**Prerequisites:**

- Working familiarity with C++ classes, templates, references, smart pointers, RAII, standard containers, exceptions, and unit tests, plus experience tracing behavior across several production files.

**Concepts this path develops:**

- Generic bounded queue and message types.
- Multi-producer and multi-consumer synchronization.
- Bounded memory and overflow guarantees.

**What you can learn:**

- Use `include/spdlog/async_logger-inl.h` to study the following transferable techniques and behaviors: Generic bounded queues, shared and weak ownership, multi-producer and multi-consumer synchronization, blocking and overrun overflow policies, worker scheduling, backend sink dispatch, flush messages, termination, exceptions, queue capacity, and concurrent tests.

**Learning path:**

- **Goal:** Understand how spdlog hands a log message to a bounded asynchronous queue and delivers it on worker threads while preserving overflow, ordering, flush, ownership, and shutdown contracts.
- **Start here:** [`include/spdlog/async_logger-inl.h`](https://github.com/gabime/spdlog/blob/f5f173a1a57d0e2e0115f2ed71ee7ea316516853/include/spdlog/async_logger-inl.h) — include/spdlog/async_logger-inl.h contains sink_it_ and flush_, where logger calls lock thread-pool lifetime and choose asynchronous post operations.
- **Then read:**
  - [`include/spdlog/async_logger.h`](https://github.com/gabime/spdlog/blob/f5f173a1a57d0e2e0115f2ed71ee7ea316516853/include/spdlog/async_logger.h)
  - [`include/spdlog/details/thread_pool-inl.h`](https://github.com/gabime/spdlog/blob/f5f173a1a57d0e2e0115f2ed71ee7ea316516853/include/spdlog/details/thread_pool-inl.h)
  - [`include/spdlog/details/mpmc_blocking_q.h`](https://github.com/gabime/spdlog/blob/f5f173a1a57d0e2e0115f2ed71ee7ea316516853/include/spdlog/details/mpmc_blocking_q.h)
  - [`tests/test_async.cpp`](https://github.com/gabime/spdlog/blob/f5f173a1a57d0e2e0115f2ed71ee7ea316516853/tests/test_async.cpp)
  - [`tests/test_mpmc_q.cpp`](https://github.com/gabime/spdlog/blob/f5f173a1a57d0e2e0115f2ed71ee7ea316516853/tests/test_mpmc_q.cpp)
- **Trace:** Follow async_logger::sink_it_ and flush_ as they lock the thread-pool lifetime and post work, then follow thread_pool queue insertion, overflow selection, worker dequeue, backend sink or flush dispatch, and termination; correlate asynchronous logger and direct multi-producer/multi-consumer queue tests.

**Why this level:**

- **Language technique 3:** Generics and ownership-aware abstractions materially organize the path without expert metaprogramming.
- **Behavioral reasoning 4:** Concurrency, queue state, scheduling, resource ownership, and shutdown invariants recur and must be reasoned about together.
- **Design span 3:** The trace crosses several meaningful concurrency and logging boundaries whose responsibilities remain locally understandable.
- **Constraint burden 4:** Multiple strict concurrency, resource, reliability, and performance guarantees interact across the asynchronous handoff.
- **Placement:** The four scores 3/4/3/4 sum to 14; their arithmetic mean is 3.50 and rounds half-up to Level 4. The published result is Level 4.

**License:** MIT ([evidence 1](https://github.com/gabime/spdlog/blob/f5f173a1a57d0e2e0115f2ed71ee7ea316516853/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The repository publishes header-only and compiled packages used for application logging across desktop, server, mobile, and embedded platforms.

**Language evidence:** Logger orchestration, asynchronous queues, formatters, registries, and platform-specific sinks are C++ under include/spdlog and src.

**Coding relevance:**

Logging and bounded queues need only short explanations; the path teaches transferable producer-consumer design, ownership transfer, backpressure, worker lifecycles, synchronization, failure handling, and concurrency testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Async logger, thread-pool, and blocking-queue code names posting, overflow selection, dequeue, backend dispatch, flush, termination, and ownership transitions directly.
- **Architecture:** async_logger owns the public handoff, thread_pool schedules and dispatches work, mpmc_blocking_queue owns bounded synchronization, and backend sinks perform final output.
- **Naming and idiom:** sink_it_, flush_, post_log, post_flush, async_msg, overflow_policy, overrun_oldest, dequeue_for, process_next_msg_, and terminate state queue behavior.
- **Tests:** tests/test_async.cpp and tests/test_mpmc_q.cpp cover blocking and overrun policies, queue capacity, ordering, flush, shutdown, exceptions, multiple workers, and concurrent producers and consumers.
- **Documentation:** spdlog's asynchronous logging documentation explains thread-pool ownership, queue size, overflow policy, worker behavior, and logger lifetime for this exact path.
- **Traceability:** A log message can be followed from async_logger::sink_it_ through thread_pool insertion and overflow policy, worker dequeue and backend dispatch, then matched to logger and direct queue tests.
- **Maintainability:** Explicit logger, pool, queue, and sink boundaries plus stress and lifecycle tests constrain concurrency changes across a performance-sensitive handoff.
- **Educational value:** The path provides a bounded production study of ownership-aware asynchronous delivery in which concurrency, capacity, loss policy, and shutdown are all observable.

**Inspection record:** commit `f5f173a1a57d0e2e0115f2ed71ee7ea316516853`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `include/spdlog/async_logger-inl.h`, `include/spdlog/async_logger.h`, `include/spdlog/details/thread_pool-inl.h`, `include/spdlog/details/mpmc_blocking_q.h`, `tests/test_async.cpp`, `tests/test_mpmc_q.cpp`, `LICENSE`. GitHub Linguist label: C++.

</details>

## Level 5 — Expert

### [boostorg/asio](https://github.com/boostorg/asio)

**Language 5 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

Boost.Asio's portable asynchronous I/O library for networking, timers, executors, completion tokens, coroutines, and composed operations.

**Why study it:** The async_compose path shows how a user state machine becomes a conforming asynchronous operation while preserving completion-token return types, handler characteristics, outstanding work, cancellation, Asio work-guard release, and the model's at-most-once completion contract.

**Short context:**

- An initiating function starts background work, a completion token selects the caller-facing result mechanism, and the resulting completion handler is invoked at most once after temporary operation resources are released.
- An asynchronous agent's associated executor, allocator, and cancellation slot determine where completion runs, how memory is obtained, and how one operation receives targeted cancellation.

**Prerequisites:**

- Strong working familiarity with C++ classes, templates, references, smart pointers, RAII, standard containers, exceptions, and unit tests, plus experience tracing state, resources, or asynchronous control flow across many production files.

**Concepts this path develops:**

- Variadic completion signatures and recursive template specializations.
- Multi-step asynchronous state-machine re-entry.
- The implementation must invoke its completion handler at most once.

**What you can learn:**

- Use `include/boost/asio/compose.hpp` to study the following transferable techniques and behaviors: Variadic completion signatures, forwarding and decay, completion-token adaptation, stateful intermediate handlers, associated executor and allocator propagation, outstanding-work guards, per-operation cancellation filters, asynchronous state machines, resource lifetime, result delivery, and at-most-once completion contracts.

**Learning path:**

- **Goal:** Understand how async_compose turns a stateful implementation into a conforming asynchronous operation while preserving completion-token behavior, associated characteristics, work, cancellation, and the at-most-once result-delivery contract.
- **Start here:** [`include/boost/asio/compose.hpp`](https://github.com/boostorg/asio/blob/a7dc25b4cb6c49a6946d86ea20664f1027203225/include/boost/asio/compose.hpp) — compose.hpp exposes async_compose, its completion signature and token contract, the supplied I/O executors, cancellation policy, and the handoff into composed and async_initiate.
- **Then read:**
  - [`include/boost/asio/composed.hpp`](https://github.com/boostorg/asio/blob/a7dc25b4cb6c49a6946d86ea20664f1027203225/include/boost/asio/composed.hpp)
  - [`include/boost/asio/async_result.hpp`](https://github.com/boostorg/asio/blob/a7dc25b4cb6c49a6946d86ea20664f1027203225/include/boost/asio/async_result.hpp)
  - [`include/boost/asio/detail/composed_work.hpp`](https://github.com/boostorg/asio/blob/a7dc25b4cb6c49a6946d86ea20664f1027203225/include/boost/asio/detail/composed_work.hpp)
  - [`include/boost/asio/detail/base_from_cancellation_state.hpp`](https://github.com/boostorg/asio/blob/a7dc25b4cb6c49a6946d86ea20664f1027203225/include/boost/asio/detail/base_from_cancellation_state.hpp)
  - [`test/compose.cpp`](https://github.com/boostorg/asio/blob/a7dc25b4cb6c49a6946d86ea20664f1027203225/test/compose.cpp)
  - [`test/composed.cpp`](https://github.com/boostorg/asio/blob/a7dc25b4cb6c49a6946d86ea20664f1027203225/test/composed.cpp)
  - [`doc/overview/compose.qbk`](https://github.com/boostorg/asio/blob/a7dc25b4cb6c49a6946d86ea20664f1027203225/doc/overview/compose.qbk)
  - [`doc/overview/model/async_ops.qbk`](https://github.com/boostorg/asio/blob/a7dc25b4cb6c49a6946d86ea20664f1027203225/doc/overview/model/async_ops.qbk)
  - [`doc/overview/model/associators.qbk`](https://github.com/boostorg/asio/blob/a7dc25b4cb6c49a6946d86ea20664f1027203225/doc/overview/model/associators.qbk)
  - [`doc/overview/model/cancellation.qbk`](https://github.com/boostorg/asio/blob/a7dc25b4cb6c49a6946d86ea20664f1027203225/doc/overview/model/cancellation.qbk)
- **Trace:** Begin at async_compose's completion signature, implementation, token, and I/O objects; follow async_initiate into composed's initiation object, composed_op handler wrapping, associated executor and allocator forwarding, recursive work guards, cancellation-state setup and reset, state-machine re-entry, Asio work-guard reset, and final handler call; close both public APIs with test/compose.cpp and test/composed.cpp across zero- and one-result cases and the default, partial, and total cancellation matrix.

**Why this level:**

- **Language technique 5:** Several expert generic-programming, callable-adaptation, customization, and overload mechanisms interact pervasively across the public and intermediate-handler path.
- **Behavioral reasoning 5:** Scheduling, cancellation, state transitions, handler invocation, and resource lifetime interact across callbacks and require nonlocal asynchronous reasoning.
- **Design span 4:** The selected behavior crosses many meaningful generic and runtime boundaries while remaining one bounded Asio composition subsystem.
- **Constraint burden 5:** Several system-wide correctness, resource, compatibility, and scheduling guarantees interact across the asynchronous operation lifecycle.
- **Placement:** The four scores 5/5/4/5 sum to 19; their arithmetic mean is 4.75 and rounds half-up to Level 5. The published result is Level 5.

**License:** BSL-1.0 ([evidence 1](https://github.com/boostorg/asio/blob/a7dc25b4cb6c49a6946d86ea20664f1027203225/include/boost/asio/compose.hpp))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Boost distributes Asio as its portable low-level I/O library with versioned reference documentation, examples, tests, and release integration.

**Language evidence:** The async_compose and composed APIs, intermediate handler, work tracking, completion-token adaptation, associated executor and allocator propagation, cancellation state, and direct tests are C++ under include/boost/asio, test/compose.cpp, and test/composed.cpp.

**Coding relevance:**

The asynchronous-operation vocabulary is documented locally and consists of broadly reusable concurrency abstractions; the difficulty comes from transferable generic API design, scheduling, cancellation, resource lifetime, ownership, compatibility, and race-sensitive contracts.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Public composition, handler wrapping, work tracking, cancellation state, and token adaptation are separated into named templates with detailed lifecycle and contract comments.
- **Architecture:** async_compose exposes the API, async_result adapts tokens, composed_op owns intermediate state and handler characteristics, composed_work retains executors, and the cancellation base isolates per-operation policy.
- **Naming and idiom:** async_compose, async_initiate, composed_op, complete, composed_work, get_executor, get_allocator, reset_cancellation_state, and cancelled preserve the asynchronous model's vocabulary.
- **Tests:** test/compose.cpp and test/composed.cpp directly cover the two public composition APIs with deferred execution, lvalue and bound handlers, zero and one result arguments, single invocation in the tested state machines, and no, terminal, partial, and total cancellation behavior; they do not directly isolate associator forwarding or work guards.
- **Documentation:** The composition and asynchronous-model guides explain initiating functions, completion tokens, at-most-once handlers, resource release, associators, work tracking, cancellation slots, and the state-machine pattern used by this path.
- **Traceability:** A composed operation can be followed from its initiating function and token through handler construction, associated characteristics, state-machine callbacks, cancellation filtering, Asio work-guard reset, final result delivery, and the focused cancellation matrix.
- **Maintainability:** Explicit API, initiation, handler, work, and cancellation boundaries plus direct contract tests constrain changes to a highly generic asynchronous subsystem.
- **Educational value:** The path provides an expert production account of building a reusable asynchronous abstraction where template adaptation, scheduling, cancellation, resource lifetime, and an at-most-once completion contract must agree; composed_op helps conforming code but does not prevent a user state machine from calling complete twice.

**Inspection record:** commit `a7dc25b4cb6c49a6946d86ea20664f1027203225`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `include/boost/asio/compose.hpp`, `include/boost/asio/composed.hpp`, `include/boost/asio/async_result.hpp`, `include/boost/asio/detail/composed_work.hpp`, `include/boost/asio/detail/base_from_cancellation_state.hpp`, `test/compose.cpp`, `test/composed.cpp`, `doc/overview/compose.qbk`, `doc/overview/model/async_ops.qbk`, `doc/overview/model/associators.qbk`, `doc/overview/model/cancellation.qbk`. GitHub Linguist label: C++.

</details>

### [facebook/folly](https://github.com/facebook/folly)

**Language 5 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

Meta's performance-oriented collection of C++20 components for concurrency, containers, memory, networking, I/O, executors, futures, and utilities.

**Why study it:** The Folly Future path shows how Promise and Future coordinate through synchronized shared state and schedule exactly-once continuations on an Executor across values, exceptions, interruption, cancellation, and races.

**Short context:**

- A Future represents a value that may arrive later, a Promise completes it, and an Executor chooses where registered continuations run.

**Prerequisites:**

- Strong working familiarity with C++ classes, templates, references, smart pointers, RAII, standard containers, exceptions, and unit tests, plus experience tracing state, resources, or asynchronous control flow across many production files.

**Concepts this path develops:**

- Variadic and conditional continuation result types.
- Concurrent shared-state fulfillment and callback installation.
- Exactly-once completion and continuation execution.

**What you can learn:**

- Use `folly/futures/Future.h` to study the following transferable techniques and behaviors: Variadic and conditional continuation types, perfect forwarding, callable adaptation, type erasure, Future and SemiFuture value-category transitions, synchronized shared Core state, executor handoff, continuation chaining, exception transfer, interruption, broken promises, ownership release, destruction, and races.

**Learning path:**

- **Goal:** Understand how Folly connects a Promise and Future through synchronized shared state and schedules exactly-once continuations on an Executor across success, exception, cancellation, and race paths.
- **Start here:** [`folly/futures/Future.h`](https://github.com/facebook/folly/blob/011e8761a42b20085ce3937e73b5b7aaf482d499/folly/futures/Future.h) — folly/futures/Future.h defines the continuation and executor-facing public API that leads into Future-inl.h, Promise.h, and detail/Core.h for shared-state execution.
- **Then read:**
  - [`folly/futures/Future-inl.h`](https://github.com/facebook/folly/blob/011e8761a42b20085ce3937e73b5b7aaf482d499/folly/futures/Future-inl.h)
  - [`folly/futures/Promise.h`](https://github.com/facebook/folly/blob/011e8761a42b20085ce3937e73b5b7aaf482d499/folly/futures/Promise.h)
  - [`folly/futures/detail/Core.h`](https://github.com/facebook/folly/blob/011e8761a42b20085ce3937e73b5b7aaf482d499/folly/futures/detail/Core.h)
  - [`folly/Executor.h`](https://github.com/facebook/folly/blob/011e8761a42b20085ce3937e73b5b7aaf482d499/folly/Executor.h)
  - [`folly/futures/test/FutureTest.cpp`](https://github.com/facebook/folly/blob/011e8761a42b20085ce3937e73b5b7aaf482d499/folly/futures/test/FutureTest.cpp)
- **Trace:** Begin with Future's continuation and executor-facing API, follow then-style composition into callback installation on the shared Core, then follow Promise fulfillment, state synchronization, executor scheduling, result or exception transfer, interruption, ownership release, and broken-promise behavior; correlate the focused lifecycle, scheduling, exception, move, and race tests.

**Why this level:**

- **Language technique 5:** Multiple advanced template, value-category, type-erasure, and overload mechanisms interact pervasively throughout the API and implementation.
- **Behavioral reasoning 5:** Several advanced concurrency, scheduling, recovery, and resource-lifetime concerns interact pervasively and require nonlocal reasoning.
- **Design span 4:** Many modules, extension points, and execution modes contribute to the future path without requiring the rest of the Folly platform.
- **Constraint burden 5:** Several system-wide correctness, safety, compatibility, reliability, and performance guarantees interact across the shared asynchronous state.
- **Placement:** The four scores 5/5/4/5 sum to 19; their arithmetic mean is 4.75 and rounds half-up to Level 5. The published result is Level 5.

**License:** Apache-2.0 ([evidence 1](https://github.com/facebook/folly/blob/011e8761a42b20085ce3937e73b5b7aaf482d499/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The README states that Folly components are used extensively at Meta and underpin other production open-source C++ projects.

**Language evidence:** The component library, futures, coroutines, executors, containers, synchronization, networking, I/O, and portability layers are C++ under folly.

**Coding relevance:**

Future, Promise, and Executor concepts are standard concurrency abstractions documented locally; the path's difficulty comes from transferable template API design, shared-state synchronization, scheduling, ownership, cancellation, exception propagation, and race safety.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Future, Promise, Core, and Executor code heavily documents state ownership, callback installation, fulfillment, scheduling, result transfer, interruption, and destruction invariants.
- **Architecture:** Future and Promise expose complementary public handles, Core owns synchronized shared state, Executor controls scheduling, and adapted callbacks connect result modes.
- **Naming and idiom:** Future, SemiFuture, Promise, Core, Try, thenValue, thenTry, via, setValue, setException, raise, interruptHandler, and broken promise preserve asynchronous vocabulary.
- **Tests:** FutureTest.cpp covers values, exceptions, continuation forms, executor handoff, ordering, broken promises, interruption, collections, moves, races, and object lifetime.
- **Documentation:** Folly's Future, Promise, Executor, continuation, cancellation, and exception documentation plus source comments explain the contracts followed here.
- **Traceability:** A continuation can be followed from Future's then-style API into Core callback installation, Promise fulfillment, synchronized state transition, Executor scheduling, result transfer, and race-focused tests.
- **Maintainability:** Explicit handle, Core, Executor, and callback boundaries plus heavily instrumented lifecycle tests constrain changes to shared asynchronous state.
- **Educational value:** The path offers an expert account of typed asynchronous composition where templates, memory ordering, ownership, scheduling, and failure semantics must agree.

**Inspection record:** commit `011e8761a42b20085ce3937e73b5b7aaf482d499`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `folly/futures/Future.h`, `folly/futures/Future-inl.h`, `folly/futures/Promise.h`, `folly/futures/detail/Core.h`, `folly/Executor.h`, `folly/futures/test/FutureTest.cpp`, `LICENSE`. GitHub Linguist label: C++.

</details>

_Generated from `catalog/cpp.json`; do not edit by hand._

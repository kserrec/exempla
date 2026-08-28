# C++

10 qualified repositories. Scores assume the learner described in [the SDC rubric](../../docs/sdc.md).

[← All languages](../README.md)

## SDC 1

### [agauniyal/rang](https://github.com/agauniyal/rang)

**S1 / D2 / C1 → SDC 1**

A small header-only library that adds portable terminal colors and text styles through C++ stream operators.

**Real-world evidence:** The project ships an installable CMake, Conan, Meson, and pkg-config compatible terminal-formatting library.

**Language evidence:** Terminal detection, ANSI and native Windows coloring, stream operators, and public enums are implemented in include/rang.hpp.

**Why study it:** A compact public API exposes the real platform work behind portable terminal styling, including TTY detection and Windows console modes.

**What you can learn:**

- Operator overloading, scoped enums, stream buffers, TTY detection, platform compilation, atomic configuration, and header-only packaging.

**Prerequisites:**

- C++ streams, enums, operator overloading, conditional compilation, and basic operating-system APIs.

**Start here:** [`include/rang.hpp`](https://github.com/agauniyal/rang/blob/56419fe3348a475c8dd83852d907794cec0ec798/include/rang.hpp) — The enums lead directly into terminal capability checks and the stream insertion overloads that emit or apply styles.

**Why this level:**

- **S1:** 424 meaningful implementation LOC measured with tokei 14.0.0. Count covers the complete production header, excluding tests, packaging probes, and build metadata.
- **D2:** Platform branches require modest systems knowledge, but each operation is short and conventional.
- **C1:** One component maps style enums to one of two terminal output mechanisms.
- **Placement:** S1/D2/C1 averages to 1.33, so Rang is an SDC 1 study despite its useful portability boundary.

**Quality-gate evidence:**

- **Source quality:** Capability checks, modes, and platform-specific output are small, guarded, and separated inside the implementation namespace.
- **Architecture:** Public styling enums delegate to a single header's Unix ANSI or Windows console implementation.
- **Naming and idiom:** style, fg, bg, control, winTerm, supportsColor, and isTerminal state the terminal model plainly.
- **Tests:** Automated and visual tests exercise stream output, control modes, environment behavior, and terminal backends.
- **Documentation:** The README documents supported styles, modes, platforms, installation methods, and concrete output examples.
- **Traceability:** A stream insertion moves from an enum overload through mode and TTY checks to an ANSI sequence or Windows attribute call.
- **Maintainability:** The narrow API and isolated conditional compilation keep platform changes reviewable.
- **Educational value:** It teaches that a friendly operator-based API can still expose understandable operating-system boundaries.

**Inspection record:** commit `56419fe3348a475c8dd83852d907794cec0ec798`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `CMakeLists.txt`, `include/rang.hpp`, `test/colorTest.cpp`. GitHub Linguist label: C++. LOC exclusions: test/, test_package/.

**License:** [Unlicense](https://github.com/agauniyal/rang/blob/56419fe3348a475c8dd83852d907794cec0ec798/LICENSE)

### [kainjow/Mustache](https://github.com/kainjow/Mustache)

**S1 / D2 / C1 → SDC 1**

A dependency-free, header-only Mustache template engine for STL-compatible narrow and wide string types.

**Real-world evidence:** The repository publishes an embeddable C++ library that implements the Mustache template specification for application use.

**Language evidence:** The complete template parser, data model, renderer, escaping, sections, lambdas, and partials are implemented in mustache.hpp.

**Why study it:** One header contains a real parser-renderer pipeline, a tagged data model, context lookup, escaping, sections, partials, and error reporting.

**What you can learn:**

- Template parsing, tagged data representation, recursive rendering, context stacks, HTML escaping, callbacks, and header-only library design.

**Prerequisites:**

- C++ classes and templates, smart pointers, standard containers, iterators, callbacks, and basic parsing.

**Start here:** [`mustache.hpp`](https://github.com/kainjow/Mustache/blob/3f654942a70c46a775070d7a09ca7acfa3e205b7/mustache.hpp) — The whole library is here; begin with basic_mustache and follow parse, render_internal, and variable lookup.

**Why this level:**

- **S1:** 1,006 meaningful implementation LOC measured with tokei 14.0.0. Count covers the complete production header and excludes tests, their bundled harness, and build metadata.
- **D2:** Parsing and recursive sections add one modest concern, while the implementation remains direct and contained.
- **C1:** One component owns parsing and rendering without services, plugins, persistence, or platform boundaries.
- **Placement:** S1/D2/C1 averages to 1.33, making this a complete but approachable SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** Parsing state, data variants, rendering contexts, and error positions are explicit in a dependency-free implementation.
- **Architecture:** A typed data model feeds one parsed component tree and recursive renderer inside a single public header.
- **Naming and idiom:** Names such as delimiter_set, context, component, render_internal, and get_variable reflect the template domain.
- **Tests:** The Catch-based suite covers variables, escaping, delimiters, sections, lists, lambdas, partials, whitespace, invalid templates, and wide strings.
- **Documentation:** The README gives complete feature coverage and runnable examples for the major Mustache constructs.
- **Traceability:** A template variable can be followed from token parsing through context lookup and escaping into a focused assertion.
- **Maintainability:** One distributable header and broad behavioral tests keep changes localized despite the hand-built parser.
- **Educational value:** It demonstrates a whole useful language-processing feature without compiler-framework machinery.

**Inspection record:** commit `3f654942a70c46a775070d7a09ca7acfa3e205b7`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `CMakeLists.txt`, `mustache.hpp`, `tests/tests.cpp`. GitHub Linguist label: C++. LOC exclusions: tests/.

**License:** [BSL-1.0](https://github.com/kainjow/Mustache/blob/3f654942a70c46a775070d7a09ca7acfa3e205b7/LICENSE)

## SDC 2

### [CLIUtils/CLI11](https://github.com/CLIUtils/CLI11)

**S2 / D3 / C2 → SDC 2**

A command-line parser supporting typed options, flags, subcommands, validation, configuration files, aliases, and rich help output.

**Real-world evidence:** The repository ships a header-only, precompiled, and module-capable library through major C++ package systems.

**Language evidence:** Argument models, parsers, validators, config formats, help formatters, encoding, and public APIs are C++ under include/CLI.

**Why study it:** It turns argv into a typed command tree while handling ambiguity, inheritance, callbacks, platform conventions, configuration, and detailed diagnostics.

**What you can learn:**

- Recursive command trees, typed conversion, validators, positional matching, subcommand inheritance, configuration parsing, callbacks, and exception invariants.

**Prerequisites:**

- C++ templates, callbacks, smart pointers, containers, command-line conventions, parsing, and exception safety.

**Start here:** [`include/CLI/App.hpp`](https://github.com/CLIUtils/CLI11/blob/c1cfe00d2f3d862aecfe6e69ec810414d5f4c906/include/CLI/App.hpp) — App defines the command tree, inherited settings, options, subcommands, callbacks, and parsing entry points before their inline implementation.

**Why this level:**

- **S2:** 9,755 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party public and inline implementation headers plus production module sources, excluding tests, examples, docs, and generated single-header output.
- **D3:** Several parsing and generic concerns interact, but code uses familiar containers and explicit validation paths.
- **C2:** A few cohesive modules implement one command-line domain within one process.
- **Placement:** S2/D3/C2 averages to 2.33, making CLI11 an upper SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** Ambiguity checks preserve exception invariants and parsing stages use named helpers rather than one undifferentiated token loop.
- **Architecture:** App owns the command tree while Option, validators, converters, config handlers, and formatters provide focused collaborators.
- **Naming and idiom:** App, Option, subcommand, positional, fallthrough, configurable, callback, and formatter are consistent domain terms.
- **Tests:** The broad suite covers flags, types, subcommands, positionals, config files, Unicode, Windows syntax, errors, callbacks, and fuzz regressions.
- **Documentation:** The README, book, and examples document common and advanced parsing, integration, testing, and packaging.
- **Traceability:** An option can be followed from add_option through name-conflict checks, parse classification, conversion, validation, callback, and App tests.
- **Maintainability:** Public declarations and inline implementations are separated, while tests target the many policy combinations.
- **Educational value:** It teaches production parsing and generic APIs without the broader concerns of a full application framework.

**Inspection record:** commit `c1cfe00d2f3d862aecfe6e69ec810414d5f4c906`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `CMakeLists.txt`, `include/CLI/App.hpp`, `include/CLI/impl/App_inl.hpp`, `tests/AppTest.cpp`. GitHub Linguist label: C++. LOC exclusions: tests/, examples/, docs/.

**License:** [BSD-3-Clause](https://github.com/CLIUtils/CLI11/blob/c1cfe00d2f3d862aecfe6e69ec810414d5f4c906/LICENSE)

### [gabime/spdlog](https://github.com/gabime/spdlog)

**S2 / D3 / C2 → SDC 2**

A high-performance logging library with synchronous and asynchronous loggers, formatters, registries, and many output sinks.

**Real-world evidence:** The repository publishes header-only and compiled packages used for application logging across desktop, server, mobile, and embedded platforms.

**Language evidence:** Logger orchestration, asynchronous queues, formatters, registries, and platform-specific sinks are C++ under include/spdlog and src.

**Why study it:** It connects a familiar logging API to compile-time formatting, sink composition, bounded queues, worker threads, backtraces, files, and platform outputs.

**What you can learn:**

- Variadic formatting APIs, sink composition, bounded concurrent queues, asynchronous worker lifecycle, log filtering, formatting, and portability.

**Prerequisites:**

- C++ templates, threads, atomics, mutexes, condition variables, smart pointers, files, and logging concepts.

**Start here:** [`include/spdlog/logger.h`](https://github.com/gabime/spdlog/blob/f5f173a1a57d0e2e0115f2ed71ee7ea316516853/include/spdlog/logger.h) — The logger exposes filtering, message construction, sink fan-out, formatting, flushing, and the handoff to asynchronous subclasses.

**Why this level:**

- **S2:** 8,142 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party headers and compiled sources, excluding tests, benchmarks, examples, and the bundled fmt dependency.
- **D3:** Concurrency, formatting, and platform sinks recur, though each is isolated behind recognizable interfaces.
- **C2:** Several clear modules cooperate within one process and expose limited extension boundaries.
- **Placement:** S2/D3/C2 averages to 2.33, placing spdlog at SDC 2.

**Quality-gate evidence:**

- **Source quality:** Hot paths make filtering and ownership explicit, while concurrent queue policies and worker termination are named and tested.
- **Architecture:** Loggers create messages, formatters render them, sinks own destinations, a registry manages named instances, and a thread pool handles async delivery.
- **Naming and idiom:** logger, sink, pattern_formatter, async_msg, overflow_policy, and thread_pool match the runtime roles.
- **Tests:** Focused tests cover async ordering and overflow, sinks, files, rotation, format patterns, errors, configuration, backtraces, and platform behavior.
- **Documentation:** The README explains build modes, sinks, async setup, customization, formatting, performance, and examples.
- **Traceability:** A log call can be followed through level filtering, message creation, async enqueue, worker dispatch, sink formatting, and async tests.
- **Maintainability:** Header-only and compiled modes share implementation files, and destination-specific behavior remains behind sink types.
- **Educational value:** It is a manageable introduction to performance-aware concurrency and extension-oriented library design.

**Inspection record:** commit `f5f173a1a57d0e2e0115f2ed71ee7ea316516853`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `CMakeLists.txt`, `include/spdlog/logger.h`, `include/spdlog/details/thread_pool-inl.h`, `tests/test_async.cpp`. GitHub Linguist label: C++. LOC exclusions: tests/, bench/, example/, include/spdlog/fmt/bundled/.

**License:** [MIT](https://github.com/gabime/spdlog/blob/f5f173a1a57d0e2e0115f2ed71ee7ea316516853/LICENSE)

## SDC 3

### [catchorg/Catch2](https://github.com/catchorg/Catch2)

**S3 / D3 / C3 → SDC 3**

A C++ testing framework with expressive assertions, matchers, generators, test discovery, filtering, reporters, and benchmarking.

**Real-world evidence:** The repository releases libraries, a test runner, CMake discovery integration, and packages used to test C++ software.

**Language evidence:** Test registration, assertions, matchers, generators, reporters, command handling, execution, and discovery support are C++ under src/catch2.

**Why study it:** Because the framework tests itself, learners can trace macros into registration, execution, assertion decomposition, event capture, reporting, and end-to-end test scripts.

**What you can learn:**

- Macro-generated registration, static initialization, expression decomposition, type-erased test invocation, filtering, sharding, reporters, and CLI lifecycle.

**Prerequisites:**

- C++ templates and macros, static initialization, polymorphism, exceptions, command-line parsing, testing concepts, and build integration.

**Start here:** [`src/catch2/catch_session.cpp`](https://github.com/catchorg/Catch2/blob/317ac1ed4c0bb6e6b91eafc817e05c488feffcb3/src/catch2/catch_session.cpp) — Session connects command-line configuration, registry state, test execution, reporters, output, errors, and process exit codes.

**Why this level:**

- **S3:** 21,367 meaningful implementation LOC measured with tokei 14.0.0. Count covers production framework code under src/catch2, excluding self-tests, scripts, benchmarks, fuzzers, examples, docs, and third-party code.
- **D3:** Several advanced language mechanisms matter, but orchestration and data structures remain conventional and well named.
- **C3:** A test crosses registries, configuration, filtering, invocation, assertion capture, reporters, output, and build-system discovery.
- **Placement:** S3/D3/C3 makes Catch2 a balanced SDC 3 codebase.

**Quality-gate evidence:**

- **Source quality:** Framework state and interfaces are explicit, ownership is deliberate, and compatibility macros stay behind dedicated headers.
- **Architecture:** Registries, session/configuration, test tracking, assertion handling, matchers, reporters, generators, and discovery have distinct roles.
- **Naming and idiom:** TestCaseHandle, Session, RegistryHub, AssertionHandler, Reporter, and TestSpec expose the framework model.
- **Tests:** Self-tests, extra executables, approval outputs, and Python/CMake scripts cover framework behavior, diagnostics, discovery, crashes, and regressions.
- **Documentation:** Versioned user and contributor documentation covers assertions, matchers, generators, reporters, configuration, integrations, and internals.
- **Traceability:** A declared test can be followed from macro registration into TestRegistry, Session filtering and execution, assertion events, and reporter output.
- **Maintainability:** Interfaces separate extensions from the core, while the self-hosting test matrix protects many compilers and configurations.
- **Educational value:** It reveals the machinery behind familiar testing syntax in a repository whose own tests demonstrate the design.

**Inspection record:** commit `317ac1ed4c0bb6e6b91eafc817e05c488feffcb3`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `CMakeLists.txt`, `src/catch2/catch_session.cpp`, `src/catch2/internal/catch_test_case_registry_impl.cpp`, `tests/SelfTest/UsageTests/Matchers.tests.cpp`. GitHub Linguist label: C++. LOC exclusions: tests/, benchmarks/, fuzzing/, examples/, third_party/.

**License:** [BSL-1.0](https://github.com/catchorg/Catch2/blob/317ac1ed4c0bb6e6b91eafc817e05c488feffcb3/LICENSE.txt)

### [fmtlib/fmt](https://github.com/fmtlib/fmt)

**S3 / D4 / C2 → SDC 3**

A fast type-safe formatting library that implements the model behind C++20 std::format and C++23 std::print.

**Real-world evidence:** The repository releases a production formatting library used directly and as the basis of standard-library formatting APIs.

**Language evidence:** Format parsing, compile-time checking, argument erasure, numeric algorithms, Unicode handling, and output APIs are C++ under include/fmt and src.

**Why study it:** It combines a small public API with compile-time parsing, type erasure, buffer management, correct floating-point conversion, Unicode, and compiler portability.

**What you can learn:**

- Compile-time format parsing, variadic templates, type erasure, output buffers, Dragonbox conversion, Unicode, customization points, and compiler portability.

**Prerequisites:**

- Advanced C++ templates and constexpr, floating-point representation, parsing, memory layout, iterators, and Unicode basics.

**Start here:** [`include/fmt/base.h`](https://github.com/fmtlib/fmt/blob/e76a9520a3c339d2cb6a1510db43a05ea9bd8ae6/include/fmt/base.h) — The base API introduces format strings, argument mapping, buffers, parsing contexts, and the path from typed calls to erased formatting.

**Why this level:**

- **S3:** 13,832 meaningful implementation LOC measured with tokei 14.0.0. Count covers production headers and compiled sources, excluding tests, fuzzers, documentation, release tooling, and bundled test dependencies.
- **D4:** Advanced type machinery, constexpr execution, binary number conversion, and portability recur throughout the core.
- **C2:** Despite deep internals, the system is one library with a small set of cohesive formatting modules.
- **Placement:** S3/D4/C2 averages exactly to SDC 3, separating code difficulty from system breadth.

**Quality-gate evidence:**

- **Source quality:** Non-obvious algorithms and compatibility branches are documented, assertions protect invariants, and hot abstractions minimize overhead.
- **Architecture:** A base API and erased argument model support formatting algorithms plus optional ranges, chrono, OS, color, and printf modules.
- **Naming and idiom:** format_string, parse_context, appender, buffer, formatter, and format_arg consistently describe the pipeline.
- **Tests:** Extensive unit, compile-failure, fuzz, portability, Unicode, numeric, and integration tests protect both output and diagnostics.
- **Documentation:** The README and maintained API/syntax documentation explain safety, performance, customization, build modes, and every format family.
- **Traceability:** A format call can be followed from compile-time string checking through argument mapping, parsing, formatting, buffer append, and format tests.
- **Maintainability:** Core concepts are centralized and exhaustive tests cover compilers, standards, types, and malformed formats.
- **Educational value:** It is an excellent study of zero-overhead API design and algorithmic library engineering.

**Inspection record:** commit `e76a9520a3c339d2cb6a1510db43a05ea9bd8ae6`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `CMakeLists.txt`, `include/fmt/base.h`, `include/fmt/format.h`, `test/format-test.cc`. GitHub Linguist label: C++. LOC exclusions: test/, doc/, support/.

**License:** [MIT](https://github.com/fmtlib/fmt/blob/e76a9520a3c339d2cb6a1510db43a05ea9bd8ae6/LICENSE)

## SDC 4

### [facebook/folly](https://github.com/facebook/folly)

**S5 / D4 / C4 → SDC 4**

Meta's performance-oriented collection of C++20 components for concurrency, containers, memory, networking, I/O, executors, futures, and utilities.

**Real-world evidence:** The README states that Folly components are used extensively at Meta and underpin other production open-source C++ projects.

**Language evidence:** The component library, futures, coroutines, executors, containers, synchronization, networking, I/O, and portability layers are C++ under folly.

**Why study it:** It offers many expert library case studies under one roof, unified by high-scale performance, portability, concurrency, and careful ownership.

**What you can learn:**

- Futures and coroutines, executors, lock-free and concurrent structures, allocators, I/O, networking, portability, benchmarking, and performance tradeoffs.

**Prerequisites:**

- Advanced C++20, concurrency and memory models, atomics, templates, networking, operating-system APIs, performance analysis, and large-library navigation.

**Start here:** [`folly/futures/Future.h`](https://github.com/facebook/folly/blob/011e8761a42b20085ce3937e73b5b7aaf482d499/folly/futures/Future.h) — The documented future API leads into shared state, continuations, executors, interruption, error transport, and a large focused test suite.

**Why this level:**

- **S5:** 245,932 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party Folly implementation, excluding tests, benchmarks, documentation, generated build content, and dependency-build tooling.
- **D4:** Advanced concurrency, representation, allocation, vectorization, and performance constraints recur across central components.
- **C4:** Many library families interoperate, but Folly remains a component library rather than one distributed product or compiler platform.
- **Placement:** S5/D4/C4 averages to 4.33, honestly placing this very large library platform at SDC 4.

**Quality-gate evidence:**

- **Source quality:** Performance-sensitive choices document invariants and ownership, and specialized primitives are backed by reusable low-level utilities.
- **Architecture:** Relatively independent component families share portability, memory, synchronization, executor, and error-handling foundations.
- **Naming and idiom:** Future, Promise, Executor, Baton, EventBase, IOBuf, F14, and synchronization terms map consistently to their domains.
- **Tests:** Component-level unit, stress, benchmark, portability, concurrency, and regression tests accompany the library families.
- **Documentation:** The README, per-component docs, API comments, examples, and build guidance explain design and use, though breadth requires selective navigation.
- **Traceability:** A Future continuation can be followed through its shared Core, executor scheduling, result or exception propagation, interruption, and Future tests.
- **Maintainability:** Component ownership and focused test neighbors help contain a large flat library whose internal dependencies are intentionally permissive.
- **Educational value:** It is a deep advanced library-reading corpus where learners can choose bounded subsystems before mapping the whole repository.

**Inspection record:** commit `011e8761a42b20085ce3937e73b5b7aaf482d499`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `CMakeLists.txt`, `folly/futures/Future.h`, `folly/executors/CPUThreadPoolExecutor.cpp`, `folly/futures/test/FutureTest.cpp`. GitHub Linguist label: C++. LOC exclusions: **/test/, *Test.cpp, *Benchmark.cpp, build/.

**License:** [Apache-2.0](https://github.com/facebook/folly/blob/011e8761a42b20085ce3937e73b5b7aaf482d499/LICENSE)

### [protocolbuffers/protobuf](https://github.com/protocolbuffers/protobuf)

**S5 / D4 / C4 → SDC 4**

A schema language, compiler, binary wire format, reflection system, and multi-language runtime ecosystem for structured data interchange.

**Real-world evidence:** The repository releases protoc and maintained runtime packages used for data exchange and RPC contracts across many languages.

**Language evidence:** The protoc compiler, descriptor system, reflection, generated-code runtime, wire formats, arenas, text/JSON support, and core conformance machinery are principally C++ under src/google/protobuf.

**Why study it:** It joins a recursive-descent language front end to descriptors, code generation, compact binary encoding, reflection, compatibility editions, and many runtime implementations.

**What you can learn:**

- Language parsing, descriptors and reflection, wire encoding, generated APIs, arena allocation, schema evolution, multi-language runtimes, conformance, and build generation.

**Prerequisites:**

- Advanced C++, compilers, binary protocols, memory management, reflection, code generation, API compatibility, and monorepo navigation.

**Start here:** [`src/google/protobuf/compiler/parser.cc`](https://github.com/protocolbuffers/protobuf/blob/5b1c20741838b8359193b97895cb0ff35b4ecf79/src/google/protobuf/compiler/parser.cc) — The readable recursive-descent parser turns source tokens into descriptor protos that drive the compiler and runtime ecosystem.

**Why this level:**

- **S5:** 516,827 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party compiler and production runtimes across supported languages, excluding tests, benchmarks, fuzzers, generated sources, examples, docs, and third-party code.
- **D4:** Parsing, descriptors, arenas, reflection, encoding, generated APIs, and compatibility rules require several advanced domains.
- **C4:** Many packages share a schema and compatibility contract, but the repository is a bounded serialization platform rather than a distributed application.
- **Placement:** S5/D4/C4 averages to 4.33, so Protobuf is a large SDC 4 system rather than being promoted by size alone.

**Quality-gate evidence:**

- **Source quality:** Core parsers and descriptor builders expose error recovery and invariants, while low-level runtime paths isolate representation-specific optimization.
- **Architecture:** Schema parsing feeds descriptors and code generators; language runtimes implement shared wire, reflection, JSON/text, and compatibility contracts.
- **Naming and idiom:** Descriptor, Message, Field, Arena, CodedStream, Parser, Generator, and Edition consistently connect schema and runtime concepts.
- **Tests:** Large unit, conformance, compatibility, generated-code, language-runtime, fuzz, and integration suites protect the wire and API contracts.
- **Documentation:** The README and official language, encoding, API, edition, and contributor documentation cover use and architecture.
- **Traceability:** A field declaration can be followed through parser output, descriptor construction, code generation, runtime reflection, wire encoding, and descriptor tests.
- **Maintainability:** Shared descriptors and conformance rules anchor many runtimes, while language-specific packages own their implementation details.
- **Educational value:** It is a strong advanced study of how one protocol definition becomes compatible code and bytes across ecosystems.

**Inspection record:** commit `5b1c20741838b8359193b97895cb0ff35b4ecf79`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `CMakeLists.txt`, `src/google/protobuf/compiler/parser.cc`, `src/google/protobuf/descriptor.cc`, `src/google/protobuf/descriptor_unittest.cc`. GitHub Linguist label: C++. LOC exclusions: **/*test*, **/*benchmark*, **/*fuzz*, **/*generated*, third_party/.

**License:** [BSD-3-Clause](https://github.com/protocolbuffers/protobuf/blob/5b1c20741838b8359193b97895cb0ff35b4ecf79/LICENSE)

## SDC 5

### [llvm/llvm-project](https://github.com/llvm/llvm-project)

**S5 / D5 / C5 → SDC 5**

A compiler and toolchain monorepo containing LLVM, Clang, LLD, LLDB, MLIR, language runtimes, standard libraries, sanitizers, and optimization tools.

**Real-world evidence:** The repository builds production compilers, linkers, debuggers, runtimes, libraries, and developer tools used across operating systems and hardware targets.

**Language evidence:** LLVM IR, optimization, code generation, Clang, linkers, debuggers, MLIR, runtimes, standard libraries, and tools are overwhelmingly implemented in C++ despite GitHub's specialized LLVM label.

**Why study it:** It is a definitive compiler-platform corpus: language semantics become ASTs and IR, passes transform programs, backends target machines, linkers emit binaries, and runtimes execute them.

**What you can learn:**

- Compiler front ends, semantic analysis, IR design, optimization passes, instruction selection, object formats, linking, debugging, runtimes, target backends, and toolchain testing.

**Prerequisites:**

- Expert C++, compiler theory, programming-language semantics, dataflow analysis, assembly and ABIs, object formats, operating systems, and very large monorepo navigation.

**Start here:** [`llvm/lib/IR/Instructions.cpp`](https://github.com/llvm/llvm-project/blob/6d890e71354accdc496fdd9ef4f1fce8b366c7c4/llvm/lib/IR/Instructions.cpp) — LLVM instruction construction and invariants provide a bounded entry into the shared intermediate representation used by analyses, transforms, and backends.

**Why this level:**

- **S5:** 6,754,140 meaningful implementation LOC measured with tokei 14.0.0. Count covers major first-party compiler, tool, runtime, and library projects, excluding tests, benchmarks, examples, docs, generated content, and third-party code.
- **D5:** Expert algorithms, domain theory, low-level representation, concurrency, and metaprogramming recur across every major project.
- **C5:** Front ends, IR, optimizers, backends, linkers, debuggers, runtimes, libraries, tools, and targets form a deeply interconnected platform.
- **Placement:** S5/D5/C5 makes LLVM Project a maximum SDC 5 capstone.

**Quality-gate evidence:**

- **Source quality:** Core abstractions pair explicit invariants and diagnostics with reusable support libraries and extensive target-independent algorithms.
- **Architecture:** Shared support and IR layers connect distinct front ends, optimization pipelines, target backends, linkers, debuggers, runtimes, libraries, and tools.
- **Naming and idiom:** Decl, Sema, Instruction, Pass, MachineFunction, Target, ObjectFile, and Runtime vocabulary remains stable across subsystems.
- **Tests:** Unit, lit, regression, conformance, code-generation, execution, sanitizer, target, and integration suites cover languages and platforms at enormous scale.
- **Documentation:** Architecture, command, API, language-reference, target, pass, testing, coding-standard, and contributor documentation is extensive.
- **Traceability:** An instruction can be traced from Clang semantic analysis into LLVM IR construction, transformations, target lowering, and focused IR tests.
- **Maintainability:** Project and library boundaries, table-driven definitions, shared ADTs, diagnostics, review conventions, and layered tests support many specialist teams.
- **Educational value:** It is a premier capstone for understanding production compilers and native toolchains, best approached one subsystem at a time.

**Inspection record:** commit `6d890e71354accdc496fdd9ef4f1fce8b366c7c4`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `llvm/CMakeLists.txt`, `llvm/lib/IR/Instructions.cpp`, `clang/lib/Sema/SemaExpr.cpp`, `llvm/unittests/IR/InstructionsTest.cpp`. GitHub Linguist label: LLVM. LOC exclusions: **/*test*, **/*Test*, **/*benchmark*, **/*examples*, **/*docs*, **/*generated*, third-party/, third_party/.

**License:** [Apache-2.0 WITH LLVM-exception](https://github.com/llvm/llvm-project/blob/6d890e71354accdc496fdd9ef4f1fce8b366c7c4/llvm/LICENSE.TXT)

### [opencv/opencv](https://github.com/opencv/opencv)

**S5 / D5 / C5 → SDC 5**

A computer-vision and image-processing platform spanning matrix primitives, algorithms, video, calibration, machine learning, DNN inference, codecs, and hardware acceleration.

**Real-world evidence:** The repository builds and releases the OpenCV library used by production desktop, mobile, embedded, robotics, and server applications.

**Language evidence:** Core arrays, image processing, calibration, features, video, DNN, codecs, hardware backends, and public APIs are principally C++ across modules.

**Why study it:** It demonstrates how numerical algorithms, data layout, SIMD, CPU dispatch, OpenCL, codecs, device backends, and stable APIs coexist in a long-lived native platform.

**What you can learn:**

- Image and matrix representation, numerical vision algorithms, SIMD and hardware dispatch, GPU backends, codecs, module architecture, bindings, performance testing, and portability.

**Prerequisites:**

- Advanced C++, linear algebra, image processing, numerical methods, memory layout, SIMD/GPU concepts, build configuration, and large-system navigation.

**Start here:** [`modules/core/src/matrix.cpp`](https://github.com/opencv/opencv/blob/397e70d0447d7d5a5ada6dfe3302ee78856eae6b/modules/core/src/matrix.cpp) — Matrix shape, allocation, reference counting, views, copying, and invariants underpin nearly every higher-level OpenCV algorithm.

**Why this level:**

- **S5:** 705,649 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production modules and apps, excluding tests, performance harnesses, samples, generated bindings/kernels, documentation, and third-party code.
- **D5:** Expert mathematics, representation, performance, and hardware knowledge recur in core learning paths.
- **C5:** Core data structures connect dozens of algorithm modules, dispatch layers, device backends, codecs, bindings, and build configurations.
- **Placement:** All dimensions are 5, making OpenCV an unambiguous SDC 5 platform.

**Quality-gate evidence:**

- **Source quality:** Core code uses assertions, dispatch boundaries, specialized kernels, and explicit data-layout rules to contain performance-sensitive behavior.
- **Architecture:** A core matrix/runtime layer supports modular algorithm families, codecs, hardware abstraction, DNN, apps, and generated bindings.
- **Naming and idiom:** Mat, InputArray, OutputArray, cvtColor, AlgorithmHint, HAL, and module names consistently express the vision domain.
- **Tests:** Module unit, accuracy, regression, performance, backend, codec, binding, and platform suites exercise a vast input and hardware matrix.
- **Documentation:** API references, tutorials, module guides, samples, wiki material, and contribution rules accompany the codebase.
- **Traceability:** A color conversion can be followed from cvtColor dispatch through CPU or OpenCL kernels, data-shape checks, and imgproc/core tests.
- **Maintainability:** Module ownership and hardware abstraction constrain a large compatibility matrix, with tests colocated by domain.
- **Educational value:** It is a capstone for reading high-performance mathematical software across platform and hardware boundaries.

**Inspection record:** commit `397e70d0447d7d5a5ada6dfe3302ee78856eae6b`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `CMakeLists.txt`, `modules/core/src/matrix.cpp`, `modules/imgproc/src/color.cpp`, `modules/core/test/test_mat.cpp`. GitHub Linguist label: C++. LOC exclusions: **/*test*, **/*perf*, samples/, 3rdparty/, **/*generated*.

**License:** [Apache-2.0](https://github.com/opencv/opencv/blob/397e70d0447d7d5a5ada6dfe3302ee78856eae6b/LICENSE)

_Generated from `catalog/cpp.json`; do not edit by hand._

# Go

10 qualified repositories. Scores assume the learner described in [the SDC rubric](../../docs/sdc.md).

[← All languages](../README.md)

## SDC 1

### [mattn/go-isatty](https://github.com/mattn/go-isatty)

**S1 / D2 / C1 → SDC 1**

A small cross-platform library that determines whether a file descriptor is a terminal or a Cygwin/MSYS terminal.

**Real-world evidence:** The repository publishes a Go module intended for command-line programs that must adapt output to terminal capabilities.

**Language evidence:** Terminal detection, operating-system branches, and the public API are implemented in Go files selected by build constraints.

**Why study it:** It offers a very small, concrete introduction to build tags, platform system calls, file descriptors, and keeping one API consistent across operating systems.

**What you can learn:**

- Go build constraints, Unix ioctl calls, Windows console detection, Cygwin/MSYS pipe recognition, file descriptors, and platform-specific tests.

**Prerequisites:**

- Go packages and build tags, basic operating-system concepts, file descriptors or handles, and unit testing.

**Start here:** [`isatty_others.go`](https://github.com/mattn/go-isatty/blob/c44dc0b9c702c76577fdb7898032969e0611efc2/isatty_others.go) — The Unix implementation shows the common API and ioctl-based decision before the learner compares BSD and Windows variants.

**Why this level:**

- **S1:** 165 meaningful implementation LOC measured with tokei 14.0.0. Count includes every platform production implementation and excludes tests and module metadata.
- **D2:** The operating-system boundary is unfamiliar to many learners, but each platform implementation is short and explicit.
- **C1:** The package exposes two checks and has no runtime components beyond the local operating-system query.
- **Placement:** S1/D2/C1 averages to 1.33, making go-isatty an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** Each platform file performs the minimum required system query and returns a direct boolean result.
- **Architecture:** Build constraints select focused Unix, BSD, Windows, App Engine, and unsupported implementations behind one API.
- **Naming and idiom:** IsTerminal and IsCygwinTerminal describe observable questions while platform suffixes make compilation boundaries visible.
- **Tests:** Unix and Windows tests exercise real descriptors or handles, standard streams, files, and the Cygwin/MSYS path where supported.
- **Documentation:** The README explains both checks, supported platforms, installation, usage, and licensing.
- **Traceability:** A call to IsTerminal can be followed from the public symbol to the active build-tagged file, system call, and matching platform test.
- **Maintainability:** Small independent platform files prevent conditional logic from accumulating inside a single implementation.
- **Educational value:** It is a bounded example of designing a portable Go facade over genuinely different operating-system mechanisms.

**Inspection record:** commit `c44dc0b9c702c76577fdb7898032969e0611efc2`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `go.mod`, `isatty_others.go`, `isatty_bsd.go`, `isatty_windows.go`, `isatty_others_test.go`, `isatty_windows_test.go`, `LICENSE`. GitHub Linguist label: Go. LOC exclusions: *_test.go.

**License:** [MIT](https://github.com/mattn/go-isatty/blob/c44dc0b9c702c76577fdb7898032969e0611efc2/LICENSE)

### [tidwall/match](https://github.com/tidwall/match)

**S1 / D2 / C1 → SDC 1**

A compact wildcard-matching library with Unicode support and an optional complexity limit.

**Real-world evidence:** The repository publishes an importable Go module for matching strings against wildcard patterns in applications and libraries.

**Language evidence:** The wildcard matcher, limit-aware traversal, Unicode handling, and public API are implemented in the root Go package.

**Why study it:** Its tiny surface turns a familiar feature into a careful lesson in byte versus rune handling, escaping, suffix optimization, and bounding adversarial work.

**What you can learn:**

- Iterative wildcard matching, UTF-8 decoding, escape rules, fast-path trimming, complexity budgets, fuzzing, and denial-of-service-aware API design.

**Prerequisites:**

- Go functions and loops, strings and byte slices, UTF-8 basics, table-driven tests, and elementary algorithm analysis.

**Start here:** [`match.go`](https://github.com/tidwall/match/blob/afc69bce52e08c02e78156a7697bd808fc868ec5/match.go) — The complete algorithm and both public entry points fit in one file, so every branch can be followed directly into its tests.

**Why this level:**

- **S1:** 205 meaningful implementation LOC measured with tokei 14.0.0. Count covers the root production package and excludes tests and repository metadata.
- **D2:** The algorithm has a few subtle edge cases, but it is compact, iterative, and locally explained.
- **C1:** There is no persistence, networking, shared state, or cross-package control flow.
- **Placement:** S1/D2/C1 averages to 1.33, making match an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** The implementation separates public wrappers from the internal traversal, documents the limit contract, and keeps allocation and state minimal.
- **Architecture:** One package contains the matcher and an optional limit-aware variant without unnecessary layers.
- **Naming and idiom:** Match, MatchLimit, Allowable, pattern, str, and maxcomp expose the small domain directly.
- **Tests:** Deterministic, randomized, Unicode, escape, allowable-range, complexity-limit, regression, and fuzz tests reveal the matching contract.
- **Documentation:** The README states the wildcard grammar, examples, complexity protection, installation, and license.
- **Traceability:** A pattern can be traced from Match into the shared matcher loop and then to literal, wildcard, escape, Unicode, and limit tests.
- **Maintainability:** The small API, no dependencies, bounded state, and broad edge-case suite make changes easy to reason about.
- **Educational value:** It shows that even a tiny text algorithm benefits from explicit adversarial limits and Unicode-aware decisions.

**Inspection record:** commit `afc69bce52e08c02e78156a7697bd808fc868ec5`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `go.mod`, `match.go`, `match_test.go`, `LICENSE`. GitHub Linguist label: Go. LOC exclusions: *_test.go.

**License:** [MIT](https://github.com/tidwall/match/blob/afc69bce52e08c02e78156a7697bd808fc868ec5/LICENSE)

## SDC 2

### [robfig/cron](https://github.com/robfig/cron)

**S1 / D3 / C2 → SDC 2**

A cron expression parser and in-process job scheduler for Go applications.

**Real-world evidence:** The repository publishes a versioned Go module for applications that schedule recurring work inside a process.

**Language evidence:** The schedule parser, scheduler loop, job wrappers, and public interfaces are implemented in the root Go package.

**Why study it:** It combines parsing, time arithmetic, goroutines, channels, job ordering, lifecycle state, and middleware-style wrappers without becoming a large codebase.

**What you can learn:**

- Cron expression parsing, time-zone-aware schedule calculation, event-loop ownership, goroutines and channels, sorted job queues, lifecycle APIs, and composable job wrappers.

**Prerequisites:**

- Go interfaces and structs, goroutines and channels, time.Time and locations, parsing, sorting, and table-driven tests.

**Start here:** [`cron.go`](https://github.com/robfig/cron/blob/bc59245fe10efaed9d51b56900192527ed733435/cron.go) — Cron.run owns the scheduler state and exposes how additions, removals, snapshots, timers, stops, and job launches are serialized.

**Why this level:**

- **S1:** 884 meaningful implementation LOC measured with tokei 14.0.0. Count covers scheduler, parser, specification, constants, chain, and logger production files while excluding tests.
- **D3:** The code is readable, but concurrent lifecycle behavior and calendar semantics require material prerequisite knowledge.
- **C2:** Several responsibilities interact, but all scheduling state is coordinated within one process and one owning loop.
- **Placement:** S1/D3/C2 averages to 2.00, making cron an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** The scheduler centralizes mutable state, the parser isolates grammar decisions, and job wrappers keep recovery and overlap policies composable.
- **Architecture:** Clear Schedule, Job, Entry, Parser, Cron, Chain, and Logger abstractions separate timing, execution, and configuration.
- **Naming and idiom:** EntryID, Schedule.Next, AddFunc, Entries, SkipIfStillRunning, and Recover communicate the scheduling domain in ordinary Go.
- **Tests:** Parser, time-zone, daylight-saving, ordering, add/remove, stop, wrapper, panic recovery, and concurrent behavior tests specify difficult boundaries.
- **Documentation:** The README, package documentation, examples, compatibility notes, and issue-linked change log explain both normal use and semantic choices.
- **Traceability:** Adding a job can be followed through parsing, entry creation, the run-loop channel, next-time sorting, timer wake-up, job launch, and lifecycle tests.
- **Maintainability:** Single-owner state, narrow interfaces, options, and extensive time-based tests contain concurrency and compatibility risk.
- **Educational value:** It teaches how to make a stateful concurrent service small enough that its full control loop remains understandable.

**Inspection record:** commit `bc59245fe10efaed9d51b56900192527ed733435`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `go.mod`, `cron.go`, `parser.go`, `chain.go`, `cron_test.go`, `parser_test.go`, `LICENSE`. GitHub Linguist label: Go. LOC exclusions: *_test.go.

**License:** [MIT](https://github.com/robfig/cron/blob/bc59245fe10efaed9d51b56900192527ed733435/LICENSE)

### [spf13/pflag](https://github.com/spf13/pflag)

**S2 / D2 / C2 → SDC 2**

A drop-in Go flag package that adds POSIX/GNU-style long options, shorthand flags, and richer flag-set behavior.

**Real-world evidence:** The repository publishes an importable command-line parsing module designed for Go applications and compatibility with the standard flag package.

**Language evidence:** GNU-style parsing, FlagSet state, typed values, normalization, deprecation, and compatibility behavior are implemented in Go.

**Why study it:** It shows how a stable library grows around one core parser while preserving compatibility, typed conversions, diagnostics, annotations, and ergonomic command-line conventions.

**What you can learn:**

- Command-line token parsing, typed Value interfaces, FlagSet state, shorthand clusters, normalization, deprecation, compatibility adapters, error policies, and API evolution.

**Prerequisites:**

- Go interfaces, maps and slices, error handling, command-line conventions, string conversion, and table-driven testing.

**Start here:** [`flag.go`](https://github.com/spf13/pflag/blob/4f8e9056816a26ecbac9fe26cde50968eb3626f8/flag.go) — FlagSet and parseLongArg or parseSingleShortArg connect registration, token interpretation, mutation, errors, and usage behavior.

**Why this level:**

- **S2:** 4,755 meaningful implementation LOC measured with tokei 14.0.0. Count includes the parser and all production typed flag implementations, excluding tests and examples.
- **D2:** There are many edge cases and value types, but control flow and conversions remain direct and idiomatic.
- **C2:** The package has several cohesive files around one parser and no services, persistence, or distributed behavior.
- **Placement:** S2/D2/C2 averages to 2.00, making pflag an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** Parsing branches make token cases explicit, typed values isolate conversion, and errors preserve actionable context.
- **Architecture:** FlagSet owns registration and parsing while small Value implementations provide type-specific behavior behind a standard interface.
- **Naming and idiom:** FlagSet, Value, Changed, NoOptDefVal, Shorthand, NormalizeFunc, and ParseErrorsWhitelist expose command-line semantics.
- **Tests:** Extensive tests cover long and short syntax, clusters, defaults, normalization, deprecation, unknown flags, type conversions, compatibility, and regressions.
- **Documentation:** The README documents differences from the standard package, usage, shorthand forms, normalization, deprecation, and compatibility.
- **Traceability:** A token can be followed from Parse through long or shorthand handling, flag lookup, Value.Set, Changed state, and focused parser tests.
- **Maintainability:** The central parser, stable interfaces, one-file value types, and broad compatibility suite constrain changes to a mature API.
- **Educational value:** It is a strong example of evolving a familiar standard-library design while keeping compatibility and edge cases visible.

**Inspection record:** commit `4f8e9056816a26ecbac9fe26cde50968eb3626f8`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `go.mod`, `flag.go`, `string.go`, `flag_test.go`, `LICENSE`. GitHub Linguist label: Go. LOC exclusions: *_test.go.

**License:** [BSD-3-Clause](https://github.com/spf13/pflag/blob/4f8e9056816a26ecbac9fe26cde50968eb3626f8/LICENSE)

## SDC 3

### [gin-gonic/gin](https://github.com/gin-gonic/gin)

**S2 / D3 / C3 → SDC 3**

A high-performance HTTP web framework with routing, middleware, request binding, rendering, recovery, and server utilities.

**Real-world evidence:** The repository publishes the Gin Go module for building HTTP services and documents supported production deployment patterns.

**Language evidence:** The HTTP engine, radix route trees, request context, middleware chain, binding, rendering, recovery, and server adapters are implemented in Go.

**Why study it:** It provides a compact but substantial framework path from net/http through route matching, pooled request context, middleware control flow, input binding, output rendering, and recovery.

**What you can learn:**

- HTTP framework architecture, radix-tree routing, middleware chains, context pooling, request binding and validation, rendering, panic recovery, trusted proxies, and net/http integration.

**Prerequisites:**

- Go interfaces and concurrency basics, net/http, HTTP semantics, trees, middleware, serialization formats, reflection, and integration testing.

**Start here:** [`gin.go`](https://github.com/gin-gonic/gin/blob/dcaa4296d111981ffb31ac3eba90bb63e1eb5ab9/gin.go) — Engine.ServeHTTP and handleHTTPRequest connect the standard HTTP entry point to context pooling, route lookup, middleware execution, and response handling.

**Why this level:**

- **S2:** 5,468 meaningful implementation LOC measured with tokei 14.0.0. Count includes all production framework packages while excluding tests, examples, documentation, fixtures, and generated assets.
- **D3:** Framework internals combine several moderate concepts, but responsibilities and request flow remain inspectable.
- **C3:** A request crosses multiple framework layers and protocol boundaries, though the system remains a single library in one process.
- **Placement:** S2/D3/C3 averages to 2.67 and rounds to SDC 3.

**Quality-gate evidence:**

- **Source quality:** Hot-path routing and context reuse are contained, middleware control flow is explicit, and error or recovery behavior is visible at boundaries.
- **Architecture:** Engine and RouterGroup configure route trees; Context drives each request; focused binding, render, middleware, and server packages provide services.
- **Naming and idiom:** Engine, Context, HandlerFunc, Next, Abort, RouterGroup, Routes, Bind, Render, and Recovery describe the HTTP framework model.
- **Tests:** Unit, integration, fuzz, race-sensitive, server, TLS, h2c, routing, middleware, binding, rendering, proxy, and regression tests cover the public contract.
- **Documentation:** The README, package docs, examples, benchmarks, deployment notes, API docs, and migration guidance give several entry paths.
- **Traceability:** An HTTP request can be followed from ServeHTTP through context reset, radix lookup, handler chain execution, binding or rendering, response writing, and request tests.
- **Maintainability:** Stable core types, specialized packages, options, benchmarks, fuzzing, and broad compatibility tests contain performance-driven code.
- **Educational value:** It is a manageable framework codebase for studying the gap between a standard-library HTTP server and a production web framework.

**Inspection record:** commit `dcaa4296d111981ffb31ac3eba90bb63e1eb5ab9`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `go.mod`, `gin.go`, `context.go`, `tree.go`, `gin_test.go`, `LICENSE`. GitHub Linguist label: Go. LOC exclusions: *_test.go, examples/, docs/, testdata/.

**License:** [MIT](https://github.com/gin-gonic/gin/blob/dcaa4296d111981ffb31ac3eba90bb63e1eb5ab9/LICENSE)

### [spf13/cobra](https://github.com/spf13/cobra)

**S2 / D3 / C3 → SDC 3**

A framework for building command-line applications with nested commands, flags, help, validation, and shell completion.

**Real-world evidence:** The repository publishes the Cobra Go module and its generator for developers building production command-line applications.

**Language evidence:** Command trees, execution, argument validation, flag inheritance, help, usage, and completion behavior are implemented in Go.

**Why study it:** It demonstrates how a compact framework coordinates command trees, inherited state, lifecycle hooks, documentation, validation, suggestions, and multiple shell protocols.

**What you can learn:**

- Tree-structured command dispatch, flag inheritance, lifecycle hooks, argument contracts, help and usage templates, shell completion protocols, error handling, and framework API design.

**Prerequisites:**

- Comfort with Go interfaces, pointers, closures, pflag-style parsing, tree traversal, templates, command-line UX, and test doubles.

**Start here:** [`command.go`](https://github.com/spf13/cobra/blob/adbc8813901bba65827259daa8e22ff94ec1f30e/command.go) — Command.Execute and execute connect tree lookup, flag parsing, validation, hooks, context, errors, help, and completion behavior.

**Why this level:**

- **S2:** 4,925 meaningful implementation LOC measured with tokei 14.0.0. Count covers the reusable Cobra framework package, excluding tests, the documentation site, generated docs, examples, and the separate generator command.
- **D3:** Several moderate concerns interact through a flexible API, options, callbacks, and compatibility behavior.
- **C3:** Tracing a command crosses the tree, inherited flags, validation, hooks, output policy, and optional shell completion boundaries.
- **Placement:** S2/D3/C3 averages to 2.67 and rounds to SDC 3.

**Quality-gate evidence:**

- **Source quality:** Execution stages, validators, output destinations, flag relationships, and completion responses are represented explicitly despite a broad compatibility surface.
- **Architecture:** Command is the central composition object, with focused argument, completion, help, documentation, and flag-group modules around it.
- **Naming and idiom:** Use, Short, Long, Args, RunE, PersistentPreRunE, Find, Traverse, and SilenceUsage mirror the command-line lifecycle.
- **Tests:** Large suites cover command search, aliases, flags, hooks, contexts, errors, templates, suggestions, help, completion, and regression behavior.
- **Documentation:** The README, user guide, generated-reference support, examples, and shell completion docs orient both application authors and contributors.
- **Traceability:** An invocation can be traced through Execute, command discovery, flag parsing, Args validation, lifecycle hooks, RunE, output selection, and command tests.
- **Maintainability:** Compatibility-sensitive behavior is protected by focused tests, stable extension points, explicit options, and localized shell adapters.
- **Educational value:** It shows how an ergonomic framework API translates declarative command definitions into a disciplined execution pipeline.

**Inspection record:** commit `adbc8813901bba65827259daa8e22ff94ec1f30e`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `go.mod`, `command.go`, `args.go`, `command_test.go`, `LICENSE.txt`. GitHub Linguist label: Go. LOC exclusions: *_test.go, site/, doc/, cobra-cli/.

**License:** [Apache-2.0](https://github.com/spf13/cobra/blob/adbc8813901bba65827259daa8e22ff94ec1f30e/LICENSE.txt)

## SDC 4

### [caddyserver/caddy](https://github.com/caddyserver/caddy)

**S3 / D4 / C4 → SDC 4**

An extensible server platform and web server with automatic HTTPS, dynamic configuration, multiple HTTP protocols, and a module system.

**Real-world evidence:** The repository builds the released Caddy server used to host sites and services, and documents production installation, operation, and extension.

**Language evidence:** Configuration loading, module lifecycle, administration, HTTP servers, routing, automatic HTTPS, storage integration, and bundled modules are implemented in Go.

**Why study it:** It exposes a production server's complete lifecycle: typed modules, transactional configuration reloads, administration API, route compilation, HTTP serving, certificate automation, storage, logging, and graceful cleanup.

**What you can learn:**

- Server lifecycle, module registries and provisioning, transactional configuration reloads, HTTP routing and middleware, automatic TLS, storage abstractions, graceful operation, observability, and extensible platform design.

**Prerequisites:**

- Strong Go, interfaces and reflection, concurrency and contexts, net/http, TLS and PKI, JSON configuration, networking, storage, logging, and plugin architecture.

**Start here:** [`caddy.go`](https://github.com/caddyserver/caddy/blob/502691f5182123ef30f463d7f132e7c2fe55e2bf/caddy.go) — Config, Run, Load, and changeConfig reveal how JSON configuration becomes provisioned modules and how a live server changes safely.

**Why this level:**

- **S3:** 47,547 meaningful implementation LOC measured with tokei 14.0.0. Count covers the core server, command, HTTP, TLS, logging, storage, and bundled module implementations while excluding tests, fixtures, documentation, and helper scripts.
- **D4:** Advanced lifecycle, concurrency, extension, and security-sensitive networking concerns recur across the main path.
- **C4:** Many configurable components interact across startup, live reload, request handling, certificate automation, and shutdown.
- **Placement:** S3/D4/C4 averages to 3.67 and rounds to SDC 4.

**Quality-gate evidence:**

- **Source quality:** Lifecycle stages, validation, rollback, concurrency control, configuration hashes, and module ownership are explicit at security-sensitive boundaries.
- **Architecture:** A small core owns configuration and module lifecycle while registered apps and modules provide HTTP, TLS, storage, logging, events, PKI, and protocol features.
- **Naming and idiom:** Config, Module, Provisioner, Validator, App, Load, Cleanup, Route, Handler, Matcher, and AutomationPolicy expose lifecycle and server concepts.
- **Tests:** Unit, integration, adapter, module, routing, TLS, configuration, storage, command, fuzz, and regression suites cover behavior across packages.
- **Documentation:** The README, architecture guide, generated module reference, API documentation, tutorials, conventions, and inline lifecycle contracts support deep study.
- **Traceability:** A configuration change can be followed through the admin API, JSON mutation and hash checks, module loading, provisioning and validation, app start, route execution, and reload tests.
- **Maintainability:** Explicit module interfaces, transactional replacement, cleanup hooks, namespaces, validation, structured logs, and extensive tests isolate extension risk.
- **Educational value:** It is a strong advanced example of making a network server both operationally safe and deeply extensible without hiding lifecycle mechanics.

**Inspection record:** commit `502691f5182123ef30f463d7f132e7c2fe55e2bf`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `go.mod`, `caddy.go`, `modules/caddyhttp/app.go`, `caddy_test.go`, `LICENSE`. GitHub Linguist label: Go. LOC exclusions: *_test.go, caddytest/, integration/, testdata/, docs/.

**License:** [Apache-2.0](https://github.com/caddyserver/caddy/blob/502691f5182123ef30f463d7f132e7c2fe55e2bf/LICENSE)

### [gohugoio/hugo](https://github.com/gohugoio/hugo)

**S4 / D4 / C4 → SDC 4**

A static site generator with content modeling, templates, multilingual sites, asset processing, modules, and fast incremental builds.

**Real-world evidence:** The repository builds the released Hugo command-line application used to generate and serve real websites from content and templates.

**Language evidence:** Site assembly, content processing, templates, resources, asset pipelines, modules, file watching, and build orchestration are implemented primarily in Go.

**Why study it:** It demonstrates a large local application that converts heterogeneous inputs into deterministic sites while supporting templates, content graphs, assets, multilingual variants, modules, caches, and incremental rebuilds.

**What you can learn:**

- Build orchestration, content graphs, template execution, resource pipelines, caching, incremental invalidation, file watching, modules, multilingual variants, command architecture, and performance-oriented application design.

**Prerequisites:**

- Strong Go, interfaces and generics, concurrency, filesystems, templates, parsing, dependency graphs, caching, web assets, command-line applications, and integration testing.

**Start here:** [`hugolib/hugo_sites.go`](https://github.com/gohugoio/hugo/blob/d6e6f9e500eebdeae8e28de830fff2e3bfc7d534/hugolib/hugo_sites.go) — HugoSites and its build orchestration connect configuration, sites, pages, dependencies, rendering, caching, and rebuild state at the product's center.

**Why this level:**

- **S4:** 97,826 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party application, library, template, content, resource, module, command, and support packages while excluding tests, fixtures, examples, documentation, vendored, and generated material.
- **D4:** Performance-sensitive state, graph invalidation, templating, and many content rules recur through the main build path.
- **C4:** A site build crosses many subsystems and variants, though it remains a coherent local build application rather than a distributed platform.
- **Placement:** S4/D4/C4 averages to 4.00, making Hugo an SDC 4 project.

**Quality-gate evidence:**

- **Source quality:** Build state, dependency tracking, cache ownership, rendering phases, and content variants use explicit domain types and guarded transitions.
- **Architecture:** Commands and configuration feed HugoSites, which composes content, page maps, templates, resources, modules, filesystems, publishers, and build-state services.
- **Naming and idiom:** HugoSites, Site, Page, Resource, Template, BuildCfg, BuildState, DependencyManager, and OutputFormat reflect the publishing domain.
- **Tests:** Extensive unit, integration, golden, benchmark, content, template, resource, module, server, filesystem, race, and regression suites cover site generation.
- **Documentation:** The README, contributor guide, package docs, architecture notes, command help, and full public documentation support both use and maintenance.
- **Traceability:** A site build can be followed from command configuration into HugoSites.Build, content assembly, template lookup and execution, resource processing, publication, and build tests.
- **Maintainability:** Domain packages, interfaces, immutable or scoped build data, layered caches, explicit dependencies, and large integration suites contain product breadth.
- **Educational value:** It shows how to organize a large performance-sensitive transformation pipeline whose output must remain predictable across many content variants.

**Inspection record:** commit `d6e6f9e500eebdeae8e28de830fff2e3bfc7d534`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `go.mod`, `hugolib/hugo_sites.go`, `tpl/tplimpl/templates.go`, `hugolib/hugo_sites_build_test.go`, `LICENSE`. GitHub Linguist label: Go. LOC exclusions: *_test.go, testdata/, examples/, docs/, resources/testdata/, vendor/, generated files.

**License:** [Apache-2.0](https://github.com/gohugoio/hugo/blob/d6e6f9e500eebdeae8e28de830fff2e3bfc7d534/LICENSE)

## SDC 5

### [golang/go](https://github.com/golang/go)

**S5 / D5 / C5 → SDC 5**

The Go programming language implementation, including its compiler, runtime, standard library, build tools, assembler, linker, and platform ports.

**Real-world evidence:** The repository is the upstream source used to build official Go toolchains and standard-library releases across supported operating systems and architectures.

**Language evidence:** The compiler, runtime, garbage collector, scheduler, standard library, assembler, linker, debugger support, and developer tools are implemented predominantly in Go with first-party assembly and small C boundaries.

**Why study it:** It joins a self-hosting compiler, concurrent runtime, garbage collector, scheduler, networking and cryptography libraries, build system, linker, assembler, tooling, and extensive portability work in one rigorously documented system.

**What you can learn:**

- Compiler pipelines, parsing and type checking, intermediate representations and SSA optimization, code generation, runtime scheduling, garbage collection, stacks and memory, reflection, interfaces, standard-library design, networking, cryptography, toolchains, bootstrapping, portability, and compatibility.

**Prerequisites:**

- Expert Go, compiler construction, operating systems, concurrency and memory models, garbage collection, assembly and computer architecture, networking, cryptography, filesystems, build systems, performance engineering, and very large codebase navigation.

**Start here:** [`src/cmd/compile/README.md`](https://github.com/golang/go/blob/da7c67f59526a02ef22f80fe91fd2960a6547e59/src/cmd/compile/README.md) — The compiler guide maps parsing, type checking, IR construction, optimization, SSA lowering, code generation, export data, and package boundaries before source-level study begins.

**Why this level:**

- **S5:** 868,648 meaningful implementation LOC measured with tokei 14.0.0. Count covers non-generated first-party Go, C, header, and GNU-style assembly implementation under src/, excluding tests, fixtures, vendored dependencies, documentation, compatibility manifests, miscellaneous support trees, and 661,972 generated implementation lines identified by standard generated-file headers.
- **D5:** Expert compiler, runtime, operating-system, architecture, concurrency, performance, protocol, and security concerns recur throughout the toolchain and standard library.
- **C5:** The repository is a platform-scale language ecosystem whose components must coordinate across compilation, execution, tooling, packages, operating systems, and architectures.
- **Placement:** S5/D5/C5 averages to 5.00 and satisfies the two-dimensions-at-5 guardrail, making Go an SDC 5 project.

**Quality-gate evidence:**

- **Source quality:** Critical compiler and runtime paths document invariants, isolate architecture-specific code, expose phases explicitly, and favor inspectable mechanisms over hidden frameworks.
- **Architecture:** The source tree separates compiler phases, runtime, internal platform support, standard packages, commands, assembler, linker, tracing, profiling, testing, and release machinery around stable package boundaries.
- **Naming and idiom:** Package and symbol names such as syntax, types2, ir, noder, escape, ssa, ssagen, runtime, goroutine, m, p, schedule, and findRunnable encode language and runtime concepts consistently.
- **Tests:** Package tests, compiler error and code-generation tests, runtime stress tests, race tests, fuzzing, benchmarks, platform builders, API checks, and full toolchain tests cover semantics and regressions.
- **Documentation:** Language specifications, package documentation, compiler and runtime guides, design notes, memory-model documentation, contributor guides, proposals, and source comments orient expert readers.
- **Traceability:** Compiling a function can be followed from compiler Main through parsing, types, unified IR, transformations, SSA, architecture lowering, object emission, linking, runtime scheduling, and focused phase tests.
- **Maintainability:** Compatibility policy, explicit internal boundaries, generated-code markers, platform build constraints, exhaustive builders, proposals, benchmarks, and rigorous review protect a self-hosting system.
- **Educational value:** It is an unusually complete expert reference for how a modern language moves from specification through compilation and runtime execution to a portable standard ecosystem.

**Inspection record:** commit `da7c67f59526a02ef22f80fe91fd2960a6547e59`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/cmd/compile/README.md`, `src/cmd/compile/internal/gc/main.go`, `src/cmd/compile/internal/noder/noder.go`, `src/cmd/compile/internal/ssa/compile.go`, `src/runtime/proc.go`, `src/runtime/proc_test.go`, `LICENSE`. GitHub Linguist label: Go. LOC exclusions: *_test.go, test/, testdata/, cmd/vendor/, vendor/, misc/, doc/, api/, files marked as generated.

**License:** [BSD-3-Clause](https://github.com/golang/go/blob/da7c67f59526a02ef22f80fe91fd2960a6547e59/LICENSE)

### [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)

**S5 / D5 / C5 → SDC 5**

A distributed container orchestration platform with declarative APIs, scheduling, controllers, node agents, networking, storage, and extensibility.

**Real-world evidence:** The repository builds the upstream Kubernetes control plane and node components released for operating containerized workloads across clusters.

**Language evidence:** The API server, controllers, scheduler, kubelet, proxy, storage and API machinery, command binaries, and core control-plane behavior are implemented primarily in Go.

**Why study it:** It is an expert reference for declarative distributed control: versioned APIs, watches, reconciliation, admission, scheduling, resource ownership, leader election, node management, storage, networking, and compatibility at platform scale.

**What you can learn:**

- Distributed control planes, declarative reconciliation, API machinery, storage and watches, admission and authorization, scheduling algorithms, controllers, leader election, node agents, networking and storage plugins, versioning, observability, and large-project governance.

**Prerequisites:**

- Expert Go, distributed systems, consensus-backed storage, concurrency, networking, containers, Linux, authentication and authorization, API versioning, scheduling, fault tolerance, observability, and monorepo navigation.

**Start here:** [`cmd/kube-apiserver/app/server.go`](https://github.com/kubernetes/kubernetes/blob/e72c2715ade37738aa5c029e8de5285cbe1c9441/cmd/kube-apiserver/app/server.go) — The API server construction path exposes authentication, admission, storage, versioning, discovery, aggregation, controllers, and lifecycle boundaries shared across the control plane.

**Why this level:**

- **S5:** 927,813 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party command, package, plugin, and staging-module implementation across the platform while excluding tests, fixtures, vendored and copied code, documentation, examples, generated clients, apply configurations, and protobuf output.
- **D5:** Expert distributed-systems, security, scheduling, networking, storage, and compatibility concerns recur across every central learning path.
- **C5:** Kubernetes is a platform-scale system whose useful behaviors span independently deployed components, shared APIs, persistent cluster state, and reconciliation loops.
- **Placement:** S5/D5/C5 averages to 5.00 and satisfies the two-dimensions-at-5 guardrail, making Kubernetes an SDC 5 project.

**Quality-gate evidence:**

- **Source quality:** Core paths make ownership, contexts, queues, retries, feature gates, API conversions, validation, and failure handling explicit despite platform breadth.
- **Architecture:** Versioned APIs and shared machinery connect the API server and storage to controllers, scheduler, kubelet, proxy, plugins, generated clients, and ecosystem extension points.
- **Naming and idiom:** Pod, Node, Scheduler, Informer, Lister, Reconciler, Controller, Queue, Admission, Strategy, and Kubelet expose the control-plane model.
- **Tests:** Unit, integration, conformance, end-to-end, scalability, upgrade, fuzz, API compatibility, scheduler, storage, node, and component suites protect the platform.
- **Documentation:** The README, contributor site, architecture and enhancement proposals, API references, component docs, code-generation guides, and operational documentation provide deep context.
- **Traceability:** Scheduling a pod can be followed from API creation and persisted watch events through informers, the scheduler queue and framework, binding, kubelet observation, runtime execution, status updates, and integration tests.
- **Maintainability:** Versioned APIs, generated boundaries, feature gates, shared libraries, ownership conventions, review processes, compatibility policy, and broad tests manage change at exceptional scale.
- **Educational value:** It is a definitive expert corpus for studying how declarative APIs and reconciliation organize a distributed infrastructure platform.

**Inspection record:** commit `e72c2715ade37738aa5c029e8de5285cbe1c9441`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `go.mod`, `cmd/kube-apiserver/app/server.go`, `pkg/scheduler/scheduler.go`, `test/integration/scheduler/scheduler_test.go`, `LICENSE`. GitHub Linguist label: Go. LOC exclusions: *_test.go, test/, vendor/, third_party/, docs/, examples/, generated files, protobuf outputs, staging/src/k8s.io/client-go/applyconfigurations/.

**License:** [Apache-2.0](https://github.com/kubernetes/kubernetes/blob/e72c2715ade37738aa5c029e8de5285cbe1c9441/LICENSE)

_Generated from `catalog/go.json`; do not edit by hand._

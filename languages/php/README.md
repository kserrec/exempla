# PHP

10 qualified repositories. Scores assume the learner described in [the SDC rubric](../../docs/sdc.md).

[← All languages](../README.md)

## SDC 1

### [doctrine/lexer](https://github.com/doctrine/lexer)

**S1 / D2 / C1 → SDC 1**

A small reusable base for tokenizing strings for top-down recursive-descent parsers and domain-specific languages.

**Real-world evidence:** Doctrine publishes the package as lexer infrastructure used by its annotation, query, and persistence tooling.

**Language evidence:** The generic lexer state, token value object, and extension hooks under src are implemented in strict PHP.

**Why study it:** A tiny abstract class shows how regex tokenization, lookahead, peeking, position management, generic annotations, and extension hooks fit together.

**What you can learn:**

- Lexing, regex token capture, lookahead, token streams, resettable cursors, generics in static analysis, and template-method APIs.

**Prerequisites:**

- PHP classes, regular expressions, arrays, enums, exceptions, and basic parser terminology.

**Start here:** [`src/AbstractLexer.php`](https://github.com/doctrine/lexer/blob/e96fe45e92a54233726014a7cc7340abf29bb14c/src/AbstractLexer.php) — Almost the entire runtime lives here: input scanning, token creation, lookahead, movement, matching, and subclass hooks.

**Why this level:**

- **S1:** 155 meaningful implementation LOC measured with tokei 14.0.0. Count covers the two production PHP files under src, excluding tests, documentation, and package metadata.
- **D2:** Lexer concepts and cursor invariants need modest care, but the full algorithm is short and explicit.
- **C1:** One class scans and navigates tokens while one value object carries results; no external systems are involved.
- **Placement:** A complete and reusable lexer foundation in 155 lines is a strong SDC 1 reading project.

**Quality-gate evidence:**

- **Source quality:** State is private, movement operations are explicit, generics document token types, and subclasses override only recognition and patterns.
- **Architecture:** AbstractLexer owns scanning and navigation while Token represents the immutable output of recognition.
- **Naming and idiom:** lookahead, token, peek, moveNext, isNextToken, getCatchablePatterns, and getType match parser vocabulary.
- **Tests:** Tests exercise scanning, movement, peeking, resets, positions, enum token types, invalid input, and token equality.
- **Documentation:** README and API comments explain extension, token types, cursor behavior, and package compatibility.
- **Traceability:** Input can be followed from setInput through regex splitting and getType into the token array and navigation methods.
- **Maintainability:** A two-file surface and protected template hooks sharply constrain extension and change impact.
- **Educational value:** It teaches a real parser primitive without framework setup or generated machinery.

**Inspection record:** commit `e96fe45e92a54233726014a7cc7340abf29bb14c`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/AbstractLexer.php`, `src/Token.php`, `tests/AbstractLexerTest.php`. GitHub Linguist label: PHP. LOC exclusions: tests, export-only package metadata.

**License:** [MIT](https://github.com/doctrine/lexer/blob/e96fe45e92a54233726014a7cc7340abf29bb14c/LICENSE)

### [webmozarts/assert](https://github.com/webmozarts/assert)

**S2 / D1 / C1 → SDC 1**

A defensive-programming library providing typed assertions for method inputs, outputs, values, collections, files, classes, and objects.

**Real-world evidence:** The package is released through Composer as reusable validation infrastructure across production PHP libraries and applications.

**Language evidence:** The assertion API, generated mixin variants, static-analysis plugin, and exception type under src are PHP.

**Why study it:** Its repetitive but disciplined API shows precise type narrowing, useful error construction, callable messages, compound assertions, and exhaustive edge testing.

**What you can learn:**

- Guard clauses, type refinement, static-analysis annotations, reusable error messages, collection validation, reflection checks, and data-driven testing.

**Prerequisites:**

- PHP types and exceptions, iterables, callables, reflection basics, and Psalm/PHPStan assertion annotations.

**Start here:** [`src/Assert.php`](https://github.com/webmozarts/assert/blob/2ccb7c2e821038c03a3e6e1700c570c158c55f70/src/Assert.php) — The primary class contains the base assertions, shared message helpers, type formatting, and extension seam from which variants are derived.

**Why this level:**

- **S2:** 3,671 meaningful implementation LOC measured with tokei 14.0.0. Count covers production PHP under src, including generated assertion variants used by the shipped package, excluding tests and project metadata.
- **D1:** Each method is a straightforward predicate and exception, with annotations adding precision rather than runtime indirection.
- **C1:** Nearly every behavior is local to one static API and shared formatting helpers.
- **Placement:** S2 length is primarily a broad, repetitive contract; direct code and one-component architecture yield SDC 1.

**Quality-gate evidence:**

- **Source quality:** Assertions return narrowed values, centralize message formatting, accept lazy messages, and consistently raise one package exception.
- **Architecture:** One base assertion class, one generated variant trait, a small static-analysis plugin, and an exception form the package.
- **Naming and idiom:** stringNotEmpty, positiveInteger, isInstanceOf, allString, and nullOrString make contracts readable at call sites.
- **Tests:** Large data-driven tests cover success, failure, custom messages, variant parity, edge values, resources, reflection, and static analysis.
- **Documentation:** The README documents installation, generated variants, extending the class, and every assertion in a searchable reference.
- **Traceability:** A guard call stays in one method before reaching shared message resolution and reportInvalidArgument.
- **Maintainability:** Generated variants remove manual drift while project-code tests enforce synchronization and public API constraints.
- **Educational value:** It shows how rigor and developer ergonomics matter even in deliberately simple validation code.

**Inspection record:** commit `2ccb7c2e821038c03a3e6e1700c570c158c55f70`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/Assert.php`, `src/Mixin.php`, `tests/AssertTest.php`. GitHub Linguist label: PHP. LOC exclusions: tests.

**License:** [MIT](https://github.com/webmozarts/assert/blob/2ccb7c2e821038c03a3e6e1700c570c158c55f70/LICENSE)

## SDC 2

### [nikic/FastRoute](https://github.com/nikic/FastRoute)

**S1 / D3 / C2 → SDC 2**

A fast HTTP request router that compiles static and variable routes into compact dispatch data and matched parameters.

**Real-world evidence:** FastRoute is a published production routing library used by PHP web frameworks and applications.

**Language evidence:** Route parsing, regex data generation, dispatch strategies, caching, and URI generation under src are PHP.

**Why study it:** It makes route compilation tangible: readable route syntax becomes chunked regular expressions, marker strategies, dispatch results, and reverse URI generation.

**What you can learn:**

- Route parsing, regular-expression compilation, dispatch tables, capture-group strategies, conflict detection, caching, and immutable results.

**Prerequisites:**

- Regular expressions, HTTP routing, PHP interfaces and arrays, exceptions, and basic parsing.

**Start here:** [`src/RouteParser/Std.php`](https://github.com/nikic/FastRoute/blob/1c961398bef1ff6ecd8b273bef651d7afe90312b/src/RouteParser/Std.php) — The parser turns optional segments, placeholders, and custom patterns into route alternatives consumed by data generators.

**Why this level:**

- **S1:** 1,243 meaningful implementation LOC measured with tokei 14.0.0. Calibration count covers production PHP under src, excluding tests, benchmarks, documentation, and packaging files.
- **D3:** Correct placeholder parsing and several optimized dispatch encodings require sustained regex and representation reasoning.
- **C2:** The pipeline has a few clear interfaces and strategy variants but remains a small in-process library.
- **Placement:** Very small size is balanced by nontrivial regex compilation, producing SDC 2.

**Quality-gate evidence:**

- **Source quality:** Parsing, bad-route validation, data generation, and match decoding are explicit and separated by small interfaces.
- **Architecture:** Configuration connects route collectors, parsers, data generators, dispatchers, caches, and URI generators through stable roles.
- **Naming and idiom:** RouteParser, DataGenerator, Dispatcher, Matched, MethodNotAllowed, and GenerateUri express the full routing lifecycle.
- **Tests:** Focused suites cover conflicts, optional segments, custom regex, dispatcher strategies, cache behavior, URI generation, and invalid routes.
- **Documentation:** The README explains route syntax, dispatch outcomes, caching, shortcuts, and strategy choices with executable examples.
- **Traceability:** A route can be followed from registration through parsing and data generation to dispatcher matching and extracted variables.
- **Maintainability:** Strategy interfaces isolate performance experiments while common results and validation preserve the public contract.
- **Educational value:** It shows why a production router is more than matching a path against a list of strings.

**Inspection record:** commit `1c961398bef1ff6ecd8b273bef651d7afe90312b`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/RouteParser/Std.php`, `src/Dispatcher/GroupCountBased.php`, `test/Dispatcher/GroupCountBasedTest.php`. GitHub Linguist label: PHP. LOC exclusions: tests, benchmarks.

**License:** [BSD-3-Clause](https://github.com/nikic/FastRoute/blob/1c961398bef1ff6ecd8b273bef651d7afe90312b/LICENSE)

### [ramsey/uuid](https://github.com/ramsey/uuid)

**S2 / D3 / C2 → SDC 2**

A UUID library supporting standard versions, binary and string codecs, generation strategies, validation, conversion, and multiple math backends.

**Real-world evidence:** ramsey/uuid is a widely consumed Composer package used to generate and interpret production identifiers.

**Language evidence:** UUID parsing, generation, fields, codecs, math, conversion, validation, and RFC 4122 variants under src are PHP.

**Why study it:** It converts a binary standard into typed value objects and swappable providers while keeping compatibility and platform limitations explicit.

**What you can learn:**

- Binary layouts, RFC variants and versions, codecs, factories, time and random providers, immutable values, validation, and fallback strategies.

**Prerequisites:**

- UUID standards, bit and byte representations, PHP interfaces and traits, immutable values, time, randomness, and big-number concepts.

**Start here:** [`src/Uuid.php`](https://github.com/ramsey/uuid/blob/da5b521600a707d2dd097598464bd3090de850f5/src/Uuid.php) — The central value object and factory methods connect textual parsing, bytes, fields, comparison, generation, and version-specific subclasses.

**Why this level:**

- **S2:** 4,283 meaningful implementation LOC measured with tokei 14.0.0. Count covers production PHP under src, excluding tests, benchmarks, static-analysis fixtures, docs, and package metadata.
- **D3:** Bit layouts, endian conversions, timestamp epochs, name hashing, and variant rules require domain knowledge beyond ordinary value objects.
- **C2:** Several interchangeable helpers support one identifier abstraction in one process with clear interfaces.
- **Placement:** Moderate size plus contained standards and binary reasoning make ramsey/uuid SDC 2.

**Quality-gate evidence:**

- **Source quality:** Version rules, invalid representations, provider failures, and conversion boundaries are typed and reported through focused exceptions.
- **Architecture:** Value types depend on factories, builders, fields, codecs, generators, providers, converters, math, and validators through interfaces.
- **Naming and idiom:** UuidV4, Fields, Codec, TimeProvider, RandomGenerator, Validator, and Converter match the standard's concepts.
- **Tests:** Extensive suites cover versions, variants, bytes, strings, timestamps, providers, math backends, invalid inputs, and expected behavior.
- **Documentation:** README, docs, upgrade notes, API references, and examples explain generation, conversion, databases, and customization.
- **Traceability:** A versioned UUID can be followed from a factory through providers and fields into a concrete immutable value and encoded output.
- **Maintainability:** Interfaces isolate environment-dependent randomness, clocks, number math, and codecs from the value model.
- **Educational value:** It is a strong example of translating a binary interoperability standard into an approachable PHP API.

**Inspection record:** commit `da5b521600a707d2dd097598464bd3090de850f5`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/Uuid.php`, `src/Rfc4122/UuidV7.php`, `tests/UuidTest.php`. GitHub Linguist label: PHP. LOC exclusions: tests, benchmarks, static-analysis fixtures.

**License:** [MIT](https://github.com/ramsey/uuid/blob/da5b521600a707d2dd097598464bd3090de850f5/LICENSE)

## SDC 3

### [guzzle/guzzle](https://github.com/guzzle/guzzle)

**S3 / D3 / C3 → SDC 3**

An extensible HTTP client that composes PSR messages, middleware, asynchronous promises, cURL or stream handlers, redirects, retries, and cookies.

**Real-world evidence:** Guzzle is published as production HTTP infrastructure and underpins networking in a large part of the PHP ecosystem.

**Language evidence:** Client configuration, middleware, handlers, authentication, redirects, cookies, retries, proxying, and transfer state under src are PHP.

**Why study it:** It shows how immutable messages and handler stacks turn a rich request configuration into sync or async network transfers across multiple transports.

**What you can learn:**

- Middleware stacks, promises, PSR interfaces, transport handlers, request normalization, redirects, retries, cookies, proxying, TLS, and resource cleanup.

**Prerequisites:**

- HTTP, PSR-7 and PSR-18 concepts, closures, promises, streams, cURL, exceptions, and TLS basics.

**Start here:** [`src/Client.php`](https://github.com/guzzle/guzzle/blob/7b7b04a0f5a548bfe9ced4b56f5661deee229ac3/src/Client.php) — The client merges configuration, builds requests, transfers through the handler stack, and adapts promise results to sync and async APIs.

**Why this level:**

- **S3:** 11,664 meaningful implementation LOC measured with tokei 14.0.0. Count covers production PHP under src, excluding tests, local server fixtures, docs, packaging, and generated artifacts.
- **D3:** Handler composition, async results, redirects, proxy selection, body framing, timeouts, and cleanup introduce recurring technical depth.
- **C3:** A request crosses configuration, messages, middleware, handlers, promises, transport state, and response or exception adaptation.
- **Placement:** Moderate source size and a layered cross-transport request lifecycle place Guzzle at SDC 3.

**Quality-gate evidence:**

- **Source quality:** Client and handler code validates options, isolates protocol concerns, protects terminal resources, and preserves exception context.
- **Architecture:** A Client drives immutable messages through a HandlerStack of middleware into cURL, multi-cURL, stream, or mock handlers.
- **Naming and idiom:** HandlerStack, Middleware, RequestOptions, CurlFactory, TransferStats, and CookieJar provide consistent HTTP vocabulary.
- **Tests:** Unit and integration suites cover clients, handlers, middleware, redirects, retries, proxies, auth, cookies, streams, failures, and cleanup.
- **Documentation:** Quickstarts, request options, handlers, middleware, testing, FAQ, and migration guides cover the full API.
- **Traceability:** A request can be followed from Client.requestAsync through middleware and a handler into transfer completion and response mapping.
- **Maintainability:** PSR boundaries and handler interfaces isolate message, promise, and transport packages from client orchestration.
- **Educational value:** It demonstrates how production networking hides transport variation without hiding the lifecycle from source readers.

**Inspection record:** commit `7b7b04a0f5a548bfe9ced4b56f5661deee229ac3`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/Client.php`, `src/Handler/CurlHandler.php`, `tests/ClientTest.php`. GitHub Linguist label: PHP. LOC exclusions: tests, server fixtures, documentation.

**License:** [MIT](https://github.com/guzzle/guzzle/blob/7b7b04a0f5a548bfe9ced4b56f5661deee229ac3/LICENSE)

### [Seldaek/monolog](https://github.com/Seldaek/monolog)

**S2 / D3 / C3 → SDC 3**

A logging library that routes structured records through processors, formatters, filters, buffers, groups, files, sockets, databases, and web services.

**Real-world evidence:** Monolog is a production PSR-3 logging implementation used by major PHP applications and frameworks.

**Language evidence:** Logger channels, immutable records, handlers, formatters, processors, error integration, and reset contracts under src/Monolog are PHP.

**Why study it:** A simple record pipeline grows into an extensible integration library while retaining clear handler, processor, formatter, and bubbling contracts.

**What you can learn:**

- Pipeline composition, immutable log records, handler stacks, filtering and bubbling, buffering, formatting, integration adapters, fibers, and error handling.

**Prerequisites:**

- Interfaces and traits, exceptions, callables, streams, PSR-3, serialization, and common logging destinations.

**Start here:** [`src/Monolog/Logger.php`](https://github.com/Seldaek/monolog/blob/2a50ae6f387a6da963bf2e2662803a01517a58ca/src/Monolog/Logger.php) — Logger constructs records, applies channel processors, prevents logging loops, and walks the handler stack according to bubbling rules.

**Why this level:**

- **S2:** 7,887 meaningful implementation LOC measured with tokei 14.0.0. Count covers production PHP under src/Monolog, excluding tests, docs, package metadata, and build files.
- **D3:** Most handlers are direct adapters, while buffering, grouping, retries, streams, signals, and recursive logging create several advanced paths.
- **C3:** Records move through a compact core into a broad but consistently shaped family of transport integrations.
- **Placement:** S2 size is raised by extension breadth and nontrivial pipeline behavior, making Monolog SDC 3.

**Quality-gate evidence:**

- **Source quality:** The core record path is explicit, immutable data limits mutation, and handlers share processing and formatting templates.
- **Architecture:** Logger coordinates records, processors, formatters, and a stack of handlers whose adapters share small contracts.
- **Naming and idiom:** LogRecord, Level, Handler, Processor, Formatter, bubbling, buffering, and reset are consistent across integrations.
- **Tests:** Handler-specific and core suites cover routing, levels, processors, formatting, buffering, failures, resources, fibers, and integrations.
- **Documentation:** README, usage guide, handler catalog, extension notes, recipes, and changelog make the ecosystem navigable.
- **Traceability:** A log call can be followed through record creation and processors into each handler's format, write, and bubbling decision.
- **Maintainability:** Abstract handlers and narrow interfaces let destinations vary without duplicating core filtering and processing behavior.
- **Educational value:** It shows how a tiny conceptual pipeline can support many production boundaries without losing a common model.

**Inspection record:** commit `2a50ae6f387a6da963bf2e2662803a01517a58ca`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/Monolog/Logger.php`, `src/Monolog/Handler/AbstractProcessingHandler.php`, `tests/Monolog/LoggerTest.php`. GitHub Linguist label: PHP. LOC exclusions: tests, documentation.

**License:** [MIT](https://github.com/Seldaek/monolog/blob/2a50ae6f387a6da963bf2e2662803a01517a58ca/LICENSE)

## SDC 4

### [composer/composer](https://github.com/composer/composer)

**S3 / D4 / C4 → SDC 4**

PHP's dependency manager, resolving version constraints and then downloading, installing, locking, autoloading, auditing, and running package plugins.

**Real-world evidence:** Composer is the production package manager and dependency resolver used throughout the modern PHP ecosystem.

**Language evidence:** Dependency solving, repositories, downloads, installation, autoloading, plugins, command handling, and package models under src/Composer are PHP.

**Why study it:** It joins a SAT-based dependency solver to practical repository protocols, lockfiles, secure downloads, filesystem transactions, autoload generation, and plugins.

**What you can learn:**

- SAT solving, semantic-version constraints, repositories and caches, lock transactions, download/install pipelines, autoloading, plugins, CLI orchestration, and security policy.

**Prerequisites:**

- Advanced PHP, graph and SAT concepts, package management, filesystems, HTTP, processes, serialization, and CLI design.

**Start here:** [`src/Composer/DependencyResolver/Solver.php`](https://github.com/composer/composer/blob/2616959b478c47ef3968dde41ec98bd7cba6d050/src/Composer/DependencyResolver/Solver.php) — The solver turns package constraints into rules, propagates decisions, analyzes conflicts, backtracks, and returns an install transaction.

**Why this level:**

- **S3:** 46,701 meaningful implementation LOC measured with tokei 14.0.0. Count covers production PHP under src, excluding tests, docs, JSON schemas, generated phar output, and packaging support.
- **D4:** The solver, repository policies, archive/download security, VCS behavior, and rollback paths repeatedly require advanced algorithmic and systems reasoning.
- **C4:** One command crosses configuration, repositories, pools, the solver, operations, downloads, installation, lockfiles, plugins, and autoload generation.
- **Placement:** Advanced algorithmic code and a broad side-effecting package pipeline raise the S3-sized repository to SDC 4.

**Quality-gate evidence:**

- **Source quality:** Solver invariants, transaction objects, policy boundaries, platform filters, and error explanations keep difficult behavior inspectable.
- **Architecture:** Console and factories assemble package, repository, dependency resolver, downloader, installer, plugin, autoload, cache, and audit layers.
- **Naming and idiom:** Pool, RuleSet, Decisions, Solver, LockTransaction, Repository, Downloader, Installer, and Locker encode the package workflow.
- **Tests:** Extensive unit and integration tests cover resolution, conflicts, repositories, downloads, plugins, lockfiles, autoloading, security, and regressions.
- **Documentation:** README, command and schema docs, articles, troubleshooting, version guides, and plugin APIs cover users and extenders.
- **Traceability:** A requirement can be followed from repository loading through rules, SAT decisions, operations, downloads, installation, and the lockfile.
- **Maintainability:** Interfaces and operation objects separate algorithms from external systems while compatibility and security policies are explicit.
- **Educational value:** It is a rare accessible implementation of both a real dependency solver and the operational machinery around it.

**Inspection record:** commit `2616959b478c47ef3968dde41ec98bd7cba6d050`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/Composer/Composer.php`, `src/Composer/DependencyResolver/Solver.php`, `tests/Composer/Test/DependencyResolver/SolverTest.php`. GitHub Linguist label: PHP. LOC exclusions: tests, documentation, schemas, compiled phar output.

**License:** [MIT](https://github.com/composer/composer/blob/2616959b478c47ef3968dde41ec98bd7cba6d050/LICENSE)

### [phpstan/phpstan-src](https://github.com/phpstan/phpstan-src)

**S4 / D4 / C4 → SDC 4**

The development source of PHPStan, a static analyzer that infers PHP types and reports errors through an extensible rule system.

**Real-world evidence:** PHPStan is released as production developer tooling and is integrated into large PHP codebases and CI systems.

**Language evidence:** Parser integration, reflection, type lattice, scope analysis, rules, extensions, dependency export, and diagnostics under src are PHP.

**Why study it:** It exposes a rich type system, flow-sensitive scopes, reflection models, AST traversal, extension points, caching, and diagnostic policy in PHP itself.

**What you can learn:**

- Abstract interpretation, type lattices, flow-sensitive narrowing, AST analysis, reflection, generics, rule extensions, dependency graphs, caching, and diagnostics.

**Prerequisites:**

- Advanced PHP, compiler and AST concepts, type theory, generics, control-flow analysis, reflection, and static-analysis architecture.

**Start here:** [`src/Analyser/Analyser.php`](https://github.com/phpstan/phpstan-src/blob/4f80a48ebac54bee75500661a1664ae52df56ace/src/Analyser/Analyser.php) — The analyzer coordinates file processing, node scopes, rule evaluation, ignored errors, internal failures, dependencies, and result aggregation.

**Why this level:**

- **S4:** 174,051 meaningful implementation LOC measured with tokei 14.0.0. Count covers production PHP under src, excluding tests, benchmark and end-to-end fixtures, docs, generated outputs, and packaging.
- **D4:** Understanding the main path requires repeated reasoning about type lattices, scopes, templates, reflection variants, and AST semantics.
- **C4:** Analysis crosses parsing, node scopes, types, reflection, rules, extensions, dependency export, caching, parallel workers, and output.
- **Placement:** S4 breadth plus advanced compiler-like mechanisms and a highly extensible architecture make PHPStan SDC 4.

**Quality-gate evidence:**

- **Source quality:** Interfaces and immutable result objects make analysis stages explicit, while precise type declarations document complex data flow.
- **Architecture:** Parser, analyzer, types, reflection, rules, dependency resolution, cache, command, parallel, and extension packages have distinct contracts.
- **Naming and idiom:** Scope, Type, TrinaryLogic, Rule, ReflectionProvider, NodeScopeResolver, and AnalyserResult provide a rigorous shared model.
- **Tests:** A vast fixture-driven suite covers types, rules, language versions, extensions, reflection, generics, performance, and regressions.
- **Documentation:** User guides, rule and extension references, type-system docs, error identifiers, upgrade notes, and contributor docs are extensive.
- **Traceability:** A source node can be followed through parsed nodes and scope resolution into matching rules, errors, dependencies, and cached results.
- **Maintainability:** Extension interfaces, error identifiers, compatibility tests, and isolated type/reflection abstractions govern a difficult domain.
- **Educational value:** It is an expert but readable example of implementing a modern static-analysis system in the language it analyzes.

**Inspection record:** commit `4f80a48ebac54bee75500661a1664ae52df56ace`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/Analyser/Analyser.php`, `src/Rules/Rule.php`, `tests/PHPStan/Analyser/AnalyserTest.php`. GitHub Linguist label: PHP. LOC exclusions: tests, benchmarks, end-to-end fixtures.

**License:** [MIT](https://github.com/phpstan/phpstan-src/blob/4f80a48ebac54bee75500661a1664ae52df56ace/LICENSE)

## SDC 5

### [nextcloud/server](https://github.com/nextcloud/server)

**S5 / D4 / C5 → SDC 5**

A self-hosted collaboration server providing file storage and sync, sharing, users, apps, federation, security, APIs, background work, and web administration.

**Real-world evidence:** Nextcloud Server is continuously released and deployed as a production data and collaboration platform.

**Language evidence:** The server container, files platform, sharing, users, security, federation, APIs, apps, background jobs, and web runtime are primarily PHP with first-party client code.

**Why study it:** It exposes the architecture required to sustain a security-sensitive multi-user web platform across storage, apps, databases, federation, background jobs, APIs, and upgrades.

**What you can learn:**

- Service containers, virtual filesystems, sharing and permissions, app lifecycles, database abstraction, federation, background jobs, security controls, migrations, and web APIs.

**Prerequisites:**

- Expert PHP and web security, databases, storage systems, distributed services, JavaScript clients, background processing, and large-codebase navigation.

**Start here:** [`lib/private/Server.php`](https://github.com/nextcloud/server/blob/529c4e4a6b236e6367e926d9a375ae9600335d73/lib/private/Server.php) — The central container registers and wires storage, users, apps, security, HTTP, federation, background jobs, and platform services.

**Why this level:**

- **S5:** 592,334 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party PHP, JavaScript, TypeScript, Vue, styles, and shell, excluding tests, 3rdparty and vendor code, docs, generated bundles, and build output.
- **D4:** Correctness repeatedly depends on permissions, locking, encryption, caches, databases, remote federation, migrations, and async jobs.
- **C5:** User actions cross a large container, virtual storage, databases, apps, APIs, security, sharing, federation, jobs, and client assets.
- **Placement:** S5 and C5 make Nextcloud Server an unambiguous SDC 5 platform.

**Quality-gate evidence:**

- **Source quality:** Core services use interfaces, typed constructors, explicit security checks, migrations, and failure-aware storage abstractions.
- **Architecture:** A central container connects public OCP contracts to private services, apps, storage, databases, HTTP APIs, jobs, and security layers.
- **Naming and idiom:** Server, AppManager, RootFolder, ShareManager, UserSession, BackgroundJob, Federation, and OCP contracts define the platform.
- **Tests:** Unit, integration, database, app, API, browser, upgrade, storage, security, and acceptance suites cover the system.
- **Documentation:** Administrator, developer, app, API, architecture, security, upgrade, and contributor documentation is extensive.
- **Traceability:** A file action can be traced from an HTTP or OCS route through controllers and services into virtual storage, permissions, events, and persistence.
- **Maintainability:** Public OCP interfaces, app boundaries, migrations, code ownership, review tooling, and layered test suites govern the large surface.
- **Educational value:** It is a rich advanced case study in sustaining a self-hosted application platform where user data and trust are central.

**Inspection record:** commit `529c4e4a6b236e6367e926d9a375ae9600335d73`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `lib/base.php`, `lib/private/Server.php`, `tests/lib/ServerTest.php`. GitHub Linguist label: PHP. LOC exclusions: tests, third-party libraries, documentation, generated and built assets.

**License:** [AGPL-3.0-or-later](https://github.com/nextcloud/server/blob/529c4e4a6b236e6367e926d9a375ae9600335d73/COPYING)

### [symfony/symfony](https://github.com/symfony/symfony)

**S5 / D4 / C5 → SDC 5**

A component framework spanning dependency injection, HTTP kernels, console tools, events, routing, security, messaging, forms, validation, and integrations.

**Real-world evidence:** Symfony is actively released production infrastructure used directly and as a foundation for major PHP applications and frameworks.

**Language evidence:** The framework's dependency injection, HTTP, console, event, routing, security, messaging, persistence bridges, and component implementations are PHP.

**Why study it:** It shows how independently useful components become a coherent application platform through stable contracts, events, compiled containers, bridges, and compatibility policy.

**What you can learn:**

- Dependency-injection compilation, HTTP request lifecycles, event dispatch, routing, console architecture, messaging, security, extension contracts, and long-term compatibility.

**Prerequisites:**

- Expert PHP, reflection, attributes, dependency injection, HTTP, event systems, security, concurrency, databases, and framework architecture.

**Start here:** [`src/Symfony/Component/HttpKernel/HttpKernel.php`](https://github.com/symfony/symfony/blob/c69a0a62bc6cff4c25ae9447e16f52960dba71af/src/Symfony/Component/HttpKernel/HttpKernel.php) — The kernel's compact handle path connects requests, controller resolution, arguments, events, responses, exceptions, and request-stack cleanup.

**Why this level:**

- **S5:** 1,250,347 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party PHP and small supporting source under src, excluding Tests directories, docs, fixtures, generated output, and build artifacts.
- **D4:** Advanced framework mechanisms and many specialist domains recur, though individual components generally favor explicit, idiomatic PHP.
- **C5:** Full behavior spans containers, kernels, events, routing, security, messaging, persistence bridges, configuration, console, and deployment concerns.
- **Placement:** S5 and C5 place the full Symfony monorepo at SDC 5 under the rubric guardrail.

**Quality-gate evidence:**

- **Source quality:** Core components make lifecycle stages, contracts, event transitions, cleanup, and error conversion explicit despite broad features.
- **Architecture:** Independent Components and Contracts connect through Bridges and Bundles into a full-stack framework without erasing standalone boundaries.
- **Naming and idiom:** ContainerBuilder, Request, Response, HttpKernel, EventDispatcher, RouteCollection, Messenger, and Constraint form stable language.
- **Tests:** Component-level and integration suites cover kernels, containers, events, security, messaging, forms, bridges, compatibility, and regressions.
- **Documentation:** Books, component docs, API references, recipes, best practices, upgrade guides, and contributor documentation are comprehensive.
- **Traceability:** A request can be followed through HttpKernel events and controller resolution while service construction is traced separately through ContainerBuilder.
- **Maintainability:** Small contracts, component boundaries, deprecations, backward-compatibility promises, and exhaustive tests control a huge ecosystem.
- **Educational value:** Advanced readers can compare focused component design with the integration demands of a mature application platform.

**Inspection record:** commit `c69a0a62bc6cff4c25ae9447e16f52960dba71af`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/Symfony/Component/HttpKernel/HttpKernel.php`, `src/Symfony/Component/DependencyInjection/ContainerBuilder.php`, `src/Symfony/Component/HttpKernel/Tests/HttpKernelTest.php`. GitHub Linguist label: PHP. LOC exclusions: tests, documentation, fixtures, generated files.

**License:** [MIT](https://github.com/symfony/symfony/blob/c69a0a62bc6cff4c25ae9447e16f52960dba71af/LICENSE)

_Generated from `catalog/php.json`; do not edit by hand._

# R

10 qualified repositories. Scores assume the learner described in [the SDC rubric](../../docs/sdc.md).

[← All languages](../README.md)

## SDC 1

### [r-lib/pkgconfig](https://github.com/r-lib/pkgconfig)

**S1 / D2 / C1 → SDC 1**

A tiny package for configuration values that are private to each calling R package instead of globally shared.

**Real-world evidence:** The repository publishes the pkgconfig CRAN package for libraries that need caller-specific configuration without global-option collisions.

**Language evidence:** Per-package configuration storage, stack inspection, lookup precedence, validation, and the public API are implemented in the root R package.

**Why study it:** Forty-eight lines turn R environments and call-stack metadata into a complete, useful API with explicit fallback and precedence behavior.

**What you can learn:**

- R environments, call-stack frames, namespaces, package identity, named variadic arguments, fallback values, and small API design.

**Prerequisites:**

- R functions and lists, environments, packages and namespaces, call stacks, and testthat basics.

**Start here:** [`R/getset.R`](https://github.com/r-lib/pkgconfig/blob/687e3154aa407642649beb00334940c71d6f22d9/R/getset.R) — The complete implementation shows storage, caller discovery, precedence, validation, and mutation in one short file.

**Why this level:**

- **S1:** 48 meaningful implementation LOC measured with tokei 14.0.0. Count covers all production R files and excludes tests, generated reference documentation, and README source.
- **D2:** The mechanism uses reflective R facilities, but the full control flow is short and direct.
- **C1:** One package and one environment implement the behavior without I/O or external services.
- **Placement:** S1/D2/C1 averages to 1.33, making pkgconfig an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** The implementation keeps lookup precedence, caller detection, validation, and mutation separate despite its tiny size.
- **Architecture:** One private environment stores keys whose values are maps from calling package to configured value.
- **Naming and idiom:** get_config, set_config, set_config_in, get_from_session, who, and fallback make the policy visible.
- **Tests:** Tests create temporary packages to verify caller isolation, nesting precedence, global fallback, custom APIs, validation, and errors.
- **Documentation:** The README explains the global-state problem, a realistic package scenario, nested calls, installation, and usage.
- **Traceability:** A get_config call can be followed through stored values, sys.frames, namespace identification, reverse precedence, and custom-package tests.
- **Maintainability:** The small representation and focused contract make all precedence behavior auditable in one sitting.
- **Educational value:** It demonstrates how a language's reflective runtime can solve a real package-isolation problem with almost no machinery.

**Inspection record:** commit `687e3154aa407642649beb00334940c71d6f22d9`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `DESCRIPTION`, `R/getset.R`, `tests/testthat/test-api.R`, `LICENSE`. GitHub Linguist label: R. LOC exclusions: tests/, man/, README.Rmd.

**License:** [MIT](https://github.com/r-lib/pkgconfig/blob/687e3154aa407642649beb00334940c71d6f22d9/LICENSE)

### [r-lib/rematch2](https://github.com/r-lib/rematch2)

**S1 / D2 / C1 → SDC 1**

A small wrapper that turns base R regular-expression matches and capture groups into tidy tabular results.

**Real-world evidence:** The repository publishes the rematch2 CRAN package for programs that need structured first-match and all-match data.

**Language evidence:** Regex result conversion, capture-group indexing, tidy table construction, match-record classes, and the public API are implemented in R.

**Why study it:** It is a compact adapter study: awkward attribute-rich base results become stable tabular objects while preserving strings, positions, groups, missing matches, and vectorized inputs.

**What you can learn:**

- Regular-expression match metadata, capture groups, vectorization, substring indexing, list columns, S3 classes and methods, tidy data frames, and adapter APIs.

**Prerequisites:**

- R vectors, lists and attributes, regular expressions and capture groups, S3 methods, data frames or tibbles, and unit tests.

**Start here:** [`R/exec.R`](https://github.com/r-lib/rematch2/blob/be7c3a05c060dce37277098967d42ffc695a6943/R/exec.R) — re_exec converts regexpr attributes into match records, capture columns, positions, missing values, and the final tidy result.

**Why this level:**

- **S1:** 250 meaningful implementation LOC measured with tokei 14.0.0. Count covers every production R file and excludes tests, snapshots, generated reference documentation, and README source.
- **D2:** Indexing and unmatched-group cases need care, but each transformation is local and well tested.
- **C1:** The library wraps base regex functions without I/O, shared state, or architectural layers.
- **Placement:** S1/D2/C1 averages to 1.33, making rematch2 an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** The code normalizes match, start, end, groups, names, and missing values explicitly rather than hiding conversions.
- **Architecture:** First-match and all-match paths share record constructors, indexing methods, bind helpers, and a minimal tibble boundary.
- **Naming and idiom:** re_match, re_exec, re_match_all, re_exec_all, match, start, end, and capture names preserve regex vocabulary.
- **Tests:** Tests cover named and unnamed groups, no matches, empty input, vectorization, all matches, indexing, binding, Unicode, and malformed requests.
- **Documentation:** The README compares the predecessor API and develops realistic first-match, all-match, and position examples.
- **Traceability:** A capture can be followed from regexpr attributes through substring extraction and record construction to list-column access tests.
- **Maintainability:** Small dedicated helpers and exhaustive shape tests protect an adapter whose main risk is indexing detail.
- **Educational value:** It teaches how to make a low-level return format easier to use without discarding information or rewriting the underlying engine.

**Inspection record:** commit `be7c3a05c060dce37277098967d42ffc695a6943`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `DESCRIPTION`, `R/exec.R`, `R/exec-all.R`, `tests/testthat/test-exec.R`, `LICENSE`. GitHub Linguist label: R. LOC exclusions: tests/, man/, README.Rmd.

**License:** [MIT](https://github.com/r-lib/rematch2/blob/be7c3a05c060dce37277098967d42ffc695a6943/LICENSE)

## SDC 2

### [r-lib/withr](https://github.com/r-lib/withr)

**S1 / D3 / C2 → SDC 2**

A library for running code with temporary changes to global process state and reliably restoring that state afterward.

**Real-world evidence:** The repository publishes the withr CRAN package used by packages, tests, scripts, and tools that must scope side effects safely.

**Language evidence:** Temporary state setters, dynamic function construction, deferred cleanup, resource helpers, and integrations are implemented in R.

**Why study it:** It turns a broad maintenance hazard into a reusable pattern across options, environment variables, paths, locales, files, connections, databases, graphics devices, random state, and namespaces.

**What you can learn:**

- Resource acquisition and cleanup, on.exit and deferred handlers, dynamic function construction, non-standard evaluation, process-global state, files and connections, nested scopes, and exception-safe APIs.

**Prerequisites:**

- R environments and evaluation, functions and formals, on.exit, conditions, files and connections, process state, and package namespaces.

**Start here:** [`R/with_.R`](https://github.com/r-lib/withr/blob/d82e4bc2d69a34f044ad205210e26207bfb8f3e0/R/with_.R) — The with_ constructor generates the common set-change-evaluate-reset protocol used by the package's concrete helpers.

**Why this level:**

- **S1:** 1,298 meaningful implementation LOC measured with tokei 14.0.0. Count covers all production R helpers while excluding tests, snapshots, vignettes, generated reference material, website sources, and reverse-dependency data.
- **D3:** The central pattern is simple, but evaluation frames, early exits, nested scopes, and diverse resources create subtle behavior.
- **C2:** Many helpers share one lifecycle abstraction and remain confined to the current R process.
- **Placement:** S1/D3/C2 averages to 2.00, making withr an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** Constructors establish cleanup before risky mutation when possible, and each resource helper makes capture and restoration explicit.
- **Architecture:** with_ and local_ generate the lifecycle wrappers; defer manages frame-bound cleanup; small modules adapt individual kinds of state.
- **Naming and idiom:** with_, local_, defer, set, get, reset, action, and .local_envir state lifetime and ownership clearly.
- **Tests:** Tests exercise success, errors, early exits, nesting, setters that fail, cleanup order, files, connections, paths, locales, random state, graphics, databases, and integration boundaries.
- **Documentation:** The README inventories supported state, contrasts with and local lifetimes, and demonstrates both built-in and custom wrappers.
- **Traceability:** with_options can be followed from a resource-specific setter through with_, on.exit registration, code evaluation, restoration, and failure-path tests.
- **Maintainability:** Central lifecycle constructors prevent dozens of state helpers from reimplementing cleanup semantics inconsistently.
- **Educational value:** It is a practical study in making side effects safe through scope, ownership, and guaranteed restoration.

**Inspection record:** commit `d82e4bc2d69a34f044ad205210e26207bfb8f3e0`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `DESCRIPTION`, `R/with_.R`, `R/local_.R`, `R/defer.R`, `tests/testthat/test-with.R`, `tests/testthat/test-local_.R`, `LICENSE`. GitHub Linguist label: R. LOC exclusions: tests/, vignettes/, man/, pkgdown/, revdep/, man-roxygen/.

**License:** [MIT](https://github.com/r-lib/withr/blob/d82e4bc2d69a34f044ad205210e26207bfb8f3e0/LICENSE)

### [tidyverse/glue](https://github.com/tidyverse/glue)

**S1 / D3 / C2 → SDC 2**

A dependency-light string interpolation library that evaluates expressions inside customizable delimiters.

**Real-world evidence:** The repository publishes the glue CRAN package for applications and packages that construct text, messages, SQL, and data-aware strings.

**Language evidence:** Expression capture and evaluation, transformers, quoting, SQL support, vector recycling, and the interpolation parser are implemented in R and C.

**Why study it:** A familiar API reveals language evaluation, a hand-written delimiter parser, escaping, vectorization, custom transformers, SQL quoting, and safe restricted interpolation.

**What you can learn:**

- Non-standard evaluation, expression parsing, lexical state machines in C, escaping and delimiters, vector recycling, custom transformers, SQL quoting, S3 output, and safe API variants.

**Prerequisites:**

- R expressions and environments, vectors and recycling, S3 methods, basic C extension interfaces, parsers, and SQL quoting concepts.

**Start here:** [`R/glue.R`](https://github.com/tidyverse/glue/blob/da9c73f7a3de6a27f3103cb5bb2355820a4c3a6a/R/glue.R) — The public glue function assembles arguments, environments, transformers, delimiters, recycling, and the C-backed parsing path.

**Why this level:**

- **S1:** 984 meaningful implementation LOC measured with tokei 14.0.0. Count covers production R and C under R/ and src/, excluding tests, snapshots, vignettes, generated documentation, website sources, and reverse-dependency material.
- **D3:** Parsing and evaluation semantics cross R and C and contain enough edge cases to require substantial prerequisite knowledge.
- **C2:** Several cohesive adapters share one interpolation engine within a single package.
- **Placement:** S1/D3/C2 averages to 2.00, making glue an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** Evaluation, parsing, escaping, recycling, transformation, and output classes are separated with explicit boundary checks.
- **Architecture:** R functions prepare contexts and variants while a small C state machine scans literal and expression segments.
- **Naming and idiom:** glue, glue_data, transformer, open, close, trim, literal, comment, and recycle0 expose interpolation policy.
- **Tests:** Tests cover delimiters, escaping, multiline trimming, comments, evaluation scope, recycling, NA and NULL, custom transformers, SQL, safe mode, and regressions.
- **Documentation:** The README, vignettes, function reference, maintenance notes, and examples explain both everyday use and extension mechanisms.
- **Traceability:** An interpolation can be followed from glue through argument preparation into the C scanner, expression evaluation, vector assembly, and focused tests.
- **Maintainability:** One parser, explicit callbacks, small variant modules, a minimal dependency surface, and broad edge-case tests contain semantic risk.
- **Educational value:** It shows how a tiny user-facing convenience rests on careful language, parsing, and data-shape contracts.

**Inspection record:** commit `da9c73f7a3de6a27f3103cb5bb2355820a4c3a6a`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `DESCRIPTION`, `R/glue.R`, `src/glue.c`, `tests/testthat/test-glue.R`, `LICENSE`. GitHub Linguist label: R. LOC exclusions: tests/, vignettes/, man/, pkgdown/, revdep/.

**License:** [MIT](https://github.com/tidyverse/glue/blob/da9c73f7a3de6a27f3103cb5bb2355820a4c3a6a/LICENSE)

## SDC 3

### [r-lib/testthat](https://github.com/r-lib/testthat)

**S2 / D4 / C3 → SDC 3**

R's xUnit-style testing framework, with expressive expectations, reporters, snapshots, package integration, and parallel execution.

**Real-world evidence:** The repository publishes the testthat CRAN package used to run and report automated tests for R packages and applications.

**Language evidence:** Test discovery and execution, expectations, conditions and restarts, reporters, snapshots, mocking, parallel workers, and package integration are implemented primarily in R.

**Why study it:** It is a self-referential production framework whose source exposes test isolation, structured conditions, restarts, source references, reporters, snapshots, process workers, and compatibility editions.

**What you can learn:**

- Test-runner architecture, condition systems and restarts, isolated evaluation environments, source references, reporter objects, snapshots, parallel processes, mocking, state-leak detection, and backward-compatible framework evolution.

**Prerequisites:**

- Strong R, environments and evaluation, conditions and restarts, R6, files and processes, serialization, source references, package loading, and testing concepts.

**Start here:** [`R/test-files.R`](https://github.com/r-lib/testthat/blob/9b6f12b9f50c297b4b5f485f728a2a19305770eb/R/test-files.R) — test_dir and test_files connect discovery, environment setup, reporters, serial or parallel execution, teardown, result collection, and failure policy.

**Why this level:**

- **S2:** 9,814 meaningful implementation LOC measured with tokei 14.0.0. Count covers production R plus small compiled support under R/ and src/, excluding the framework's own tests and fixtures, installed examples, vignettes, generated documentation, website, and reverse-dependency data.
- **D4:** Advanced evaluation and condition behavior recurs throughout the execution path, with additional concurrency and compatibility constraints.
- **C3:** Several framework subsystems interact, but they compose around one test-runner domain and a bounded process topology.
- **Placement:** S2/D4/C3 averages to 3.00, making testthat an SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** Test lifecycle, result conditions, restart boundaries, reporter callbacks, cleanup, and process modes are explicit and protected against recursive failures.
- **Architecture:** Discovery feeds serial or parallel runners; isolated test environments signal expectation conditions into composable reporters and snapshot managers.
- **Naming and idiom:** test_dir, test_file, test_that, expectation, reporter, snapshot, teardown, skip, and edition reflect testing vocabulary directly.
- **Tests:** The framework tests its expectations, runners, every reporter, snapshots, mocks, source locations, parallel lifecycle, package loading, state leaks, output, errors, warnings, and regressions.
- **Documentation:** The README, reference site, vignettes, package-development book links, release notes, and inline lifecycle documentation provide multiple learning paths.
- **Traceability:** A test file can be followed from discovery through environment setup, test_that evaluation, condition signaling, reporter collection, snapshot handling, teardown, and runner tests.
- **Maintainability:** Structured conditions, reporter interfaces, lifecycle helpers, compatibility editions, self-tests, snapshots, and process isolation contain a wide behavioral surface.
- **Educational value:** It shows what a mature testing framework must do beyond comparing values: isolate state, preserve source context, survive failures, and communicate results.

**Inspection record:** commit `9b6f12b9f50c297b4b5f485f728a2a19305770eb`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `DESCRIPTION`, `R/test-files.R`, `R/test-that.R`, `R/expectation.R`, `R/reporter.R`, `tests/testthat/test-test-files.R`, `LICENSE`. GitHub Linguist label: R. LOC exclusions: tests/, inst/, vignettes/, man/, pkgdown/, revdep/.

**License:** [MIT](https://github.com/r-lib/testthat/blob/9b6f12b9f50c297b4b5f485f728a2a19305770eb/LICENSE)

### [tidyverse/dplyr](https://github.com/tidyverse/dplyr)

**S3 / D4 / C3 → SDC 3**

A grammar of data manipulation built around consistent verbs for selecting, filtering, mutating, summarizing, arranging, and joining tabular data.

**Real-world evidence:** The repository publishes the dplyr CRAN package used by data workflows and downstream packages to transform in-memory and backend tabular data.

**Language evidence:** Data-manipulation verbs, grouping, data masks, tidy evaluation, joins, selection, reconstruction, and performance-critical grouped operations are implemented in R and C++.

**Why study it:** It connects a declarative user grammar to generic dispatch, tidy evaluation, grouped data masks, vector-size rules, type restoration, joins, and native loops while preserving data-frame subclasses.

**What you can learn:**

- Data-frame algebra, generic verbs, tidy evaluation and data masks, grouping, vector recycling and type stability, joins, selection, native R extension code, error context, and extensible backend design.

**Prerequisites:**

- Strong R, S3 and R6, quosures and tidy evaluation, environments and active bindings, data frames, vector type systems, C++ extension interfaces, relational operations, and testing.

**Start here:** [`R/mutate.R`](https://github.com/tidyverse/dplyr/blob/d5e94e7fa8fd4a5f79c1a707d1842216bb4c691f/R/mutate.R) — mutate.data.frame and mutate_cols connect the public verb to grouping, data-mask evaluation, native chunk execution, recycling, reconstruction, relocation, and column-retention policy.

**Why this level:**

- **S3:** 12,482 meaningful implementation LOC measured with tokei 14.0.0. Count covers production R, C++, and headers under R/ and src/, excluding tests, fixtures, data, vignettes, generated documentation, website sources, and reverse-dependency material.
- **D4:** Advanced evaluation, type, grouping, and native-interface concerns recur across core verbs and error paths.
- **C3:** Many cohesive subsystems interact, but the repository implements one data-manipulation layer rather than a whole distributed engine.
- **Placement:** S3/D4/C3 averages to 3.33, making dplyr an SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** Public verbs separate policy from data-mask evaluation and native loops, with explicit size, type, grouping, and reconstruction checks.
- **Architecture:** S3 verbs and helpers build grouping metadata and data masks, delegate tight grouped work to C++, then reconstruct the appropriate tabular type.
- **Naming and idiom:** mutate, summarise, filter, arrange, join, group_by, DataMask, chunks, rows, and reconstruct preserve the data-manipulation model.
- **Tests:** Large suites cover every verb, grouping, rowwise data, joins, selection, data masks, evaluation, recycling, type errors, subclasses, locale behavior, and regressions.
- **Documentation:** The README, reference site, vignettes, programming guides, release notes, and detailed function contracts explain both user grammar and extension points.
- **Traceability:** A grouped mutate can be followed from generic dispatch through grouping computation, DataMask active bindings, per-group native evaluation, column modification, reconstruction, and mutate tests.
- **Maintainability:** Generic boundaries, centralized masks and grouping, vector contracts, native error objects, extensive regression tests, and stable verb semantics manage evolution.
- **Educational value:** It is a strong study of translating a small declarative vocabulary into type-stable, extensible, performance-conscious execution.

**Inspection record:** commit `d5e94e7fa8fd4a5f79c1a707d1842216bb4c691f`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `DESCRIPTION`, `R/mutate.R`, `R/data-mask.R`, `src/mutate.cpp`, `tests/testthat/test-mutate.R`, `LICENSE`. GitHub Linguist label: R. LOC exclusions: tests/, data/, data-raw/, vignettes/, man/, pkgdown/, revdep/.

**License:** [MIT](https://github.com/tidyverse/dplyr/blob/d5e94e7fa8fd4a5f79c1a707d1842216bb4c691f/LICENSE)

## SDC 4

### [rstudio/shiny](https://github.com/rstudio/shiny)

**S3 / D4 / C4 → SDC 4**

A reactive web application framework that connects R server functions to a browser client over persistent sessions.

**Real-world evidence:** The repository publishes the Shiny CRAN package and browser runtime used to build, serve, test, and deploy interactive R web applications.

**Language evidence:** The server runtime, reactive graph, sessions, application loading, rendering, caching, resources, inputs, and testing API are implemented in R, with a first-party TypeScript browser runtime.

**Why study it:** It spans both sides of a framework: reactive invalidation and flushing, application and session lifecycle, HTTP and WebSocket transport, browser bindings, message queues, file uploads, caching, modules, bookmarking, and testing.

**What you can learn:**

- Reactive dependency graphs, invalidation and scheduling, session lifecycle, HTTP and WebSocket protocols, asynchronous queues, browser input and output bindings, application loading and hot reload, caching, modules, observability, and cross-language framework design.

**Prerequisites:**

- Strong R and TypeScript, environments and R6, reactive systems, concurrency and promises, HTTP and WebSockets, browser events and DOM APIs, serialization, caching, files, and integration testing.

**Start here:** [`R/reactives.R`](https://github.com/rstudio/shiny/blob/81844600fc15f1952838546faa6699d0506ce7f9/R/reactives.R) — ReactiveVal, Observable, Observer, contexts, invalidation, dependency registration, priorities, and flush behavior define the framework's central execution model.

**Why this level:**

- **S3:** 23,979 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party R under R/ and TypeScript source under srcts/src/, excluding tests and fixture applications, generated declarations and browser bundles, static resources, generated documentation, and reverse-dependency material.
- **D4:** Advanced evaluation, graph, asynchronous, protocol, and lifecycle concerns recur across central server and browser paths.
- **C4:** A user interaction crosses persistent client/server state and many framework services, though deployment infrastructure remains outside this repository.
- **Placement:** S3/D4/C4 averages to 3.67 and rounds to SDC 4.

**Quality-gate evidence:**

- **Source quality:** Reactive ownership, invalidation state, session cleanup, message ordering, binding registration, resource paths, and application lifetimes are represented explicitly.
- **Architecture:** An R reactive and session runtime communicates through a defined message protocol with TypeScript input/output bindings and a stateful ShinyApp browser client.
- **Naming and idiom:** ReactiveVal, Observable, Observer, Context, Session, ShinyApp, InputBinding, OutputBinding, invalidate, flush, bind, and reconnect expose the model.
- **Tests:** Unit, browser, application-fixture, module, reactive, session, server, snapshot, accessibility, TypeScript, protocol, encoding, and regression suites cover both runtimes.
- **Documentation:** The README, reference site, articles, function docs, deployment guides, TypeScript notes, package examples, and testing helpers support study.
- **Traceability:** Changing an input can be followed from a browser binding and queued WebSocket message through session input handling, reactive invalidation and flush, output rendering, return messages, and client updates.
- **Maintainability:** Explicit lifecycle objects, scoped domains, message handlers, modular bindings, cleanup hooks, typed client source, observability hooks, and broad tests contain cross-runtime risk.
- **Educational value:** It is an advanced reference for how reactive programming becomes a full client/server product without obscuring the dependency graph.

**Inspection record:** commit `81844600fc15f1952838546faa6699d0506ce7f9`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `DESCRIPTION`, `R/reactives.R`, `R/shinyapp.R`, `srcts/src/shiny/shinyapp.ts`, `tests/testthat/test-reactives.R`, `LICENSE`. GitHub Linguist label: R. LOC exclusions: tests/, smoketests/, srcts/src/**/__tests__/, srcts/types/, inst/www/ compiled assets, res/, man/, man-roxygen/, revdep/, generated JavaScript.

**License:** [MIT](https://github.com/rstudio/shiny/blob/81844600fc15f1952838546faa6699d0506ce7f9/LICENSE)

### [tidyverse/ggplot2](https://github.com/tidyverse/ggplot2)

**S3 / D4 / C4 → SDC 4**

A declarative graphics system that implements a layered grammar of data, aesthetics, scales, statistics, geometry, coordinates, faceting, guides, and themes.

**Real-world evidence:** The repository publishes the ggplot2 CRAN package used to create static visualizations and as a platform for a large extension ecosystem.

**Language evidence:** The grammar, plot object, build pipeline, layers, scales, coordinates, facets, guides, themes, geoms, stats, positions, and extension system are implemented in R.

**Why study it:** It turns a deep domain model into a staged compiler-like pipeline, custom object protocols, reusable coordinate and statistical transformations, layout, guide training, and grid graphics output.

**What you can learn:**

- Grammar-of-graphics architecture, declarative object composition, staged build pipelines, prototype and S7 object systems, scale training and mapping, statistics and geometry, coordinate transforms, faceting, guides, themes, extension protocols, and backward compatibility.

**Prerequisites:**

- Strong R, object systems and method dispatch, non-standard evaluation, data frames, statistics, coordinate systems, grid graphics, layout, functional composition, and visual-testing concepts.

**Start here:** [`R/plot-build.R`](https://github.com/tidyverse/ggplot2/blob/6870419aa6e106c3580c45c81d5b688cb31758bd/R/plot-build.R) — build_ggplot presents the complete staged path from layers and raw data through aesthetics, scales, statistics, positions, layout, guides, themes, and render-ready objects.

**Why this level:**

- **S3:** 24,718 meaningful implementation LOC measured with tokei 14.0.0. Count covers production R under R/, excluding tests and visual snapshots, datasets, assets, vignettes, generated documentation, website sources, and reverse-dependency material.
- **D4:** Deep visualization theory, extensible object behavior, and transformations recur across the main plot-building path.
- **C4:** Rendering one plot crosses many configurable components whose ordering and contracts are central to correctness.
- **Placement:** S3/D4/C4 averages to 3.67 and rounds to SDC 4.

**Quality-gate evidence:**

- **Source quality:** The build pipeline names each transformation phase, isolates extension protocols, and adds contextual errors at layer boundaries.
- **Architecture:** A declarative plot composes layers and shared settings, then a staged builder trains and maps data before grid-based rendering.
- **Naming and idiom:** Layer, Geom, Stat, Scale, Coord, Facet, Guide, Theme, Layout, train, map, setup, compute, and draw encode the grammar.
- **Tests:** Extensive behavioral, snapshot, visual, extension, scale, stat, geom, coordinate, facet, guide, theme, layout, accessibility, and regression tests protect output.
- **Documentation:** The README, reference site, internals book, extension guide, vignettes, governance, release notes, and examples explain theory and implementation.
- **Traceability:** A point plot can be followed from object composition through build_ggplot's layer data, aesthetics, scale training, statistics, positions, layout, guides, geometry, and build tests.
- **Maintainability:** Stable grammar objects, extension contracts, staged transformations, deprecation policy, governance, visual snapshots, and broad tests manage a mature ecosystem.
- **Educational value:** It is a rare production example of a declarative domain language becoming an explicit, extensible compilation pipeline.

**Inspection record:** commit `6870419aa6e106c3580c45c81d5b688cb31758bd`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `DESCRIPTION`, `R/plot-build.R`, `R/ggproto.R`, `tests/testthat/test-plot-build.R`, `LICENSE`. GitHub Linguist label: R. LOC exclusions: tests/, data/, data-raw/, inst/, icons/, vignettes/, man/, pkgdown/, revdep/.

**License:** [MIT](https://github.com/tidyverse/ggplot2/blob/6870419aa6e106c3580c45c81d5b688cb31758bd/LICENSE)

## SDC 5

### [nimble-dev/nimble](https://github.com/nimble-dev/nimble)

**S4 / D5 / C5 → SDC 5**

A programmable hierarchical-modeling system that compiles BUGS-style models and model-generic algorithms from R into customized C++.

**Real-world evidence:** The repository publishes the NIMBLE CRAN package used to build and fit hierarchical models with MCMC, particle filtering, Laplace approximation, and custom statistical algorithms.

**Language evidence:** The BUGS-compatible modeling language, graph construction, algorithm DSL, MCMC configuration, compiler and C++ generation pipeline, and R interfaces are implemented in substantial first-party R alongside the generated-code runtime in C++.

**Why study it:** It combines two embedded languages, probabilistic graph analysis, model specialization, C++ code generation and compilation, automatic differentiation, R/native interfaces, configurable samplers, and several inference systems.

**What you can learn:**

- Probabilistic programming languages, graphical models, language parsing and semantic analysis, dependency graphs, partial evaluation, source generation, native compilation, automatic differentiation, MCMC and particle methods, numerical inference, R/C++ bridges, and scientific-software architecture.

**Prerequisites:**

- Expert R and C++, Bayesian statistics and graphical models, MCMC and numerical inference, compilers and code generation, graph algorithms, automatic differentiation, native extension APIs, linear algebra, and large scientific systems.

**Start here:** [`packages/nimble/R/BUGS_model.R`](https://github.com/nimble-dev/nimble/blob/0181166733112cdaaf4edf7d7b0817a8f03cbdac/packages/nimble/R/BUGS_model.R) — The model classes expose how BUGS code becomes declarations, graph nodes, dependencies, executable model objects, data state, and the input to compilation.

**Why this level:**

- **S4:** 66,315 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party R under packages/nimble/R plus the reusable C++ runtime under packages/nimble/inst/CppCode and packages/nimble/inst/include/nimble, excluding tests, model corpora, examples, benchmarks, manuals, data, generated reference material, and vendored numeric libraries.
- **D5:** Expert compiler, graph, statistical, numerical, automatic-differentiation, and cross-language concerns recur throughout the main path.
- **C5:** NIMBLE is a specialized probabilistic-programming platform whose useful workflows cross two languages, graph state, generated code, a native runtime, and multiple inference engines.
- **Placement:** S4/D5/C5 has two dimensions at 5 and therefore requires SDC 5.

**Quality-gate evidence:**

- **Source quality:** Model declarations, graph identities, dependencies, compiler intermediates, generated types, native ownership, sampler configuration, and diagnostic failures are represented explicitly.
- **Architecture:** BUGS models and nimbleFunctions become typed graph and expression intermediates, generated C++, compiled runtime objects, and configurable inference algorithms behind R interfaces.
- **Naming and idiom:** nimbleCode, nimbleModel, nimbleFunction, modelBaseClass, graphNode, compileNimble, configureMCMC, sampler, node, dependency, and calculate expose the platform model.
- **Tests:** Large unit, compiler, model-corpus, MCMC, automatic-differentiation, graph, distribution, indexing, native-interface, optimization, benchmark, and regression suites compare interpreted and compiled behavior.
- **Documentation:** The README, full user manual, developer documentation, examples, workshops, package reference, publications, contributor guide, and inline compiler notes support expert study.
- **Traceability:** A BUGS model can be followed through nimbleCode capture, declaration analysis, graph construction, model class creation, compiler intermediates and generated C++, native graph execution, configured MCMC, and interpreted-versus-compiled tests.
- **Maintainability:** Named compiler stages, explicit intermediates, separated runtime headers, compatible interpreted mode, generated-code boundaries, gold comparisons, model corpora, and extensive tests manage a very difficult system.
- **Educational value:** It is a rare open source example of a probabilistic programming system whose modeling language, algorithm language, compiler, runtime, and inference machinery are all inspectable.

**Inspection record:** commit `0181166733112cdaaf4edf7d7b0817a8f03cbdac`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `packages/nimble/DESCRIPTION`, `packages/nimble/R/BUGS_model.R`, `packages/nimble/R/nimbleFunction_compile.R`, `packages/nimble/R/genCpp_generateCpp.R`, `packages/nimble/inst/CppCode/nimbleGraph.cpp`, `packages/nimble/tests/testthat/test-models.R`, `LICENSE`. GitHub Linguist label: C++. LOC exclusions: packages/nimble/tests/, packages/AD-full-tests/, packages/Laplace-examples/, packages/nimble/inst/classic-bugs/, UserManual/, packages/nimble/man/, vendored Eigen and CppAD headers, examples, benchmarks, data, and generated documentation.

**License:** [BSD-3-Clause OR GPL-2.0-or-later](https://github.com/nimble-dev/nimble/blob/0181166733112cdaaf4edf7d7b0817a8f03cbdac/LICENSE)

### [wch/r-source](https://github.com/wch/r-source)

**S5 / D5 / C5 → SDC 5**

The R language implementation, runtime, garbage collector, standard and recommended packages, graphics, statistics, compiler, build system, and platform ports.

**Real-world evidence:** This read-only mirror tracks the upstream R source tree used to build the R language and standard software distribution.

**Language evidence:** The repository is the R language implementation itself: its evaluator and runtime are written in C, its base and standard packages substantially in R, and numerical kernels in C and Fortran.

**Why study it:** It exposes a mature statistical language from evaluator and promises through environments, object systems, bytecode, memory management, numerical libraries, graphics, packages, foreign interfaces, platform ports, and compatibility tests.

**What you can learn:**

- Interpreter evaluation, lexical environments and promises, object dispatch, bytecode compilation, garbage collection and object representation, numerical and statistical computing, graphics engines, package loading, native interfaces, internationalization, platform portability, and language compatibility.

**Prerequisites:**

- Expert R, C, Fortran, interpreters and virtual machines, garbage collection, language semantics and object systems, compilers, numerical analysis and statistics, operating systems, graphics, native ABIs, build systems, and very large codebase navigation.

**Start here:** [`doc/manual/R-ints.texi`](https://github.com/wch/r-source/blob/780021752eb83a71e2198019acf069ba8741103b/doc/manual/R-ints.texi) — R Internals explains core representations, evaluation, memory, environments, serialization, graphics, and native interfaces before the reader enters runtime source.

**Why this level:**

- **S5:** 432,178 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party C, R, Fortran, headers, lexer and grammar sources, Tcl, Objective-C, and assembly under src/, excluding tests, documentation, data and translations, bundled or recommended third-party source, generated compiler output, and build machinery.
- **D5:** Expert language-runtime, memory, numerical, platform, and compatibility concerns recur across the implementation and standard libraries.
- **C5:** R is a platform-scale language ecosystem whose runtime, libraries, tools, interfaces, and ports must evolve as one compatible system.
- **Placement:** S5/D5/C5 averages to 5.00 and satisfies the two-dimensions-at-5 guardrail, making R an SDC 5 project.

**Quality-gate evidence:**

- **Source quality:** Core runtime code documents protection, contexts, evaluation, dispatch, allocation, collection, and platform invariants at the points where violations would corrupt semantics.
- **Architecture:** A C evaluator and runtime support R-level base and standard packages, a bytecode compiler, numerical and graphics subsystems, package loading, native interfaces, tools, and platform ports.
- **Naming and idiom:** SEXP, eval, applyClosure, promise, environment, context, protect, gc, dispatch, package, primitive, and bytecode reflect the implementation model.
- **Tests:** Regression, evaluation, arithmetic, numerical, methods, encoding, graphics, package, embedding, native-interface, platform, example, and no-crash suites protect language behavior.
- **Documentation:** R Internals, the Language Definition, Writing R Extensions, Installation and Administration, data import, package help, source comments, and contributor history provide extensive guidance.
- **Traceability:** Evaluating a closure can be followed from eval through promise and argument handling, applyClosure and contexts, allocation and garbage-collection protection, standard functions, and evaluation regression tests.
- **Maintainability:** Stable internal APIs, explicit protection discipline, platform separation, generated-source boundaries, exhaustive regression tests, manuals, and conservative compatibility practices manage a decades-old runtime.
- **Educational value:** It is the definitive expert source for understanding how R's visible statistical language semantics are realized by its evaluator, memory system, and standard distribution.

**Inspection record:** commit `780021752eb83a71e2198019acf069ba8741103b`, reviewed 2026-08-28 by Codex. Files sampled: `README`, `src/main/eval.c`, `src/main/memory.c`, `doc/manual/R-ints.texi`, `tests/eval-etc.R`, `COPYING`. GitHub Linguist label: R. LOC exclusions: tests/, doc/, share/, po/ translation catalogs, src/library/Recommended/ external package archives, src/extra/ bundled third-party libraries, generated src/library/compiler/R/cmp.R, build and configuration files.

**License:** [GPL-2.0-or-later](https://github.com/wch/r-source/blob/780021752eb83a71e2198019acf069ba8741103b/COPYING)

_Generated from `catalog/r.json`; do not edit by hand._

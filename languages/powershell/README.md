# PowerShell

7 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

[← All languages](../README.md)

## Level 1

No qualified learning path has been published at this level. Standards are not lowered to fill a slot.

## Level 2

### [deadlydog/Invoke-MsBuild](https://github.com/deadlydog/Invoke-MsBuild)

**Language 2 / Behavior 2 / Design 1 / Constraints 3 → Level 2**

A small PowerShell module that locates an installed MSBuild, runs a project or solution with structured options, manages logs, and reports a typed build result.

**Why study it:** The selected discovery function shows how a PowerShell adapter searches versioned installation layouts, orders candidates, chooses an architecture, falls back to legacy locations, and makes absence explicit.

**Prerequisites:**

- Basic familiarity with PowerShell functions, scriptblocks, pipelines, arrays and hashtables, .NET objects, errors, and Pester tests.

**Concepts this path develops:**

- PowerShell functions over filesystem and .NET path APIs.
- Ordered candidate probing.
- Visual Studio generations use different directory layouts.

**What you can learn:**

- Use `Get-LatestMsBuildPath` in `Invoke-MsBuild.psm1` to study advanced functions, filesystem candidate discovery, version sorting, architecture selection, legacy fallback, explicit missing-tool behavior, and mocked installation-layout tests.

**Learning path:**

- **Goal:** Understand how a PowerShell adapter discovers a versioned external build executable across operating-system installation conventions and validates its fallback choices.
- **Start here:** [`src/Invoke-MsBuild/Invoke-MsBuild.psm1`](https://github.com/deadlydog/Invoke-MsBuild/blob/7fee8e141296ea6c337e433537d7061f52e24157/src/Invoke-MsBuild/Invoke-MsBuild.psm1) — Get-LatestMsBuildPath is the exact entry to the scored discovery behavior inside the module and connects directly to fake-installation tests for its ordering and fallback choices.
- **Then read:**
  - [`src/Tests/Invoke-MsBuild.Tests.ps1`](https://github.com/deadlydog/Invoke-MsBuild/blob/7fee8e141296ea6c337e433537d7061f52e24157/src/Tests/Invoke-MsBuild.Tests.ps1)
  - [`ReadMe.md`](https://github.com/deadlydog/Invoke-MsBuild/blob/7fee8e141296ea6c337e433537d7061f52e24157/ReadMe.md)
  - [`License.md`](https://github.com/deadlydog/Invoke-MsBuild/blob/7fee8e141296ea6c337e433537d7061f52e24157/License.md)
- **Trace:** Begin at Get-LatestMsBuildPath, follow conventional Visual Studio and MSBuild directory candidates through version sorting, architecture choice, legacy fallback, and missing-path behavior, then close those decisions in the fake-installation tests. The broader invocation, process, logging, cleanup, and result lifecycle is intentionally not claimed because the listed suite does not directly close it.

**Why this level:**

- **Language technique 2:** The path uses common professional PowerShell and .NET interoperation without recurring advanced language machinery.
- **Behavioral reasoning 2:** The discovery decision tree is synchronous, bounded, and locally inspectable.
- **Design span 1:** A single cohesive module contains the complete scored discovery behavior.
- **Constraint burden 3:** Several platform and backward-compatibility contracts constrain an otherwise small adapter.
- **Placement:** The four scores 2/2/1/3 sum to 8; their arithmetic mean is 2.00 and rounds half-up to Level 2. The published result is Level 2.

**License:** MIT ([evidence 1](https://github.com/deadlydog/Invoke-MsBuild/blob/7fee8e141296ea6c337e433537d7061f52e24157/License.md))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The repository publishes the Invoke-MsBuild PowerShell module and documents use from build scripts, continuous-integration jobs, and ordinary PowerShell sessions.

**Language evidence:** MSBuild discovery, argument construction, process execution, log lifecycle, result classification, and Pester tests are implemented in PowerShell under src/Invoke-MsBuild.

**Coding relevance:**

The short tool vocabulary is subordinate to transferable lessons in filesystem probing, version ordering, architecture selection, fallbacks, parameter validation, and isolating operating-system dependencies behind focused tests.

Required domain context:

- MSBuild discovery means locating the executable or developer command prompt across conventional Visual Studio installation generations and architectures.

**Eight-part quality gate:**

- **Source quality:** The discovery path makes candidate roots, version ordering, architecture choice, legacy fallback, and missing-path outcomes visible in ordinary PowerShell control flow.
- **Architecture:** The selected path is bounded to one executable-discovery responsibility in the production module and one Pester suite that supplies fake installation layouts.
- **Naming and idiom:** Get-LatestMsBuildPath, VisualStudioVersion, MsBuildArchitecture, and the candidate path variables communicate the selected policy directly.
- **Tests:** The selected Pester cases construct representative installation layouts and close version preference, architecture selection, legacy fallback, explicit paths, and not-found behavior.
- **Documentation:** The README explains supported MSBuild and Visual Studio choices and the public parameters that lead into executable discovery.
- **Traceability:** A requested or inferred tool version can be followed through candidate-directory construction, version sorting, architecture selection, fallback, and the matching mocked filesystem assertion.
- **Maintainability:** Keeping discovery in a named function and testing filesystem conventions through mocks lets installation-policy changes remain separate from the unscored build-process lifecycle.
- **Educational value:** This path teaches how to make environment-dependent executable discovery explicit, deterministic, and testable without claiming the broader process and logging behavior.

**Inspection record:** commit `7fee8e141296ea6c337e433537d7061f52e24157`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/Invoke-MsBuild/Invoke-MsBuild.psm1`, `src/Tests/Invoke-MsBuild.Tests.ps1`, `ReadMe.md`, `License.md`. GitHub Linguist label: PowerShell.

</details>

### [lipkau/PSIni](https://github.com/lipkau/PSIni)

**Language 2 / Behavior 2 / Design 1 / Constraints 3 → Level 2**

A compact PowerShell module that reads and writes INI files as ordered hashtables while preserving sections, comments, repeated keys, and encoding choices.

**Why study it:** Import-Ini is a compact production parser whose path, literal-path, and string inputs converge on explicit section, comment, key-value, duplicate-key, and malformed-line policies.

**Prerequisites:**

- Basic familiarity with PowerShell functions, scriptblocks, pipelines, arrays and hashtables, .NET objects, errors, and Pester tests.

**Concepts this path develops:**

- Advanced-function parameter sets and pipeline input.
- Current-section parser state.
- Input order and case behavior must remain stable.

**What you can learn:**

- Use `PSIni/Public/Import-Ini.ps1` to study advanced functions, parameter sets, pipeline input, encoding selection, ordered case-insensitive dictionaries, line-oriented regular-expression parsing, duplicate-key policy, comment preservation, and direct Pester contracts.

**Learning path:**

- **Goal:** Understand how a compact PowerShell advanced function parses line-oriented configuration text into an ordered object model without losing its practical edge cases.
- **Start here:** [`PSIni/Public/Import-Ini.ps1`](https://github.com/lipkau/PSIni/blob/6895c42fdba461a1a171fe70e11d67c037bac1d0/PSIni/Public/Import-Ini.ps1) — Import-Ini contains the entire selected read path, from input and encoding choice through line classification to the ordered object returned by the focused unit suite.
- **Then read:**
  - [`Tests/Import-Ini.Unit.Tests.ps1`](https://github.com/lipkau/PSIni/blob/6895c42fdba461a1a171fe70e11d67c037bac1d0/Tests/Import-Ini.Unit.Tests.ps1)
  - [`README.md`](https://github.com/lipkau/PSIni/blob/6895c42fdba461a1a171fe70e11d67c037bac1d0/README.md)
  - [`LICENSE`](https://github.com/lipkau/PSIni/blob/6895c42fdba461a1a171fe70e11d67c037bac1d0/LICENSE)
- **Trace:** Start with Import-Ini's path, literal-path, and string parameter sets, follow each line through section, comment, and key-value matching into ordered case-insensitive dictionaries, observe how repeated values and the no-section sentinel are represented, then close malformed and compatibility behavior in the direct import suite. Export-Ini is intentionally outside this import-only scored trace.

**Why this level:**

- **Language technique 2:** Common professional PowerShell idioms materially shape the parser, but no advanced runtime or metaprogramming machinery recurs.
- **Behavioral reasoning 2:** Behavior is a synchronous line transformation with only local parser state and explicit branches.
- **Design span 1:** The complete scored behavior is contained in one cohesive implementation unit and its tests.
- **Constraint burden 3:** Several parser and compatibility guarantees recur even though the control flow is compact.
- **Placement:** The four scores 2/2/1/3 sum to 8; their arithmetic mean is 2.00 and rounds half-up to Level 2. The published result is Level 2.

**License:** MIT ([evidence 1](https://github.com/lipkau/PSIni/blob/6895c42fdba461a1a171fe70e11d67c037bac1d0/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** PSIni is maintained as a versioned PowerShell Gallery module, and its README documents command-line and pipeline use for application and system configuration files.

**Language evidence:** INI parsing, ordered-hashtable construction, duplicate-key handling, comment preservation, serialization, encoding support, and the test suite are implemented in PowerShell under PSIni and Tests.

**Coding relevance:**

That small vocabulary is subordinate to transferable PowerShell lessons in advanced-function input, regular-expression classification, ordered object construction, localized parser state, duplicate handling, and encoding-aware file boundaries.

Required domain context:

- An INI document is line-oriented configuration text containing sections, comments, keys, values, and repeated-key policy.

**Eight-part quality gate:**

- **Source quality:** Import-Ini keeps section, comment, key-value, duplicate, malformed-line, and encoding branches explicit while deliberately preserving input order.
- **Architecture:** The selected path stays within one public advanced function and its direct Import-Ini unit suite, with path, literal-path, and string parameter sets converging on one parser.
- **Naming and idiom:** Import-Ini, AllowDuplicateKeys, SkipComments, NoSection, and the ordered section tables make the parser's representation and edge-case policy discoverable.
- **Tests:** The Import-Ini unit suite covers file and literal content, comments, blank lines, global keys, sections, duplicate keys, malformed input, parameter forms, and compatibility cases used by this trace.
- **Documentation:** The README explains Import-Ini inputs, returned object shape, parsing switches, encodings, and examples needed to interpret the selected path.
- **Traceability:** An input line can be followed through Import-Ini's section, comment, key-value, and malformed branches into a specific ordered-table assertion in the direct suite.
- **Maintainability:** The narrow public read surface, explicit behavior flags, standard PowerShell representation, and nearby regression cases keep parser changes bounded.
- **Educational value:** This path is an approachable example of a useful line-oriented parser with real input-policy decisions, without claiming the separate export implementation.

**Inspection record:** commit `6895c42fdba461a1a171fe70e11d67c037bac1d0`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `PSIni/Public/Import-Ini.ps1`, `Tests/Import-Ini.Unit.Tests.ps1`, `README.md`, `LICENSE`. GitHub Linguist label: PowerShell.

</details>

## Level 3

### [Badgerati/Pode](https://github.com/Badgerati/Pode)

**Language 3 / Behavior 2 / Design 3 / Constraints 4 → Level 3**

A cross-platform PowerShell application-server framework with its own asynchronous HTTP, WebSocket, server-sent events, TCP, SMTP, file-watcher, and TLS runtime plus routing, middleware, authentication, sessions, OpenAPI, schedules, and serverless adapters.

**Why study it:** Pode's routing subsystem is a compact PowerShell example of normalizing declarative inputs into a registry and retrieving the correct ordered match.

**Prerequisites:**

- Readers should know PowerShell scriptblocks, hashtables and concurrent collections, regular expressions, middleware composition, and basic HTTP methods, routes, and path parameters.

**Concepts this path develops:**

- Scriptblock and middleware composition.
- Localized registration mutation.
- Methods, literal and parameterized paths, endpoints, and duplicate policy must remain consistent.

**What you can learn:**

- Follow route methods, paths, groups, middleware, authentication, endpoints, and handlers through validation, normalization, duplicate policy, registry insertion, and matching.

**Learning path:**

- **Goal:** Understand how a PowerShell web framework turns declarative method, path, handler, middleware, and endpoint inputs into a normalized route registry and retrieves the correct match.
- **Start here:** [`src/Public/Routes.ps1`](https://github.com/Badgerati/Pode/blob/512a99018dc13027de2d746d5467c4d39a9401b2/src/Public/Routes.ps1) — The reviewed trace begins in public Routes.ps1 because Add-PodeRoute defines and validates the user-facing route before private helpers normalize and index it.
- **Then read:**
  - [`src/Private/Routes.ps1`](https://github.com/Badgerati/Pode/blob/512a99018dc13027de2d746d5467c4d39a9401b2/src/Private/Routes.ps1)
  - [`tests/unit/Routes.Tests.ps1`](https://github.com/Badgerati/Pode/blob/512a99018dc13027de2d746d5467c4d39a9401b2/tests/unit/Routes.Tests.ps1)
  - [`README.md`](https://github.com/Badgerati/Pode/blob/512a99018dc13027de2d746d5467c4d39a9401b2/README.md)
  - [`LICENSE.txt`](https://github.com/Badgerati/Pode/blob/512a99018dc13027de2d746d5467c4d39a9401b2/LICENSE.txt)
- **Trace:** Begin at Add-PodeRoute, follow method and path validation, route-group inheritance, placeholder-to-regex normalization, scoped handler and middleware conversion, access and authentication middleware injection, endpoint-aware duplicate policy, and registry insertion; continue to Find-PodeRoute's exact, wildcard, regex, and endpoint filtering, then close registration, lookup, removal, duplicate, middleware, static-route, content-type, and failure behavior in the direct unit suite.

**Why this level:**

- **Language technique 3:** Advanced cmdlet, scriptblock, collection, and dynamic metadata techniques materially shape registration without expert runtime machinery.
- **Behavioral reasoning 2:** The selected registry path is synchronous and locally inspectable; request and server lifecycles are deliberately outside it.
- **Design span 3:** Several cohesive components and adapter boundaries cooperate around one route model.
- **Constraint burden 4:** Routing, composition, safety, API, and compatibility guarantees recur throughout registration and lookup.
- **Placement:** The four scores 3/2/3/4 sum to 12; their arithmetic mean is 3.00 and rounds half-up to Level 3. The published result is Level 3.

**License:** MIT ([evidence 1](https://github.com/Badgerati/Pode/blob/512a99018dc13027de2d746d5467c4d39a9401b2/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Pode is released through the PowerShell Gallery, Chocolatey, and Docker and documents production hosting for APIs, sites, protocol servers, serverless functions, and container deployments.

**Language evidence:** Server lifecycle, routing, middleware, authentication, sessions, OpenAPI, scheduling, MCP, and runspace orchestration are PowerShell, while first-party C# implements asynchronous listeners, sockets, HTTP, TCP, SMTP, WebSocket, TLS, concurrent structures, and transport logging.

**Coding relevance:**

That short routing vocabulary is subordinate to transferable lessons in scriptblock composition, registry design, normalization, validation, duplicate policy, regex matching, metadata inheritance, concurrent collections, and direct behavior testing.

Required domain context:

- An HTTP route associates a method and normalized path pattern with a handler, middleware, endpoint, and optional access metadata.

**Eight-part quality gate:**

- **Source quality:** Public and private Routes.ps1 keep validation, inheritance, normalization, middleware conversion, endpoint indexing, duplicate handling, and lookup visible.
- **Architecture:** A public registration API produces normalized route records in an endpoint-aware registry, and Find-PodeRoute resolves exact, wildcard, and regular-expression candidates.
- **Naming and idiom:** Add-PodeRoute, Find-PodeRoute, route groups, middleware, endpoints, and path parameters make the registry model clear through PowerShell-native scriptblocks and collections.
- **Tests:** Routes.Tests.ps1 covers adding, finding, removing, clearing, endpoints, middleware, static paths, duplicates, content types, and invalid inputs.
- **Documentation:** README.md documents routing and supplies the framework context required for the bounded registration-and-lookup path.
- **Traceability:** A route declaration can be followed from Add-PodeRoute through normalization and indexing to Find-PodeRoute and the direct unit assertions.
- **Maintainability:** Registration and retrieval share explicit route records, and one direct unit suite constrains normalization, duplicate, and matching policies.
- **Educational value:** The path teaches registry and matching design in PowerShell without requiring the broader server and protocol platform.

**Inspection record:** commit `512a99018dc13027de2d746d5467c4d39a9401b2`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/Public/Routes.ps1`, `src/Private/Routes.ps1`, `tests/unit/Routes.Tests.ps1`, `README.md`, `LICENSE.txt`. GitHub Linguist label: PowerShell.

</details>

### [dfinke/ImportExcel](https://github.com/dfinke/ImportExcel)

**Language 3 / Behavior 3 / Design 2 / Constraints 4 → Level 3**

A PowerShell module for reading, writing, formatting, charting, and pivoting Excel workbooks without requiring Microsoft Excel.

**Why study it:** ImportExcel provides a practical PowerShell adapter path in which workbook ownership, rectangular ranges, header policy, typed values, and deterministic cleanup are all visible.

**Prerequisites:**

- Readers should know PowerShell parameter sets and pipelines, .NET object interoperation, try and finally cleanup, and basic workbook, worksheet, row, column, and header concepts.

**Concepts this path develops:**

- Advanced-function parameter sets and pipeline modes.
- Path-owned versus caller-owned package lifecycle.
- Valid extensions, paths, worksheets, dimensions, and unique headers.

**What you can learn:**

- Trace a path-owned or caller-owned Excel package through worksheet selection, range bounds, headers, typed cell extraction, ordered objects, and finally-based disposal.

**Learning path:**

- **Goal:** Understand how a PowerShell adapter opens an Excel package, turns bounded worksheet cells into ordered objects, and releases only the resources it owns.
- **Start here:** [`Public/Import-Excel.ps1`](https://github.com/dfinke/ImportExcel/blob/5387c061461c811d106b125588f064c4739342cb/Public/Import-Excel.ps1) — The reviewed trace begins in Import-Excel.ps1 because it distinguishes package ownership and coordinates the complete worksheet-to-object conversion.
- **Then read:**
  - [`Public/Open-ExcelPackage.ps1`](https://github.com/dfinke/ImportExcel/blob/5387c061461c811d106b125588f064c4739342cb/Public/Open-ExcelPackage.ps1)
  - [`Public/Close-ExcelPackage.ps1`](https://github.com/dfinke/ImportExcel/blob/5387c061461c811d106b125588f064c4739342cb/Public/Close-ExcelPackage.ps1)
  - [`__tests__/ImportExcelTests/Simple.tests.ps1`](https://github.com/dfinke/ImportExcel/blob/5387c061461c811d106b125588f064c4739342cb/__tests__/ImportExcelTests/Simple.tests.ps1)
  - [`__tests__/ImportExcelTests/ImportExcelEndRowEndColumn.tests.ps1`](https://github.com/dfinke/ImportExcel/blob/5387c061461c811d106b125588f064c4739342cb/__tests__/ImportExcelTests/ImportExcelEndRowEndColumn.tests.ps1)
  - [`__tests__/ImportExcelTests/ImportExcelReadSheets.tests.ps1`](https://github.com/dfinke/ImportExcel/blob/5387c061461c811d106b125588f064c4739342cb/__tests__/ImportExcelTests/ImportExcelReadSheets.tests.ps1)
  - [`README.md`](https://github.com/dfinke/ImportExcel/blob/5387c061461c811d106b125588f064c4739342cb/README.md)
  - [`LICENSE.txt`](https://github.com/dfinke/ImportExcel/blob/5387c061461c811d106b125588f064c4739342cb/LICENSE.txt)
- **Trace:** Start with Import-Excel's path-versus-ExcelPackage parameter sets, follow path validation and stream loading into worksheet selection, row and column bounds, header derivation, duplicate rejection, typed cell extraction, ordered PSCustomObject rows, and finally-based close and disposal; compare caller-owned Open-ExcelPackage and Close-ExcelPackage behavior, then close simple, multiple-sheet, bounded-range, pipeline, resource, and performance behavior in the focused import suites.

**Why this level:**

- **Language technique 3:** Advanced cmdlet composition, pipeline behavior, typed .NET resources, and dynamic property construction materially shape the adapter without expert metaprogramming.
- **Behavioral reasoning 3:** The learner follows resource and iteration state across several stages while the lifecycle remains bounded to one import operation.
- **Design span 2:** A few cohesive modules and one third-party package boundary contain the complete behavior.
- **Constraint burden 4:** Artifact validity, mapping, ownership, error, performance, and compatibility guarantees recur throughout the adapter.
- **Placement:** The four scores 3/3/2/4 sum to 12; their arithmetic mean is 3.00 and rounds half-up to Level 3. The published result is Level 3.

**License:** Apache-2.0 ([evidence 1](https://github.com/dfinke/ImportExcel/blob/5387c061461c811d106b125588f064c4739342cb/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** ImportExcel is published on the PowerShell Gallery and documents automation workflows for reports, inventory, charts, pivot tables, SQL data, and workbook transformation.

**Language evidence:** Workbook import and export, cell typing and formatting, tables, charts, pivot tables, conditional formatting, worksheet operations, and Pester tests are implemented in PowerShell around the bundled EPPlus API.

**Coding relevance:**

That short spreadsheet vocabulary is subordinate to transferable lessons in pipeline adapters, typed .NET interoperation, input normalization, resource ownership, row-to-object mapping, validation, and deterministic cleanup.

Required domain context:

- An Excel workbook exposes worksheets, rectangular cell ranges, header rows, typed values, and an open or owned package resource.

**Eight-part quality gate:**

- **Source quality:** Import-Excel.ps1 keeps input modes, worksheet selection, range derivation, header rules, row mapping, error handling, and cleanup visible; open and close helpers clarify ownership.
- **Architecture:** The adapter either opens a package or accepts a caller-owned one, projects bounded cells into ordered objects, and disposes only resources it acquired.
- **Naming and idiom:** Import-Excel, Open-ExcelPackage, Close-ExcelPackage, worksheet and range parameters, and PSCustomObject rows mirror PowerShell and spreadsheet intent.
- **Tests:** Simple.tests.ps1, ImportExcelEndRowEndColumn.tests.ps1, and ImportExcelReadSheets.tests.ps1 cover real XLSX input, sheets, bounds, pipelines, ownership, and representative performance.
- **Documentation:** README.md documents importing, worksheet selection, ranges, and explicit package use.
- **Traceability:** A workbook path or package can be followed through sheet and range normalization into emitted objects and then matched against focused artifact-based tests.
- **Maintainability:** Ownership rules are explicit, conversion stays in one public adapter, and direct real-file tests constrain resource and mapping regressions.
- **Educational value:** The path teaches that a useful data adapter must make lifetime and input-shape policy as clear as its happy-path conversion.

**Inspection record:** commit `5387c061461c811d106b125588f064c4739342cb`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `Public/Import-Excel.ps1`, `Public/Open-ExcelPackage.ps1`, `Public/Close-ExcelPackage.ps1`, `__tests__/ImportExcelTests/Simple.tests.ps1`, `__tests__/ImportExcelTests/ImportExcelEndRowEndColumn.tests.ps1`, `__tests__/ImportExcelTests/ImportExcelReadSheets.tests.ps1`, `README.md`, `LICENSE.txt`. GitHub Linguist label: PowerShell.

</details>

## Level 4

### [nightroman/Invoke-Build](https://github.com/nightroman/Invoke-Build)

**Language 3 / Behavior 4 / Design 3 / Constraints 4 → Level 4**

A compact build-automation engine for PowerShell with task graphs, incremental inputs and outputs, nested builds, checkpoints, hooks, structured results, and parallel build execution.

**Why study it:** Invoke-Build's parallel coordinator is a bounded example of scheduling asynchronous PowerShell workers while preserving concurrency, output, timeout, and failure contracts.

**Prerequisites:**

- Readers should know PowerShell scripts, pipelines, collections, errors, asynchronous invocation, and the basic idea of limiting concurrent build workers.

**Concepts this path develops:**

- System.Management.Automation.PowerShell instances.
- Pending, active, completed, failed, and timed-out worker states.
- MaximumBuilds must bound concurrency.

**What you can learn:**

- Trace queued build scripts through admission, PowerShell instance creation, asynchronous invocation, completion polling, timeout stopping, output collection, and final error aggregation.

**Learning path:**

- **Goal:** Understand how a PowerShell coordinator schedules several build scripts concurrently, limits active workers, and preserves output, timeout, and failure contracts.
- **Start here:** [`Build-Parallel.ps1`](https://github.com/nightroman/Invoke-Build/blob/16e0279db6dcc3845d0a550373e1f9f137f2f51b/Build-Parallel.ps1) — The reviewed trace begins in Build-Parallel.ps1 because it owns the pending and active queues, worker limit, asynchronous lifecycle, timeout, and aggregate result.
- **Then read:**
  - [`Invoke-Build.ps1`](https://github.com/nightroman/Invoke-Build/blob/16e0279db6dcc3845d0a550373e1f9f137f2f51b/Invoke-Build.ps1)
  - [`Tests/Build-Parallel/Parallel.build.ps1`](https://github.com/nightroman/Invoke-Build/blob/16e0279db6dcc3845d0a550373e1f9f137f2f51b/Tests/Build-Parallel/Parallel.build.ps1)
  - [`Tests/Build-Parallel/Parallel.test.ps1`](https://github.com/nightroman/Invoke-Build/blob/16e0279db6dcc3845d0a550373e1f9f137f2f51b/Tests/Build-Parallel/Parallel.test.ps1)
  - [`Docs/Parallel-Builds.md`](https://github.com/nightroman/Invoke-Build/blob/16e0279db6dcc3845d0a550373e1f9f137f2f51b/Docs/Parallel-Builds.md)
  - [`Docs/Design-Notes.md`](https://github.com/nightroman/Invoke-Build/blob/16e0279db6dcc3845d0a550373e1f9f137f2f51b/Docs/Design-Notes.md)
  - [`README.md`](https://github.com/nightroman/Invoke-Build/blob/16e0279db6dcc3845d0a550373e1f9f137f2f51b/README.md)
  - [`LICENSE`](https://github.com/nightroman/Invoke-Build/blob/16e0279db6dcc3845d0a550373e1f9f137f2f51b/LICENSE)
- **Trace:** Start with Build-Parallel's queue, MaximumBuilds admission rule, PowerShell instance creation, BeginInvoke and EndInvoke lifecycle, completion polling, timeout stop, output collection, and final error aggregation; use Invoke-Build only as the worker boundary, then close concurrent success, partial failure, timeout, nesting, and validation in the dedicated build and test scripts plus design notes.

**Why this level:**

- **Language technique 3:** Asynchronous PowerShell APIs and language-native worker composition materially shape the path without recurring expert runtime manipulation.
- **Behavioral reasoning 4:** Scheduling and failure state must be followed across several asynchronous workers and lifecycle transitions, matching the Level 4 anchor.
- **Design span 3:** Several cohesive components and one asynchronous runtime boundary contain the complete behavior.
- **Constraint burden 4:** Concurrency, timeout, resource, compatibility, and error contracts recur throughout the coordinator.
- **Placement:** The four scores 3/4/3/4 sum to 14; their arithmetic mean is 3.50 and rounds half-up to Level 4. The published result is Level 4.

**License:** Apache-2.0 ([evidence 1](https://github.com/nightroman/Invoke-Build/blob/16e0279db6dcc3845d0a550373e1f9f137f2f51b/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Invoke-Build is distributed through the PowerShell Gallery, NuGet, and a dotnet tool, and its documentation links to production projects that use its build-script model.

**Language evidence:** Task declaration, dependency validation, incremental scheduling, execution, error propagation, checkpoints, parallel builds, graph output, and the behavior suites are PowerShell.

**Coding relevance:**

That small build vocabulary is subordinate to transferable lessons in asynchronous PowerShell instances, bounded scheduling, coordinator state, timeout and cancellation, output capture, nested invocation, and aggregated failure reporting.

Required domain context:

- A parallel build coordinator starts independent build scripts as workers while limiting concurrency and collecting their results.

**Eight-part quality gate:**

- **Source quality:** Build-Parallel.ps1 keeps pending, active, completed, failed, and timed-out worker state visible in one coordinator.
- **Architecture:** The coordinator admits bounded workers, delegates each script to Invoke-Build, polls asynchronous handles, and consolidates output and failures.
- **Naming and idiom:** MaximumBuilds, BeginInvoke, EndInvoke, pending and active collections, and timeout state make the scheduler legible through standard PowerShell hosting APIs.
- **Tests:** Parallel.build.ps1 and Parallel.test.ps1 exercise overlap, concurrency limits, partial failure, timeout, nesting, information output, and invalid input.
- **Documentation:** Parallel-Builds.md explains use, and Design-Notes.md documents the coordinator boundary and lifecycle decisions.
- **Traceability:** A queued build path can be followed through worker admission and asynchronous completion to exact scenarios in the dedicated parallel test files.
- **Maintainability:** The selected coordinator is separate from the broader task engine, and direct executable scenarios constrain its scheduling and reporting behavior.
- **Educational value:** The path makes bounded concurrency and asynchronous resource cleanup inspectable in ordinary PowerShell rather than hiding them behind a build service.

**Inspection record:** commit `16e0279db6dcc3845d0a550373e1f9f137f2f51b`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `Build-Parallel.ps1`, `Invoke-Build.ps1`, `Tests/Build-Parallel/Parallel.build.ps1`, `Tests/Build-Parallel/Parallel.test.ps1`, `Docs/Parallel-Builds.md`, `Docs/Design-Notes.md`, `README.md`, `LICENSE`. GitHub Linguist label: PowerShell.

</details>

### [PoshCode/ModuleBuilder](https://github.com/PoshCode/ModuleBuilder)

**Language 5 / Behavior 3 / Design 3 / Constraints 4 → Level 4**

A PowerShell build module that compiles source folders into versioned modules, rewrites manifests, preserves source mappings, applies syntax-tree generators, and prepares packages for publication.

**Why study it:** ModuleBuilder shows how PowerShell's own parser and syntax tree can support a source-to-source transformation that remains syntactically valid and executable.

**Prerequisites:**

- Readers should know PowerShell functions and scriptblocks, begin, process, and end blocks, abstract syntax trees, visitors, source offsets, and parsing errors.

**Concepts this path develops:**

- PowerShell parser, token, extent, and typed AST hierarchy APIs.
- Parse, visit, collect, replace, generate, and reparse stages.
- Replacement offsets and ordering must preserve source structure.

**What you can learn:**

- Follow named-block and function AST discovery through exact source extents, ordered replacements, script generation, reparsing, and behavior tests.

**Learning path:**

- **Goal:** Understand how PowerShell's parser and AST can drive a source-to-source generator that merges scriptblocks without corrupting syntax or execution structure.
- **Start here:** [`Source/Public/Merge-ScriptBlock.ps1`](https://github.com/PoshCode/ModuleBuilder/blob/3b19a45518b99aded3ecc20e709d96a19a3e937b/Source/Public/Merge-ScriptBlock.ps1) — The reviewed trace begins in Merge-ScriptBlock.ps1 because its visitor decides which syntax nodes become the generated merged scriptblock.
- **Then read:**
  - [`Source/Private/ConvertToAst.ps1`](https://github.com/PoshCode/ModuleBuilder/blob/3b19a45518b99aded3ecc20e709d96a19a3e937b/Source/Private/ConvertToAst.ps1)
  - [`Source/Classes/10. TextReplacement.ps1`](https://github.com/PoshCode/ModuleBuilder/blob/3b19a45518b99aded3ecc20e709d96a19a3e937b/Source/Classes/10.%20TextReplacement.ps1)
  - [`Source/Public/Invoke-ScriptGenerator.ps1`](https://github.com/PoshCode/ModuleBuilder/blob/3b19a45518b99aded3ecc20e709d96a19a3e937b/Source/Public/Invoke-ScriptGenerator.ps1)
  - [`Tests/Private/ConvertToAst.Tests.ps1`](https://github.com/PoshCode/ModuleBuilder/blob/3b19a45518b99aded3ecc20e709d96a19a3e937b/Tests/Private/ConvertToAst.Tests.ps1)
  - [`Tests/Public/Merge-ScriptBlock.Tests.ps1`](https://github.com/PoshCode/ModuleBuilder/blob/3b19a45518b99aded3ecc20e709d96a19a3e937b/Tests/Public/Merge-ScriptBlock.Tests.ps1)
  - [`ReadMe.md`](https://github.com/PoshCode/ModuleBuilder/blob/3b19a45518b99aded3ecc20e709d96a19a3e937b/ReadMe.md)
  - [`LICENSE`](https://github.com/PoshCode/ModuleBuilder/blob/3b19a45518b99aded3ecc20e709d96a19a3e937b/LICENSE)
- **Trace:** Start with Merge-ScriptBlock's BlockGenerator visitor over NamedBlockAst and FunctionDefinitionAst nodes, follow ConvertToAst selection and exact source extents into ordered TextReplacement edits and Invoke-ScriptGenerator execution, then reparse the generated text and close begin, process, end, parameter, function, and parse-failure behavior in the two direct AST suites.

**Why this level:**

- **Language technique 5:** Multiple advanced PowerShell language and compiler-facing mechanisms interact pervasively across the selected transformation, meeting the expert Language 5 anchor.
- **Behavioral reasoning 3:** The learner follows a multistage synchronous transformation whose state is explicit and bounded.
- **Design span 3:** Several cohesive components cooperate across parser, transformation, generator, and test boundaries.
- **Constraint burden 4:** Syntax preservation, transformation ordering, semantic compatibility, and version guarantees recur throughout the path.
- **Placement:** The four scores 5/3/3/4 sum to 15; their arithmetic mean is 3.75 and rounds half-up to Level 4. The published result is Level 4.

**License:** MIT ([evidence 1](https://github.com/PoshCode/ModuleBuilder/blob/3b19a45518b99aded3ecc20e709d96a19a3e937b/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** ModuleBuilder is published as a PowerShell Gallery module and documents a source-to-package workflow used by PowerShell module authors.

**Language evidence:** Module assembly, manifest rewriting, syntax-tree parsing, using-statement relocation, source mapping, generator transforms, signing and packaging support, and tests are PowerShell.

**Coding relevance:**

The compact module-build vocabulary is subordinate to transferable lessons in syntax trees, visitor dispatch, source extents, ordered text replacement, scriptblock generation, closure capture, reparsing, and transformation contracts.

Required domain context:

- A module build generator rewrites PowerShell source blocks while preserving valid module structure and source meaning.

**Eight-part quality gate:**

- **Source quality:** Merge-ScriptBlock.ps1 and ConvertToAst.ps1 keep traversal and selection explicit, while TextReplacement.ps1 and Invoke-ScriptGenerator.ps1 isolate mutation and execution.
- **Architecture:** A parser produces AST nodes and exact extents, a visitor plans ordered replacements, a generator applies them, and the output is reparsed before use.
- **Naming and idiom:** BlockGenerator, ConvertToAst, TextReplacement, and Invoke-ScriptGenerator expose each transformation stage and use PowerShell AST APIs directly.
- **Tests:** ConvertToAst.Tests.ps1 and Merge-ScriptBlock.Tests.ps1 verify begin, process, end, parameter, function, source-selection, and parse-failure behavior.
- **Documentation:** ReadMe.md explains module generation and gives the context needed to understand why scriptblocks are merged.
- **Traceability:** A selected NamedBlockAst or FunctionDefinitionAst can be followed from visitor dispatch through extent replacement and reparsing into direct AST test assertions.
- **Maintainability:** Parsing, transformation planning, text application, and generator execution have separate boundaries, with focused tests around generated syntax.
- **Educational value:** The path demonstrates advanced PowerShell as a language-tooling platform, not only as a command shell.

**Inspection record:** commit `3b19a45518b99aded3ecc20e709d96a19a3e937b`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `Source/Public/Merge-ScriptBlock.ps1`, `Source/Private/ConvertToAst.ps1`, `Source/Classes/10. TextReplacement.ps1`, `Source/Public/Invoke-ScriptGenerator.ps1`, `Tests/Private/ConvertToAst.Tests.ps1`, `Tests/Public/Merge-ScriptBlock.Tests.ps1`, `ReadMe.md`, `LICENSE`. GitHub Linguist label: PowerShell.

</details>

## Level 5

### [pester/Pester](https://github.com/pester/Pester)

**Language 5 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

PowerShell's test and mock framework, with a discovery and execution runtime, assertions, scope-aware mocks, filtering, plugins, code coverage, parallel containers, and CI result formats.

**Why study it:** Pester exposes an expert PowerShell framework lifecycle from Describe and It declarations through discovery, scoping, hooks, execution, errors, filtering, and results.

**Prerequisites:**

- Readers should know advanced PowerShell scriptblocks, scopes and session state, dynamic parameters, recursive trees, hooks, error records, and ordinary test-framework vocabulary.

**Concepts this path develops:**

- Dynamic scriptblock generation and closure handling.
- Separate discovery and execution phases over a recursive block tree.
- Discovery must never accidentally execute test bodies.

**What you can learn:**

- Trace declared scriptblocks into a discovered tree, then through recursive execution, session-state switching, setup and teardown, plugin callbacks, filtering, timing, and result decoration.

**Learning path:**

- **Goal:** Understand how Pester turns Describe and It scriptblocks into a discovered test tree and then executes that tree with correct scopes, hooks, errors, timing, filtering, and results.
- **Start here:** [`src/functions/Describe.ps1`](https://github.com/pester/Pester/blob/bfcbd4d2b0fc5e89d058f59da19feabf853d33c2/src/functions/Describe.ps1) — The reviewed trace begins in Describe.ps1 because Describe establishes the outer DSL contract and registers blocks that the runtime later discovers and executes.
- **Then read:**
  - [`src/functions/It.ps1`](https://github.com/pester/Pester/blob/bfcbd4d2b0fc5e89d058f59da19feabf853d33c2/src/functions/It.ps1)
  - [`src/Pester.Runtime.ps1`](https://github.com/pester/Pester/blob/bfcbd4d2b0fc5e89d058f59da19feabf853d33c2/src/Pester.Runtime.ps1)
  - [`src/Pester.RSpec.ps1`](https://github.com/pester/Pester/blob/bfcbd4d2b0fc5e89d058f59da19feabf853d33c2/src/Pester.RSpec.ps1)
  - [`tst/Pester.Runtime.ts.ps1`](https://github.com/pester/Pester/blob/bfcbd4d2b0fc5e89d058f59da19feabf853d33c2/tst/Pester.Runtime.ts.ps1)
  - [`tst/Pester.RSpec.ts.ps1`](https://github.com/pester/Pester/blob/bfcbd4d2b0fc5e89d058f59da19feabf853d33c2/tst/Pester.RSpec.ts.ps1)
  - [`README.md`](https://github.com/pester/Pester/blob/bfcbd4d2b0fc5e89d058f59da19feabf853d33c2/README.md)
  - [`LICENSE`](https://github.com/pester/Pester/blob/bfcbd4d2b0fc5e89d058f59da19feabf853d33c2/LICENSE)
- **Trace:** Start with Describe and It validation, parameterized block and test registration, and interactive handling; follow New-Block and New-Test into Pester.Runtime's discovery tree, recursive Invoke-Block execution, session-state and scriptblock scope switching, setup and teardown order, plugin callbacks, filtering, errors, timing, and result decoration in Pester.RSpec; then close nested, generated, scoped, skipped, failed, and filtered lifecycle behavior in the focused runtime and DSL suites.

**Why this level:**

- **Language technique 5:** Multiple expert PowerShell runtime, scope, reflection, and dynamic-language mechanisms interact pervasively across declaration, discovery, and execution.
- **Behavioral reasoning 5:** Expert nonlocal lifecycle reasoning is pervasive across nested state machines, callbacks, scopes, failures, and recovery.
- **Design span 4:** Several major subsystems and boundaries cooperate, while the selected trace remains narrower than the entire framework including mocking, coverage, and parallel orchestration.
- **Constraint burden 5:** Scope, lifecycle, error, isolation, determinism, API, version, and platform guarantees are pervasive and tightly coupled.
- **Placement:** The four scores 5/5/4/5 sum to 19; their arithmetic mean is 4.75 and rounds half-up to Level 5. The published result is Level 5.

**License:** Apache-2.0 ([evidence 1](https://github.com/pester/Pester/blob/bfcbd4d2b0fc5e89d058f59da19feabf853d33c2/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Pester is the standard PowerShell testing framework, is distributed through the PowerShell Gallery, ships with older Windows installations, and integrates with editors and continuous-integration systems.

**Language evidence:** Test discovery and execution, nested scopes, hooks, assertions, mocking, filtering, output and result formats, code coverage integration, parallel orchestration, and supporting runtime types are implemented in PowerShell and first-party C#.

**Coding relevance:**

That familiar testing vocabulary is subordinate to transferable expert PowerShell lessons in scriptblock scope, session-state manipulation, dynamic test generation, tree construction, recursive lifecycle execution, plugin hooks, error capture, timing, filtering, and isolation.

Required domain context:

- Describe and It declare nested test blocks whose discovery, filtering, setup, execution, result, and cleanup lifecycle is managed by the framework runtime.

**Eight-part quality gate:**

- **Source quality:** Describe.ps1 and It.ps1 validate and register test declarations, while Pester.Runtime.ps1 and Pester.RSpec.ps1 make discovery and execution state explicit.
- **Architecture:** The public DSL builds block and test records during discovery, and a recursive runtime executes that tree with scopes, hooks, plugins, filters, timing, and results.
- **Naming and idiom:** Describe, It, New-Block, New-Test, Invoke-Block, discovery state, and execution state map directly to the framework lifecycle and PowerShell scriptblock semantics.
- **Tests:** Pester.Runtime.ts.ps1 and Pester.RSpec.ts.ps1 exercise nesting, data expansion, scope fidelity, setup paths, filtering, skips, failures, and aggregated results.
- **Documentation:** README.md introduces the DSL and expected lifecycle, supplying the user-facing contract for the selected runtime path.
- **Traceability:** A Describe and It declaration can be followed into discovered records, recursive execution, hook and error handling, and the focused runtime and RSpec suites.
- **Maintainability:** Discovery and execution are separated, lifecycle state has named records and phases, and self-tests protect scope and ordering behavior.
- **Educational value:** The path reveals how a familiar test DSL depends on careful dynamic scope and lifecycle engineering underneath.

**Inspection record:** commit `bfcbd4d2b0fc5e89d058f59da19feabf853d33c2`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/functions/Describe.ps1`, `src/functions/It.ps1`, `src/Pester.Runtime.ps1`, `src/Pester.RSpec.ps1`, `tst/Pester.Runtime.ts.ps1`, `tst/Pester.RSpec.ts.ps1`, `README.md`, `LICENSE`. GitHub Linguist label: PowerShell.

</details>

_Generated from `catalog/powershell.json`; do not edit by hand._

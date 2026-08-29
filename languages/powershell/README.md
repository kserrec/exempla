# PowerShell

10 qualified repositories. Scores assume the learner described in [the SDC rubric](../../docs/sdc.md).

[← All languages](../README.md)

## SDC 1

### [deadlydog/Invoke-MsBuild](https://github.com/deadlydog/Invoke-MsBuild)

**S1 / D2 / C1 → SDC 1**

A small PowerShell module that locates an installed MSBuild, runs a project or solution with structured options, manages logs, and reports a typed build result.

**Real-world evidence:** The repository publishes the Invoke-MsBuild PowerShell module and documents use from build scripts, continuous-integration jobs, and ordinary PowerShell sessions.

**Language evidence:** MSBuild discovery, argument construction, process execution, log lifecycle, result classification, and Pester tests are implemented in PowerShell under src/Invoke-MsBuild.

**Why study it:** One production module shows how to wrap a real external tool responsibly: discover it, translate friendly parameters into command-line arguments, isolate process execution, capture logs, and distinguish success from failure.

**What you can learn:**

- Advanced functions, parameter sets, executable discovery, Visual Studio installation probing, command-line construction, System.Diagnostics.Process, output and error capture, temporary logs, result objects, mocking, and platform-dependent tests.

**Prerequisites:**

- PowerShell modules and advanced functions, filesystem paths, external processes, quoting, hashtables, try/finally cleanup, and basic MSBuild concepts.

**Start here:** [`src/Invoke-MsBuild/Invoke-MsBuild.psm1`](https://github.com/deadlydog/Invoke-MsBuild/blob/7fee8e141296ea6c337e433537d7061f52e24157/src/Invoke-MsBuild/Invoke-MsBuild.psm1) — The single production file contains executable discovery, argument assembly, process invocation, logging, cleanup, and result construction, so the complete adapter can be read in sequence.

**Why this level:**

- **S1:** 420 meaningful implementation LOC measured with tokei 14.0.0. Count covers the complete production module under src/Invoke-MsBuild and excludes tests, examples, documentation, and package metadata.
- **D2:** The wrapper crosses a process boundary and several installation layouts, but the logic remains direct and uses standard .NET and PowerShell facilities.
- **C1:** There is no internal subsystem graph; discovery and execution are cohesive stages in one file.
- **Placement:** S1/D2/C1 averages to 1.33, making Invoke-MsBuild an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** Input validation, command construction, process ownership, log cleanup, and failure reporting are visible rather than hidden behind a generic shell helper.
- **Architecture:** Discovery resolves an executable, the public command builds its argument vector, a process wrapper executes it, and a result object exposes the outcome and log.
- **Naming and idiom:** Invoke-MsBuild, Get-MsBuildPath, BuildParameters, LogVerbosity, and BuildResult communicate the adapter's responsibilities directly.
- **Tests:** Pester tests mock installation layouts and process calls while covering path selection, parameters, logging, success, failure, cleanup, and pipeline behavior.
- **Documentation:** The README explains installation, common calls, every major option, returned data, logging, and continuous-integration usage.
- **Traceability:** A project path can be followed into the exact MSBuild argument string, ProcessStartInfo, log file, exit classification, and corresponding mocked test.
- **Maintainability:** The module has one clear dependency boundary, keeps discovery replaceable, and exercises operating-system-specific decisions with mocks.
- **Educational value:** It demonstrates that even a small command wrapper benefits from explicit process, path, quoting, cleanup, and error contracts.

**Inspection record:** commit `7fee8e141296ea6c337e433537d7061f52e24157`, reviewed 2026-08-28 by Codex. Files sampled: `ReadMe.md`, `src/Invoke-MsBuild/Invoke-MsBuild.psm1`, `src/Tests/Invoke-MsBuild.Tests.ps1`, `License.md`. GitHub Linguist label: PowerShell. LOC exclusions: src/Tests/, examples and sample build files, documentation and packaging files.

**License:** [MIT](https://github.com/deadlydog/Invoke-MsBuild/blob/7fee8e141296ea6c337e433537d7061f52e24157/License.md)

### [lipkau/PSIni](https://github.com/lipkau/PSIni)

**S1 / D1 / C1 → SDC 1**

A compact PowerShell module that reads and writes INI files as ordered hashtables while preserving sections, comments, repeated keys, and encoding choices.

**Real-world evidence:** PSIni is maintained as a versioned PowerShell Gallery module, and its README documents command-line and pipeline use for application and system configuration files.

**Language evidence:** INI parsing, ordered-hashtable construction, duplicate-key handling, comment preservation, serialization, encoding support, and the test suite are implemented in PowerShell under PSIni and Tests.

**Why study it:** Two small public commands expose the complete path from line-oriented text through section and key parsing into an ordered object model and back to a stable file representation.

**What you can learn:**

- Advanced functions, pipeline input, ordered hashtables, line-oriented parsing, regular expressions, repeated-key policies, comment preservation, text encodings, ShouldProcess, and focused Pester tests.

**Prerequisites:**

- PowerShell functions and parameters, hashtables, pipelines, regular expressions, filesystem cmdlets, encodings, and basic Pester assertions.

**Start here:** [`PSIni/Public/Import-Ini.ps1`](https://github.com/lipkau/PSIni/blob/6895c42fdba461a1a171fe70e11d67c037bac1d0/PSIni/Public/Import-Ini.ps1) — Import-Ini contains the whole read path: it selects an encoding, recognizes sections, comments, and key-value lines, applies duplicate-key policy, and returns the ordered structure exercised by the unit suite.

**Why this level:**

- **S1:** 413 meaningful implementation LOC measured with tokei 14.0.0. Count covers the complete production PowerShell module under PSIni and excludes tests, documentation, and release metadata.
- **D1:** The parser handles useful edge cases, but its state is limited to the current section and output hashtable, with no advanced algorithm or runtime concern.
- **C1:** All behavior is local to one small module with no services, concurrency, persistence model, or plugin topology.
- **Placement:** S1/D1/C1 averages to 1.00, making PSIni an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** Parsing and serialization keep their branches explicit, preserve input order deliberately, and report malformed or duplicate data through visible policies.
- **Architecture:** Import-Ini builds an ordered section model and Export-Ini serializes the same model; small private helpers centralize encoding and formatting details.
- **Naming and idiom:** Import-Ini, Export-Ini, AllowDuplicateKeys, SkipComments, and NoSection make both the object model and edge-case policy discoverable.
- **Tests:** Pester suites cover files and literal content, comments, blank lines, global keys, sections, duplicate keys, malformed input, encodings, pipelines, and round trips.
- **Documentation:** The README explains installation, both commands, object shapes, switches, encodings, examples, and compatibility.
- **Traceability:** A line can be followed through Import-Ini's match branches into a specific hashtable entry and then through Export-Ini into exact text assertions.
- **Maintainability:** The public surface is narrow, behavior flags are explicit, the representation is a standard PowerShell type, and regression cases are close to the implementation.
- **Educational value:** It is an approachable complete parser and serializer whose useful edge cases do not overwhelm the central control flow.

**Inspection record:** commit `6895c42fdba461a1a171fe70e11d67c037bac1d0`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `PSIni/Public/Import-Ini.ps1`, `PSIni/Public/Export-Ini.ps1`, `Tests/Import-Ini.Unit.Tests.ps1`, `LICENSE`. GitHub Linguist label: PowerShell. LOC exclusions: Tests/, build and packaging files, README.md.

**License:** [MIT](https://github.com/lipkau/PSIni/blob/6895c42fdba461a1a171fe70e11d67c037bac1d0/LICENSE)

## SDC 2

### [nightroman/Invoke-Build](https://github.com/nightroman/Invoke-Build)

**S1 / D3 / C2 → SDC 2**

A compact build-automation engine for PowerShell with task graphs, incremental inputs and outputs, nested builds, checkpoints, hooks, structured results, and parallel build execution.

**Real-world evidence:** Invoke-Build is distributed through the PowerShell Gallery, NuGet, and a dotnet tool, and its documentation links to production projects that use its build-script model.

**Language evidence:** Task declaration, dependency validation, incremental scheduling, execution, error propagation, checkpoints, parallel builds, graph output, and the behavior suites are PowerShell.

**Why study it:** The project fits a real build engine into a small codebase while leaving task registration, graph validation, up-to-date checks, scope handling, job execution, and parallel orchestration inspectable.

**What you can learn:**

- PowerShell dynamic parameters, build DSLs, task dependency graphs, cycle detection, incremental timestamps, nested script scopes, hooks, structured errors, asynchronous PowerShell instances, timeouts, checkpoints, and executable specification tests.

**Prerequisites:**

- Advanced PowerShell functions and scopes, scriptblocks, dynamic parameters, collections, graph traversal, filesystem timestamps, asynchronous invocation, and build-system concepts.

**Start here:** [`Invoke-Build.ps1`](https://github.com/nightroman/Invoke-Build/blob/16e0279db6dcc3845d0a550373e1f9f137f2f51b/Invoke-Build.ps1) — The engine file defines the task DSL, constructs and validates the graph, evaluates incremental work, manages nested scopes, runs jobs, and records results; Build-Parallel.ps1 then extends the same contract across asynchronous PowerShell instances.

**Why this level:**

- **S1:** 1,731 meaningful implementation LOC measured with tokei 14.0.0. Count covers Invoke-Build.ps1 and the production companion scripts for parallel execution, checkpoints, task selection, help, argument completion, graph output, and MSBuild resolution; duplicated package content, tests, samples, and documentation are excluded.
- **D3:** The engine depends on nontrivial PowerShell runtime behavior and graph state, but its algorithms and state transitions are explicit in a small set of scripts.
- **C2:** Multiple cohesive mechanisms cooperate around one build model, without the broader topology of a service platform.
- **Placement:** S1/D3/C2 averages to 2.00, making Invoke-Build an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** The implementation is dense but disciplined: task state is explicit, cycles and missing references fail early, cleanup uses finally blocks, and errors retain source positions.
- **Architecture:** A task-registration DSL builds an ordered graph; validation checks references; the executor applies conditions and freshness rules; companion scripts add parallelism, checkpoints, and projections.
- **Naming and idiom:** Add-BuildTask, Inputs, Outputs, Partial, Enter-BuildTask, Get-BuildError, Build-Parallel, and Result map directly to the build model.
- **Tests:** Executable build scripts cover graph ordering, cycles, incremental and partial work, dynamic parameters, nested scopes, hooks, errors, safe mode, checkpoints, timeouts, parallel failures, and regressions.
- **Documentation:** The README, command help, concepts, design notes, tutorials, templates, and comparisons explain both usage and the engine's choices.
- **Traceability:** A task declaration can be followed into the graph table, recursive reference checks, freshness evaluation, job execution, result aggregation, and an exact .test.ps1 scenario.
- **Maintainability:** The core model has remained compact, optional tools are separate scripts, errors are observable, and the test corpus doubles as runnable behavior documentation.
- **Educational value:** It is a rare small implementation of a genuine build system and a strong study of how a language-native DSL becomes a scheduler.

**Inspection record:** commit `16e0279db6dcc3845d0a550373e1f9f137f2f51b`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Invoke-Build.ps1`, `Build-Parallel.ps1`, `Tests/Incremental.test.ps1`, `Tests/Build-Parallel/Parallel.test.ps1`, `LICENSE`. GitHub Linguist label: PowerShell. LOC exclusions: Tests/, Tasks/ samples, Docs/, packaged Content copies, build and release files.

**License:** [Apache-2.0](https://github.com/nightroman/Invoke-Build/blob/16e0279db6dcc3845d0a550373e1f9f137f2f51b/LICENSE)

### [PoshCode/ModuleBuilder](https://github.com/PoshCode/ModuleBuilder)

**S1 / D3 / C2 → SDC 2**

A PowerShell build module that compiles source folders into versioned modules, rewrites manifests, preserves source mappings, applies syntax-tree generators, and prepares packages for publication.

**Real-world evidence:** ModuleBuilder is published as a PowerShell Gallery module and documents a source-to-package workflow used by PowerShell module authors.

**Language evidence:** Module assembly, manifest rewriting, syntax-tree parsing, using-statement relocation, source mapping, generator transforms, signing and packaging support, and tests are PowerShell.

**Why study it:** It turns ordinary module source files into reproducible artifacts while demonstrating when text concatenation is insufficient and PowerShell's abstract syntax tree should guide safe transformations.

**What you can learn:**

- PowerShell module layout, manifests, semantic versions, abstract syntax trees, token and extent handling, using-statement normalization, source-line mapping, generator visitors, function and alias discovery, packaging, signing, and integration tests.

**Prerequisites:**

- Advanced PowerShell modules, manifests, scriptblocks, AST and token concepts, filesystem builds, semantic versioning, metadata, and Pester.

**Start here:** [`Source/Public/Build-Module.ps1`](https://github.com/PoshCode/ModuleBuilder/blob/3b19a45518b99aded3ecc20e709d96a19a3e937b/Source/Public/Build-Module.ps1) — Build-Module owns the end-to-end pipeline from source discovery and output selection through content assembly, manifest updates, optional AST generators, versioning, and the final module artifact.

**Why this level:**

- **S1:** 1,473 meaningful implementation LOC measured with tokei 14.0.0. Count covers every production PowerShell file under Source and excludes tests, generated build artifacts, experimental contribution material, documentation, and release metadata.
- **D3:** Safe source transformation and metadata synchronization require compiler-facing APIs and careful offsets, even though the project remains compact.
- **C2:** The pipeline has several explicit stages but one artifact flow and no persistent or distributed runtime.
- **Placement:** S1/D3/C2 averages to 2.00, making ModuleBuilder an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** Build stages are named functions, AST parsing returns tokens and errors together, transformations operate on source extents, and output ownership is explicit.
- **Architecture:** Initialization resolves module metadata; content assembly normalizes scripts; manifest helpers synchronize exports and versions; optional generators rewrite AST regions before packaging.
- **Naming and idiom:** Build-Module, ConvertToAst, SetModuleContent, Merge-ScriptBlock, Update-Metadata, and ResolveOutputFolder expose the compilation pipeline.
- **Tests:** Pester unit and integration suites verify clean versus build targets, using placement, file combination, exports, aliases, semantic versions, metadata, AST parsing, generator replacements, and idempotence.
- **Documentation:** The README explains conventions, build settings, versioned output, publishing, generators, source mappings, and complete examples.
- **Traceability:** A source function can be followed from directory discovery through AST-aware content generation into the built psm1, manifest export list, and integration assertions.
- **Maintainability:** Compiler-like operations are isolated behind helpers, public build policy is parameterized, and integration fixtures constrain emitted artifacts rather than implementation calls alone.
- **Educational value:** It gives module authors a concrete introduction to build pipelines and syntax-aware code generation without requiring a general compiler framework.

**Inspection record:** commit `3b19a45518b99aded3ecc20e709d96a19a3e937b`, reviewed 2026-08-28 by Codex. Files sampled: `ReadMe.md`, `Source/Public/Build-Module.ps1`, `Source/Public/Merge-ScriptBlock.ps1`, `Source/Private/ConvertToAst.ps1`, `Tests/Public/Build-Module.Tests.ps1`, `Tests/Public/Merge-ScriptBlock.Tests.ps1`, `LICENSE`. GitHub Linguist label: PowerShell. LOC exclusions: Tests/, Build/ generated output, PotentialContribution/, documentation and release files.

**License:** [MIT](https://github.com/PoshCode/ModuleBuilder/blob/3b19a45518b99aded3ecc20e709d96a19a3e937b/LICENSE)

## SDC 3

### [dfinke/ImportExcel](https://github.com/dfinke/ImportExcel)

**S2 / D3 / C3 → SDC 3**

A PowerShell module for reading, writing, formatting, charting, and pivoting Excel workbooks without requiring Microsoft Excel.

**Real-world evidence:** ImportExcel is published on the PowerShell Gallery and documents automation workflows for reports, inventory, charts, pivot tables, SQL data, and workbook transformation.

**Language evidence:** Workbook import and export, cell typing and formatting, tables, charts, pivot tables, conditional formatting, worksheet operations, and Pester tests are implemented in PowerShell around the bundled EPPlus API.

**Why study it:** It shows how a PowerShell-friendly pipeline API maps dynamic objects onto a rich document model while preserving types, formats, formulas, tables, charts, pivots, and workbook resource ownership.

**What you can learn:**

- Pipeline object discovery, workbook and worksheet lifecycles, cell addressing, type and number-format inference, formulas, tables, charts and series, pivot tables, conditional formatting, streamed row conversion, resource cleanup, and artifact-level tests.

**Prerequisites:**

- PowerShell objects and pipelines, .NET object interop, spreadsheets and cell ranges, dates and number formats, disposable resources, charts, pivot tables, and Pester.

**Start here:** [`Public/Export-Excel.ps1`](https://github.com/dfinke/ImportExcel/blob/5387c061461c811d106b125588f064c4739342cb/Public/Export-Excel.ps1) — Export-Excel is the main composition path: it opens or creates a package, infers pipeline properties and cell types, writes data, applies tables and formatting, adds charts or pivots, and saves or returns the workbook.

**Why this level:**

- **S2:** 4,341 meaningful implementation LOC measured with tokei 14.0.0. Count covers production PowerShell in Public, Private, Charting, Pivot, and the module loader; tests, examples, binary dependencies, documentation, and package metadata are excluded.
- **D3:** Correct output depends on a large third-party object model and many spreadsheet-specific rules, though the algorithms themselves remain conventional.
- **C3:** A report can combine several document subsystems and resource lifecycles, but execution stays within one process and one workbook model.
- **Placement:** S2/D3/C3 averages to 2.67 and rounds upward, making ImportExcel an SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** Public commands separate workbook concerns into helpers, handle null and type distinctions explicitly, and make package ownership and save behavior configurable.
- **Architecture:** Public pipeline commands coordinate package helpers; charting, pivot, formatting, validation, and worksheet operations wrap focused regions of the EPPlus object model.
- **Naming and idiom:** Import-Excel, Export-Excel, Open-ExcelPackage, Add-ExcelChart, New-PivotTableDefinition, Set-ExcelRange, and Close-ExcelPackage mirror workbook operations.
- **Tests:** Pester suites create and reopen real xlsx artifacts to verify rows, columns, values, formats, formulas, ranges, worksheets, charts, pivots, protection, validation, imports, and performance bounds.
- **Documentation:** The README and example collection show installation, one-line exports, charts, pivots, conditional formatting, SQL workflows, and the richer API surface.
- **Traceability:** A pipeline property can be followed through discovery and type conversion into a worksheet cell, table or chart range, saved package, reopened workbook, and exact artifact assertion.
- **Maintainability:** Spreadsheet features are partitioned into domain-named commands, compatibility decisions stay at the EPPlus boundary, and output tests detect document regressions.
- **Educational value:** It teaches how a dynamic shell can provide an ergonomic facade over a complex document API without hiding the underlying workbook lifecycle.

**Inspection record:** commit `5387c061461c811d106b125588f064c4739342cb`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Public/Export-Excel.ps1`, `Public/Import-Excel.ps1`, `Public/Add-ExcelChart.ps1`, `Pivot/Pivot.ps1`, `__tests__/Export-Excel.Tests.ps1`, `__tests__/ImportExcelTests/Simple.tests.ps1`, `LICENSE.txt`. GitHub Linguist label: PowerShell. LOC exclusions: __tests__/, Examples/, bundled EPPlus binaries, documentation and build files.

**License:** [Apache-2.0](https://github.com/dfinke/ImportExcel/blob/5387c061461c811d106b125588f064c4739342cb/LICENSE.txt)

### [ScoopInstaller/Scoop](https://github.com/ScoopInstaller/Scoop)

**S2 / D3 / C3 → SDC 3**

A command-line package manager for Windows that installs applications from declarative manifests with dependency resolution, verified downloads, extraction, shims, persistence, and reversible environment changes.

**Real-world evidence:** Scoop is an actively maintained installer used with public application buckets, and the project documents repeatable user-level installation and package-author workflows.

**Language evidence:** Manifest resolution, dependency traversal, downloads, hash verification, extraction, installation hooks, shims, persistence, environment changes, updates, and tests are implemented in PowerShell.

**Why study it:** Its source exposes the concrete lifecycle behind a package manager: find a manifest, resolve a dependency graph, select architecture-specific data, fetch and verify artifacts, extract them, run constrained hooks, create shims, persist data, and record installation state.

**What you can learn:**

- Command dispatch, JSON manifests, recursive dependency resolution, cycle detection, architecture selection, HTTP downloads, hashes and cache policy, archive extraction, install hooks, path containment, shims, persistent data, environment mutation, rollback concerns, and mocked integration tests.

**Prerequisites:**

- PowerShell scripting, JSON, recursive graph traversal, web requests, checksums, archives, Windows paths and environment variables, symbolic links or junctions, and package-manager concepts.

**Start here:** [`lib/install.ps1`](https://github.com/ScoopInstaller/Scoop/blob/b588a06e41d920d2123ec70aee682bae14935939/lib/install.ps1) — install_app composes manifest selection, download and verification, extraction, hooks, installer execution, shims, shortcuts, modules, environment changes, persistence, and installation records; lib/depends.ps1 supplies the preceding graph step.

**Why this level:**

- **S2:** 7,302 meaningful implementation LOC measured with tokei 14.0.0. Count covers Scoop's production PowerShell under lib, libexec, and bin/scoop.ps1 and excludes tests, fixtures, external bucket manifests, documentation, and release metadata.
- **D3:** Package installation crosses security-sensitive filesystem, network, archive, process, and environment boundaries with architecture- and manifest-dependent branches.
- **C3:** A normal install traverses several cooperating components and durable state transitions, but the system remains a single-machine command-line application.
- **Placement:** S2/D3/C3 averages to 2.67 and rounds upward, making Scoop an SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** Lifecycle steps are separate functions, path escape is checked before installer execution, hashes are first-class, and manifest-dependent mutations are visible.
- **Architecture:** Command scripts call shared libraries for manifest interpretation, dependencies, downloads, extraction, installation, shims, persistence, configuration, and updates.
- **Naming and idiom:** Get-Dependency, Get-Manifest, Invoke-ScoopDownload, Invoke-Extraction, Invoke-Installer, create_shims, persist_data, and save_install_info reveal the package lifecycle.
- **Tests:** Pester suites cover manifests, dependency order and cycles, helper selection, downloads, hashes, archives, install definitions, containment, shims, persistence, configuration, command dispatch, and regressions.
- **Documentation:** The README explains user behavior and installation, while the maintained wiki and contributing material cover manifests, buckets, configuration, and package authoring.
- **Traceability:** A package name can be followed from command dispatch into manifest selection, dependency expansion, verified download, extraction, installation mutations, saved metadata, and targeted tests.
- **Maintainability:** Manifest policy is separated from execution helpers, functions are organized by domain, and broad fixture-driven tests protect the supported package shapes.
- **Educational value:** It is a readable production package manager that makes operational and trust boundaries visible instead of reducing installation to a download command.

**Inspection record:** commit `b588a06e41d920d2123ec70aee682bae14935939`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `lib/depends.ps1`, `lib/download.ps1`, `lib/manifest.ps1`, `lib/install.ps1`, `test/Scoop-Depends.Tests.ps1`, `test/Scoop-Install.Tests.ps1`, `LICENSE`. GitHub Linguist label: PowerShell. LOC exclusions: test/, bucket and fixture data, documentation, installer bootstrap repository, build and release files.

**License:** [Unlicense OR MIT](https://github.com/ScoopInstaller/Scoop/blob/b588a06e41d920d2123ec70aee682bae14935939/LICENSE)

## SDC 4

### [dataplat/dbatools](https://github.com/dataplat/dbatools)

**S4 / D4 / C4 → SDC 4**

A broad PowerShell automation toolkit for administering and migrating SQL Server estates, from connections and configuration through backup, restore, availability, security, diagnostics, and cloud workflows.

**Real-world evidence:** dbatools is released as a PowerShell module for database administrators and documents production operations across SQL Server instances, migrations, disaster recovery, security, and estate management.

**Language evidence:** SQL Server discovery, connections, migrations, backup and restore, availability, security, performance, configuration, messaging, background maintenance, and the test corpus are predominantly PowerShell.

**Why study it:** The project demonstrates how a large operational toolkit builds consistent command contracts over a complex external platform while centralizing connections, configuration, messaging, types, runspaces, safety behavior, and test infrastructure.

**What you can learn:**

- Large PowerShell module architecture, advanced command contracts, SQL Management Objects, connection reuse, credentials and encryption, backup and restore planning, ShouldProcess, configuration persistence, typed output, background runspaces, structured messaging, remote operations, cloud storage, integration fixtures, and operational failure handling.

**Prerequisites:**

- Advanced PowerShell, SQL Server administration, SMO, credentials and connection strings, T-SQL, backup and recovery concepts, remoting, concurrency, configuration systems, and large integration suites.

**Start here:** [`public/Connect-DbaInstance.ps1`](https://github.com/dataplat/dbatools/blob/0473789e928c8e9e7d891770c95cfcfa76724d3e/public/Connect-DbaInstance.ps1) — Connect-DbaInstance introduces the common input, credential, encryption, connection-reuse, SMO, error, and output conventions that many commands share; Backup-DbaDatabase then shows those conventions driving a state-changing workflow.

**Why this level:**

- **S4:** 104,547 meaningful implementation LOC measured with tokei 14.0.0. Count covers production PowerShell in public, private, and dbatools.psm1; tests, binary dependencies, documentation, generated help, and build metadata are excluded.
- **D4:** Individual commands must encode expert database operations and failure policy across versions and environments, although they build on established SQL Server APIs rather than implementing a database engine.
- **C4:** Real workflows cross many shared services and external systems, but the repository remains a modular administration toolkit rather than a database or distributed runtime itself.
- **Placement:** S4/D4/C4 averages to 4.00, making dbatools an SDC 4 project.

**Quality-gate evidence:**

- **Source quality:** Commands expose safety switches, return domain objects, centralize connection and messaging behavior, and document operational caveats close to parameters and branches.
- **Architecture:** Public commands express administrator workflows; private functions centralize platform mechanics; shared configuration, types, connection caches, messages, and runspaces enforce module-wide conventions.
- **Naming and idiom:** Connect-DbaInstance, Backup-DbaDatabase, Restore-DbaDatabase, Test-DbaConnection, Write-Message, Register-DbaRunspace, and Get-DbatoolsConfig map to administrator intent.
- **Tests:** Unit, integration, compliance, and hardening suites exercise command contracts, supported SQL versions, real instances, backup and restore states, migrations, configuration, safety behavior, and regression scenarios.
- **Documentation:** Each public command carries extensive help and examples, and the maintained site organizes installation, command reference, concepts, migration paths, and contribution guidance.
- **Traceability:** A backup request can be followed from parameter validation through connection acquisition, database selection, path and option planning, generated SMO or T-SQL work, verification, typed history output, and integration cleanup.
- **Maintainability:** Shared infrastructure avoids repeating connection and error policy, commands remain domain-focused, compliance tests enforce conventions, and integration fixtures model actual server state.
- **Educational value:** It is a strong advanced example of turning deep operational expertise into a consistent, safe, discoverable automation surface.

**Inspection record:** commit `0473789e928c8e9e7d891770c95cfcfa76724d3e`, reviewed 2026-08-28 by Codex. Files sampled: `readme.md`, `dbatools.psm1`, `public/Connect-DbaInstance.ps1`, `public/Backup-DbaDatabase.ps1`, `public/Restore-DbaDatabase.ps1`, `private/functions/runspaces/Register-DbaRunspace.ps1`, `private/functions/configuration/Read-DbatoolsConfigFile.ps1`, `tests/Backup-DbaDatabase.Tests.ps1`, `license`. GitHub Linguist label: PowerShell. LOC exclusions: tests/, bin/ and bundled assemblies, docs and website material, build and release files.

**License:** [MIT](https://github.com/dataplat/dbatools/blob/0473789e928c8e9e7d891770c95cfcfa76724d3e/license)

### [pester/Pester](https://github.com/pester/Pester)

**S3 / D5 / C4 → SDC 4**

PowerShell's test and mock framework, with a discovery and execution runtime, assertions, scope-aware mocks, filtering, plugins, code coverage, parallel containers, and CI result formats.

**Real-world evidence:** Pester is the standard PowerShell testing framework, is distributed through the PowerShell Gallery, ships with older Windows installations, and integrates with editors and continuous-integration systems.

**Language evidence:** Test discovery and execution, nested scopes, hooks, assertions, mocking, filtering, output and result formats, code coverage integration, parallel orchestration, and supporting runtime types are implemented in PowerShell and first-party C#.

**Why study it:** The repository reveals how a language-native test DSL becomes a real runtime: script discovery, nested block trees, user-scope execution, setup and teardown, assertion dispatch, command interception, result modeling, tracing, reporting, and parallel isolation.

**What you can learn:**

- Test discovery versus execution, runtime trees, scriptblock session state, reflection over PowerShell internals, nested setup and teardown, plugin hooks, assertion protocols, command mocking, parameter filters, code-coverage tracing, parallel runspaces, result formats, and self-hosting tests.

**Prerequisites:**

- Expert PowerShell scopes and session state, scriptblocks and ASTs, reflection, command resolution, mocking semantics, concurrency and runspaces, tracing, test-runner architecture, and C# interoperability.

**Start here:** [`src/Pester.Runtime.ps1`](https://github.com/pester/Pester/blob/bfcbd4d2b0fc5e89d058f59da19feabf853d33c2/src/Pester.Runtime.ps1) — Pester.Runtime.ps1 constructs block and test objects, separates discovery from execution, moves between user and framework scopes, invokes hooks and plugins, filters work, records results, and hands containers to higher-level orchestration.

**Why this level:**

- **S3:** 21,665 meaningful implementation LOC measured with tokei 14.0.0. Count covers 16,582 production PowerShell lines and 5,083 first-party C# lines under src, including the runtime, mocks, assertions, reporting, configuration, tracing, and result types; tests, documentation, examples, and build metadata are excluded.
- **D5:** Core correctness depends on expert knowledge of PowerShell's runtime, scope ownership, command resolution, reflection, tracing, and concurrent isolation.
- **C4:** A test run crosses many coordinated subsystems and representations, while remaining one developer-tool platform rather than a distributed service.
- **Placement:** S3/D5/C4 averages to 4.00; the D5 floor also prevents placement below level 4, making Pester an SDC 4 project.

**Quality-gate evidence:**

- **Source quality:** Runtime state, domain types, plugin steps, timers, and result conversion are explicit; delicate scope manipulation is documented and tested, though the core appropriately assumes advanced readers.
- **Architecture:** DSL commands create a block tree; the runtime discovers and executes it; plugins attach mocks, coverage, and output; C# types carry stable configuration and result models.
- **Naming and idiom:** Discover-Test, Invoke-ContainerRun, Invoke-TestItem, Invoke-InNewScriptScope, Get-MockPlugin, Should-Invoke, Coverage, and PesterConfiguration reveal lifecycle and ownership.
- **Tests:** Pester's extensive self-tests cover discovery, filtering, nested hooks, data-driven cases, scope movement, mocks, assertions, coverage, output formats, configuration, parallel containers, timing, failures, and regressions.
- **Documentation:** The README gives a production example and feature map, while the maintained documentation covers quick starts, assertions, mocks, configuration, coverage, CI, migration, and contribution internals.
- **Traceability:** A Describe and It pair can be followed from DSL registration into block objects, discovery filters, scoped execution, assertion or mock plugins, result post-processing, output rendering, and focused runtime tests.
- **Maintainability:** Typed result and configuration models constrain the public contract, plugins isolate cross-cutting features, and deep self-hosting suites guard runtime behavior across supported PowerShell versions.
- **Educational value:** It is an advanced study of implementing a testing language inside the language being tested, including the runtime seams that simple test examples conceal.

**Inspection record:** commit `bfcbd4d2b0fc5e89d058f59da19feabf853d33c2`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/Pester.Runtime.ps1`, `src/Pester.RSpec.ps1`, `src/functions/Pester.SessionState.Mock.ps1`, `src/csharp/Pester/Tracing/CodeCoverageTracer.cs`, `tst/Pester.Runtime.ts.ps1`, `tst/Pester.Mock.RSpec.ts.ps1`, `tst/Pester.RSpec.Parallel.ts.ps1`, `LICENSE`. GitHub Linguist label: PowerShell. LOC exclusions: tst/, docs/ and examples, build and release files.

**License:** [Apache-2.0](https://github.com/pester/Pester/blob/bfcbd4d2b0fc5e89d058f59da19feabf853d33c2/LICENSE)

## SDC 5

### [Badgerati/Pode](https://github.com/Badgerati/Pode)

**S3 / D5 / C5 → SDC 5**

A cross-platform PowerShell application-server framework with its own asynchronous HTTP, WebSocket, server-sent events, TCP, SMTP, file-watcher, and TLS runtime plus routing, middleware, authentication, sessions, OpenAPI, schedules, and serverless adapters.

**Real-world evidence:** Pode is released through the PowerShell Gallery, Chocolatey, and Docker and documents production hosting for APIs, sites, protocol servers, serverless functions, and container deployments.

**Language evidence:** Server lifecycle, routing, middleware, authentication, sessions, OpenAPI, scheduling, MCP, and runspace orchestration are PowerShell, while first-party C# implements asynchronous listeners, sockets, HTTP, TCP, SMTP, WebSocket, TLS, concurrent structures, and transport logging.

**Why study it:** Pode is the smallest project in the catalog that still exposes a full server platform: sockets and request strategies, asynchronous listeners, concurrent runspaces, protocol contexts, middleware, routing, security, state, schedules, documentation generation, and multiple hosting modes.

**What you can learn:**

- Asynchronous sockets, HTTP request and response handling, TCP and SMTP strategies, TLS, WebSockets and server-sent events, cancellation tokens, runspace pools, concurrent collections, routing, middleware, sessions, authentication and authorization, OpenAPI, cron schedules, serverless adapters, logging, and end-to-end protocol tests.

**Prerequisites:**

- Expert PowerShell and C#, asynchronous I/O, sockets and TLS, HTTP and WebSocket protocols, SMTP and TCP servers, concurrency and cancellation, runspaces, web security, authentication, OpenAPI, and application-server architecture.

**Start here:** [`src/Private/PodeServer.ps1`](https://github.com/Badgerati/Pode/blob/512a99018dc13027de2d746d5467c4d39a9401b2/src/Private/PodeServer.ps1) — PodeServer selects endpoints, configures the C# listeners, creates request runspaces, builds each WebEvent, applies middleware and routes, writes responses, and coordinates cancellation; the Listener subtree provides the transport implementation beneath it.

**Why this level:**

- **S3:** 49,408 meaningful implementation LOC measured with tokei 14.0.0. Count covers 41,540 production PowerShell lines and 7,868 first-party C# lines under src, including the listener and transport runtime; tests, examples, documentation, generated distribution output, third-party assets, and build metadata are excluded.
- **D5:** The main path combines expert protocol, concurrency, runtime, lifecycle, and security work rather than delegating the server engine to an external web framework.
- **C5:** Pode is a platform whose normal behavior crosses multiple independently meaningful subsystems, execution models, and protocol-specific state machines.
- **Placement:** S3/D5/C5 triggers the two-dimensions-at-5 rule, making Pode an SDC 5 project despite remaining below the S5 size band.

**Quality-gate evidence:**

- **Source quality:** Transport and protocol types are explicit, cancellation flows through listener APIs, PowerShell orchestration separates event construction from middleware and routes, and subtle boundaries carry targeted error handling.
- **Architecture:** C# listener adapters and request strategies own sockets and protocol I/O; PowerShell server loops construct events and invoke middleware, routes, security, state, schedules, and response helpers through shared context.
- **Naming and idiom:** PodeHttpListener, PodeSocket, PodeRequestStrategy, Start-PodeWebServer, WebEvent, Invoke-PodeMiddleware, Add-PodeRoute, and Close-PodeDisposable expose the runtime path.
- **Tests:** Unit, integration, compliance, and performance suites cover HTTP and HTTPS, WebSockets, authentication, sessions, routes, endpoints, OpenAPI 3.0 and 3.1, schedules, timers, serverless contexts, security, headers, state, and shutdown.
- **Documentation:** The README provides a minimal server and feature map, and the maintained documentation spans tutorials, protocols, hosting, middleware, security, OpenAPI, schedules, deployment, and internals.
- **Traceability:** An incoming socket can be followed through a protocol listener and request strategy into a WebEvent, middleware, authentication, route logic, response encoding, connection completion, and a live integration test.
- **Maintainability:** Protocol-specific C# types isolate byte-level concerns, PowerShell modules partition server features, cancellation and disposal have shared primitives, and integration suites verify cross-layer contracts.
- **Educational value:** It provides an unusually transparent advanced path from application-server ergonomics down to the network and concurrency mechanisms that implement them.

**Inspection record:** commit `512a99018dc13027de2d746d5467c4d39a9401b2`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/Private/PodeServer.ps1`, `src/Private/Runspaces.ps1`, `src/Private/TcpServer.ps1`, `src/Private/WebSockets.ps1`, `src/Private/MCP.ps1`, `src/Listener/Protocols/Http/PodeHttpListener.cs`, `src/Listener/Protocols/Smtp/PodeSmtpRequestStrategy.cs`, `src/Listener/Transport/Sockets/PodeSocket.cs`, `tests/integration/WebSocket.Tests.ps1`, `tests/integration/Authentication.Tests.ps1`, `tests/integration/OpenApi.Tests.ps1`, `LICENSE.txt`. GitHub Linguist label: PowerShell. LOC exclusions: tests/, examples/, docs/, generated module output, bundled third-party web assets, build and release files.

**License:** [MIT](https://github.com/Badgerati/Pode/blob/512a99018dc13027de2d746d5467c4d39a9401b2/LICENSE.txt)

### [Microsoft365DSC/Microsoft365DSC](https://github.com/Microsoft365DSC/Microsoft365DSC)

**S5 / D5 / C5 → SDC 5**

A Desired State Configuration platform that deploys, extracts, compares, reports, and monitors configuration across Microsoft 365, Azure, Entra ID, Exchange, Intune, Teams, SharePoint, Security and Compliance, Power Platform, and related workloads.

**Real-world evidence:** Microsoft365DSC is released as a PowerShell module for organizations to manage tenant configuration through DSC, and the repository runs workload-specific unit and integration pipelines against its broad resource catalog.

**Language evidence:** Hundreds of Desired State Configuration resources, tenant extraction, authentication, workload orchestration, drift comparison, export, monitoring, telemetry, dependency handling, and tests are PowerShell, with first-party C# comparison, conversion, cache, connection, and Intune helpers.

**Why study it:** The repository shows configuration management at platform scale: normalize many cloud APIs into get, test, set, and export contracts; support several authentication modes; compare nested desired state; order dependencies; parallelize extraction; generate portable configuration; and test hundreds of resources.

**What you can learn:**

- PowerShell Desired State Configuration resources, cloud control-plane APIs, Microsoft Graph, workload-specific cmdlets, delegated and application authentication, certificates and managed identity, reverse configuration extraction, nested state normalization and comparison, dependency graphs, parallel export, configuration drift, telemetry, code generation, and large mocked plus live test matrices.

**Prerequisites:**

- Expert PowerShell and C#, DSC resource contracts, Microsoft 365 administration, Microsoft Graph and service APIs, OAuth application and delegated authentication, certificates, cloud configuration management, schema-driven comparison, concurrency, and very large modular systems.

**Start here:** [`Modules/Microsoft365DSC/Modules/M365DSCReverse.psm1`](https://github.com/Microsoft365DSC/Microsoft365DSC/blob/f79f29719b824fd534d51839f87f728cf83d64d1/Modules/Microsoft365DSC/Modules/M365DSCReverse.psm1) — Start-M365DSCConfigurationExtract shows the platform-level path: validate the tool, resolve workloads and resources, select authentication, build dependencies and configuration data, export resources sequentially or in parallel, validate output, and emit statistics.

**Why this level:**

- **S5:** 399,138 meaningful implementation LOC measured with tokei 14.0.0. Count covers 394,750 production PowerShell lines under Modules/Microsoft365DSC and 4,388 first-party C# lines under src for comparison, conversion, caching, connections, utilities, and Intune export; tests, examples, documentation, binaries, and build metadata are excluded.
- **D5:** Correctness requires expert knowledge across DSC, identity, cloud APIs, authentication, schema comparison, concurrency, and many Microsoft 365 workloads.
- **C5:** A tenant configuration is a platform-scale graph spanning many APIs, authentication contexts, resource schemas, state transitions, and output artifacts.
- **Placement:** S5/D5/C5 triggers the two-dimensions-at-5 rule and makes Microsoft365DSC an SDC 5 project.

**Quality-gate evidence:**

- **Source quality:** Resource contracts and shared helpers make a vast surface navigable, while typed C# normalizers and comparers reduce repeated dynamic-object logic; the scale also exposes ordinary local defects, so learners should study representative paths rather than assume uniform perfection.
- **Architecture:** DSC resources implement workload state; shared modules own authentication, export, comparison, telemetry, dependencies, and utilities; C# libraries normalize and compare complex objects and accelerate repeated policy transformations.
- **Naming and idiom:** Get-TargetResource, Test-TargetResource, Set-TargetResource, Start-M365DSCConfigurationExtract, Compare-M365DSCResourceState, ResourceComparer, and New-M365DSCConnection expose the convergence model.
- **Tests:** Hundreds of Pester suites mock workload APIs for present, absent, drift, update, export, and authentication cases, while QA and workload-specific integration pipelines check schemas, manifests, examples, and live service behavior.
- **Documentation:** The README establishes deployment and licensing constraints, and the project site and generated resource references cover setup, authentication, workloads, exports, monitoring, examples, and each DSC contract.
- **Traceability:** An AADGroup declaration can be followed through connection creation, Graph retrieval and batching, normalized current state, comparison, create or update operations, export formatting, and mocked present, absent, and drift tests.
- **Maintainability:** Uniform DSC contracts, generated schema metadata, shared authentication and comparison layers, workload partitions, QA checks, and broad automated suites make coordinated changes possible across hundreds of resources.
- **Educational value:** It is an advanced study of how one configuration-management model is adapted across a heterogeneous cloud suite while retaining convergence, export, and audit semantics.

**Inspection record:** commit `f79f29719b824fd534d51839f87f728cf83d64d1`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Modules/Microsoft365DSC/Modules/M365DSCReverse.psm1`, `Modules/Microsoft365DSC/Modules/M365DSCCompare.psm1`, `Modules/Microsoft365DSC/Modules/M365DSCExportUtil.psm1`, `Modules/Microsoft365DSC/DscResources/MSFT_AADGroup/MSFT_AADGroup.psm1`, `src/Microsoft365DSC.Compare/ResourceComparer.cs`, `src/Microsoft365DSC.Intune/SettingCatalogPolicyExporter.cs`, `Tests/Unit/Microsoft365DSC/Microsoft365DSC.AADGroup.Tests.ps1`, `LICENSE`. GitHub Linguist label: PowerShell. LOC exclusions: Tests/, generator tests and generated documentation, examples and sample configurations, vendored module binaries, build and release files.

**License:** [MIT](https://github.com/Microsoft365DSC/Microsoft365DSC/blob/f79f29719b824fd534d51839f87f728cf83d64d1/LICENSE)

_Generated from `catalog/powershell.json`; do not edit by hand._

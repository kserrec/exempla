# Shell

10 qualified repositories. Scores assume the learner described in [the SDC rubric](../../docs/sdc.md).

[← All languages](../README.md)

## SDC 1

### [bats-core/bats-support](https://github.com/bats-core/bats-support)

**S1 / D2 / C1 → SDC 1**

A compact support library that supplies output and error helpers for reusable Bats test libraries.

**Real-world evidence:** The repository publishes a versioned Bats helper package intended to be loaded by other test libraries and suites.

**Language evidence:** Output formatting, error emission, caller detection, and the Bats load entry point are implemented in Bash under the repository root and src directory.

**Why study it:** Its tiny surface shows how a support library can make failure output consistent while preserving streams, prefixes, multiline values, and useful caller context.

**What you can learn:**

- Source-based shell libraries, caller-stack inspection, stdout and stderr discipline, multiline formatting, width calculation, prefixes and decoration, composable helpers, and Bats contracts.

**Prerequisites:**

- Bash functions and arrays, file descriptors, command substitution, sourcing, terminal output, and basic Bats usage.

**Start here:** [`src/output.bash`](https://github.com/bats-core/bats-support/blob/0954abb9925cad550424cebca2b99255d4eabe96/src/output.bash) — The output helpers form the largest behavior surface and connect directly to focused tests for line counting, alignment, prefixes, and multiline values.

**Why this level:**

- **S1:** 120 meaningful implementation LOC measured with tokei 14.0.0. Count covers load.bash and all production files under src/, excluding tests, documentation, and package metadata.
- **D2:** A few shell-specific details require care, but every helper is short, local, and named after its visible behavior.
- **C1:** The package has no service topology, persistence, or state beyond a caller's shell process.
- **Placement:** S1/D2/C1 averages to 1.33, making bats-support an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** Small functions keep formatting decisions explicit and use caller-controlled streams instead of hidden global output machinery.
- **Architecture:** The load file exposes independent language, output, and error modules that other Bats libraries can compose.
- **Naming and idiom:** batslib_err, batslib_count_lines, batslib_prefix, batslib_mark, and batslib_decorate state their output transformations directly.
- **Tests:** Individual Bats files exercise each helper with empty, single-line, multiline, marked, prefixed, aligned, and caller-sensitive cases.
- **Documentation:** The README explains the package's role, installation, loading, compatibility promise, and relationship to Bats helper libraries.
- **Traceability:** A formatted diagnostic can be followed from a public batslib helper through its line transformation and into one narrowly named test file.
- **Maintainability:** The tiny API, module separation, no runtime dependencies beyond Bash, and one-test-file-per-helper organization make changes easy to bound.
- **Educational value:** It is an approachable example of designing a reusable shell library instead of a one-off script.

**Inspection record:** commit `0954abb9925cad550424cebca2b99255d4eabe96`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `load.bash`, `src/output.bash`, `src/error.bash`, `src/lang.bash`, `test/50-output-16-batslib_print_kv_single_or_multi.bats`, `test/52-lang-10-batslib_is_caller.bats`, `LICENSE`. GitHub Linguist label: Shell. LOC exclusions: test/, README.md, package-lock.json.

**License:** [0BSD](https://github.com/bats-core/bats-support/blob/0954abb9925cad550424cebca2b99255d4eabe96/LICENSE)

### [fsaintjacques/semver-tool](https://github.com/fsaintjacques/semver-tool)

**S1 / D2 / C1 → SDC 1**

A small command-line utility for validating, comparing, inspecting, and incrementing Semantic Versioning 2.0 versions.

**Real-world evidence:** The repository publishes an executable release used directly from shell scripts, Git hooks, asdf, and bpkg workflows.

**Language evidence:** Semantic-version parsing, validation, precedence comparison, extraction, bumping, and command dispatch are implemented in one Bash program.

**Why study it:** One file turns a written specification into regex validation, structured comparison rules, transformations, and a practical command-line interface.

**What you can learn:**

- Specification-driven parsing, Bash regular expressions and capture groups, numeric versus lexical precedence, arrays, command dispatch, strict shell options, and table-like Bats tests.

**Prerequisites:**

- Bash functions, arrays and conditionals, regular-expression basics, command exit status, Semantic Versioning concepts, and shell test fundamentals.

**Start here:** [`src/semver`](https://github.com/fsaintjacques/semver-tool/blob/1a547a75f946717223fb7ca821ba6f3f337e9aca/src/semver) — The entire production path is visible in one file, from the SemVer grammar through comparison helpers to command dispatch.

**Why this level:**

- **S1:** 345 meaningful implementation LOC measured with tokei 14.0.0. Count covers the complete production Bash executable and excludes tests, documentation, and build metadata.
- **D2:** Semantic Versioning has meaningful edge cases, but the implementation follows the specification with direct functions and data flow.
- **C1:** There is no persistence, networking, plugin system, or multi-process architecture.
- **Placement:** S1/D2/C1 averages to 1.33, making semver-tool an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** Validation, comparison, prerelease handling, bumping, extraction, and dispatch are separated into short functions with strict shell failure settings.
- **Architecture:** A single executable holds pure comparison and transformation helpers behind a small command dispatcher.
- **Naming and idiom:** validate_version, compare_fields, bump_prerel, command_compare, and command_validate mirror the specification and CLI vocabulary.
- **Tests:** Bats suites cover every precedence example from the specification, invalid forms, build metadata, bumps, extraction, differences, documentation output, and argument errors.
- **Documentation:** The README explains installation, the complete command contract, version grammar, examples, integrations, development, and license.
- **Traceability:** A compare request can be followed through validation, captured components, release comparison, prerelease field ordering, and the corresponding Bats cases.
- **Maintainability:** One source file, strict options, focused helpers, specification-linked comments, ShellCheck, and broad behavior tests keep the contract auditable.
- **Educational value:** It demonstrates how to translate a compact public specification into a complete, tested shell tool.

**Inspection record:** commit `1a547a75f946717223fb7ca821ba6f3f337e9aca`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/semver`, `test/compare.bats`, `test/validate.bats`, `test/bump.bats`, `LICENSE`. GitHub Linguist label: Shell. LOC exclusions: test/, README.md, Makefile.

**License:** [Apache-2.0](https://github.com/fsaintjacques/semver-tool/blob/1a547a75f946717223fb7ca821ba6f3f337e9aca/LICENSE)

## SDC 2

### [ko1nksm/getoptions](https://github.com/ko1nksm/getoptions)

**S1 / D3 / C2 → SDC 2**

A portable POSIX-shell option parser and parser generator supporting short, long, optional, abbreviated, and subcommand forms.

**Real-world evidence:** The repository publishes standalone release scripts and a Homebrew package for shell programs that need a richer option grammar than getopts provides.

**Language evidence:** The portable option grammar, parser-code generator, abbreviation and help modules, and executable interfaces are implemented in POSIX shell.

**Why study it:** It is a concentrated lesson in what production portability costs: quoting, eval-based code generation, multiple scanning modes, validation hooks, help generation, and cross-shell workarounds.

**What you can learn:**

- POSIX shell portability, parser generation, safe quoting, eval and indirect variables, option grammars, scanning modes, subcommands, validation callbacks, ambiguity detection, and cross-shell testing.

**Prerequisites:**

- Strong POSIX shell fluency, quoting and expansion rules, eval, regular-expression and pattern matching, command-line conventions, and generated-code reasoning.

**Start here:** [`lib/getoptions_base.sh`](https://github.com/ko1nksm/getoptions/blob/139d121807db67f632b412b2a00ece851df73203/lib/getoptions_base.sh) — The base module builds the generated parser and exposes how definitions become initialization, token cases, validation, rest arguments, and errors.

**Why this level:**

- **S1:** 632 meaningful implementation LOC measured with tokei 14.0.0. Count covers authoring source under src/ and the production library modules under lib/, excluding tests, examples, documentation, and development tooling.
- **D3:** The source is small but materially abstract: readers must reason about shell code that emits and later evaluates other shell code across many implementations.
- **C2:** Several cohesive modules and delivery modes interact, but the result remains one local parser library with no external services.
- **Placement:** S1/D3/C2 averages to 2.00, making getoptions an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** The dense metaprogramming is purposeful, factored into small emitters, and guarded by explicit portability workarounds rather than accidental cleverness.
- **Architecture:** Definition collection feeds a base generator, with abbreviation and help behavior layered as optional modules and a separate generator CLI for delivery modes.
- **Naming and idiom:** setup, flag, param, option, disp, msg, prehook, validate, OPTARG, and OPTIND preserve familiar option-parser concepts.
- **Tests:** ShellSpec suites exercise scanning modes, combined flags, optional and required values, abbreviations, ambiguity, validation, subcommands, custom hooks, quoting, errors, and many supported shells.
- **Documentation:** The README compares getopt, getopts, and getoptions; documents the grammar and three delivery modes; and links detailed references and portability workarounds.
- **Traceability:** A declared option can be followed from the definition DSL through code emission, token matching, validation, assignment, and a matching ShellSpec context.
- **Maintainability:** Generated artifacts come from explicit source modules, portability decisions are documented, and broad multi-shell tests constrain changes to delicate quoting behavior.
- **Educational value:** It shows why line count alone cannot predict difficulty and gives advanced shell learners a bounded metaprogramming system to unpack.

**Inspection record:** commit `139d121807db67f632b412b2a00ece851df73203`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/getoptions`, `src/gengetoptions`, `lib/getoptions_base.sh`, `lib/getoptions_abbr.sh`, `spec/getoptions_base_spec.sh`, `spec/getoptions_abbr_spec.sh`, `LICENSE`. GitHub Linguist label: Shell. LOC exclusions: spec/, examples/, docs/, tools/.

**License:** [CC0-1.0](https://github.com/ko1nksm/getoptions/blob/139d121807db67f632b412b2a00ece851df73203/LICENSE)

### [rbenv/rbenv](https://github.com/rbenv/rbenv)

**S1 / D2 / C2 → SDC 2**

A per-user Ruby version manager that selects installations through PATH shims, directory-local version files, environment overrides, and plugins.

**Real-world evidence:** The repository ships the rbenv command installed by major operating-system package managers and used to select Ruby runtimes for projects and shells.

**Language evidence:** Command dispatch, version selection, shim generation, hook discovery, executable lookup, and shell initialization are implemented as Bash executables under libexec/.

**Why study it:** It solves runtime selection with ordinary filesystem and PATH mechanisms, making shims, precedence, command dispatch, locking, and plugin hooks visible without a daemon.

**What you can learn:**

- Unix command dispatch, PATH shims, configuration precedence, filesystem traversal, plugin hooks, shell initialization, atomic-ish lock files, executable discovery, and Bats integration tests.

**Prerequisites:**

- Bash arrays and parameter expansion, PATH lookup, files and symlinks, processes and exec, environment variables, shell startup files, and basic plugin concepts.

**Start here:** [`libexec/rbenv`](https://github.com/rbenv/rbenv/blob/07e9b1e297a5977298c6aadc9971ae0e9eb7f0dc/libexec/rbenv) — The dispatcher establishes roots and hook paths, discovers plugin commands, and execs the selected subcommand; every user operation starts there.

**Why this level:**

- **S1:** 1,142 meaningful implementation LOC measured with tokei 14.0.0. Count covers production command executables under libexec/ and excludes tests, documentation, completions, and optional build-time native-helper sources.
- **D2:** The mechanisms require Unix familiarity, but each command is a short executable with explicit inputs, filesystem operations, and exit behavior.
- **C2:** Several commands coordinate through a shared directory convention, but there is no daemon, database, network service, or distributed state.
- **Placement:** S1/D2/C2 averages to 1.67 and rounds upward, making rbenv an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** Commands are narrowly scoped, fail early, and make precedence and filesystem effects explicit.
- **Architecture:** One dispatcher locates rbenv-prefixed executables; small commands share environment conventions while hooks and plugin bin directories extend behavior.
- **Naming and idiom:** RBENV_ROOT, RBENV_DIR, rbenv-version-name, rbenv-version-origin, rbenv-rehash, and rbenv-which reveal both ownership and precedence.
- **Tests:** Bats suites cover each command, version precedence, missing installations, hook mutation, shim creation and cleanup, command lookup, initialization, completions, and regressions.
- **Documentation:** The README explains installation, commands, shims, version selection, shell integration, plugins, alternatives, and the full mechanism.
- **Traceability:** A Ruby invocation can be followed from the generated shim through rbenv exec, version-name precedence, prefix selection, executable lookup, and focused tests.
- **Maintainability:** One-command-per-file organization, stable naming conventions, plugin boundaries, and command-level tests localize changes.
- **Educational value:** It is a clear study of replacing a complex-seeming runtime manager with Unix path indirection and small cooperating scripts.

**Inspection record:** commit `07e9b1e297a5977298c6aadc9971ae0e9eb7f0dc`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `libexec/rbenv`, `libexec/rbenv-version-name`, `libexec/rbenv-rehash`, `libexec/rbenv-which`, `test/version-name.bats`, `test/rehash.bats`, `LICENSE`. GitHub Linguist label: Shell. LOC exclusions: test/, README.md, completions/, src/.

**License:** [MIT](https://github.com/rbenv/rbenv/blob/07e9b1e297a5977298c6aadc9971ae0e9eb7f0dc/LICENSE)

## SDC 3

### [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh)

**S3 / D3 / C4 → SDC 3**

A Zsh configuration framework with a core loader, shared libraries, themes, a management CLI, update machinery, and a large plugin ecosystem.

**Real-world evidence:** The repository distributes an installable interactive-shell framework whose plugins and themes integrate everyday developer tools and operating systems.

**Language evidence:** Framework loading, interactive-shell behavior, the omz CLI, update lifecycle, themes, completion definitions, and hundreds of plugins are implemented in Zsh and shell files.

**Why study it:** It shows how conventions, dynamic loading, shell-native data structures, completion, user configuration, and extension discovery can support a very broad ecosystem without a separate plugin runtime.

**What you can learn:**

- Zsh startup sequencing, autoload and completion, plugin discovery, theme loading, shell option isolation, command dispatch, update locking, terminal input, configuration rewriting, and convention-based extension systems.

**Prerequisites:**

- Strong Zsh fluency, interactive-shell startup, arrays and parameter flags, completion functions, Git, terminal modes, filesystem conventions, and plugin architecture basics.

**Start here:** [`oh-my-zsh.sh`](https://github.com/ohmyzsh/ohmyzsh/blob/4b657407c98bbc8830ae66c2ac7ff3d737c55a83/oh-my-zsh.sh) — The main loader validates configuration, builds function paths, selects plugins and themes, sources shared libraries, and reveals the framework's extension contract.

**Why this level:**

- **S3:** 31,265 meaningful implementation LOC measured with tokei 14.0.0. Count includes production Zsh, Bash, POSIX shell, and Python under the core loader, lib/, plugins/, themes/, and tools/; focused tests and non-code data are excluded.
- **D3:** Individual modules are usually direct, but recurring Zsh-specific semantics and interactive state require substantial prerequisites.
- **C4:** The framework is a large convention-driven ecosystem with many optional cross-cutting integrations, even though each user's runtime is one shell process.
- **Placement:** S3/D3/C4 averages to 3.33, making Oh My Zsh an SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** The core loader and CLI make order and side effects explicit, while most integrations stay in small plugin-local files.
- **Architecture:** A shared loader and library layer establishes conventions that independent plugins, completions, themes, tools, and the omz CLI follow.
- **Naming and idiom:** ZSH, ZSH_CUSTOM, plugins, fpath, _omz::plugin, _omz::theme, and zstyle use the shell's own vocabulary and scoping conventions.
- **Tests:** Focused Zsh tests cover core CLI configuration rewriting and plugin behavior, while repository automation checks syntax, formatting, metadata, and selected integration paths.
- **Documentation:** The README and plugin-local guides explain installation, configuration, plugins, themes, updates, safety, removal, and contribution paths.
- **Traceability:** Enabling a plugin can be followed from user configuration through loader discovery and sourcing into the plugin file, CLI mutation logic, and focused CLI tests.
- **Maintainability:** Directory conventions and local plugin ownership contain a very large extension set; core helpers and automated checks guard shared behavior.
- **Educational value:** It teaches how a dynamic language can scale an ecosystem primarily through naming and loading conventions rather than framework objects.

**Inspection record:** commit `4b657407c98bbc8830ae66c2ac7ff3d737c55a83`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `oh-my-zsh.sh`, `lib/cli.zsh`, `tools/check_for_upgrade.sh`, `lib/tests/cli.test.zsh`, `plugins/git/git.plugin.zsh`, `plugins/git/README.md`, `LICENSE.txt`. GitHub Linguist label: Shell. LOC exclusions: **/tests/, documentation, JSON and static data, repository metadata.

**License:** [MIT](https://github.com/ohmyzsh/ohmyzsh/blob/4b657407c98bbc8830ae66c2ac7ff3d737c55a83/LICENSE.txt)

### [pyenv/pyenv](https://github.com/pyenv/pyenv)

**S2 / D3 / C3 → SDC 3**

A Python version manager that selects installed runtimes through shims and can download and build many Python implementations.

**Real-world evidence:** The repository ships the pyenv command and bundled python-build plugin installed through common package managers and used for per-user and per-project Python selection.

**Language evidence:** Runtime selection, command dispatch, shims, hooks, shell setup, Python download and compilation, and binary packaging are implemented primarily in Bash.

**Why study it:** It extends the small shim pattern into a multi-plugin tool that must detect shells and platforms, resolve versions, fetch and verify source, compile runtimes, and preserve extensibility.

**What you can learn:**

- Command and hook architectures, PATH shims, version precedence, shell-specific initialization, portable platform detection, checksummed downloads, source builds, compiler configuration, plugin discovery, and integration testing.

**Prerequisites:**

- Comfortable Bash, Unix processes and PATH, build toolchains, checksums and archives, shell startup behavior, plugins, and basic C compilation.

**Start here:** [`libexec/pyenv`](https://github.com/pyenv/pyenv/blob/4733cca31b0f63eab95937f179584ba0d47d44d5/libexec/pyenv) — The dispatcher establishes installation and user roots, merges plugin command and hook paths, and routes every operation into the command suite.

**Why this level:**

- **S2:** 4,933 meaningful implementation LOC measured with tokei 14.0.0. Count covers the core command suite, runtime hooks, python-build and pyenv-binary production executables, and the small C realpath helper; version-definition data, tests, maintenance scripts, completions, and documentation are excluded.
- **D3:** Understanding the main path requires build-system and platform knowledge beyond shell syntax, with subtle quoting and failure behavior across operating systems.
- **C3:** Several subsystems and platform boundaries cooperate, although all work remains local to one machine and filesystem hierarchy.
- **Placement:** S2/D3/C3 averages to 2.67 and rounds upward, making pyenv an SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** Core commands preserve the rbenv-style single-purpose shape while build logic is divided into named download, verification, compiler, and install helpers.
- **Architecture:** The dispatcher and hook convention support a core command suite plus bundled python-build and binary plugins without folding every concern into one process.
- **Naming and idiom:** PYENV_ROOT, PYENV_VERSION, pyenv-rehash, pyenv-version-name, install_package, fetch_tarball, and build_package expose lifecycle and ownership.
- **Tests:** Core and plugin Bats suites cover dispatch, version precedence, shims, hooks, shell setup, downloads, caches, checksums, patches, compilers, installation, relocation, and failure cases.
- **Documentation:** The README explains setup, usage, shims, version resolution, plugins, shell behavior, build prerequisites, upgrading, and development.
- **Traceability:** Installing and selecting a runtime can be followed from dispatch through python-build definition resolution, verified source acquisition, compilation, installation, rehashing, and command lookup tests.
- **Maintainability:** Stable extension conventions, small core commands, separated build helpers, explicit compatibility branches, and broad Bats suites contain a large portability surface.
- **Educational value:** It forms a natural progression from a small shim manager to a production tool that owns runtime acquisition and cross-platform integration.

**Inspection record:** commit `4733cca31b0f63eab95937f179584ba0d47d44d5`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `libexec/pyenv`, `libexec/pyenv-init`, `libexec/pyenv-rehash`, `plugins/python-build/bin/python-build`, `test/rehash.bats`, `plugins/python-build/test/checksum.bats`, `LICENSE`. GitHub Linguist label: Shell. LOC exclusions: test/, plugins/**/test/, plugins/python-build/share/python-build/, plugins/python-build/scripts/, completions/, docs and media.

**License:** [MIT](https://github.com/pyenv/pyenv/blob/4733cca31b0f63eab95937f179584ba0d47d44d5/LICENSE)

## SDC 4

### [dokku/dokku](https://github.com/dokku/dokku)

**S4 / D4 / C4 → SDC 4**

A self-hosted platform as a service that builds, deploys, configures, networks, schedules, and serves applications on a user's server.

**Real-world evidence:** The repository publishes installable Dokku releases and packages for operating a multi-application deployment platform on supported Ubuntu and Debian hosts.

**Language evidence:** The command router and core deployment plugins are implemented in Bash, with substantial first-party Go modules extending application, builder, proxy, storage, Docker, and Kubernetes behavior.

**Why study it:** It shows shell as an orchestration language at platform scale, combining a plugin command bus with Docker builds, Git deployment, process lifecycle, proxies, storage, certificates, and optional Kubernetes scheduling.

**What you can learn:**

- Plugin command dispatch, privilege boundaries, Git receive deployments, buildpack and Dockerfile builders, container lifecycle, proxy configuration, persistent settings, application metadata, Bash and Go interoperability, Kubernetes clients, Helm templates, and end-to-end deployment tests.

**Prerequisites:**

- Advanced Bash and Go, Linux users and permissions, Git transport, Docker images and containers, reverse proxies, process models, storage and networking, Kubernetes and Helm basics, and deployment-system testing.

**Start here:** [`dokku`](https://github.com/dokku/dokku/blob/c712429b095e8bbd58029787b64a9f23f98cb5fb/dokku) — The top-level executable establishes host state and permissions, authenticates SSH commands, resolves aliases, and dispatches into the enabled plugin graph.

**Why this level:**

- **S4:** 50,388 meaningful implementation LOC measured with tokei 14.0.0. Count includes 14,656 production Bash lines and 35,732 production Go lines in the main executable and core plugins, excluding tests, templates, documentation, packaging, and release tooling.
- **D4:** Several systems domains and failure-prone boundaries recur in normal deployment flows and require substantial operational expertise.
- **C4:** Many interacting components and execution modes form a platform, while the default control plane remains centered on one Dokku host.
- **Placement:** S4/D4/C4 averages to 4.00, making Dokku an SDC 4 project.

**Quality-gate evidence:**

- **Source quality:** The router makes privilege and dispatch decisions visible, shell plugins remain command-focused, and newer Go packages use explicit inputs, outputs, and errors.
- **Architecture:** A common plugin protocol joins command modules for apps, Git, builders, schedulers, proxies, processes, storage, networking, certificates, and configuration.
- **Naming and idiom:** PLUGIN_PATH, execute_dokku_cmd, cmd-deploy, builder, scheduler, proxy, report, and trigger vocabulary maps directly to platform operations.
- **Tests:** ShellCheck, extensive Bats suites, Go tests, and deployment fixtures exercise commands, configuration, security boundaries, builders, proxies, schedulers, failures, and real example applications.
- **Documentation:** The repository and project documentation cover installation, architecture by feature, plugin development, commands, deployment paths, operations, upgrades, troubleshooting, and testing.
- **Traceability:** A Git push can be followed from SSH authorization and command routing through the Git plugin, source preparation, builder selection, scheduler deployment, proxy updates, and Bats deployment tests.
- **Maintainability:** Stable plugin boundaries, shared common helpers, typed Go modules, generated command metadata, and layered unit and deployment tests contain a broad platform surface.
- **Educational value:** It demonstrates where shell remains effective in a production platform and how typed modules can be introduced around increasingly complex integrations.

**Inspection record:** commit `c712429b095e8bbd58029787b64a9f23f98cb5fb`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `dokku`, `plugins/common/functions`, `plugins/git/functions`, `plugins/scheduler-k3s/functions.go`, `tests/unit/git_1.bats`, `docs/development/testing.md`, `LICENSE`. GitHub Linguist label: Shell. LOC exclusions: tests/, *_test.go, docs/, contrib/, debian/, plugin templates and static assets.

**License:** [MIT](https://github.com/dokku/dokku/blob/c712429b095e8bbd58029787b64a9f23f98cb5fb/LICENSE)

### [testssl/testssl.sh](https://github.com/testssl/testssl.sh)

**S3 / D4 / C4 → SDC 4**

A standalone command-line scanner for TLS protocols, ciphers, certificates, configuration weaknesses, and cryptographic vulnerabilities on many network services.

**Real-world evidence:** The repository publishes a directly executable scanner and official container used for local security assessment of TLS and STARTTLS endpoints.

**Language evidence:** Transport setup, TLS record construction and parsing, cipher and protocol discovery, vulnerability probes, certificate checks, rating, reporting, and CLI orchestration are implemented in Bash.

**Why study it:** It exposes an unusually deep systems program in shell: raw protocol bytes, OpenSSL fallbacks, socket I/O, certificate logic, security findings, multiple report formats, parallel scans, and portable execution.

**What you can learn:**

- TLS record and handshake parsing, Bash TCP sockets, OpenSSL integration, binary-to-text conversion, cipher and protocol enumeration, certificate trust and revocation, vulnerability probes, severity models, structured reporting, STARTTLS, and parallel scanning.

**Prerequisites:**

- Advanced Bash, TCP/IP and sockets, TLS handshakes and certificates, cryptographic vulnerability concepts, binary encodings, OpenSSL, structured output formats, and security-test interpretation.

**Start here:** [`testssl.sh`](https://github.com/testssl/testssl.sh/blob/853850e3f4433c7717035a84cfe873dd0e63dfd3/testssl.sh) — The single production program is organized into named sections; parse_cmd_line and initialize_engine lead into protocol discovery, certificate analysis, vulnerability probes, reporting, and mass-scan orchestration.

**Why this level:**

- **S3:** 21,416 meaningful implementation LOC measured with tokei 14.0.0. Count covers the production testssl.sh scanner and excludes tests, maintenance utilities, bundled OpenSSL binaries, documentation, and static protocol/reference data.
- **D4:** Low-level protocol behavior and security interpretation recur throughout the main path, and safe changes require deep TLS and shell knowledge.
- **C4:** Many scanning and reporting modes share cross-cutting connection, finding, severity, and output state inside one large executable.
- **Placement:** S3/D4/C4 averages to 3.67 and rounds upward, making testssl.sh an SDC 4 project.

**Quality-gate evidence:**

- **Source quality:** Although intentionally delivered as one large script, the file uses stable sectioning, descriptive functions, explicit status codes, and consistent finding/report helpers.
- **Architecture:** Initialization selects a socket or OpenSSL engine, reusable discovery state feeds specialized checks, and a shared output layer emits terminal and machine-readable findings.
- **Naming and idiom:** run_protocols, parse_tls_serverhello, determine_trust, run_heartbleed, run_starttls_injection, fileout, and run_mass_testing expose the security workflow.
- **Tests:** Pinned Perl suites verify help and syntax, baseline scans, socket versus OpenSSL behavior, protocol output, valid JSON and HTML, severity contracts, STARTTLS, certificate failures, revocation, and known public endpoints.
- **Documentation:** The README, man page, FAQ, coding convention, Docker guide, security policy, and test guide cover operation, internals, contribution, and risk boundaries.
- **Traceability:** A protocol or vulnerability finding can be followed from connection setup through byte parsing and detection logic into fileout severity records and baseline or endpoint tests.
- **Maintainability:** Coding conventions, shared output and transport helpers, baseline artifacts, multi-platform CI, and live behavior tests constrain a necessarily broad compatibility surface.
- **Educational value:** It is a rare inspectable example of implementing a security scanner close to the wire without hiding the protocol behind a high-level library.

**Inspection record:** commit `853850e3f4433c7717035a84cfe873dd0e63dfd3`, reviewed 2026-08-28 by Codex. Files sampled: `Readme.md`, `testssl.sh`, `Coding_Convention.md`, `t/10_baseline_ipv4_http.t`, `t/31_isJSON_valid.t`, `t/51_badssl.com.t`, `t/Readme.md`, `LICENSE`. GitHub Linguist label: Shell. LOC exclusions: t/, utils/, bin/, doc/, etc/, generated reports.

**License:** [GPL-2.0-only](https://github.com/testssl/testssl.sh/blob/853850e3f4433c7717035a84cfe873dd0e63dfd3/LICENSE)

## SDC 5

### [termux/termux-packages](https://github.com/termux/termux-packages)

**S4 / D5 / C5 → SDC 5**

The build system and package-recipe corpus that produces the Termux userland and repositories for multiple Android architectures.

**Real-world evidence:** This repository builds and validates the package repositories consumed by the Termux Android application and its package manager.

**Language evidence:** The build engine, toolchain setup, package metadata, dependency handling, validation, and active package and subpackage recipes are overwhelmingly implemented in Bash and POSIX shell.

**Why study it:** It is an expert study in porting a Unix userland onto Android: thousands of recipes feed a modular cross-build engine that configures NDK, libc, compilers, language toolchains, dependency graphs, patches, packaging, signing, and multi-architecture CI.

**What you can learn:**

- Cross-compilation, Android NDK and Bionic constraints, ABI and architecture flags, dependency graph traversal, reproducible builds, source verification, package recipes and subpackages, toolchain adapters for many languages, patch pipelines, repository assembly, CI artifact flow, and defensive path validation.

**Prerequisites:**

- Expert Bash, compiler and linker toolchains, Android NDK and ABI concepts, C and C++ build systems, multiple language package ecosystems, Debian packages and repositories, dependency resolution, containers, release engineering, and supply-chain security.

**Start here:** [`build-package.sh`](https://github.com/termux/termux-packages/blob/dd1290e0fc0912dae71ab8627ded804566d28e92/build-package.sh) — The primary entry point loads the build modules in lifecycle order, establishes architecture and toolchain state, resolves dependencies, runs package hooks, and produces repository artifacts.

**Why this level:**

- **S4:** 95,348 meaningful implementation LOC measured with tokei 14.0.0. Count conservatively includes active package and subpackage recipes plus the core build, utility, setup, and toolchain Shell and Python implementation; copied patch context, bundled source, static data, tests, and disabled recipes are excluded.
- **D5:** The normal learning path repeatedly crosses expert compiler, linker, ABI, operating-system, and packaging concerns rather than containing them in one optional subsystem.
- **C5:** The repository is an interconnected operating environment and release platform whose important behavior spans core orchestration, toolchains, thousands of recipes, CI, and package repositories.
- **Placement:** S4/D5/C5 triggers the two-dimensions-at-5 guardrail, making termux-packages an SDC 5 project.

**Quality-gate evidence:**

- **Source quality:** The large entry point delegates lifecycle stages to named modules, toolchain setup is separated by concern, and package recipes declare metadata before narrowly overriding hooks.
- **Architecture:** A common build engine owns state and stages; setup and toolchain modules adapt ecosystems; repository directories contribute package recipes; CI selects, lints, builds, and publishes architecture-specific artifacts.
- **Naming and idiom:** TERMUX_PKG variables, termux_step functions, termux_setup_toolchain, package build.sh files, subpackage hooks, and repository paths make the build protocol visible.
- **Tests:** Changed recipes are linted and built across aarch64, arm, i686, and x86_64; repository-health checks, dry-run simulations, validation scripts, and package-specific tests cover metadata, dependency, artifact, and runtime boundaries.
- **Documentation:** The README, contribution guide, developer wiki links, inline module contracts, package conventions, security policy, and workflow definitions orient both package maintainers and build-system contributors.
- **Traceability:** A package can be followed from its build.sh metadata into property validation, dependency resolution, source verification, toolchain setup, build hooks, package creation, CI selection, and architecture artifacts.
- **Maintainability:** Named lifecycle modules, shared validators, recipe conventions, automated linting, architecture matrices, and scoped package ownership control a very large heterogeneous surface.
- **Educational value:** It shows shell coordinating a real cross-compiled distribution where operating-system, compiler, and supply-chain concerns are inseparable from the code.

**Inspection record:** commit `dd1290e0fc0912dae71ab8627ded804566d28e92`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `LICENSE.md`, `build-package.sh`, `scripts/properties.sh`, `scripts/build/termux_step_get_dependencies.sh`, `scripts/build/toolchain/termux_setup_toolchain_29.sh`, `packages/bash/build.sh`, `scripts/bin/validation`, `.github/workflows/packages.yml`. GitHub Linguist label: Shell. LOC exclusions: tests and test payloads, disabled-packages/, sample/, *.patch and *.diff, bundled upstream helper source, static XML and data, documentation and CI-only tooling.

**License:** [Apache-2.0 AND LicenseRef-Package-Specific](https://github.com/termux/termux-packages/blob/dd1290e0fc0912dae71ab8627ded804566d28e92/LICENSE.md)

### [void-linux/void-packages](https://github.com/void-linux/void-packages)

**S5 / D4 / C5 → SDC 5**

The xbps-src build system and source-package collection used to build the Void Linux distribution across architectures and libc variants.

**Real-world evidence:** The repository is Void Linux's maintained source-package system; its templates and build engine produce distribution packages and are exercised by official continuous integration.

**Language evidence:** xbps-src, build stages, dependency resolution, chroot and environment adapters, hooks, build styles, architecture profiles, and 9,661 package templates are implemented as Bash or POSIX-shell programs.

**Why study it:** It combines a full source-package DSL with dependency solving, isolated build environments, cross compilation, reusable build styles, installation hooks, metadata generation, quality checks, and an operating-system-sized recipe corpus.

**What you can learn:**

- Source-package DSL design, staged builds, dependency graph resolution, chroots and namespaces, cross compilation, architecture and libc profiles, reusable build styles, package hooks and triggers, subpackages, repository metadata, package QA, and distribution CI.

**Prerequisites:**

- Expert Bash and POSIX shell, Linux build and packaging systems, dependency resolution, chroots and namespaces, cross toolchains, ELF and shared libraries, libc differences, package repositories, and operating-system release engineering.

**Start here:** [`xbps-src`](https://github.com/void-linux/void-packages/blob/876ee5650a22d8ef731e955dd1c629b962a329e3/xbps-src) — The public command establishes configuration and master directories, resolves targets and options, and dispatches into the common xbps-src build machinery.

**Why this level:**

- **S5:** 269,448 meaningful implementation LOC measured with tokei 14.0.0. Count includes 260,038 Shell lines in 9,661 extensionless srcpkgs/*/template files plus 9,410 core Shell lines in xbps-src, build helpers, profiles, build styles, chroot and container adapters, environments, hooks, wrappers, and shutils. Tokei classified templates through a temporary hard-linked mirror with only a .sh filename suffix; file contents were unchanged.
- **D4:** Several expert systems concerns recur across the build path, though the code favors explicit staged shell functions over unusually dense algorithms or concurrency.
- **C5:** Understanding distribution behavior requires following interactions across the core build engine, thousands of templates, architecture profiles, package hooks, dependency repositories, and CI.
- **Placement:** S5/D4/C5 averages to 4.67 and rounds upward, making void-packages an SDC 5 project.

**Quality-gate evidence:**

- **Source quality:** Build stages, dependency helpers, environments, hooks, styles, and templates follow stable conventions and keep package-specific overrides separate from shared machinery.
- **Architecture:** xbps-src dispatches into shutils and stage executables; build styles and hooks provide reusable lifecycle behavior; templates declare packages and subpackages; profiles specialize architecture and libc targets.
- **Naming and idiom:** XBPS variables, do_fetch through do_pkg stages, build_style, hostmakedepends, makedepends, checkdepends, vmove, and package functions expose the distribution model.
- **Tests:** Continuous integration lints changed templates, builds and runs package checks across native and cross targets with glibc and musl, compares artifacts, detects conflicts, and verifies dependent packages can be installed.
- **Documentation:** The README, comprehensive Manual, contribution guide, build-style and hook READMEs, inline stage contracts, and template examples document both package authorship and engine behavior.
- **Traceability:** A package can be followed from its template through target parsing, dependency resolution, environment setup, selected build style, stage hooks, checks, subpackage splitting, metadata scripts, package output, and CI installation validation.
- **Maintainability:** A strict template convention, reusable build styles, isolated hooks, lint tools, architecture matrices, and artifact comparisons let many maintainers evolve a distribution-sized corpus coherently.
- **Educational value:** It is a complete study of how a shell-based DSL and engine can build an operating system without obscuring the package lifecycle behind a separate language.

**Inspection record:** commit `876ee5650a22d8ef731e955dd1c629b962a329e3`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Manual.md`, `xbps-src`, `common/xbps-src/libexec/build.sh`, `common/xbps-src/shutils/build_dependencies.sh`, `common/hooks/post-install/04-create-xbps-metadata-scripts.sh`, `srcpkgs/bash/template`, `.github/workflows/build.yaml`, `common/travis/check-install.sh`, `COPYING`. GitHub Linguist label: Shell. LOC exclusions: srcpkgs/**/patches/, srcpkgs/**/files/, tests and fixtures, common/travis/, common/scripts/, documentation, package payload data.

**License:** [BSD-2-Clause](https://github.com/void-linux/void-packages/blob/876ee5650a22d8ef731e955dd1c629b962a329e3/COPYING)

_Generated from `catalog/shell.json`; do not edit by hand._

# Shell

6 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

[← All languages](../README.md)

## Level 1

No qualified learning path has been published at this level. Standards are not lowered to fill a slot.

## Level 2

### [bats-core/bats-support](https://github.com/bats-core/bats-support)

**Language 2 / Behavior 2 / Design 1 / Constraints 2 → Level 2**

A compact support library that supplies output and error helpers for reusable Bats test libraries.

**Why study it:** The selected output module shows how a small sourced Bash library keeps single-line and multiline diagnostics consistent while preserving prefixes, alignment, and caller-selected output streams.

**Prerequisites:**

- Basic familiarity with Shell functions, parameter expansion, quoting, pipelines, exit statuses, arrays where supported, and Bats-style tests.

**Concepts this path develops:**

- Sourced Bash modules and arrays.
- Empty, single-line, and multiline branches.
- Multiline alignment must remain stable.

**What you can learn:**

- Use `src/output.bash` to study sourced-library boundaries, line-oriented transformations, file-descriptor selection, prefix and mark composition, multiline alignment, and direct Bats contracts.

**Learning path:**

- **Goal:** Understand how a small sourced Bash library produces consistent single-line and multiline diagnostic output without losing stream or formatting contracts.
- **Start here:** [`src/output.bash`](https://github.com/bats-core/bats-support/blob/0954abb9925cad550424cebca2b99255d4eabe96/src/output.bash) — The output module contains the selected formatting behavior and connects directly to the focused single-line-versus-multiline Bats specification.
- **Then read:**
  - [`load.bash`](https://github.com/bats-core/bats-support/blob/0954abb9925cad550424cebca2b99255d4eabe96/load.bash)
  - [`src/error.bash`](https://github.com/bats-core/bats-support/blob/0954abb9925cad550424cebca2b99255d4eabe96/src/error.bash)
  - [`test/50-output-16-batslib_print_kv_single_or_multi.bats`](https://github.com/bats-core/bats-support/blob/0954abb9925cad550424cebca2b99255d4eabe96/test/50-output-16-batslib_print_kv_single_or_multi.bats)
  - [`README.md`](https://github.com/bats-core/bats-support/blob/0954abb9925cad550424cebca2b99255d4eabe96/README.md)
  - [`LICENSE`](https://github.com/bats-core/bats-support/blob/0954abb9925cad550424cebca2b99255d4eabe96/LICENSE)
- **Trace:** Start with line counting and batslib_print_kv_single_or_multi, follow prefixes, widths, multiline values, and selected file descriptors through the output helpers, then close with the narrowly named Bats cases and the load entry point.

**Why this level:**

- **Language technique 2:** Common professional Bash library and stream idioms shape the path without advanced abstraction.
- **Behavioral reasoning 2:** Formatting has meaningful local branches and mutable counters but no nonlocal lifecycle.
- **Design span 1:** The selected behavior stays within one focused unit.
- **Constraint burden 2:** Routine production formatting, stream, and error safeguards constrain the helper.
- **Placement:** The four scores 2/2/1/2 sum to 7; their arithmetic mean is 1.75 and rounds half-up to Level 2. The published result is Level 2.

**License:** 0BSD ([evidence 1](https://github.com/bats-core/bats-support/blob/0954abb9925cad550424cebca2b99255d4eabe96/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The repository publishes a versioned Bats helper package intended to be loaded by other test libraries and suites.

**Language evidence:** Output formatting, error emission, caller detection, and the Bats load entry point are implemented in Bash under the repository root and src directory.

**Coding relevance:**

The short testing-library context is subordinate to reusable lessons in sourced modules, arrays, line transforms, stream discipline, prefixes, alignment, and focused behavior contracts.

Required domain context:

- Bats helper libraries format diagnostic values and write them to caller-selected output streams.

**Eight-part quality gate:**

- **Source quality:** The selected helpers keep line counting, prefixing, marking, alignment, and stream selection in small visible transformations.
- **Architecture:** The load entry sources a narrow output module and a separate error module, keeping the selected formatting behavior composable without a hidden runtime.
- **Naming and idiom:** batslib_count_lines, batslib_prefix, batslib_mark, and batslib_print_kv_single_or_multi state their output transformations directly.
- **Tests:** The selected Bats specification closes empty, single-line, multiline, prefixed, marked, aligned, and alternate-file-descriptor behavior for batslib_print_kv_single_or_multi.
- **Documentation:** The README explains the package's purpose, installation, sourced loading model, compatibility promise, and relationship to other Bats helper libraries.
- **Traceability:** A key-value diagnostic can be followed through the selected output helpers into the narrowly named single-or-multiline Bats cases.
- **Maintainability:** The small sourced modules, explicit helper composition, and focused test file keep the selected output contract easy to bound.
- **Educational value:** This path is an approachable example of turning recurring shell-output conventions into a reusable, tested library.

**Inspection record:** commit `0954abb9925cad550424cebca2b99255d4eabe96`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/output.bash`, `load.bash`, `src/error.bash`, `test/50-output-16-batslib_print_kv_single_or_multi.bats`, `README.md`, `LICENSE`. GitHub Linguist label: Shell.

</details>

### [fsaintjacques/semver-tool](https://github.com/fsaintjacques/semver-tool)

**Language 2 / Behavior 2 / Design 1 / Constraints 3 → Level 2**

A small command-line utility for validating, comparing, inspecting, and incrementing Semantic Versioning 2.0 versions.

**Why study it:** Understand how a Bash command turns the Semantic Versioning grammar into validation, precedence comparison, extraction, and version transformations. The version grammar is stated in the program and README, and the bounded path teaches Bash regular-expression captures, array-based comparison, validation, transformation, and command dispatch without requiring specialist domain knowledge.

**Prerequisites:**

- Basic familiarity with Shell functions, parameter expansion, quoting, pipelines, exit statuses, arrays where supported, and Bats-style tests.
- Semantic Versioning orders major, minor, patch, and prerelease identifiers while ignoring build metadata for precedence.

**Concepts this path develops:**

- Bash regular expressions and BASH_REMATCH captures.
- Validation and command-error branches.
- The published SemVer grammar must be accepted exactly.

**What you can learn:**

- Study these transferable Shell mechanisms in `src/semver`: Bash regular expressions and BASH_REMATCH captures and arrays, parameter expansion, and indirect variable lookup.
- Trace these states and branches from `src/semver` through its selected supporting files: validation and command-error branches, numeric, lexical, missing-field, and prerelease ordering cases, and localized bump and extraction state.
- Identify these architectural responsibilities in the path beginning at `src/semver`: one production executable and focused helper functions behind one command dispatcher.
- Study these change constraints for the path beginning at `src/semver`: the published SemVer grammar must be accepted exactly, numeric and alphanumeric prerelease identifiers have different ordering, build metadata must not affect precedence, and bump and extraction commands must preserve the remaining contract.

**Learning path:**

- **Goal:** Understand how a Bash command turns the Semantic Versioning grammar into validation, precedence comparison, extraction, and version transformations.
- **Start here:** [`src/semver`](https://github.com/fsaintjacques/semver-tool/blob/1a547a75f946717223fb7ca821ba6f3f337e9aca/src/semver) — Begin with `src/semver` because it exposes how a Bash command turns the Semantic Versioning grammar into validation, precedence comparison, extraction, and version transformations.
- **Then read:**
  - [`test/compare.bats`](https://github.com/fsaintjacques/semver-tool/blob/1a547a75f946717223fb7ca821ba6f3f337e9aca/test/compare.bats)
  - [`test/validate.bats`](https://github.com/fsaintjacques/semver-tool/blob/1a547a75f946717223fb7ca821ba6f3f337e9aca/test/validate.bats)
  - [`test/bump.bats`](https://github.com/fsaintjacques/semver-tool/blob/1a547a75f946717223fb7ca821ba6f3f337e9aca/test/bump.bats)
  - [`README.md`](https://github.com/fsaintjacques/semver-tool/blob/1a547a75f946717223fb7ca821ba6f3f337e9aca/README.md)
  - [`LICENSE`](https://github.com/fsaintjacques/semver-tool/blob/1a547a75f946717223fb7ca821ba6f3f337e9aca/LICENSE)
- **Trace:** Start with SEMVER_REGEX and validate_version, follow BASH_REMATCH fields into compare_fields and compare_version, then trace bump and get dispatch; close with the exact precedence, invalid-version, and transformation cases in the three Bats suites.

**Why this level:**

- **Language technique 2:** These are meaningful professional Bash idioms, but substantial abstraction or advanced metaprogramming does not recur in the path.
- **Behavioral reasoning 2:** The path has meaningful branching and local state while remaining synchronous and easy to trace.
- **Design span 1:** The complete behavior remains one focused unit.
- **Constraint burden 3:** Several specification, compatibility, and command-contract guarantees constrain ordinary changes.
- **Placement:** The four scores 2/2/1/3 sum to 8; their arithmetic mean is 2.00 and rounds half-up to Level 2. The published result is Level 2.

**License:** Apache-2.0 ([evidence 1](https://github.com/fsaintjacques/semver-tool/blob/1a547a75f946717223fb7ca821ba6f3f337e9aca/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The repository publishes an executable release used directly from shell scripts, Git hooks, asdf, and bpkg workflows.

**Language evidence:** Semantic-version parsing, validation, precedence comparison, extraction, bumping, and command dispatch are implemented in one Bash program.

**Coding relevance:**

The version grammar is stated in the program and README, and the bounded path teaches Bash regular-expression captures, array-based comparison, validation, transformation, and command dispatch without requiring specialist domain knowledge.

Required domain context:

- Semantic Versioning orders major, minor, patch, and prerelease identifiers while ignoring build metadata for precedence.

**Eight-part quality gate:**

- **Source quality:** src/semver separates validation, field ordering, prerelease bumping, extraction, and dispatch into specification-named functions; compare, validate, and bump Bats suites directly cover precedence, invalid forms, transformations, metadata, and argument errors; the README documents the complete contract; and the pinned Apache-2.0 license, focused single-file architecture, direct trace, and maintained tests satisfy all eight quality dimensions.
- **Architecture:** The audited architecture of the path beginning at `src/semver` has these boundaries: one production executable and focused helper functions behind one command dispatcher.
- **Naming and idiom:** `src/semver` and its supporting files use these characteristic Shell mechanisms: Bash regular expressions and BASH_REMATCH captures and arrays, parameter expansion, and indirect variable lookup.
- **Tests:** Direct tests in `test/compare.bats`, `test/validate.bats`, and `test/bump.bats` cover these states and branches in the selected path: validation and command-error branches, numeric, lexical, missing-field, and prerelease ordering cases, and localized bump and extraction state.
- **Documentation:** `src/semver` and its selected supporting material document the contracts needed to understand how a Bash command turns the Semantic Versioning grammar into validation, precedence comparison, extraction, and version transformations.
- **Traceability:** Start with SEMVER_REGEX and validate_version, follow BASH_REMATCH fields into compare_fields and compare_version, then trace bump and get dispatch; close with the exact precedence, invalid-version, and transformation cases in the three Bats suites.
- **Maintainability:** Changes to the path beginning at `src/semver` are constrained by these audited guarantees: the published SemVer grammar must be accepted exactly, numeric and alphanumeric prerelease identifiers have different ordering, build metadata must not affect precedence, and bump and extraction commands must preserve the remaining contract.
- **Educational value:** Understand how a Bash command turns the Semantic Versioning grammar into validation, precedence comparison, extraction, and version transformations. The version grammar is stated in the program and README, and the bounded path teaches Bash regular-expression captures, array-based comparison, validation, transformation, and command dispatch without requiring specialist domain knowledge.

**Inspection record:** commit `1a547a75f946717223fb7ca821ba6f3f337e9aca`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/semver`, `test/compare.bats`, `test/validate.bats`, `test/bump.bats`, `README.md`, `LICENSE`. GitHub Linguist label: Shell.

</details>

## Level 3

### [dokku/dokku](https://github.com/dokku/dokku)

**Language 3 / Behavior 3 / Design 3 / Constraints 3 → Level 3**

A self-hosted platform as a service that builds, deploys, configures, networks, schedules, and serves applications on a user's server.

**Why study it:** Understand how Dokku resolves aliases and dispatches a command through enabled plugin subcommands and the legacy command protocol. The bounded execute_dokku_cmd trace needs only concise plugin-dispatch vocabulary and primarily teaches associative alias maps, argument adaptation, extension precedence, dynamic executable routing, compatibility fallback, and explicit exit semantics; Docker, Git deployment, proxies, certificates, and Kubernetes are excluded.

**Prerequisites:**

- Basic familiarity with Shell functions, parameter expansion, quoting, pipelines, exit statuses, arrays where supported, and Bats-style tests.
- Dokku commands are implemented by enabled plugins whose executable files follow a documented command and exit-status convention.

**Concepts this path develops:**

- Bash associative alias map and arrays.
- Alias, default, exact subcommand, colon subcommand, and legacy fallback states.
- New and legacy plugin protocols must remain compatible.

**What you can learn:**

- Study these transferable Shell mechanisms in `dokku`: Bash associative alias map and arrays, parameter-based plugin and subcommand decomposition, and dynamic executable dispatch through a framework convention.
- Trace these states and branches from `dokku` through its selected supporting files: alias, default, exact subcommand, colon subcommand, and legacy fallback states, implemented, not implemented, valid, and failed exit outcomes, and application argument and selected build-capture branches.
- Identify these architectural responsibilities in the path beginning at `dokku`: public command router, enabled-plugin filesystem boundary, new subcommand and legacy command protocols, and shared helper and Bats integration boundaries.
- Study these change constraints for the path beginning at `dokku`: new and legacy plugin protocols must remain compatible, resolution precedence and argument adaptation must be deterministic, reserved exit statuses must distinguish fallback, success, and failure, and unknown commands must fail through the public contract.

**Learning path:**

- **Goal:** Understand how Dokku resolves aliases and dispatches a command through enabled plugin subcommands and the legacy command protocol.
- **Start here:** [`dokku`](https://github.com/dokku/dokku/blob/c712429b095e8bbd58029787b64a9f23f98cb5fb/dokku) — Begin with `dokku` because it exposes how Dokku resolves aliases and dispatches a command through enabled plugin subcommands and the legacy command protocol.
- **Then read:**
  - [`plugins/common/functions`](https://github.com/dokku/dokku/blob/c712429b095e8bbd58029787b64a9f23f98cb5fb/plugins/common/functions)
  - [`tests/unit/core_2.bats`](https://github.com/dokku/dokku/blob/c712429b095e8bbd58029787b64a9f23f98cb5fb/tests/unit/core_2.bats)
  - [`tests/unit/plugin.bats`](https://github.com/dokku/dokku/blob/c712429b095e8bbd58029787b64a9f23f98cb5fb/tests/unit/plugin.bats)
  - [`docs/development/testing.md`](https://github.com/dokku/dokku/blob/c712429b095e8bbd58029787b64a9f23f98cb5fb/docs/development/testing.md)
  - [`README.md`](https://github.com/dokku/dokku/blob/c712429b095e8bbd58029787b64a9f23f98cb5fb/README.md)
  - [`LICENSE`](https://github.com/dokku/dokku/blob/c712429b095e8bbd58029787b64a9f23f98cb5fb/LICENSE)
- **Trace:** Start at execute_dokku_cmd, follow associative alias replacement, command and application argument adaptation, default, exact, and colon-subcommand executable lookup, then trace the legacy commands fan-out through not-implemented, valid, and error exits to the unknown-command result; close with core and plugin Bats cases. SSH authorization and deployment-platform breadth are excluded.

**Why this level:**

- **Language technique 3:** A substantial convention-driven plugin framework idiom materially shapes the path without recurring code generation or expert language machinery.
- **Behavioral reasoning 3:** The command lifecycle and extension fallback are nontrivial, while the bounded trace does not include advanced platform scheduling or recovery.
- **Design span 3:** Several meaningful routing, extension, compatibility, and verification boundaries cooperate.
- **Constraint burden 3:** Several extension, compatibility, ordering, and error guarantees constrain the dispatcher.
- **Placement:** The four scores 3/3/3/3 sum to 12; their arithmetic mean is 3.00 and rounds half-up to Level 3. The published result is Level 3.

**License:** MIT ([evidence 1](https://github.com/dokku/dokku/blob/c712429b095e8bbd58029787b64a9f23f98cb5fb/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The repository publishes installable Dokku releases and packages for operating a multi-application deployment platform on supported Ubuntu and Debian hosts.

**Language evidence:** The command router and core deployment plugins are implemented in Bash, with substantial first-party Go modules extending application, builder, proxy, storage, Docker, and Kubernetes behavior.

**Coding relevance:**

The bounded execute_dokku_cmd trace needs only concise plugin-dispatch vocabulary and primarily teaches associative alias maps, argument adaptation, extension precedence, dynamic executable routing, compatibility fallback, and explicit exit semantics; Docker, Git deployment, proxies, certificates, and Kubernetes are excluded.

Required domain context:

- Dokku commands are implemented by enabled plugins whose executable files follow a documented command and exit-status convention.

**Eight-part quality gate:**

- **Source quality:** The dokku executable names the command-routing phases and keeps plugin discovery explicit, plugins/common/functions provides shared logging and narrowly called helpers, core_2.bats directly verifies unknown-command behavior and invokes routed core commands, plugin.bats exercises plugin commands through the same public executable, the README and testing guide orient the command architecture, and the pinned MIT license, stable extension boundary, direct observable trace, and production purpose satisfy all eight quality dimensions.
- **Architecture:** The audited architecture of the path beginning at `dokku` has these boundaries: public command router, enabled-plugin filesystem boundary, new subcommand and legacy command protocols, and shared helper and Bats integration boundaries.
- **Naming and idiom:** `dokku` and its supporting files use these characteristic Shell mechanisms: Bash associative alias map and arrays, parameter-based plugin and subcommand decomposition, and dynamic executable dispatch through a framework convention.
- **Tests:** `tests/unit/core_2.bats` verifies unknown-command behavior and invokes routed core commands, while `tests/unit/plugin.bats` exercises plugin commands through the public `dokku` executable; `docs/development/testing.md` is supporting guidance, not a test suite.
- **Documentation:** `dokku` and its selected supporting material document the contracts needed to understand how Dokku resolves aliases and dispatches a command through enabled plugin subcommands and the legacy command protocol.
- **Traceability:** Start at execute_dokku_cmd, follow associative alias replacement, command and application argument adaptation, default, exact, and colon-subcommand executable lookup, then trace the legacy commands fan-out through not-implemented, valid, and error exits to the unknown-command result; close with core and plugin Bats cases. SSH authorization and deployment-platform breadth are excluded.
- **Maintainability:** Changes to the path beginning at `dokku` are constrained by these audited guarantees: new and legacy plugin protocols must remain compatible, resolution precedence and argument adaptation must be deterministic, reserved exit statuses must distinguish fallback, success, and failure, and unknown commands must fail through the public contract.
- **Educational value:** Understand how Dokku resolves aliases and dispatches a command through enabled plugin subcommands and the legacy command protocol. The bounded execute_dokku_cmd trace needs only concise plugin-dispatch vocabulary and primarily teaches associative alias maps, argument adaptation, extension precedence, dynamic executable routing, compatibility fallback, and explicit exit semantics; Docker, Git deployment, proxies, certificates, and Kubernetes are excluded.

**Inspection record:** commit `c712429b095e8bbd58029787b64a9f23f98cb5fb`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `dokku`, `plugins/common/functions`, `tests/unit/core_2.bats`, `tests/unit/plugin.bats`, `docs/development/testing.md`, `README.md`, `LICENSE`. GitHub Linguist label: Shell.

</details>

### [rbenv/rbenv](https://github.com/rbenv/rbenv)

**Language 2 / Behavior 3 / Design 2 / Constraints 4 → Level 3**

A per-user Ruby version manager that selects installations through PATH shims, directory-local version files, environment overrides, and plugins.

**Why study it:** Understand how rbenv safely reconciles a directory of executable shims with installed runtimes and plugin-provided commands. The short runtime-selection context is subordinate to transferable lessons in filesystem reconciliation, lock ownership, cleanup traps, generated wrappers, plugin hooks, exact-name matching, and behavior-driven tests.

**Prerequisites:**

- Basic familiarity with Shell functions, parameter expansion, quoting, pipelines, exit statuses, arrays where supported, and Bats-style tests.
- A shim is a small executable placed earlier in PATH so a version manager can choose the real runtime command.

**Concepts this path develops:**

- Arrays, process substitution, and parameter expansion.
- Lock acquisition, owned cleanup, and failed acquisition.
- Only one rehash process may own the prototype.

**What you can learn:**

- Study these transferable Shell mechanisms in `libexec/rbenv-rehash`: arrays, process substitution, and parameter expansion, heredoc-generated shim and sourced plugin hooks, and EXIT trap and noclobber lock idioms.
- Trace these states and branches from `libexec/rbenv-rehash` through its selected supporting files: lock acquisition, owned cleanup, and failed acquisition, prototype creation and outdated-shim replacement, and registered, installed, stale, and removed shim states.
- Identify these architectural responsibilities in the path beginning at `libexec/rbenv-rehash`: rehash reconciler, hook discovery boundary, and generated shim and direct test suite.
- Study these change constraints for the path beginning at `libexec/rbenv-rehash`: only one rehash process may own the prototype, cleanup must occur on every owned exit path, upgrades and stale commands must reconcile without deleting valid exact-name shims, and spaces, permissions, hook IFS, GEM_HOME, and shell behavior must remain compatible.

**Learning path:**

- **Goal:** Understand how rbenv safely reconciles a directory of executable shims with installed runtimes and plugin-provided commands.
- **Start here:** [`libexec/rbenv-rehash`](https://github.com/rbenv/rbenv/blob/07e9b1e297a5977298c6aadc9971ae0e9eb7f0dc/libexec/rbenv-rehash) — Begin with `libexec/rbenv-rehash` because it exposes how rbenv safely reconciles a directory of executable shims with installed runtimes and plugin-provided commands.
- **Then read:**
  - [`libexec/rbenv-hooks`](https://github.com/rbenv/rbenv/blob/07e9b1e297a5977298c6aadc9971ae0e9eb7f0dc/libexec/rbenv-hooks)
  - [`test/rehash.bats`](https://github.com/rbenv/rbenv/blob/07e9b1e297a5977298c6aadc9971ae0e9eb7f0dc/test/rehash.bats)
  - [`README.md`](https://github.com/rbenv/rbenv/blob/07e9b1e297a5977298c6aadc9971ae0e9eb7f0dc/README.md)
  - [`LICENSE`](https://github.com/rbenv/rbenv/blob/07e9b1e297a5977298c6aadc9971ae0e9eb7f0dc/LICENSE)
- **Trace:** Start with the noclobber prototype-shim lock and EXIT cleanup, follow prototype generation, installed executable discovery, plugin hook sourcing, shim installation, and stale removal, then close with the rehash tests for concurrency, permissions, spaces, exact names, and preserved shell state.

**Why this level:**

- **Language technique 2:** Common professional Bash process, file, and extension idioms shape the path without substantial abstraction.
- **Behavioral reasoning 3:** A nontrivial resource and reconciliation lifecycle materially affects the trace.
- **Design span 2:** One process and a few explicit components contain the behavior.
- **Constraint burden 4:** Concurrency, cleanup, filesystem reconciliation, extension, and compatibility guarantees interact throughout rehash.
- **Placement:** The four scores 2/3/2/4 sum to 11; their arithmetic mean is 2.75 and rounds half-up to Level 3. The published result is Level 3.

**License:** MIT ([evidence 1](https://github.com/rbenv/rbenv/blob/07e9b1e297a5977298c6aadc9971ae0e9eb7f0dc/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The repository ships the rbenv command installed by major operating-system package managers and used to select Ruby runtimes for projects and shells.

**Language evidence:** Command dispatch, version selection, shim generation, hook discovery, executable lookup, and shell initialization are implemented as Bash executables under libexec/.

**Coding relevance:**

The short runtime-selection context is subordinate to transferable lessons in filesystem reconciliation, lock ownership, cleanup traps, generated wrappers, plugin hooks, exact-name matching, and behavior-driven tests.

Required domain context:

- A shim is a small executable placed earlier in PATH so a version manager can choose the real runtime command.

**Eight-part quality gate:**

- **Source quality:** libexec/rbenv-rehash documents each phase, uses narrow functions and explicit ownership, rbenv-hooks isolates extension discovery, test/rehash.bats directly covers empty and concurrent runs, permissions, creation, outdated and stale shims, exact names, paths with spaces, GEM_HOME, hook state, and shell integration, the README explains the mechanism, and the pinned MIT license and direct trace satisfy all eight quality dimensions.
- **Architecture:** The audited architecture of the path beginning at `libexec/rbenv-rehash` has these boundaries: rehash reconciler, hook discovery boundary, and generated shim and direct test suite.
- **Naming and idiom:** `libexec/rbenv-rehash` and its supporting files use these characteristic Shell mechanisms: arrays, process substitution, and parameter expansion, heredoc-generated shim and sourced plugin hooks, and EXIT trap and noclobber lock idioms.
- **Tests:** Direct tests in `test/rehash.bats` cover these states and branches in the selected path: lock acquisition, owned cleanup, and failed acquisition, prototype creation and outdated-shim replacement, and registered, installed, stale, and removed shim states.
- **Documentation:** `libexec/rbenv-rehash` and its selected supporting material document the contracts needed to understand how rbenv safely reconciles a directory of executable shims with installed runtimes and plugin-provided commands.
- **Traceability:** Start with the noclobber prototype-shim lock and EXIT cleanup, follow prototype generation, installed executable discovery, plugin hook sourcing, shim installation, and stale removal, then close with the rehash tests for concurrency, permissions, spaces, exact names, and preserved shell state.
- **Maintainability:** Changes to the path beginning at `libexec/rbenv-rehash` are constrained by these audited guarantees: only one rehash process may own the prototype, cleanup must occur on every owned exit path, upgrades and stale commands must reconcile without deleting valid exact-name shims, and spaces, permissions, hook IFS, GEM_HOME, and shell behavior must remain compatible.
- **Educational value:** Understand how rbenv safely reconciles a directory of executable shims with installed runtimes and plugin-provided commands. The short runtime-selection context is subordinate to transferable lessons in filesystem reconciliation, lock ownership, cleanup traps, generated wrappers, plugin hooks, exact-name matching, and behavior-driven tests.

**Inspection record:** commit `07e9b1e297a5977298c6aadc9971ae0e9eb7f0dc`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `libexec/rbenv-rehash`, `libexec/rbenv-hooks`, `test/rehash.bats`, `README.md`, `LICENSE`. GitHub Linguist label: Shell.

</details>

## Level 4

### [ko1nksm/getoptions](https://github.com/ko1nksm/getoptions)

**Language 4 / Behavior 3 / Design 3 / Constraints 4 → Level 4**

A portable POSIX-shell option parser and parser generator supporting short, long, optional, abbreviated, and subcommand forms.

**Why study it:** Understand how a portable Shell definition DSL emits and evaluates a parser for flags, values, validation, scanning modes, abbreviations, subcommands, and rest arguments. Command-line option vocabulary is concise; the path primarily teaches portable Shell metaprogramming, quoting, generated parsers, stateful scanning, callbacks, modular extensions, and cross-shell contracts.

**Prerequisites:**

- Working familiarity with Shell functions, parameter expansion, quoting, pipelines, exit statuses, arrays where supported, and Bats-style tests, plus experience tracing behavior across several production files.
- An option definition describes flags, required and optional values, subcommands, validation, and remaining positional arguments.

**Concepts this path develops:**

- Nested definition functions and dynamic dispatch.
- Definition collection followed by generated parser execution.
- Portable behavior across POSIX-like shells.

**What you can learn:**

- Study these transferable Shell mechanisms in `lib/getoptions_base.sh`: nested definition functions and dynamic dispatch, portable quoting and indirect variables, and eval-based Shell code generation.
- Trace these states and branches from `lib/getoptions_base.sh` through its selected supporting files: definition collection followed by generated parser execution, default, stop, and subcommand scanning modes, and flag, value, validation, ambiguity, rest, and error states.
- Identify these architectural responsibilities in the path beginning at `lib/getoptions_base.sh`: base parser generator, optional abbreviation module, executable and embedding delivery layer, and direct specification suites.
- Study these change constraints for the path beginning at `lib/getoptions_base.sh`: portable behavior across POSIX-like shells, generated code and eval quoting must remain safe and exact, GNU-style option forms, modes, callbacks, and errors must remain compatible, and optional modules and embedding must preserve the generated contract.

**Learning path:**

- **Goal:** Understand how a portable Shell definition DSL emits and evaluates a parser for flags, values, validation, scanning modes, abbreviations, subcommands, and rest arguments.
- **Start here:** [`lib/getoptions_base.sh`](https://github.com/ko1nksm/getoptions/blob/139d121807db67f632b412b2a00ece851df73203/lib/getoptions_base.sh) — Begin with `lib/getoptions_base.sh` because it exposes how a portable Shell definition DSL emits and evaluates a parser for flags, values, validation, scanning modes, abbreviations, subcommands, and rest arguments.
- **Then read:**
  - [`lib/getoptions_abbr.sh`](https://github.com/ko1nksm/getoptions/blob/139d121807db67f632b412b2a00ece851df73203/lib/getoptions_abbr.sh)
  - [`src/getoptions`](https://github.com/ko1nksm/getoptions/blob/139d121807db67f632b412b2a00ece851df73203/src/getoptions)
  - [`src/gengetoptions`](https://github.com/ko1nksm/getoptions/blob/139d121807db67f632b412b2a00ece851df73203/src/gengetoptions)
  - [`spec/getoptions_base_spec.sh`](https://github.com/ko1nksm/getoptions/blob/139d121807db67f632b412b2a00ece851df73203/spec/getoptions_base_spec.sh)
  - [`spec/getoptions_abbr_spec.sh`](https://github.com/ko1nksm/getoptions/blob/139d121807db67f632b412b2a00ece851df73203/spec/getoptions_abbr_spec.sh)
  - [`README.md`](https://github.com/ko1nksm/getoptions/blob/139d121807db67f632b412b2a00ece851df73203/README.md)
  - [`LICENSE`](https://github.com/ko1nksm/getoptions/blob/139d121807db67f632b412b2a00ece851df73203/LICENSE)
- **Trace:** Start with getoptions definition collection and its quoting and code emitters, follow flag, param, option, validation, scanning-mode, subcommand, rest, and error definitions into the generated parser, then close with the direct base and abbreviation ShellSpec contexts and the executable delivery layer.

**Why this level:**

- **Language technique 4:** Advanced metaprogramming and generated-code mechanisms recur, but the bounded generator does not require several distinct expert language systems interacting pervasively.
- **Behavioral reasoning 3:** A nontrivial parser state machine materially shapes the path, while concurrency, scheduling, recovery, or comparable advanced nonlocal behavior does not recur.
- **Design span 3:** Several meaningful generator, extension, delivery, and verification boundaries cooperate.
- **Constraint burden 4:** Multiple portability, quoting, grammar, extension, and compatibility guarantees interact throughout the path.
- **Placement:** The four scores 4/3/3/4 sum to 14; their arithmetic mean is 3.50 and rounds half-up to Level 4. The published result is Level 4.

**License:** CC0-1.0 ([evidence 1](https://github.com/ko1nksm/getoptions/blob/139d121807db67f632b412b2a00ece851df73203/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The repository publishes standalone release scripts and a Homebrew package for shell programs that need a richer option grammar than getopts provides.

**Language evidence:** The portable option grammar, parser-code generator, abbreviation and help modules, and executable interfaces are implemented in POSIX shell.

**Coding relevance:**

Command-line option vocabulary is concise; the path primarily teaches portable Shell metaprogramming, quoting, generated parsers, stateful scanning, callbacks, modular extensions, and cross-shell contracts.

Required domain context:

- An option definition describes flags, required and optional values, subcommands, validation, and remaining positional arguments.

**Eight-part quality gate:**

- **Source quality:** lib/getoptions_base.sh uses deliberate emitters and a definition vocabulary rather than accidental density, abbreviation remains an optional module, src/getoptions and src/gengetoptions expose delivery and embedding, the ShellSpec suites directly cover scanning modes, option forms, callbacks, validation, ambiguity, subcommands, quoting, and errors, the README documents purpose and portability, and the pinned CC0-1.0 license plus direct trace satisfy all eight quality dimensions.
- **Architecture:** The audited architecture of the path beginning at `lib/getoptions_base.sh` has these boundaries: base parser generator, optional abbreviation module, executable and embedding delivery layer, and direct specification suites.
- **Naming and idiom:** `lib/getoptions_base.sh` and its supporting files use these characteristic Shell mechanisms: nested definition functions and dynamic dispatch, portable quoting and indirect variables, and eval-based Shell code generation.
- **Tests:** Direct tests in `spec/getoptions_base_spec.sh` and `spec/getoptions_abbr_spec.sh` cover these states and branches in the selected path: definition collection followed by generated parser execution, default, stop, and subcommand scanning modes, and flag, value, validation, ambiguity, rest, and error states.
- **Documentation:** `lib/getoptions_base.sh` and its selected supporting material document the contracts needed to understand how a portable Shell definition DSL emits and evaluates a parser for flags, values, validation, scanning modes, abbreviations, subcommands, and rest arguments.
- **Traceability:** Start with getoptions definition collection and its quoting and code emitters, follow flag, param, option, validation, scanning-mode, subcommand, rest, and error definitions into the generated parser, then close with the direct base and abbreviation ShellSpec contexts and the executable delivery layer.
- **Maintainability:** Changes to the path beginning at `lib/getoptions_base.sh` are constrained by these audited guarantees: portable behavior across POSIX-like shells, generated code and eval quoting must remain safe and exact, GNU-style option forms, modes, callbacks, and errors must remain compatible, and optional modules and embedding must preserve the generated contract.
- **Educational value:** Understand how a portable Shell definition DSL emits and evaluates a parser for flags, values, validation, scanning modes, abbreviations, subcommands, and rest arguments. Command-line option vocabulary is concise; the path primarily teaches portable Shell metaprogramming, quoting, generated parsers, stateful scanning, callbacks, modular extensions, and cross-shell contracts.

**Inspection record:** commit `139d121807db67f632b412b2a00ece851df73203`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `lib/getoptions_base.sh`, `lib/getoptions_abbr.sh`, `src/getoptions`, `src/gengetoptions`, `spec/getoptions_base_spec.sh`, `spec/getoptions_abbr_spec.sh`, `README.md`, `LICENSE`. GitHub Linguist label: Shell.

</details>

### [pyenv/pyenv](https://github.com/pyenv/pyenv)

**Language 4 / Behavior 3 / Design 3 / Constraints 4 → Level 4**

A Python version manager that selects installed runtimes through shims and can download and build many Python implementations.

**Why study it:** Understand how pyenv detects a caller shell, emits compatible initialization code, and safely installs startup configuration across several shell languages. Startup-file vocabulary is short and the selected path teaches cross-language code generation, parent-shell detection, persistent configuration safeguards, idempotent PATH handling, and directly tested compatibility without Python build-toolchain breadth.

**Prerequisites:**

- Working familiarity with Shell functions, parameter expansion, quoting, pipelines, exit statuses, arrays where supported, and Bats-style tests, plus experience tracing behavior across several production files.
- Shell startup files establish environment variables, PATH entries, completions, and wrapper functions for interactive sessions.

**Concepts this path develops:**

- Bash that generates Bash, Zsh, Ksh, Fish, and PowerShell code.
- Help, path, print, detect-shell, and install modes.
- Generated syntax must be correct in several shell languages.

**What you can learn:**

- Study these transferable Shell mechanisms in `libexec/pyenv-init`: Bash that generates Bash, Zsh, Ksh, Fish, and PowerShell code, arrays and shell-specific parameter and quoting machinery, and dynamic wrapper-function and PATH-program generation.
- Trace these states and branches from `libexec/pyenv-init` through its selected supporting files: help, path, print, detect-shell, and install modes, shell detection and profile-selection branches, and unchecked, refused, created, appended, and failed configuration states.
- Identify these architectural responsibilities in the path beginning at `libexec/pyenv-init`: shell and profile detection, dialect-specific code emitters, startup-file validation and mutation, PATH, completion, rehash, and wrapper behavior, and direct init tests.
- Study these change constraints for the path beginning at `libexec/pyenv-init`: generated syntax must be correct in several shell languages, PATH changes must be ordered and idempotent, all startup files must pass preflight before any write, and existing configuration, unreadable files, shell differences, and historical SSH behavior must fail safely.

**Learning path:**

- **Goal:** Understand how pyenv detects a caller shell, emits compatible initialization code, and safely installs startup configuration across several shell languages.
- **Start here:** [`libexec/pyenv-init`](https://github.com/pyenv/pyenv/blob/4733cca31b0f63eab95937f179584ba0d47d44d5/libexec/pyenv-init) — Begin with `libexec/pyenv-init` because it exposes how pyenv detects a caller shell, emits compatible initialization code, and safely installs startup configuration across several shell languages.
- **Then read:**
  - [`test/init.bats`](https://github.com/pyenv/pyenv/blob/4733cca31b0f63eab95937f179584ba0d47d44d5/test/init.bats)
  - [`README.md`](https://github.com/pyenv/pyenv/blob/4733cca31b0f63eab95937f179584ba0d47d44d5/README.md)
  - [`LICENSE`](https://github.com/pyenv/pyenv/blob/4733cca31b0f63eab95937f179584ba0d47d44d5/LICENSE)
- **Trace:** Start with mode parsing and parent-shell detection, follow profile selection and Bash/Zsh/Ksh, Fish, and PowerShell setup generation into startup-file preflight and append behavior, then trace PATH de-duplication, completions, rehash, and wrapper emission; close with the focused init Bats suite.

**Why this level:**

- **Language technique 4:** Cross-shell code generation and advanced quoting recur throughout initialization.
- **Behavioral reasoning 3:** Persistent setup and generated-runtime state form a nontrivial but bounded lifecycle.
- **Design span 3:** Several meaningful generation, persistence, runtime, and verification boundaries cooperate.
- **Constraint burden 4:** Cross-shell compatibility, persistence safety, idempotence, and startup reliability constraints interact throughout the path.
- **Placement:** The four scores 4/3/3/4 sum to 14; their arithmetic mean is 3.50 and rounds half-up to Level 4. The published result is Level 4.

**License:** MIT ([evidence 1](https://github.com/pyenv/pyenv/blob/4733cca31b0f63eab95937f179584ba0d47d44d5/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The repository ships the pyenv command and bundled python-build plugin installed through common package managers and used for per-user and per-project Python selection.

**Language evidence:** Runtime selection, command dispatch, shims, hooks, shell setup, Python download and compilation, and binary packaging are implemented primarily in Bash.

**Coding relevance:**

Startup-file vocabulary is short and the selected path teaches cross-language code generation, parent-shell detection, persistent configuration safeguards, idempotent PATH handling, and directly tested compatibility without Python build-toolchain breadth.

Required domain context:

- Shell startup files establish environment variables, PATH entries, completions, and wrapper functions for interactive sessions.

**Eight-part quality gate:**

- **Source quality:** libexec/pyenv-init separates detection, setup generation, startup-file checks, appending, PATH handling, completion, rehash, and wrapper generation into named functions; test/init.bats directly covers modes, detected and explicit shells, Bash, Zsh, Ksh, Fish, PowerShell, setup refusal, unreadable files, existing code, directory creation, newlines, and PATH behavior; the README documents initialization; and the pinned MIT license plus direct trace satisfy all eight quality dimensions.
- **Architecture:** The audited architecture of the path beginning at `libexec/pyenv-init` has these boundaries: shell and profile detection, dialect-specific code emitters, startup-file validation and mutation, PATH, completion, rehash, and wrapper behavior, and direct init tests.
- **Naming and idiom:** `libexec/pyenv-init` and its supporting files use these characteristic Shell mechanisms: Bash that generates Bash, Zsh, Ksh, Fish, and PowerShell code, arrays and shell-specific parameter and quoting machinery, and dynamic wrapper-function and PATH-program generation.
- **Tests:** Direct tests in `test/init.bats` cover these states and branches in the selected path: help, path, print, detect-shell, and install modes, shell detection and profile-selection branches, and unchecked, refused, created, appended, and failed configuration states.
- **Documentation:** `libexec/pyenv-init` and its selected supporting material document the contracts needed to understand how pyenv detects a caller shell, emits compatible initialization code, and safely installs startup configuration across several shell languages.
- **Traceability:** Start with mode parsing and parent-shell detection, follow profile selection and Bash/Zsh/Ksh, Fish, and PowerShell setup generation into startup-file preflight and append behavior, then trace PATH de-duplication, completions, rehash, and wrapper emission; close with the focused init Bats suite.
- **Maintainability:** Changes to the path beginning at `libexec/pyenv-init` are constrained by these audited guarantees: generated syntax must be correct in several shell languages, PATH changes must be ordered and idempotent, all startup files must pass preflight before any write, and existing configuration, unreadable files, shell differences, and historical SSH behavior must fail safely.
- **Educational value:** Understand how pyenv detects a caller shell, emits compatible initialization code, and safely installs startup configuration across several shell languages. Startup-file vocabulary is short and the selected path teaches cross-language code generation, parent-shell detection, persistent configuration safeguards, idempotent PATH handling, and directly tested compatibility without Python build-toolchain breadth.

**Inspection record:** commit `4733cca31b0f63eab95937f179584ba0d47d44d5`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `libexec/pyenv-init`, `test/init.bats`, `README.md`, `LICENSE`. GitHub Linguist label: Shell.

</details>

## Level 5

No qualified learning path has been published at this level. Standards are not lowered to fill a slot.

_Generated from `catalog/shell.json`; do not edit by hand._

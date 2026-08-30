# Shell

4 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

**Source legend:** Production software is built primarily for real users or systems. Educational exemplars are complete teaching-oriented software and may appear only at Levels 1 and 2.

[← All languages](../README.md)

## Level 1 — First real code

No qualified learning path has been published at this level. An empty Level 1 means Exempla has not yet found a path gentle enough to publish here; learners are not being told to jump to Level 2.

## Level 2 — Guided real-world patterns

No qualified learning path has been published at this level. Standards are not lowered to fill a slot.

## Level 3 — Intermediate production software

### [dokku/dokku](https://github.com/dokku/dokku)

**Language 3 / Behavior 3 / Design 3 / Constraints 3 → Level 3**

**Source:** Production software

A self-hosted platform as a service that builds, deploys, configures, networks, schedules, and serves applications on a user's server.

**Why study it:** Understand how Dokku resolves aliases and dispatches a command through enabled plugin subcommands and the legacy command protocol. The bounded execute_dokku_cmd trace needs only concise plugin-dispatch vocabulary and primarily teaches associative alias maps, argument adaptation, extension precedence, dynamic executable routing, compatibility fallback, and explicit exit semantics; Docker, Git deployment, proxies, certificates, and Kubernetes are excluded.

**Short context:**

- Dokku commands are implemented by enabled plugins whose executable files follow a documented command and exit-status convention.

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

**Purpose evidence:** The repository publishes installable Dokku releases and packages for operating a multi-application deployment platform on supported Ubuntu and Debian hosts.

**Language evidence:** The command router and core deployment plugins are implemented in Bash, with substantial first-party Go modules extending application, builder, proxy, storage, Docker, and Kubernetes behavior.

**Coding relevance:**

The bounded execute_dokku_cmd trace needs only concise plugin-dispatch vocabulary and primarily teaches associative alias maps, argument adaptation, extension precedence, dynamic executable routing, compatibility fallback, and explicit exit semantics; Docker, Git deployment, proxies, certificates, and Kubernetes are excluded.

The learner-facing short context appears above.

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

**Source:** Production software

A per-user Ruby version manager that selects installations through PATH shims, directory-local version files, environment overrides, and plugins.

**Why study it:** Understand how rbenv safely reconciles a directory of executable shims with installed runtimes and plugin-provided commands. The short runtime-selection context is subordinate to transferable lessons in filesystem reconciliation, lock ownership, cleanup traps, generated wrappers, plugin hooks, exact-name matching, and behavior-driven tests.

**Short context:**

- A shim is a small executable placed earlier in PATH so a version manager can choose the real runtime command.

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

**Purpose evidence:** The repository ships the rbenv command installed by major operating-system package managers and used to select Ruby runtimes for projects and shells.

**Language evidence:** Command dispatch, version selection, shim generation, hook discovery, executable lookup, and shell initialization are implemented as Bash executables under libexec/.

**Coding relevance:**

The short runtime-selection context is subordinate to transferable lessons in filesystem reconciliation, lock ownership, cleanup traps, generated wrappers, plugin hooks, exact-name matching, and behavior-driven tests.

The learner-facing short context appears above.

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

## Level 4 — Advanced

### [ko1nksm/getoptions](https://github.com/ko1nksm/getoptions)

**Language 4 / Behavior 3 / Design 3 / Constraints 4 → Level 4**

**Source:** Production software

A portable POSIX-shell option parser and parser generator supporting short, long, optional, abbreviated, and subcommand forms.

**Why study it:** Understand how a portable Shell definition DSL emits and evaluates a parser for flags, values, validation, scanning modes, abbreviations, subcommands, and rest arguments. Command-line option vocabulary is concise; the path primarily teaches portable Shell metaprogramming, quoting, generated parsers, stateful scanning, callbacks, modular extensions, and cross-shell contracts.

**Short context:**

- An option definition describes flags, required and optional values, subcommands, validation, and remaining positional arguments.

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

**Purpose evidence:** The repository publishes standalone release scripts and a Homebrew package for shell programs that need a richer option grammar than getopts provides.

**Language evidence:** The portable option grammar, parser-code generator, abbreviation and help modules, and executable interfaces are implemented in POSIX shell.

**Coding relevance:**

Command-line option vocabulary is concise; the path primarily teaches portable Shell metaprogramming, quoting, generated parsers, stateful scanning, callbacks, modular extensions, and cross-shell contracts.

The learner-facing short context appears above.

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

**Source:** Production software

A Python version manager that selects installed runtimes through shims and can download and build many Python implementations.

**Why study it:** Understand how pyenv detects a caller shell, emits compatible initialization code, and safely installs startup configuration across several shell languages. Startup-file vocabulary is short and the selected path teaches cross-language code generation, parent-shell detection, persistent configuration safeguards, idempotent PATH handling, and directly tested compatibility without Python build-toolchain breadth.

**Short context:**

- Shell startup files establish environment variables, PATH entries, completions, and wrapper functions for interactive sessions.

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

**Purpose evidence:** The repository ships the pyenv command and bundled python-build plugin installed through common package managers and used for per-user and per-project Python selection.

**Language evidence:** Runtime selection, command dispatch, shims, hooks, shell setup, Python download and compilation, and binary packaging are implemented primarily in Bash.

**Coding relevance:**

Startup-file vocabulary is short and the selected path teaches cross-language code generation, parent-shell detection, persistent configuration safeguards, idempotent PATH handling, and directly tested compatibility without Python build-toolchain breadth.

The learner-facing short context appears above.

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

## Level 5 — Expert

No qualified learning path has been published at this level. Standards are not lowered to fill a slot.

_Generated from `catalog/shell.json`; do not edit by hand._

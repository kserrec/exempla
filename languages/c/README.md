# C

8 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

**Source legend:** Production software is built primarily for real users or systems. Educational exemplars are complete teaching-oriented software and may appear only at Levels 1 and 2.

**You are not expected to understand the whole repository.** Follow the exact starting lines and focused tests in one entry; everything else can wait.

[← All languages](../README.md)

## Level 1 — First real code

### [recp/cglm](https://github.com/recp/cglm)

**Recommended first path**

**Source:** Production software

The production cglm math library clamps one floating-point value by composing its inline maximum and minimum functions.

**Just start:** Read lines 184–193 of `util.h`, then compare them with `test_clamp.c`.

**Start with: 10 lines of source.** [Open `cglm/util.h`, lines 184–193.](https://github.com/recp/cglm/blob/58d8c15a124c202188d0094705f778f6129a2612/include/cglm/util.h#L184-L193)

**Why study it:** See a complete boundary operation expressed as one composition, then connect values below, within, and above the range to direct assertions.

**Prerequisites:**

- The global novice C baseline: functions, parameters, return values, floating-point literals, header declarations, macros, includes, and assertions.
- CGLM_INLINE is the library's portability spelling for an inline function; it does not change the clamp formula.

**Concepts this path develops:**

- Composing minimum and maximum to enforce two bounds.
- Keeping a small utility in a public header as an inline function.
- Testing below-range, in-range, and above-range inputs.

**Learning path:**

- **Goal:** Understand how cglm keeps a scalar inside caller-supplied bounds and verifies each region of the input space.
- **Start here:** [`cglm/util.h`, lines 184–193](https://github.com/recp/cglm/blob/58d8c15a124c202188d0094705f778f6129a2612/include/cglm/util.h#L184-L193) — The range contains the clamp contract and complete formula; the named minimum and maximum helpers are short follow-up reads in the same file.
- **Then read:**
  - [`test/src/test_clamp.c`](https://github.com/recp/cglm/blob/58d8c15a124c202188d0094705f778f6129a2612/test/src/test_clamp.c)
  - [`docs/source/util.rst`](https://github.com/recp/cglm/blob/58d8c15a124c202188d0094705f778f6129a2612/docs/source/util.rst)
  - [`README.md`](https://github.com/recp/cglm/blob/58d8c15a124c202188d0094705f778f6129a2612/README.md)
  - [`LICENSE`](https://github.com/recp/cglm/blob/58d8c15a124c202188d0094705f778f6129a2612/LICENSE)
- **Trace:** Pass val, minVal, and maxVal into glm_clamp, follow glm_max as it enforces the lower bound, follow glm_min as it enforces the upper bound, then match the three scalar assertions to values above, below, and inside the interval.

**Why this level:**

**Level 1:** The clamp formula and all test cases are novice C material; the inline macro needs only a local note and does not affect behavior.

**License:** MIT ([evidence 1](https://github.com/recp/cglm/blob/58d8c15a124c202188d0094705f778f6129a2612/LICENSE))

<details>
<summary>Detailed Level, learning, quality, and review evidence</summary>

**What you can learn:**

- Raise a value to the lower bound with a maximum operation.
- Lower the intermediate value to the upper bound with a minimum operation.
- Verify the three observable regions around a bounded interval.

**Language 1 / Behavior 1 / Design 1 / Constraints 1 → Level 1**

- **Language technique 1:** The complete implementation is ordinary C function composition over three float parameters.
- **Behavioral reasoning 1:** The output follows from two local comparisons embodied by min and max.
- **Design span 1:** One header and one focused test contain the complete selected behavior.
- **Constraint burden 1:** The utility enforces one simple interval contract without state or external effects.
- **Novice accessibility floor 1:** The clamp formula and all test cases are novice C material; the inline macro needs only a local note and does not affect behavior.
  - **Central concepts:** float parameters and return values; minimum and maximum; nested function calls; boundary assertions
  - **Incidental concepts:** the CGLM_INLINE portability macro
- **Placement:** The four scores 1/1/1/1 produce rubric Level 1. Novice accessibility floor 1 preserves published Level 1.

**Purpose evidence:** cglm is a maintained C mathematics library for graphics applications, and glm_clamp is a documented public utility used by other library operations.

**Language evidence:** glm_clamp, glm_min, glm_max, the focused clamp test, and the public header documentation are first-party C; GitHub labels the repository C.

**Coding relevance:**

Bounds enforcement, small function composition, public C headers, and boundary-partition tests are general programming techniques.

No specialist domain context is required.

**Eight-part quality gate:**

- **Source quality:** The implementation is the actual clamp formula, not a forwarding wrapper, and every operation is visible in one return statement.
- **Architecture:** The scalar utility sits with the library's related public math helpers and is reused by higher operations.
- **Naming and idiom:** val, minVal, maxVal, glm_min, glm_max, and glm_clamp make the data flow literal.
- **Tests:** The upstream test directly covers a value above the interval, below it, and inside it; the exact pinned test body compiled and ran successfully in isolation.
- **Documentation:** The header comment and utility reference name the operation and each parameter, while the README establishes the production library context.
- **Traceability:** Each scalar assertion isolates one of the formula's three possible outcomes.
- **Maintainability:** The implementation reuses the library's min and max semantics, so one formula remains the source of truth for clamping.
- **Educational value:** A novice can derive every result by hand and still encounter a real public C library function and test harness.

**Inspection record:** commit `58d8c15a124c202188d0094705f778f6129a2612`, inspected 2026-08-30. Review passes: Codex 85% Level 1 investigation; Codex resumed-session source verification. Files inspected: `include/cglm/util.h`, `test/src/test_clamp.c`, `docs/source/util.rst`, `README.md`, `LICENSE`. GitHub Linguist label: C.

</details>

## Level 2 — Guided real-world patterns

### [benhoyt/inih](https://github.com/benhoyt/inih)

**Source:** Production software

A small C parser that reads an INI settings file line by line and reports each section, name, and value to a callback.

**Just start:** Read lines 98–270 of `ini.c`, then compare them with `unittest.c`.

**Start with: 173 lines of source.** [Open `ini.c`, lines 98–270.](https://github.com/benhoyt/inih/blob/577ae2dee1f0d9c2d11c7f10375c1715f3d6940c/ini.c#L98-L270)

**Why study it:** Follow one input line from whitespace cleanup through comment, section, key-value, continuation, or error handling, then see the parsed result cross one callback boundary.

**Short context:**

- An INI file uses [section] headings and name=value lines; this parser reports text and deliberately leaves value interpretation to its caller.

**Prerequisites:**

- The global novice C baseline, including pointers, character arrays, structs, callbacks, file input, and focused tests.
- An INI file groups name=value lines under [section] headings; blank lines and prefixed lines can be ignored as comments.

**Concepts this path develops:**

- Classifying one cleaned input line into a small grammar.
- Sending parsed section, name, and value strings through a callback.
- Keeping parsing policy configurable without changing the public trace.

**Learning path:**

- **Goal:** Understand how a compact C parser reads INI text one line at a time and reports each result through a callback.
- **Start here:** [`ini.c`, lines 98–270](https://github.com/benhoyt/inih/blob/577ae2dee1f0d9c2d11c7f10375c1715f3d6940c/ini.c#L98-L270) — Begin at ini_parse_stream, where every input source joins the same line-classification and handler-callback loop.
- **Then read:**
  - [`ini.h`](https://github.com/benhoyt/inih/blob/577ae2dee1f0d9c2d11c7f10375c1715f3d6940c/ini.h)
  - [`README.md`](https://github.com/benhoyt/inih/blob/577ae2dee1f0d9c2d11c7f10375c1715f3d6940c/README.md)
  - [`tests/unittest.c`](https://github.com/benhoyt/inih/blob/577ae2dee1f0d9c2d11c7f10375c1715f3d6940c/tests/unittest.c)
  - [`tests/unittest.sh`](https://github.com/benhoyt/inih/blob/577ae2dee1f0d9c2d11c7f10375c1715f3d6940c/tests/unittest.sh)
  - [`tests/unittest_alloc.c`](https://github.com/benhoyt/inih/blob/577ae2dee1f0d9c2d11c7f10375c1715f3d6940c/tests/unittest_alloc.c)
  - [`tests/unittest_string.c`](https://github.com/benhoyt/inih/blob/577ae2dee1f0d9c2d11c7f10375c1715f3d6940c/tests/unittest_string.c)
- **Trace:** Start at ini_parse_stream, follow line reading and bounded growth through whitespace and comment handling, section and name-value classification, optional continuations, callback failure, and error recovery; compare file and string readers, then close with baseline, allocation, and string-source tests.

**Why this level:**

**Level 2:** The full INI grammar and callback role fit a short primer, after which representative lines are predictable; configuration branches stretch the path but remain subordinate to one local loop.

**License:** BSD-3-Clause ([evidence 1](https://github.com/benhoyt/inih/blob/577ae2dee1f0d9c2d11c7f10375c1715f3d6940c/LICENSE.txt))

<details>
<summary>Detailed Level, learning, quality, and review evidence</summary>

**What you can learn:**

- Trace a line-oriented parser with direct branches for comments, sections, values, continuations, and malformed input.
- See how a callback lets application code decide what parsed names and values mean.
- Compare file, stream, and string readers that share the same parser.
- Use baseline and configuration tests to understand bounded lines, optional allocation, and compile-time policy choices.

**Language 2 / Behavior 2 / Design 1 / Constraints 3 → Level 2**

- **Language technique 2:** Common professional C callbacks, buffers, and preprocessor options materially shape the parser without advanced memory techniques.
- **Behavioral reasoning 2:** Several related parser branches recur, but each line is handled synchronously in one loop.
- **Design span 1:** The complete reader-to-handler lesson remains in one focused component and its tests.
- **Constraint burden 3:** Several material input, resource, configuration, and portability guarantees constrain the otherwise compact parser.
- **Novice accessibility floor 2:** The full INI grammar and callback role fit a short primer, after which representative lines are predictable; configuration branches stretch the path but remain subordinate to one local loop.
  - **Central concepts:** a trivial section-and-name-value grammar; line-oriented parsing; reporting parsed values through a callback
  - **Incidental concepts:** compile-time policy switches; optional stack or heap line storage; UTF-8 byte-order-mark compatibility
- **Placement:** The four structural scores 2/2/1/3 produce rubric Level 2 under the documented formula and guardrails. Novice accessibility floor 2 produces published Level 2.

**Purpose evidence:** inih ships a maintained embeddable parser used and packaged across C and C++ ecosystems, with configurable allocation and syntax policies plus a direct compiler test matrix.

**Language evidence:** The selected line parser, public callbacks, string and file readers, allocation policies, and baseline tests are implemented in C in ini.c, ini.h, and tests/unittest.c.

**Coding relevance:**

The complete grammar fits the short context above; the path teaches callbacks, line scanning, bounded buffers, recovery, optional allocation, compile-time policies, and direct tests.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The compact implementation separates trimming helpers, one parser loop, and three input adapters; callback and error contracts are explicit, and malformed-input plus allocation variants are directly exercised.
- **Architecture:** One implementation and public header own parsing, while caller callbacks own value interpretation and small input adapters reuse the same stream loop.
- **Naming and idiom:** Names such as ini_parse_stream, ini_reader, ini_handler, section, name, value, and lineno expose the trace; bounded C buffers and callbacks are used conventionally.
- **Tests:** The checked baseline covers missing files, ordinary data, bad sections and comments, callback errors, continuations, byte-order marks, duplicate sections, no-value lines, long sections and lines, with separate string and allocation variants.
- **Documentation:** The header and README define the callback contract, return codes, line syntax, configuration switches, allocation modes, continuation behavior, and C and C++ usage.
- **Traceability:** All input forms converge on ini_parse_stream, whose line branches call one handler and map directly to the baseline cases.
- **Maintainability:** Small helpers isolate trimming and input adaptation, while compile-time policies are named centrally and the compiler matrix checks supported combinations.
- **Educational value:** The path is a complete, production-tested example of a deliberately small grammar, callbacks, bounded input, recovery, configuration, and portable C design.

**Inspection record:** commit `577ae2dee1f0d9c2d11c7f10375c1715f3d6940c`, inspected 2026-08-30. Review passes: Codex exact-pin gap research; Codex cold self-review; Codex novice-accessibility re-review. Files inspected: `ini.c`, `ini.h`, `README.md`, `tests/unittest.c`, `tests/unittest.sh`, `tests/unittest_alloc.c`, `tests/unittest_string.c`, `LICENSE.txt`. GitHub Linguist label: C++.

</details>

## Level 3 — Intermediate production software

_Ordered from gentler to more demanding within this Level._

### [cktan/tomlc17](https://github.com/cktan/tomlc17)

**Language 3 / Behavior 3 / Design 3 / Constraints 4 → Level 3**

**Source:** Production software

A lightweight C17 TOML parser that builds an owned typed tree and supports lookup, merge, structural comparison, source locations, and custom allocators.

**Why study it:** Understand how tomlc17 scans a bounded byte buffer, builds an owned tagged tree, and releases every allocation on success or failure. TOML needs only a short syntax primer; the path teaches transferable scanner and parser state, tagged unions, arena ownership, recursive construction, error propagation, configurable allocation, and sanitizer-backed edge testing.

**Short context:**

- TOML maps keys to typed scalar, array, and table values; dotted keys and table headers construct nested paths, and malformed documents must fail without leaking a partial tree.

**Prerequisites:**

- Basic familiarity with C functions, pointers, structs, enums, arrays, manual allocation, function pointers, and focused tests.
- TOML maps keys to typed scalar, array, and table values; dotted keys and table headers construct nested paths, and malformed documents must fail without leaking a partial tree.

**Concepts this path develops:**

- Pointer-and-length source spans and scanner snapshots.
- Scanner position, lookahead, and token-mode transitions.
- TOML grammar, numeric, timestamp, escape, and UTF-8 compatibility.

**What you can learn:**

- Study these transferable C mechanisms in `src/tomlc17.c`: pointer-and-length spans over caller input, tagged unions for heterogeneous values, and separate arena and growable-cell allocation strategies.
- Trace these states and branches from `src/tomlc17.c` through its selected supporting files: scanner token and lookahead state, recursive table, array, scalar, and dotted-key construction, and success, malformed-input, allocation-failure, merge, and teardown paths.
- Identify these architectural responsibilities in the path beginning at `src/tomlc17.c`: scanner, recursive-descent parser, typed tree and lookup API, memory ownership layer, and focused parser, pool, and merge tests.
- Study these change constraints for the path beginning at `src/tomlc17.c`: TOML grammar and UTF-8 conformance, bounded input and stable source locations, result-owned pointer lifetime and complete failure cleanup, and C99, C17, C++, allocator, and sanitizer compatibility.

**Learning path:**

- **Goal:** Understand how tomlc17 scans a bounded byte buffer, builds an owned tagged tree, and releases every allocation on success or failure.
- **Start here:** [`src/tomlc17.c`](https://github.com/cktan/tomlc17/blob/64a063b8636a4b48d142f978270f5e53e605e240/src/tomlc17.c) — Begin at `toml_parse_named`, then read the scanner, parser, tree construction, and pool helpers in the same translation unit so every ownership transition remains visible.
- **Then read:**
  - [`src/tomlc17.h`](https://github.com/cktan/tomlc17/blob/64a063b8636a4b48d142f978270f5e53e605e240/src/tomlc17.h)
  - [`DESIGN.md`](https://github.com/cktan/tomlc17/blob/64a063b8636a4b48d142f978270f5e53e605e240/DESIGN.md)
  - [`API.md`](https://github.com/cktan/tomlc17/blob/64a063b8636a4b48d142f978270f5e53e605e240/API.md)
  - [`test/parser/parser.c`](https://github.com/cktan/tomlc17/blob/64a063b8636a4b48d142f978270f5e53e605e240/test/parser/parser.c)
  - [`test/parser/run.sh`](https://github.com/cktan/tomlc17/blob/64a063b8636a4b48d142f978270f5e53e605e240/test/parser/run.sh)
  - [`test/pool/test1.c`](https://github.com/cktan/tomlc17/blob/64a063b8636a4b48d142f978270f5e53e605e240/test/pool/test1.c)
  - [`test/merge/test1.c`](https://github.com/cktan/tomlc17/blob/64a063b8636a4b48d142f978270f5e53e605e240/test/merge/test1.c)
- **Trace:** Start at toml_parse_named, follow parser initialization and scan_next into table, array, key-value, and scalar dispatch, watch spans become pool-owned normalized strings and tagged tree nodes, then trace both error and success cleanup through datum_free and pool_destroy; close with malformed parser fixtures, allocator-boundary tests, and merge ownership tests that free inputs before reading the result.

**Why this level:**

- **Language technique 3:** Nontrivial type modeling and manual ownership materially shape the path, while the implementation deliberately avoids pervasive metaprogramming or platform-specific expert machinery.
- **Behavioral reasoning 3:** Several parser and ownership states interact across the synchronous lifecycle, but concurrency and distributed recovery are absent.
- **Design span 3:** The trace crosses several meaningful responsibilities even though the implementation remains intentionally amalgamated into one source file.
- **Constraint burden 4:** Grammar conformance, memory safety, ownership, error reporting, and language interoperability recur together through ordinary parser changes.
- **Placement:** The four scores 3/3/3/4 sum to 13; their arithmetic mean is 3.25 and rounds half-up to Level 3. The published result is Level 3.

**License:** MIT ([evidence 1](https://github.com/cktan/tomlc17/blob/64a063b8636a4b48d142f978270f5e53e605e240/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository ships an embeddable C library for reading TOML configuration, documents C and C++ integration, and validates its parser against the standard toml-test corpus.

**Language evidence:** The public API, hand-written scanner and recursive-descent parser, tagged value tree, arena and growable-cell allocators, merge behavior, teardown, and direct tests are first-party C in src/ and test/.

**Coding relevance:**

TOML needs only a short syntax primer; the path teaches transferable scanner and parser state, tagged unions, arena ownership, recursive construction, error propagation, configurable allocation, and sanitizer-backed edge testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The implementation names scanner, parser, tree, and allocator responsibilities directly, uses one cleanup contract for every result, and avoids hidden dependencies; focused tests exercise syntax, pool boundaries, structural equivalence, merge behavior, and ownership after freeing inputs under address and undefined-behavior sanitizers.
- **Architecture:** DESIGN.md maps the scanner, recursive-descent parser, typed tree, cell storage, string pool, merge, comparison, and teardown boundaries to exact source functions and ownership rules.
- **Naming and idiom:** The path demonstrates idiomatic explicit C representation through spans, tagged unions, function-pointer allocator hooks, recursive helpers, and narrow public structures with opaque internal ownership.
- **Tests:** The selected parser fixture suite covers valid and invalid tables, arrays, dotted keys, and values; pool tests cover allocation thresholds and page growth; merge tests cover overrides, recursive tables, array-of-table behavior, type conflicts, empty inputs, and result lifetime after both inputs are freed.
- **Documentation:** README.md, API.md, DESIGN.md, and OPTIONS.md explain integration, public lifetime rules, every major internal boundary, global allocator constraints, and the standard conformance suite.
- **Traceability:** A learner can follow toml_parse_named through scan_next and parse dispatch into tagged nodes and pooled strings, then reach explicit cleanup and direct parser, pool, and merge tests without leaving the selected files.
- **Maintainability:** The revision centralizes result ownership, isolates unsynchronized global allocator configuration, asserts allocator invariants, documents threading limits, and runs focused tests with compiler warnings plus address and undefined-behavior sanitizers.
- **Educational value:** The path combines practical parsing with visible low-level ownership and failure handling while keeping the format vocabulary subordinate to reusable C engineering lessons.

**Inspection record:** commit `64a063b8636a4b48d142f978270f5e53e605e240`, inspected 2026-08-29. Review passes: Codex primary pass; Codex cold verification pass. Files inspected: `src/tomlc17.c`, `src/tomlc17.h`, `README.md`, `DESIGN.md`, `API.md`, `OPTIONS.md`, `test/parser/parser.c`, `test/parser/run.sh`, `test/pool/test1.c`, `test/merge/test1.c`, `LICENSE`. GitHub Linguist label: C.

</details>

### [DaveGamble/cJSON](https://github.com/DaveGamble/cJSON)

**Language 4 / Behavior 3 / Design 2 / Constraints 4 → Level 3**

**Source:** Production software

An ultralightweight JSON parser, tree model, printer, and manipulation library written in portable ANSI C.

**Why study it:** Understand how cJSON parses bounded text into an owned recursive object tree and cleans up correctly across success and failure. The short data-format vocabulary is sufficient context; the path teaches transferable recursive parsing, linked ownership, allocator discipline, error positions, depth limits, and public/private API boundaries.

**Short context:**

- JSON values form a recursive tree of objects, arrays, strings, numbers, booleans, and null, with ownership transferred into containers.

**Prerequisites:**

- Basic familiarity with C functions, pointers, structs, enums, arrays, manual allocation, function pointers, and focused tests.
- JSON values form a recursive tree of objects, arrays, strings, numbers, booleans, and null, with ownership transferred into containers.

**Concepts this path develops:**

- Ownership transfer and cleanup for recursive parse trees, including partially built failures.
- Recursive value and object dispatch.
- Bounded and null-terminated input modes.

**What you can learn:**

- Study these transferable C mechanisms in `cJSON.c`: manual recursive tree ownership, intrusive child and sibling links, and pluggable allocation hooks and pointer arithmetic.
- Trace these states and branches from `cJSON.c` through its selected supporting files: recursive value and object dispatch, bounded parse position and depth state, and success and partial-construction cleanup branches.
- Identify these architectural responsibilities in the path beginning at `cJSON.c`: public data and ownership API, private parser helpers, and two focused test files.
- Study these change constraints for the path beginning at `cJSON.c`: bounded and null-terminated input modes, allocator and ownership correctness, and nesting limits, locale-sensitive numbers, and stable error positions.

**Learning path:**

- **Goal:** Understand how cJSON parses bounded text into an owned recursive object tree and cleans up correctly across success and failure.
- **Start here:** [`cJSON.c`](https://github.com/DaveGamble/cJSON/blob/fb16e5cf358798aabb049655975cde8427101056/cJSON.c) — Begin with `cJSON.c` because it exposes how cJSON parses bounded text into an owned recursive object tree and cleans up correctly across success and failure.
- **Then read:**
  - [`cJSON.h`](https://github.com/DaveGamble/cJSON/blob/fb16e5cf358798aabb049655975cde8427101056/cJSON.h)
  - [`tests/parse_value.c`](https://github.com/DaveGamble/cJSON/blob/fb16e5cf358798aabb049655975cde8427101056/tests/parse_value.c)
  - [`tests/parse_object.c`](https://github.com/DaveGamble/cJSON/blob/fb16e5cf358798aabb049655975cde8427101056/tests/parse_object.c)
- **Trace:** Start at cJSON_ParseWithLengthOpts, follow parse_buffer bounds and parse_value dispatch into recursive object parsing, linked child ownership, duplicate-key and depth behavior, and failure cleanup; then close the contract with the focused value and object parser tests and the public ownership rules in cJSON.h.

**Why this level:**

- **Language technique 4:** Substantial manual memory and representation technique shapes normal parsing and cleanup work, matching the published C calibration anchor.
- **Behavioral reasoning 3:** Meaningful recursive state and failure behavior remain traceable within one synchronous parse lifecycle.
- **Design span 2:** The representative behavior crosses only a small number of clearly separated responsibilities.
- **Constraint burden 4:** Several interacting memory, compatibility, and malformed-input guarantees constrain ordinary changes.
- **Placement:** The four scores 4/3/2/4 sum to 13; their arithmetic mean is 3.25 and rounds half-up to Level 3. The published result is Level 3.

**License:** MIT ([evidence 1](https://github.com/DaveGamble/cJSON/blob/fb16e5cf358798aabb049655975cde8427101056/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository ships installable and embeddable C libraries used to parse and generate JSON in native applications.

**Language evidence:** JSON parsing, tree ownership, printing, mutation, comparison, JSON Pointer, Patch, Merge Patch, and sorting are C in cJSON.c and cJSON_Utils.c.

**Coding relevance:**

The short data-format vocabulary is sufficient context; the path teaches transferable recursive parsing, linked ownership, allocator discipline, error positions, depth limits, and public/private API boundaries.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The public header documents ownership and allocator contracts, the implementation names parse state and cleanup branches directly, and the selected private tests exercise value and object parsing, malformed input, depth, duplicate keys, null termination, and allocation failures without pulling in the separate cJSON_Utils feature set.
- **Architecture:** The audited architecture of the path beginning at `cJSON.c` has these boundaries: public data and ownership API, private parser helpers, and two focused test files.
- **Naming and idiom:** `cJSON.c` and its supporting files use these characteristic C mechanisms: manual recursive tree ownership, intrusive child and sibling links, and pluggable allocation hooks and pointer arithmetic.
- **Tests:** Direct tests in `tests/parse_value.c` and `tests/parse_object.c` cover these states and branches in the selected path: recursive value and object dispatch, bounded parse position and depth state, and success and partial-construction cleanup branches.
- **Documentation:** `cJSON.c` and its selected supporting material document the contracts needed to understand how cJSON parses bounded text into an owned recursive object tree and cleans up correctly across success and failure.
- **Traceability:** Start at cJSON_ParseWithLengthOpts, follow parse_buffer bounds and parse_value dispatch into recursive object parsing, linked child ownership, duplicate-key and depth behavior, and failure cleanup; then close the contract with the focused value and object parser tests and the public ownership rules in cJSON.h.
- **Maintainability:** Changes to the path beginning at `cJSON.c` are constrained by these audited guarantees: bounded and null-terminated input modes, allocator and ownership correctness, and nesting limits, locale-sensitive numbers, and stable error positions.
- **Educational value:** Understand how cJSON parses bounded text into an owned recursive object tree and cleans up correctly across success and failure. The short data-format vocabulary is sufficient context; the path teaches transferable recursive parsing, linked ownership, allocator discipline, error positions, depth limits, and public/private API boundaries.

**Inspection record:** commit `fb16e5cf358798aabb049655975cde8427101056`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `cJSON.c`, `cJSON.h`, `tests/parse_value.c`, `tests/parse_object.c`, `LICENSE`. GitHub Linguist label: C.

</details>

## Level 4 — Advanced

_Ordered from gentler to more demanding within this Level._

### [git/git](https://github.com/git/git)

**Language 4 / Behavior 5 / Design 3 / Constraints 5 → Level 4**

**Source:** Production software

The distributed version control system implementing content-addressed history, branches, merging, network protocols, and repository maintenance.

**Why study it:** Understand how Git starts, communicates with, cleans up, and optionally schedules child processes in portable C infrastructure. The path is domain-neutral process infrastructure; it teaches transferable subprocess API design, pipe and descriptor ownership, fork or spawn lifecycles, signal cleanup, callbacks, bounded parallelism, output coordination, and shell-level integration testing.

**Short context:**

- Git's child-process layer launches external commands with controlled arguments, environment, file descriptors, cleanup, and optional parallel scheduling.

**Prerequisites:**

- Working familiarity with C functions, pointers, structs, enums, arrays, manual allocation, function pointers, and focused tests, plus experience tracing behavior across several production files.
- Git's child-process layer launches external commands with controlled arguments, environment, file descriptors, cleanup, and optional parallel scheduling.

**Concepts this path develops:**

- Function-pointer lifecycle and task callbacks.
- Prepare, launch, running, finish, signal, and cleanup process states.
- Fork, exec, and platform-specific spawn portability.

**What you can learn:**

- Study these transferable C mechanisms in `run-command.h`: function-pointer lifecycle and task callbacks, explicit child_process and parallel-process structures, and manual file-descriptor and pipe ownership.
- Trace these states and branches from `run-command.h` through its selected supporting files: prepare, launch, running, finish, signal, and cleanup process states, pipe endpoints shared across parent, child, and error paths, and parallel admission, output, abort, and completion scheduling.
- Identify these architectural responsibilities in the path beginning at `run-command.h`: public child and parallel-process contract, launch, pipe, cleanup, and scheduler implementation, and dedicated helper and shell integration suite.
- Study these change constraints for the path beginning at `run-command.h`: fork, exec, and platform-specific spawn portability, descriptor closure and deadlock avoidance on every failure path, and signal cleanup, graceful abort, and deterministic output.

**Learning path:**

- **Goal:** Understand how Git starts, communicates with, cleans up, and optionally schedules child processes in portable C infrastructure.
- **Start here:** [`run-command.h`](https://github.com/git/git/blob/c73e85354c275c9d409b26445089bc16940fc527/run-command.h) — Begin with `run-command.h` because it exposes how Git starts, communicates with, cleans up, and optionally schedules child processes in portable C infrastructure.
- **Then read:**
  - [`run-command.c`](https://github.com/git/git/blob/c73e85354c275c9d409b26445089bc16940fc527/run-command.c)
  - [`t/helper/test-run-command.c`](https://github.com/git/git/blob/c73e85354c275c9d409b26445089bc16940fc527/t/helper/test-run-command.c)
  - [`t/t0061-run-command.sh`](https://github.com/git/git/blob/c73e85354c275c9d409b26445089bc16940fc527/t/t0061-run-command.sh)
- **Trace:** Begin with child_process initialization, arguments, environment, redirection, cleanup, and callback contracts, follow start_command through pipe creation and fork, spawn, or exec setup into finish and signal cleanup, then trace pipe_command and the parallel scheduler's task admission, output buffering, abort, and completion behavior; close with the dedicated helper and t0061 tests.

**Why this level:**

- **Language technique 4:** Advanced C callback, resource, and representation techniques materially shape the process layer.
- **Behavioral reasoning 5:** Multiple nonlocal process and scheduler lifecycles interact repeatedly across operating-system boundaries.
- **Design span 3:** Several clear responsibilities collaborate within one bounded process-control subsystem.
- **Constraint burden 5:** Expert portability, resource, concurrency, and failure guarantees recur throughout normal process-layer changes.
- **Placement:** The four scores 4/5/3/5 sum to 17; their arithmetic mean is 4.25 and rounds half-up to Level 4. The published result is Level 4.

**License:** GPL-2.0-only ([evidence 1](https://github.com/git/git/blob/c73e85354c275c9d409b26445089bc16940fc527/COPYING))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository builds the Git command suite used to create, exchange, review, and maintain source histories across the software industry.

**Language evidence:** Object storage, index and working-tree operations, revision traversal, diff and merge algorithms, refs, transports, protocols, commands, and repository maintenance are principally C across the root and builtin/.

**Coding relevance:**

The path is domain-neutral process infrastructure; it teaches transferable subprocess API design, pipe and descriptor ownership, fork or spawn lifecycles, signal cleanup, callbacks, bounded parallelism, output coordination, and shell-level integration testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** run-command.h documents child_process ownership, redirection, callbacks, and parallel APIs; run-command.c isolates launch, finish, cleanup, pipe, and scheduler responsibilities; the helper and shell suite directly cover I/O, missing commands, parallel tasks, output, and graceful abort.
- **Architecture:** The audited architecture of the path beginning at `run-command.h` has these boundaries: public child and parallel-process contract, launch, pipe, cleanup, and scheduler implementation, and dedicated helper and shell integration suite.
- **Naming and idiom:** `run-command.h` and its supporting files use these characteristic C mechanisms: function-pointer lifecycle and task callbacks, explicit child_process and parallel-process structures, and manual file-descriptor and pipe ownership.
- **Tests:** The helper in `t/helper/test-run-command.c` exposes child-process scenarios to `t/t0061-run-command.sh`, whose shell assertions cover input and output, missing commands, parallel tasks, coordinated output, and graceful abort.
- **Documentation:** `run-command.h` and its selected supporting material document the contracts needed to understand how Git starts, communicates with, cleans up, and optionally schedules child processes in portable C infrastructure.
- **Traceability:** Begin with child_process initialization, arguments, environment, redirection, cleanup, and callback contracts, follow start_command through pipe creation and fork, spawn, or exec setup into finish and signal cleanup, then trace pipe_command and the parallel scheduler's task admission, output buffering, abort, and completion behavior; close with the dedicated helper and t0061 tests.
- **Maintainability:** Changes to the path beginning at `run-command.h` are constrained by these audited guarantees: fork, exec, and platform-specific spawn portability, descriptor closure and deadlock avoidance on every failure path, and signal cleanup, graceful abort, and deterministic output.
- **Educational value:** Understand how Git starts, communicates with, cleans up, and optionally schedules child processes in portable C infrastructure. The path is domain-neutral process infrastructure; it teaches transferable subprocess API design, pipe and descriptor ownership, fork or spawn lifecycles, signal cleanup, callbacks, bounded parallelism, output coordination, and shell-level integration testing.

**Inspection record:** commit `c73e85354c275c9d409b26445089bc16940fc527`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `run-command.h`, `run-command.c`, `t/helper/test-run-command.c`, `t/t0061-run-command.sh`, `COPYING`. GitHub Linguist label: C.

</details>

### [libcheck/check](https://github.com/libcheck/check)

**Language 4 / Behavior 4 / Design 3 / Constraints 4 → Level 4**

**Source:** Production software

A unit testing framework for C with fork-based isolation, fixtures, timeouts, diagnostics, and multiple output formats.

**Why study it:** Understand how Check turns public assertion macros and registered test cases into isolated executions and reliable parent-process results. Testing concepts need little special background; the path teaches transferable macro/API design, process isolation, signal and timeout control, interprocess result transport, lifecycle orchestration, and self-testing.

**Short context:**

- A C test framework registers suites and cases, runs tests in-process or in child processes, and reports assertion failures, signals, exits, and timeouts.

**Prerequisites:**

- Working familiarity with C functions, pointers, structs, enums, arrays, manual allocation, function pointers, and focused tests, plus experience tracing behavior across several production files.
- A C test framework registers suites and cases, runs tests in-process or in child processes, and reports assertion failures, signals, exits, and timeouts.

**Concepts this path develops:**

- Public variadic assertion macro machinery.
- Fork and no-fork execution lifecycles.
- Portable fork and no-fork modes.

**What you can learn:**

- Study these transferable C mechanisms in `src/check.h.in`: public variadic assertion macro machinery, function-pointer test and fixture callbacks, and manual packed message representation.
- Trace these states and branches from `src/check.h.in` through its selected supporting files: fork and no-fork execution lifecycles, signal, exit, assertion, and timeout outcomes, and setup, test, teardown, and result transitions.
- Identify these architectural responsibilities in the path beginning at `src/check.h.in`: public macro and registration contract, runner and subprocess boundary, message and packing helpers, and direct framework self-tests.
- Study these change constraints for the path beginning at `src/check.h.in`: portable fork and no-fork modes, signal and timeout correctness, and failure-safe interprocess reporting.

**Learning path:**

- **Goal:** Understand how Check turns public assertion macros and registered test cases into isolated executions and reliable parent-process results.
- **Start here:** [`src/check.h.in`](https://github.com/libcheck/check/blob/35d9cc011faa0545bf56d5062ae90bbc2688eba7/src/check.h.in) — Begin with `src/check.h.in` because it exposes how Check turns public assertion macros and registered test cases into isolated executions and reliable parent-process results.
- **Then read:**
  - [`src/check.c`](https://github.com/libcheck/check/blob/35d9cc011faa0545bf56d5062ae90bbc2688eba7/src/check.c)
  - [`src/check_run.c`](https://github.com/libcheck/check/blob/35d9cc011faa0545bf56d5062ae90bbc2688eba7/src/check_run.c)
  - [`src/check_msg.c`](https://github.com/libcheck/check/blob/35d9cc011faa0545bf56d5062ae90bbc2688eba7/src/check_msg.c)
  - [`src/check_pack.c`](https://github.com/libcheck/check/blob/35d9cc011faa0545bf56d5062ae90bbc2688eba7/src/check_pack.c)
  - [`tests/check_check_sub.c`](https://github.com/libcheck/check/blob/35d9cc011faa0545bf56d5062ae90bbc2688eba7/tests/check_check_sub.c)
  - [`tests/check_check_fork.c`](https://github.com/libcheck/check/blob/35d9cc011faa0545bf56d5062ae90bbc2688eba7/tests/check_check_fork.c)
- **Trace:** Begin with START_TEST and assertion macro expansion in the public contract, follow suite and case registration through check_run's fork or no-fork lifecycle, signal, exit and timeout classification, then trace check_msg and check_pack result transport back to the runner; close with the subprocess and fork-mode self-tests.

**Why this level:**

- **Language technique 4:** Macro metaprogramming, callbacks, and explicit representation materially shape the framework path.
- **Behavioral reasoning 4:** Several advanced process and lifecycle states recur, but the lower-anchor rule does not elevate the bounded runner to expert nonlocal behavior.
- **Design span 3:** Several clear components collaborate while remaining within one test-execution subsystem.
- **Constraint burden 4:** Portability, isolation, cleanup, and stable result guarantees interact throughout the path.
- **Placement:** The four scores 4/4/3/4 sum to 15; their arithmetic mean is 3.75 and rounds half-up to Level 4. The published result is Level 4.

**License:** LGPL-2.1-or-later ([evidence 1](https://github.com/libcheck/check/blob/35d9cc011faa0545bf56d5062ae90bbc2688eba7/COPYING.LESSER))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The project publishes the Check library and checkmk tool used to build and run isolated native test suites.

**Language evidence:** Test registration, fixtures, isolated execution, timeout and signal handling, result transport, logging, and the checkmk generator are implemented principally in C.

**Coding relevance:**

Testing concepts need little special background; the path teaches transferable macro/API design, process isolation, signal and timeout control, interprocess result transport, lifecycle orchestration, and self-testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The public macro contract, registration model, runner, message transport, and serialization are separated into named modules; direct self-tests cover assertions, subprocess isolation, fixtures, signals, exits, timeouts, and fork versus no-fork modes, closing a demanding but coherent trace.
- **Architecture:** The audited architecture of the path beginning at `src/check.h.in` has these boundaries: public macro and registration contract, runner and subprocess boundary, message and packing helpers, and direct framework self-tests.
- **Naming and idiom:** `src/check.h.in` and its supporting files use these characteristic C mechanisms: public variadic assertion macro machinery, function-pointer test and fixture callbacks, and manual packed message representation.
- **Tests:** Direct tests in `tests/check_check_sub.c` and `tests/check_check_fork.c` cover these states and branches in the selected path: fork and no-fork execution lifecycles, signal, exit, assertion, and timeout outcomes, and setup, test, teardown, and result transitions.
- **Documentation:** `src/check.h.in` and its selected supporting material document the contracts needed to understand how Check turns public assertion macros and registered test cases into isolated executions and reliable parent-process results.
- **Traceability:** Begin with START_TEST and assertion macro expansion in the public contract, follow suite and case registration through check_run's fork or no-fork lifecycle, signal, exit and timeout classification, then trace check_msg and check_pack result transport back to the runner; close with the subprocess and fork-mode self-tests.
- **Maintainability:** Changes to the path beginning at `src/check.h.in` are constrained by these audited guarantees: portable fork and no-fork modes, signal and timeout correctness, and failure-safe interprocess reporting.
- **Educational value:** Understand how Check turns public assertion macros and registered test cases into isolated executions and reliable parent-process results. Testing concepts need little special background; the path teaches transferable macro/API design, process isolation, signal and timeout control, interprocess result transport, lifecycle orchestration, and self-testing.

**Inspection record:** commit `35d9cc011faa0545bf56d5062ae90bbc2688eba7`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/check.h.in`, `src/check.c`, `src/check_run.c`, `src/check_msg.c`, `src/check_pack.c`, `tests/check_check_sub.c`, `tests/check_check_fork.c`, `COPYING.LESSER`. GitHub Linguist label: C.

</details>

## Level 5 — Expert

_Ordered from gentler to more demanding within this Level._

### [curl/curl](https://github.com/curl/curl)

**Language 4 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

**Source:** Production software

A command-line data transfer tool and reusable library supporting URL-based communication across many protocols and platforms.

**Why study it:** Understand how curl's multi engine schedules and advances many transfer state machines through caller-driven perform, poll, timeout, wakeup, and completion APIs. Protocol-specific handlers remain adapter boundaries; the selected engine teaches transferable cooperative state-machine scheduling, opaque-handle APIs, socket and timer integration, wakeups, lifecycle ownership, error propagation, and event-loop testing.

**Short context:**

- The curl multi interface advances multiple transfers without blocking and tells callers which sockets or timeouts should drive the next step.

**Prerequisites:**

- Strong working familiarity with C functions, pointers, structs, enums, arrays, manual allocation, function pointers, and focused tests, plus experience tracing state, resources, or asynchronous control flow across many production files.
- The curl multi interface advances multiple transfers without blocking and tells callers which sockets or timeouts should drive the next step.

**Concepts this path develops:**

- Opaque public and internal handle representations.
- Many concurrent transfer state machines.
- Handle ownership, removal, cleanup, and reentrancy.

**What you can learn:**

- Study these transferable C mechanisms in `lib/multi.c`: opaque public and internal handle representations, callback and socket-operation function pointers, and intrusive transfer and message collections.
- Trace these states and branches from `lib/multi.c` through its selected supporting files: many concurrent transfer state machines, perform, socket, timer, poll, wakeup, completion, and removal transitions, and reentrant and error-driven lifecycle changes.
- Identify these architectural responsibilities in the path beginning at `lib/multi.c`: public multi API, internal multihandle and scheduler, protocol adapters at the selected boundary, and public-API integration tests and data.
- Study these change constraints for the path beginning at `lib/multi.c`: handle ownership, removal, cleanup, and reentrancy, socket, timer, poll, and wakeup interoperability, and cross-platform event-loop and stable public-API compatibility.

**Learning path:**

- **Goal:** Understand how curl's multi engine schedules and advances many transfer state machines through caller-driven perform, poll, timeout, wakeup, and completion APIs.
- **Start here:** [`lib/multi.c`](https://github.com/curl/curl/blob/c2a04c080d79e1eb5d99bc0a73fd71710aa6d345/lib/multi.c) — Begin with `lib/multi.c` because it exposes how curl's multi engine schedules and advances many transfer state machines through caller-driven perform, poll, timeout, wakeup, and completion APIs.
- **Then read:**
  - [`include/curl/multi.h`](https://github.com/curl/curl/blob/c2a04c080d79e1eb5d99bc0a73fd71710aa6d345/include/curl/multi.h)
  - [`lib/multihandle.h`](https://github.com/curl/curl/blob/c2a04c080d79e1eb5d99bc0a73fd71710aa6d345/lib/multihandle.h)
  - [`tests/libtest/lib1531.c`](https://github.com/curl/curl/blob/c2a04c080d79e1eb5d99bc0a73fd71710aa6d345/tests/libtest/lib1531.c)
  - [`tests/libtest/lib3105.c`](https://github.com/curl/curl/blob/c2a04c080d79e1eb5d99bc0a73fd71710aa6d345/tests/libtest/lib3105.c)
  - [`tests/libtest/lib2414.c`](https://github.com/curl/curl/blob/c2a04c080d79e1eb5d99bc0a73fd71710aa6d345/tests/libtest/lib2414.c)
  - [`tests/data/test1531`](https://github.com/curl/curl/blob/c2a04c080d79e1eb5d99bc0a73fd71710aa6d345/tests/data/test1531)
  - [`tests/data/test3105`](https://github.com/curl/curl/blob/c2a04c080d79e1eb5d99bc0a73fd71710aa6d345/tests/data/test3105)
  - [`tests/data/test2414`](https://github.com/curl/curl/blob/c2a04c080d79e1eb5d99bc0a73fd71710aa6d345/tests/data/test2414)
- **Trace:** Begin with the public CURLM lifecycle and multi.c's add, perform, poll, wakeup, info-read, remove, and cleanup paths; follow a transfer through the internal multihandle scheduler while protocol handlers remain adapters, then close with lib1531's perform/fdset/timeout/completion flow, lib3105's repeated removal, lib2414's wakeup-to-poll exit, and their matching test definitions.

**Why this level:**

- **Language technique 4:** Advanced C API and representation techniques recur across the engine, while the hardest work lies in behavior and constraints.
- **Behavioral reasoning 5:** Multiple nonlocal asynchronous lifecycles interact repeatedly across caller actions, scheduler passes, timers, sockets, and callbacks.
- **Design span 4:** Several substantial components must be understood together, but the representative trace excludes protocol implementation breadth.
- **Constraint burden 5:** Expert lifecycle, concurrency, portability, and compatibility guarantees recur throughout ordinary multi-engine work.
- **Placement:** The four scores 4/5/4/5 sum to 18; their arithmetic mean is 4.50 and rounds half-up to Level 5. The published result is Level 5.

**License:** curl ([evidence 1](https://github.com/curl/curl/blob/c2a04c080d79e1eb5d99bc0a73fd71710aa6d345/COPYING))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository builds curl and libcurl, widely deployed for command-line transfers and embedded network clients across operating systems and devices.

**Language evidence:** Protocol engines, connection reuse, DNS, proxies, TLS adapters, HTTP versions, the multi state machine, URL API, and command-line tool are C under lib/ and src/.

**Coding relevance:**

Protocol-specific handlers remain adapter boundaries; the selected engine teaches transferable cooperative state-machine scheduling, opaque-handle APIs, socket and timer integration, wakeups, lifecycle ownership, error propagation, and event-loop testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The public multi contract and internal multihandle state are explicit, multi.c centralizes scheduling and lifecycle invariants, and three verified libtests plus matching data drive ordinary progress, duplicate removal, and wakeup-to-poll behavior through the public API.
- **Architecture:** The audited architecture of the path beginning at `lib/multi.c` has these boundaries: public multi API, internal multihandle and scheduler, protocol adapters at the selected boundary, and public-API integration tests and data.
- **Naming and idiom:** `lib/multi.c` and its supporting files use these characteristic C mechanisms: opaque public and internal handle representations, callback and socket-operation function pointers, and intrusive transfer and message collections.
- **Tests:** The public-API libtests `tests/libtest/lib1531.c`, `tests/libtest/lib3105.c`, and `tests/libtest/lib2414.c`, together with their matching `tests/data` definitions, cover perform, fd-set and timeout progress through completion, repeated removal, and wakeup-driven poll exit.
- **Documentation:** `lib/multi.c` and its selected supporting material document the contracts needed to understand how curl's multi engine schedules and advances many transfer state machines through caller-driven perform, poll, timeout, wakeup, and completion APIs.
- **Traceability:** Begin with the public CURLM lifecycle and multi.c's add, perform, poll, wakeup, info-read, remove, and cleanup paths; follow a transfer through the internal multihandle scheduler while protocol handlers remain adapters, then close with lib1531's perform/fdset/timeout/completion flow, lib3105's repeated removal, lib2414's wakeup-to-poll exit, and their matching test definitions.
- **Maintainability:** Changes to the path beginning at `lib/multi.c` are constrained by these audited guarantees: handle ownership, removal, cleanup, and reentrancy, socket, timer, poll, and wakeup interoperability, and cross-platform event-loop and stable public-API compatibility.
- **Educational value:** Understand how curl's multi engine schedules and advances many transfer state machines through caller-driven perform, poll, timeout, wakeup, and completion APIs. Protocol-specific handlers remain adapter boundaries; the selected engine teaches transferable cooperative state-machine scheduling, opaque-handle APIs, socket and timer integration, wakeups, lifecycle ownership, error propagation, and event-loop testing.

**Inspection record:** commit `c2a04c080d79e1eb5d99bc0a73fd71710aa6d345`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `lib/multi.c`, `include/curl/multi.h`, `lib/multihandle.h`, `tests/libtest/lib1531.c`, `tests/libtest/lib3105.c`, `tests/libtest/lib2414.c`, `tests/data/test1531`, `tests/data/test3105`, `tests/data/test2414`, `COPYING`. GitHub Linguist label: C.

</details>

### [libevent/libevent](https://github.com/libevent/libevent)

**Language 4 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

**Source:** Production software

A portable asynchronous event-notification library with event loops, buffered streams, networking protocols, and threading support.

**Why study it:** Understand how Libevent coordinates I/O readiness and timeouts through a portable event-base loop and dispatches callbacks safely. The operating-system vocabulary is concise; the selected core loop teaches transferable scheduling, callback lifecycles, readiness maps, timeout heaps, backend abstraction, reentrancy, synchronization, and resource cleanup without unrelated protocol breadth.

**Short context:**

- An event loop registers I/O and timeout interests with an operating-system backend, activates ready events, and dispatches callbacks by priority.

**Prerequisites:**

- Strong working familiarity with C functions, pointers, structs, enums, arrays, manual allocation, function pointers, and focused tests, plus experience tracing state, resources, or asynchronous control flow across many production files.
- An event loop registers I/O and timeout interests with an operating-system backend, activates ready events, and dispatches callbacks by priority.

**Concepts this path develops:**

- Opaque public handles and internal structures.
- Registered, ready, active, executing, persistent, and deleted event states.
- Cross-platform backend and readiness semantics.

**What you can learn:**

- Study these transferable C mechanisms in `event.c`: opaque public handles and internal structures, callback function pointers and backend operation tables, and intrusive queues, maps, and timeout heap.
- Trace these states and branches from `event.c` through its selected supporting files: registered, ready, active, executing, persistent, and deleted event states, interleaved I/O, timeout, priority, and thread-notification transitions, and reentrant callback changes to the same event base.
- Identify these architectural responsibilities in the path beginning at `event.c`: public event API and event-base core, I/O mapping and timeout scheduling, pluggable epoll backend, and core and edge-triggered regression tests.
- Study these change constraints for the path beginning at `event.c`: cross-platform backend and readiness semantics, callback reentrancy, deletion, and persistence safety, and thread notification, locking, priority, and timeout correctness.

**Learning path:**

- **Goal:** Understand how Libevent coordinates I/O readiness and timeouts through a portable event-base loop and dispatches callbacks safely.
- **Start here:** [`event.c`](https://github.com/libevent/libevent/blob/335349b9b60c860289c6c47eadadadf18dc58211/event.c) — Begin with `event.c` because it exposes how Libevent coordinates I/O readiness and timeouts through a portable event-base loop and dispatches callbacks safely.
- **Then read:**
  - [`include/event2/event.h`](https://github.com/libevent/libevent/blob/335349b9b60c860289c6c47eadadadf18dc58211/include/event2/event.h)
  - [`event-internal.h`](https://github.com/libevent/libevent/blob/335349b9b60c860289c6c47eadadadf18dc58211/event-internal.h)
  - [`evmap.c`](https://github.com/libevent/libevent/blob/335349b9b60c860289c6c47eadadadf18dc58211/evmap.c)
  - [`epoll.c`](https://github.com/libevent/libevent/blob/335349b9b60c860289c6c47eadadadf18dc58211/epoll.c)
  - [`minheap-internal.h`](https://github.com/libevent/libevent/blob/335349b9b60c860289c6c47eadadadf18dc58211/minheap-internal.h)
  - [`test/regress.c`](https://github.com/libevent/libevent/blob/335349b9b60c860289c6c47eadadadf18dc58211/test/regress.c)
  - [`test/regress_et.c`](https://github.com/libevent/libevent/blob/335349b9b60c860289c6c47eadadadf18dc58211/test/regress_et.c)
- **Trace:** Start at event_base_loop, follow event addition through evmap registration and the epoll backend, place timeout events in the min-heap, then trace readiness and expiration into priority activation and callback dispatch, including persistence, deletion, reentrancy, and thread notification; close with the core and edge-triggered regression tests.

**Why this level:**

- **Language technique 4:** Advanced C representation and callback techniques recur throughout the core without becoming the primary expert burden.
- **Behavioral reasoning 5:** Multiple nonlocal state machines and callback lifecycles interact repeatedly across the loop, backend, maps, heap, and user callbacks.
- **Design span 4:** Several substantial subsystem boundaries must be understood together, while protocol handlers remain outside the selected trace.
- **Constraint burden 5:** Expert portability, lifecycle, concurrency, and scheduling guarantees recur throughout ordinary core-loop changes.
- **Placement:** The four scores 4/5/4/5 sum to 18; their arithmetic mean is 4.50 and rounds half-up to Level 5. The published result is Level 5.

**License:** BSD-3-Clause ([evidence 1](https://github.com/libevent/libevent/blob/335349b9b60c860289c6c47eadadadf18dc58211/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The project releases a native library used by network servers and clients to multiplex I/O across operating-system backends.

**Language evidence:** Event loops, platform polling backends, buffered I/O, listeners, DNS, HTTP, RPC, TLS adapters, threading, timers, and utilities are C across the repository root and include/.

**Coding relevance:**

The operating-system vocabulary is concise; the selected core loop teaches transferable scheduling, callback lifecycles, readiness maps, timeout heaps, backend abstraction, reentrancy, synchronization, and resource cleanup without unrelated protocol breadth.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The public event contract, loop, I/O map, timeout heap, and epoll backend have explicit boundaries and invariants; the broad regression harness and edge-triggered tests exercise registration, activation, persistence, priorities, timeouts, deletion, reentrancy, and backend behavior.
- **Architecture:** The audited architecture of the path beginning at `event.c` has these boundaries: public event API and event-base core, I/O mapping and timeout scheduling, pluggable epoll backend, and core and edge-triggered regression tests.
- **Naming and idiom:** `event.c` and its supporting files use these characteristic C mechanisms: opaque public handles and internal structures, callback function pointers and backend operation tables, and intrusive queues, maps, and timeout heap.
- **Tests:** Direct tests in `test/regress.c` and `test/regress_et.c` cover these states and branches in the selected path: registered, ready, active, executing, persistent, and deleted event states, interleaved I/O, timeout, priority, and thread-notification transitions, and reentrant callback changes to the same event base.
- **Documentation:** `event.c` and its selected supporting material document the contracts needed to understand how Libevent coordinates I/O readiness and timeouts through a portable event-base loop and dispatches callbacks safely.
- **Traceability:** Start at event_base_loop, follow event addition through evmap registration and the epoll backend, place timeout events in the min-heap, then trace readiness and expiration into priority activation and callback dispatch, including persistence, deletion, reentrancy, and thread notification; close with the core and edge-triggered regression tests.
- **Maintainability:** Changes to the path beginning at `event.c` are constrained by these audited guarantees: cross-platform backend and readiness semantics, callback reentrancy, deletion, and persistence safety, and thread notification, locking, priority, and timeout correctness.
- **Educational value:** Understand how Libevent coordinates I/O readiness and timeouts through a portable event-base loop and dispatches callbacks safely. The operating-system vocabulary is concise; the selected core loop teaches transferable scheduling, callback lifecycles, readiness maps, timeout heaps, backend abstraction, reentrancy, synchronization, and resource cleanup without unrelated protocol breadth.

**Inspection record:** commit `335349b9b60c860289c6c47eadadadf18dc58211`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `event.c`, `include/event2/event.h`, `event-internal.h`, `evmap.c`, `epoll.c`, `minheap-internal.h`, `test/regress.c`, `test/regress_et.c`, `LICENSE`. GitHub Linguist label: C.

</details>

_Generated from `catalog/c.json`; do not edit by hand._

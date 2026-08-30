# Go

10 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

**Source legend:** Production software is built primarily for real users or systems. Educational exemplars are complete teaching-oriented software and may appear only at Levels 1 and 2.

[← All languages](../README.md)

## Level 1 — First real code

### [golang/go](https://github.com/golang/go)

**Language 1 / Behavior 1 / Design 2 / Constraints 1 → Level 1**

**Source:** Production software

Go's standard strings.Cut function splits text around the first separator and returns an explicit found result for the missing case.

**Why study it:** Follow one standard-library string operation from its public entry through a direct branch, then check beginning, middle, end, empty, and missing separators in table tests.

**Prerequisites:**

- The global novice Go baseline: functions, strings, conditionals, packages, multiple return values, slices of strings, and focused tests.
- Index returns the first separator position or -1; string slicing uses byte offsets and does not copy the underlying text.

**Concepts this path develops:**

- Splitting once without discarding whether a separator was present.
- Using string slices before and after a located boundary.
- Defining exact empty and missing cases with a compact test table.

**What you can learn:**

- Find the first occurrence of a separator and slice around it.
- Return several named results so callers can distinguish an empty piece from a missing separator.
- Use a table to cover separator positions and empty-string boundaries.

**Learning path:**

- **Goal:** Understand how Go's strings.Cut returns the text around the first separator without confusing an empty result with a separator that was not found.
- **Start here:** [`src/strings/strings.go`](https://github.com/golang/go/blob/603439a1c6f2d37c7f02e246342847056ed04c21/src/strings/strings.go) — The public documentation and entry point establish the exact three-result contract.
- **Then read:**
  - [`src/internal/stringslite/strings.go`](https://github.com/golang/go/blob/603439a1c6f2d37c7f02e246342847056ed04c21/src/internal/stringslite/strings.go)
  - [`src/strings/strings_test.go`](https://github.com/golang/go/blob/603439a1c6f2d37c7f02e246342847056ed04c21/src/strings/strings_test.go)
  - [`src/strings/example_test.go`](https://github.com/golang/go/blob/603439a1c6f2d37c7f02e246342847056ed04c21/src/strings/example_test.go)
  - [`README.md`](https://github.com/golang/go/blob/603439a1c6f2d37c7f02e246342847056ed04c21/README.md)
- **Trace:** Enter strings.Cut, follow the standard library's shared stringslite implementation, locate the first separator, return the two slices and true or the original string, empty suffix, and false, then compare all eight boundary rows and the four printed examples.

**Why this level:**

- **Language technique 1:** The implementation uses introductory Go string, branch, package, and multiple-return syntax.
- **Behavioral reasoning 1:** One index result selects between two local deterministic returns.
- **Design span 2:** Two clear standard-library modules share the implementation while keeping the selected trace short.
- **Constraint burden 1:** A small local contract and plainly observable outputs dominate the behavior.
- **Novice accessibility floor 1:** All central operations are introductory Go, and the internal sharing boundary needs only one sentence before every test row is predictable.
  - **Central concepts:** finding a substring; string slicing; multiple return values
  - **Incidental concepts:** the public package reuses a small internal implementation
- **Placement:** The four scores 1/1/2/1 produce rubric Level 1. Novice accessibility floor 1 preserves published Level 1.

**License:** BSD-3-Clause ([evidence 1](https://github.com/golang/go/blob/603439a1c6f2d37c7f02e246342847056ed04c21/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** golang/go is the official implementation of the Go language and standard library, where strings.Cut is a stable application-facing API.

**Language evidence:** The public strings API, shared stringslite implementation, examples, and table tests are first-party Go in the official language repository.

**Coding relevance:**

One-time splitting, explicit success results, boundary slicing, and table tests are broadly reusable programming techniques.

No specialist domain context is required.

**Eight-part quality gate:**

- **Source quality:** The implementation states the successful slices and missing fallback directly, with no mutable state or duplicated search.
- **Architecture:** The public facade and shared lightweight implementation have an explicit narrow boundary used inside the standard library.
- **Naming and idiom:** Cut, before, after, found, separator, and Index follow standard Go string vocabulary.
- **Tests:** Eight table rows cover separators at every position, the whole string, the empty separator, absent separators, and empty input; executable examples show the public results.
- **Documentation:** The public comment defines the first-match rule, all return values, and the missing case, while examples print representative calls.
- **Traceability:** Each internal return maps directly to table columns and a printed example.
- **Maintainability:** A stable public contract, shared implementation, and exhaustive small boundary table make changes easy to review.
- **Educational value:** The path is a gentle introduction to multiple returns and precise boundary behavior in production Go.

**Inspection record:** commit `603439a1c6f2d37c7f02e246342847056ed04c21`, inspected 2026-08-30. Review passes: Codex follow-up lower-level investigation; Codex resumed-session source verification. Files inspected: `src/strings/strings.go`, `src/internal/stringslite/strings.go`, `src/strings/strings_test.go`, `src/strings/example_test.go`, `README.md`, `LICENSE`. GitHub Linguist label: Go.

</details>

## Level 2 — Guided real-world patterns

### [dustin/go-humanize](https://github.com/dustin/go-humanize)

**Language 2 / Behavior 2 / Design 1 / Constraints 3 → Level 2**

**Source:** Production software

A production Go formatter that writes any signed 64-bit integer with comma-separated three-digit groups.

**Why study it:** Trace a visible number-to-string algorithm while learning how production code handles signs, exact buffer sizing, and the one integer that cannot be negated.

**Prerequisites:**

- The global novice Go baseline: functions, integers, loops, conditionals, slices, packages, and focused tests.
- Signed int64 ranges from -9,223,372,036,854,775,808 through 9,223,372,036,854,775,807, so its minimum value has no positive int64 counterpart.

**Concepts this path develops:**

- Building formatted output backward into a pre-sized buffer.
- Handling a numeric boundary before the ordinary algorithm.
- Combining example tables with a property-based fuzz check.

**What you can learn:**

- Count decimal digits and allocate exactly enough output space for digits, separators, and a sign.
- Fill a byte slice from right to left while inserting every third separator.
- Protect the minimum signed integer boundary and verify general formatting properties with fuzz tests.

**Learning path:**

- **Goal:** Understand how go-humanize Comma formats every int64 exactly and how examples plus a fuzz property defend the contract.
- **Start here:** [`comma.go`](https://github.com/dustin/go-humanize/blob/4d1d9082551ec085912e7d2253a33ae547fca000/comma.go) — The Comma function contains the fast path, minimum-integer guard, digit count, allocation, sign handling, and backward fill.
- **Then read:**
  - [`comma_test.go`](https://github.com/dustin/go-humanize/blob/4d1d9082551ec085912e7d2253a33ae547fca000/comma_test.go)
  - [`comma_fuzz_test.go`](https://github.com/dustin/go-humanize/blob/4d1d9082551ec085912e7d2253a33ae547fca000/comma_fuzz_test.go)
  - [`README.markdown`](https://github.com/dustin/go-humanize/blob/4d1d9082551ec085912e7d2253a33ae547fca000/README.markdown)
- **Trace:** Take an int64 through the small-number shortcut or minimum-value guard, count digits and separators, make the exact byte slice, write digits and commas from right to left, restore a negative sign, then compare table boundaries and the fuzz invariant that removing commas reproduces strconv.FormatInt.

**Why this level:**

- **Language technique 2:** Manual byte formatting and a local bitwise optimization are common professional techniques beyond the simplest string conversion.
- **Behavioral reasoning 2:** Several local states and boundary branches matter, but every step is synchronous and directly traceable.
- **Design span 1:** One implementation unit and its focused tests contain the complete selected contract.
- **Constraint burden 3:** Several material numeric and formatting guarantees recur even though the implementation is compact.
- **Novice accessibility floor 2:** A short primer on the int64 minimum and backward filling makes representative outputs predictable; the fast path can be explained as one local optimization.
  - **Central concepts:** backward buffer construction; three-digit grouping; signed integer boundary handling
  - **Incidental concepts:** the bitwise fast-path expression
- **Placement:** The four scores 2/2/1/3 produce rubric Level 2. Novice accessibility floor 2 preserves published Level 2.

**License:** MIT ([evidence 1](https://github.com/dustin/go-humanize/blob/4d1d9082551ec085912e7d2253a33ae547fca000/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** go-humanize is a maintained importable Go module whose README documents application-facing number, size, time, and text formatting functions.

**Language evidence:** The integer formatter, example documentation, table tests, and fuzz property are first-party Go; GitHub labels the repository Go.

**Coding relevance:**

Buffer construction, boundary handling, deterministic formatting, and property-focused testing are broadly transferable implementation practices.

No specialist domain context is required.

**Eight-part quality gate:**

- **Source quality:** The ordinary path is linear, the exceptional minimum value is explicit, and each counter has one visible role.
- **Architecture:** A focused formatter is accompanied by separate example and property tests without unnecessary abstraction.
- **Naming and idiom:** count, output, counter, and Comma communicate the buffer construction directly using standard Go slices and loops.
- **Tests:** Table cases cover sizes, signs, maximum and minimum int64, while the fuzz test checks digit preservation, sign, and separator positions over arbitrary inputs.
- **Documentation:** The README gives exact number mappings, import instructions, and an application-style formatting example.
- **Traceability:** Every branch and invariant in Comma has a corresponding boundary example or fuzz assertion.
- **Maintainability:** The full-range contract is explicit and protected by both examples and a general property, reducing untested numeric corners.
- **Educational value:** It introduces careful production formatting through a concrete algorithm whose safeguards remain understandable.

**Inspection record:** commit `4d1d9082551ec085912e7d2253a33ae547fca000`, inspected 2026-08-30. Review passes: Codex lower-level expansion pass. Files inspected: `comma.go`, `comma_test.go`, `comma_fuzz_test.go`, `README.markdown`, `go.mod`, `LICENSE`. GitHub Linguist label: Go.

</details>

### [mitchellh/go-wordwrap](https://github.com/mitchellh/go-wordwrap)

**Language 2 / Behavior 2 / Design 1 / Constraints 2 → Level 2**

**Source:** Production software

A small production Go package that wraps text at whitespace while preserving explicit newlines, long words, and nonbreaking spaces.

**Why study it:** Follow a practical stateful string transformation through pending spaces, words, explicit line breaks, and Unicode characters with a thorough table of examples.

**Prerequisites:**

- The global novice Go baseline: functions, strings, loops, conditionals, packages, and focused tests.
- A rune is one Unicode code point; bytes.Buffer accumulates output without repeated string concatenation.

**Concepts this path develops:**

- Delaying whitespace output until the next word determines whether a line fits.
- Maintaining local counters alongside word and space buffers.
- Separating explicit line breaks from automatic wrapping decisions.

**What you can learn:**

- Accumulate a pending word and whitespace separately until a wrapping decision is possible.
- Distinguish breakable whitespace from explicit newlines and nonbreaking spaces.
- Use boundary examples to define trailing-space, long-word, and multi-byte behavior.

**Learning path:**

- **Goal:** Understand how WrapString inserts line breaks only at breakable whitespace while preserving the package's explicit text contracts.
- **Start here:** [`wordwrap.go`](https://github.com/mitchellh/go-wordwrap/blob/ecf0936a077a4bd73a1cc2ac5c370f2b55618d62/wordwrap.go) — The sole function contains the pending word, whitespace, width counters, newline cases, and final buffer flush.
- **Then read:**
  - [`wordwrap_test.go`](https://github.com/mitchellh/go-wordwrap/blob/ecf0936a077a4bd73a1cc2ac5c370f2b55618d62/wordwrap_test.go)
  - [`README.md`](https://github.com/mitchellh/go-wordwrap/blob/ecf0936a077a4bd73a1cc2ac5c370f2b55618d62/README.md)
- **Trace:** Scan each rune into a word or space buffer, flush completed pieces when whitespace or an explicit newline resolves them, insert an automatic newline when the next word would exceed the limit, finish the remaining buffers, and compare each boundary with the table test.

**Why this level:**

- **Language technique 2:** Rune-aware scanning and incremental buffers are common professional Go techniques central to the function.
- **Behavioral reasoning 2:** Several local states interact, but they move forward through the input in one synchronous pass.
- **Design span 1:** The entire path is one implementation unit plus its exhaustive examples.
- **Constraint burden 2:** Several routine text-boundary guarantees matter but remain local to the formatter.
- **Novice accessibility floor 2:** A short primer on buffers, runes, and pending spaces is enough to simulate each test; no text-layout theory or parser grammar is required.
  - **Central concepts:** incremental text buffering; pending whitespace; line-width state
  - **Incidental concepts:** Unicode rune representation; the nonbreaking-space code point
- **Placement:** The four scores 2/2/1/2 produce rubric Level 2. Novice accessibility floor 2 preserves published Level 2.

**License:** MIT ([evidence 1](https://github.com/mitchellh/go-wordwrap/blob/ecf0936a077a4bd73a1cc2ac5c370f2b55618d62/LICENSE.md))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository documents go-wordwrap as an importable package for formatting command-line output and exposes a stable WrapString API under an MIT license.

**Language evidence:** The complete wrapping implementation and its direct table test are first-party Go; GitHub labels the repository Go.

**Coding relevance:**

Incremental text transformation, local state, Unicode-aware scanning, and edge-case tests are transferable implementation skills.

No specialist domain context is required.

**Eight-part quality gate:**

- **Source quality:** The buffers and counters are explicit, comments explain the algorithm's intended limits, and control flow advances in one pass.
- **Architecture:** One exported function and one direct test table are proportionate to the package's focused responsibility.
- **Naming and idiom:** wordBuf, spaceBuf, current, and lim expose the pending state using conventional Go buffer and rune APIs.
- **Tests:** The direct table covers normal and long words, whitespace runs, explicit newlines, trailing spaces, nonbreaking spaces, and multi-byte characters.
- **Documentation:** The README states the CLI-formatting purpose, installation, usage, output, and the algorithm's deliberate simplicity.
- **Traceability:** Each named input category in the test follows a specific visible branch in WrapString.
- **Maintainability:** The documented non-goals and exhaustive boundary table constrain changes to one small public function.
- **Educational value:** The path demonstrates meaningful local state and Unicode-aware processing without requiring a parser or framework.

**Inspection record:** commit `ecf0936a077a4bd73a1cc2ac5c370f2b55618d62`, inspected 2026-08-30. Review passes: Codex lower-level expansion pass. Files inspected: `wordwrap.go`, `wordwrap_test.go`, `README.md`, `go.mod`, `LICENSE.md`. GitHub Linguist label: Go.

</details>

### [tidwall/match](https://github.com/tidwall/match)

**Language 1 / Behavior 2 / Design 1 / Constraints 3 → Level 2**

**Source:** Production software

A small Go matcher that checks text against ordinary characters, question marks, and stars.

**Why study it:** Follow a compact loop through literal matches, one-character matches, star backtracking, and the boundary where either the text or pattern ends.

**Short context:**

- A glob pattern uses literal bytes, question marks, and stars to decide whether a string matches.

**Prerequisites:**

- The global novice Go baseline: functions, byte slices, loops, conditionals, and table-driven tests.
- In this path, a question mark matches one byte and a star matches zero or more bytes.

**Concepts this path develops:**

- Walking text and pattern indexes together.
- Trying literal, one-byte, and star cases in a clear order.
- Backtracking to the most recent star when a later match fails.

**What you can learn:**

- Trace representative literal, question-mark, and star patterns by hand.
- See how one saved star position supports bounded backtracking.
- Use boundary-focused tests to understand empty and exhausted inputs.

**Learning path:**

- **Goal:** Understand how a compact Go matcher handles literal bytes, single-byte wildcards, star backtracking, and case folding.
- **Start here:** [`match.go`](https://github.com/tidwall/match/blob/afc69bce52e08c02e78156a7697bd808fc868ec5/match.go) — Begin with `match.go` because it exposes how a compact Go matcher handles literal bytes, single-byte wildcards, star backtracking, and case folding.
- **Then read:**
  - [`match_test.go`](https://github.com/tidwall/match/blob/afc69bce52e08c02e78156a7697bd808fc868ec5/match_test.go)
- **Trace:** Start with the main pattern and string scan, follow literal and question-mark consumption into the star branch and recursive or iterative suffix search, then compare the case-insensitive path; close with table tests and randomized TestRandomInput, which is randomized coverage rather than a Go Fuzz target.

**Why this level:**

- **Language technique 1:** The implementation relies on basic Go mechanics with no recurring intermediate language technique.
- **Behavioral reasoning 2:** A few related matcher states recur within one compact algorithm.
- **Design span 1:** The complete lesson stays within one local component and its tests.
- **Constraint burden 3:** Several material boundary and backtracking guarantees recur despite the tiny design span.
- **Novice accessibility floor 2:** The entire pattern language is three locally defined forms, so a short primer is sufficient even though star backtracking stretches beyond first-production-code reasoning.
  - **Central concepts:** literal and wildcard matching; star backtracking; input and pattern exhaustion
  - **Incidental concepts:** byte-oriented scanning; optional case folding
- **Placement:** The four structural scores 1/2/1/3 produce rubric Level 2 under the documented formula and guardrails. Novice accessibility floor 2 produces published Level 2.

**License:** MIT ([evidence 1](https://github.com/tidwall/match/blob/afc69bce52e08c02e78156a7697bd808fc868ec5/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository publishes an importable Go module for matching strings against wildcard patterns in applications and libraries.

**Language evidence:** The wildcard matcher, limit-aware traversal, Unicode handling, and public API are implemented in the root Go package.

**Coding relevance:**

Glob vocabulary is explained immediately; the path is programming-led and teaches byte scanning, local branching, star backtracking, case folding, and boundary-focused testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** match.go keeps the complete matcher and case-folding behavior in one compact implementation, while match_test.go covers literals, wildcards, empty strings, Unicode byte behavior, case-insensitive matching, adversarial patterns, and randomized TestRandomInput coverage.
- **Architecture:** The audited architecture of the path beginning at `match.go` has these boundaries: one matcher implementation and one direct test file.
- **Naming and idiom:** `match.go` and its supporting files use these characteristic Go mechanisms: plain byte slices and indexes, loops and local conditionals, and small helper functions.
- **Tests:** Direct tests in `match_test.go` cover these states and branches in the selected path: literal, question-mark, and star branches, empty and exhausted input states, and case-sensitive and insensitive modes.
- **Documentation:** `match.go` and its selected supporting material document the contracts needed to understand how a compact Go matcher handles literal bytes, single-byte wildcards, star backtracking, and case folding.
- **Traceability:** Start with the main pattern and string scan, follow literal and question-mark consumption into the star branch and recursive or iterative suffix search, then compare the case-insensitive path; close with table tests and randomized TestRandomInput, which is randomized coverage rather than a Go Fuzz target.
- **Maintainability:** Changes to the path beginning at `match.go` are constrained by these audited guarantees: stars may match zero or many bytes, pattern and input exhaustion must align, and case folding and arbitrary input must terminate consistently.
- **Educational value:** Understand how a compact Go matcher handles literal bytes, single-byte wildcards, star backtracking, and case folding. Glob vocabulary is explained immediately; the path is programming-led and teaches byte scanning, local branching, star backtracking, case folding, and boundary-focused testing.

**Inspection record:** commit `afc69bce52e08c02e78156a7697bd808fc868ec5`, inspected 2026-08-30. Review passes: Codex primary pass; independent Codex verification pass; Codex novice-accessibility audit. Files inspected: `match.go`, `match_test.go`, `LICENSE`. GitHub Linguist label: Go.

</details>

## Level 3 — Intermediate production software

### [gin-gonic/gin](https://github.com/gin-gonic/gin)

**Language 2 / Behavior 3 / Design 3 / Constraints 4 → Level 3**

**Source:** Production software

A high-performance HTTP web framework with routing, middleware, request binding, rendering, recovery, and server utilities.

**Why study it:** Understand how Gin carries one HTTP request from ServeHTTP through route lookup, parameter capture, a middleware chain, and pooled-context cleanup. HTTP routing vocabulary is concise; the bounded trace teaches pooling, radix-tree route lookup, parameter capture, middleware-chain indexing, abort behavior, response state, and integration tests without requiring Gin's binding or rendering breadth.

**Short context:**

- An HTTP engine matches a request method and path, prepares a reusable Context, and executes the selected handler chain.

**Prerequisites:**

- Basic familiarity with Go functions, structs and interfaces, slices and maps, errors, goroutines and channels at a basic level, and table-driven tests.
- An HTTP engine matches a request method and path, prepares a reusable Context, and executes the selected handler chain.

**Concepts this path develops:**

- Sync.Pool context reuse.
- Acquire, reset, route, handle, abort, respond, and release states.
- Pooled contexts must be fully reset between requests.

**What you can learn:**

- Study these transferable Go mechanisms in `gin.go`: sync.Pool context reuse, slice-backed handler chains, and tree and map-based routing.
- Trace these states and branches from `gin.go` through its selected supporting files: acquire, reset, route, handle, abort, respond, and release states, match, not-found, parameter, middleware, and error branches, and handler index progression.
- Identify these architectural responsibilities in the path beginning at `gin.go`: Engine entry and pool owner, routing tree, and Context handler-chain executor and focused tests.
- Study these change constraints for the path beginning at `gin.go`: pooled contexts must be fully reset between requests, route precedence and parameter capture must stay deterministic, and middleware order, aborts, and response state must remain coherent.

**Learning path:**

- **Goal:** Understand how Gin carries one HTTP request from ServeHTTP through route lookup, parameter capture, a middleware chain, and pooled-context cleanup.
- **Start here:** [`gin.go`](https://github.com/gin-gonic/gin/blob/dcaa4296d111981ffb31ac3eba90bb63e1eb5ab9/gin.go) — Begin with `gin.go` because it exposes how Gin carries one HTTP request from ServeHTTP through route lookup, parameter capture, a middleware chain, and pooled-context cleanup.
- **Then read:**
  - [`tree.go`](https://github.com/gin-gonic/gin/blob/dcaa4296d111981ffb31ac3eba90bb63e1eb5ab9/tree.go)
  - [`context.go`](https://github.com/gin-gonic/gin/blob/dcaa4296d111981ffb31ac3eba90bb63e1eb5ab9/context.go)
  - [`gin_test.go`](https://github.com/gin-gonic/gin/blob/dcaa4296d111981ffb31ac3eba90bb63e1eb5ab9/gin_test.go)
  - [`tree_test.go`](https://github.com/gin-gonic/gin/blob/dcaa4296d111981ffb31ac3eba90bb63e1eb5ab9/tree_test.go)
  - [`context_test.go`](https://github.com/gin-gonic/gin/blob/dcaa4296d111981ffb31ac3eba90bb63e1eb5ab9/context_test.go)
- **Trace:** Start at Engine.ServeHTTP, follow Context acquisition and reset into method-tree lookup and parameter capture, then trace handlers through Context.Next and abort behavior before the response and context return to the pool; close with focused engine, tree, and context tests.

**Why this level:**

- **Language technique 2:** Familiar Go collections, pooling, and method techniques recur without advanced language machinery.
- **Behavioral reasoning 3:** Several related request states recur within one bounded routing lifecycle.
- **Design span 3:** A few cohesive components span request entry through routing and handler completion.
- **Constraint burden 4:** Reuse, ordering, matching, and response guarantees recur in normal request handling.
- **Placement:** The four scores 2/3/3/4 sum to 12; their arithmetic mean is 3.00 and rounds half-up to Level 3. The published result is Level 3.

**License:** MIT ([evidence 1](https://github.com/gin-gonic/gin/blob/dcaa4296d111981ffb31ac3eba90bb63e1eb5ab9/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository publishes the Gin Go module for building HTTP services and documents supported production deployment patterns.

**Language evidence:** The HTTP engine, radix route trees, request context, middleware chain, binding, rendering, recovery, and server adapters are implemented in Go.

**Coding relevance:**

HTTP routing vocabulary is concise; the bounded trace teaches pooling, radix-tree route lookup, parameter capture, middleware-chain indexing, abort behavior, response state, and integration tests without requiring Gin's binding or rendering breadth.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** gin.go provides the production ServeHTTP entry and pooled-context lifecycle, tree.go isolates routing, context.go owns handler-chain progression, and focused engine, tree, and context tests cover matching, parameters, middleware, aborts, errors, reuse, and response behavior.
- **Architecture:** The audited architecture of the path beginning at `gin.go` has these boundaries: Engine entry and pool owner, routing tree, and Context handler-chain executor and focused tests.
- **Naming and idiom:** `gin.go` and its supporting files use these characteristic Go mechanisms: sync.Pool context reuse, slice-backed handler chains, and tree and map-based routing.
- **Tests:** Direct tests in `gin_test.go`, `tree_test.go`, and `context_test.go` cover these states and branches in the selected path: acquire, reset, route, handle, abort, respond, and release states, match, not-found, parameter, middleware, and error branches, and handler index progression.
- **Documentation:** `gin.go` and its selected supporting material document the contracts needed to understand how Gin carries one HTTP request from ServeHTTP through route lookup, parameter capture, a middleware chain, and pooled-context cleanup.
- **Traceability:** Start at Engine.ServeHTTP, follow Context acquisition and reset into method-tree lookup and parameter capture, then trace handlers through Context.Next and abort behavior before the response and context return to the pool; close with focused engine, tree, and context tests.
- **Maintainability:** Changes to the path beginning at `gin.go` are constrained by these audited guarantees: pooled contexts must be fully reset between requests, route precedence and parameter capture must stay deterministic, and middleware order, aborts, and response state must remain coherent.
- **Educational value:** Understand how Gin carries one HTTP request from ServeHTTP through route lookup, parameter capture, a middleware chain, and pooled-context cleanup. HTTP routing vocabulary is concise; the bounded trace teaches pooling, radix-tree route lookup, parameter capture, middleware-chain indexing, abort behavior, response state, and integration tests without requiring Gin's binding or rendering breadth.

**Inspection record:** commit `dcaa4296d111981ffb31ac3eba90bb63e1eb5ab9`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `gin.go`, `tree.go`, `context.go`, `gin_test.go`, `tree_test.go`, `context_test.go`, `LICENSE`. GitHub Linguist label: Go.

</details>

### [robfig/cron](https://github.com/robfig/cron)

**Language 2 / Behavior 4 / Design 2 / Constraints 4 → Level 3**

**Source:** Production software

A cron expression parser and in-process job scheduler for Go applications.

**Why study it:** Understand how robfig/cron owns scheduler state in one goroutine and coordinates timers, live updates, job launches, and shutdown. Scheduling vocabulary is brief; the path teaches a goroutine-owned event loop, timer reset rules, channels for mutation and shutdown, sorted deadlines, job wrappers, and explicit recovery policy.

**Short context:**

- A Cron scheduler calculates each entry's next time, sleeps until work is due, launches jobs, and accepts updates while running.

**Prerequisites:**

- Basic familiarity with Go functions, structs and interfaces, slices and maps, errors, goroutines and channels at a basic level, and table-driven tests.
- A Cron scheduler calculates each entry's next time, sleeps until work is due, launches jobs, and accepts updates while running.

**Concepts this path develops:**

- Goroutines, channels, and timers.
- Stopped, running, sleeping, waking, and stopping states.
- Timer reset and deadline ordering must avoid missed work.

**What you can learn:**

- Study these transferable Go mechanisms in `cron.go`: goroutines, channels, and timers, sort-based deadline ordering, and function and interface job wrappers.
- Trace these states and branches from `cron.go` through its selected supporting files: stopped, running, sleeping, waking, and stopping states, timer, add, remove, snapshot, and stop events, and due, delayed, empty, and panic branches.
- Identify these architectural responsibilities in the path beginning at `cron.go`: Cron scheduler owner, job wrapper chain, and direct lifecycle tests.
- Study these change constraints for the path beginning at `cron.go`: timer reset and deadline ordering must avoid missed work, live mutation must remain serialized with scheduling, and shutdown, overlapping jobs, and optional panic recovery require explicit policy.

**Learning path:**

- **Goal:** Understand how robfig/cron owns scheduler state in one goroutine and coordinates timers, live updates, job launches, and shutdown.
- **Start here:** [`cron.go`](https://github.com/robfig/cron/blob/bc59245fe10efaed9d51b56900192527ed733435/cron.go) — Begin with `cron.go` because it exposes how robfig/cron owns scheduler state in one goroutine and coordinates timers, live updates, job launches, and shutdown.
- **Then read:**
  - [`chain.go`](https://github.com/robfig/cron/blob/bc59245fe10efaed9d51b56900192527ed733435/chain.go)
  - [`cron_test.go`](https://github.com/robfig/cron/blob/bc59245fe10efaed9d51b56900192527ed733435/cron_test.go)
- **Trace:** Start at Cron.run, follow next-time calculation and sorting into timer selection, then trace wakeups alongside add, remove, snapshot, and stop channels before jobs launch in goroutines; compare chain wrappers and verify that panic recovery occurs only when WithChain(Recover(...)) is explicitly configured, contrary to the localized cron.go comment.

**Why this level:**

- **Language technique 2:** Familiar Go concurrency primitives recur without advanced language machinery.
- **Behavioral reasoning 4:** Several coupled scheduler states and event branches recur throughout the run loop.
- **Design span 2:** A few compact components cover one scheduler lifecycle.
- **Constraint burden 4:** Concurrency, timing, mutation, and failure constraints recur in normal scheduler operation.
- **Placement:** The four scores 2/4/2/4 sum to 12; their arithmetic mean is 3.00 and rounds half-up to Level 3. The published result is Level 3.

**License:** MIT ([evidence 1](https://github.com/robfig/cron/blob/bc59245fe10efaed9d51b56900192527ed733435/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository publishes a versioned Go module for applications that schedule recurring work inside a process.

**Language evidence:** The schedule parser, scheduler loop, job wrappers, and public interfaces are implemented in the root Go package.

**Coding relevance:**

Scheduling vocabulary is brief; the path teaches a goroutine-owned event loop, timer reset rules, channels for mutation and shutdown, sorted deadlines, job wrappers, and explicit recovery policy.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** cron.go centralizes the scheduler loop and lifecycle, chain.go makes wrappers including Recover explicit, and cron_test.go uses controlled schedules and synchronization to cover ordering, add and remove while running, stop, delayed jobs, and wrapper behavior.
- **Architecture:** The audited architecture of the path beginning at `cron.go` has these boundaries: Cron scheduler owner, job wrapper chain, and direct lifecycle tests.
- **Naming and idiom:** `cron.go` and its supporting files use these characteristic Go mechanisms: goroutines, channels, and timers, sort-based deadline ordering, and function and interface job wrappers.
- **Tests:** Direct tests in `cron_test.go` cover these states and branches in the selected path: stopped, running, sleeping, waking, and stopping states, timer, add, remove, snapshot, and stop events, and due, delayed, empty, and panic branches.
- **Documentation:** `cron.go` and its selected supporting material document the contracts needed to understand how robfig/cron owns scheduler state in one goroutine and coordinates timers, live updates, job launches, and shutdown.
- **Traceability:** Start at Cron.run, follow next-time calculation and sorting into timer selection, then trace wakeups alongside add, remove, snapshot, and stop channels before jobs launch in goroutines; compare chain wrappers and verify that panic recovery occurs only when WithChain(Recover(...)) is explicitly configured, contrary to the localized cron.go comment.
- **Maintainability:** Changes to the path beginning at `cron.go` are constrained by these audited guarantees: timer reset and deadline ordering must avoid missed work, live mutation must remain serialized with scheduling, and shutdown, overlapping jobs, and optional panic recovery require explicit policy.
- **Educational value:** Understand how robfig/cron owns scheduler state in one goroutine and coordinates timers, live updates, job launches, and shutdown. Scheduling vocabulary is brief; the path teaches a goroutine-owned event loop, timer reset rules, channels for mutation and shutdown, sorted deadlines, job wrappers, and explicit recovery policy.

**Inspection record:** commit `bc59245fe10efaed9d51b56900192527ed733435`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `cron.go`, `chain.go`, `cron_test.go`, `LICENSE`. GitHub Linguist label: Go.

</details>

## Level 4 — Advanced

### [caddyserver/caddy](https://github.com/caddyserver/caddy)

**Language 3 / Behavior 4 / Design 4 / Constraints 4 → Level 4**

**Source:** Production software

An extensible server platform and web server with automatic HTTPS, dynamic configuration, multiple HTTP protocols, and a module system.

**Why study it:** Understand how Caddy stages, validates, activates, and cleans up a modular configuration without losing the last working state on failure. Configuration and module vocabulary is bounded; the path teaches interface-driven plugin loading, dependency context, staged validation, transactional replacement, resource cleanup, admin-triggered reloads, and failure preservation.

**Short context:**

- Caddy loads a configuration by provisioning module values, validating an app graph, swapping active state, and cleaning up replaced resources.

**Prerequisites:**

- Working familiarity with Go functions, structs and interfaces, slices and maps, errors, goroutines and channels at a basic level, and table-driven tests, plus experience tracing behavior across several production files.
- Caddy loads a configuration by provisioning module values, validating an app graph, swapping active state, and cleaning up replaced resources.

**Concepts this path develops:**

- Interface-driven module registry.
- Decoded, provisioned, validated, started, active, replaced, and cleaned states.
- A failed candidate must not replace the working configuration.

**What you can learn:**

- Study these transferable Go mechanisms in `caddy.go`: interface-driven module registry, reflection and JSON-backed provisioning, and context-scoped lifecycle callbacks.
- Trace these states and branches from `caddy.go` through its selected supporting files: decoded, provisioned, validated, started, active, replaced, and cleaned states, success, validation, provisioning, start, and cleanup branches, and old and candidate configuration interaction.
- Identify these architectural responsibilities in the path beginning at `caddy.go`: global load and activation owner, module registry, provisioning Context, and admin reload boundary and integration tests.
- Study these change constraints for the path beginning at `caddy.go`: a failed candidate must not replace the working configuration, module dependencies must provision and clean up in valid scope, and activation, replacement, and resource cleanup must remain ordered.

**Learning path:**

- **Goal:** Understand how Caddy stages, validates, activates, and cleans up a modular configuration without losing the last working state on failure.
- **Start here:** [`caddy.go`](https://github.com/caddyserver/caddy/blob/502691f5182123ef30f463d7f132e7c2fe55e2bf/caddy.go) — Begin with `caddy.go` because it exposes how Caddy stages, validates, activates, and cleans up a modular configuration without losing the last working state on failure.
- **Then read:**
  - [`context.go`](https://github.com/caddyserver/caddy/blob/502691f5182123ef30f463d7f132e7c2fe55e2bf/context.go)
  - [`modules.go`](https://github.com/caddyserver/caddy/blob/502691f5182123ef30f463d7f132e7c2fe55e2bf/modules.go)
  - [`admin_test.go`](https://github.com/caddyserver/caddy/blob/502691f5182123ef30f463d7f132e7c2fe55e2bf/admin_test.go)
- **Trace:** Start at Load, follow configuration decoding and Context-based module provisioning into app validation and staged startup, then trace the synchronized active-config swap and cleanup of replaced modules; close with admin tests that exercise rejected and successful reloads and preservation of the prior configuration.

**Why this level:**

- **Language technique 3:** Intermediate Go extension and dynamic-loading techniques recur across configuration loading.
- **Behavioral reasoning 4:** Several coupled configuration and resource states recur throughout reload.
- **Design span 4:** Multiple cohesive components participate in one end-to-end reload lifecycle.
- **Constraint burden 4:** Failure atomicity, lifecycle, ordering, and compatibility guarantees recur in ordinary reload work.
- **Placement:** The four scores 3/4/4/4 sum to 15; their arithmetic mean is 3.75 and rounds half-up to Level 4. The published result is Level 4.

**License:** Apache-2.0 ([evidence 1](https://github.com/caddyserver/caddy/blob/502691f5182123ef30f463d7f132e7c2fe55e2bf/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository builds the released Caddy server used to host sites and services, and documents production installation, operation, and extension.

**Language evidence:** Configuration loading, module lifecycle, administration, HTTP servers, routing, automatic HTTPS, storage integration, and bundled modules are implemented in Go.

**Coding relevance:**

Configuration and module vocabulary is bounded; the path teaches interface-driven plugin loading, dependency context, staged validation, transactional replacement, resource cleanup, admin-triggered reloads, and failure preservation.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** caddy.go centralizes Load and active-config replacement, context.go handles module provisioning and cleanup scope, modules.go defines registration and lookup, and admin_test.go closes the actual reload path through admin requests, validation failures, state preservation, and successful replacement. The catalog's caddy_test.go does not close that reload trace.
- **Architecture:** The audited architecture of the path beginning at `caddy.go` has these boundaries: global load and activation owner, module registry, provisioning Context, and admin reload boundary and integration tests.
- **Naming and idiom:** `caddy.go` and its supporting files use these characteristic Go mechanisms: interface-driven module registry, reflection and JSON-backed provisioning, and context-scoped lifecycle callbacks.
- **Tests:** Direct tests in `admin_test.go` cover these states and branches in the selected path: decoded, provisioned, validated, started, active, replaced, and cleaned states, success, validation, provisioning, start, and cleanup branches, and old and candidate configuration interaction.
- **Documentation:** `caddy.go` and its selected supporting material document the contracts needed to understand how Caddy stages, validates, activates, and cleans up a modular configuration without losing the last working state on failure.
- **Traceability:** Start at Load, follow configuration decoding and Context-based module provisioning into app validation and staged startup, then trace the synchronized active-config swap and cleanup of replaced modules; close with admin tests that exercise rejected and successful reloads and preservation of the prior configuration.
- **Maintainability:** Changes to the path beginning at `caddy.go` are constrained by these audited guarantees: a failed candidate must not replace the working configuration, module dependencies must provision and clean up in valid scope, and activation, replacement, and resource cleanup must remain ordered.
- **Educational value:** Understand how Caddy stages, validates, activates, and cleans up a modular configuration without losing the last working state on failure. Configuration and module vocabulary is bounded; the path teaches interface-driven plugin loading, dependency context, staged validation, transactional replacement, resource cleanup, admin-triggered reloads, and failure preservation.

**Inspection record:** commit `502691f5182123ef30f463d7f132e7c2fe55e2bf`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `caddy.go`, `context.go`, `modules.go`, `admin_test.go`, `LICENSE`. GitHub Linguist label: Go.

</details>

### [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)

**Language 3 / Behavior 5 / Design 3 / Constraints 5 → Level 4**

**Source:** Production software

A distributed container orchestration platform with declarative APIs, scheduling, controllers, node agents, networking, storage, and extensibility.

**Why study it:** Understand how Kubernetes client-go coordinates concurrent workers with deduplicated keys, delayed retries, rate limiting, and safe shutdown. Workqueue vocabulary is brief and transferable; the replacement path teaches condition-variable coordination, dirty and processing sets, shutdown and drain semantics, delayed scheduling, rate-limiter composition, retry bookkeeping, fairness, and concurrency tests without Kubernetes API-server or scheduler expertise.

**Short context:**

- A workqueue serializes keys for concurrent workers, suppresses duplicate in-flight work, and can delay or rate-limit retries.

**Prerequisites:**

- Working familiarity with Go functions, structs and interfaces, slices and maps, errors, goroutines and channels at a basic level, and table-driven tests, plus experience tracing behavior across several production files.
- A workqueue serializes keys for concurrent workers, suppresses duplicate in-flight work, and can delay or rate-limit retries.

**Concepts this path develops:**

- Mutex and condition-variable coordination.
- Queued, dirty, processing, delayed, rate-limited, done, shutting-down, and drained states.
- One logical key must not execute concurrently or be lost when re-added.

**What you can learn:**

- Study these transferable Go mechanisms in `staging/src/k8s.io/client-go/util/workqueue/queue.go`: mutex and condition-variable coordination, goroutines, timers, and channels, and interface-composed rate limiters and typed sets.
- Trace these states and branches from `staging/src/k8s.io/client-go/util/workqueue/queue.go` through its selected supporting files: queued, dirty, processing, delayed, rate-limited, done, shutting-down, and drained states, duplicate add during processing and retry transitions, and timing, fairness, cancellation, and shutdown branches.
- Identify these architectural responsibilities in the path beginning at `staging/src/k8s.io/client-go/util/workqueue/queue.go`: core typed queue, delaying queue, rate-limiting facade and limiter policies, and corresponding focused tests.
- Study these change constraints for the path beginning at `staging/src/k8s.io/client-go/util/workqueue/queue.go`: one logical key must not execute concurrently or be lost when re-added, delays, backoff, fairness, and retries must interact predictably, and shutdown and draining must wake waiters and preserve completion invariants.

**Learning path:**

- **Goal:** Understand how Kubernetes client-go coordinates concurrent workers with deduplicated keys, delayed retries, rate limiting, and safe shutdown.
- **Start here:** [`staging/src/k8s.io/client-go/util/workqueue/queue.go`](https://github.com/kubernetes/kubernetes/blob/e72c2715ade37738aa5c029e8de5285cbe1c9441/staging/src/k8s.io/client-go/util/workqueue/queue.go) — Begin with `staging/src/k8s.io/client-go/util/workqueue/queue.go` because it exposes how Kubernetes client-go coordinates concurrent workers with deduplicated keys, delayed retries, rate limiting, and safe shutdown.
- **Then read:**
  - [`staging/src/k8s.io/client-go/util/workqueue/doc.go`](https://github.com/kubernetes/kubernetes/blob/e72c2715ade37738aa5c029e8de5285cbe1c9441/staging/src/k8s.io/client-go/util/workqueue/doc.go)
  - [`staging/src/k8s.io/client-go/util/workqueue/delaying_queue.go`](https://github.com/kubernetes/kubernetes/blob/e72c2715ade37738aa5c029e8de5285cbe1c9441/staging/src/k8s.io/client-go/util/workqueue/delaying_queue.go)
  - [`staging/src/k8s.io/client-go/util/workqueue/rate_limiting_queue.go`](https://github.com/kubernetes/kubernetes/blob/e72c2715ade37738aa5c029e8de5285cbe1c9441/staging/src/k8s.io/client-go/util/workqueue/rate_limiting_queue.go)
  - [`staging/src/k8s.io/client-go/util/workqueue/default_rate_limiters.go`](https://github.com/kubernetes/kubernetes/blob/e72c2715ade37738aa5c029e8de5285cbe1c9441/staging/src/k8s.io/client-go/util/workqueue/default_rate_limiters.go)
  - [`staging/src/k8s.io/client-go/util/workqueue/queue_test.go`](https://github.com/kubernetes/kubernetes/blob/e72c2715ade37738aa5c029e8de5285cbe1c9441/staging/src/k8s.io/client-go/util/workqueue/queue_test.go)
  - [`staging/src/k8s.io/client-go/util/workqueue/delaying_queue_test.go`](https://github.com/kubernetes/kubernetes/blob/e72c2715ade37738aa5c029e8de5285cbe1c9441/staging/src/k8s.io/client-go/util/workqueue/delaying_queue_test.go)
  - [`staging/src/k8s.io/client-go/util/workqueue/rate_limiting_queue_test.go`](https://github.com/kubernetes/kubernetes/blob/e72c2715ade37738aa5c029e8de5285cbe1c9441/staging/src/k8s.io/client-go/util/workqueue/rate_limiting_queue_test.go)
  - [`staging/src/k8s.io/client-go/util/workqueue/default_rate_limiters_test.go`](https://github.com/kubernetes/kubernetes/blob/e72c2715ade37738aa5c029e8de5285cbe1c9441/staging/src/k8s.io/client-go/util/workqueue/default_rate_limiters_test.go)
- **Trace:** Start with Add, Get, Done, dirty, processing, and the condition variable in the core queue, then follow shutdown and drain behavior into delayed scheduling and rate-limited requeue policy; close with the four focused suites for concurrency, deduplication, timing, retries, fairness, and shutdown.

**Why this level:**

- **Language technique 3:** Intermediate Go concurrency and composition techniques recur without multiple expert language mechanisms.
- **Behavioral reasoning 5:** Many tightly coupled concurrent states and failure-sensitive transitions recur in ordinary use.
- **Design span 3:** A few cohesive sibling components form one bounded workqueue subsystem.
- **Constraint burden 5:** Expert concurrency, deduplication, timing, fairness, and shutdown guarantees recur throughout the path.
- **Placement:** The four scores 3/5/3/5 sum to 16; their arithmetic mean is 4.00 and rounds half-up to Level 4. The published result is Level 4.

**License:** Apache-2.0 ([evidence 1](https://github.com/kubernetes/kubernetes/blob/e72c2715ade37738aa5c029e8de5285cbe1c9441/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository builds the upstream Kubernetes control plane and node components released for operating containerized workloads across clusters.

**Language evidence:** The API server, controllers, scheduler, kubelet, proxy, storage and API machinery, command binaries, and core control-plane behavior are implemented primarily in Go.

**Coding relevance:**

Workqueue vocabulary is brief and transferable; the replacement path teaches condition-variable coordination, dirty and processing sets, shutdown and drain semantics, delayed scheduling, rate-limiter composition, retry bookkeeping, fairness, and concurrency tests without Kubernetes API-server or scheduler expertise.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** queue.go documents and implements the core dirty, processing, condition, shutdown, and drain invariants; sibling delaying and rate-limiting layers extend the lifecycle; default limiters make retry policy explicit; and corresponding focused tests cover concurrency, deduplication, timing, shutdown, draining, fairness, and limiter behavior.
- **Architecture:** The audited architecture of the path beginning at `staging/src/k8s.io/client-go/util/workqueue/queue.go` has these boundaries: core typed queue, delaying queue, rate-limiting facade and limiter policies, and corresponding focused tests.
- **Naming and idiom:** `staging/src/k8s.io/client-go/util/workqueue/queue.go` and its supporting files use these characteristic Go mechanisms: mutex and condition-variable coordination, goroutines, timers, and channels, and interface-composed rate limiters and typed sets.
- **Tests:** Direct tests in `staging/src/k8s.io/client-go/util/workqueue/queue_test.go`, `staging/src/k8s.io/client-go/util/workqueue/delaying_queue_test.go`, `staging/src/k8s.io/client-go/util/workqueue/rate_limiting_queue_test.go`, and `staging/src/k8s.io/client-go/util/workqueue/default_rate_limiters_test.go` cover these states and branches in the selected path: queued, dirty, processing, delayed, rate-limited, done, shutting-down, and drained states, duplicate add during processing and retry transitions, and timing, fairness, cancellation, and shutdown branches.
- **Documentation:** `staging/src/k8s.io/client-go/util/workqueue/queue.go` and its selected supporting material document the contracts needed to understand how Kubernetes client-go coordinates concurrent workers with deduplicated keys, delayed retries, rate limiting, and safe shutdown.
- **Traceability:** Start with Add, Get, Done, dirty, processing, and the condition variable in the core queue, then follow shutdown and drain behavior into delayed scheduling and rate-limited requeue policy; close with the four focused suites for concurrency, deduplication, timing, retries, fairness, and shutdown.
- **Maintainability:** Changes to the path beginning at `staging/src/k8s.io/client-go/util/workqueue/queue.go` are constrained by these audited guarantees: one logical key must not execute concurrently or be lost when re-added, delays, backoff, fairness, and retries must interact predictably, and shutdown and draining must wake waiters and preserve completion invariants.
- **Educational value:** Understand how Kubernetes client-go coordinates concurrent workers with deduplicated keys, delayed retries, rate limiting, and safe shutdown. Workqueue vocabulary is brief and transferable; the replacement path teaches condition-variable coordination, dirty and processing sets, shutdown and drain semantics, delayed scheduling, rate-limiter composition, retry bookkeeping, fairness, and concurrency tests without Kubernetes API-server or scheduler expertise.

**Inspection record:** commit `e72c2715ade37738aa5c029e8de5285cbe1c9441`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `staging/src/k8s.io/client-go/util/workqueue/queue.go`, `staging/src/k8s.io/client-go/util/workqueue/doc.go`, `staging/src/k8s.io/client-go/util/workqueue/delaying_queue.go`, `staging/src/k8s.io/client-go/util/workqueue/rate_limiting_queue.go`, `staging/src/k8s.io/client-go/util/workqueue/default_rate_limiters.go`, `staging/src/k8s.io/client-go/util/workqueue/queue_test.go`, `staging/src/k8s.io/client-go/util/workqueue/delaying_queue_test.go`, `staging/src/k8s.io/client-go/util/workqueue/rate_limiting_queue_test.go`, `staging/src/k8s.io/client-go/util/workqueue/default_rate_limiters_test.go`, `LICENSE`. GitHub Linguist label: Go.

</details>

## Level 5 — Expert

### [golang/go](https://github.com/golang/go)

**Language 5 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

**Source:** Production software

The Go programming language implementation, including its compiler, runtime, standard library, build tools, assembler, linker, and platform ports.

**Why study it:** Understand how the Go runtime implements channel send, receive, close, and select while coordinating memory, goroutine parking, wakeup, and scheduler invariants. Runtime vocabulary is introduced once; the bounded path teaches unsafe memory layout, scheduler integration, sudog wait queues, lock ordering, atomic state, blocking and wakeup, select races, garbage-collector barriers, and performance-sensitive correctness.

**Short context:**

- The Go runtime implements channel send, receive, close, and select by coordinating goroutines, queues, buffers, locks, and the scheduler.

**Prerequisites:**

- Strong working familiarity with Go functions, structs and interfaces, slices and maps, errors, goroutines and channels at a basic level, and table-driven tests, plus experience tracing state, resources, or asynchronous control flow across many production files.
- The Go runtime implements channel send, receive, close, and select by coordinating goroutines, queues, buffers, locks, and the scheduler.

**Concepts this path develops:**

- Unsafe pointer arithmetic and typed memory operations.
- Open, buffered, empty, full, waiting, closed, parked, and readied states.
- Send, receive, close, and select semantics must be race-correct.

**What you can learn:**

- Study these transferable Go mechanisms in `src/runtime/chan.go`: unsafe pointer arithmetic and typed memory operations, runtime-internal atomics, locks, barriers, and scheduler primitives, and compiler-recognized and nosplit or system-stack mechanisms.
- Trace these states and branches from `src/runtime/chan.go` through its selected supporting files: open, buffered, empty, full, waiting, closed, parked, and readied states, direct handoff, buffer transfer, block, wakeup, close, panic, and select branches, and sender, receiver, scheduler, and garbage-collector interaction.
- Identify these architectural responsibilities in the path beginning at `src/runtime/chan.go`: channel core and wait queues, select implementation, shared runtime scheduler structures, and semantic tests and runtime guide.
- Study these change constraints for the path beginning at `src/runtime/chan.go`: send, receive, close, and select semantics must be race-correct, lock order, parking, wakeup, stack, and GC barriers must remain safe, and fast paths must preserve fairness, memory-model, panic, and performance guarantees.

**Learning path:**

- **Goal:** Understand how the Go runtime implements channel send, receive, close, and select while coordinating memory, goroutine parking, wakeup, and scheduler invariants.
- **Start here:** [`src/runtime/chan.go`](https://github.com/golang/go/blob/da7c67f59526a02ef22f80fe91fd2960a6547e59/src/runtime/chan.go) — Begin with `src/runtime/chan.go` because it exposes how the Go runtime implements channel send, receive, close, and select while coordinating memory, goroutine parking, wakeup, and scheduler invariants.
- **Then read:**
  - [`src/runtime/select.go`](https://github.com/golang/go/blob/da7c67f59526a02ef22f80fe91fd2960a6547e59/src/runtime/select.go)
  - [`src/runtime/runtime2.go`](https://github.com/golang/go/blob/da7c67f59526a02ef22f80fe91fd2960a6547e59/src/runtime/runtime2.go)
  - [`src/runtime/chan_test.go`](https://github.com/golang/go/blob/da7c67f59526a02ef22f80fe91fd2960a6547e59/src/runtime/chan_test.go)
  - [`src/runtime/HACKING.md`](https://github.com/golang/go/blob/da7c67f59526a02ef22f80fe91fd2960a6547e59/src/runtime/HACKING.md)
- **Trace:** Start with hchan layout and channel creation, follow fast and blocking send and receive through buffers, sudog queues, gopark, and readying, then trace close wakeups and select's lock and race protocol; close with runtime structures, channel tests, and the runtime hacking guide.

**Why this level:**

- **Language technique 5:** Multiple expert Go runtime and low-level language mechanisms recur throughout channel operations.
- **Behavioral reasoning 5:** Many tightly coupled concurrent states and race-sensitive transitions recur throughout normal channel behavior.
- **Design span 4:** Several major runtime components participate, while the trace stays bounded to channels rather than mixing compiler and unrelated runtime systems.
- **Constraint burden 5:** Expert concurrency, memory, scheduler, GC, semantic, and performance constraints recur across every channel operation.
- **Placement:** The four scores 5/5/4/5 sum to 19; their arithmetic mean is 4.75 and rounds half-up to Level 5. The published result is Level 5.

**License:** BSD-3-Clause ([evidence 1](https://github.com/golang/go/blob/da7c67f59526a02ef22f80fe91fd2960a6547e59/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository is the upstream source used to build official Go toolchains and standard-library releases across supported operating systems and architectures.

**Language evidence:** The compiler, runtime, garbage collector, scheduler, standard library, assembler, linker, debugger support, and developer tools are implemented predominantly in Go with first-party assembly and small C boundaries.

**Coding relevance:**

Runtime vocabulary is introduced once; the bounded path teaches unsafe memory layout, scheduler integration, sudog wait queues, lock ordering, atomic state, blocking and wakeup, select races, garbage-collector barriers, and performance-sensitive correctness.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** chan.go documents and implements buffered and unbuffered channel operations and close, select.go supplies multi-channel coordination, runtime2.go defines shared scheduler and wait structures, chan_test.go exercises semantics and regressions, and HACKING.md explains runtime invariants and development conventions.
- **Architecture:** The audited architecture of the path beginning at `src/runtime/chan.go` has these boundaries: channel core and wait queues, select implementation, shared runtime scheduler structures, and semantic tests and runtime guide.
- **Naming and idiom:** `src/runtime/chan.go` and its supporting files use these characteristic Go mechanisms: unsafe pointer arithmetic and typed memory operations, runtime-internal atomics, locks, barriers, and scheduler primitives, and compiler-recognized and nosplit or system-stack mechanisms.
- **Tests:** Direct tests in `src/runtime/chan_test.go` cover these states and branches in the selected path: open, buffered, empty, full, waiting, closed, parked, and readied states, direct handoff, buffer transfer, block, wakeup, close, panic, and select branches, and sender, receiver, scheduler, and garbage-collector interaction.
- **Documentation:** `src/runtime/chan.go` and its selected supporting material document the contracts needed to understand how the Go runtime implements channel send, receive, close, and select while coordinating memory, goroutine parking, wakeup, and scheduler invariants.
- **Traceability:** Start with hchan layout and channel creation, follow fast and blocking send and receive through buffers, sudog queues, gopark, and readying, then trace close wakeups and select's lock and race protocol; close with runtime structures, channel tests, and the runtime hacking guide.
- **Maintainability:** Changes to the path beginning at `src/runtime/chan.go` are constrained by these audited guarantees: send, receive, close, and select semantics must be race-correct, lock order, parking, wakeup, stack, and GC barriers must remain safe, and fast paths must preserve fairness, memory-model, panic, and performance guarantees.
- **Educational value:** Understand how the Go runtime implements channel send, receive, close, and select while coordinating memory, goroutine parking, wakeup, and scheduler invariants. Runtime vocabulary is introduced once; the bounded path teaches unsafe memory layout, scheduler integration, sudog wait queues, lock ordering, atomic state, blocking and wakeup, select races, garbage-collector barriers, and performance-sensitive correctness.

**Inspection record:** commit `da7c67f59526a02ef22f80fe91fd2960a6547e59`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/runtime/chan.go`, `src/runtime/select.go`, `src/runtime/runtime2.go`, `src/runtime/chan_test.go`, `src/runtime/HACKING.md`, `LICENSE`. GitHub Linguist label: Go.

</details>

### [grpc/grpc-go](https://github.com/grpc/grpc-go)

**Language 4 / Behavior 5 / Design 5 / Constraints 5 → Level 5**

**Source:** Production software

The Go implementation of gRPC, providing clients, servers, streaming RPCs, transports, resolution, load balancing, retries, observability, and generated-code support.

**Why study it:** Understand how a gRPC-Go ClientConn turns resolver updates into balanced subchannels, waits or fails RPC picks according to connectivity, reconnects with backoff, and closes every concurrent component in dependency order. Endpoint resolution and client-side load balancing need only a short primer; the path teaches transferable goroutine ownership, channel wakeups, serialized callbacks, connection state machines, backoff, dynamic policy, concurrent selection, shutdown ordering, observability, and race-focused tests.

**Short context:**

- A resolver produces endpoint addresses, a load balancer owns subchannels and publishes a picker, and each RPC either chooses a ready transport, waits for a usable one, or fails according to its context and wait-for-ready policy.

**Prerequisites:**

- Be fluent with Go interfaces, goroutines, channels, contexts, mutexes, atomics, error wrapping, closures, and cancellation-aware tests.
- A resolver produces endpoint addresses, a load balancer owns subchannels and publishes a picker, and each RPC either chooses a ready transport, waits for a usable one, or fails according to its context and wait-for-ready policy.

**Concepts this path develops:**

- Interacting interfaces and callback adapters across resolver, balancer, picker, and transport layers.
- Idle, connecting, ready, transient-failure, and shutdown transitions.
- Race-free state visibility, wakeups, and callback serialization.

**What you can learn:**

- Study these transferable Go mechanisms in `clientconn.go`: interface-driven resolver, balancer, picker, and transport boundaries; goroutines, channels, contexts, mutexes, atomics, and wait groups; and callback serializers with explicit ownership.
- Trace these states and branches through the selected implementation: idle, connecting, ready, transient-failure, and shutdown states; resolver and service-config updates; address attempts and backoff; picker blocking, fail-fast, and wait-for-ready behavior; and concurrent close races.
- Identify these architectural responsibilities: ClientConn orchestration, resolver and balancer wrappers, per-address connection and transport lifecycle, picker admission, connectivity publication, and direct unit and integration state-transition tests.
- Study these change constraints: state notifications and picks must not be missed, resolver and balancer callbacks must remain serialized, RPC and connection paths must stay race-safe, backoff and cancellation must bound work, and close must quiesce serializers and subchannels without deadlock or use-after-close.

**Learning path:**

- **Goal:** Understand how a gRPC-Go ClientConn turns resolver updates into balanced subchannels, waits or fails RPC picks according to connectivity, reconnects with backoff, and closes every concurrent component in dependency order.
- **Start here:** [`clientconn.go`](https://github.com/grpc/grpc-go/blob/6d697e4b65eb0dcfaf326b5b1fcdc66913872442/clientconn.go) — Begin with ClientConn and addrConn because their documented ownership, update, connection, backoff, state, and close methods connect every selected boundary.
- **Then read:**
  - [`resolver_wrapper.go`](https://github.com/grpc/grpc-go/blob/6d697e4b65eb0dcfaf326b5b1fcdc66913872442/resolver_wrapper.go)
  - [`balancer_wrapper.go`](https://github.com/grpc/grpc-go/blob/6d697e4b65eb0dcfaf326b5b1fcdc66913872442/balancer_wrapper.go)
  - [`picker_wrapper.go`](https://github.com/grpc/grpc-go/blob/6d697e4b65eb0dcfaf326b5b1fcdc66913872442/picker_wrapper.go)
  - [`connectivity/connectivity.go`](https://github.com/grpc/grpc-go/blob/6d697e4b65eb0dcfaf326b5b1fcdc66913872442/connectivity/connectivity.go)
  - [`test/clientconn_state_transition_test.go`](https://github.com/grpc/grpc-go/blob/6d697e4b65eb0dcfaf326b5b1fcdc66913872442/test/clientconn_state_transition_test.go)
  - [`balancer_wrapper_test.go`](https://github.com/grpc/grpc-go/blob/6d697e4b65eb0dcfaf326b5b1fcdc66913872442/balancer_wrapper_test.go)
  - [`picker_wrapper_test.go`](https://github.com/grpc/grpc-go/blob/6d697e4b65eb0dcfaf326b5b1fcdc66913872442/picker_wrapper_test.go)
  - [`Documentation/anti-patterns.md`](https://github.com/grpc/grpc-go/blob/6d697e4b65eb0dcfaf326b5b1fcdc66913872442/Documentation/anti-patterns.md)
- **Trace:** Start at ClientConn creation and resolverWrapper updates, follow service configuration into the balancer serializer, NewSubConn into addrConn connection attempts and backoff, connectivity publication and picker replacement into blocking or fail-fast RPC selection, then follow transport loss and address updates through reconnection; finish at ClientConn.Close's picker-before-balancer ordering, serializer drains, parallel subchannel teardown, and state, picker, and close-race tests.

**Why this level:**

- **Language technique 4:** Advanced Go concurrency and interface machinery recurs throughout the path, but the language deliberately avoids type-level or metaprogramming complexity sufficient for expert score 5.
- **Behavioral reasoning 5:** Several concurrent state machines and failure lifecycles interact pervasively, making expert nonlocal reasoning unavoidable.
- **Design span 5:** The path coordinates several major runtime subsystems and pervasive extension policies even while RPC framing and server execution stay out of scope.
- **Constraint burden 5:** Concurrency, lifecycle, reliability, extensibility, observability, and compatibility guarantees interact so local changes can strand RPCs or leak live work.
- **Placement:** The four scores 4/5/5/5 sum to 19; their arithmetic mean is 4.75 and rounds half-up to Level 5, with three dimensions scored 5. The published result is Level 5.

**License:** Apache-2.0 ([evidence 1](https://github.com/grpc/grpc-go/blob/6d697e4b65eb0dcfaf326b5b1fcdc66913872442/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The module publishes google.golang.org/grpc, the production Go runtime used to build interoperable RPC clients and servers across the gRPC ecosystem.

**Language evidence:** The selected ClientConn, resolver and balancer wrappers, address-connection state machine, picker coordination, shutdown behavior, and direct tests are handwritten first-party Go in the root, resolver/, connectivity/, and test/.

**Coding relevance:**

Endpoint resolution and client-side load balancing need only a short primer; the path teaches transferable goroutine ownership, channel wakeups, serialized callbacks, connection state machines, backoff, dynamic policy, concurrent selection, shutdown ordering, observability, and race-focused tests.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** ClientConn and addrConn document field synchronization and lifecycle assumptions; resolver, balancer, and picker wrappers isolate callbacks and publication; direct tests exercise transition sequences, address failure, blocking picks, contexts, policy updates, and close races.
- **Architecture:** The selected files expose recognizable ClientConn orchestration, resolver, configuration, balancer, subchannel, picker, transport, connectivity, and observability boundaries with explicit ownership and serializer rules.
- **Naming and idiom:** ClientConn, addrConn, updateResolverStateAndUnlock, resetTransportAndUnlock, connectivityStateManager, pickerWrapper, serializer, and firstResolveEvent make state and ownership visible while demonstrating advanced idiomatic Go concurrency.
- **Tests:** State-transition integration tests cover successful readiness, preface failure, timeouts, disconnection, multiple failed addresses, and reconnects; picker tests cover blocking, deadlines, transient failure, fail-fast, subchannel readiness, and concurrent wakeups; balancer tests target creation-versus-close races.
- **Documentation:** README.md, API comments, anti-pattern guidance, and official gRPC Go documentation explain the client abstraction, connectivity, supported use, and relevant lifecycle context.
- **Traceability:** A resolver update can be followed through serialized balancer state, subchannel creation, address connection and transport state, picker publication, RPC selection, reconnection, and ordered shutdown into direct assertions.
- **Maintainability:** Synchronization ownership is documented near fields, callback streams are serialized, close order is explained in source, state changes are centralized, and race-shaped tests protect the most dangerous interleavings.
- **Educational value:** The bounded client-connection path is a strong production study of concurrent control-plane and data-plane coordination in Go without requiring the learner to understand protobuf encoding or HTTP/2 frame implementation.

**Inspection record:** commit `6d697e4b65eb0dcfaf326b5b1fcdc66913872442`, inspected 2026-08-29. Review passes: Codex primary pass; Codex cold verification pass. Files inspected: `README.md`, `clientconn.go`, `resolver_wrapper.go`, `balancer_wrapper.go`, `picker_wrapper.go`, `connectivity/connectivity.go`, `test/clientconn_state_transition_test.go`, `balancer_wrapper_test.go`, `picker_wrapper_test.go`, `Documentation/anti-patterns.md`, `LICENSE`. GitHub Linguist label: Go.

</details>

_Generated from `catalog/go.json`; do not edit by hand._

# Rust

6 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

[← All languages](../README.md)

## Level 1 — First real code

No qualified learning path has been published at this level. An empty Level 1 means Exempla has not yet found a path gentle enough to publish here; learners are not being told to jump to Level 2.

## Level 2 — Guided real-world code

No qualified learning path has been published at this level. Standards are not lowered to fill a slot.

## Level 3 — Intermediate

### [dtolnay/semver](https://github.com/dtolnay/semver)

**Language 3 / Behavior 3 / Design 3 / Constraints 4 → Level 3**

A parser and evaluator for Cargo-flavored Semantic Versioning versions and requirements, including caret, tilde, wildcard, range, and prerelease rules.

**Why study it:** A compact domain library turns a familiar specification into explicit data types, a byte-level parser, precise position-aware errors, comparator normalization, matching semantics, and stable formatting.

**Short context:**

- Semantic versions have major, minor, patch, prerelease, and build components, while Cargo-style requirements add exact, range, caret, tilde, wildcard, conjunction, and disjunction operators.

**Prerequisites:**

- Rust structs, enums, traits and lifetimes, slices and byte parsing, semantic versioning concepts, ordering, error types, and test-driven specification work.

**Concepts this path develops:**

- Borrowed string-slice parsing with lifetimes and position-aware errors.
- Grammar state for missing and optional version components.
- Cargo-compatible caret, tilde, wildcard, range, and prerelease meanings must remain exact.

**What you can learn:**

- Domain modeling, byte parsers, semantic-version grammar, comparator operators, caret and tilde ranges, wildcards, prerelease matching, error locations, formatting, property tests, and fuzzing.

**Learning path:**

- **Goal:** Understand how semver parses Cargo-style version and requirement strings into typed comparators and evaluates their exact, range, wildcard, and prerelease meaning.
- **Start here:** [`src/parse.rs`](https://github.com/dtolnay/semver/blob/280ebcb6edac3aa4cdc545dbff8a26c5ac4861fe/src/parse.rs) — The hand-written parser shows how versions and requirements become typed values while preserving exact failure positions and grammar expectations.
- **Then read:**
  - [`src/lib.rs`](https://github.com/dtolnay/semver/blob/280ebcb6edac3aa4cdc545dbff8a26c5ac4861fe/src/lib.rs)
  - [`src/eval.rs`](https://github.com/dtolnay/semver/blob/280ebcb6edac3aa4cdc545dbff8a26c5ac4861fe/src/eval.rs)
  - [`tests/test_version.rs`](https://github.com/dtolnay/semver/blob/280ebcb6edac3aa4cdc545dbff8a26c5ac4861fe/tests/test_version.rs)
  - [`tests/test_version_req.rs`](https://github.com/dtolnay/semver/blob/280ebcb6edac3aa4cdc545dbff8a26c5ac4861fe/tests/test_version_req.rs)
  - [`README.md`](https://github.com/dtolnay/semver/blob/280ebcb6edac3aa4cdc545dbff8a26c5ac4861fe/README.md)
  - [`Cargo.toml`](https://github.com/dtolnay/semver/blob/280ebcb6edac3aa4cdc545dbff8a26c5ac4861fe/Cargo.toml)
  - [`LICENSE-APACHE`](https://github.com/dtolnay/semver/blob/280ebcb6edac3aa4cdc545dbff8a26c5ac4861fe/LICENSE-APACHE)
- **Trace:** Start with FromStr for Version, VersionReq, and Comparator, follow cursor slices through numeric and metadata identifiers, operator and wildcard parsing, comparator normalization, disjunction handling, and position-aware errors; then trace the resulting comparators through exact, inequality, tilde, caret, wildcard, and prerelease predicates and close each rule family in the direct version and requirement suites.

**Why this level:**

- **Language technique 3:** Substantial Rust type and borrowing techniques shape the implementation, but the path avoids unsafe code, concurrency, and expert metaprogramming.
- **Behavioral reasoning 3:** Several interdependent syntax and matching branches require deliberate reasoning, though all behavior is deterministic and in-process.
- **Design span 3:** Several clear units contribute to the complete text-to-semantics path without crossing external systems.
- **Constraint burden 4:** Multiple strict specification and compatibility guarantees recur; small local parser or predicate changes can silently alter dependency selection.
- **Placement:** The four scores 3/3/3/4 sum to 13; their arithmetic mean is 3.25 and rounds half-up to Level 3. The published result is Level 3.

**License:** MIT OR Apache-2.0 ([evidence 1](https://github.com/dtolnay/semver/blob/280ebcb6edac3aa4cdc545dbff8a26c5ac4861fe/LICENSE-MIT), [evidence 2](https://github.com/dtolnay/semver/blob/280ebcb6edac3aa4cdc545dbff8a26c5ac4861fe/LICENSE-APACHE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The maintained crate is published for Rust tools that interpret Cargo-compatible versions and dependency requirements.

**Language evidence:** Version and requirement models, parsing, comparator evaluation, formatting, error reporting, fuzz targets, and tests are Rust.

**Coding relevance:**

The concise version-requirement grammar is documented in the repository, and the path is programming-led: typed domain modeling, allocation-conscious parsing, position-aware failures, operator-specific predicates, normalization, formatting, and executable specification tests explain its difficulty.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Parsing state, numeric overflow, identifiers, separators, operators, wildcard normalization, evaluation predicates, and error spans are explicit.
- **Architecture:** Public value types delegate parsing to a cursor-based module and requirement matching to a separate evaluator, with formatting alongside the models.
- **Naming and idiom:** Version, VersionReq, Comparator, Op, Prerelease, BuildMetadata, parse_optional_meta, eval, and matches mirror the specification.
- **Tests:** Focused suites cover accepted and rejected versions and requirements, every operator family, prerelease rules, whitespace, overflow, display round trips, hashing, ordering, size, properties, and fuzzing.
- **Documentation:** The README and API documentation explain Cargo's flavor, parsing, construction, comparison, requirements, prerelease handling, and feature support.
- **Traceability:** A requirement string can be followed from cursor operations into comparators, through operator-specific evaluation, to a precise match or parse error assertion.
- **Maintainability:** Grammar and matching logic are separated, public types are small, errors retain positions, and dense boundary tests encode the domain contract.
- **Educational value:** It is a compact example of translating a prose specification into auditable types, parsing rules, and executable semantics.

**Inspection record:** commit `280ebcb6edac3aa4cdc545dbff8a26c5ac4861fe`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/parse.rs`, `src/lib.rs`, `src/eval.rs`, `tests/test_version.rs`, `tests/test_version_req.rs`, `README.md`, `Cargo.toml`, `LICENSE-APACHE`, `LICENSE-MIT`. GitHub Linguist label: Rust.

</details>

### [withoutboats/heck](https://github.com/withoutboats/heck)

**Language 3 / Behavior 2 / Design 2 / Constraints 3 → Level 3**

A no_std string case-conversion library supporting snake, kebab, title, train, shouty, lower camel, and upper camel forms.

**Why study it:** A small common transform turns subtle acronym, digit, lowercase, uppercase, Unicode, and separator rules into reusable conversion traits and zero-allocation display wrappers.

**Short context:**

- Identifier case styles split text into words and then format those words as snake, kebab, title, train, shouty, or camel case.
- Unicode uppercase and lowercase conversion can expand or contextually change a character, so the implementation iterates characters rather than bytes.

**Prerequisites:**

- Basic Rust modules and traits, iterators and closures, Unicode characters, string formatting, generics, and unit tests.

**Concepts this path develops:**

- Generic FnMut formatting callbacks over borrowed string slices.
- Local tri-state word-boundary scan.
- All case styles must share identical word-boundary semantics.

**What you can learn:**

- Unicode-aware character iteration, word-boundary state, acronym splitting, case conversion traits, Display wrappers, no_std design, module reuse, and table-driven tests.

**Learning path:**

- **Goal:** Understand how heck scans Unicode text into words once and reuses that boundary engine to implement several allocation and display-oriented case-conversion APIs.
- **Start here:** [`src/lib.rs`](https://github.com/withoutboats/heck/blob/252c1906cefefb8d13ecad7fce7b8f27ce6437e0/src/lib.rs) — The shared transform function defines the word-boundary algorithm that every public case module reuses.
- **Then read:**
  - [`src/snake.rs`](https://github.com/withoutboats/heck/blob/252c1906cefefb8d13ecad7fce7b8f27ce6437e0/src/snake.rs)
  - [`src/lower_camel.rs`](https://github.com/withoutboats/heck/blob/252c1906cefefb8d13ecad7fce7b8f27ce6437e0/src/lower_camel.rs)
  - [`src/upper_camel.rs`](https://github.com/withoutboats/heck/blob/252c1906cefefb8d13ecad7fce7b8f27ce6437e0/src/upper_camel.rs)
  - [`README.md`](https://github.com/withoutboats/heck/blob/252c1906cefefb8d13ecad7fce7b8f27ce6437e0/README.md)
  - [`Cargo.toml`](https://github.com/withoutboats/heck/blob/252c1906cefefb8d13ecad7fce7b8f27ce6437e0/Cargo.toml)
  - [`LICENSE-APACHE`](https://github.com/withoutboats/heck/blob/252c1906cefefb8d13ecad7fce7b8f27ce6437e0/LICENSE-APACHE)
- **Trace:** Start with the documented word-boundary rules and transform's WordMode state, follow delimiter splitting and lowercase, uppercase, acronym, digit, and trailing-word transitions into the formatting callbacks, then compare snake, lower-camel, and upper-camel trait and Display adapters and close the edge cases in their inline test matrices.

**Why this level:**

- **Language technique 3:** Substantial Rust abstractions shape reuse and public ergonomics, but the path avoids unsafe code, concurrency, macros, and advanced type machinery.
- **Behavioral reasoning 2:** Several edge-sensitive states must be traced, but they remain local to one deterministic pass without asynchronous or nonlocal behavior.
- **Design span 2:** A few clear units cooperate while the complete behavior stays within one compact library boundary.
- **Constraint burden 3:** Multiple user-visible text and portability guarantees interact, although failure remains confined to deterministic string conversion.
- **Placement:** The four scores 3/2/2/3 sum to 10; their arithmetic mean is 2.50 and rounds half-up to Level 3. The published result is Level 3.

**License:** MIT OR Apache-2.0 ([evidence 1](https://github.com/withoutboats/heck/blob/252c1906cefefb8d13ecad7fce7b8f27ce6437e0/LICENSE-MIT), [evidence 2](https://github.com/withoutboats/heck/blob/252c1906cefefb8d13ecad7fce7b8f27ce6437e0/LICENSE-APACHE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The maintained crate is published for use by Rust libraries, procedural macros, and applications that need predictable identifier and display-name conversion.

**Language evidence:** The shared word-boundary transform, eight case-style modules, display adapters, Unicode handling, and inline test matrices are Rust.

**Coding relevance:**

The short naming-convention and Unicode primer is subordinate to transferable lessons in stateful text scanning, boundary detection, callback-based reuse, trait and Display API design, no_std constraints, and table-driven edge-case testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Word boundaries are expressed as readable character predicates and each style supplies only its first-word, next-word, and boundary formatting choices.
- **Architecture:** One shared transform owns tokenization; small modules expose traits and display types for each naming convention.
- **Naming and idiom:** ToSnakeCase, AsSnakeCase, transform, word_boundary, first_word, boundary, and upper_camel state both operation and representation.
- **Tests:** Each style carries compact matrices for spaces, punctuation, digits, acronyms, mixed case, repeated separators, Greek sigma, and Unicode case expansion.
- **Documentation:** The README and module documentation enumerate the supported conventions and show direct string and display-wrapper use.
- **Traceability:** An input can be followed character by character through boundary detection into a case module and an exact expected output.
- **Maintainability:** The common algorithm prevents eight implementations from drifting, while local tests document each public convention.
- **Educational value:** It demonstrates how a tiny library can centralize subtle language rules without obscuring them behind dependencies.

**Inspection record:** commit `252c1906cefefb8d13ecad7fce7b8f27ce6437e0`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/lib.rs`, `src/snake.rs`, `src/lower_camel.rs`, `src/upper_camel.rs`, `README.md`, `Cargo.toml`, `LICENSE-APACHE`, `LICENSE-MIT`. GitHub Linguist label: Rust.

</details>

## Level 4 — Advanced

### [dtolnay/anyhow](https://github.com/dtolnay/anyhow)

**Language 5 / Behavior 4 / Design 3 / Constraints 5 → Level 4**

A flexible application-error type that carries context, error chains, downcasting, backtraces, and ergonomic propagation across arbitrary error sources.

**Why study it:** anyhow's context path connects an idiomatic Result extension to the type-erased owned representation that preserves sources, backtraces, formatting, and downcasting.

**Short context:**

- Application error context adds a higher-level explanation while preserving the lower-level source error for reporting and inspection.

**Prerequisites:**

- Readers should know advanced Rust generics and traits, Result and Option, error source chains, raw pointers, allocation and drop, type erasure, vtables, and unsafe-code invariants.

**Concepts this path develops:**

- Unsafe custom pointer ownership and lifetime wrappers.
- Context wraps while preserving both context and source type identities.
- Raw-pointer layout, alignment, aliasing, ownership, Send and Sync, and drop must remain sound.

**What you can learn:**

- Trace eager or lazy context through generic error construction, pointer ownership, custom vtables, source chains, backtraces, downcasts, mutation, and destruction.

**Learning path:**

- **Goal:** Understand how anyhow adds lazy application context to errors while preserving source traversal and concrete-type downcasting through a type-erased owned representation.
- **Start here:** [`src/context.rs`](https://github.com/dtolnay/anyhow/blob/c63b279f3f4af2b02ca6267d9eb47d6d10497f69/src/context.rs) — The reviewed trace begins in context.rs because its Result and Option extension trait is the learner-facing operation that enters the deeper error representation.
- **Then read:**
  - [`src/error.rs`](https://github.com/dtolnay/anyhow/blob/c63b279f3f4af2b02ca6267d9eb47d6d10497f69/src/error.rs)
  - [`src/ptr.rs`](https://github.com/dtolnay/anyhow/blob/c63b279f3f4af2b02ca6267d9eb47d6d10497f69/src/ptr.rs)
  - [`src/chain.rs`](https://github.com/dtolnay/anyhow/blob/c63b279f3f4af2b02ca6267d9eb47d6d10497f69/src/chain.rs)
  - [`tests/test_context.rs`](https://github.com/dtolnay/anyhow/blob/c63b279f3f4af2b02ca6267d9eb47d6d10497f69/tests/test_context.rs)
  - [`tests/test_downcast.rs`](https://github.com/dtolnay/anyhow/blob/c63b279f3f4af2b02ca6267d9eb47d6d10497f69/tests/test_downcast.rs)
  - [`README.md`](https://github.com/dtolnay/anyhow/blob/c63b279f3f4af2b02ca6267d9eb47d6d10497f69/README.md)
  - [`Cargo.toml`](https://github.com/dtolnay/anyhow/blob/c63b279f3f4af2b02ca6267d9eb47d6d10497f69/Cargo.toml)
  - [`LICENSE-APACHE`](https://github.com/dtolnay/anyhow/blob/c63b279f3f4af2b02ca6267d9eb47d6d10497f69/LICENSE-APACHE)
- **Trace:** Begin with Context implementations for Result and Option, follow eager or lazy context into Error construction and ContextError, then trace the owned, borrowed, and mutable pointer wrappers and selected ErrorVTable functions that preserve sources, backtraces, formatting, downcasting, and destruction; finish with Chain traversal and the direct context, root-cause, downcast, mutation, alignment, and drop tests.

**Why this level:**

- **Language technique 5:** Expert Rust representation machinery is central and recurring: soundness depends on raw-pointer casts, allocation layout, lifetime reconstruction, type identity, and exact ownership transfer.
- **Behavioral reasoning 4:** Advanced nonlocal representation and ownership reasoning recurs across construction, traversal, downcast, formatting, and drop behavior.
- **Design span 3:** Several meaningful internal layers cooperate, but they remain focused on one in-process application-error abstraction.
- **Constraint burden 5:** Several system-wide memory-safety, representation, compatibility, and semantic guarantees interact; a locally plausible change can introduce undefined behavior or silently lose an error's identity.
- **Placement:** The four scores 5/4/3/5 sum to 17; their arithmetic mean is 4.25 and rounds half-up to Level 4. The published result is Level 4.

**License:** MIT OR Apache-2.0 ([evidence 1](https://github.com/dtolnay/anyhow/blob/c63b279f3f4af2b02ca6267d9eb47d6d10497f69/LICENSE-MIT), [evidence 2](https://github.com/dtolnay/anyhow/blob/c63b279f3f4af2b02ca6267d9eb47d6d10497f69/LICENSE-APACHE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The crate is maintained and published for Rust applications that need one reportable error type across diverse libraries and failure paths.

**Language evidence:** The type-erased error representation, vtable operations, context chains, downcasting, formatting, backtraces, macros, and tests are Rust.

**Coding relevance:**

That short error-handling primer is subordinate to transferable systems-programming lessons in generic conversion, lazy context, type erasure, custom vtables, pointer ownership, source-chain traversal, downcasting, backtrace preservation, conditional compilation, and safety contracts.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** context.rs starts with a small public trait, while error.rs, ptr.rs, and chain.rs make construction, pointer ownership, traversal, downcasting, formatting, and destruction responsibilities explicit.
- **Architecture:** A context extension constructs a type-erased Error whose owned representation uses a selected vtable and pointer wrapper, while Chain exposes source traversal.
- **Naming and idiom:** Context, ContextError, Error, ErrorVTable, owned and borrowed pointers, Chain, source, root cause, and downcast expose both ergonomic and unsafe layers clearly.
- **Tests:** test_context.rs and test_downcast.rs cover eager and lazy context, source layers, root causes, successful and failed downcasts, mutation, alignment, and drop behavior.
- **Documentation:** Public API documentation and README.md explain why application context is added and how source inspection remains available.
- **Traceability:** A Result.context call can be followed into Error construction, its pointer and vtable operations, Chain traversal, and direct context and downcast assertions.
- **Maintainability:** Unsafe ownership is concentrated in named representation modules with safety contracts, and focused tests protect type identity, traversal, alignment, and destruction.
- **Educational value:** The path lets a learner start from ordinary Rust error handling and progressively uncover the representation techniques that make the ergonomic API possible.

**Inspection record:** commit `c63b279f3f4af2b02ca6267d9eb47d6d10497f69`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/context.rs`, `src/error.rs`, `src/ptr.rs`, `src/chain.rs`, `tests/test_context.rs`, `tests/test_downcast.rs`, `README.md`, `Cargo.toml`, `LICENSE-APACHE`, `LICENSE-MIT`. GitHub Linguist label: Rust.

</details>

### [tokio-rs/axum](https://github.com/tokio-rs/axum)

**Language 4 / Behavior 3 / Design 3 / Constraints 4 → Level 4**

A modular asynchronous web framework built around Tokio, Hyper, Tower services, typed request extractors, composable routers, middleware, and response conversion.

**Why study it:** Axum's Json type is a bounded async framework path from request metadata and one-time body ownership to typed input, precise rejection, and response serialization.

**Short context:**

- An HTTP request extractor validates request metadata, consumes the body once, and either gives typed input to a handler or turns a rejection into an HTTP response.
- JSON media types include application/json and structured suffixes such as application/cloudevents+json.

**Prerequisites:**

- Readers should know Rust generics and async traits, ownership of streaming bodies, serde JSON, typed errors, IntoResponse, and basic HTTP content types, requests, responses, and statuses.

**Concepts this path develops:**

- Generic async FromRequest and OptionalFromRequest trait implementations.
- Required versus optional content-type and body states.
- Body ownership, limits, optionality, content-type rules, and deserialization must remain coordinated.

**What you can learn:**

- Trace content-type validation and body buffering into path-aware deserialization, syntax and data rejections, optional extraction, outbound serialization, headers, statuses, and failures.

**Learning path:**

- **Goal:** Understand how Axum's Json type consumes and validates an HTTP request body, produces precise typed rejections, and serializes a typed response with correct metadata.
- **Start here:** [`axum/src/json.rs`](https://github.com/tokio-rs/axum/blob/8f6bb9cead28a3880fe2e448a41ffbfe2c7fe7d9/axum/src/json.rs) — The reviewed trace begins in axum/src/json.rs because Json's FromRequest and IntoResponse implementations contain the complete selected extraction-and-response lifecycle.
- **Then read:**
  - [`axum/src/extract/rejection.rs`](https://github.com/tokio-rs/axum/blob/8f6bb9cead28a3880fe2e448a41ffbfe2c7fe7d9/axum/src/extract/rejection.rs)
  - [`axum-core/src/extract/mod.rs`](https://github.com/tokio-rs/axum/blob/8f6bb9cead28a3880fe2e448a41ffbfe2c7fe7d9/axum-core/src/extract/mod.rs)
  - [`axum-core/src/response/into_response.rs`](https://github.com/tokio-rs/axum/blob/8f6bb9cead28a3880fe2e448a41ffbfe2c7fe7d9/axum-core/src/response/into_response.rs)
  - [`README.md`](https://github.com/tokio-rs/axum/blob/8f6bb9cead28a3880fe2e448a41ffbfe2c7fe7d9/README.md)
  - [`axum/Cargo.toml`](https://github.com/tokio-rs/axum/blob/8f6bb9cead28a3880fe2e448a41ffbfe2c7fe7d9/axum/Cargo.toml)
  - [`LICENSE`](https://github.com/tokio-rs/axum/blob/8f6bb9cead28a3880fe2e448a41ffbfe2c7fe7d9/LICENSE)
- **Trace:** Start with Json<T> and its FromRequest implementation, follow content-type recognition and one-time body buffering into from_bytes and serde_path_to_error, distinguish syntax, data, bytes, and missing-content-type rejections and their IntoResponse behavior, then trace OptionalFromRequest and outbound serialization, content type, and failure handling; close each branch in json.rs's inline async tests.

**Why this level:**

- **Language technique 4:** Advanced generic and asynchronous framework abstractions recur and materially shape the path, without requiring unsafe code or expert metaprogramming.
- **Behavioral reasoning 3:** Several request and error branches must align across asynchronous boundaries, but the complete lifecycle remains one bounded extractor and response component.
- **Design span 3:** Several meaningful framework units cooperate while the selected path avoids the broader router and middleware architecture.
- **Constraint burden 4:** Multiple strict protocol-adapter and compatibility guarantees recur, and plausible local changes can consume a body incorrectly or misclassify client and server failures.
- **Placement:** The four scores 4/3/3/4 sum to 14; their arithmetic mean is 3.50 and rounds half-up to Level 4. The published result is Level 4.

**License:** MIT ([evidence 1](https://github.com/tokio-rs/axum/blob/8f6bb9cead28a3880fe2e448a41ffbfe2c7fe7d9/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The Tokio project maintains and publishes Axum for production HTTP services, with documented middleware, WebSocket, streaming, state, tracing, and deployment patterns.

**Language evidence:** Routing, handlers, extractors, responses, middleware integration, macros, first-party extensions, and test suites are Rust.

**Coding relevance:**

The short HTTP and media-type primer is documented by Axum; the selected path is programming-led and teaches generic async extraction, body ownership, typed rejection design, source-aware serialization errors, response conversion, optional inputs, API documentation, and direct contract tests.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** json.rs keeps media-type policy, body buffering, path-aware deserialization, rejection classification, optional extraction, serialization, headers, and statuses in one readable module.
- **Architecture:** Json implements shared extractor traits to consume a request body and named rejection types to return failures, then implements IntoResponse for outbound serialization.
- **Naming and idiom:** Json, FromRequest, OptionalFromRequest, from_bytes, IntoResponse, and the syntax, data, bytes, and content-type rejections reveal the typed async flow.
- **Tests:** Inline json.rs tests cover required and optional bodies, accepted structured JSON media types, rejected types, syntax and data errors, missing headers, response metadata, and serialization failure.
- **Documentation:** The Json module documentation provides extraction, response, and error-handling examples; README.md supplies framework orientation.
- **Traceability:** A request can be followed from Json's extractor through body parsing to a typed value or named rejection, and an outbound value through IntoResponse to direct inline assertions.
- **Maintainability:** The selected type composes stable core extractor and response traits, and localized exhaustive tests protect the full bounded path without routing breadth.
- **Educational value:** The path demonstrates how typed framework APIs turn ownership and protocol failures into explicit, testable application behavior.

**Inspection record:** commit `8f6bb9cead28a3880fe2e448a41ffbfe2c7fe7d9`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `axum/src/json.rs`, `axum/src/extract/rejection.rs`, `axum-core/src/extract/mod.rs`, `axum-core/src/response/into_response.rs`, `README.md`, `axum/Cargo.toml`, `LICENSE`. GitHub Linguist label: Rust.

</details>

## Level 5 — Expert

### [rust-lang/cargo](https://github.com/rust-lang/cargo)

**Language 4 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

Rust's package manager and build orchestrator, covering manifests, workspaces, lockfiles, dependency resolution, registries and other sources, compilation units, caching, credentials, packaging, publishing, installation, and extensible commands.

**Why study it:** Cargo's JobQueue is an expert but bounded build-system path through dependency readiness, shared jobserver capacity, process orchestration, freshness, diagnostics, artifacts, failures, and shutdown.

**Short context:**

- Cargo turns compilation units and their artifact dependencies into runnable jobs; a GNU-compatible jobserver supplies shared concurrency tokens so Cargo, rustc, build scripts, and nested make processes do not collectively oversubscribe the machine.
- Fresh jobs execute compiler work while fresh jobs can replay cached metadata and messages without rerunning the process.

**Prerequisites:**

- Readers should know advanced Rust, dependency graphs, process execution, channels and state machines, concurrency permits, build freshness, diagnostics, and the GNU jobserver concept.

**Concepts this path develops:**

- Generic dependency queues keyed by units and artifact edges.
- Dependency readiness, artifact edges, freshness, and build-script expansion alter future runnable work.
- Dependency order, artifact readiness, freshness, and exactly-once completion must remain correct.

**What you can learn:**

- Trace compile units through dependency readiness, jobserver tokens, fresh or dirty jobs, process and message state, diagnostics, artifacts, cancellation, failure propagation, and queue draining.

**Learning path:**

- **Goal:** Understand how Cargo schedules dependency-ordered compiler jobs under a shared jobserver limit while coordinating freshness, process output, diagnostics, artifacts, failures, and shutdown.
- **Start here:** [`src/compiler/job_queue/mod.rs`](https://github.com/rust-lang/cargo/blob/e7167a4bac50fd878ce18530e901624d83be218e/src/compiler/job_queue/mod.rs) — The reviewed trace begins in compiler/job_queue/mod.rs because its architecture guide and JobQueue execution loop coordinate every selected graph, token, process, message, and shutdown stage.
- **Then read:**
  - [`src/util/dependency_queue.rs`](https://github.com/rust-lang/cargo/blob/e7167a4bac50fd878ce18530e901624d83be218e/src/util/dependency_queue.rs)
  - [`src/compiler/job_queue/job.rs`](https://github.com/rust-lang/cargo/blob/e7167a4bac50fd878ce18530e901624d83be218e/src/compiler/job_queue/job.rs)
  - [`src/compiler/job_queue/job_state.rs`](https://github.com/rust-lang/cargo/blob/e7167a4bac50fd878ce18530e901624d83be218e/src/compiler/job_queue/job_state.rs)
  - [`src/compiler/build_runner/mod.rs`](https://github.com/rust-lang/cargo/blob/e7167a4bac50fd878ce18530e901624d83be218e/src/compiler/build_runner/mod.rs)
  - [`src/ops/cargo_compile/mod.rs`](https://github.com/rust-lang/cargo/blob/e7167a4bac50fd878ce18530e901624d83be218e/src/ops/cargo_compile/mod.rs)
  - [`tests/testsuite/jobserver.rs`](https://github.com/rust-lang/cargo/blob/e7167a4bac50fd878ce18530e901624d83be218e/tests/testsuite/jobserver.rs)
  - [`README.md`](https://github.com/rust-lang/cargo/blob/e7167a4bac50fd878ce18530e901624d83be218e/README.md)
  - [`LICENSE-APACHE`](https://github.com/rust-lang/cargo/blob/e7167a4bac50fd878ce18530e901624d83be218e/LICENSE-APACHE)
- **Trace:** Begin with the JobQueue module guide, follow BuildRunner as it creates or inherits the jobserver and enqueues compile units, then trace DependencyQueue readiness and artifact edges into DrainState's execution loop, token acquisition, fresh or dirty Job execution, JobState messages, diagnostics, artifacts, failures, cancellation, and shutdown; close graph behavior in DependencyQueue's unit tests and process-sharing and warning behavior in jobserver.rs.

**Why this level:**

- **Language technique 4:** Advanced generic, lifetime, threading, callback, and process abstractions recur, but unsafe memory machinery is not the defining technique of this selected path.
- **Behavioral reasoning 5:** Expert nonlocal graph, concurrency, event-order, process-lifecycle, and failure reasoning recurs throughout the scheduler; validating a change requires reasoning across many possible execution orders.
- **Design span 4:** Several independently meaningful components and external process boundaries cooperate in a bounded but substantial build-execution subsystem.
- **Constraint burden 5:** Several system-wide correctness, liveness, resource, compatibility, and reproducibility guarantees interact; locally plausible scheduler changes can deadlock builds, oversubscribe nested processes, lose diagnostics, or publish incomplete artifacts.
- **Placement:** The four scores 4/5/4/5 sum to 18; their arithmetic mean is 4.50 and rounds half-up to Level 5. The published result is Level 5.

**License:** MIT OR Apache-2.0 ([evidence 1](https://github.com/rust-lang/cargo/blob/e7167a4bac50fd878ce18530e901624d83be218e/LICENSE-MIT), [evidence 2](https://github.com/rust-lang/cargo/blob/e7167a4bac50fd878ce18530e901624d83be218e/LICENSE-APACHE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The Rust project maintains Cargo as the package manager distributed with the Rust toolchain and as the client for crates.io and compatible registries.

**Language evidence:** Manifest and workspace modeling, dependency resolution, package sources, registries, compilation orchestration, caching, credentials, publishing, installation, tests, and the command-line application are Rust.

**Coding relevance:**

The short build-unit and jobserver primer is documented in the selected modules. Transferable dependency-graph scheduling, bounded concurrency, process orchestration, state machines, message queues, failure propagation, cancellation, output serialization, cache freshness, and compatibility engineering explain the path's difficulty.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** job_queue/mod.rs documents its architecture and makes enqueueing, readiness, token acquisition, execution, message draining, freshness, diagnostics, completion, errors, and shutdown explicit.
- **Architecture:** BuildRunner creates or inherits a jobserver, DependencyQueue exposes ready compile units, Job and JobState execute or replay work, and DrainState coordinates messages and completion.
- **Naming and idiom:** JobQueue, DrainState, DependencyQueue, Job, JobState, BuildRunner, freshness, artifacts, and jobserver tokens mirror the build scheduler's actual responsibilities.
- **Tests:** DependencyQueue unit tests protect graph readiness and cycles, while jobserver.rs exercises token inheritance, nested tools, explicit parallelism, invalid descriptors, and warning behavior.
- **Documentation:** The JobQueue module guide explains the internal scheduler, and README.md provides Cargo orientation for the selected build path.
- **Traceability:** A compile unit can be followed from BuildRunner enqueueing through dependency readiness and token acquisition into JobState messages, artifacts, failure, and test assertions.
- **Maintainability:** Graph, process, state, and runner responsibilities have explicit modules, and unit plus integration tests protect concurrency and compatibility boundaries.
- **Educational value:** The path exposes how a production build tool coordinates local work with nested external processes without oversubscribing or losing diagnostic state.

**Inspection record:** commit `e7167a4bac50fd878ce18530e901624d83be218e`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/compiler/job_queue/mod.rs`, `src/util/dependency_queue.rs`, `src/compiler/job_queue/job.rs`, `src/compiler/job_queue/job_state.rs`, `src/compiler/build_runner/mod.rs`, `src/ops/cargo_compile/mod.rs`, `tests/testsuite/jobserver.rs`, `README.md`, `LICENSE-APACHE`, `LICENSE-MIT`. GitHub Linguist label: Rust.

</details>

### [tokio-rs/tokio](https://github.com/tokio-rs/tokio)

**Language 5 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

An asynchronous runtime platform for Rust with multi-thread and current-thread schedulers, task lifecycles, OS-backed I/O, timers, networking, synchronization, processes, signals, files, macros, streams, and utilities.

**Why study it:** Tokio's bounded MPSC channel is a complete expert trace through permits, backpressure, lock-free storage, wakeups, cancellation, closure, destruction, and model-checked interleavings.

**Short context:**

- A bounded multi-producer, single-consumer channel gives senders permits before enqueueing values so capacity creates backpressure; closing prevents new sends while allowing already queued values and outstanding permits to resolve.
- Loom systematically explores small concurrent executions by substituting modeled atomics, threads, and synchronization primitives.

**Prerequisites:**

- Readers should know advanced Rust ownership and lifetimes, async polling and wakers, atomics, UnsafeCell and unsafe invariants, semaphores, lock-free queues, cancellation safety, and Loom-style model checking.

**Concepts this path develops:**

- Unsafe lock-free linked blocks with UnsafeCell and atomic readiness state.
- Many concurrent send, reserve, cancel, receive, close, wake, and drop interleavings.
- Memory safety, initialization, aliasing, atomic ordering, reclamation, and panic-safe destruction must remain sound.

**What you can learn:**

- Trace send and reserve through semaphore permits into linked message blocks, readiness publication, receiver wakeup, dequeue, closure, outstanding permits, drops, reclamation, and panic safety.

**Learning path:**

- **Goal:** Understand how Tokio's bounded MPSC channel coordinates permits, lock-free message storage, receiver wakeups, cancellation, closure, and destruction safely across concurrent senders.
- **Start here:** [`tokio/src/sync/mpsc/bounded.rs`](https://github.com/tokio-rs/tokio/blob/ea91b33ca57ff0581b38e735cc108f831bccbdaa/tokio/src/sync/mpsc/bounded.rs) — The reviewed trace begins in bounded.rs because it defines channel construction and the Sender, Receiver, and Permit contracts that the internal concurrent machinery must preserve.
- **Then read:**
  - [`tokio/src/sync/mpsc/mod.rs`](https://github.com/tokio-rs/tokio/blob/ea91b33ca57ff0581b38e735cc108f831bccbdaa/tokio/src/sync/mpsc/mod.rs)
  - [`tokio/src/sync/mpsc/chan.rs`](https://github.com/tokio-rs/tokio/blob/ea91b33ca57ff0581b38e735cc108f831bccbdaa/tokio/src/sync/mpsc/chan.rs)
  - [`tokio/src/sync/mpsc/list.rs`](https://github.com/tokio-rs/tokio/blob/ea91b33ca57ff0581b38e735cc108f831bccbdaa/tokio/src/sync/mpsc/list.rs)
  - [`tokio/src/sync/mpsc/block.rs`](https://github.com/tokio-rs/tokio/blob/ea91b33ca57ff0581b38e735cc108f831bccbdaa/tokio/src/sync/mpsc/block.rs)
  - [`tokio/src/sync/batch_semaphore.rs`](https://github.com/tokio-rs/tokio/blob/ea91b33ca57ff0581b38e735cc108f831bccbdaa/tokio/src/sync/batch_semaphore.rs)
  - [`tokio/src/sync/tests/loom_mpsc.rs`](https://github.com/tokio-rs/tokio/blob/ea91b33ca57ff0581b38e735cc108f831bccbdaa/tokio/src/sync/tests/loom_mpsc.rs)
  - [`tokio/src/sync/tests/loom_semaphore_batch.rs`](https://github.com/tokio-rs/tokio/blob/ea91b33ca57ff0581b38e735cc108f831bccbdaa/tokio/src/sync/tests/loom_semaphore_batch.rs)
  - [`tokio/tests/sync_mpsc.rs`](https://github.com/tokio-rs/tokio/blob/ea91b33ca57ff0581b38e735cc108f831bccbdaa/tokio/tests/sync_mpsc.rs)
  - [`README.md`](https://github.com/tokio-rs/tokio/blob/ea91b33ca57ff0581b38e735cc108f831bccbdaa/README.md)
  - [`LICENSE`](https://github.com/tokio-rs/tokio/blob/ea91b33ca57ff0581b38e735cc108f831bccbdaa/LICENSE)
- **Trace:** Begin with bounded channel construction and the Sender, Receiver, and Permit APIs, follow send or reserve into BatchSemaphore capacity acquisition and cancellation, then enter chan.rs as a value claims a list position, writes through block UnsafeCell state, marks readiness, wakes the receiver, and is polled or drained; trace sender counts, close, outstanding permits, receiver and sender drops, block reclamation, and panic guards, then close ordinary behavior in sync_mpsc.rs and adversarial interleavings in the two Loom suites.

**Why this level:**

- **Language technique 5:** Expert Rust concurrency and unsafe representation machinery is central and recurring; soundness depends on atomic ordering, aliasing, initialization, pinning, ownership, and destructor contracts.
- **Behavioral reasoning 5:** Expert nonlocal concurrency, liveness, cancellation, ownership, and event-order reasoning recurs; validating behavior requires considering adversarial interleavings rather than one trace.
- **Design span 4:** Several independently meaningful concurrency components cooperate in one bounded channel subsystem, while the broader Tokio scheduler, networking, timer, and process architecture is deliberately excluded.
- **Constraint burden 5:** Several system-wide safety, liveness, resource, ordering, compatibility, and performance guarantees interact; a locally plausible change can cause undefined behavior, deadlock, a lost wakeup, capacity leakage, or message loss.
- **Placement:** The four scores 5/5/4/5 sum to 19; their arithmetic mean is 4.75 and rounds half-up to Level 5. The published result is Level 5.

**License:** MIT ([evidence 1](https://github.com/tokio-rs/tokio/blob/ea91b33ca57ff0581b38e735cc108f831bccbdaa/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The Tokio project maintains and publishes the runtime and companion crates as infrastructure for asynchronous Rust applications and libraries.

**Language evidence:** The asynchronous runtime, task scheduler and harness, OS I/O driver, timers, synchronization channels, networking, processes, signals, filesystem adapters, macros, utilities, model tests, and integration suites are Rust.

**Coding relevance:**

The short channel and model-checking primer is documented by Tokio. Transferable async API design, atomic state, lock-free linked storage, waker protocols, semaphore permits, backpressure, cancellation safety, close and drop ownership, panic safety, model checking, and exhaustive direct tests explain the path's difficulty.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** bounded.rs documents public contracts, chan.rs owns shared state and semaphore integration, list.rs and block.rs localize lock-free storage, and batch_semaphore.rs owns fair capacity acquisition.
- **Architecture:** A sender acquires a batch-semaphore permit, enqueues into linked blocks, publishes readiness and wakes the receiver; shared state coordinates counts, close, drop, draining, and reclamation.
- **Naming and idiom:** Sender, Receiver, Permit, chan, list, block, BatchSemaphore, readiness, close, and wakeups expose the concurrency protocol alongside precise Rust ownership and safety comments.
- **Tests:** sync_mpsc.rs exhaustively covers capacity, ordering, reservation, cancellation, closure, counts, weak senders, drops, and panics; Loom suites explore MPSC and semaphore interleavings.
- **Documentation:** The bounded channel's inline API documentation states backpressure, reservation, closure, and cancellation contracts; README.md orients Tokio.
- **Traceability:** A reserved send can be followed from permit acquisition through block publication and wakeup to receive or drain, then checked in direct and Loom tests.
- **Maintainability:** Semaphore, channel state, and lock-free storage are separated, unsafe access carries explicit invariants, and model checking guards race-sensitive changes.
- **Educational value:** The path joins a familiar asynchronous channel API to the exact memory, fairness, wakeup, and lifecycle machinery needed to make it safe.

**Inspection record:** commit `ea91b33ca57ff0581b38e735cc108f831bccbdaa`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `tokio/src/sync/mpsc/bounded.rs`, `tokio/src/sync/mpsc/mod.rs`, `tokio/src/sync/mpsc/chan.rs`, `tokio/src/sync/mpsc/list.rs`, `tokio/src/sync/mpsc/block.rs`, `tokio/src/sync/batch_semaphore.rs`, `tokio/src/sync/tests/loom_mpsc.rs`, `tokio/src/sync/tests/loom_semaphore_batch.rs`, `tokio/tests/sync_mpsc.rs`, `README.md`, `LICENSE`. GitHub Linguist label: Rust.

</details>

_Generated from `catalog/rust.json`; do not edit by hand._

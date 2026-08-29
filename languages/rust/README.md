# Rust

10 qualified repositories. Scores assume the learner described in [the SDC rubric](../../docs/sdc.md).

[← All languages](../README.md)

## SDC 1

### [rust-lang/rustc-hash](https://github.com/rust-lang/rustc-hash)

**S1 / D2 / C1 → SDC 1**

A compact implementation of the fast, non-cryptographic hash algorithm used by the Rust compiler, with seeded map and set builders.

**Real-world evidence:** The Rust project maintains the crate as the Fx hash implementation used by rustc and distributes it through crates.io.

**Language evidence:** The hashers, seeded build state, HashMap and HashSet aliases, byte-compression paths, and deterministic tests are implemented in Rust.

**Why study it:** Its entire mechanism fits in a few files while exposing integer mixing, native-word specialization, chunked byte input, deterministic seeds, trait implementation, and explicit non-security boundaries.

**What you can learn:**

- Hasher and BuildHasher traits, wrapping arithmetic, polynomial mixing, 32-bit and 64-bit specialization, byte chunking, deterministic seeding, type aliases, and golden-vector tests.

**Prerequisites:**

- Basic Rust ownership and traits, integers and byte slices, generics and type aliases, hash tables, wrapping arithmetic, and unit tests.

**Start here:** [`src/lib.rs`](https://github.com/rust-lang/rustc-hash/blob/6ced6cb4235295509102d05f8915e0bb0d8cfe54/src/lib.rs) — The public aliases and complete FxHasher implementation can be read end to end before following the optional seeded builder.

**Why this level:**

- **S1:** 403 meaningful implementation LOC measured with tokei 14.0.0. Count covers the complete production Rust source under src.
- **D2:** The arithmetic needs careful reading, but the crate implements one bounded algorithm through standard library traits.
- **C1:** There are no external systems, asynchronous paths, plugins, processes, or persistent state.
- **Placement:** S1/D2/C1 averages to 1.33, making rustc-hash an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** The mixing function, byte lanes, tail handling, seeded state, and safety limitation are short, explicit, and free of hidden framework behavior.
- **Architecture:** The main module owns the hasher and collection aliases while one secondary module adds reusable seeded BuildHasher state.
- **Naming and idiom:** FxHasher, FxBuildHasher, add_to_hash, hash_word, write, seed, FxHashMap, and FxHashSet match Rust hashing vocabulary.
- **Tests:** Deterministic vectors exercise every primitive write method, byte lengths and tails, 32-bit and 64-bit behavior, seeded builders, and collection aliases.
- **Documentation:** The README and crate-level documentation explain the rustc origin, performance purpose, deterministic default, seeding option, and denial-of-service limitation.
- **Traceability:** A byte slice can be followed through native-word loads, tail construction, polynomial mixing, finish, a map alias, and exact expected hashes.
- **Maintainability:** A tiny public surface, no dependencies, platform-specific tests, and clearly isolated seeding keep changes reviewable.
- **Educational value:** It is a strong first Rust codebase because real low-level behavior is visible without requiring a large architecture.

**Inspection record:** commit `6ced6cb4235295509102d05f8915e0bb0d8cfe54`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Cargo.toml`, `src/lib.rs`, `src/seeded_state.rs`, `LICENSE-APACHE`. GitHub Linguist label: Rust. LOC exclusions: benchmarks, fuzz targets, documentation, and package metadata.

**License:** [Apache-2.0 OR MIT](https://github.com/rust-lang/rustc-hash/blob/6ced6cb4235295509102d05f8915e0bb0d8cfe54/LICENSE-APACHE)

### [withoutboats/heck](https://github.com/withoutboats/heck)

**S1 / D2 / C1 → SDC 1**

A no_std string case-conversion library supporting snake, kebab, title, train, shouty, lower camel, and upper camel forms.

**Real-world evidence:** The maintained crate is published for use by Rust libraries, procedural macros, and applications that need predictable identifier and display-name conversion.

**Language evidence:** The shared word-boundary transform, eight case-style modules, display adapters, Unicode handling, and inline test matrices are Rust.

**Why study it:** A small common transform turns subtle acronym, digit, lowercase, uppercase, Unicode, and separator rules into reusable conversion traits and zero-allocation display wrappers.

**What you can learn:**

- Unicode-aware character iteration, word-boundary state, acronym splitting, case conversion traits, Display wrappers, no_std design, module reuse, and table-driven tests.

**Prerequisites:**

- Basic Rust modules and traits, iterators and closures, Unicode characters, string formatting, generics, and unit tests.

**Start here:** [`src/lib.rs`](https://github.com/withoutboats/heck/blob/252c1906cefefb8d13ecad7fce7b8f27ce6437e0/src/lib.rs) — The shared transform function defines the word-boundary algorithm that every public case module reuses.

**Why this level:**

- **S1:** 512 meaningful implementation LOC measured with tokei 14.0.0. Count covers all production Rust modules under src, including their inline behavior tests.
- **D2:** Text edge cases require precision, but one finite state walk supplies every output style.
- **C1:** All behavior is local, synchronous, stateless, and dependency-free.
- **Placement:** S1/D2/C1 averages to 1.33, making heck an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** Word boundaries are expressed as readable character predicates and each style supplies only its first-word, next-word, and boundary formatting choices.
- **Architecture:** One shared transform owns tokenization; small modules expose traits and display types for each naming convention.
- **Naming and idiom:** ToSnakeCase, AsSnakeCase, transform, word_boundary, first_word, boundary, and upper_camel state both operation and representation.
- **Tests:** Each style carries compact matrices for spaces, punctuation, digits, acronyms, mixed case, repeated separators, Greek sigma, and Unicode case expansion.
- **Documentation:** The README and module documentation enumerate the supported conventions and show direct string and display-wrapper use.
- **Traceability:** An input can be followed character by character through boundary detection into a case module and an exact expected output.
- **Maintainability:** The common algorithm prevents eight implementations from drifting, while local tests document each public convention.
- **Educational value:** It demonstrates how a tiny library can centralize subtle language rules without obscuring them behind dependencies.

**Inspection record:** commit `252c1906cefefb8d13ecad7fce7b8f27ce6437e0`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Cargo.toml`, `src/lib.rs`, `src/snake.rs`, `src/upper_camel.rs`, `src/lower_camel.rs`, `LICENSE-APACHE`. GitHub Linguist label: Rust. LOC exclusions: documentation and package metadata.

**License:** [MIT OR Apache-2.0](https://github.com/withoutboats/heck/blob/252c1906cefefb8d13ecad7fce7b8f27ce6437e0/LICENSE-APACHE)

## SDC 2

### [dtolnay/anyhow](https://github.com/dtolnay/anyhow)

**S2 / D3 / C2 → SDC 2**

A flexible application-error type that carries context, error chains, downcasting, backtraces, and ergonomic propagation across arbitrary error sources.

**Real-world evidence:** The crate is maintained and published for Rust applications that need one reportable error type across diverse libraries and failure paths.

**Language evidence:** The type-erased error representation, vtable operations, context chains, downcasting, formatting, backtraces, macros, and tests are Rust.

**Why study it:** Its friendly Result and Context API leads into a carefully engineered pointer layout, manually selected vtables, owned and borrowed traversal, downcasting, backtrace capture, no_std support, and formatting.

**What you can learn:**

- Error trait objects, context chaining, type erasure, custom vtables, pointer layouts, downcasting, backtraces, conversion traits, macros, no_std fallbacks, and compile-time API tests.

**Prerequisites:**

- Comfortable Rust ownership, lifetimes and traits, Result and the Error trait, generic conversions, trait objects, pointers, macros, and conditional compilation.

**Start here:** [`src/error.rs`](https://github.com/dtolnay/anyhow/blob/c63b279f3f4af2b02ca6267d9eb47d6d10497f69/src/error.rs) — The Error constructors reveal how public conversions choose representations, capture backtraces, build vtables, and preserve sources for later traversal and downcasting.

**Why this level:**

- **S2:** 2,416 meaningful implementation LOC measured with tokei 14.0.0. Count covers all production Rust source under src.
- **D3:** The public API is compact, but implementing it safely requires advanced ownership and representation reasoning.
- **C2:** Several internal representations support one cohesive in-process error-reporting abstraction.
- **Placement:** S2/D3/C2 averages to 2.33, making anyhow an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** Allocation layouts, vtable functions, ownership transfers, pointer casts, source traversal, and safety assumptions are localized and documented.
- **Architecture:** A public Error and Result surface sits over constructors, context adapters, chains, formatting, pointer ownership, backtrace support, and macro modules.
- **Naming and idiom:** Context, Error, Chain, root_cause, downcast_ref, from_boxed, construct_from_std, error_impl, and vtable expose error-system roles.
- **Tests:** Runtime, compile-pass, compile-fail, no_std, formatting, context, downcast, source-chain, backtrace, size, and lifetime tests protect both semantics and API ergonomics.
- **Documentation:** The README and crate documentation teach propagation, context, downcasting, backtraces, no_std use, display forms, and the distinction from library-focused typed errors.
- **Traceability:** A concrete error can be followed into an allocated representation, through context and a source chain, then back through formatting or type-aware downcasting.
- **Maintainability:** Representation variants share vtable machinery, unsafe code stays concentrated, feature modes are tested, and the user-facing contract remains narrow.
- **Educational value:** It connects idiomatic application error handling to the advanced Rust machinery required to make that simplicity possible.

**Inspection record:** commit `c63b279f3f4af2b02ca6267d9eb47d6d10497f69`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Cargo.toml`, `src/lib.rs`, `src/error.rs`, `src/context.rs`, `tests/test_context.rs`, `tests/test_downcast.rs`, `LICENSE-APACHE`. GitHub Linguist label: Rust. LOC exclusions: tests/, compile-test fixtures, examples, documentation, and package metadata.

**License:** [MIT OR Apache-2.0](https://github.com/dtolnay/anyhow/blob/c63b279f3f4af2b02ca6267d9eb47d6d10497f69/LICENSE-APACHE)

### [dtolnay/semver](https://github.com/dtolnay/semver)

**S1 / D3 / C2 → SDC 2**

A parser and evaluator for Cargo-flavored Semantic Versioning versions and requirements, including caret, tilde, wildcard, range, and prerelease rules.

**Real-world evidence:** The maintained crate is published for Rust tools that interpret Cargo-compatible versions and dependency requirements.

**Language evidence:** Version and requirement models, parsing, comparator evaluation, formatting, error reporting, fuzz targets, and tests are Rust.

**Why study it:** A compact domain library turns a familiar specification into explicit data types, a byte-level parser, precise position-aware errors, comparator normalization, matching semantics, and stable formatting.

**What you can learn:**

- Domain modeling, byte parsers, semantic-version grammar, comparator operators, caret and tilde ranges, wildcards, prerelease matching, error locations, formatting, property tests, and fuzzing.

**Prerequisites:**

- Rust structs, enums, traits and lifetimes, slices and byte parsing, semantic versioning concepts, ordering, error types, and test-driven specification work.

**Start here:** [`src/parse.rs`](https://github.com/dtolnay/semver/blob/280ebcb6edac3aa4cdc545dbff8a26c5ac4861fe/src/parse.rs) — The hand-written parser shows how versions and requirements become typed values while preserving exact failure positions and grammar expectations.

**Why this level:**

- **S1:** 1,335 meaningful implementation LOC measured with tokei 14.0.0. Count covers the complete production Rust implementation under src.
- **D3:** Correctness is domain-heavy and edge-sensitive, but the parser and evaluator are direct, pure, and bounded.
- **C2:** Several cohesive modules implement one synchronous value-domain library without external integration.
- **Placement:** S1/D3/C2 averages to 2.00, making semver an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** Parsing state, numeric overflow, identifiers, separators, operators, wildcard normalization, evaluation predicates, and error spans are explicit.
- **Architecture:** Public value types delegate parsing to a cursor-based module and requirement matching to a separate evaluator, with formatting alongside the models.
- **Naming and idiom:** Version, VersionReq, Comparator, Op, Prerelease, BuildMetadata, parse_optional_meta, eval, and matches mirror the specification.
- **Tests:** Focused suites cover accepted and rejected versions and requirements, every operator family, prerelease rules, whitespace, overflow, display round trips, hashing, ordering, size, properties, and fuzzing.
- **Documentation:** The README and API documentation explain Cargo's flavor, parsing, construction, comparison, requirements, prerelease handling, and feature support.
- **Traceability:** A requirement string can be followed from cursor operations into comparators, through operator-specific evaluation, to a precise match or parse error assertion.
- **Maintainability:** Grammar and matching logic are separated, public types are small, errors retain positions, and dense boundary tests encode the domain contract.
- **Educational value:** It is a compact example of translating a prose specification into auditable types, parsing rules, and executable semantics.

**Inspection record:** commit `280ebcb6edac3aa4cdc545dbff8a26c5ac4861fe`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Cargo.toml`, `src/lib.rs`, `src/parse.rs`, `src/eval.rs`, `tests/test_version.rs`, `tests/test_version_req.rs`, `LICENSE-APACHE`. GitHub Linguist label: Rust. LOC exclusions: tests/, fuzz/, documentation, and package metadata.

**License:** [MIT OR Apache-2.0](https://github.com/dtolnay/semver/blob/280ebcb6edac3aa4cdc545dbff8a26c5ac4861fe/LICENSE-APACHE)

## SDC 3

### [serde-rs/json](https://github.com/serde-rs/json)

**S3 / D3 / C3 → SDC 3**

Serde's production JSON implementation for typed and untyped data, streaming readers and writers, arbitrary-precision options, raw values, and no_std allocation environments.

**Real-world evidence:** The Serde project maintains and publishes serde_json as the JSON format implementation used by Rust applications and libraries.

**Language evidence:** JSON serialization and deserialization, streaming input, value and number models, raw values, error handling, tests, and fuzz targets are implemented in Rust.

**Why study it:** It shows a mature format implementation from byte and I/O readers through grammar, visitor-driven deserialization, serializers, dynamic values, number semantics, raw fragments, streaming, limits, and exhaustive regressions.

**What you can learn:**

- Serde data models and visitors, JSON grammar, streaming deserialization, generic readers and writers, escaping, number representations, recursion limits, raw values, feature flags, fuzzing, and regression design.

**Prerequisites:**

- Comfortable Rust generics, traits and lifetimes, Serde concepts, byte and text encodings, JSON grammar, I/O, macros, feature flags, and property or fuzz testing.

**Start here:** [`src/de.rs`](https://github.com/serde-rs/json/blob/afdf6fc67247dd7fa4fcde1381e6ecc6bcc7a30e/src/de.rs) — The deserializer connects input abstractions, whitespace and token handling, recursion limits, numeric paths, strings, sequences, maps, enums, and streaming iteration.

**Why this level:**

- **S3:** 10,622 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production Rust under src plus build.rs, excluding the explicitly attributed lexical implementation.
- **D3:** Many representation and input modes must agree, but the format is familiar and responsibilities are clearly divided.
- **C3:** Multiple public modes and compile configurations interact inside one substantial format library.
- **Placement:** S3/D3/C3 averages to 3.00, making serde_json an SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** Token dispatch, visitor calls, recursion checks, map and sequence termination, escaping, number conversion, I/O errors, and raw-fragment boundaries are explicit.
- **Architecture:** Input adapters feed a generic deserializer; a mirrored serializer writes outputs; value, map, number, raw, error, read, and feature modules provide focused representations.
- **Naming and idiom:** Deserializer, Serializer, Value, Number, RawValue, StreamDeserializer, read, peek, parse_value, serialize_map, and end follow Serde and JSON concepts.
- **Tests:** Large suites cover parsing and writing, streams, recursion, numeric boundaries and round trips, maps, raw values, features, regressions, malformed corpora, allocation modes, and fuzz targets.
- **Documentation:** The README and crate documentation explain typed, untyped, and streaming use, construction, I/O, feature flags, no_std support, and common errors.
- **Traceability:** Input bytes can be followed through a reader and JSON token path into a Serde visitor or Value, then back through the serializer and exact round-trip assertions.
- **Maintainability:** Core format concerns are separated, alternate modes are feature-gated and tested, compatibility is explicit, and attributed third-party-derived code is identifiable.
- **Educational value:** It is a production-scale bridge from parser fundamentals to generic framework integration without yet requiring service architecture.

**Inspection record:** commit `afdf6fc67247dd7fa4fcde1381e6ecc6bcc7a30e`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Cargo.toml`, `src/de.rs`, `src/ser.rs`, `src/value/mod.rs`, `src/raw.rs`, `tests/test.rs`, `LICENSE-APACHE`. GitHub Linguist label: Rust. LOC exclusions: tests/, fuzz/, examples, documentation, package metadata, and src/lexical/ derived or adapted from rust-lexical.

**License:** [MIT OR Apache-2.0](https://github.com/serde-rs/json/blob/afdf6fc67247dd7fa4fcde1381e6ecc6bcc7a30e/LICENSE-APACHE)

### [tokio-rs/axum](https://github.com/tokio-rs/axum)

**S3 / D3 / C3 → SDC 3**

A modular asynchronous web framework built around Tokio, Hyper, Tower services, typed request extractors, composable routers, middleware, and response conversion.

**Real-world evidence:** The Tokio project maintains and publishes Axum for production HTTP services, with documented middleware, WebSocket, streaming, state, tracing, and deployment patterns.

**Language evidence:** Routing, handlers, extractors, responses, middleware integration, macros, first-party extensions, and test suites are Rust.

**Why study it:** It makes HTTP application composition traceable across route recognition, handler trait conversion, ordered body-consuming extractors, state, response types, Tower middleware, rejection handling, and macro diagnostics.

**What you can learn:**

- Async HTTP services, route matching, handler traits, request extractors, body ownership, response conversion, application state, middleware layers, Tower Service integration, WebSockets, macros, and compile-fail API tests.

**Prerequisites:**

- Comfortable Rust traits, generics, async and Future, Tokio, HTTP requests and responses, ownership of streaming bodies, middleware concepts, macros, and integration testing.

**Start here:** [`axum/src/routing/path_router.rs`](https://github.com/tokio-rs/axum/blob/8f6bb9cead28a3880fe2e448a41ffbfe2c7fe7d9/axum/src/routing/path_router.rs) — The path router connects user routes to matching, nesting, conflict checks, method routers, URL parameters, fallbacks, state, and Tower service calls.

**Why this level:**

- **S3:** 21,005 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production Rust in axum, axum-core, axum-extra, and axum-macros.
- **D3:** The type system and asynchronous HTTP lifecycle require fluency, but user-facing concepts map cleanly to focused modules.
- **C3:** Several framework subsystems compose a full request path, while established Tokio, Hyper, and Tower layers own lower-level transport machinery.
- **Placement:** S3/D3/C3 averages to 3.00, making Axum an SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** Route insertion and matching, handler futures, extractor ordering, body ownership, rejection conversion, and Service implementations expose their invariants rather than hiding them in generated code.
- **Architecture:** axum-core defines extraction and response contracts; axum supplies routing and handlers; axum-macros improves diagnostics; axum-extra carries optional higher-level integrations.
- **Naming and idiom:** Router, MethodRouter, Handler, FromRequestParts, FromRequest, IntoResponse, State, Extension, rejection, and layer match HTTP application roles.
- **Tests:** Unit, integration, compile-fail, macro, routing, extraction, response, middleware, state, WebSocket, and example tests cover behavior and invalid API composition.
- **Documentation:** The README, module documentation, examples, and API guides explain routing, extraction, responses, state, middleware, error handling, testing, and common deployment patterns.
- **Traceability:** A request can be followed from URI matching through a method route, handler future, ordered extractors, application code, IntoResponse, middleware, and an integration assertion.
- **Maintainability:** Core contracts are small, optional features and extensions are separated, diagnostics are tested, and compatibility work remains at explicit framework boundaries.
- **Educational value:** It teaches how idiomatic Rust types become an ergonomic web framework while keeping the underlying HTTP service pipeline visible.

**Inspection record:** commit `8f6bb9cead28a3880fe2e448a41ffbfe2c7fe7d9`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `axum/Cargo.toml`, `axum/src/routing/path_router.rs`, `axum/src/handler/mod.rs`, `axum/src/json.rs`, `axum-core/src/extract/mod.rs`, `axum-core/src/response/into_response.rs`, `LICENSE`. GitHub Linguist label: Rust. LOC exclusions: examples/, tests/, benches, embedded documentation examples, generated artifacts, and package metadata.

**License:** [MIT](https://github.com/tokio-rs/axum/blob/8f6bb9cead28a3880fe2e448a41ffbfe2c7fe7d9/LICENSE)

## SDC 4

### [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)

**S3 / D4 / C4 → SDC 4**

A recursive command-line search tool that combines regex engines, Git-style ignore rules, parallel filesystem traversal, binary and encoding detection, decompression, preprocessors, and multiple printers.

**Real-world evidence:** The maintained project ships cross-platform ripgrep releases as a general-purpose replacement for recursive grep workflows.

**Language evidence:** Command normalization, parallel traversal, ignore matching, regex search, encoding and decompression paths, printers, output formats, and tests are Rust.

**Why study it:** It carries a rich CLI through normalized configuration into ignore-aware walks, engine selection, sequential or parallel search, buffering and memory maps, binary and encoding policy, match sinks, and human or machine output.

**What you can learn:**

- CLI normalization, filesystem traversal, ignore and glob precedence, regex-engine selection, parallel work, buffered and memory-mapped search, binary detection, transcoding, decompression, preprocessors, match sinks, terminal output, JSON Lines, and regression testing.

**Prerequisites:**

- Advanced Rust, command-line and filesystem semantics, regular expressions, concurrency, byte-oriented I/O, encodings, process spawning, terminal behavior, and cross-platform testing.

**Start here:** [`crates/core/main.rs`](https://github.com/BurntSushi/ripgrep/blob/3fce3b5bb0236da2df6d99672afb8a719642eca7/crates/core/main.rs) — The main execution path turns parsed flags into high-level arguments, chooses help, version, and search modes, builds the search worker, and selects parallel or sequential traversal.

**Why this level:**

- **S3:** 35,938 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production Rust across the ripgrep workspace crates.
- **D4:** Performance and correctness cross many operating-system and input boundaries, though the product remains a local command-line application.
- **C4:** A broad workspace composes many libraries into one tool with numerous modes and platform-specific branches.
- **Placement:** S3/D4/C4 averages to 3.67, making ripgrep an SDC 4 project.

**Quality-gate evidence:**

- **Source quality:** High-level argument normalization centralizes policy, search workers separate setup from execution, and match sinks make output and stopping behavior explicit.
- **Architecture:** A binary-facing core composes dedicated crates for ignore traversal, globs, regex engines, matching, searching, printing, terminal colors, and process helpers.
- **Naming and idiom:** HiArgs, SearchWorker, Searcher, Matcher, Sink, WalkBuilder, Override, Printer, haystack, preprocessor, and mode expose the search domain.
- **Tests:** Workspace unit tests and end-to-end regression suites cover flags, ignore precedence, globs, encodings, binary files, multiline search, engines, contexts, replacements, archives, preprocessors, paths, colors, and JSON output.
- **Documentation:** The README, user guide, FAQ, man page sources, completion definitions, and crate documentation explain behavior, performance tradeoffs, configuration, engines, encodings, and platform caveats.
- **Traceability:** A command-line flag can be followed through HiArgs into walker and searcher construction, a selected matcher and sink, a printer event, and an end-to-end regression fixture.
- **Maintainability:** Workspace crates preserve narrow responsibilities, policy is normalized once, output formats have explicit contracts, and extensive cross-platform regressions protect user-visible semantics.
- **Educational value:** It is an unusually traceable example of evolving a fast systems tool without sacrificing command-line ergonomics or correctness.

**Inspection record:** commit `3fce3b5bb0236da2df6d99672afb8a719642eca7`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `GUIDE.md`, `Cargo.toml`, `crates/core/main.rs`, `crates/core/flags/hiargs.rs`, `crates/core/search.rs`, `COPYING`. GitHub Linguist label: Rust. LOC exclusions: tests, examples, benches, documentation, shell completions, static metadata, generated artifacts, and non-Rust support files.

**License:** [Unlicense OR MIT](https://github.com/BurntSushi/ripgrep/blob/3fce3b5bb0236da2df6d99672afb8a719642eca7/COPYING)

### [rustls/rustls](https://github.com/rustls/rustls)

**S3 / D5 / C4 → SDC 4**

A modern TLS 1.2 and TLS 1.3 library with client and server state machines, pluggable cryptographic providers, certificate verification, encrypted records, and safe high-level APIs.

**Real-world evidence:** The maintained rustls project publishes production TLS crates and integrations and documents an attacker-controlled-network threat model and security reporting process.

**Language evidence:** TLS protocol state, records and messages, client and server connections, certificate verification, provider interfaces, fuzz targets, and tests are Rust.

**Why study it:** It exposes how an adversarial wire protocol becomes parsed messages, handshake state, key schedules, record protection, certificate verification, connection I/O, resumption, and deliberately constrained public configuration.

**What you can learn:**

- TLS 1.2 and 1.3 state machines, protocol messages, records, key schedules, certificate verification, cryptographic provider interfaces, client and server configuration, session resumption, secrets, fuzzing, and security-oriented API design.

**Prerequisites:**

- Advanced Rust, network protocols and byte parsing, TLS concepts, public-key infrastructure, cryptographic primitives at an integration level, state machines, I/O buffering, adversarial testing, and secure API design.

**Start here:** [`rustls/src/conn/mod.rs`](https://github.com/rustls/rustls/blob/3925f65934364edafe8d6b20707d9e5e6183648e/rustls/src/conn/mod.rs) — The connection core ties public client and server objects to common protocol state, encrypted and plaintext I/O, packet processing, limits, secrets, and lifecycle transitions.

**Why this level:**

- **S3:** 36,965 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production Rust in the core rustls crate and its shared supporting source.
- **D5:** Errors at protocol, verification, or key-state boundaries can compromise confidentiality or authentication, demanding expert security review.
- **C4:** Many security-sensitive modules and implementations cooperate, although the project remains a library rather than an independently deployed distributed system.
- **Placement:** S3/D5/C4 averages to 4.00; the D5 floor also requires at least SDC 4.

**Quality-gate evidence:**

- **Source quality:** Protocol states, message expectations, record limits, key transitions, authentication outcomes, secret extraction, and error propagation are explicit and typed.
- **Architecture:** Shared connection machinery supports separate client and server handshakes over message and record modules, verification interfaces, cryptographic providers, PKI types, resumption, and persistence.
- **Naming and idiom:** ClientConnection, ServerConnection, CommonState, ConnectionCore, Message, HandshakeType, ServerCertVerifier, CryptoProvider, traffic_secret, and wants_read expose protocol roles.
- **Tests:** Protocol, API, interoperability, bad-message, handshake, verification, resumption, fragmentation, I/O, provider, property, benchmark, and fuzz suites exercise success and adversarial paths.
- **Documentation:** The README, security policy, crate documentation, examples, and API comments explain protocol support, providers, platform verification, dangerous configuration, limits, threat assumptions, and integration patterns.
- **Traceability:** A received TLS record can be followed through decoding, state-specific message handling, certificate or key checks, traffic-state changes, plaintext release, and hostile-input tests.
- **Maintainability:** Protocol versions and roles are partitioned, cryptography is provider-gated, unsafe code is restricted, security boundaries are documented, and fuzz and interoperability coverage protect changes.
- **Educational value:** It is a rigorous study of how to represent a security protocol so invalid states, hostile bytes, and dangerous configuration remain reviewable.

**Inspection record:** commit `3925f65934364edafe8d6b20707d9e5e6183648e`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `SECURITY.md`, `rustls/Cargo.toml`, `rustls/src/lib.rs`, `rustls/src/conn/mod.rs`, `rustls/src/client/connection.rs`, `rustls/src/server/connection.rs`, `rustls/src/verify.rs`, `LICENSE`. GitHub Linguist label: Rust. LOC exclusions: tests/, fuzz/, examples, benches, provider test crates, documentation, generated artifacts, and package metadata.

**License:** [Apache-2.0 OR ISC OR MIT](https://github.com/rustls/rustls/blob/3925f65934364edafe8d6b20707d9e5e6183648e/LICENSE)

## SDC 5

### [rust-lang/cargo](https://github.com/rust-lang/cargo)

**S4 / D5 / C5 → SDC 5**

Rust's package manager and build orchestrator, covering manifests, workspaces, lockfiles, dependency resolution, registries and other sources, compilation units, caching, credentials, packaging, publishing, installation, and extensible commands.

**Real-world evidence:** The Rust project maintains Cargo as the package manager distributed with the Rust toolchain and as the client for crates.io and compatible registries.

**Language evidence:** Manifest and workspace modeling, dependency resolution, package sources, registries, compilation orchestration, caching, credentials, publishing, installation, tests, and the command-line application are Rust.

**Why study it:** It shows a mature developer tool coordinating dependency graphs, workspace inheritance, source identities, registry protocols, downloads and caches, authentication, rustc and rustdoc invocations, job scheduling, fingerprints, lockfiles, packaging, publishing, and compatibility.

**What you can learn:**

- Package-manager architecture, manifest and workspace models, semantic dependency resolution, feature unification, source abstractions, registries and Git, lockfiles, caches, credentials, build units and graphs, job queues, fingerprints, compiler processes, packaging, publishing, installation, and compatibility testing.

**Prerequisites:**

- Expert Rust, dependency graphs and semantic versions, package registries, Git and HTTP, filesystems and caches, process orchestration, parallel scheduling, compiler toolchains, authentication, reproducible builds, and large-codebase navigation.

**Start here:** [`src/lib.rs`](https://github.com/rust-lang/cargo/blob/e7167a4bac50fd878ce18530e901624d83be218e/src/lib.rs) — The crate-level architecture guide maps Cargo's model, source, operation, resolver, compiler, utility, and command layers before a reader follows a specific workflow.

**Why this level:**

- **S4:** 89,910 meaningful implementation LOC measured with tokei 14.0.0. Count combines the main production src tree with selected production support crates required by the shipped Cargo application.
- **D5:** Cargo must preserve dependency meaning and build reproducibility across hostile or unreliable external systems, long compatibility histories, and concurrent execution.
- **C5:** A large application coordinates numerous independently evolving subsystems and external ecosystems across the complete Rust package lifecycle.
- **Placement:** S4/D5/C5 averages to 4.67 and rounds to SDC 5; two dimensions at score 5 also require SDC 5.

**Quality-gate evidence:**

- **Source quality:** Package identities, source kinds, resolution contexts, feature sets, unit graphs, fingerprints, job states, cache locks, credentials, and process commands are explicit domain types.
- **Architecture:** Core models feed resolvers and source backends; operations build high-level workflows; the compiler layer creates units and executes jobs; commands adapt user intent; utilities isolate protocols and platform behavior.
- **Naming and idiom:** Workspace, Package, PackageId, SourceId, Resolve, CliFeatures, PackageSet, Unit, BuildRunner, Fingerprint, Compilation, Registry, and GlobalContext form a coherent package-manager vocabulary.
- **Tests:** A large in-process testsuite, resolver suites, source and registry fixtures, unit tests, snapshots, shell completion checks, and compatibility cases cover commands, failures, networks, caches, manifests, lockfiles, features, workspaces, builds, publishing, and installation.
- **Documentation:** The repository includes architecture documentation, the Cargo Book sources, command references, contributor guidance, schema and format explanations, changelogs, and extensive module comments.
- **Traceability:** A manifest dependency can be followed through workspace loading, resolver activation, source querying and download, unit-graph construction, fingerprinting, rustc execution, artifacts, lockfile updates, and a command-level fixture.
- **Maintainability:** Layered modules, stable domain identities, explicit context objects, feature gates, compatibility tests, injectable registries and processes, and detailed diagnostics constrain a sprawling tool.
- **Educational value:** It is a complete advanced study of how a language ecosystem turns declarative package intent into reproducible local builds and published artifacts.

**Inspection record:** commit `e7167a4bac50fd878ce18530e901624d83be218e`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Cargo.toml`, `src/lib.rs`, `src/resolver/mod.rs`, `src/workspace/package.rs`, `src/sources/registry/mod.rs`, `src/ops/cargo_compile/mod.rs`, `src/compiler/build_runner/mod.rs`, `LICENSE-APACHE`. GitHub Linguist label: Rust. LOC exclusions: tests/, examples, benchmarks, test-support crates, macro and resolver-test crates, maintainer tools, static assets, documentation, generated files, and package metadata.

**License:** [MIT OR Apache-2.0](https://github.com/rust-lang/cargo/blob/e7167a4bac50fd878ce18530e901624d83be218e/LICENSE-APACHE)

### [tokio-rs/tokio](https://github.com/tokio-rs/tokio)

**S4 / D5 / C5 → SDC 5**

An asynchronous runtime platform for Rust with multi-thread and current-thread schedulers, task lifecycles, OS-backed I/O, timers, networking, synchronization, processes, signals, files, macros, streams, and utilities.

**Real-world evidence:** The Tokio project maintains and publishes the runtime and companion crates as infrastructure for asynchronous Rust applications and libraries.

**Language evidence:** The asynchronous runtime, task scheduler and harness, OS I/O driver, timers, synchronization channels, networking, processes, signals, filesystem adapters, macros, utilities, model tests, and integration suites are Rust.

**Why study it:** It connects Future polling to atomic task state, wakers, work-stealing workers, cooperative budgets, reactor readiness, timers, cancellation and backpressure, networking, process and signal integration, feature gating, deterministic tests, and concurrency models.

**What you can learn:**

- Async runtime architecture, Future polling and wakers, atomic task state, cooperative scheduling, work stealing, local and multi-thread runtimes, OS readiness drivers, timers and wheels, channels and backpressure, cancellation safety, networking, processes, signals, blocking work, macros, loom model checking, and feature design.

**Prerequisites:**

- Expert Rust ownership, pinning and unsafe contracts, Future, Waker and async, atomics and memory ordering, concurrent queues, operating-system I/O readiness, timers, sockets and processes, cancellation, model checking, and performance engineering.

**Start here:** [`tokio/src/runtime/mod.rs`](https://github.com/tokio-rs/tokio/blob/ea91b33ca57ff0581b38e735cc108f831bccbdaa/tokio/src/runtime/mod.rs) — The runtime module maps builders, handles, schedulers, drivers, tasks, blocking pools, metrics, and context before deeper scheduler or reactor study.

**Why this level:**

- **S4:** 55,880 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production Rust across the shipped Tokio runtime and companion production crates, excluding dedicated testing infrastructure.
- **D5:** Soundness and liveness depend on memory ordering, pinning, wakeup, queue, driver, and cancellation invariants under arbitrary concurrency.
- **C5:** Many foundational runtime components cooperate across operating systems and concurrency models while serving a broad downstream ecosystem.
- **Placement:** S4/D5/C5 averages to 4.67 and rounds to SDC 5; two dimensions at score 5 also require SDC 5.

**Quality-gate evidence:**

- **Source quality:** Task states, ownership transitions, queue choices, wakeups, budgets, readiness tokens, timer entries, channel permits, cancellation branches, and platform conditions are encoded in focused types and comments.
- **Architecture:** The runtime composes schedulers, task harnesses, context, I/O and time drivers, blocking pools, and metrics; public sync, net, process, signal, fs, time, task, macro, stream, and utility crates layer over it.
- **Naming and idiom:** Runtime, Builder, Handle, Core, Worker, OwnedTasks, Harness, Notified, Driver, Registration, Sleep, Permit, Sender, Receiver, coop, and blocking define operational roles.
- **Tests:** Unit, integration, runtime, network, timer, synchronization, cancellation, feature, platform, compile, stress, benchmark, and loom model tests exercise behavior from APIs down to atomic interleavings.
- **Documentation:** The README, security policy, crate and module documentation, tutorial links, examples, API comments, feature tables, metrics guidance, and contribution material explain both use and internal contracts.
- **Traceability:** A spawned future can be followed into task allocation and state, a worker queue and poll, I/O or timer registration, wakeup, rescheduling, completion or cancellation, and deterministic or loom assertions.
- **Maintainability:** Subsystem boundaries, feature gates, platform adapters, model tests, loom-specific paths, metrics, explicit safety comments, and extensive regression suites contain runtime risk.
- **Educational value:** It is a capstone for understanding how Rust's async surface rests on a full concurrent runtime, operating-system integration, and carefully proved unsafe foundations.

**Inspection record:** commit `ea91b33ca57ff0581b38e735cc108f831bccbdaa`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `SECURITY.md`, `tokio/Cargo.toml`, `tokio/src/lib.rs`, `tokio/src/runtime/mod.rs`, `tokio/src/runtime/scheduler/multi_thread/worker.rs`, `tokio/src/runtime/task/harness.rs`, `tokio/src/runtime/io/driver.rs`, `tokio/src/runtime/time/mod.rs`, `tokio/src/sync/mpsc/mod.rs`, `LICENSE`. GitHub Linguist label: Rust. LOC exclusions: tokio-test/, tests/, examples/, stress/, benchmarks, integration and build-test harnesses, documentation, generated files, and package metadata.

**License:** [MIT](https://github.com/tokio-rs/tokio/blob/ea91b33ca57ff0581b38e735cc108f831bccbdaa/LICENSE)

_Generated from `catalog/rust.json`; do not edit by hand._

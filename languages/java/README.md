# Java

8 qualified repositories. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

[← All languages](../README.md)

## Level 1

No qualified repository has been published at this level. Standards are not lowered to fill a slot.

## Level 2

### [FasterXML/jackson-annotations](https://github.com/FasterXML/jackson-annotations)

**Language 3 / Behavior 2 / Design 1 / Constraints 3 → Level 2**

The standalone annotation contract used to configure Jackson serialization, deserialization, polymorphism, creators, and property handling.

**Real-world evidence:** FasterXML releases this artifact as a core dependency of the production Jackson data-processing ecosystem.

**Language evidence:** The published annotation types, value objects, and metadata contracts under src/main/java are Java.

**Why study it:** JsonTypeInfo is a compact study of how a public runtime annotation and an immutable programmatic Value object preserve the same polymorphic-serialization contract across reflection and framework configuration.

**What you can learn:**

- Use `src/main/java/com/fasterxml/jackson/annotation/JsonTypeInfo.java` to study the following transferable techniques and behaviors: Runtime annotation design, nested policy enums, generic annotation-value contracts, immutable copy-with APIs, default normalization, feature precedence, equality, hashing, Java serialization, and compatibility discipline.

**Prerequisites:**

- Before reading `src/main/java/com/fasterxml/jackson/annotation/JsonTypeInfo.java`, be familiar with the following concepts: Java annotations, enums, interfaces, immutable value objects, equality and hashing, reflection, Java serialization, and basic polymorphic-serialization concepts.

**Coding relevance:**

The short annotation and serialization context is documented in the source; the path teaches transferable annotation API design, immutable configuration values, normalization, compatibility, and reflection-based testing.

Required domain context:

- Jackson annotations attach serialization and polymorphic-type configuration to Java program elements for a separate data-binding implementation to consume.

**Learning path:**

- **Goal:** Understand how JsonTypeInfo exposes polymorphic serialization metadata and mirrors it in an immutable normalized Value object suitable for framework configuration and compatibility.
- **Start here:** [`src/main/java/com/fasterxml/jackson/annotation/JsonTypeInfo.java`](https://github.com/FasterXML/jackson-annotations/blob/474f7c9449f0efc6bf2200aac7ea4c348b429536/src/main/java/com/fasterxml/jackson/annotation/JsonTypeInfo.java) — JsonTypeInfo.java defines both the annotation users write and the normalized Value representation frameworks consume, so one file introduces the complete selected contract and its compatibility surface.
- **Then read:**
  - [`src/main/java/com/fasterxml/jackson/annotation/JacksonAnnotation.java`](https://github.com/FasterXML/jackson-annotations/blob/474f7c9449f0efc6bf2200aac7ea4c348b429536/src/main/java/com/fasterxml/jackson/annotation/JacksonAnnotation.java)
  - [`src/main/java/com/fasterxml/jackson/annotation/JacksonAnnotationValue.java`](https://github.com/FasterXML/jackson-annotations/blob/474f7c9449f0efc6bf2200aac7ea4c348b429536/src/main/java/com/fasterxml/jackson/annotation/JacksonAnnotationValue.java)
  - [`src/main/java/com/fasterxml/jackson/annotation/OptBoolean.java`](https://github.com/FasterXML/jackson-annotations/blob/474f7c9449f0efc6bf2200aac7ea4c348b429536/src/main/java/com/fasterxml/jackson/annotation/OptBoolean.java)
  - [`src/test/java/com/fasterxml/jackson/annotation/JsonTypeInfoTest.java`](https://github.com/FasterXML/jackson-annotations/blob/474f7c9449f0efc6bf2200aac7ea4c348b429536/src/test/java/com/fasterxml/jackson/annotation/JsonTypeInfoTest.java)
- **Trace:** Read the runtime annotation contract and its Id, As, and None types, then follow JsonTypeInfo.Value construction, default normalization, copy-with methods, feature merging, equality, hashing, and serialization; correlate reflected annotation defaults, immutable mutations, equality, and JDK serialization in JsonTypeInfoTest.

**Why this level:**

- **Language technique 3:** Annotations and nontrivial type modeling materially shape the component, satisfying substantial abstraction without recurring advanced machinery.
- **Behavioral reasoning 2:** Branches and configuration state matter, but the behavior remains synchronous, local, and easy to enumerate.
- **Design span 1:** The selected behavior stays within one cohesive API unit despite its rich contract.
- **Constraint burden 3:** Public compatibility, reflection-visible defaults, serialization, and safe polymorphic configuration impose several material guarantees.
- **Placement:** The four scores 3/2/1/3 sum to 9; their arithmetic mean is 2.25 and rounds half-up to Level 2. The published result is Level 2.

**Quality-gate evidence:**

- **Source quality:** The annotation contract, nested Id and As policies, defaults, immutable Value construction, normalization, and copy-with methods are explicit and unusually well documented.
- **Architecture:** One cohesive annotation and Value component uses small marker and value interfaces plus OptBoolean rather than spreading behavior across a larger data-binding implementation.
- **Naming and idiom:** JsonTypeInfo, Id, As, None, Value, withIdType, withInclusionType, and feature flags preserve the vocabulary of polymorphic metadata.
- **Tests:** JsonTypeInfoTest checks reflected defaults, normalization, immutable mutations, equality, hashing, feature behavior, and JDK serialization for the selected component.
- **Documentation:** Detailed Javadocs explain inclusion modes, identifiers, defaults, compatibility, security considerations, and how the immutable Value mirrors the annotation.
- **Traceability:** A learner can read the annotation members and enums, follow them into Value normalization and copy-with methods, then match reflection and serialization behavior to focused tests.
- **Maintainability:** A small stable contract, immutable value semantics, normalized defaults, and focused compatibility tests make changes locally reviewable despite broad downstream use.
- **Educational value:** The path shows how careful API modeling can make annotation-driven framework configuration explicit, immutable, and testable.

**Inspection record:** commit `474f7c9449f0efc6bf2200aac7ea4c348b429536`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `src/main/java/com/fasterxml/jackson/annotation/JsonTypeInfo.java`, `src/main/java/com/fasterxml/jackson/annotation/JacksonAnnotation.java`, `src/main/java/com/fasterxml/jackson/annotation/JacksonAnnotationValue.java`, `src/main/java/com/fasterxml/jackson/annotation/OptBoolean.java`, `src/test/java/com/fasterxml/jackson/annotation/JsonTypeInfoTest.java`, `LICENSE`. GitHub Linguist label: Java.

**License:** Apache-2.0 ([evidence 1](https://github.com/FasterXML/jackson-annotations/blob/474f7c9449f0efc6bf2200aac7ea4c348b429536/LICENSE))

### [ralfstx/minimal-json](https://github.com/ralfstx/minimal-json)

**Language 2 / Behavior 2 / Design 2 / Constraints 3 → Level 2**

A dependency-free JSON parser and writer built around a compact Java value model and streaming parser.

**Real-world evidence:** The repository publishes a reusable JSON library that has served Java applications and EclipseSource products.

**Language evidence:** The parser, writer, value model, and public factory API in com.eclipsesource.json are implemented entirely in Java.

**Why study it:** The parser path shows how a small Java library turns String and Reader input into a value tree while preserving buffer boundaries, nesting limits, complete-input checks, and precise source errors.

**What you can learn:**

- Use `com.eclipsesource.json/src/main/java/com/eclipsesource/json/JsonParser.java` to study the following transferable techniques and behaviors: Recursive-descent parsing, Reader buffering, character capture across refills, handler callbacks, JSON value construction, nesting guards, complete-input validation, and line-and-column diagnostics.

**Prerequisites:**

- Before reading `com.eclipsesource.json/src/main/java/com/eclipsesource/json/JsonParser.java`, be familiar with the following concepts: Java classes and interfaces, generics, Readers, arrays and lists, callbacks, recursion, exceptions, and JSON syntax.

**Coding relevance:**

The format context is short and self-contained; the selected path primarily teaches buffered reading, recursive parsing, callbacks, state management, error reporting, and resource limits.

Required domain context:

- JSON consists of objects, arrays, strings, numbers, booleans, and null, with a small documented grammar.

**Learning path:**

- **Goal:** Understand how minimal-json turns a String or Reader into a JsonValue while preserving buffer-boundary behavior, nesting limits, and precise parse errors.
- **Start here:** [`com.eclipsesource.json/src/main/java/com/eclipsesource/json/JsonParser.java`](https://github.com/ralfstx/minimal-json/blob/c091e6985620da04d5abcd902aafb6c9583c48ea/com.eclipsesource.json/src/main/java/com/eclipsesource/json/JsonParser.java) — com.eclipsesource.json/src/main/java/com/eclipsesource/json/JsonParser.java owns character reading, token recognition, recursive container parsing, handler events, nesting checks, and error locations.
- **Then read:**
  - [`com.eclipsesource.json/src/main/java/com/eclipsesource/json/Json.java`](https://github.com/ralfstx/minimal-json/blob/c091e6985620da04d5abcd902aafb6c9583c48ea/com.eclipsesource.json/src/main/java/com/eclipsesource/json/Json.java)
  - [`com.eclipsesource.json/src/main/java/com/eclipsesource/json/JsonHandler.java`](https://github.com/ralfstx/minimal-json/blob/c091e6985620da04d5abcd902aafb6c9583c48ea/com.eclipsesource.json/src/main/java/com/eclipsesource/json/JsonHandler.java)
  - [`com.eclipsesource.json/src/test/java/com/eclipsesource/json/JsonParser_Test.java`](https://github.com/ralfstx/minimal-json/blob/c091e6985620da04d5abcd902aafb6c9583c48ea/com.eclipsesource.json/src/test/java/com/eclipsesource/json/JsonParser_Test.java)
- **Trace:** Begin with Json.parse and its DefaultHandler, follow JsonParser as it reads and captures characters across buffer fills, dispatches object, array, literal, number, and string events through JsonHandler, enforces nesting and complete-input rules, and reports line and column; correlate valid forms, malformed syntax, buffer boundaries, repeated parsing, source locations, and excessive nesting in JsonParser_Test.

**Why this level:**

- **Language technique 2:** Interfaces, callbacks, composition, and conventional Java classes shape the path without advanced language machinery.
- **Behavioral reasoning 2:** Meaningful state and branching remain localized in one parser and are straightforward to trace.
- **Design span 2:** A few explicit modules contain the complete in-process behavior.
- **Constraint burden 3:** Correctness, resource protection, streaming reliability, and exact diagnostics materially constrain parser changes.
- **Placement:** The four scores 2/2/2/3 sum to 9; their arithmetic mean is 2.25 and rounds half-up to Level 2. The published result is Level 2.

**Quality-gate evidence:**

- **Source quality:** JsonParser keeps input position, capture state, buffer refill, container recursion, and malformed-input branches explicit in one focused implementation.
- **Architecture:** Json.parse supplies the public facade and DefaultHandler, JsonParser performs syntax recognition, and JsonHandler receives typed parsing events.
- **Naming and idiom:** JsonParser, JsonHandler, readValue, readObject, readArray, readString, captureStart, captureEnd, nestingLevel, line, and column state parser intent.
- **Tests:** JsonParser_Test covers valid values, malformed syntax, incomplete input, repeated parsing, buffer refill boundaries, source positions, Unicode escapes, and excessive nesting.
- **Documentation:** Public API and parser Javadocs document accepted input forms, Reader use, exceptions, and the handler boundary exercised by the selected path.
- **Traceability:** A Json.parse call can be followed into JsonParser character reads and captures, through JsonHandler events and DefaultHandler construction, then matched to exact parser tests.
- **Maintainability:** A compact parser-handler seam, explicit position state, and exhaustive syntax and boundary tests make changes locally reviewable.
- **Educational value:** The path provides a complete production parser whose streaming, recursion, resource guard, and diagnostic contracts fit within a small reading scope.

**Inspection record:** commit `c091e6985620da04d5abcd902aafb6c9583c48ea`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `com.eclipsesource.json/src/main/java/com/eclipsesource/json/JsonParser.java`, `com.eclipsesource.json/src/main/java/com/eclipsesource/json/Json.java`, `com.eclipsesource.json/src/main/java/com/eclipsesource/json/JsonHandler.java`, `com.eclipsesource.json/src/test/java/com/eclipsesource/json/JsonParser_Test.java`, `LICENSE`. GitHub Linguist label: Java.

**License:** MIT ([evidence 1](https://github.com/ralfstx/minimal-json/blob/c091e6985620da04d5abcd902aafb6c9583c48ea/LICENSE))

## Level 3

### [java-diff-utils/java-diff-utils](https://github.com/java-diff-utils/java-diff-utils)

**Language 3 / Behavior 2 / Design 2 / Constraints 3 → Level 3**

A library for computing sequence differences, applying and restoring patches, parsing unified diffs, and producing comparison output.

**Real-world evidence:** The project publishes reusable Maven artifacts used by applications that compare text and other ordered data.

**Language evidence:** Diff algorithms, deltas, patches, unified-diff parsing, and output helpers in the two production modules are Java.

**Why study it:** The Patch path separates reversible transformation and conflict validation from diff-generation theory, making a familiar algorithmic product readable as a typed production API.

**What you can learn:**

- Use `java-diff-utils/src/main/java/com/github/difflib/patch/Patch.java` to study the following transferable techniques and behaviors: Generic patches and chunks, polymorphic insert, delete, and change deltas, reverse-ordered mutation, input verification, conflict callbacks, inverse restoration, and serialization contracts.

**Prerequisites:**

- Before reading `java-diff-utils/src/main/java/com/github/difflib/patch/Patch.java`, be familiar with the following concepts: Java generics and collections, polymorphism, sequence mutation, equality, exceptions, serialization, and the basic meaning of insert, delete, change, and patch.

**Coding relevance:**

This compact patch model is sufficient context and avoids making Myers edit-graph theory the lesson; the selected behavior teaches transferable generics, reversible transformations, validation, conflict handling, and serialization.

Required domain context:

- A patch is an ordered collection of insert, delete, and change deltas whose source chunks must match before they can be applied or reversed.

**Learning path:**

- **Goal:** Understand how java-diff-utils validates and applies an existing generic patch, detects conflicts, and reverses the same delta sequence.
- **Start here:** [`java-diff-utils/src/main/java/com/github/difflib/patch/Patch.java`](https://github.com/java-diff-utils/java-diff-utils/blob/5e2e5b981533964aaeb19e2ba56d0f53dbd8b2dc/java-diff-utils/src/main/java/com/github/difflib/patch/Patch.java) — Patch.java owns delta ordering, applyTo, restore, conflict handling, and the public reversible-transformation contract, allowing learners to study application without first learning a diff-generation algorithm.
- **Then read:**
  - [`java-diff-utils/src/main/java/com/github/difflib/patch/AbstractDelta.java`](https://github.com/java-diff-utils/java-diff-utils/blob/5e2e5b981533964aaeb19e2ba56d0f53dbd8b2dc/java-diff-utils/src/main/java/com/github/difflib/patch/AbstractDelta.java)
  - [`java-diff-utils/src/main/java/com/github/difflib/patch/Chunk.java`](https://github.com/java-diff-utils/java-diff-utils/blob/5e2e5b981533964aaeb19e2ba56d0f53dbd8b2dc/java-diff-utils/src/main/java/com/github/difflib/patch/Chunk.java)
  - [`java-diff-utils/src/main/java/com/github/difflib/patch/ChangeDelta.java`](https://github.com/java-diff-utils/java-diff-utils/blob/5e2e5b981533964aaeb19e2ba56d0f53dbd8b2dc/java-diff-utils/src/main/java/com/github/difflib/patch/ChangeDelta.java)
  - [`java-diff-utils/src/main/java/com/github/difflib/patch/DeleteDelta.java`](https://github.com/java-diff-utils/java-diff-utils/blob/5e2e5b981533964aaeb19e2ba56d0f53dbd8b2dc/java-diff-utils/src/main/java/com/github/difflib/patch/DeleteDelta.java)
  - [`java-diff-utils/src/main/java/com/github/difflib/patch/InsertDelta.java`](https://github.com/java-diff-utils/java-diff-utils/blob/5e2e5b981533964aaeb19e2ba56d0f53dbd8b2dc/java-diff-utils/src/main/java/com/github/difflib/patch/InsertDelta.java)
  - [`java-diff-utils/src/test/java/com/github/difflib/patch/PatchWithAllDiffAlgorithmsTest.java`](https://github.com/java-diff-utils/java-diff-utils/blob/5e2e5b981533964aaeb19e2ba56d0f53dbd8b2dc/java-diff-utils/src/test/java/com/github/difflib/patch/PatchWithAllDiffAlgorithmsTest.java)
  - [`java-diff-utils/src/test/java/com/github/difflib/patch/ChunkTest.java`](https://github.com/java-diff-utils/java-diff-utils/blob/5e2e5b981533964aaeb19e2ba56d0f53dbd8b2dc/java-diff-utils/src/test/java/com/github/difflib/patch/ChunkTest.java)
- **Trace:** Follow Patch.applyTo into reverse-ordered delta iteration, AbstractDelta.verifyAndApplyTo, Chunk verification, and the concrete insert, delete, and change mutations; then follow restore through inverse delta behavior and correlate application across both bundled generators, serialization, content mismatch, position, and fuzz verification tests without studying the diff-generation algorithm itself.

**Why this level:**

- **Language technique 3:** Generics and a typed polymorphic transformation model materially shape the path.
- **Behavioral reasoning 2:** State and ordering require care but remain synchronous and locally traceable.
- **Design span 2:** A few explicit modules contain the complete application behavior.
- **Constraint burden 3:** Application, restoration, input verification, arbitrary element types, conflicts, and serialized patches impose several material guarantees.
- **Placement:** The four scores 3/2/2/3 sum to 10; their arithmetic mean is 2.50 and rounds half-up to Level 3. The published result is Level 3.

**Quality-gate evidence:**

- **Source quality:** Patch application and restoration expose delta order and conflict behavior directly, while AbstractDelta and Chunk isolate source verification and concrete mutation.
- **Architecture:** Patch orchestration, the delta hierarchy, chunk verification, conflict callbacks, and algorithm-independent tests have distinct responsibilities.
- **Naming and idiom:** Patch, AbstractDelta, ChangeDelta, DeleteDelta, InsertDelta, Chunk, applyTo, restore, and verifyAndApplyTo make the transformation model explicit.
- **Tests:** PatchWithAllDiffAlgorithmsTest and ChunkTest cover application across both generators, reversal, serialization, content mismatches, positions, fuzz tolerance, and generic values.
- **Documentation:** The README explains patch creation, application, restoration, algorithm substitution, unified forms, and conflicts sufficiently to orient the selected path.
- **Traceability:** A patch can be followed through reverse-ordered delta iteration, chunk verification, concrete sequence mutation, inverse restoration, and algorithm-independent assertions.
- **Maintainability:** Generic domain values and explicit delta and verification boundaries keep patch behavior independent from edit-path algorithms and external formats.
- **Educational value:** This path demonstrates how reversible algorithms become safe reusable libraries through typed models, validation, conflict policy, and tests.

**Inspection record:** commit `5e2e5b981533964aaeb19e2ba56d0f53dbd8b2dc`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `java-diff-utils/src/main/java/com/github/difflib/patch/Patch.java`, `java-diff-utils/src/main/java/com/github/difflib/patch/AbstractDelta.java`, `java-diff-utils/src/main/java/com/github/difflib/patch/Chunk.java`, `java-diff-utils/src/main/java/com/github/difflib/patch/ChangeDelta.java`, `java-diff-utils/src/main/java/com/github/difflib/patch/DeleteDelta.java`, `java-diff-utils/src/main/java/com/github/difflib/patch/InsertDelta.java`, `java-diff-utils/src/test/java/com/github/difflib/patch/PatchWithAllDiffAlgorithmsTest.java`, `java-diff-utils/src/test/java/com/github/difflib/patch/ChunkTest.java`, `LICENSE`. GitHub Linguist label: Java.

**License:** Apache-2.0 ([evidence 1](https://github.com/java-diff-utils/java-diff-utils/blob/5e2e5b981533964aaeb19e2ba56d0f53dbd8b2dc/LICENSE))

### [jhy/jsoup](https://github.com/jhy/jsoup)

**Language 2 / Behavior 3 / Design 3 / Constraints 4 → Level 3**

An HTML parser and manipulation library with DOM traversal, CSS selectors, fetching, sanitization, and standards-aware error recovery.

**Real-world evidence:** jsoup is released as a production HTML library used for scraping, editing, validation, and safe content cleaning.

**Language evidence:** HTML tokenization, tree building, DOM nodes, selectors, networking, cleaning, and output under src/main are Java.

**Why study it:** The Jsoup.clean path exposes a practical security boundary: parse untrusted HTML, rebuild a separate document, and admit only tags, attributes, and URL protocols allowed by an explicit policy.

**What you can learn:**

- Use `src/main/java/org/jsoup/Jsoup.java` to study the following transferable techniques and behaviors: Facade design, DOM visitor traversal, destination-stack state, safe document reconstruction, fluent policy configuration, tag and attribute checks, URL normalization, enforced attributes, immutability, and concurrency-safe policy reuse.

**Prerequisites:**

- Before reading `src/main/java/org/jsoup/Jsoup.java`, be familiar with the following concepts: Java collections and callbacks, HTML elements and attributes, DOM trees, visitor traversal, URLs and protocols, and basic cross-site-scripting risk.

**Coding relevance:**

The original HtmlTreeBuilder path fails this gate because WHATWG insertion modes, active formatting and open-element stacks, foster parenting, foreign-content rules, and quirks dominate its program logic. The replacement Jsoup.clean-to-Cleaner-to-Safelist path is a substantial documented production feature whose short HTML and XSS context remains subordinate to transferable traversal, policy, normalization, validation, and security-boundary engineering.

Required domain context:

- An HTML sanitizer parses untrusted body content, copies only allowed elements and attributes into a new document, and restricts URL-bearing attributes to configured protocols.

**Learning path:**

- **Goal:** Understand how jsoup cleans untrusted HTML by parsing a body fragment, copying only safelisted DOM nodes and attributes, normalizing URLs, and enforcing security policy without mutating the input.
- **Start here:** [`src/main/java/org/jsoup/Jsoup.java`](https://github.com/jhy/jsoup/blob/7860d088e044236e288c1f88a743b68b2a0edece/src/main/java/org/jsoup/Jsoup.java) — Jsoup.java contains the public clean overloads that define the learner-visible security promise and lead directly into Cleaner and Safelist, avoiding the rejected specification-heavy tree-builder path.
- **Then read:**
  - [`src/main/java/org/jsoup/safety/Cleaner.java`](https://github.com/jhy/jsoup/blob/7860d088e044236e288c1f88a743b68b2a0edece/src/main/java/org/jsoup/safety/Cleaner.java)
  - [`src/main/java/org/jsoup/safety/Safelist.java`](https://github.com/jhy/jsoup/blob/7860d088e044236e288c1f88a743b68b2a0edece/src/main/java/org/jsoup/safety/Safelist.java)
  - [`src/test/java/org/jsoup/safety/CleanerTest.java`](https://github.com/jhy/jsoup/blob/7860d088e044236e288c1f88a743b68b2a0edece/src/test/java/org/jsoup/safety/CleanerTest.java)
  - [`src/test/java/org/jsoup/safety/SafelistTest.java`](https://github.com/jhy/jsoup/blob/7860d088e044236e288c1f88a743b68b2a0edece/src/test/java/org/jsoup/safety/SafelistTest.java)
- **Trace:** Follow Jsoup.clean into body-fragment parsing and Cleaner.clean, then traverse the dirty DOM with CleaningVisitor as it copies safe elements, text, data, and source ranges into a fresh shell; follow Safelist tag and attribute checks, protocol validation, absolute or preserved relative URLs, and enforced attributes, then correlate XSS payloads, malformed input, pseudo-tag rules, URL normalization, nofollow, input immutability, and concurrent reuse in the safety tests.

**Why this level:**

- **Language technique 2:** The path uses common professional Java composition, callbacks, visitors, and fluent configuration without advanced language machinery.
- **Behavioral reasoning 3:** Traversal state, document reconstruction, policy decisions, URL normalization, and validation materially affect the end-to-end result.
- **Design span 3:** The behavior crosses several meaningful, locally understandable layers and interfaces.
- **Constraint burden 4:** Multiple strict security, normalization, URL, immutability, and concurrency guarantees interact across the sanitizer path.
- **Placement:** The four scores 2/3/3/4 sum to 12; their arithmetic mean is 3.00 and rounds half-up to Level 3. The published result is Level 3.

**Quality-gate evidence:**

- **Source quality:** The public clean facade, CleaningVisitor, destination stack, Safelist checks, URL normalization, and copy-into-new-document behavior expose security decisions directly.
- **Architecture:** Jsoup parsing, DOM nodes, Cleaner traversal, and Safelist policy are separated into recognizable layers with the untrusted input never reused as output.
- **Naming and idiom:** clean, Cleaner, CleaningVisitor, Safelist, isSafeTag, isSafeAttribute, protocols, enforced attributes, and preserveRelativeLinks state policy intent.
- **Tests:** CleanerTest and SafelistTest cover XSS payloads, malformed input, tag and attribute policy, pseudo-tags, protocols, relative and absolute URLs, nofollow, immutability, and concurrent reuse.
- **Documentation:** Public API documentation and explicit security warnings explain cleaning, safelists, protocol restrictions, URL handling, and the limits of the sanitizer.
- **Traceability:** An input fragment can be followed from Jsoup.clean through parsing, safe-node copying, attribute and protocol validation, normalization, and serialization into focused security tests.
- **Maintainability:** A small public facade, separate traversal and policy components, explicit normalization rules, and focused regressions localize a security-sensitive feature.
- **Educational value:** The path teaches secure transformation as an explicit parse, copy, validate, and normalize pipeline rather than as string filtering.

**Inspection record:** commit `7860d088e044236e288c1f88a743b68b2a0edece`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `src/main/java/org/jsoup/Jsoup.java`, `src/main/java/org/jsoup/safety/Cleaner.java`, `src/main/java/org/jsoup/safety/Safelist.java`, `src/test/java/org/jsoup/safety/CleanerTest.java`, `src/test/java/org/jsoup/safety/SafelistTest.java`, `LICENSE`. GitHub Linguist label: Java.

**License:** MIT ([evidence 1](https://github.com/jhy/jsoup/blob/7860d088e044236e288c1f88a743b68b2a0edece/LICENSE))

## Level 4

### [google/gson](https://github.com/google/gson)

**Language 4 / Behavior 4 / Design 3 / Constraints 4 → Level 4**

A JSON serialization library that maps Java object graphs and generic types through configurable streaming and tree adapters.

**Real-world evidence:** Google releases Gson as production serialization infrastructure consumed broadly through Maven and Android ecosystems.

**Language evidence:** The JSON model, streaming reader/writer, reflection adapters, type tokens, and serialization engine in the Gson modules are Java.

**Why study it:** The Gson adapter path shows how a serialization library resolves and caches behavior for a generic type, breaks recursive construction cycles, and falls back to reflective fields or records.

**What you can learn:**

- Use `gson/src/main/java/com/google/gson/Gson.java` to study the following transferable techniques and behaviors: Erased generic TypeToken recovery, ordered adapter factories, concurrent caching, thread-local recursion placeholders, reflective field binding, record construction, access filtering, streaming conversion, and stable errors.

**Prerequisites:**

- Before reading `gson/src/main/java/com/google/gson/Gson.java`, be familiar with the following concepts: Advanced Java generics, reflection, concurrent maps and ThreadLocal, factories and adapters, records, field access, recursive types, and JSON streaming.

**Coding relevance:**

Basic JSON and reflection context is short and documented; the path teaches transferable erased-type modeling, recursive cache construction, concurrency, factory composition, reflective access policy, streaming, and compatibility.

Required domain context:

- Gson maps Java types to JSON through an ordered chain of TypeAdapterFactory implementations, using reflective binding when no earlier adapter handles a type.

**Learning path:**

- **Goal:** Understand how Gson resolves and caches a type adapter, breaks recursive construction cycles, falls back to reflective field or record binding, and uses the result for JSON conversion.
- **Start here:** [`gson/src/main/java/com/google/gson/Gson.java`](https://github.com/google/gson/blob/b3f4ca20087f9066de4c340522ff84e0558e1ad1/gson/src/main/java/com/google/gson/Gson.java) — gson/src/main/java/com/google/gson/Gson.java owns getAdapter and the read and write facade, so it exposes cache lookup, recursive construction, ordered factory selection, and adapter use.
- **Then read:**
  - [`gson/src/main/java/com/google/gson/TypeAdapterFactory.java`](https://github.com/google/gson/blob/b3f4ca20087f9066de4c340522ff84e0558e1ad1/gson/src/main/java/com/google/gson/TypeAdapterFactory.java)
  - [`gson/src/main/java/com/google/gson/reflect/TypeToken.java`](https://github.com/google/gson/blob/b3f4ca20087f9066de4c340522ff84e0558e1ad1/gson/src/main/java/com/google/gson/reflect/TypeToken.java)
  - [`gson/src/main/java/com/google/gson/internal/bind/ReflectiveTypeAdapterFactory.java`](https://github.com/google/gson/blob/b3f4ca20087f9066de4c340522ff84e0558e1ad1/gson/src/main/java/com/google/gson/internal/bind/ReflectiveTypeAdapterFactory.java)
  - [`gson/src/test/java/com/google/gson/GsonTest.java`](https://github.com/google/gson/blob/b3f4ca20087f9066de4c340522ff84e0558e1ad1/gson/src/test/java/com/google/gson/GsonTest.java)
  - [`gson/src/test/java/com/google/gson/functional/ReflectionAccessFilterTest.java`](https://github.com/google/gson/blob/b3f4ca20087f9066de4c340522ff84e0558e1ad1/gson/src/test/java/com/google/gson/functional/ReflectionAccessFilterTest.java)
  - [`gson/src/test/java/com/google/gson/functional/Java17RecordTest.java`](https://github.com/google/gson/blob/b3f4ca20087f9066de4c340522ff84e0558e1ad1/gson/src/test/java/com/google/gson/functional/Java17RecordTest.java)
- **Trace:** Follow Gson.getAdapter from TypeToken lookup through the concurrent cache, per-thread construction map, FutureTypeAdapter recursion placeholder, and ordered factories; enter ReflectiveTypeAdapterFactory for access filtering, generic field resolution, duplicate-name rejection, bound-field adapters, and record construction, then return through streaming read or write while correlating recursion, concurrency, factory order, access, record, strictness, and error tests.

**Why this level:**

- **Language technique 4:** Reflection, advanced generic-type recovery, and implicit runtime binding recur throughout adapter resolution.
- **Behavioral reasoning 4:** Concurrency, recursion, cache publication, streaming state, and construction failures require advanced nonlocal reasoning.
- **Design span 3:** The trace crosses several meaningful, locally understandable layers and interfaces, but it does not require Gson's broader architecture.
- **Constraint burden 4:** Thread safety, reflective access, type correctness, Java compatibility, streaming modes, and stable serialized behavior interact across ordinary changes.
- **Placement:** The four scores 4/4/3/4 sum to 15; their arithmetic mean is 3.75 and rounds half-up to Level 4. The published result is Level 4.

**Quality-gate evidence:**

- **Source quality:** Gson.getAdapter makes cache hits, per-thread construction state, FutureTypeAdapter placeholders, factory order, publication, and cleanup explicit.
- **Architecture:** The Gson facade, TypeToken, TypeAdapterFactory chain, ReflectiveTypeAdapterFactory, stream adapters, and access filters have clear roles.
- **Naming and idiom:** getAdapter, TypeToken, TypeAdapterFactory, FutureTypeAdapter, threadLocalAdapterResults, ReflectiveTypeAdapterFactory, bound fields, and access filters expose the resolution model.
- **Tests:** The selected Gson, reflection-access, and Java record suites cover recursion, concurrency, factory precedence, access policy, records, strictness, compatibility, and failures.
- **Documentation:** Extensive API Javadocs describe adapter lookup, factories, generic types, reflection access, records, and streaming behavior used by this trace.
- **Traceability:** A TypeToken can be followed through cache and recursion handling, across ordered factories into reflective binding, and back through streaming read or write into focused tests.
- **Maintainability:** Explicit cache publication, factory seams, access policy, and regression coverage constrain changes across type identity, recursion, Java versions, and serialized compatibility.
- **Educational value:** The path connects Java's erased type system and reflection to a disciplined, cached runtime serialization strategy.

**Inspection record:** commit `b3f4ca20087f9066de4c340522ff84e0558e1ad1`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `gson/src/main/java/com/google/gson/Gson.java`, `gson/src/main/java/com/google/gson/TypeAdapterFactory.java`, `gson/src/main/java/com/google/gson/reflect/TypeToken.java`, `gson/src/main/java/com/google/gson/internal/bind/ReflectiveTypeAdapterFactory.java`, `gson/src/test/java/com/google/gson/GsonTest.java`, `gson/src/test/java/com/google/gson/functional/ReflectionAccessFilterTest.java`, `gson/src/test/java/com/google/gson/functional/Java17RecordTest.java`, `LICENSE`. GitHub Linguist label: Java.

**License:** Apache-2.0 ([evidence 1](https://github.com/google/gson/blob/b3f4ca20087f9066de4c340522ff84e0558e1ad1/LICENSE))

### [junit-team/junit4](https://github.com/junit-team/junit4)

**Language 4 / Behavior 4 / Design 4 / Constraints 4 → Level 4**

The fourth-generation JUnit testing framework, including reflective discovery, runners, rules, assertions, lifecycle statements, and reports.

**Real-world evidence:** JUnit 4 remains maintained production test infrastructure and a compatibility foundation across the Java ecosystem.

**Language evidence:** The test runner, descriptions, statements, rules, assertions, matchers, and extension model under src/main/java are Java.

**Why study it:** The BlockJUnit4ClassRunner path shows how JUnit 4 discovers one annotated method, composes its execution lifecycle from Statements and rules, schedules it, and reports failures safely.

**What you can learn:**

- Use `src/main/java/org/junit/runners/BlockJUnit4ClassRunner.java` to study the following transferable techniques and behaviors: Reflection and annotations, runner hierarchies, Statement decoration, expected exceptions, timeouts, before and after hooks, ordered rules, child scheduling, listener events, and failure isolation.

**Prerequisites:**

- Before reading `src/main/java/org/junit/runners/BlockJUnit4ClassRunner.java`, be familiar with the following concepts: Java reflection, annotations, inheritance and generics, decorators, exceptions, threads and timeouts, callbacks, and unit-test lifecycle concepts.

**Coding relevance:**

The familiar test-runner model is short and documented; the path's difficulty is transferable reflection, lifecycle composition, extension ordering, event propagation, isolation, and failure handling.

Required domain context:

- A JUnit 4 runner discovers annotated test methods, wraps each invocation with setup, teardown, timeout, expected-exception, and rule behavior, and reports events to listeners.

**Learning path:**

- **Goal:** Understand how JUnit 4 discovers and executes one annotated test method through its composable statement lifecycle and reports the result safely.
- **Start here:** [`src/main/java/org/junit/runners/BlockJUnit4ClassRunner.java`](https://github.com/junit-team/junit4/blob/890f3c972647de378f25e7271d8fbbd9d3456b79/src/main/java/org/junit/runners/BlockJUnit4ClassRunner.java) — BlockJUnit4ClassRunner.java connects reflective test-method discovery to methodBlock, where invocation, expected-exception, timeout, fixture, and rule Statements are assembled.
- **Then read:**
  - [`src/main/java/org/junit/runners/ParentRunner.java`](https://github.com/junit-team/junit4/blob/890f3c972647de378f25e7271d8fbbd9d3456b79/src/main/java/org/junit/runners/ParentRunner.java)
  - [`src/main/java/org/junit/runners/model/Statement.java`](https://github.com/junit-team/junit4/blob/890f3c972647de378f25e7271d8fbbd9d3456b79/src/main/java/org/junit/runners/model/Statement.java)
  - [`src/main/java/org/junit/runners/RuleContainer.java`](https://github.com/junit-team/junit4/blob/890f3c972647de378f25e7271d8fbbd9d3456b79/src/main/java/org/junit/runners/RuleContainer.java)
  - [`src/main/java/org/junit/runner/notification/RunNotifier.java`](https://github.com/junit-team/junit4/blob/890f3c972647de378f25e7271d8fbbd9d3456b79/src/main/java/org/junit/runner/notification/RunNotifier.java)
  - [`src/test/java/org/junit/tests/running/classes/BlockJUnit4ClassRunnerTest.java`](https://github.com/junit-team/junit4/blob/890f3c972647de378f25e7271d8fbbd9d3456b79/src/test/java/org/junit/tests/running/classes/BlockJUnit4ClassRunnerTest.java)
  - [`src/test/java/org/junit/tests/running/methods/ExpectedTest.java`](https://github.com/junit-team/junit4/blob/890f3c972647de378f25e7271d8fbbd9d3456b79/src/test/java/org/junit/tests/running/methods/ExpectedTest.java)
  - [`src/test/java/org/junit/tests/running/methods/TimeoutTest.java`](https://github.com/junit-team/junit4/blob/890f3c972647de378f25e7271d8fbbd9d3456b79/src/test/java/org/junit/tests/running/methods/TimeoutTest.java)
  - [`src/test/java/org/junit/runners/RuleContainerTest.java`](https://github.com/junit-team/junit4/blob/890f3c972647de378f25e7271d8fbbd9d3456b79/src/test/java/org/junit/runners/RuleContainerTest.java)
- **Trace:** Follow reflective method discovery and validation into runChild and methodBlock, then compose invocation, expected-exception, timeout, before, after, and ordered rule Statements; continue through ParentRunner scheduling and interrupt isolation into RunNotifier's failure-contained listener events, correlating runner construction, expected exceptions, timeouts, rule order, customization, and notification behavior in the focused tests.

**Why this level:**

- **Language technique 4:** Reflection, annotations, generic framework types, and implicit decorator composition recur in important behavior.
- **Behavioral reasoning 4:** Lifecycle ordering, event propagation, resource cleanup, and failure behavior require advanced nonlocal reasoning.
- **Design span 4:** Many framework modules, extension points, and cross-cutting execution policies contribute directly to one test run.
- **Constraint burden 4:** Compatibility, deterministic order, error aggregation, threading, and isolation guarantees interact throughout the path.
- **Placement:** The four scores 4/4/4/4 sum to 16; their arithmetic mean is 4.00 and rounds half-up to Level 4. The published result is Level 4.

**Quality-gate evidence:**

- **Source quality:** Runner, Statement, RuleContainer, ParentRunner, and RunNotifier responsibilities are explicit, with lifecycle order documented beside composition points.
- **Architecture:** BlockJUnit4ClassRunner builds method execution, ParentRunner schedules children, RuleContainer orders extensions, Statement represents each layer, and RunNotifier contains listener failures.
- **Naming and idiom:** runChild, methodBlock, methodInvoker, possiblyExpectingExceptions, withPotentialTimeout, withBefores, withAfters, withRules, and fireTestFailure expose execution order.
- **Tests:** The selected runner, expected-exception, timeout, and rule-container suites cover discovery, validation, statement order, customization, errors, interruption, and notification behavior.
- **Documentation:** Source Javadocs and JUnit 4 runner and rule documentation explain the composable lifecycle and extension contracts followed here.
- **Traceability:** An annotated method can be followed through reflective discovery, methodBlock's nested Statements, ParentRunner scheduling, and RunNotifier events into focused lifecycle tests.
- **Maintainability:** Small lifecycle decorators, explicit extension points, stable event boundaries, and ordering tests protect a mature compatibility-sensitive framework.
- **Educational value:** The path demonstrates how a test framework represents execution policy as composable objects while preserving deterministic cleanup and reporting.

**Inspection record:** commit `890f3c972647de378f25e7271d8fbbd9d3456b79`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `src/main/java/org/junit/runners/BlockJUnit4ClassRunner.java`, `src/main/java/org/junit/runners/ParentRunner.java`, `src/main/java/org/junit/runners/model/Statement.java`, `src/main/java/org/junit/runners/RuleContainer.java`, `src/main/java/org/junit/runner/notification/RunNotifier.java`, `src/test/java/org/junit/tests/running/classes/BlockJUnit4ClassRunnerTest.java`, `src/test/java/org/junit/tests/running/methods/ExpectedTest.java`, `src/test/java/org/junit/tests/running/methods/TimeoutTest.java`, `src/test/java/org/junit/runners/RuleContainerTest.java`, `LICENSE-junit.txt`. GitHub Linguist label: Java.

**License:** EPL-1.0 ([evidence 1](https://github.com/junit-team/junit4/blob/890f3c972647de378f25e7271d8fbbd9d3456b79/LICENSE-junit.txt))

## Level 5

### [jenkinsci/jenkins](https://github.com/jenkinsci/jenkins)

**Language 4 / Behavior 5 / Design 5 / Constraints 5 → Level 5**

The Jenkins automation server core, including its persistent task queue, extension-driven eligibility policy, executor placement, work handoff, and completion lifecycle.

**Real-world evidence:** Jenkins publishes weekly and long-term-support automation-server releases used to build, test, analyze, and deploy production software.

**Language evidence:** The queue, placement, work-unit, executor, extension, persistence, and integration-test implementation in the selected path is first-party Java.

**Why study it:** The queue-to-executor path exposes how a mature extensible platform coordinates persistent scheduling state, resource assignment, concurrent execution, failure recovery, and compatibility without hiding the difficult invariants.

**What you can learn:**

- Use `core/src/main/java/hudson/model/Queue.java` to study transferable task-state machines, concurrency control, extension policy, constrained resource assignment, multi-unit work handoff, persistence recovery, listener isolation, and completion guarantees.

**Prerequisites:**

- Before reading `core/src/main/java/hudson/model/Queue.java`, be comfortable with Java generics, nested classes, annotations, locks, threads, futures, callbacks, serialization, and the short Jenkins vocabulary of tasks, agents or nodes, labels, and executors.

**Coding relevance:**

That vocabulary is short and documented in the selected source; the path's difficulty comes from transferable scheduling, concurrent state, resource assignment, extension policy, recovery, and lifecycle engineering rather than a specialist external discipline.

Required domain context:

- Jenkins queues tasks, assigns their subtasks to eligible executors on agents or the built-in node, and exposes extension points that may veto execution or placement.

**Learning path:**

- **Goal:** Understand how Jenkins accepts a task, moves it through waiting, blocked, buildable, and pending states, assigns its work to eligible executors, runs it, and resolves completion or recovery paths.
- **Start here:** [`core/src/main/java/hudson/model/Queue.java`](https://github.com/jenkinsci/jenkins/blob/982bc91d866ed90aa135b87a2cb4ac1e68c2412e/core/src/main/java/hudson/model/Queue.java) — Queue.schedule2 and Queue.maintain define the central state transitions, extension vetoes, executor offers, placement call, pending handoff, persistence, and lost-executor recovery that organize the complete trace.
- **Then read:**
  - [`core/src/main/java/hudson/model/queue/QueueTaskDispatcher.java`](https://github.com/jenkinsci/jenkins/blob/982bc91d866ed90aa135b87a2cb4ac1e68c2412e/core/src/main/java/hudson/model/queue/QueueTaskDispatcher.java)
  - [`core/src/main/java/hudson/model/queue/MappingWorksheet.java`](https://github.com/jenkinsci/jenkins/blob/982bc91d866ed90aa135b87a2cb4ac1e68c2412e/core/src/main/java/hudson/model/queue/MappingWorksheet.java)
  - [`core/src/main/java/hudson/model/LoadBalancer.java`](https://github.com/jenkinsci/jenkins/blob/982bc91d866ed90aa135b87a2cb4ac1e68c2412e/core/src/main/java/hudson/model/LoadBalancer.java)
  - [`core/src/main/java/hudson/model/queue/WorkUnitContext.java`](https://github.com/jenkinsci/jenkins/blob/982bc91d866ed90aa135b87a2cb4ac1e68c2412e/core/src/main/java/hudson/model/queue/WorkUnitContext.java)
  - [`core/src/main/java/hudson/model/queue/WorkUnit.java`](https://github.com/jenkinsci/jenkins/blob/982bc91d866ed90aa135b87a2cb4ac1e68c2412e/core/src/main/java/hudson/model/queue/WorkUnit.java)
  - [`core/src/main/java/hudson/model/Executor.java`](https://github.com/jenkinsci/jenkins/blob/982bc91d866ed90aa135b87a2cb4ac1e68c2412e/core/src/main/java/hudson/model/Executor.java)
  - [`test/src/test/java/hudson/model/QueueTest.java`](https://github.com/jenkinsci/jenkins/blob/982bc91d866ed90aa135b87a2cb4ac1e68c2412e/test/src/test/java/hudson/model/QueueTest.java)
  - [`test/src/test/java/hudson/model/queue/QueueTaskDispatcherTest.java`](https://github.com/jenkinsci/jenkins/blob/982bc91d866ed90aa135b87a2cb4ac1e68c2412e/test/src/test/java/hudson/model/queue/QueueTaskDispatcherTest.java)
  - [`test/src/test/java/hudson/model/ExecutorTest.java`](https://github.com/jenkinsci/jenkins/blob/982bc91d866ed90aa135b87a2cb4ac1e68c2412e/test/src/test/java/hudson/model/ExecutorTest.java)
- **Trace:** Begin at schedule2, decision extensions, duplicate folding, and WaitingItem creation; follow maintain through blocked and buildable transitions, lost-pending recovery, QueueTaskDispatcher eligibility, MappingWorksheet constraints, and LoadBalancer's consistent-hash greedy mapping; continue through WorkUnitContext and WorkUnit assignment into Executor.run, node revalidation, pending-to-left transition, executable creation, synchronized start and finish, future and listener completion, executor release, and renewed maintenance.

**Why this level:**

- **Language technique 4:** Advanced Java annotations, extension discovery, reflective persistence, generics, nested polymorphic states, locks, latches, and futures recur materially, but do not require expert command of several interacting language mechanisms everywhere.
- **Behavioral reasoning 5:** Concurrent state, plugin vetoes, assignment, executor churn, multi-unit barriers, asynchronous completion, persistence, and recovery interact pervasively and require unavoidable nonlocal reasoning.
- **Design span 5:** The selected behavior coordinates several major platform subsystems and pervasive extension and lifecycle boundaries rather than a bounded group of ordinary modules.
- **Constraint burden 5:** Thread safety, resource policy, permission checks, extension compatibility, fault isolation, executor churn, persistence normalization, and completion guarantees interact so a local scheduling change can violate system-wide correctness.
- **Placement:** The four scores 4/5/5/5 sum to 19; their arithmetic mean is 4.75 and rounds half-up to Level 5. Three dimensions score 5, satisfying the Level 5 guardrail.

**Quality-gate evidence:**

- **Source quality:** Queue's central maintain method is large, but its explicit state collections, lock boundaries, transition comments, snapshots, and recovery branches make its demanding invariants intentional and readable.
- **Architecture:** Queue, QueueTaskDispatcher, MappingWorksheet, LoadBalancer, WorkUnitContext, WorkUnit, and Executor separate state, policy, placement, handoff, synchronization, and execution responsibilities.
- **Naming and idiom:** WaitingItem, BlockedItem, BuildableItem, pending, JobOffer, MappingWorksheet, WorkUnitContext, synchronizeStart, and synchronizeEnd expose the scheduling lifecycle precisely.
- **Tests:** Enabled tests exercise blockage, permissions, pending-loss recovery, assignment policy, save and load recovery, executor failure, start, and completion; the two dedicated restart tests are disabled for flakiness and are not claimed as protection.
- **Documentation:** The README establishes the production platform and extensive source Javadocs document queue states, extension contracts, mapping, handoff, persistence normalization, and executor lifecycle.
- **Traceability:** The complete implementation-to-result path is observable across focused queue, dispatcher, and executor integration tests, although its evidence is necessarily distributed and does not isolate every mapping or multi-unit-latch branch.
- **Maintainability:** Explicit locking, immutable snapshots, compatibility converters, plugin exception containment, recovery paths, and regression tests constrain changes to the mature scheduler.
- **Educational value:** The path is a rare source-closed study of platform-scale scheduling and concurrency; it does not promise globally optimal placement or exactly-once execution across process crashes.

**Inspection record:** commit `982bc91d866ed90aa135b87a2cb4ac1e68c2412e`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `core/src/main/java/hudson/model/Queue.java`, `core/src/main/java/hudson/model/queue/QueueTaskDispatcher.java`, `core/src/main/java/hudson/model/queue/MappingWorksheet.java`, `core/src/main/java/hudson/model/LoadBalancer.java`, `core/src/main/java/hudson/model/queue/WorkUnitContext.java`, `core/src/main/java/hudson/model/queue/WorkUnit.java`, `core/src/main/java/hudson/model/Executor.java`, `test/src/test/java/hudson/model/QueueTest.java`, `test/src/test/java/hudson/model/queue/QueueTaskDispatcherTest.java`, `test/src/test/java/hudson/model/ExecutorTest.java`, `test/src/test/java/hudson/model/QueueRestartTest.java`, `README.md`, `pom.xml`, `LICENSE.txt`. GitHub Linguist label: Java.

**License:** MIT ([evidence 1](https://github.com/jenkinsci/jenkins/blob/982bc91d866ed90aa135b87a2cb4ac1e68c2412e/LICENSE.txt))

### [spring-projects/spring-framework](https://github.com/spring-projects/spring-framework)

**Language 5 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

A comprehensive application framework spanning dependency injection, AOP, transactions, data access, messaging, web stacks, and testing.

**Real-world evidence:** Spring Framework is actively released production infrastructure underlying a large portion of the enterprise Java ecosystem.

**Language evidence:** Core containers, reflection and type systems, AOP, transactions, data access, messaging, MVC, reactive web, and testing support are primarily Java.

**Why study it:** The bean-factory path exposes how Spring resolves typed and qualified dependencies, constructs and post-processes one singleton, and preserves identity through concurrency and circular references.

**What you can learn:**

- Use `spring-beans/src/main/java/org/springframework/beans/factory/support/DefaultListableBeanFactory.java` to study the following transferable techniques and behaviors: Bean-definition registration, generic ResolvableType matching, DependencyDescriptor policy, qualifiers and priorities, constructor selection, reflective instantiation, post-processors, singleton caches, circular references, locking, initialization, and destruction.

**Prerequisites:**

- Before reading `spring-beans/src/main/java/org/springframework/beans/factory/support/DefaultListableBeanFactory.java`, be familiar with the following concepts: Expert Java generics and reflection, annotations, dependency injection, factories, proxies and providers, concurrent caches, object lifecycles, and extension callbacks.

**Coding relevance:**

Dependency injection and object lifecycle are documented programming-framework concepts; the selected path's difficulty is transferable reflection, generic type resolution, extension policy, concurrent lifecycle management, caching, compatibility, and error handling.

Required domain context:

- A Spring bean factory stores object definitions, resolves dependencies by type and metadata, constructs and post-processes objects, manages singleton identity and circular references, and runs initialization callbacks.

**Learning path:**

- **Goal:** Understand how Spring registers a bean definition, resolves generic and qualified dependencies, constructs and post-processes one singleton, handles circular or concurrent creation, and completes initialization.
- **Start here:** [`spring-beans/src/main/java/org/springframework/beans/factory/support/DefaultListableBeanFactory.java`](https://github.com/spring-projects/spring-framework/blob/1b56f58999046051d76a653922c3ab72b4db9cf7/spring-beans/src/main/java/org/springframework/beans/factory/support/DefaultListableBeanFactory.java) — DefaultListableBeanFactory.java owns bean-definition registration and dependency selection, providing the entrance to constructor resolution, creation callbacks, and singleton-registry coordination.
- **Then read:**
  - [`spring-beans/src/main/java/org/springframework/beans/factory/config/DependencyDescriptor.java`](https://github.com/spring-projects/spring-framework/blob/1b56f58999046051d76a653922c3ab72b4db9cf7/spring-beans/src/main/java/org/springframework/beans/factory/config/DependencyDescriptor.java)
  - [`spring-beans/src/main/java/org/springframework/beans/factory/support/AbstractAutowireCapableBeanFactory.java`](https://github.com/spring-projects/spring-framework/blob/1b56f58999046051d76a653922c3ab72b4db9cf7/spring-beans/src/main/java/org/springframework/beans/factory/support/AbstractAutowireCapableBeanFactory.java)
  - [`spring-beans/src/main/java/org/springframework/beans/factory/support/ConstructorResolver.java`](https://github.com/spring-projects/spring-framework/blob/1b56f58999046051d76a653922c3ab72b4db9cf7/spring-beans/src/main/java/org/springframework/beans/factory/support/ConstructorResolver.java)
  - [`spring-beans/src/main/java/org/springframework/beans/factory/support/DefaultSingletonBeanRegistry.java`](https://github.com/spring-projects/spring-framework/blob/1b56f58999046051d76a653922c3ab72b4db9cf7/spring-beans/src/main/java/org/springframework/beans/factory/support/DefaultSingletonBeanRegistry.java)
  - [`spring-core/src/main/java/org/springframework/core/ResolvableType.java`](https://github.com/spring-projects/spring-framework/blob/1b56f58999046051d76a653922c3ab72b4db9cf7/spring-core/src/main/java/org/springframework/core/ResolvableType.java)
  - [`spring-beans/src/test/java/org/springframework/beans/factory/DefaultListableBeanFactoryTests.java`](https://github.com/spring-projects/spring-framework/blob/1b56f58999046051d76a653922c3ab72b4db9cf7/spring-beans/src/test/java/org/springframework/beans/factory/DefaultListableBeanFactoryTests.java)
  - [`spring-beans/src/test/java/org/springframework/beans/factory/support/DefaultSingletonBeanRegistryTests.java`](https://github.com/spring-projects/spring-framework/blob/1b56f58999046051d76a653922c3ab72b4db9cf7/spring-beans/src/test/java/org/springframework/beans/factory/support/DefaultSingletonBeanRegistryTests.java)
- **Trace:** Follow bean-definition registration and singleton pre-instantiation into dependency resolution, where DependencyDescriptor and ResolvableType drive optional, provider, lazy, collection, map, qualifier, name, primary, priority, and fallback matching; continue through AbstractAutowireCapableBeanFactory and ConstructorResolver into instantiation, property population, post-processors, and initialization, with DefaultSingletonBeanRegistry coordinating cache publication, circular references, locking, destruction, and failures; correlate matching, construction, lifecycle, concurrency, and registry tests.

**Why this level:**

- **Language technique 5:** Multiple advanced Java mechanisms interact pervasively across dependency discovery, construction, and lifecycle policy.
- **Behavioral reasoning 5:** Concurrency, cache state, cycles, dynamic resolution, extension callbacks, recovery, and resource lifecycles interact pervasively.
- **Design span 4:** Many container modules and pervasive extension policies contribute directly, satisfying broad architecture without requiring the entire Spring platform.
- **Constraint burden 5:** Several system-wide type, lifecycle, concurrency, extension, AOT, and compatibility guarantees interact so local changes can break applications elsewhere.
- **Placement:** The four scores 5/5/4/5 sum to 19; their arithmetic mean is 4.75 and rounds half-up to Level 5. The published result is Level 5.

**Quality-gate evidence:**

- **Source quality:** Bean definitions, dependency descriptors, type resolution, candidate selection, construction, lifecycle callbacks, and singleton states use explicit types and detailed contract comments.
- **Architecture:** DefaultListableBeanFactory, DependencyDescriptor, ResolvableType, ConstructorResolver, AbstractAutowireCapableBeanFactory, and DefaultSingletonBeanRegistry separate selection, construction, and identity.
- **Naming and idiom:** resolveDependency, DependencyDescriptor, ResolvableType, autowireCandidate, ConstructorResolver, createBean, earlySingletonObjects, and singletonFactories preserve container vocabulary.
- **Tests:** The selected bean-factory and singleton-registry suites cover generic and qualified matching, construction, lifecycle callbacks, circular references, concurrency, failures, and destruction.
- **Documentation:** Spring's bean-container reference and extensive source Javadocs document dependency resolution, scopes, lifecycle callbacks, post-processors, and circular references used here.
- **Traceability:** A registered definition can be followed through candidate matching and generic type resolution, constructor selection, instantiation and post-processing, then singleton cache publication and lifecycle tests.
- **Maintainability:** Strongly named container layers, explicit extension contracts, synchronized singleton state, and mature compatibility tests constrain changes to shared application infrastructure.
- **Educational value:** The path offers an expert study of how reflection-heavy dependency injection becomes a deterministic type, lifecycle, concurrency, and extension system.

**Inspection record:** commit `1b56f58999046051d76a653922c3ab72b4db9cf7`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `spring-beans/src/main/java/org/springframework/beans/factory/support/DefaultListableBeanFactory.java`, `spring-beans/src/main/java/org/springframework/beans/factory/config/DependencyDescriptor.java`, `spring-beans/src/main/java/org/springframework/beans/factory/support/AbstractAutowireCapableBeanFactory.java`, `spring-beans/src/main/java/org/springframework/beans/factory/support/ConstructorResolver.java`, `spring-beans/src/main/java/org/springframework/beans/factory/support/DefaultSingletonBeanRegistry.java`, `spring-core/src/main/java/org/springframework/core/ResolvableType.java`, `spring-beans/src/test/java/org/springframework/beans/factory/DefaultListableBeanFactoryTests.java`, `spring-beans/src/test/java/org/springframework/beans/factory/support/DefaultSingletonBeanRegistryTests.java`, `LICENSE.txt`. GitHub Linguist label: Java.

**License:** Apache-2.0 ([evidence 1](https://github.com/spring-projects/spring-framework/blob/1b56f58999046051d76a653922c3ab72b4db9cf7/LICENSE.txt))

_Generated from `catalog/java.json`; do not edit by hand._

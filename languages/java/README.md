# Java

7 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

**Source legend:** Production software is built primarily for real users or systems. Educational exemplars are complete teaching-oriented software and may appear only at Levels 1 and 2.

[← All languages](../README.md)

## Level 1 — First real code

No qualified learning path has been published at this level. An empty Level 1 means Exempla has not yet found a path gentle enough to publish here; learners are not being told to jump to Level 2.

## Level 2 — Guided real-world patterns

### [junit-team/junit-examples](https://github.com/junit-team/junit-examples)

**Language 3 / Behavior 1 / Design 2 / Constraints 2 → Level 2**

**Source:** Educational exemplar

JUnit's complete Gradle starter pairs a tiny Java class with one example test and one table-driven parameterized test.

**Why study it:** See how a finished small Java project turns examples and a table of inputs into repeatable tests with descriptive failure messages.

Levels 1–2 may use intentionally instructive software when it provides a gentler path into reading good source code.

**Prerequisites:**

- The global novice Java baseline: classes, methods, integers, imports, and focused tests.
- A test annotation marks a method for the test runner; a parameterized test repeats one method with each declared data row.

**Concepts this path develops:**

- Organizing production and test source into explicit project roles.
- Expressing one behavior with both example-based and table-driven tests.
- Configuring a build tool to discover tests through the JUnit Platform.

**What you can learn:**

- Separate the class being checked from its test class and test-only dependencies.
- Compare one ordinary test with a parameterized test driven by CSV rows.
- Connect Gradle's JUnit Platform configuration to the annotations that discover and run tests.

**Learning path:**

- **Goal:** Understand how JUnit's complete Gradle starter discovers and runs ordinary and parameterized tests against a small Java class.
- **Start here:** [`junit-jupiter-starter-gradle/src/main/java/com/example/project/Calculator.java`](https://github.com/junit-team/junit-examples/blob/02dedb783f4f98c4d6b5bd53ae96bf8986eeebf7/junit-jupiter-starter-gradle/src/main/java/com/example/project/Calculator.java) — The single public add behavior provides the exact contract that every selected test exercises.
- **Then read:**
  - [`junit-jupiter-starter-gradle/src/test/java/com/example/project/CalculatorTests.java`](https://github.com/junit-team/junit-examples/blob/02dedb783f4f98c4d6b5bd53ae96bf8986eeebf7/junit-jupiter-starter-gradle/src/test/java/com/example/project/CalculatorTests.java)
  - [`junit-jupiter-starter-gradle/build.gradle`](https://github.com/junit-team/junit-examples/blob/02dedb783f4f98c4d6b5bd53ae96bf8986eeebf7/junit-jupiter-starter-gradle/build.gradle)
  - [`junit-jupiter-starter-gradle/README.md`](https://github.com/junit-team/junit-examples/blob/02dedb783f4f98c4d6b5bd53ae96bf8986eeebf7/junit-jupiter-starter-gradle/README.md)
- **Trace:** Read Calculator.add, follow the ordinary @Test assertion, then follow each @CsvSource row into the parameterized add method and expected result; finish at build.gradle where JUnit dependencies and useJUnitPlatform make those annotated methods executable.

**Why this level:**

- **Language technique 3:** Annotations materially drive discovery and data injection, while the surrounding Java remains deliberately basic.
- **Behavioral reasoning 1:** Each test has direct inputs, one method call, and an exact expected value with no mutable lifecycle.
- **Design span 2:** A few explicit project boundaries connect the class, its tests, and the runner configuration.
- **Constraint burden 2:** Routine build and test safeguards matter, but the artifact has no wider application constraints.
- **Novice accessibility floor 2:** A short primer on annotations, parameter rows, and source sets makes every execution predictable; no framework lifecycle beyond test discovery is required.
  - **Central concepts:** test discovery annotations; parameterized test data; main and test source separation
  - **Incidental concepts:** Gradle's Groovy configuration syntax; a lazy assertion-message lambda
- **Placement:** The four scores 3/1/2/2 produce rubric Level 2. Novice accessibility floor 2 preserves published Level 2.

**License:** EPL-2.0 ([evidence 1](https://github.com/junit-team/junit-examples/blob/02dedb783f4f98c4d6b5bd53ae96bf8986eeebf7/LICENSE.md))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The JUnit team documents junit-jupiter-starter-gradle as its bare-minimum complete setup for Java tests on JUnit Jupiter with Gradle, and CI builds the example projects.

**Language evidence:** The selected starter's calculator, JUnit Jupiter tests, and Gradle setup are first-party Java and Groovy maintained by the JUnit team; GitHub labels the repository Java.

**Coding relevance:**

Test organization, data-driven verification, failure diagnostics, and build integration are transferable software-engineering practices.

No specialist domain context is required.

**Eight-part quality gate:**

- **Source quality:** The selected project is intentionally minimal, complete, and free of placeholder methods or exercises.
- **Architecture:** Main code, test code, dependencies, and runner configuration have clear conventional boundaries.
- **Naming and idiom:** CalculatorTests, addsTwoNumbers, expectedResult, @Test, and @ParameterizedTest communicate their roles directly.
- **Tests:** One direct case and four parameter rows verify the complete behavior with exact values and useful messages.
- **Documentation:** The subproject README states its purpose, language, build system, and JUnit Platform relationship; the root README records CI coverage.
- **Traceability:** Every test input reaches the one add method and one exact assertion, while the build file explains discovery.
- **Maintainability:** Pinned dependencies, a standard source layout, and one explicit runner setting keep the starter current and easy to change.
- **Educational value:** The artifact teaches professional automated-test structure without hiding it behind application complexity.

**Inspection record:** commit `02dedb783f4f98c4d6b5bd53ae96bf8986eeebf7`, inspected 2026-08-30. Review passes: Codex lower-level expansion pass. Files inspected: `junit-jupiter-starter-gradle/src/main/java/com/example/project/Calculator.java`, `junit-jupiter-starter-gradle/src/test/java/com/example/project/CalculatorTests.java`, `junit-jupiter-starter-gradle/build.gradle`, `junit-jupiter-starter-gradle/README.md`, `README.md`, `LICENSE.md`. GitHub Linguist label: Java.

</details>

## Level 3 — Intermediate production software

### [java-diff-utils/java-diff-utils](https://github.com/java-diff-utils/java-diff-utils)

**Language 3 / Behavior 2 / Design 2 / Constraints 3 → Level 3**

**Source:** Production software

A library for computing sequence differences, applying and restoring patches, parsing unified diffs, and producing comparison output.

**Why study it:** The Patch path separates reversible transformation and conflict validation from diff-generation theory, making a familiar algorithmic product readable as a typed production API.

**Short context:**

- A patch is an ordered collection of insert, delete, and change deltas whose source chunks must match before they can be applied or reversed.

**Prerequisites:**

- Basic familiarity with Java classes and interfaces, generics, collections, exceptions, annotations and reflection at a basic level, and unit tests.

**Concepts this path develops:**

- Generic patch and chunk types.
- Reverse-ordered mutation.
- Generic sequence correctness.

**What you can learn:**

- Use `java-diff-utils/src/main/java/com/github/difflib/patch/Patch.java` to study the following transferable techniques and behaviors: Generic patches and chunks, polymorphic insert, delete, and change deltas, reverse-ordered mutation, input verification, conflict callbacks, inverse restoration, and serialization contracts.

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

**License:** Apache-2.0 ([evidence 1](https://github.com/java-diff-utils/java-diff-utils/blob/5e2e5b981533964aaeb19e2ba56d0f53dbd8b2dc/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The project publishes reusable Maven artifacts used by applications that compare text and other ordered data.

**Language evidence:** Diff algorithms, deltas, patches, unified-diff parsing, and output helpers in the two production modules are Java.

**Coding relevance:**

This compact patch model is sufficient context and avoids making Myers edit-graph theory the lesson; the selected behavior teaches transferable generics, reversible transformations, validation, conflict handling, and serialization.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Patch application and restoration expose delta order and conflict behavior directly, while AbstractDelta and Chunk isolate source verification and concrete mutation.
- **Architecture:** Patch orchestration, the delta hierarchy, chunk verification, conflict callbacks, and algorithm-independent tests have distinct responsibilities.
- **Naming and idiom:** Patch, AbstractDelta, ChangeDelta, DeleteDelta, InsertDelta, Chunk, applyTo, restore, and verifyAndApplyTo make the transformation model explicit.
- **Tests:** PatchWithAllDiffAlgorithmsTest and ChunkTest cover application across both generators, reversal, serialization, content mismatches, positions, fuzz tolerance, and generic values.
- **Documentation:** The README explains patch creation, application, restoration, algorithm substitution, unified forms, and conflicts sufficiently to orient the selected path.
- **Traceability:** A patch can be followed through reverse-ordered delta iteration, chunk verification, concrete sequence mutation, inverse restoration, and algorithm-independent assertions.
- **Maintainability:** Generic domain values and explicit delta and verification boundaries keep patch behavior independent from edit-path algorithms and external formats.
- **Educational value:** This path demonstrates how reversible algorithms become safe reusable libraries through typed models, validation, conflict policy, and tests.

**Inspection record:** commit `5e2e5b981533964aaeb19e2ba56d0f53dbd8b2dc`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `java-diff-utils/src/main/java/com/github/difflib/patch/Patch.java`, `java-diff-utils/src/main/java/com/github/difflib/patch/AbstractDelta.java`, `java-diff-utils/src/main/java/com/github/difflib/patch/Chunk.java`, `java-diff-utils/src/main/java/com/github/difflib/patch/ChangeDelta.java`, `java-diff-utils/src/main/java/com/github/difflib/patch/DeleteDelta.java`, `java-diff-utils/src/main/java/com/github/difflib/patch/InsertDelta.java`, `java-diff-utils/src/test/java/com/github/difflib/patch/PatchWithAllDiffAlgorithmsTest.java`, `java-diff-utils/src/test/java/com/github/difflib/patch/ChunkTest.java`, `LICENSE`. GitHub Linguist label: Java.

</details>

### [jhy/jsoup](https://github.com/jhy/jsoup)

**Language 2 / Behavior 3 / Design 3 / Constraints 4 → Level 3**

**Source:** Production software

An HTML parser and manipulation library with DOM traversal, CSS selectors, fetching, sanitization, and standards-aware error recovery.

**Why study it:** The Jsoup.clean path exposes a practical security boundary: parse untrusted HTML, rebuild a separate document, and admit only tags, attributes, and URL protocols allowed by an explicit policy.

**Short context:**

- An HTML sanitizer parses untrusted body content, copies only allowed elements and attributes into a new document, and restricts URL-bearing attributes to configured protocols.

**Prerequisites:**

- Basic familiarity with Java classes and interfaces, generics, collections, exceptions, annotations and reflection at a basic level, and unit tests.

**Concepts this path develops:**

- Visitor callbacks and fluent policy configuration.
- Destination stack during tree traversal.
- XSS security boundary.

**What you can learn:**

- Use `src/main/java/org/jsoup/Jsoup.java` to study the following transferable techniques and behaviors: Facade design, DOM visitor traversal, destination-stack state, safe document reconstruction, fluent policy configuration, tag and attribute checks, URL normalization, enforced attributes, immutability, and concurrency-safe policy reuse.

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

**License:** MIT ([evidence 1](https://github.com/jhy/jsoup/blob/7860d088e044236e288c1f88a743b68b2a0edece/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** jsoup is released as a production HTML library used for scraping, editing, validation, and safe content cleaning.

**Language evidence:** HTML tokenization, tree building, DOM nodes, selectors, networking, cleaning, and output under src/main are Java.

**Coding relevance:**

The original HtmlTreeBuilder path fails this gate because WHATWG insertion modes, active formatting and open-element stacks, foster parenting, foreign-content rules, and quirks dominate its program logic. The replacement Jsoup.clean-to-Cleaner-to-Safelist path is a substantial documented production feature whose short HTML and XSS context remains subordinate to transferable traversal, policy, normalization, validation, and security-boundary engineering.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The public clean facade, CleaningVisitor, destination stack, Safelist checks, URL normalization, and copy-into-new-document behavior expose security decisions directly.
- **Architecture:** Jsoup parsing, DOM nodes, Cleaner traversal, and Safelist policy are separated into recognizable layers with the untrusted input never reused as output.
- **Naming and idiom:** clean, Cleaner, CleaningVisitor, Safelist, isSafeTag, isSafeAttribute, protocols, enforced attributes, and preserveRelativeLinks state policy intent.
- **Tests:** CleanerTest and SafelistTest cover XSS payloads, malformed input, tag and attribute policy, pseudo-tags, protocols, relative and absolute URLs, nofollow, immutability, and concurrent reuse.
- **Documentation:** Public API documentation and explicit security warnings explain cleaning, safelists, protocol restrictions, URL handling, and the limits of the sanitizer.
- **Traceability:** An input fragment can be followed from Jsoup.clean through parsing, safe-node copying, attribute and protocol validation, normalization, and serialization into focused security tests.
- **Maintainability:** A small public facade, separate traversal and policy components, explicit normalization rules, and focused regressions localize a security-sensitive feature.
- **Educational value:** The path teaches secure transformation as an explicit parse, copy, validate, and normalize pipeline rather than as string filtering.

**Inspection record:** commit `7860d088e044236e288c1f88a743b68b2a0edece`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/main/java/org/jsoup/Jsoup.java`, `src/main/java/org/jsoup/safety/Cleaner.java`, `src/main/java/org/jsoup/safety/Safelist.java`, `src/test/java/org/jsoup/safety/CleanerTest.java`, `src/test/java/org/jsoup/safety/SafelistTest.java`, `LICENSE`. GitHub Linguist label: Java.

</details>

## Level 4 — Advanced

### [google/gson](https://github.com/google/gson)

**Language 4 / Behavior 4 / Design 3 / Constraints 4 → Level 4**

**Source:** Production software

A JSON serialization library that maps Java object graphs and generic types through configurable streaming and tree adapters.

**Why study it:** The Gson adapter path shows how a serialization library resolves and caches behavior for a generic type, breaks recursive construction cycles, and falls back to reflective fields or records.

**Short context:**

- Gson maps Java types to JSON through an ordered chain of TypeAdapterFactory implementations, using reflective binding when no earlier adapter handles a type.

**Prerequisites:**

- Working familiarity with Java classes and interfaces, generics, collections, exceptions, annotations and reflection at a basic level, and unit tests, plus experience tracing behavior across several production files.

**Concepts this path develops:**

- Reflection and erased generic type tokens.
- Concurrent adapter cache.
- Thread-safe cache identity and recursion.

**What you can learn:**

- Use `gson/src/main/java/com/google/gson/Gson.java` to study the following transferable techniques and behaviors: Erased generic TypeToken recovery, ordered adapter factories, concurrent caching, thread-local recursion placeholders, reflective field binding, record construction, access filtering, streaming conversion, and stable errors.

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

**License:** Apache-2.0 ([evidence 1](https://github.com/google/gson/blob/b3f4ca20087f9066de4c340522ff84e0558e1ad1/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** Google releases Gson as production serialization infrastructure consumed broadly through Maven and Android ecosystems.

**Language evidence:** The JSON model, streaming reader/writer, reflection adapters, type tokens, and serialization engine in the Gson modules are Java.

**Coding relevance:**

Basic JSON and reflection context is short and documented; the path teaches transferable erased-type modeling, recursive cache construction, concurrency, factory composition, reflective access policy, streaming, and compatibility.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Gson.getAdapter makes cache hits, per-thread construction state, FutureTypeAdapter placeholders, factory order, publication, and cleanup explicit.
- **Architecture:** The Gson facade, TypeToken, TypeAdapterFactory chain, ReflectiveTypeAdapterFactory, stream adapters, and access filters have clear roles.
- **Naming and idiom:** getAdapter, TypeToken, TypeAdapterFactory, FutureTypeAdapter, threadLocalAdapterResults, ReflectiveTypeAdapterFactory, bound fields, and access filters expose the resolution model.
- **Tests:** The selected Gson, reflection-access, and Java record suites cover recursion, concurrency, factory precedence, access policy, records, strictness, compatibility, and failures.
- **Documentation:** Extensive API Javadocs describe adapter lookup, factories, generic types, reflection access, records, and streaming behavior used by this trace.
- **Traceability:** A TypeToken can be followed through cache and recursion handling, across ordered factories into reflective binding, and back through streaming read or write into focused tests.
- **Maintainability:** Explicit cache publication, factory seams, access policy, and regression coverage constrain changes across type identity, recursion, Java versions, and serialized compatibility.
- **Educational value:** The path connects Java's erased type system and reflection to a disciplined, cached runtime serialization strategy.

**Inspection record:** commit `b3f4ca20087f9066de4c340522ff84e0558e1ad1`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `gson/src/main/java/com/google/gson/Gson.java`, `gson/src/main/java/com/google/gson/TypeAdapterFactory.java`, `gson/src/main/java/com/google/gson/reflect/TypeToken.java`, `gson/src/main/java/com/google/gson/internal/bind/ReflectiveTypeAdapterFactory.java`, `gson/src/test/java/com/google/gson/GsonTest.java`, `gson/src/test/java/com/google/gson/functional/ReflectionAccessFilterTest.java`, `gson/src/test/java/com/google/gson/functional/Java17RecordTest.java`, `LICENSE`. GitHub Linguist label: Java.

</details>

### [junit-team/junit4](https://github.com/junit-team/junit4)

**Language 4 / Behavior 4 / Design 4 / Constraints 4 → Level 4**

**Source:** Production software

The fourth-generation JUnit testing framework, including reflective discovery, runners, rules, assertions, lifecycle statements, and reports.

**Why study it:** The BlockJUnit4ClassRunner path shows how JUnit 4 discovers one annotated method, composes its execution lifecycle from Statements and rules, schedules it, and reports failures safely.

**Short context:**

- A JUnit 4 runner discovers annotated test methods, wraps each invocation with setup, teardown, timeout, expected-exception, and rule behavior, and reports events to listeners.

**Prerequisites:**

- Working familiarity with Java classes and interfaces, generics, collections, exceptions, annotations and reflection at a basic level, and unit tests, plus experience tracing behavior across several production files.

**Concepts this path develops:**

- Reflection and runtime annotations.
- Nested test and class lifecycles.
- JUnit 3 and 4 compatibility.

**What you can learn:**

- Use `src/main/java/org/junit/runners/BlockJUnit4ClassRunner.java` to study the following transferable techniques and behaviors: Reflection and annotations, runner hierarchies, Statement decoration, expected exceptions, timeouts, before and after hooks, ordered rules, child scheduling, listener events, and failure isolation.

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

**License:** EPL-1.0 ([evidence 1](https://github.com/junit-team/junit4/blob/890f3c972647de378f25e7271d8fbbd9d3456b79/LICENSE-junit.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** JUnit 4 remains maintained production test infrastructure and a compatibility foundation across the Java ecosystem.

**Language evidence:** The test runner, descriptions, statements, rules, assertions, matchers, and extension model under src/main/java are Java.

**Coding relevance:**

The familiar test-runner model is short and documented; the path's difficulty is transferable reflection, lifecycle composition, extension ordering, event propagation, isolation, and failure handling.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Runner, Statement, RuleContainer, ParentRunner, and RunNotifier responsibilities are explicit, with lifecycle order documented beside composition points.
- **Architecture:** BlockJUnit4ClassRunner builds method execution, ParentRunner schedules children, RuleContainer orders extensions, Statement represents each layer, and RunNotifier contains listener failures.
- **Naming and idiom:** runChild, methodBlock, methodInvoker, possiblyExpectingExceptions, withPotentialTimeout, withBefores, withAfters, withRules, and fireTestFailure expose execution order.
- **Tests:** The selected runner, expected-exception, timeout, and rule-container suites cover discovery, validation, statement order, customization, errors, interruption, and notification behavior.
- **Documentation:** Source Javadocs and JUnit 4 runner and rule documentation explain the composable lifecycle and extension contracts followed here.
- **Traceability:** An annotated method can be followed through reflective discovery, methodBlock's nested Statements, ParentRunner scheduling, and RunNotifier events into focused lifecycle tests.
- **Maintainability:** Small lifecycle decorators, explicit extension points, stable event boundaries, and ordering tests protect a mature compatibility-sensitive framework.
- **Educational value:** The path demonstrates how a test framework represents execution policy as composable objects while preserving deterministic cleanup and reporting.

**Inspection record:** commit `890f3c972647de378f25e7271d8fbbd9d3456b79`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/main/java/org/junit/runners/BlockJUnit4ClassRunner.java`, `src/main/java/org/junit/runners/ParentRunner.java`, `src/main/java/org/junit/runners/model/Statement.java`, `src/main/java/org/junit/runners/RuleContainer.java`, `src/main/java/org/junit/runner/notification/RunNotifier.java`, `src/test/java/org/junit/tests/running/classes/BlockJUnit4ClassRunnerTest.java`, `src/test/java/org/junit/tests/running/methods/ExpectedTest.java`, `src/test/java/org/junit/tests/running/methods/TimeoutTest.java`, `src/test/java/org/junit/runners/RuleContainerTest.java`, `LICENSE-junit.txt`. GitHub Linguist label: Java.

</details>

## Level 5 — Expert

### [jenkinsci/jenkins](https://github.com/jenkinsci/jenkins)

**Language 4 / Behavior 5 / Design 5 / Constraints 5 → Level 5**

**Source:** Production software

The Jenkins automation server core, including its persistent task queue, extension-driven eligibility policy, executor placement, work handoff, and completion lifecycle.

**Why study it:** The queue-to-executor path exposes how a mature extensible platform coordinates persistent scheduling state, resource assignment, concurrent execution, failure recovery, and compatibility without hiding the difficult invariants.

**Short context:**

- Jenkins queues tasks, assigns their subtasks to eligible executors on agents or the built-in node, and exposes extension points that may veto execution or placement.

**Prerequisites:**

- Strong working familiarity with Java classes and interfaces, generics, collections, exceptions, annotations and reflection at a basic level, and unit tests, plus experience tracing state, resources, or asynchronous control flow across many production files.

**Concepts this path develops:**

- Annotation and lookup-driven extension discovery.
- Concurrent queue-state transitions and scheduling.
- Lock and snapshot consistency.

**What you can learn:**

- Use `core/src/main/java/hudson/model/Queue.java` to study transferable task-state machines, concurrency control, extension policy, constrained resource assignment, multi-unit work handoff, persistence recovery, listener isolation, and completion guarantees.

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

**License:** MIT ([evidence 1](https://github.com/jenkinsci/jenkins/blob/982bc91d866ed90aa135b87a2cb4ac1e68c2412e/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** Jenkins publishes weekly and long-term-support automation-server releases used to build, test, analyze, and deploy production software.

**Language evidence:** The queue, placement, work-unit, executor, extension, persistence, and integration-test implementation in the selected path is first-party Java.

**Coding relevance:**

That vocabulary is short and documented in the selected source; the path's difficulty comes from transferable scheduling, concurrent state, resource assignment, extension policy, recovery, and lifecycle engineering rather than a specialist external discipline.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Queue's central maintain method is large, but its explicit state collections, lock boundaries, transition comments, snapshots, and recovery branches make its demanding invariants intentional and readable.
- **Architecture:** Queue, QueueTaskDispatcher, MappingWorksheet, LoadBalancer, WorkUnitContext, WorkUnit, and Executor separate state, policy, placement, handoff, synchronization, and execution responsibilities.
- **Naming and idiom:** WaitingItem, BlockedItem, BuildableItem, pending, JobOffer, MappingWorksheet, WorkUnitContext, synchronizeStart, and synchronizeEnd expose the scheduling lifecycle precisely.
- **Tests:** Enabled tests exercise blockage, permissions, pending-loss recovery, assignment policy, save and load recovery, executor failure, start, and completion; the two dedicated restart tests are disabled for flakiness and are not claimed as protection.
- **Documentation:** The README establishes the production platform and extensive source Javadocs document queue states, extension contracts, mapping, handoff, persistence normalization, and executor lifecycle.
- **Traceability:** The complete implementation-to-result path is observable across focused queue, dispatcher, and executor integration tests, although its evidence is necessarily distributed and does not isolate every mapping or multi-unit-latch branch.
- **Maintainability:** Explicit locking, immutable snapshots, compatibility converters, plugin exception containment, recovery paths, and regression tests constrain changes to the mature scheduler.
- **Educational value:** The path is a rare source-closed study of platform-scale scheduling and concurrency; it does not promise globally optimal placement or exactly-once execution across process crashes.

**Inspection record:** commit `982bc91d866ed90aa135b87a2cb4ac1e68c2412e`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `core/src/main/java/hudson/model/Queue.java`, `core/src/main/java/hudson/model/queue/QueueTaskDispatcher.java`, `core/src/main/java/hudson/model/queue/MappingWorksheet.java`, `core/src/main/java/hudson/model/LoadBalancer.java`, `core/src/main/java/hudson/model/queue/WorkUnitContext.java`, `core/src/main/java/hudson/model/queue/WorkUnit.java`, `core/src/main/java/hudson/model/Executor.java`, `test/src/test/java/hudson/model/QueueTest.java`, `test/src/test/java/hudson/model/queue/QueueTaskDispatcherTest.java`, `test/src/test/java/hudson/model/ExecutorTest.java`, `test/src/test/java/hudson/model/QueueRestartTest.java`, `README.md`, `pom.xml`, `LICENSE.txt`. GitHub Linguist label: Java.

</details>

### [spring-projects/spring-framework](https://github.com/spring-projects/spring-framework)

**Language 5 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

**Source:** Production software

A comprehensive application framework spanning dependency injection, AOP, transactions, data access, messaging, web stacks, and testing.

**Why study it:** The bean-factory path exposes how Spring resolves typed and qualified dependencies, constructs and post-processes one singleton, and preserves identity through concurrency and circular references.

**Short context:**

- A Spring bean factory stores object definitions, resolves dependencies by type and metadata, constructs and post-processes objects, manages singleton identity and circular references, and runs initialization callbacks.

**Prerequisites:**

- Strong working familiarity with Java classes and interfaces, generics, collections, exceptions, annotations and reflection at a basic level, and unit tests, plus experience tracing state, resources, or asynchronous control flow across many production files.

**Concepts this path develops:**

- Reflection and runtime construction.
- Singleton creation and circular-reference state.
- Thread-safe singleton identity and circular references.

**What you can learn:**

- Use `spring-beans/src/main/java/org/springframework/beans/factory/support/DefaultListableBeanFactory.java` to study the following transferable techniques and behaviors: Bean-definition registration, generic ResolvableType matching, DependencyDescriptor policy, qualifiers and priorities, constructor selection, reflective instantiation, post-processors, singleton caches, circular references, locking, initialization, and destruction.

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

**License:** Apache-2.0 ([evidence 1](https://github.com/spring-projects/spring-framework/blob/1b56f58999046051d76a653922c3ab72b4db9cf7/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** Spring Framework is actively released production infrastructure underlying a large portion of the enterprise Java ecosystem.

**Language evidence:** Core containers, reflection and type systems, AOP, transactions, data access, messaging, MVC, reactive web, and testing support are primarily Java.

**Coding relevance:**

Dependency injection and object lifecycle are documented programming-framework concepts; the selected path's difficulty is transferable reflection, generic type resolution, extension policy, concurrent lifecycle management, caching, compatibility, and error handling.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Bean definitions, dependency descriptors, type resolution, candidate selection, construction, lifecycle callbacks, and singleton states use explicit types and detailed contract comments.
- **Architecture:** DefaultListableBeanFactory, DependencyDescriptor, ResolvableType, ConstructorResolver, AbstractAutowireCapableBeanFactory, and DefaultSingletonBeanRegistry separate selection, construction, and identity.
- **Naming and idiom:** resolveDependency, DependencyDescriptor, ResolvableType, autowireCandidate, ConstructorResolver, createBean, earlySingletonObjects, and singletonFactories preserve container vocabulary.
- **Tests:** The selected bean-factory and singleton-registry suites cover generic and qualified matching, construction, lifecycle callbacks, circular references, concurrency, failures, and destruction.
- **Documentation:** Spring's bean-container reference and extensive source Javadocs document dependency resolution, scopes, lifecycle callbacks, post-processors, and circular references used here.
- **Traceability:** A registered definition can be followed through candidate matching and generic type resolution, constructor selection, instantiation and post-processing, then singleton cache publication and lifecycle tests.
- **Maintainability:** Strongly named container layers, explicit extension contracts, synchronized singleton state, and mature compatibility tests constrain changes to shared application infrastructure.
- **Educational value:** The path offers an expert study of how reflection-heavy dependency injection becomes a deterministic type, lifecycle, concurrency, and extension system.

**Inspection record:** commit `1b56f58999046051d76a653922c3ab72b4db9cf7`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `spring-beans/src/main/java/org/springframework/beans/factory/support/DefaultListableBeanFactory.java`, `spring-beans/src/main/java/org/springframework/beans/factory/config/DependencyDescriptor.java`, `spring-beans/src/main/java/org/springframework/beans/factory/support/AbstractAutowireCapableBeanFactory.java`, `spring-beans/src/main/java/org/springframework/beans/factory/support/ConstructorResolver.java`, `spring-beans/src/main/java/org/springframework/beans/factory/support/DefaultSingletonBeanRegistry.java`, `spring-core/src/main/java/org/springframework/core/ResolvableType.java`, `spring-beans/src/test/java/org/springframework/beans/factory/DefaultListableBeanFactoryTests.java`, `spring-beans/src/test/java/org/springframework/beans/factory/support/DefaultSingletonBeanRegistryTests.java`, `LICENSE.txt`. GitHub Linguist label: Java.

</details>

_Generated from `catalog/java.json`; do not edit by hand._

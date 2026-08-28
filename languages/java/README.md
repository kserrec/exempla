# Java

10 qualified repositories. Scores assume the learner described in [the SDC rubric](../../docs/sdc.md).

[← All languages](../README.md)

## SDC 1

### [FasterXML/jackson-annotations](https://github.com/FasterXML/jackson-annotations)

**S2 / D1 / C1 → SDC 1**

The standalone annotation contract used to configure Jackson serialization, deserialization, polymorphism, creators, and property handling.

**Real-world evidence:** FasterXML releases this artifact as a core dependency of the production Jackson data-processing ecosystem.

**Language evidence:** The published annotation types, value objects, and metadata contracts under src/main/java are Java.

**Why study it:** It shows how a stable metadata API encodes nuanced behavior through annotations, enums, defaults, compatibility rules, and unusually strong Javadocs.

**What you can learn:**

- Java annotations, retention and targets, public compatibility contracts, enum-based configuration, metadata defaults, and API documentation.

**Prerequisites:**

- Annotations, enums, reflection concepts, Java serialization terminology, and binary compatibility basics.

**Start here:** [`src/main/java/com/fasterxml/jackson/annotation/JsonProperty.java`](https://github.com/FasterXML/jackson-annotations/blob/474f7c9449f0efc6bf2200aac7ea4c348b429536/src/main/java/com/fasterxml/jackson/annotation/JsonProperty.java) — This central annotation demonstrates targets, defaults, access rules, nullability signals, compatibility history, and user-facing documentation.

**Why this level:**

- **S2:** 2,566 meaningful implementation LOC measured with tokei 14.0.0. Count covers Java in src/main, excluding tests, generated historical Javadocs, documentation, and build support.
- **D1:** Most implementation is declarative and readable once the learner understands Java annotation syntax.
- **C1:** Types define independent metadata contracts without an execution pipeline, service topology, or hidden state.
- **Placement:** S2 volume is mostly clear declarative API surface, so the simple code and architecture yield SDC 1.

**Quality-gate evidence:**

- **Source quality:** Defaults, precedence, version history, and edge cases are documented at the exact declaration where users depend on them.
- **Architecture:** One dependency-light artifact contains annotations and their supporting enum/value contracts, separate from Jackson engines.
- **Naming and idiom:** JsonProperty, JsonCreator, JsonTypeInfo, JsonIgnore, and OptBoolean consistently describe metadata intent.
- **Tests:** Tests verify annotation targets, default values, equality contracts, bundles, polymorphic settings, and compatibility behavior.
- **Documentation:** Extensive Javadocs serve as the canonical behavioral reference, supplemented by README and version notes.
- **Traceability:** A configuration option is declared, documented, and verified without needing to navigate a serializer implementation.
- **Maintainability:** The small dependency boundary and conservative public contracts support long-lived compatibility.
- **Educational value:** It teaches careful library API design through real annotations rather than a contrived reflection example.

**Inspection record:** commit `474f7c9449f0efc6bf2200aac7ea4c348b429536`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/main/java/com/fasterxml/jackson/annotation/JsonProperty.java`, `src/main/java/com/fasterxml/jackson/annotation/JsonTypeInfo.java`, `src/test/java/com/fasterxml/jackson/annotation/JsonTypeInfoTest.java`. GitHub Linguist label: Java. LOC exclusions: tests, docs, release notes.

**License:** [Apache-2.0](https://github.com/FasterXML/jackson-annotations/blob/474f7c9449f0efc6bf2200aac7ea4c348b429536/LICENSE)

### [ralfstx/minimal-json](https://github.com/ralfstx/minimal-json)

**S1 / D2 / C1 → SDC 1**

A dependency-free JSON parser and writer built around a compact Java value model and streaming parser.

**Real-world evidence:** The repository publishes a reusable JSON library that has served Java applications and EclipseSource products.

**Language evidence:** The parser, writer, value model, and public factory API in com.eclipsesource.json are implemented entirely in Java.

**Why study it:** Nearly the whole implementation is approachable in one sitting while still showing parsing, buffered input, immutable literals, mutable containers, and API design.

**What you can learn:**

- Recursive data models, streaming parsing, character buffering, fluent factories, serialization, and boundary-focused tests.

**Prerequisites:**

- Java classes and interfaces, collections, readers, exceptions, and JSON syntax.

**Start here:** [`com.eclipsesource.json/src/main/java/com/eclipsesource/json/JsonParser.java`](https://github.com/ralfstx/minimal-json/blob/c091e6985620da04d5abcd902aafb6c9583c48ea/com.eclipsesource.json/src/main/java/com/eclipsesource/json/JsonParser.java) — The parser exposes the complete token-to-handler flow, buffering, nesting guard, and error-location behavior.

**Why this level:**

- **S1:** 1,741 meaningful implementation LOC measured with tokei 14.0.0. Count covers the library's production Java source, excluding tests and the separate performance-test module.
- **D2:** Parsing and buffer boundaries require attention, but control flow is direct and uses ordinary Java constructs.
- **C1:** An important behavior crosses only a handful of classes with no plugins, persistence, networking, or services.
- **Placement:** A complete parser in fewer than two thousand production lines remains an SDC 1 project despite modest parser-specific reasoning.

**Quality-gate evidence:**

- **Source quality:** The parser uses explicit states, input guards, a nesting limit, and precise source locations without unnecessary abstraction.
- **Architecture:** A small value hierarchy surrounds one parser and writer, with a factory class providing the public entry point.
- **Naming and idiom:** JsonValue, JsonObject, readValue, readArray, and ParseException align directly with the data format.
- **Tests:** Focused tests cover every JSON form, malformed input, buffer boundaries, deep nesting, equality, mutation, and writing.
- **Documentation:** The README and Javadocs explain installation, parsing, construction, mutation, and performance tradeoffs.
- **Traceability:** A JSON string can be followed from Json.parse through JsonParser callbacks into the value objects and writer.
- **Maintainability:** No runtime dependencies, compact modules, and exhaustive behavioral tests keep changes local.
- **Educational value:** It is genuine library code whose entire data-format implementation is small enough for a first repository study.

**Inspection record:** commit `c091e6985620da04d5abcd902aafb6c9583c48ea`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `com.eclipsesource.json/src/main/java/com/eclipsesource/json/Json.java`, `com.eclipsesource.json/src/main/java/com/eclipsesource/json/JsonParser.java`, `com.eclipsesource.json/src/test/java/com/eclipsesource/json/JsonParser_Test.java`. GitHub Linguist label: Java. LOC exclusions: performance tests, tests.

**License:** [MIT](https://github.com/ralfstx/minimal-json/blob/c091e6985620da04d5abcd902aafb6c9583c48ea/LICENSE)

## SDC 2

### [java-diff-utils/java-diff-utils](https://github.com/java-diff-utils/java-diff-utils)

**S2 / D2 / C2 → SDC 2**

A library for computing sequence differences, applying and restoring patches, parsing unified diffs, and producing comparison output.

**Real-world evidence:** The project publishes reusable Maven artifacts used by applications that compare text and other ordered data.

**Language evidence:** Diff algorithms, deltas, patches, unified-diff parsing, and output helpers in the two production modules are Java.

**Why study it:** It connects a recognizable algorithm to clean domain objects and practical formats without expanding into a large framework.

**What you can learn:**

- Sequence diff algorithms, deltas and patches, generic APIs, conflict verification, unified-diff parsing, and algorithm substitution.

**Prerequisites:**

- Java generics and collections, sequence algorithms, equality, exceptions, and basic diff notation.

**Start here:** [`java-diff-utils/src/main/java/com/github/difflib/DiffUtils.java`](https://github.com/java-diff-utils/java-diff-utils/blob/5e2e5b981533964aaeb19e2ba56d0f53dbd8b2dc/java-diff-utils/src/main/java/com/github/difflib/DiffUtils.java) — The public facade selects algorithms and turns edit paths into patches, providing a map of the core domain.

**Why this level:**

- **S2:** 2,873 meaningful implementation LOC measured with tokei 14.0.0. Count covers production source in java-diff-utils and its JGit adapter, excluding tests and examples.
- **D2:** The Myers-style path computation needs algorithmic attention, while public objects and most transformations remain straightforward.
- **C2:** A few cohesive modules collaborate in one process with a narrow optional integration.
- **Placement:** Small-to-moderate size plus a substantive but contained algorithm makes this a clear SDC 2 study.

**Quality-gate evidence:**

- **Source quality:** Algorithms are isolated behind interfaces and patch application validates source positions and content before mutation.
- **Architecture:** Facades, algorithms, delta/patch domain objects, unified-diff parsing, and output utilities have distinct roles.
- **Naming and idiom:** DiffUtils, Patch, Delta, Chunk, ConflictOutput, and DiffAlgorithm make the model explicit.
- **Tests:** Tests cover algorithm cases, patch and unpatch symmetry, conflicts, unified formats, fuzzy matching, and output generation.
- **Documentation:** The README provides API examples, algorithm selection, patch usage, unified diffs, and integration guidance.
- **Traceability:** Two sequences can be followed from DiffUtils through the chosen algorithm into deltas and validated application.
- **Maintainability:** Algorithm interfaces and immutable-ish domain values let core comparison evolve independently of formats.
- **Educational value:** It shows how an algorithm becomes a useful, typed production library rather than remaining a textbook function.

**Inspection record:** commit `5e2e5b981533964aaeb19e2ba56d0f53dbd8b2dc`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `java-diff-utils/src/main/java/com/github/difflib/DiffUtils.java`, `java-diff-utils/src/main/java/com/github/difflib/patch/Patch.java`, `java-diff-utils/src/test/java/com/github/difflib/DiffUtilsTest.java`. GitHub Linguist label: Java. LOC exclusions: tests, examples.

**License:** [Apache-2.0](https://github.com/java-diff-utils/java-diff-utils/blob/5e2e5b981533964aaeb19e2ba56d0f53dbd8b2dc/LICENSE)

### [junit-team/junit4](https://github.com/junit-team/junit4)

**S3 / D2 / C2 → SDC 2**

The fourth-generation JUnit testing framework, including reflective discovery, runners, rules, assertions, lifecycle statements, and reports.

**Real-world evidence:** JUnit 4 remains maintained production test infrastructure and a compatibility foundation across the Java ecosystem.

**Language evidence:** The test runner, descriptions, statements, rules, assertions, matchers, and extension model under src/main/java are Java.

**Why study it:** It turns annotations and reflection into an explicit statement pipeline and runner extension model that is mature but still navigable.

**What you can learn:**

- Reflection-based discovery, runner templates, composable statements, rules, annotations, result notification, and backward compatibility.

**Prerequisites:**

- Java reflection and annotations, inheritance, exceptions, generics, testing frameworks, and design patterns.

**Start here:** [`src/main/java/org/junit/runners/BlockJUnit4ClassRunner.java`](https://github.com/junit-team/junit4/blob/890f3c972647de378f25e7271d8fbbd9d3456b79/src/main/java/org/junit/runners/BlockJUnit4ClassRunner.java) — The runner constructs children, validates test classes, wraps lifecycle statements, applies rules, and executes one test method.

**Why this level:**

- **S3:** 10,834 meaningful implementation LOC measured with tokei 14.0.0. Count covers Java under src/main, excluding the self-test suite, site content, historical documentation, and build files.
- **D2:** Annotations and reflective calls add indirection, but runners and Statements encode lifecycle order with conventional object-oriented patterns.
- **C2:** Several packages participate, yet a test method can be traced through one in-process runner pipeline.
- **Placement:** S3 breadth is offset by familiar framework patterns and a coherent lifecycle, producing SDC 2.

**Quality-gate evidence:**

- **Source quality:** Runner templates separate validation, discovery, lifecycle wrapping, execution, and notification into overridable methods.
- **Architecture:** JUnitCore drives Runners, Description trees, Statements, Rules, RunNotifier, and Results through explicit interfaces.
- **Naming and idiom:** ParentRunner, BlockJUnit4ClassRunner, Statement, TestRule, Description, and RunNotifier describe the execution model.
- **Tests:** The framework tests itself across runners, rules, assumptions, timeouts, parameterization, notifications, and historical bugs.
- **Documentation:** README, Javadocs, cookbook material, release notes, and a maintained wiki explain both use and extension.
- **Traceability:** A test method can be followed from JUnitCore into its runner, methodBlock wrappers, RunNotifier events, and Result.
- **Maintainability:** Stable interfaces and small lifecycle objects contain extensive backward-compatibility requirements.
- **Educational value:** It teaches how reflective framework magic can be decomposed into understandable object-oriented steps.

**Inspection record:** commit `890f3c972647de378f25e7271d8fbbd9d3456b79`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/main/java/org/junit/runner/JUnitCore.java`, `src/main/java/org/junit/runners/BlockJUnit4ClassRunner.java`, `src/test/java/org/junit/runner/JUnitCoreTest.java`. GitHub Linguist label: Java. LOC exclusions: tests, site documentation.

**License:** [EPL-1.0](https://github.com/junit-team/junit4/blob/890f3c972647de378f25e7271d8fbbd9d3456b79/LICENSE-junit.txt)

## SDC 3

### [google/gson](https://github.com/google/gson)

**S3 / D3 / C3 → SDC 3**

A JSON serialization library that maps Java object graphs and generic types through configurable streaming and tree adapters.

**Real-world evidence:** Google releases Gson as production serialization infrastructure consumed broadly through Maven and Android ecosystems.

**Language evidence:** The JSON model, streaming reader/writer, reflection adapters, type tokens, and serialization engine in the Gson modules are Java.

**Why study it:** It combines a friendly facade with reflection, generic type recovery, adapter factories, streaming tokens, recursion handling, and compatibility safeguards.

**What you can learn:**

- Reflection, generic TypeTokens, adapter factories, streaming JSON, object construction, recursion placeholders, and configurable serialization policy.

**Prerequisites:**

- Java reflection and generics, JSON, object construction, recursion, exceptions, and factory patterns.

**Start here:** [`gson/src/main/java/com/google/gson/Gson.java`](https://github.com/google/gson/blob/b3f4ca20087f9066de4c340522ff84e0558e1ad1/gson/src/main/java/com/google/gson/Gson.java) — The central facade builds and caches adapter chains, then connects tree, stream, and object representations.

**Why this level:**

- **S3:** 12,081 meaningful implementation LOC measured with tokei 14.0.0. Count covers production source in Gson, extras, and protocol-support modules, excluding tests, metrics, fixtures, and build support.
- **D3:** Type resolution, reflective access, recursion placeholders, unsafe allocation fallbacks, and streaming state require substantial Java knowledge.
- **C3:** Serialization crosses configuration, type tokens, constructor selection, adapter factories, reflection, and stream or tree representations.
- **Placement:** Moderate size with recurring reflection and a multi-layer conversion pipeline makes Gson SDC 3.

**Quality-gate evidence:**

- **Source quality:** Adapter resolution, recursive lookups, type checks, and reflection filters are explicit and guarded with descriptive failures.
- **Architecture:** Gson coordinates streaming, tree, reflection, type, construction, exclusion, and adapter-factory packages behind one facade.
- **Naming and idiom:** TypeAdapter, TypeAdapterFactory, TypeToken, JsonReader, JsonWriter, and Excluder consistently describe conversion roles.
- **Tests:** Extensive suites cover types, reflection, adapters, streams, malformed input, concurrency, security restrictions, and compatibility.
- **Documentation:** README, user guide, troubleshooting guide, Javadocs, and design notes explain both ordinary use and adapter extension.
- **Traceability:** An object can be followed from Gson.toJson through TypeToken lookup and adapter factories to JsonWriter tokens.
- **Maintainability:** Factory ordering and separate policies isolate extensibility from the streaming parser and public facade.
- **Educational value:** It demonstrates how Java's type erasure and reflection constraints shape a mature serialization library.

**Inspection record:** commit `b3f4ca20087f9066de4c340522ff84e0558e1ad1`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `gson/src/main/java/com/google/gson/Gson.java`, `gson/src/main/java/com/google/gson/internal/bind/ReflectiveTypeAdapterFactory.java`, `gson/src/test/java/com/google/gson/GsonTest.java`. GitHub Linguist label: Java. LOC exclusions: tests, metrics, native-image tests.

**License:** [Apache-2.0](https://github.com/google/gson/blob/b3f4ca20087f9066de4c340522ff84e0558e1ad1/LICENSE)

### [jhy/jsoup](https://github.com/jhy/jsoup)

**S3 / D3 / C3 → SDC 3**

An HTML parser and manipulation library with DOM traversal, CSS selectors, fetching, sanitization, and standards-aware error recovery.

**Real-world evidence:** jsoup is released as a production HTML library used for scraping, editing, validation, and safe content cleaning.

**Language evidence:** HTML tokenization, tree building, DOM nodes, selectors, networking, cleaning, and output under src/main are Java.

**Why study it:** It turns the HTML parsing specification into readable token and tree-builder state machines while preserving an ergonomic public DOM API.

**What you can learn:**

- Tokenizers and tree builders, state machines, error recovery, DOM models, CSS selection, sanitization, encodings, and HTTP boundaries.

**Prerequisites:**

- HTML and DOM concepts, state machines, Java collections, HTTP, character encodings, and parsing basics.

**Start here:** [`src/main/java/org/jsoup/parser/HtmlTreeBuilder.java`](https://github.com/jhy/jsoup/blob/7860d088e044236e288c1f88a743b68b2a0edece/src/main/java/org/jsoup/parser/HtmlTreeBuilder.java) — The tree builder connects tokenizer states, insertion modes, formatting elements, scope rules, and DOM construction.

**Why this level:**

- **S3:** 18,633 meaningful implementation LOC measured with tokei 14.0.0. Count covers production Java under src/main, excluding tests, generated Javadocs, benchmarks, documentation, and build support.
- **D3:** Tokenizer and insertion-mode behavior require HTML parsing knowledge, while the DOM and public APIs remain conventional.
- **C3:** Fetching and parsing cross several subsystems, but they are organized around a coherent document model.
- **Placement:** A mid-sized codebase with one deep standards domain and several clear subsystems fits SDC 3.

**Quality-gate evidence:**

- **Source quality:** Parsing states and recovery rules are explicit, validation helpers guard assumptions, and public APIs keep standards detail contained.
- **Architecture:** Parser, nodes, selectors, safety, helper, and HTTP packages separate document construction from use and transport.
- **Naming and idiom:** Tokeniser, TreeBuilder, Document, Element, Selector, Safelist, and Cleaner provide consistent domain language.
- **Tests:** Broad tests cover malformed and standards fixtures, encodings, selectors, DOM mutation, cleaners, connections, and regressions.
- **Documentation:** The project site, cookbook, API docs, changelog, and source comments explain common use and parsing behavior.
- **Traceability:** HTML input can be followed through tokenization and insertion modes into nodes, selectors, and serialized output.
- **Maintainability:** Specification-heavy behavior is isolated in parser states while the DOM and transport surfaces evolve independently.
- **Educational value:** It is a practical bridge from a readable Java API into a real browser-grade parsing problem.

**Inspection record:** commit `7860d088e044236e288c1f88a743b68b2a0edece`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/main/java/org/jsoup/Jsoup.java`, `src/main/java/org/jsoup/parser/HtmlTreeBuilder.java`, `src/test/java/org/jsoup/parser/HtmlParserTest.java`. GitHub Linguist label: Java. LOC exclusions: tests, Javadocs, benchmarks.

**License:** [MIT](https://github.com/jhy/jsoup/blob/7860d088e044236e288c1f88a743b68b2a0edece/LICENSE)

## SDC 4

### [apache/maven](https://github.com/apache/maven)

**S4 / D3 / C4 → SDC 4**

The core of Apache Maven: project-model building, dependency resolution, reactor planning, lifecycle execution, plugins, sessions, and CLI behavior.

**Real-world evidence:** Apache Maven is a production build and dependency-management system central to the Java ecosystem.

**Language evidence:** The model, resolver integration, reactor graph, lifecycle, plugin execution, CLI, and compatibility layers are implemented in Java.

**Why study it:** Its source exposes how declarative project models become dependency graphs and ordered plugin executions across local and remote repositories.

**What you can learn:**

- Build lifecycles, dependency graphs, model inheritance, repository resolution, plugin containers, session scope, parallel reactors, and compatibility layers.

**Prerequisites:**

- Advanced Java, dependency injection, graphs, artifact repositories, concurrency, class loading, and build-tool concepts.

**Start here:** [`impl/maven-core/src/main/java/org/apache/maven/DefaultMaven.java`](https://github.com/apache/maven/blob/e53b7bd98f7352a90af8795af75a2f4c5d3f179c/impl/maven-core/src/main/java/org/apache/maven/DefaultMaven.java) — The numbered execution path assembles repository sessions, reads projects, builds the reactor graph, invokes participants, and starts lifecycles.

**Why this level:**

- **S4:** 132,793 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party Java and small supporting scripts, excluding tests, documentation, generated sources, fixtures, and build output.
- **D3:** Most code uses familiar enterprise Java patterns, while model resolution, class realms, graphs, and concurrency add recurring technical depth.
- **C4:** A build crosses CLI configuration, model inheritance, repositories, graph planning, lifecycles, plugins, classloaders, events, and parallel builders.
- **Placement:** Large size and many interacting build subsystems make Maven SDC 4 even though much individual Java is conventional.

**Quality-gate evidence:**

- **Source quality:** Core execution documents its phases and maintains explicit session, graph, event, error, and cleanup boundaries.
- **Architecture:** API, model, resolver, core implementation, lifecycle, plugin, CLI, compatibility, and daemon modules have recognizable roles.
- **Naming and idiom:** MavenSession, MavenProject, ProjectDependencyGraph, LifecycleStarter, MojoExecution, and RepositorySystem form stable vocabulary.
- **Tests:** Unit, integration, compatibility, resolver, plugin, reactor, and CLI suites exercise builds across many realistic projects.
- **Documentation:** User guides, plugin and extension references, model documentation, architecture material, and contributor guides are extensive.
- **Traceability:** A build request can be followed through DefaultMaven, graph creation, LifecycleStarter, task segments, builders, and plugin executions.
- **Maintainability:** Interfaces and compatibility modules isolate long-lived ecosystem contracts from newer core implementations.
- **Educational value:** It is a strong case study in how a ubiquitous declarative build tool becomes an extensible execution engine.

**Inspection record:** commit `e53b7bd98f7352a90af8795af75a2f4c5d3f179c`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `impl/maven-core/src/main/java/org/apache/maven/DefaultMaven.java`, `impl/maven-core/src/main/java/org/apache/maven/lifecycle/internal/DefaultLifecycleStarter.java`, `impl/maven-core/src/test/java/org/apache/maven/DefaultMavenTest.java`. GitHub Linguist label: Java. LOC exclusions: tests, site documentation, generated sources.

**License:** [Apache-2.0](https://github.com/apache/maven/blob/e53b7bd98f7352a90af8795af75a2f4c5d3f179c/LICENSE)

### [netty/netty](https://github.com/netty/netty)

**S5 / D4 / C4 → SDC 4**

An asynchronous networking framework providing event loops, channel pipelines, pooled buffers, transports, and many protocol codecs.

**Real-world evidence:** Netty is production networking infrastructure embedded in servers, clients, databases, RPC systems, and JVM frameworks.

**Language evidence:** Buffers, channels, event loops, transports, protocol codecs, handlers, resolvers, and native bridges are predominantly Java.

**Why study it:** It exposes high-performance event-driven design, reference-counted memory, platform transports, concurrency contracts, and codec composition at industrial scale.

**What you can learn:**

- Event loops, futures, channel pipelines, byte buffers, reference counting, zero-copy I/O, native transports, protocol codecs, and backpressure.

**Prerequisites:**

- Advanced Java concurrency, NIO, memory management, networking protocols, generics, and operating-system I/O.

**Start here:** [`transport/src/main/java/io/netty/channel/DefaultChannelPipeline.java`](https://github.com/netty/netty/blob/ada3b9ab0c7a54f6e73f821216ba3db81bd90d55/transport/src/main/java/io/netty/channel/DefaultChannelPipeline.java) — The pipeline shows handler composition, event direction, executor assignment, lifecycle callbacks, and how a Channel processes I/O.

**Why this level:**

- **S5:** 275,763 meaningful implementation LOC measured with tokei 14.0.0. Count covers production Java, native C, and supporting shell across modules, excluding tests, examples, benchmarks, generated metadata, and build output.
- **D4:** Performance-sensitive concurrency, resource ownership, lock-free structures, unsafe/native paths, and binary protocols recur throughout core code.
- **C4:** Network behavior crosses event loops, pipelines, buffers, transports, handlers, codecs, DNS, TLS, and native platform integrations.
- **Placement:** Netty's S5 size is balanced by a coherent framework architecture; D4 and C4 place it at the upper end of SDC 4.

**Quality-gate evidence:**

- **Source quality:** Hot paths document ownership, thread-affinity, indexing, reference counts, and lifecycle invariants alongside defensive checks.
- **Architecture:** Common utilities support buffers, transports, channels, handlers, codecs, resolvers, TLS, and platform-native modules behind stable interfaces.
- **Naming and idiom:** Channel, EventLoop, Pipeline, Handler, ByteBuf, Future, Bootstrap, and Codec consistently model event-driven networking.
- **Tests:** Extensive unit, integration, leak, transport, protocol, concurrency, fuzz, and platform suites exercise edge behavior.
- **Documentation:** Guides, API references, examples, transport notes, contributor material, and design comments support deep study.
- **Traceability:** An inbound buffer can be traced from a transport event through the ChannelPipeline and handlers into protocol decoding and release.
- **Maintainability:** Module and interface boundaries isolate protocols and platforms while shared concurrency and buffer contracts remain centralized.
- **Educational value:** It is a demanding but exemplary source for understanding how managed-language networking reaches systems-level performance.

**Inspection record:** commit `ada3b9ab0c7a54f6e73f821216ba3db81bd90d55`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `transport/src/main/java/io/netty/channel/DefaultChannelPipeline.java`, `buffer/src/main/java/io/netty/buffer/AbstractByteBuf.java`, `transport/src/test/java/io/netty/channel/DefaultChannelPipelineTest.java`. GitHub Linguist label: Java. LOC exclusions: tests, examples, benchmarks, generated native-image metadata.

**License:** [Apache-2.0](https://github.com/netty/netty/blob/ada3b9ab0c7a54f6e73f821216ba3db81bd90d55/LICENSE.txt)

## SDC 5

### [apache/cassandra](https://github.com/apache/cassandra)

**S5 / D5 / C5 → SDC 5**

A distributed transactional database built around partitioned storage, replication, consensus, compaction, repair, and failure-tolerant cluster operation.

**Real-world evidence:** Apache Cassandra is an actively released production database deployed for large, fault-tolerant data workloads.

**Language evidence:** Storage engines, consensus, replication, query processing, compaction, streaming, networking, repair, and cluster services are predominantly Java.

**Why study it:** The source brings database internals and distributed systems together: on-disk formats, memtables, logs, consensus, replication, streaming, repair, and operational control.

**What you can learn:**

- LSM storage, commit logs, SSTables, compaction, partitioning, replication, consensus, failure detection, repair, streaming, concurrency, and operational invariants.

**Prerequisites:**

- Expert Java and concurrency, data structures, storage engines, distributed consensus, networking, filesystems, and database operations.

**Start here:** [`src/java/org/apache/cassandra/db/ColumnFamilyStore.java`](https://github.com/apache/cassandra/blob/92530a18db31715bc0e9ec2363a735bc034ee530/src/java/org/apache/cassandra/db/ColumnFamilyStore.java) — This table-level service connects memtables, flushing, SSTables, compaction, indexes, metrics, snapshots, and lifecycle transactions.

**Why this level:**

- **S5:** 501,795 meaningful implementation LOC measured with tokei 14.0.0. Count covers production Java plus first-party Python tooling under src and pylib, excluding tests, bundled libraries, docs, examples, build support, and static assets.
- **D5:** Correctness depends repeatedly on expert database algorithms, persistent formats, concurrency, failure modes, cluster metadata, and consensus protocols.
- **C5:** Queries and maintenance cross storage, schema, replication, consensus, networking, streaming, repair, security, metrics, and multi-node coordination.
- **Placement:** All three dimensions independently occupy the highest band, making Cassandra an unequivocal SDC 5 codebase.

**Quality-gate evidence:**

- **Source quality:** Critical storage and cluster code names invariants, separates lifecycle transactions, and tests failures and recovery at multiple levels.
- **Architecture:** Query, schema, storage, commit log, SSTable, compaction, consensus, replication, messaging, streaming, repair, and tooling subsystems are explicit.
- **Naming and idiom:** ColumnFamilyStore, Memtable, SSTableReader, CommitLog, Gossiper, Replica, Repair, and ClusterMetadata encode the database model.
- **Tests:** Unit, distributed, upgrade, fuzz, stress, compatibility, topology, and failure-injection suites exercise data and cluster behavior.
- **Documentation:** Architecture, operations, data modeling, CQL, development, testing, and compatibility documentation supports expert navigation.
- **Traceability:** A mutation can be followed through coordination, commit log and memtable, flushing, SSTables, compaction, replication, and repair.
- **Maintainability:** Subsystem ownership, compatibility gates, persistent-format discipline, lifecycle abstractions, and broad testing constrain high-risk changes.
- **Educational value:** It is a deep production study in the intersection of storage engines, distributed consensus, and long-lived operational software.

**Inspection record:** commit `92530a18db31715bc0e9ec2363a735bc034ee530`, reviewed 2026-08-28 by Codex. Files sampled: `README.asc`, `src/java/org/apache/cassandra/service/StorageService.java`, `src/java/org/apache/cassandra/db/ColumnFamilyStore.java`, `test/unit/org/apache/cassandra/db/ColumnFamilyStoreTest.java`. GitHub Linguist label: Java. LOC exclusions: tests, third-party libraries, documentation, examples, build infrastructure.

**License:** [Apache-2.0](https://github.com/apache/cassandra/blob/92530a18db31715bc0e9ec2363a735bc034ee530/LICENSE.txt)

### [spring-projects/spring-framework](https://github.com/spring-projects/spring-framework)

**S5 / D4 / C5 → SDC 5**

A comprehensive application framework spanning dependency injection, AOP, transactions, data access, messaging, web stacks, and testing.

**Real-world evidence:** Spring Framework is actively released production infrastructure underlying a large portion of the enterprise Java ecosystem.

**Language evidence:** Core containers, reflection and type systems, AOP, transactions, data access, messaging, MVC, reactive web, and testing support are primarily Java.

**Why study it:** It shows how decades of compatibility, extension points, reflection, proxying, reactive and servlet stacks, and cross-cutting concerns are governed in one platform.

**What you can learn:**

- Dependency injection, bean lifecycles, reflection and type resolution, proxies and AOP, transactions, reactive streams, web dispatch, extension contracts, and compatibility.

**Prerequisites:**

- Expert Java, reflection and generics, concurrency, annotations, proxying, HTTP, databases, reactive streams, and enterprise architecture.

**Start here:** [`spring-beans/src/main/java/org/springframework/beans/factory/support/DefaultListableBeanFactory.java`](https://github.com/spring-projects/spring-framework/blob/1b56f58999046051d76a653922c3ab72b4db9cf7/spring-beans/src/main/java/org/springframework/beans/factory/support/DefaultListableBeanFactory.java) — The central bean factory connects definitions, type matching, dependency resolution, scopes, post-processors, and lifecycle behavior.

**Why this level:**

- **S5:** 391,522 meaningful implementation LOC measured with tokei 14.0.0. Calibration measurement covers first-party framework implementation across Java and Kotlin, excluding tests, fixtures, docs, benchmarks, generated source, and build output.
- **D4:** Advanced Java mechanisms and domain-specific web, data, transaction, messaging, and reactive behavior recur across the main learning paths.
- **C5:** Core containers interact with dozens of modules, deployment modes, integration contracts, infrastructure layers, and compatibility surfaces.
- **Placement:** S5 and C5 trigger the SDC 5 guardrail, matching the expert effort required to understand the framework as a whole.

**Quality-gate evidence:**

- **Source quality:** Complex lifecycle and reflection code is strongly documented, typed, guarded, and decomposed around stable interfaces.
- **Architecture:** Core, beans, context, AOP, transactions, data, messaging, servlet web, reactive web, testing, and observability modules have explicit boundaries.
- **Naming and idiom:** BeanDefinition, ApplicationContext, HandlerMapping, Advisor, TransactionManager, and ResolvableType form precise shared language.
- **Tests:** Massive unit, integration, compatibility, web, reactive, transaction, container, and regression suites cover the platform.
- **Documentation:** Reference manuals, API docs, architecture guidance, migration notes, and contributor material are comprehensive.
- **Traceability:** A bean can be traced from definition registration through type resolution, dependency selection, construction, post-processing, proxying, and shutdown.
- **Maintainability:** Module boundaries, public contracts, deprecation policy, exhaustive tests, and careful compatibility layers govern a large surface.
- **Educational value:** For advanced readers it is a canonical study of sustaining an extensible framework across generations of Java applications.

**Inspection record:** commit `1b56f58999046051d76a653922c3ab72b4db9cf7`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `spring-core/src/main/java/org/springframework/core/ResolvableType.java`, `spring-beans/src/main/java/org/springframework/beans/factory/support/DefaultListableBeanFactory.java`, `spring-beans/src/test/java/org/springframework/beans/factory/DefaultListableBeanFactoryTests.java`. GitHub Linguist label: Java. LOC exclusions: tests, test fixtures, documentation, benchmarks, generated source.

**License:** [Apache-2.0](https://github.com/spring-projects/spring-framework/blob/1b56f58999046051d76a653922c3ab72b4db9cf7/LICENSE.txt)

_Generated from `catalog/java.json`; do not edit by hand._

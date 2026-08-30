# Scala

6 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

**Source legend:** Production software is built primarily for real users or systems. Educational exemplars are complete teaching-oriented software and may appear only at Levels 1 and 2.

[← All languages](../README.md)

## Level 1 — First real code

No qualified learning path has been published at this level. An empty Level 1 means Exempla has not yet found a path gentle enough to publish here; learners are not being told to jump to Level 2.

## Level 2 — Guided real-world patterns

No qualified learning path has been published at this level. Standards are not lowered to fill a slot.

## Level 3 — Intermediate production software

### [scopt/scopt](https://github.com/scopt/scopt)

**Language 3 / Behavior 2 / Design 3 / Constraints 3 → Level 3**

**Source:** Production software

A small cross-platform command-line option parser for Scala with functional and object-oriented declaration styles and interceptable effects.

**Why study it:** Its source connects a typed declaration DSL to token matching, occurrence constraints, configuration updates, validation, usage rendering, and effect handling without a large framework.

**Short context:**

- A command-line parser maps option, positional, and command tokens into a typed application configuration and explicit effects.

**Prerequisites:**

- Scala generics, type classes, case classes, immutable collections, higher-order functions, command-line conventions, and basic cross-platform source layouts.

**Concepts this path develops:**

- Generic typed Read instances.
- Synchronous token-consumption loop.
- Short, long, grouped, attached, command, and positional token forms.

**What you can learn:**

- Typed option readers, builder DSLs, immutable parser descriptions, token classification, commands and positionals, occurrence constraints, validation, effect separation, usage rendering, and cross-platform parsing.

**Learning path:**

- **Goal:** Understand how scopt turns a typed declarative option DSL into token matching, configuration updates, validation, and separately interpreted effects.
- **Start here:** [`shared/src/main/scala/scopt/OParser.scala`](https://github.com/scopt/scopt/blob/f1906911a989320a87c0670fb2e654d48731747d/shared/src/main/scala/scopt/OParser.scala) — OParser builds the declarative option list and hands it to ORunner, providing the shortest path from user-facing DSL calls to token execution and parser effects.
- **Then read:**
  - [`shared/src/main/scala/scopt/OptionDef.scala`](https://github.com/scopt/scopt/blob/f1906911a989320a87c0670fb2e654d48731747d/shared/src/main/scala/scopt/OptionDef.scala)
  - [`shared/src/main/scala/scopt/ORunner.scala`](https://github.com/scopt/scopt/blob/f1906911a989320a87c0670fb2e654d48731747d/shared/src/main/scala/scopt/ORunner.scala)
  - [`shared/src/main/scala/scopt/Read.scala`](https://github.com/scopt/scopt/blob/f1906911a989320a87c0670fb2e654d48731747d/shared/src/main/scala/scopt/Read.scala)
  - [`shared/src/test/scala/scopttest/ImmutableParserSpec.scala`](https://github.com/scopt/scopt/blob/f1906911a989320a87c0670fb2e654d48731747d/shared/src/test/scala/scopttest/ImmutableParserSpec.scala)
  - [`shared/src/test/scala/scopttest/MonadicParserSpec.scala`](https://github.com/scopt/scopt/blob/f1906911a989320a87c0670fb2e654d48731747d/shared/src/test/scala/scopttest/MonadicParserSpec.scala)
  - [`README.md`](https://github.com/scopt/scopt/blob/f1906911a989320a87c0670fb2e654d48731747d/README.md)
  - [`LICENSE.md`](https://github.com/scopt/scopt/blob/f1906911a989320a87c0670fb2e654d48731747d/LICENSE.md)
- **Trace:** Start with OParser's typed builder operations, follow the resulting OptionDefs into ORunner's token loop, pending options and arguments, commands, occurrence checks, configuration actions, validation, and emitted effects, then close both supported parser APIs in the direct suites.

**Why this level:**

- **Language technique 3:** Generics, typed readers, higher-order updates, and algebraic descriptions recur without expert language machinery.
- **Behavioral reasoning 2:** The parser has meaningful state and branching, but the selected lifecycle remains synchronous and locally inspectable.
- **Design span 3:** Several meaningful declaration, representation, execution, conversion, and verification boundaries cooperate.
- **Constraint burden 3:** Several syntax, validation, API, rendering, and portability guarantees constrain parser changes.
- **Placement:** The four scores 3/2/3/3 sum to 11; their arithmetic mean is 2.75 and rounds half-up to Level 3. The published result is Level 3.

**License:** MIT ([evidence 1](https://github.com/scopt/scopt/blob/f1906911a989320a87c0670fb2e654d48731747d/LICENSE.md))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The project publishes scopt artifacts for Scala 2, Scala 3, JVM, Scala.js, and Scala Native and documents a mature application configuration API.

**Language evidence:** The option definitions, functional and object-oriented DSLs, parser runner, validation, rendering, effects, type readers, and platform adapters are Scala.

**Coding relevance:**

The concise command-line vocabulary is subordinate to transferable lessons in generic readers, declarative builders, immutable descriptions, token-state execution, recursive commands, validation, and effect separation.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Parser descriptions are immutable, effects are represented explicitly, and token, validation, and rendering responsibilities remain separated.
- **Architecture:** OParser builds OptionDefs, ORunner consumes arguments into configurations and OEffects, and a separate interpreter performs display or termination effects.
- **Naming and idiom:** OptionDefKind, minOccurs, validateConfig, runParser, runEffects, RenderingMode, and DefaultOEffectSetup reveal the parsing lifecycle.
- **Tests:** Shared and platform suites cover both APIs, option forms, grouped flags, commands, arguments, validation, fallback values, rendering, URI and platform readers, and regression cases.
- **Documentation:** The README supplies complete functional and object-oriented examples, generated usage output, supported readers, commands, validation, and effect interception.
- **Traceability:** A declared option can be followed from OParserBuilder into an OptionDef, ORunner's token match and action, an updated configuration, emitted effects, and ImmutableParserSpec.
- **Maintainability:** The dual APIs converge on one representation, platform dependencies stay at the edge, and behavior-focused suites cover the supported matrix.
- **Educational value:** It is a compact example of separating a declarative interface, a pure-ish execution result, and side-effect interpretation.

**Inspection record:** commit `f1906911a989320a87c0670fb2e654d48731747d`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `shared/src/main/scala/scopt/OParser.scala`, `shared/src/main/scala/scopt/OptionDef.scala`, `shared/src/main/scala/scopt/ORunner.scala`, `shared/src/main/scala/scopt/Read.scala`, `shared/src/test/scala/scopttest/ImmutableParserSpec.scala`, `shared/src/test/scala/scopttest/MonadicParserSpec.scala`, `README.md`, `LICENSE.md`. GitHub Linguist label: Scala.

</details>

### [softwaremill/retry](https://github.com/softwaremill/retry)

**Language 3 / Behavior 3 / Design 2 / Constraints 3 → Level 3**

**Source:** Production software

A compact library of composable retry policies for Scala Futures, including immediate, paused, exponential-backoff, jittered, conditional, and fail-fast strategies.

**Why study it:** softwaremill/retry is a small, inspectable example of composing nonblocking retry policies around deferred Future work without obscuring delays or failures.

**Short context:**

- A retry policy classifies a Future result, chooses whether and when to try deferred work again, and optionally modifies the delay with backoff or jitter.

**Prerequisites:**

- Readers should know Scala Futures, by-name parameters, pattern matching, higher-order functions, type-class-style predicates, and basic retry and backoff terminology.

**Concepts this path develops:**

- Generic Future policies and deferred by-name work.
- Asynchronous recursive retries.
- Work must remain deferred and nonblocking.

**What you can learn:**

- Trace direct, paused, backoff, conditional, fail-fast, and jittered policies through deferred Future evaluation, result classification, countdown recursion, and external scheduling.

**Learning path:**

- **Goal:** Understand how a compact Scala library composes nonblocking retry policies around deferred Future work while preserving result, delay, and failure contracts.
- **Start here:** [`retry/src/main/scala/Policy.scala`](https://github.com/softwaremill/retry/blob/f5d887b23adb8c34b2dc891a4d25a6263e300c48/retry/src/main/scala/Policy.scala) — The reviewed trace begins in Policy.scala because it defines policy composition and the recursive decision point for every retry attempt.
- **Then read:**
  - [`retry/src/main/scala/Defaults.scala`](https://github.com/softwaremill/retry/blob/f5d887b23adb8c34b2dc891a4d25a6263e300c48/retry/src/main/scala/Defaults.scala)
  - [`retry/src/main/scala/Jitter.scala`](https://github.com/softwaremill/retry/blob/f5d887b23adb8c34b2dc891a4d25a6263e300c48/retry/src/main/scala/Jitter.scala)
  - [`retry/src/main/scala/Success.scala`](https://github.com/softwaremill/retry/blob/f5d887b23adb8c34b2dc891a4d25a6263e300c48/retry/src/main/scala/Success.scala)
  - [`retry/src/test/scala/PolicySpec.scala`](https://github.com/softwaremill/retry/blob/f5d887b23adb8c34b2dc891a4d25a6263e300c48/retry/src/test/scala/PolicySpec.scala)
  - [`retry/src/test/scala/JitterSpec.scala`](https://github.com/softwaremill/retry/blob/f5d887b23adb8c34b2dc891a4d25a6263e300c48/retry/src/test/scala/JitterSpec.scala)
  - [`README.md`](https://github.com/softwaremill/retry/blob/f5d887b23adb8c34b2dc891a4d25a6263e300c48/README.md)
  - [`LICENSE`](https://github.com/softwaremill/retry/blob/f5d887b23adb8c34b2dc891a4d25a6263e300c48/LICENSE)
- **Trace:** Start with Policy's directly, pause, backoff, conditional, and fail-fast implementations; follow deferred Future evaluation through Success classification, countdown recursion, Defaults and odelay scheduling, then close capped delay, jitter, attempt-count, timing, and failure behavior in the two focused suites. Timer is supplied by the external odelay dependency, so no nonexistent repository-local Timer.scala is listed.

**Why this level:**

- **Language technique 3:** Generics, Futures, type-class dispatch, and higher-order composition materially shape the path without recurring expert metaprogramming or type machinery.
- **Behavioral reasoning 3:** The learner must follow asynchronous repetition and policy state across Future completion while the lifecycle remains bounded to one retry operation.
- **Design span 2:** A few cohesive modules and one external timer boundary contain the complete behavior.
- **Constraint burden 3:** Several asynchronous, arithmetic, timing, and API guarantees constrain ordinary policy changes.
- **Placement:** The four scores 3/3/2/3 sum to 11; their arithmetic mean is 2.75 and rounds half-up to Level 3. The published result is Level 3.

**License:** MIT ([evidence 1](https://github.com/softwaremill/retry/blob/f5d887b23adb8c34b2dc891a4d25a6263e300c48/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** SoftwareMill maintains and publishes the versioned com.softwaremill.retry artifact, and the README documents application-facing policy configuration and timer integration.

**Language evidence:** Retry policies, success predicates, jitter algorithms, asynchronous scheduling, and the complete test suite are implemented in Scala under retry/src.

**Coding relevance:**

The small retry vocabulary is subordinate to transferable lessons in deferred computation, asynchronous recursion, policy composition, type-class predicates, delay scheduling, bounded arithmetic, and failure propagation.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Policy.scala, Defaults.scala, Success.scala, and Jitter.scala have narrow responsibilities and keep retry decisions and delay arithmetic visible.
- **Architecture:** Policies classify a completed Future result, choose a delay, and defer another attempt through the external odelay timer boundary.
- **Naming and idiom:** Policy, Success, Defaults, Jitter, pause, backoff, and failFast state the behavior directly and use Scala Futures and composable functions idiomatically.
- **Tests:** PolicySpec.scala and JitterSpec.scala cover attempt counts, by-name reevaluation, failures, timing, conditions, caps, bounds, and overflow.
- **Documentation:** README.md documents each policy and makes the external odelay scheduling boundary explicit.
- **Traceability:** A deferred Future passed to a Policy can be followed through Success classification and delay selection into the next attempt and its focused specifications.
- **Maintainability:** The implementation is compact, policy concerns are separated, and direct timing and failure tests constrain behavioral changes.
- **Educational value:** The path demonstrates asynchronous recursion and policy composition without requiring a large effect system or framework.

**Inspection record:** commit `f5d887b23adb8c34b2dc891a4d25a6263e300c48`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `retry/src/main/scala/Policy.scala`, `retry/src/main/scala/Defaults.scala`, `retry/src/main/scala/Jitter.scala`, `retry/src/main/scala/Success.scala`, `retry/src/test/scala/PolicySpec.scala`, `retry/src/test/scala/JitterSpec.scala`, `README.md`, `LICENSE`. GitHub Linguist label: Scala.

</details>

## Level 4 — Advanced

### [circe/circe](https://github.com/circe/circe)

**Language 4 / Behavior 3 / Design 3 / Constraints 4 → Level 4**

**Source:** Production software

A modular functional JSON library for Scala with immutable values, typed codecs, cursor navigation, generic derivation, parsing integrations, literals, and JSON Pointer.

**Why study it:** Circe's core decoder path shows how typed composition, immutable cursors, navigation history, and two error strategies fit together in a production functional API.

**Short context:**

- A JSON decoder traverses a cursor, produces typed values or precise failures, and can fail fast or accumulate independent errors.

**Prerequisites:**

- Readers should know Scala type classes, higher-kinded types, algebraic data types, applicative validation, recursion, and basic JSON values and fields.

**Concepts this path develops:**

- Higher-kinded Decoder type class and Cats instances.
- Recursive JSON and collection traversal.
- Fail-fast and accumulating results must remain semantically aligned.

**What you can learn:**

- Follow typed Decoder instances through HCursor success, ACursor failure and history, recursive JSON traversal, fail-fast decoding, and applicative error accumulation.

**Learning path:**

- **Goal:** Understand how Circe composes typed decoders over immutable JSON cursors while preserving navigation history and both fail-fast and accumulating error semantics.
- **Start here:** [`modules/core/shared/src/main/scala/io/circe/Decoder.scala`](https://github.com/circe/circe/blob/2fb611bb49619e4287b6ac048d2283c2781f4943/modules/core/shared/src/main/scala/io/circe/Decoder.scala) — The reviewed trace begins in Decoder.scala because it defines the typed entry points, instances, and fail-fast and accumulating application modes.
- **Then read:**
  - [`modules/core/shared/src/main/scala/io/circe/ACursor.scala`](https://github.com/circe/circe/blob/2fb611bb49619e4287b6ac048d2283c2781f4943/modules/core/shared/src/main/scala/io/circe/ACursor.scala)
  - [`modules/core/shared/src/main/scala/io/circe/HCursor.scala`](https://github.com/circe/circe/blob/2fb611bb49619e4287b6ac048d2283c2781f4943/modules/core/shared/src/main/scala/io/circe/HCursor.scala)
  - [`modules/core/shared/src/main/scala/io/circe/Json.scala`](https://github.com/circe/circe/blob/2fb611bb49619e4287b6ac048d2283c2781f4943/modules/core/shared/src/main/scala/io/circe/Json.scala)
  - [`modules/tests/shared/src/test/scala/io/circe/DecoderSuite.scala`](https://github.com/circe/circe/blob/2fb611bb49619e4287b6ac048d2283c2781f4943/modules/tests/shared/src/test/scala/io/circe/DecoderSuite.scala)
  - [`README.md`](https://github.com/circe/circe/blob/2fb611bb49619e4287b6ac048d2283c2781f4943/README.md)
  - [`LICENSE`](https://github.com/circe/circe/blob/2fb611bb49619e4287b6ac048d2283c2781f4943/LICENSE)
- **Trace:** Start with Decoder's typed entry points and instances, follow fail-fast or accumulating application through HCursor success, ACursor failure and history, recursive JSON and collection traversal, and precise DecodingFailure construction, then close those contracts in DecoderSuite. Jawn parsing and generic macro derivation are separate optional modules and are excluded from this bounded core-decoder path.

**Why this level:**

- **Language technique 4:** Advanced functional and higher-kinded abstractions recur across the entire selected decoder path without expert macro machinery.
- **Behavioral reasoning 3:** Nontrivial traversal and error state cross decoder composition, but the path remains synchronous and has no advanced resource or concurrency lifecycle.
- **Design span 3:** Several meaningful model, navigation, decoding, failure, and verification boundaries cooperate in one core module.
- **Constraint burden 4:** Error-mode parity, diagnostics, recursion, laws, and compatibility guarantees recur and interact throughout decoder implementation and tests.
- **Placement:** The four scores 4/3/3/4 sum to 14; their arithmetic mean is 3.50 and rounds half-up to Level 4. The published result is Level 4.

**License:** Apache-2.0 ([evidence 1](https://github.com/circe/circe/blob/2fb611bb49619e4287b6ac048d2283c2781f4943/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The circe organization publishes cross-platform modules and maintains versioned documentation for production JSON encoding and decoding across the Scala ecosystem.

**Language evidence:** The immutable JSON model, cursors, codecs, numeric representation, parser integrations, printing, generic derivation, literal macros, pointers, and platform modules are Scala.

**Coding relevance:**

The small JSON vocabulary is subordinate to transferable lessons in higher-kinded type classes, recursive traversal, cursor state and history, applicative error accumulation, validation, and stack-safe composition.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Decoder.scala, ACursor.scala, HCursor.scala, and Json.scala separate typed decoding, navigation failure, successful focus, and the data model.
- **Architecture:** Decoders consume immutable cursors, carry navigation history into DecodingFailure values, and compose either sequentially or applicatively.
- **Naming and idiom:** Decoder, ACursor, HCursor, Json, and DecodingFailure reveal the model while demonstrating typed functional composition and immutable traversal.
- **Tests:** DecoderSuite.scala exercises primitives, collections, products, recursion, missing fields, cursor history, fail-fast behavior, and accumulating errors.
- **Documentation:** README.md introduces Circe and its decoding model without pulling unrelated parser or derivation modules into the trace.
- **Traceability:** A JSON focus can be followed from Decoder.scala through HCursor or ACursor transitions into a typed value or history-bearing failure asserted in DecoderSuite.scala.
- **Maintainability:** The bounded core path has stable typed boundaries and direct tests, while Jawn parsing and macro derivation remain explicitly outside scope.
- **Educational value:** The path gives a concrete reason for higher-kinded and applicative abstractions by tying them to precise, testable decoding outcomes.

**Inspection record:** commit `2fb611bb49619e4287b6ac048d2283c2781f4943`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `modules/core/shared/src/main/scala/io/circe/Decoder.scala`, `modules/core/shared/src/main/scala/io/circe/ACursor.scala`, `modules/core/shared/src/main/scala/io/circe/HCursor.scala`, `modules/core/shared/src/main/scala/io/circe/Json.scala`, `modules/tests/shared/src/test/scala/io/circe/DecoderSuite.scala`, `README.md`, `LICENSE`. GitHub Linguist label: Scala.

</details>

### [http4s/http4s](https://github.com/http4s/http4s)

**Language 4 / Behavior 4 / Design 3 / Constraints 4 → Level 4**

**Source:** Production software

A purely functional, streaming HTTP toolkit for Scala with protocol types, clients, servers, routing, middleware, codecs, and the Ember network implementation.

**Why study it:** http4s makes resource ownership visible by modeling a client response as an effectful Resource whose streaming body and connection lifetime stay in one scope.

**Short context:**

- An effect-polymorphic HTTP client acquires a response as a Resource so the caller can consume a streaming body and reliably release the underlying connection.

**Prerequisites:**

- Readers should know Scala higher-kinded types, effects, Resource-style scoped ownership, streams, and basic HTTP request, response, status, and body concepts.

**Concepts this path develops:**

- Higher-kinded Client[F] and HttpApp[F] abstractions.
- Response acquisition and release lifecycle.
- Responses must be released on success, failure, and cancellation.

**What you can learn:**

- Follow Client.run, fetch, expect, status validation, body streaming, transformations, failures, and connection release through the Resource contract.

**Learning path:**

- **Goal:** Understand how http4s models a client response as an effectful Resource so streaming body consumption, errors, transformation, and connection release remain safely scoped.
- **Start here:** [`docs/docs/client.md`](https://github.com/http4s/http4s/blob/a95ed19a5d377276d1eb98d93897cea45cbad921/docs/docs/client.md) — The reviewed trace begins in the client guide because it establishes the response-ownership rule a learner must understand before reading Client.scala.
- **Then read:**
  - [`client/shared/src/main/scala/org/http4s/client/Client.scala`](https://github.com/http4s/http4s/blob/a95ed19a5d377276d1eb98d93897cea45cbad921/client/shared/src/main/scala/org/http4s/client/Client.scala)
  - [`core/shared/src/main/scala/org/http4s/HttpApp.scala`](https://github.com/http4s/http4s/blob/a95ed19a5d377276d1eb98d93897cea45cbad921/core/shared/src/main/scala/org/http4s/HttpApp.scala)
  - [`core/shared/src/main/scala/org/http4s/Message.scala`](https://github.com/http4s/http4s/blob/a95ed19a5d377276d1eb98d93897cea45cbad921/core/shared/src/main/scala/org/http4s/Message.scala)
  - [`client/shared/src/test/scala/org/http4s/client/ClientSuite.scala`](https://github.com/http4s/http4s/blob/a95ed19a5d377276d1eb98d93897cea45cbad921/client/shared/src/test/scala/org/http4s/client/ClientSuite.scala)
  - [`README.md`](https://github.com/http4s/http4s/blob/a95ed19a5d377276d1eb98d93897cea45cbad921/README.md)
  - [`LICENSE`](https://github.com/http4s/http4s/blob/a95ed19a5d377276d1eb98d93897cea45cbad921/LICENSE)
- **Trace:** Begin with the client guide's warning that a response is a managed Resource, follow Client.run, fetch, expect, status validation, and transformations through HttpApp and Message's streamed body, then close success, failure, disposal, mapping, and scoped-use behavior in ClientSuite. Ember parser, server, and protocol breadth are deliberately excluded.

**Why this level:**

- **Language technique 4:** Advanced effect-polymorphic, Resource, and stream abstractions recur throughout the bounded client path.
- **Behavioral reasoning 4:** Resource ownership, streaming evaluation, errors, transformation, and cleanup require advanced nonlocal lifecycle reasoning.
- **Design span 3:** Several meaningful documentation, client, application, message, resource, and verification boundaries cooperate.
- **Constraint burden 4:** Lifecycle, streaming, error, cancellation, API, and portability guarantees interact throughout ordinary client use.
- **Placement:** The four scores 4/4/3/4 sum to 15; their arithmetic mean is 3.75 and rounds half-up to Level 4. The published result is Level 4.

**License:** Apache-2.0 ([evidence 1](https://github.com/http4s/http4s/blob/a95ed19a5d377276d1eb98d93897cea45cbad921/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The http4s project publishes a versioned family of core, DSL, client, server, Ember, codec, and integration artifacts for production services on multiple Scala platforms.

**Language evidence:** The HTTP model, codecs, header parsers, routing DSL, client and server algebras, middleware, Ember HTTP/1 and HTTP/2 engine, WebSockets, TLS, and platform integrations are Scala.

**Coding relevance:**

The short HTTP request and response vocabulary is documented locally and remains subordinate to transferable lessons in higher-kinded interfaces, Resource ownership, streaming values, scoped use, transformation, error handling, cleanup, and contract tests.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** client.md states the ownership contract, while Client.scala, HttpApp.scala, and Message.scala separate acquisition, application, and streaming-message behavior.
- **Architecture:** Client.run acquires a response as a Resource, higher-level client methods transform or validate it, and Message carries the streamed body within that scope.
- **Naming and idiom:** Client, run, fetch, expect, HttpApp, Message, and Resource make acquisition and scoped use explicit while demonstrating effect-polymorphic Scala design.
- **Tests:** ClientSuite.scala directly exercises successful use, status failures, disposal, response mapping, transformations, and resource behavior.
- **Documentation:** docs/docs/client.md is the selected starting document because it explains why response use and release must share a Resource scope.
- **Traceability:** The documented ownership rule can be followed into Client.run and Message body handling and then closed by ClientSuite.scala's disposal and failure cases.
- **Maintainability:** Acquisition and use are encoded in types, direct client tests protect cleanup, and Ember parser and server breadth are deliberately excluded.
- **Educational value:** The path shows how a type-level resource abstraction prevents a concrete network-lifecycle error without requiring a tour of the whole server stack.

**Inspection record:** commit `a95ed19a5d377276d1eb98d93897cea45cbad921`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `docs/docs/client.md`, `client/shared/src/main/scala/org/http4s/client/Client.scala`, `core/shared/src/main/scala/org/http4s/HttpApp.scala`, `core/shared/src/main/scala/org/http4s/Message.scala`, `client/shared/src/test/scala/org/http4s/client/ClientSuite.scala`, `README.md`, `LICENSE`. GitHub Linguist label: Scala.

</details>

## Level 5 — Expert

### [typelevel/cats-effect](https://github.com/typelevel/cats-effect)

**Language 5 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

**Source:** Production software

Typelevel's pure asynchronous runtime and effect-kernel for resource-safe, cancelable, concurrent Scala applications.

**Why study it:** Cats Effect provides a complete expert trace from an IO algebra through a cancelable fiber interpreter into a fair work-stealing runtime.

**Short context:**

- An IO fiber interprets an effect algebra while coordinating asynchronous suspension, cancellation, finalization, joining, tracing, and runtime scheduling.

**Prerequisites:**

- Readers should know advanced Scala, effect algebras, fibers, continuation stacks, cancellation and finalization, atomics, work stealing, and race-sensitive concurrency tests.

**Concepts this path develops:**

- Higher-kinded effect algebra and type-class instances.
- Asynchronous suspend and resume state machine.
- Stack safety and exactly-once asynchronous resumption.

**What you can learn:**

- Trace IO tags through IOFiber's run loop, continuation stacks, asynchronous suspension, cancellation masks, finalizers, outcomes, joins, and work-stealing scheduling.

**Learning path:**

- **Goal:** Understand how Cats Effect interprets IO as a cancelable fiber and schedules it fairly on a work-stealing runtime while preserving asynchronous and finalization guarantees.
- **Start here:** [`core/shared/src/main/scala/cats/effect/IOFiber.scala`](https://github.com/typelevel/cats-effect/blob/3d4486d47a22a40ba33f822cf4adb1eccfdb4feb/core/shared/src/main/scala/cats/effect/IOFiber.scala) — The reviewed trace begins in IOFiber.scala because its interpreter run loop turns the public IO algebra into observable asynchronous, cancelable execution.
- **Then read:**
  - [`core/shared/src/main/scala/cats/effect/IO.scala`](https://github.com/typelevel/cats-effect/blob/3d4486d47a22a40ba33f822cf4adb1eccfdb4feb/core/shared/src/main/scala/cats/effect/IO.scala)
  - [`core/shared/src/main/scala/cats/effect/unsafe/IORuntime.scala`](https://github.com/typelevel/cats-effect/blob/3d4486d47a22a40ba33f822cf4adb1eccfdb4feb/core/shared/src/main/scala/cats/effect/unsafe/IORuntime.scala)
  - [`core/jvm/src/main/scala/cats/effect/unsafe/IORuntimeCompanionPlatform.scala`](https://github.com/typelevel/cats-effect/blob/3d4486d47a22a40ba33f822cf4adb1eccfdb4feb/core/jvm/src/main/scala/cats/effect/unsafe/IORuntimeCompanionPlatform.scala)
  - [`core/jvm-native/src/main/scala/cats/effect/unsafe/WorkStealingThreadPool.scala`](https://github.com/typelevel/cats-effect/blob/3d4486d47a22a40ba33f822cf4adb1eccfdb4feb/core/jvm-native/src/main/scala/cats/effect/unsafe/WorkStealingThreadPool.scala)
  - [`core/jvm-native/src/main/scala/cats/effect/unsafe/WorkerThread.scala`](https://github.com/typelevel/cats-effect/blob/3d4486d47a22a40ba33f822cf4adb1eccfdb4feb/core/jvm-native/src/main/scala/cats/effect/unsafe/WorkerThread.scala)
  - [`tests/shared/src/test/scala/cats/effect/IOFiberSuite.scala`](https://github.com/typelevel/cats-effect/blob/3d4486d47a22a40ba33f822cf4adb1eccfdb4feb/tests/shared/src/test/scala/cats/effect/IOFiberSuite.scala)
  - [`tests/jvm-native/src/test/scala/cats/effect/IOConcurrencySuite.scala`](https://github.com/typelevel/cats-effect/blob/3d4486d47a22a40ba33f822cf4adb1eccfdb4feb/tests/jvm-native/src/test/scala/cats/effect/IOConcurrencySuite.scala)
  - [`docs/core/starvation-and-tuning.md`](https://github.com/typelevel/cats-effect/blob/3d4486d47a22a40ba33f822cf4adb1eccfdb4feb/docs/core/starvation-and-tuning.md)
  - [`README.md`](https://github.com/typelevel/cats-effect/blob/3d4486d47a22a40ba33f822cf4adb1eccfdb4feb/README.md)
  - [`LICENSE.txt`](https://github.com/typelevel/cats-effect/blob/3d4486d47a22a40ba33f822cf4adb1eccfdb4feb/LICENSE.txt)
- **Trace:** Start with IOFiber's run loop and continuation stacks, map each interpreted tag back to IO's algebra, follow asynchronous suspension and resumption, cancellation masks, finalizer unwinding, outcomes and joins into IORuntime and the JVM/Native work-stealing scheduler, then close stack, race, fairness, cancellation, and error contracts in the direct suites and starvation guide.

**Why this level:**

- **Language technique 5:** Expert functional, generic, continuation, atomic, and low-level runtime techniques are pervasive across the selected fiber-to-scheduler trace.
- **Behavioral reasoning 5:** Correctness requires expert nonlocal reasoning across concurrency, scheduling, cancellation, finalization, recovery, and publication state.
- **Design span 4:** Several substantial algebra, interpreter, runtime, platform, scheduler, verification, and documentation boundaries cooperate in one coherent execution path.
- **Constraint burden 5:** Expert concurrency, lifecycle, memory-model, fairness, performance, diagnostic, and compatibility guarantees interact pervasively.
- **Placement:** The four scores 5/5/4/5 sum to 19; their arithmetic mean is 4.75 and rounds half-up to Level 5. The published result is Level 5.

**License:** Apache-2.0 ([evidence 1](https://github.com/typelevel/cats-effect/blob/3d4486d47a22a40ba33f822cf4adb1eccfdb4feb/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** Typelevel publishes the stable Cats Effect kernel, runtime, standard primitives, laws, and testkit that underpin production libraries and applications across JVM, Scala.js, and Native.

**Language evidence:** The effect type classes, IO algebra and interpreter, fibers, runtime, schedulers, queues, synchronization primitives, test control, metrics, and platform implementations are Scala.

**Coding relevance:**

Concurrency and runtime scheduling are core programming subject matter; the path directly teaches effect interpreters, manual continuation state, lock-free publication, work stealing, cancellation masks, finalizers, fairness, and race-sensitive contract testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** IO.scala defines effect nodes, IOFiber.scala contains the interpreter, and IORuntime plus the work-stealing classes make scheduling responsibilities explicit.
- **Architecture:** An IO value is interpreted by a fiber whose suspension, resumption, cancellation, and completion are scheduled through IORuntime and a work-stealing thread pool.
- **Naming and idiom:** IOFiber, IORuntime, WorkStealingThreadPool, WorkerThread, outcomes, and finalizers expose the runtime model while using advanced functional and concurrent Scala consistently.
- **Tests:** IOFiberSuite.scala and IOConcurrencySuite.scala cover stack safety, asynchronous execution, cancellation, finalizers, fairness, races, and error propagation.
- **Documentation:** starvation-and-tuning.md explains scheduler behavior and tuning, while README.md supplies project orientation.
- **Traceability:** An IO node can be followed through IOFiber's interpreter state to runtime scheduling and then to direct fiber and concurrency assertions.
- **Maintainability:** Interpreter and scheduler boundaries are explicit, critical lifecycle rules are directly tested, and the selected files exclude unrelated ecosystem modules.
- **Educational value:** The path connects high-level effect semantics to the concrete stacks, queues, cancellation masks, and workers that enforce them.

**Inspection record:** commit `3d4486d47a22a40ba33f822cf4adb1eccfdb4feb`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `core/shared/src/main/scala/cats/effect/IOFiber.scala`, `core/shared/src/main/scala/cats/effect/IO.scala`, `core/shared/src/main/scala/cats/effect/unsafe/IORuntime.scala`, `core/jvm/src/main/scala/cats/effect/unsafe/IORuntimeCompanionPlatform.scala`, `core/jvm-native/src/main/scala/cats/effect/unsafe/WorkStealingThreadPool.scala`, `core/jvm-native/src/main/scala/cats/effect/unsafe/WorkerThread.scala`, `tests/shared/src/test/scala/cats/effect/IOFiberSuite.scala`, `tests/jvm-native/src/test/scala/cats/effect/IOConcurrencySuite.scala`, `docs/core/starvation-and-tuning.md`, `README.md`, `LICENSE.txt`. GitHub Linguist label: Scala.

</details>

### [typelevel/fs2](https://github.com/typelevel/fs2)

**Language 5 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

**Source:** Production software

A compositional, effect-polymorphic streaming I/O library for Scala with resource-safe and concurrent stream processing.

**Why study it:** Understand how FS2 compiles a typed Pull program into an effect while opening and closing nested scopes, preserving resource finalizers, interruption, stack safety, and error semantics. A short stream, effect, and resource-scope primer is sufficient; the path teaches higher-kinded algebras, interpreter normalization, continuation state, effect capabilities, tree-structured resource ownership, cancellation masks, composite failures, concurrency races, and law-based tests.

**Short context:**

- A Stream is represented by a Pull program; compilation interprets that program in an effect while scopes own resources and guarantee cleanup across success, failure, cancellation, interruption, and early termination.

**Prerequisites:**

- Be fluent with advanced Scala, higher-kinded types, variance, type classes, algebraic data types, natural transformations, functional effects, Resource, cancellation, references, and property-based concurrency tests.
- A Stream is represented by a Pull program; compilation interprets that program in an effect while scopes own resources and guarantee cleanup across success, failure, cancellation, interruption, and early termination.

**Concepts this path develops:**

- Interpreting a typed `Pull` program into a target effect through normalized continuations.
- Nested scope ownership, leases, interruption, and exactly-once resource finalization.
- Stack-safe compilation with defined composition of use errors and finalizer errors.

**What you can learn:**

- Study these expert Scala mechanisms in `core/shared/src/main/scala/fs2/Compiler.scala`: higher-kinded effect parameters and type classes, a typed Pull algebra with variance and natural transformations, interpreter normalization and continuations, and capability-selected compilation targets.
- Trace these states and branches through the selected implementation: output, evaluation, bind, failure, interruption, scope open and close, acquire and release, lease, cancellation, early termination, and composite finalizer failure.
- Identify these architectural responsibilities: public Stream and Pull program representation, compiler and target effect boundary, scope tree, scoped resources and leases, interruption context, and direct algebraic, lifecycle, and race tests.
- Study these change constraints: compilation must remain stack safe, acquired resources must finalize exactly once, children cannot outlive parents, release is uncancelable, interruption must propagate without leaking work, concurrent scope mutation must be race safe, and errors from use and finalizers must retain defined composition semantics.

**Learning path:**

- **Goal:** Understand how FS2 compiles a typed Pull program into an effect while opening and closing nested scopes, preserving resource finalizers, interruption, stack safety, and error semantics.
- **Start here:** [`core/shared/src/main/scala/fs2/Compiler.scala`](https://github.com/typelevel/fs2/blob/3320f42213d00a9ec68a15273efadade5efc0ce1/core/shared/src/main/scala/fs2/Compiler.scala) — Begin with Compiler and Target because they create the root scope, choose the effect capabilities available to interpretation, and connect public compilation to Pull's internal run loop.
- **Then read:**
  - [`core/shared/src/main/scala/fs2/Pull.scala`](https://github.com/typelevel/fs2/blob/3320f42213d00a9ec68a15273efadade5efc0ce1/core/shared/src/main/scala/fs2/Pull.scala)
  - [`core/shared/src/main/scala/fs2/Stream.scala`](https://github.com/typelevel/fs2/blob/3320f42213d00a9ec68a15273efadade5efc0ce1/core/shared/src/main/scala/fs2/Stream.scala)
  - [`core/shared/src/main/scala/fs2/internal/Scope.scala`](https://github.com/typelevel/fs2/blob/3320f42213d00a9ec68a15273efadade5efc0ce1/core/shared/src/main/scala/fs2/internal/Scope.scala)
  - [`core/shared/src/main/scala/fs2/internal/ScopedResource.scala`](https://github.com/typelevel/fs2/blob/3320f42213d00a9ec68a15273efadade5efc0ce1/core/shared/src/main/scala/fs2/internal/ScopedResource.scala)
  - [`core/shared/src/main/scala/fs2/internal/InterruptContext.scala`](https://github.com/typelevel/fs2/blob/3320f42213d00a9ec68a15273efadade5efc0ce1/core/shared/src/main/scala/fs2/internal/InterruptContext.scala)
  - [`core/shared/src/test/scala/fs2/BracketSuite.scala`](https://github.com/typelevel/fs2/blob/3320f42213d00a9ec68a15273efadade5efc0ce1/core/shared/src/test/scala/fs2/BracketSuite.scala)
  - [`core/shared/src/test/scala/fs2/PullLawsSuite.scala`](https://github.com/typelevel/fs2/blob/3320f42213d00a9ec68a15273efadade5efc0ce1/core/shared/src/test/scala/fs2/PullLawsSuite.scala)
  - [`core/shared/src/test/scala/fs2/StreamInterruptSuite.scala`](https://github.com/typelevel/fs2/blob/3320f42213d00a9ec68a15273efadade5efc0ce1/core/shared/src/test/scala/fs2/StreamInterruptSuite.scala)
  - [`docs/implementation-notes.markdown`](https://github.com/typelevel/fs2/blob/3320f42213d00a9ec68a15273efadade5efc0ce1/docs/implementation-notes.markdown)
  - [`site/guide.md`](https://github.com/typelevel/fs2/blob/3320f42213d00a9ec68a15273efadade5efc0ce1/site/guide.md)
  - [`README.md`](https://github.com/typelevel/fs2/blob/3320f42213d00a9ec68a15273efadade5efc0ce1/README.md)
  - [`LICENSE`](https://github.com/typelevel/fs2/blob/3320f42213d00a9ec68a15273efadade5efc0ce1/LICENSE)
- **Trace:** Start with Compiler.Target creating a root Scope and invoking Pull.compile; follow Pull's typed nodes, binds, outputs, evaluations, failures, and scope operations through normalization and the interpreter loop; then trace Scope open, resource registration, leases, interruption contexts, uncancelable child-first close, composite failure collection, and parent unlinking; close with bracket ordering and exactly-once cleanup, pull laws and stack safety, and nested interruption and cancellation races.

**Why this level:**

- **Language technique 5:** Expert generic, functional, interpreter, effect, and concurrency mechanisms are pervasive throughout the selected compiler and scope path.
- **Behavioral reasoning 5:** Several coupled interpreter and resource state machines interact nonlocally across every normal and exceptional completion path.
- **Design span 4:** Multiple substantial API, algebra, interpreter, lifecycle, concurrency, verification, and documentation boundaries cooperate, while the trace stays inside fs2-core.
- **Constraint burden 5:** Expert type, lifecycle, concurrency, cancellation, failure, stack, performance, and compatibility guarantees constrain the entire path.
- **Placement:** The four scores 5/5/4/5 sum to 19; their arithmetic mean is 4.75 and rounds half-up to Level 5, with three dimensions scored 5. The published result is Level 5.

**License:** MIT ([evidence 1](https://github.com/typelevel/fs2/blob/3320f42213d00a9ec68a15273efadade5efc0ce1/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** Typelevel publishes fs2-core for JVM, Scala.js, and Scala Native; production libraries and applications use its Stream abstraction for effectful, resource-safe incremental processing.

**Language evidence:** The selected Stream and Pull algebras, compiler, scope tree, resource lifecycle, interruption coordination, and direct law and concurrency suites are handwritten first-party Scala under core/shared.

**Coding relevance:**

A short stream, effect, and resource-scope primer is sufficient; the path teaches higher-kinded algebras, interpreter normalization, continuation state, effect capabilities, tree-structured resource ownership, cancellation masks, composite failures, concurrency races, and law-based tests.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Compiler, Pull, Scope, ScopedResource, and InterruptContext document their roles and encode transitions in focused types and methods; the direct suites target laws, cleanup order, interruption, cancellation, and regressions.
- **Architecture:** Stream delegates to a Pull program, Compiler selects target effect capabilities and owns the root scope, the interpreter evaluates Pull nodes, and a tree of scopes owns resources, leases, interruption, and close ordering.
- **Naming and idiom:** Compiler.Target, Pull, Terminal, Scope, ScopedResource, Lease, InterruptContext, Outcome, Poll, and CompositeFailure expose the execution model while demonstrating advanced idiomatic functional Scala.
- **Tests:** BracketSuite exercises success, failure, early termination, deep nesting, LIFO release, cancellation, interruption, finalizer failure, leases, and uncancelable release; PullLawsSuite protects algebraic behavior; StreamInterruptSuite targets hung evaluations, nesting, recovery, cancellation, and race-sensitive interruption.
- **Documentation:** README.md, the public ScalaDoc, site guide, and implementation notes explain stream representation, Pull interpretation, resource safety, composition, and the implementation's continuation technique.
- **Traceability:** A compiled stream can be followed from Compiler into Pull normalization and evaluation, scope and resource transitions, interruption and close behavior, then directly into law, bracket, and interruption assertions.
- **Maintainability:** State ownership and lifecycle rules are documented beside implementation, transitions are centralized, public and internal boundaries are explicit, and regression suites exercise the most dangerous stack, cancellation, and resource races.
- **Educational value:** The bounded core path connects high-level functional streaming to the concrete typed interpreter, scope tree, references, masks, and finalizer ordering that make its guarantees real.

**Inspection record:** commit `3320f42213d00a9ec68a15273efadade5efc0ce1`, inspected 2026-08-29. Review passes: Codex primary pass; Codex cold verification pass. Files inspected: `core/shared/src/main/scala/fs2/Compiler.scala`, `core/shared/src/main/scala/fs2/Pull.scala`, `core/shared/src/main/scala/fs2/Stream.scala`, `core/shared/src/main/scala/fs2/internal/Scope.scala`, `core/shared/src/main/scala/fs2/internal/ScopedResource.scala`, `core/shared/src/main/scala/fs2/internal/InterruptContext.scala`, `core/shared/src/test/scala/fs2/BracketSuite.scala`, `core/shared/src/test/scala/fs2/PullLawsSuite.scala`, `core/shared/src/test/scala/fs2/StreamInterruptSuite.scala`, `docs/implementation-notes.markdown`, `site/guide.md`, `README.md`, `LICENSE`. GitHub Linguist label: Scala.

</details>

_Generated from `catalog/scala.json`; do not edit by hand._

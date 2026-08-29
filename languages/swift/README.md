# Swift

8 qualified repositories. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

[← All languages](../README.md)

## Level 1

No qualified repository has been published at this level. Standards are not lowered to fill a slot.

## Level 2

### [JohnSundell/Files](https://github.com/JohnSundell/Files)

**Language 2 / Behavior 2 / Design 2 / Constraints 3 → Level 2**

A small object-oriented filesystem library that wraps Foundation paths as File and Folder values.

**Real-world evidence:** The repository publishes Swift Package Manager and CocoaPods libraries used by macOS, iOS, Linux, tvOS, and watchOS code.

**Language evidence:** File and folder values, traversal, creation, copying, moving, renaming, deletion, attributes, and Foundation interoperation are implemented in Swift in Sources/Files.swift.

**Why study it:** Understand how a small Swift API turns directory traversal into lazy typed sequences over files and folders. Filesystem vocabulary is brief and subordinate; the bounded path teaches Sequence and IteratorProtocol composition, lazy traversal, filtering, value construction, and error-aware Foundation bridging.

**What you can learn:**

- Study these transferable Swift mechanisms in `Sources/Files.swift`: Sequence and IteratorProtocol conformances, lazy typed child construction, and Foundation error bridging.
- Trace these states and branches from `Sources/Files.swift` through its selected supporting files: shallow and recursive traversal, file and folder filtering, and end-of-sequence and lookup failures.
- Identify these architectural responsibilities in the path beginning at `Sources/Files.swift`: Folder sequence facade, child iterator, and FileManager-backed location model.
- Study these change constraints for the path beginning at `Sources/Files.swift`: lazy enumeration must preserve path and type identity, recursive and shallow modes must remain distinct, and filesystem errors cross the Foundation boundary.

**Prerequisites:**

- Before reading `Sources/Files.swift`, be comfortable with these mechanisms: Sequence and IteratorProtocol conformances, lazy typed child construction, and Foundation error bridging.
- Folder children are filesystem entries exposed as typed File and Folder values.

**Coding relevance:**

Filesystem vocabulary is brief and subordinate; the bounded path teaches Sequence and IteratorProtocol composition, lazy traversal, filtering, value construction, and error-aware Foundation bridging.

Required domain context:

- Folder children are filesystem entries exposed as typed File and Folder values.

**Learning path:**

- **Goal:** Understand how a small Swift API turns directory traversal into lazy typed sequences over files and folders.
- **Start here:** [`Sources/Files.swift`](https://github.com/JohnSundell/Files/blob/e85f2b4a8dfa0f242889f45236f3867d16e40480/Sources/Files.swift) — Begin with `Sources/Files.swift` because it exposes how a small Swift API turns directory traversal into lazy typed sequences over files and folders.
- **Then read:**
  - [`Tests/FilesTests/FilesTests.swift`](https://github.com/JohnSundell/Files/blob/e85f2b4a8dfa0f242889f45236f3867d16e40480/Tests/FilesTests/FilesTests.swift)
- **Trace:** Begin at Folder.ChildIterator and ChildSequence, follow FileManager enumeration into typed File or Folder values, then compare shallow, recursive, file-only, and folder-only child sequences; close with temporary-directory tests that verify iteration order, filtering, paths, and failures.

**Why this level:**

- **Language technique 2:** Familiar Swift protocol and iterator techniques recur without advanced type-level machinery.
- **Behavioral reasoning 2:** A few related traversal branches recur within one bounded iterator lifecycle.
- **Design span 2:** A small set of cohesive pieces spans the public traversal API and platform adapter.
- **Constraint burden 3:** Real filesystem state adds recurring correctness constraints, though the selected trace remains compact.
- **Placement:** The four scores 2/2/2/3 sum to 9; their arithmetic mean is 2.25 and rounds half-up to Level 2. The published result is Level 2.

**Quality-gate evidence:**

- **Source quality:** Files.swift keeps Folder.ChildIterator and ChildSequence beside the File and Folder model, and FilesTests.swift exercises real temporary-directory traversal, recursive and shallow enumeration, filtering, paths, errors, and mutations.
- **Architecture:** The audited architecture of the path beginning at `Sources/Files.swift` has these boundaries: Folder sequence facade, child iterator, and FileManager-backed location model.
- **Naming and idiom:** `Sources/Files.swift` and its supporting files use these characteristic Swift mechanisms: Sequence and IteratorProtocol conformances, lazy typed child construction, and Foundation error bridging.
- **Tests:** Direct tests in `Tests/FilesTests/FilesTests.swift` cover these states and branches in the selected path: shallow and recursive traversal, file and folder filtering, and end-of-sequence and lookup failures.
- **Documentation:** `Sources/Files.swift` and its selected supporting material document the contracts needed to understand how a small Swift API turns directory traversal into lazy typed sequences over files and folders.
- **Traceability:** Begin at Folder.ChildIterator and ChildSequence, follow FileManager enumeration into typed File or Folder values, then compare shallow, recursive, file-only, and folder-only child sequences; close with temporary-directory tests that verify iteration order, filtering, paths, and failures.
- **Maintainability:** Changes to the path beginning at `Sources/Files.swift` are constrained by these audited guarantees: lazy enumeration must preserve path and type identity, recursive and shallow modes must remain distinct, and filesystem errors cross the Foundation boundary.
- **Educational value:** Understand how a small Swift API turns directory traversal into lazy typed sequences over files and folders. Filesystem vocabulary is brief and subordinate; the bounded path teaches Sequence and IteratorProtocol composition, lazy traversal, filtering, value construction, and error-aware Foundation bridging.

**Inspection record:** commit `e85f2b4a8dfa0f242889f45236f3867d16e40480`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `Sources/Files.swift`, `Tests/FilesTests/FilesTests.swift`, `LICENSE`. GitHub Linguist label: Swift.

**License:** MIT ([evidence 1](https://github.com/JohnSundell/Files/blob/e85f2b4a8dfa0f242889f45236f3867d16e40480/LICENSE))

### [pointfreeco/swift-tagged](https://github.com/pointfreeco/swift-tagged)

**Language 4 / Behavior 1 / Design 1 / Constraints 3 → Level 2**

A tiny generic wrapper that gives otherwise identical raw values distinct compile-time identities.

**Real-world evidence:** The repository publishes Swift packages used by applications to prevent identifier and domain-value mixups without runtime overhead.

**Language evidence:** The generic tag wrapper, conditional conformances, literal support, serialization, identifiers, money, and time helpers are implemented in Swift under Sources/.

**Why study it:** Understand how Swift can give identical raw values distinct compile-time identities without adding a second runtime state machine. The tag idea needs one brief explanation; the selected path is programming-led and teaches generic wrappers, conditional conformances, dynamic-member forwarding, literal and Codable forwarding, mapping, and explicit coercion.

**What you can learn:**

- Study these transferable Swift mechanisms in `Sources/Tagged/Tagged.swift`: phantom generic tag parameter, conditional protocol conformances, and dynamic-member, literal, and Codable forwarding.
- Trace these states and branches from `Sources/Tagged/Tagged.swift` through its selected supporting files: one wrapped raw value, local forwarding operations, and no independent runtime lifecycle.
- Identify these architectural responsibilities in the path beginning at `Sources/Tagged/Tagged.swift`: one core wrapper abstraction and one direct test suite.
- Study these change constraints for the path beginning at `Sources/Tagged/Tagged.swift`: operations exist only when RawValue satisfies matching constraints, type identity must not alter raw representation, and encoding and literal behavior must preserve RawValue semantics.

**Prerequisites:**

- Before reading `Sources/Tagged/Tagged.swift`, be comfortable with these mechanisms: phantom generic tag parameter, conditional protocol conformances, and dynamic-member, literal, and Codable forwarding.
- A phantom Tag parameter distinguishes values with the same RawValue at compile time while the runtime representation remains one wrapped value.

**Coding relevance:**

The tag idea needs one brief explanation; the selected path is programming-led and teaches generic wrappers, conditional conformances, dynamic-member forwarding, literal and Codable forwarding, mapping, and explicit coercion.

Required domain context:

- A phantom Tag parameter distinguishes values with the same RawValue at compile time while the runtime representation remains one wrapped value.

**Learning path:**

- **Goal:** Understand how Swift can give identical raw values distinct compile-time identities without adding a second runtime state machine.
- **Start here:** [`Sources/Tagged/Tagged.swift`](https://github.com/pointfreeco/swift-tagged/blob/6a8517578035408b6c14ccba00ee990a1435515c/Sources/Tagged/Tagged.swift) — Begin with `Sources/Tagged/Tagged.swift` because it exposes how Swift can give identical raw values distinct compile-time identities without adding a second runtime state machine.
- **Then read:**
  - [`Tests/TaggedTests/TaggedTests.swift`](https://github.com/pointfreeco/swift-tagged/blob/6a8517578035408b6c14ccba00ee990a1435515c/Tests/TaggedTests/TaggedTests.swift)
- **Trace:** Start with Tagged's Tag and RawValue parameters and single rawValue field, then follow mapping and dynamic-member lookup into the recurring conditional conformances; close with tests that show which operations are forwarded, encoded, compared, or deliberately coerced.

**Why this level:**

- **Language technique 4:** Advanced Swift type-system techniques recur throughout the compact implementation.
- **Behavioral reasoning 1:** The main trace has one local value state, so compile-time sophistication does not raise runtime behavior above the Level 1 anchor.
- **Design span 1:** The lesson is intentionally contained in one production type and its tests.
- **Constraint burden 3:** Several type-safety and representation constraints recur, but they are compiler-enforced and locally visible.
- **Placement:** The four scores 4/1/1/3 sum to 9; their arithmetic mean is 2.25 and rounds half-up to Level 2. The published result is Level 2.

**Quality-gate evidence:**

- **Source quality:** Tagged.swift keeps the representation and conditional protocol extensions in one documented source file, while TaggedTests.swift directly covers construction, mapping, dynamic members, comparison, literals, encoding, numeric behavior, and coercion.
- **Architecture:** The audited architecture of the path beginning at `Sources/Tagged/Tagged.swift` has these boundaries: one core wrapper abstraction and one direct test suite.
- **Naming and idiom:** `Sources/Tagged/Tagged.swift` and its supporting files use these characteristic Swift mechanisms: phantom generic tag parameter, conditional protocol conformances, and dynamic-member, literal, and Codable forwarding.
- **Tests:** Direct tests in `Tests/TaggedTests/TaggedTests.swift` cover these states and branches in the selected path: one wrapped raw value, local forwarding operations, and no independent runtime lifecycle.
- **Documentation:** `Sources/Tagged/Tagged.swift` and its selected supporting material document the contracts needed to understand how Swift can give identical raw values distinct compile-time identities without adding a second runtime state machine.
- **Traceability:** Start with Tagged's Tag and RawValue parameters and single rawValue field, then follow mapping and dynamic-member lookup into the recurring conditional conformances; close with tests that show which operations are forwarded, encoded, compared, or deliberately coerced.
- **Maintainability:** Changes to the path beginning at `Sources/Tagged/Tagged.swift` are constrained by these audited guarantees: operations exist only when RawValue satisfies matching constraints, type identity must not alter raw representation, and encoding and literal behavior must preserve RawValue semantics.
- **Educational value:** Understand how Swift can give identical raw values distinct compile-time identities without adding a second runtime state machine. The tag idea needs one brief explanation; the selected path is programming-led and teaches generic wrappers, conditional conformances, dynamic-member forwarding, literal and Codable forwarding, mapping, and explicit coercion.

**Inspection record:** commit `6a8517578035408b6c14ccba00ee990a1435515c`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `Sources/Tagged/Tagged.swift`, `Tests/TaggedTests/TaggedTests.swift`, `LICENSE`. GitHub Linguist label: Swift.

**License:** MIT ([evidence 1](https://github.com/pointfreeco/swift-tagged/blob/6a8517578035408b6c14ccba00ee990a1435515c/LICENSE))

## Level 3

### [apple/swift-log](https://github.com/apple/swift-log)

**Language 3 / Behavior 3 / Design 3 / Constraints 4 → Level 3**

The Swift server ecosystem's vendor-neutral logging API with pluggable backends and structured metadata.

**Real-world evidence:** The project publishes the Logging package used by Swift libraries and applications to share a stable logging abstraction across backend implementations.

**Language evidence:** Logger values, levels, messages, metadata, backend protocols, global bootstrap, multiplexing, streams, concurrency safety, and testing handlers are Swift under Sources/.

**Why study it:** Understand how a stable Swift logging facade lazily filters calls and delegates them to replaceable backends with one-time global setup. Logging concepts are familiar and quickly defined; the path teaches protocol-backed adapters, value semantics around an existential handler, autoclosure laziness, metadata merging, process-wide bootstrap, and concurrency-safe setup.

**What you can learn:**

- Study these transferable Swift mechanisms in `Sources/Logging/Logger.swift`: protocol existential backend, autoclosure-based lazy messages, and value facade with Sendable-aware mutation.
- Trace these states and branches from `Sources/Logging/Logger.swift` through its selected supporting files: level filtering before message construction, metadata precedence and handler mutation, and initial and bootstrapped factory states.
- Identify these architectural responsibilities in the path beginning at `Sources/Logging/Logger.swift`: Logger facade, LogHandler extension boundary, and LoggingSystem bootstrap and focused tests.
- Study these change constraints for the path beginning at `Sources/Logging/Logger.swift`: messages must stay lazy below the active level, metadata precedence and source attribution must remain stable, and global bootstrap must be concurrency-safe and effectively one-time.

**Prerequisites:**

- Before reading `Sources/Logging/Logger.swift`, be comfortable with these mechanisms: protocol existential backend, autoclosure-based lazy messages, and value facade with Sendable-aware mutation.
- A Logger filters a level, combines structured metadata, and delegates emission to a configured LogHandler.

**Coding relevance:**

Logging concepts are familiar and quickly defined; the path teaches protocol-backed adapters, value semantics around an existential handler, autoclosure laziness, metadata merging, process-wide bootstrap, and concurrency-safe setup.

Required domain context:

- A Logger filters a level, combines structured metadata, and delegates emission to a configured LogHandler.

**Learning path:**

- **Goal:** Understand how a stable Swift logging facade lazily filters calls and delegates them to replaceable backends with one-time global setup.
- **Start here:** [`Sources/Logging/Logger.swift`](https://github.com/apple/swift-log/blob/47a917767fde0cd7f5b5dfdabbec733d2cb2dd95/Sources/Logging/Logger.swift) — Begin with `Sources/Logging/Logger.swift` because it exposes how a stable Swift logging facade lazily filters calls and delegates them to replaceable backends with one-time global setup.
- **Then read:**
  - [`Sources/Logging/LogHandler.swift`](https://github.com/apple/swift-log/blob/47a917767fde0cd7f5b5dfdabbec733d2cb2dd95/Sources/Logging/LogHandler.swift)
  - [`Sources/Logging/LoggingSystem.swift`](https://github.com/apple/swift-log/blob/47a917767fde0cd7f5b5dfdabbec733d2cb2dd95/Sources/Logging/LoggingSystem.swift)
  - [`Tests/LoggingTests/LoggingTest.swift`](https://github.com/apple/swift-log/blob/47a917767fde0cd7f5b5dfdabbec733d2cb2dd95/Tests/LoggingTests/LoggingTest.swift)
  - [`Tests/LoggingTests/GlobalLoggingTest.swift`](https://github.com/apple/swift-log/blob/47a917767fde0cd7f5b5dfdabbec733d2cb2dd95/Tests/LoggingTests/GlobalLoggingTest.swift)
  - [`Sources/Logging/Docs.docc/UnderstandingLoggers.md`](https://github.com/apple/swift-log/blob/47a917767fde0cd7f5b5dfdabbec733d2cb2dd95/Sources/Logging/Docs.docc/UnderstandingLoggers.md)
- **Trace:** Start at Logger.log and convenience methods, follow level filtering before autoclosure materialization and metadata combination into LogHandler.log, then trace LoggingSystem bootstrap into the handler factory; close with direct call-site and global-bootstrap tests plus the conceptual guide.

**Why this level:**

- **Language technique 3:** Several intermediate Swift techniques recur across the facade and backend boundary.
- **Behavioral reasoning 3:** Multiple related states and branches recur but remain bounded to one logging pipeline.
- **Design span 3:** A few cohesive components form the complete producer-to-backend trace.
- **Constraint burden 4:** Performance, compatibility, and process-wide concurrency guarantees recur in ordinary use.
- **Placement:** The four scores 3/3/3/4 sum to 13; their arithmetic mean is 3.25 and rounds half-up to Level 3. The published result is Level 3.

**Quality-gate evidence:**

- **Source quality:** Logger and LogHandler document producer and backend contracts, LoggingSystem isolates one-time factory bootstrap, focused logging and global-bootstrap tests cover filtering, laziness, metadata, mutation, concurrency, and repeated setup, and UnderstandingLoggers.md explains the model.
- **Architecture:** The audited architecture of the path beginning at `Sources/Logging/Logger.swift` has these boundaries: Logger facade, LogHandler extension boundary, and LoggingSystem bootstrap and focused tests.
- **Naming and idiom:** `Sources/Logging/Logger.swift` and its supporting files use these characteristic Swift mechanisms: protocol existential backend, autoclosure-based lazy messages, and value facade with Sendable-aware mutation.
- **Tests:** Direct tests in `Tests/LoggingTests/LoggingTest.swift` and `Tests/LoggingTests/GlobalLoggingTest.swift` cover these states and branches in the selected path: level filtering before message construction, metadata precedence and handler mutation, and initial and bootstrapped factory states.
- **Documentation:** `Sources/Logging/Logger.swift` and its selected supporting material document the contracts needed to understand how a stable Swift logging facade lazily filters calls and delegates them to replaceable backends with one-time global setup.
- **Traceability:** Start at Logger.log and convenience methods, follow level filtering before autoclosure materialization and metadata combination into LogHandler.log, then trace LoggingSystem bootstrap into the handler factory; close with direct call-site and global-bootstrap tests plus the conceptual guide.
- **Maintainability:** Changes to the path beginning at `Sources/Logging/Logger.swift` are constrained by these audited guarantees: messages must stay lazy below the active level, metadata precedence and source attribution must remain stable, and global bootstrap must be concurrency-safe and effectively one-time.
- **Educational value:** Understand how a stable Swift logging facade lazily filters calls and delegates them to replaceable backends with one-time global setup. Logging concepts are familiar and quickly defined; the path teaches protocol-backed adapters, value semantics around an existential handler, autoclosure laziness, metadata merging, process-wide bootstrap, and concurrency-safe setup.

**Inspection record:** commit `47a917767fde0cd7f5b5dfdabbec733d2cb2dd95`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `Sources/Logging/Logger.swift`, `Sources/Logging/LogHandler.swift`, `Sources/Logging/LoggingSystem.swift`, `Tests/LoggingTests/LoggingTest.swift`, `Tests/LoggingTests/GlobalLoggingTest.swift`, `Sources/Logging/Docs.docc/UnderstandingLoggers.md`, `LICENSE.txt`. GitHub Linguist label: Swift.

**License:** Apache-2.0 ([evidence 1](https://github.com/apple/swift-log/blob/47a917767fde0cd7f5b5dfdabbec733d2cb2dd95/LICENSE.txt))

### [vapor/vapor](https://github.com/vapor/vapor)

**Language 3 / Behavior 3 / Design 3 / Constraints 3 → Level 3**

A server-side Swift web framework built on SwiftNIO with routing, middleware, content, authentication, sessions, clients, and operational integrations.

**Real-world evidence:** The repository publishes the Vapor package used to build and run production HTTP and WebSocket services in Swift.

**Language evidence:** Application lifecycle, routing, requests and responses, middleware, content coding, authentication, sessions, clients, servers, WebSockets, validation, views, caching, tracing, metrics, and testing are Swift under Sources/.

**Why study it:** Understand how Vapor builds an ordered middleware chain around a terminal responder and preserves request, response, and error flow. HTTP request and response vocabulary is brief; the path is programming-led and teaches protocol composition, responder wrapping, ordered configuration, type erasure, error propagation, and direct integration testing.

**What you can learn:**

- Study these transferable Swift mechanisms in `Sources/Vapor/Middleware/Middleware.swift`: protocol-based middleware and responder contracts, closure and type-erased composition, and asynchronous response values.
- Trace these states and branches from `Sources/Vapor/Middleware/Middleware.swift` through its selected supporting files: ordered before and after behavior, continue, transform, short-circuit, and error branches, and terminal responder completion.
- Identify these architectural responsibilities in the path beginning at `Sources/Vapor/Middleware/Middleware.swift`: middleware extension point, ordered configuration, and application assembly and terminal responder.
- Study these change constraints for the path beginning at `Sources/Vapor/Middleware/Middleware.swift`: configured order must be preserved, each layer must invoke or intentionally bypass the next responder, and responses and errors must propagate through the chain.

**Prerequisites:**

- Before reading `Sources/Vapor/Middleware/Middleware.swift`, be comfortable with these mechanisms: protocol-based middleware and responder contracts, closure and type-erased composition, and asynchronous response values.
- Middleware wraps an HTTP Responder so request handling can be composed as an ordered chain.

**Coding relevance:**

HTTP request and response vocabulary is brief; the path is programming-led and teaches protocol composition, responder wrapping, ordered configuration, type erasure, error propagation, and direct integration testing.

Required domain context:

- Middleware wraps an HTTP Responder so request handling can be composed as an ordered chain.

**Learning path:**

- **Goal:** Understand how Vapor builds an ordered middleware chain around a terminal responder and preserves request, response, and error flow.
- **Start here:** [`Sources/Vapor/Middleware/Middleware.swift`](https://github.com/vapor/vapor/blob/86ab4300efa1b3e270eeba2ca4b253998b734669/Sources/Vapor/Middleware/Middleware.swift) — Begin with `Sources/Vapor/Middleware/Middleware.swift` because it exposes how Vapor builds an ordered middleware chain around a terminal responder and preserves request, response, and error flow.
- **Then read:**
  - [`Sources/Vapor/Middleware/MiddlewareConfiguration.swift`](https://github.com/vapor/vapor/blob/86ab4300efa1b3e270eeba2ca4b253998b734669/Sources/Vapor/Middleware/MiddlewareConfiguration.swift)
  - [`Sources/Vapor/Middleware/Application+Middleware.swift`](https://github.com/vapor/vapor/blob/86ab4300efa1b3e270eeba2ca4b253998b734669/Sources/Vapor/Middleware/Application%2BMiddleware.swift)
  - [`Sources/Vapor/HTTP/Responder.swift`](https://github.com/vapor/vapor/blob/86ab4300efa1b3e270eeba2ca4b253998b734669/Sources/Vapor/HTTP/Responder.swift)
  - [`Tests/VaporTests/MiddlewareTests.swift`](https://github.com/vapor/vapor/blob/86ab4300efa1b3e270eeba2ca4b253998b734669/Tests/VaporTests/MiddlewareTests.swift)
- **Trace:** Start with Middleware.respond(to:chainingTo:), follow configuration order as middleware wraps the next Responder, then trace the application-built chain into its terminal responder; close with tests for execution order, transformed responses, short circuits, and propagated failures.

**Why this level:**

- **Language technique 3:** Intermediate Swift protocol and composition techniques recur across the chain.
- **Behavioral reasoning 3:** Several related chain states recur without a broad independent lifecycle.
- **Design span 3:** A few cohesive components cover the complete composition path.
- **Constraint burden 3:** Composition and propagation constraints recur but are locally inspectable and directly tested.
- **Placement:** The four scores 3/3/3/3 sum to 12; their arithmetic mean is 3.00 and rounds half-up to Level 3. The published result is Level 3.

**Quality-gate evidence:**

- **Source quality:** Middleware.swift defines the extension contract, MiddlewareConfiguration owns ordering, Application+Middleware connects configured middleware to the application, Responder defines the terminal boundary, and MiddlewareTests verifies order, short-circuiting, errors, and composition.
- **Architecture:** The audited architecture of the path beginning at `Sources/Vapor/Middleware/Middleware.swift` has these boundaries: middleware extension point, ordered configuration, and application assembly and terminal responder.
- **Naming and idiom:** `Sources/Vapor/Middleware/Middleware.swift` and its supporting files use these characteristic Swift mechanisms: protocol-based middleware and responder contracts, closure and type-erased composition, and asynchronous response values.
- **Tests:** Direct tests in `Tests/VaporTests/MiddlewareTests.swift` cover these states and branches in the selected path: ordered before and after behavior, continue, transform, short-circuit, and error branches, and terminal responder completion.
- **Documentation:** `Sources/Vapor/Middleware/Middleware.swift` and its selected supporting material document the contracts needed to understand how Vapor builds an ordered middleware chain around a terminal responder and preserves request, response, and error flow.
- **Traceability:** Start with Middleware.respond(to:chainingTo:), follow configuration order as middleware wraps the next Responder, then trace the application-built chain into its terminal responder; close with tests for execution order, transformed responses, short circuits, and propagated failures.
- **Maintainability:** Changes to the path beginning at `Sources/Vapor/Middleware/Middleware.swift` are constrained by these audited guarantees: configured order must be preserved, each layer must invoke or intentionally bypass the next responder, and responses and errors must propagate through the chain.
- **Educational value:** Understand how Vapor builds an ordered middleware chain around a terminal responder and preserves request, response, and error flow. HTTP request and response vocabulary is brief; the path is programming-led and teaches protocol composition, responder wrapping, ordered configuration, type erasure, error propagation, and direct integration testing.

**Inspection record:** commit `86ab4300efa1b3e270eeba2ca4b253998b734669`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `Sources/Vapor/Middleware/Middleware.swift`, `Sources/Vapor/Middleware/MiddlewareConfiguration.swift`, `Sources/Vapor/Middleware/Application+Middleware.swift`, `Sources/Vapor/HTTP/Responder.swift`, `Tests/VaporTests/MiddlewareTests.swift`, `LICENSE`. GitHub Linguist label: Swift.

**License:** MIT ([evidence 1](https://github.com/vapor/vapor/blob/86ab4300efa1b3e270eeba2ca4b253998b734669/LICENSE))

## Level 4

### [Alamofire/Alamofire](https://github.com/Alamofire/Alamofire)

**Language 3 / Behavior 4 / Design 4 / Constraints 4 → Level 4**

An HTTP networking library for Apple platforms built over URLSession with fluent, async, Combine, streaming, and WebSocket APIs.

**Real-world evidence:** The repository releases Alamofire through Swift Package Manager and CocoaPods for production iOS, macOS, tvOS, watchOS, and visionOS applications.

**Language evidence:** Session management, requests, uploads, downloads, streams, WebSockets, serialization, validation, authentication, retries, trust evaluation, reachability, and event monitoring are Swift under Source/.

**Why study it:** Understand how Alamofire coordinates one request's task completion, interceptor decision, retry, cancellation, and final cleanup. HTTP and URLSession context is brief; the bounded path teaches synchronized mutable state, callback-to-task coordination, adapter and retrier boundaries, cancellation, completion ordering, and cleanup.

**What you can learn:**

- Study these transferable Swift mechanisms in `Source/Core/Request.swift`: closure and protocol-based interceptor callbacks, synchronized mutable request state, and typed request and task coordination.
- Trace these states and branches from `Source/Core/Request.swift` through its selected supporting files: created, resumed, suspended, cancelled, completed, and retried states, delegate callback and interceptor decision ordering, and success, failure, retry, cancellation, and invalidation branches.
- Identify these architectural responsibilities in the path beginning at `Source/Core/Request.swift`: Request state owner, Session task coordinator, task map and delegate bridge, and interceptor extension point and integration tests.
- Study these change constraints for the path beginning at `Source/Core/Request.swift`: callbacks must serialize state transitions, retry must not leak or duplicate URLSession tasks, and cancellation, invalidation, and completion cleanup must remain ordered.

**Prerequisites:**

- Before reading `Source/Core/Request.swift`, be comfortable with these mechanisms: closure and protocol-based interceptor callbacks, synchronized mutable request state, and typed request and task coordination.
- A Request owns a URLSession task lifecycle and may consult a RequestInterceptor before retrying a completed attempt.

**Coding relevance:**

HTTP and URLSession context is brief; the bounded path teaches synchronized mutable state, callback-to-task coordination, adapter and retrier boundaries, cancellation, completion ordering, and cleanup.

Required domain context:

- A Request owns a URLSession task lifecycle and may consult a RequestInterceptor before retrying a completed attempt.

**Learning path:**

- **Goal:** Understand how Alamofire coordinates one request's task completion, interceptor decision, retry, cancellation, and final cleanup.
- **Start here:** [`Source/Core/Request.swift`](https://github.com/Alamofire/Alamofire/blob/0455bfb650893e86ad07ace16e5f2d36dadf46f4/Source/Core/Request.swift) — Begin with `Source/Core/Request.swift` because it exposes how Alamofire coordinates one request's task completion, interceptor decision, retry, cancellation, and final cleanup.
- **Then read:**
  - [`Source/Core/Session.swift`](https://github.com/Alamofire/Alamofire/blob/0455bfb650893e86ad07ace16e5f2d36dadf46f4/Source/Core/Session.swift)
  - [`Source/Core/RequestTaskMap.swift`](https://github.com/Alamofire/Alamofire/blob/0455bfb650893e86ad07ace16e5f2d36dadf46f4/Source/Core/RequestTaskMap.swift)
  - [`Source/Core/SessionDelegate.swift`](https://github.com/Alamofire/Alamofire/blob/0455bfb650893e86ad07ace16e5f2d36dadf46f4/Source/Core/SessionDelegate.swift)
  - [`Source/Features/RequestInterceptor.swift`](https://github.com/Alamofire/Alamofire/blob/0455bfb650893e86ad07ace16e5f2d36dadf46f4/Source/Features/RequestInterceptor.swift)
  - [`Tests/SessionTests.swift`](https://github.com/Alamofire/Alamofire/blob/0455bfb650893e86ad07ace16e5f2d36dadf46f4/Tests/SessionTests.swift)
- **Trace:** Start at Request completion and retry handling, follow state changes and interceptor decisions into Session task creation, RequestTaskMap ownership, and SessionDelegate callbacks, then return through retry or terminal cleanup; close with Session tests for successful completion, cancellation, retry, invalidation, and task-map removal.

**Why this level:**

- **Language technique 3:** Intermediate Swift abstraction and synchronization techniques recur without requiring multiple expert language mechanisms.
- **Behavioral reasoning 4:** Several coupled asynchronous states and branches recur throughout the bounded request lifecycle.
- **Design span 4:** Multiple cohesive components participate in one end-to-end retry and completion path.
- **Constraint burden 4:** Concurrency, lifecycle, and cleanup constraints recur, but the lesson does not require the whole networking framework.
- **Placement:** The four scores 3/4/4/4 sum to 15; their arithmetic mean is 3.75 and rounds half-up to Level 4. The published result is Level 4.

**Quality-gate evidence:**

- **Source quality:** Request.swift documents and centralizes request state, completion, cancellation, and retry; Session, RequestTaskMap, SessionDelegate, and RequestInterceptor expose the coordinating boundaries, and SessionTests exercises task creation, completion, cancellation, retry, invalidation, and cleanup.
- **Architecture:** The audited architecture of the path beginning at `Source/Core/Request.swift` has these boundaries: Request state owner, Session task coordinator, task map and delegate bridge, and interceptor extension point and integration tests.
- **Naming and idiom:** `Source/Core/Request.swift` and its supporting files use these characteristic Swift mechanisms: closure and protocol-based interceptor callbacks, synchronized mutable request state, and typed request and task coordination.
- **Tests:** Direct tests in `Tests/SessionTests.swift` cover these states and branches in the selected path: created, resumed, suspended, cancelled, completed, and retried states, delegate callback and interceptor decision ordering, and success, failure, retry, cancellation, and invalidation branches.
- **Documentation:** `Source/Core/Request.swift` and its selected supporting material document the contracts needed to understand how Alamofire coordinates one request's task completion, interceptor decision, retry, cancellation, and final cleanup.
- **Traceability:** Start at Request completion and retry handling, follow state changes and interceptor decisions into Session task creation, RequestTaskMap ownership, and SessionDelegate callbacks, then return through retry or terminal cleanup; close with Session tests for successful completion, cancellation, retry, invalidation, and task-map removal.
- **Maintainability:** Changes to the path beginning at `Source/Core/Request.swift` are constrained by these audited guarantees: callbacks must serialize state transitions, retry must not leak or duplicate URLSession tasks, and cancellation, invalidation, and completion cleanup must remain ordered.
- **Educational value:** Understand how Alamofire coordinates one request's task completion, interceptor decision, retry, cancellation, and final cleanup. HTTP and URLSession context is brief; the bounded path teaches synchronized mutable state, callback-to-task coordination, adapter and retrier boundaries, cancellation, completion ordering, and cleanup.

**Inspection record:** commit `0455bfb650893e86ad07ace16e5f2d36dadf46f4`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `Source/Core/Request.swift`, `Source/Core/Session.swift`, `Source/Core/RequestTaskMap.swift`, `Source/Core/SessionDelegate.swift`, `Source/Features/RequestInterceptor.swift`, `Tests/SessionTests.swift`, `LICENSE`. GitHub Linguist label: Swift.

**License:** MIT ([evidence 1](https://github.com/Alamofire/Alamofire/blob/0455bfb650893e86ad07ace16e5f2d36dadf46f4/LICENSE))

### [realm/SwiftLint](https://github.com/realm/SwiftLint)

**Language 4 / Behavior 3 / Design 3 / Constraints 4 → Level 4**

A configurable Swift style and static-analysis tool with hundreds of rules, autocorrection, baselines, reporters, and build integrations.

**Real-world evidence:** The repository releases the SwiftLint command, frameworks, package plugins, and build-tool integrations used by Swift projects and CI systems.

**Language evidence:** Rule protocols and implementations, SwiftSyntax and SourceKit analysis, configuration, corrections, baselines, caching, reporters, file discovery, command execution, plugins, and macros are Swift under Source/ and Plugins/.

**Why study it:** Understand how one SwiftLint rule detects and safely corrects unsorted import blocks while preserving source structure and configuration. Lint-rule vocabulary is brief and the code remains programming-led; the path teaches SwiftSyntax visitors and rewriters, macros, configurable comparison, source trivia preservation, disabled-region handling, correction accounting, generated tests, and reusable test helpers.

**What you can learn:**

- Study these transferable Swift mechanisms in `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift`: SwiftSyntax visitor and rewriter subclasses, macro-generated rule conformance, and typed syntax and trivia transformations.
- Trace these states and branches from `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift` through its selected supporting files: collect, group, compare, report, and rewrite phases, adjacent, conditional-compilation, disabled-region, and trivia branches, and violation and correction outcomes.
- Identify these architectural responsibilities in the path beginning at `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift`: built-in rule implementation, shared visitor and correction protocols, and macro integration and generated test harness.
- Study these change constraints for the path beginning at `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift`: sorting must respect configured grouping and case behavior, comments, trivia, conditional blocks, and disabled regions must survive correction, and reported positions and correction counts must remain stable.

**Prerequisites:**

- Before reading `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift`, be comfortable with these mechanisms: SwiftSyntax visitor and rewriter subclasses, macro-generated rule conformance, and typed syntax and trivia transformations.
- The sorted_imports rule groups adjacent Swift import declarations, reports inversions, and rewrites each block into configured order.

**Coding relevance:**

Lint-rule vocabulary is brief and the code remains programming-led; the path teaches SwiftSyntax visitors and rewriters, macros, configurable comparison, source trivia preservation, disabled-region handling, correction accounting, generated tests, and reusable test helpers.

Required domain context:

- The sorted_imports rule groups adjacent Swift import declarations, reports inversions, and rewrites each block into configured order.

**Learning path:**

- **Goal:** Understand how one SwiftLint rule detects and safely corrects unsorted import blocks while preserving source structure and configuration.
- **Start here:** [`Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift`](https://github.com/realm/SwiftLint/blob/29d5c2b0484c9cf52d9745402160e59b7741b1db/Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift) — Begin with `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift` because it exposes how one SwiftLint rule detects and safely corrects unsorted import blocks while preserving source structure and configuration.
- **Then read:**
  - [`Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRuleExamples.swift`](https://github.com/realm/SwiftLint/blob/29d5c2b0484c9cf52d9745402160e59b7741b1db/Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRuleExamples.swift)
  - [`Source/SwiftLintBuiltInRules/Rules/RuleConfigurations/SortedImportsConfiguration.swift`](https://github.com/realm/SwiftLint/blob/29d5c2b0484c9cf52d9745402160e59b7741b1db/Source/SwiftLintBuiltInRules/Rules/RuleConfigurations/SortedImportsConfiguration.swift)
  - [`Source/SwiftLintCore/Protocols/SwiftSyntaxCorrectableRule.swift`](https://github.com/realm/SwiftLint/blob/29d5c2b0484c9cf52d9745402160e59b7741b1db/Source/SwiftLintCore/Protocols/SwiftSyntaxCorrectableRule.swift)
  - [`Source/SwiftLintCore/Visitors/ViolationsSyntaxVisitor.swift`](https://github.com/realm/SwiftLint/blob/29d5c2b0484c9cf52d9745402160e59b7741b1db/Source/SwiftLintCore/Visitors/ViolationsSyntaxVisitor.swift)
  - [`Source/SwiftLintCoreMacros/SwiftSyntaxRule.swift`](https://github.com/realm/SwiftLint/blob/29d5c2b0484c9cf52d9745402160e59b7741b1db/Source/SwiftLintCoreMacros/SwiftSyntaxRule.swift)
  - [`Tests/GeneratedTests/GeneratedTests_08.swift`](https://github.com/realm/SwiftLint/blob/29d5c2b0484c9cf52d9745402160e59b7741b1db/Tests/GeneratedTests/GeneratedTests_08.swift)
  - [`Tests/TestHelpers/TestHelpers.swift`](https://github.com/realm/SwiftLint/blob/29d5c2b0484c9cf52d9745402160e59b7741b1db/Tests/TestHelpers/TestHelpers.swift)
- **Trace:** Start with the rule's visitor collecting adjacent ImportDeclSyntax nodes and reporting inversions, then follow the rewriter's block sorting, configuration, disabled regions, trivia preservation, and correction count through shared visitor and macro machinery; close with examples and generated rule tests.

**Why this level:**

- **Language technique 4:** Advanced compiler-tooling and source-rewriting techniques recur across the rule lifecycle.
- **Behavioral reasoning 3:** Several related rule states recur, but they remain bounded to one syntax transformation.
- **Design span 3:** A few clear components connect one rule to reusable infrastructure and direct tests.
- **Constraint burden 4:** Source-preservation and diagnostic correctness constraints recur across detection and correction.
- **Placement:** The four scores 4/3/3/4 sum to 14; their arithmetic mean is 3.50 and rounds half-up to Level 4. The published result is Level 4.

**Quality-gate evidence:**

- **Source quality:** SortedImportsRule.swift contains a focused visitor and rewriter, its examples and configuration define observable contracts, the core visitor and correctable-rule protocols plus macro expose integration mechanics, and generated tests and TestHelpers close the rule's violation and correction path.
- **Architecture:** The audited architecture of the path beginning at `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift` has these boundaries: built-in rule implementation, shared visitor and correction protocols, and macro integration and generated test harness.
- **Naming and idiom:** `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift` and its supporting files use these characteristic Swift mechanisms: SwiftSyntax visitor and rewriter subclasses, macro-generated rule conformance, and typed syntax and trivia transformations.
- **Tests:** `Tests/GeneratedTests/GeneratedTests_08.swift` runs the sorted-imports examples as violation and correction cases, while `Tests/TestHelpers/TestHelpers.swift` supplies the shared harness rather than an independent rule suite.
- **Documentation:** `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift` and its selected supporting material document the contracts needed to understand how one SwiftLint rule detects and safely corrects unsorted import blocks while preserving source structure and configuration.
- **Traceability:** Start with the rule's visitor collecting adjacent ImportDeclSyntax nodes and reporting inversions, then follow the rewriter's block sorting, configuration, disabled regions, trivia preservation, and correction count through shared visitor and macro machinery; close with examples and generated rule tests.
- **Maintainability:** Changes to the path beginning at `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift` are constrained by these audited guarantees: sorting must respect configured grouping and case behavior, comments, trivia, conditional blocks, and disabled regions must survive correction, and reported positions and correction counts must remain stable.
- **Educational value:** Understand how one SwiftLint rule detects and safely corrects unsorted import blocks while preserving source structure and configuration. Lint-rule vocabulary is brief and the code remains programming-led; the path teaches SwiftSyntax visitors and rewriters, macros, configurable comparison, source trivia preservation, disabled-region handling, correction accounting, generated tests, and reusable test helpers.

**Inspection record:** commit `29d5c2b0484c9cf52d9745402160e59b7741b1db`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift`, `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRuleExamples.swift`, `Source/SwiftLintBuiltInRules/Rules/RuleConfigurations/SortedImportsConfiguration.swift`, `Source/SwiftLintCore/Protocols/SwiftSyntaxCorrectableRule.swift`, `Source/SwiftLintCore/Visitors/ViolationsSyntaxVisitor.swift`, `Source/SwiftLintCoreMacros/SwiftSyntaxRule.swift`, `Tests/GeneratedTests/GeneratedTests_08.swift`, `Tests/TestHelpers/TestHelpers.swift`, `LICENSE`. GitHub Linguist label: Swift.

**License:** MIT ([evidence 1](https://github.com/realm/SwiftLint/blob/29d5c2b0484c9cf52d9745402160e59b7741b1db/LICENSE))

## Level 5

### [apple/swift-nio](https://github.com/apple/swift-nio)

**Language 5 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

A cross-platform high-performance event-driven networking framework for building protocol servers and clients in Swift.

**Real-world evidence:** The project publishes the core SwiftNIO packages that underpin production server frameworks, protocol libraries, and network clients across the Swift ecosystem.

**Language evidence:** Event loops, channels and pipelines, futures, byte buffers, sockets, selectors, bootstraps, HTTP/1, WebSockets, TLS abstractions, async sequences, and filesystem APIs are primarily Swift under Sources/.

**Why study it:** Understand how SwiftNIO completes, transforms, combines, and bridges futures while preserving event-loop affinity and callback ordering. Event-loop vocabulary is explained once; the path teaches advanced generic future and promise APIs, callback scheduling, event-loop affinity, cascading, aggregation, cancellation and failure propagation, async interoperation, and concurrency invariants.

**What you can learn:**

- Study these transferable Swift mechanisms in `Sources/NIOCore/EventLoopFuture.swift`: deep generic future and promise composition, Sendable and concurrency-aware callback APIs, and async-await bridging with performance-sensitive specialization.
- Trace these states and branches from `Sources/NIOCore/EventLoopFuture.swift` through its selected supporting files: pending and completed success or failure states, scheduled callback, cascade, aggregate, and cancellation behavior, and cross-thread submission and event-loop-affine execution.
- Identify these architectural responsibilities in the path beginning at `Sources/NIOCore/EventLoopFuture.swift`: future and promise core, EventLoop execution contract, async compatibility policy, and large focused regression suite.
- Study these change constraints for the path beginning at `Sources/NIOCore/EventLoopFuture.swift`: callbacks must execute on the owning event loop, completion must be exactly once with ordered propagation, and thread safety, cancellation, failure, and allocation costs must remain controlled.

**Prerequisites:**

- Before reading `Sources/NIOCore/EventLoopFuture.swift`, be comfortable with these mechanisms: deep generic future and promise composition, Sendable and concurrency-aware callback APIs, and async-await bridging with performance-sensitive specialization.
- EventLoopFuture represents a result whose callbacks and transformations are confined to an EventLoop.

**Coding relevance:**

Event-loop vocabulary is explained once; the path teaches advanced generic future and promise APIs, callback scheduling, event-loop affinity, cascading, aggregation, cancellation and failure propagation, async interoperation, and concurrency invariants.

Required domain context:

- EventLoopFuture represents a result whose callbacks and transformations are confined to an EventLoop.

**Learning path:**

- **Goal:** Understand how SwiftNIO completes, transforms, combines, and bridges futures while preserving event-loop affinity and callback ordering.
- **Start here:** [`Sources/NIOCore/EventLoopFuture.swift`](https://github.com/apple/swift-nio/blob/a931f2c1de8dd49381ce3bf2e279d033f68d8865/Sources/NIOCore/EventLoopFuture.swift) — Begin with `Sources/NIOCore/EventLoopFuture.swift` because it exposes how SwiftNIO completes, transforms, combines, and bridges futures while preserving event-loop affinity and callback ordering.
- **Then read:**
  - [`Sources/NIOCore/EventLoop.swift`](https://github.com/apple/swift-nio/blob/a931f2c1de8dd49381ce3bf2e279d033f68d8865/Sources/NIOCore/EventLoop.swift)
  - [`Tests/NIOPosixTests/EventLoopFutureTest.swift`](https://github.com/apple/swift-nio/blob/a931f2c1de8dd49381ce3bf2e279d033f68d8865/Tests/NIOPosixTests/EventLoopFutureTest.swift)
  - [`docs/public-async-nio-apis.md`](https://github.com/apple/swift-nio/blob/a931f2c1de8dd49381ce3bf2e279d033f68d8865/docs/public-async-nio-apis.md)
- **Trace:** Begin with EventLoopFuture and Promise completion, follow map, flatMap, cascade, and aggregate operations through event-loop scheduling and callback queues, then examine failure and async-await bridges; close with the focused future tests and the public async API compatibility guidance.

**Why this level:**

- **Language technique 5:** Multiple expert Swift mechanisms recur in the core future implementation and public composition surface.
- **Behavioral reasoning 5:** Many coupled asynchronous states and failure branches recur throughout normal future work.
- **Design span 4:** Several major components participate, but the path remains bounded below the entire networking stack.
- **Constraint burden 5:** Expert concurrency, ordering, safety, and performance guarantees recur throughout the representative path.
- **Placement:** The four scores 5/5/4/5 sum to 19; their arithmetic mean is 4.75 and rounds half-up to Level 5. The published result is Level 5.

**Quality-gate evidence:**

- **Source quality:** EventLoopFuture.swift and EventLoop.swift carry extensive contracts for affinity, completion, callback ordering, and thread safety; EventLoopFutureTest covers transformations, combination, cascading, failure, scheduling, and edge cases, while the public async API guide explains compatibility boundaries.
- **Architecture:** The audited architecture of the path beginning at `Sources/NIOCore/EventLoopFuture.swift` has these boundaries: future and promise core, EventLoop execution contract, async compatibility policy, and large focused regression suite.
- **Naming and idiom:** `Sources/NIOCore/EventLoopFuture.swift` and its supporting files use these characteristic Swift mechanisms: deep generic future and promise composition, Sendable and concurrency-aware callback APIs, and async-await bridging with performance-sensitive specialization.
- **Tests:** Direct tests in `Tests/NIOPosixTests/EventLoopFutureTest.swift` cover these states and branches in the selected path: pending and completed success or failure states, scheduled callback, cascade, aggregate, and cancellation behavior, and cross-thread submission and event-loop-affine execution.
- **Documentation:** `Sources/NIOCore/EventLoopFuture.swift` and its selected supporting material document the contracts needed to understand how SwiftNIO completes, transforms, combines, and bridges futures while preserving event-loop affinity and callback ordering.
- **Traceability:** Begin with EventLoopFuture and Promise completion, follow map, flatMap, cascade, and aggregate operations through event-loop scheduling and callback queues, then examine failure and async-await bridges; close with the focused future tests and the public async API compatibility guidance.
- **Maintainability:** Changes to the path beginning at `Sources/NIOCore/EventLoopFuture.swift` are constrained by these audited guarantees: callbacks must execute on the owning event loop, completion must be exactly once with ordered propagation, and thread safety, cancellation, failure, and allocation costs must remain controlled.
- **Educational value:** Understand how SwiftNIO completes, transforms, combines, and bridges futures while preserving event-loop affinity and callback ordering. Event-loop vocabulary is explained once; the path teaches advanced generic future and promise APIs, callback scheduling, event-loop affinity, cascading, aggregation, cancellation and failure propagation, async interoperation, and concurrency invariants.

**Inspection record:** commit `a931f2c1de8dd49381ce3bf2e279d033f68d8865`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `Sources/NIOCore/EventLoopFuture.swift`, `Sources/NIOCore/EventLoop.swift`, `Tests/NIOPosixTests/EventLoopFutureTest.swift`, `docs/public-async-nio-apis.md`, `LICENSE.txt`. GitHub Linguist label: Swift.

**License:** Apache-2.0 ([evidence 1](https://github.com/apple/swift-nio/blob/a931f2c1de8dd49381ce3bf2e279d033f68d8865/LICENSE.txt))

### [swiftlang/swift-syntax](https://github.com/swiftlang/swift-syntax)

**Language 5 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

Swift's source-accurate syntax-tree libraries, parser tooling, refactoring support, and macro-expansion infrastructure.

**Real-world evidence:** The package publishes the SwiftSyntax libraries used by Swift macros, source tooling, formatting, refactoring, and compiler-adjacent developer tools across supported platforms.

**Language evidence:** The selected macro-expansion system, syntax rewriter, role dispatch, expansion context, diagnostics, formatting, and direct behavioral tests are handwritten first-party Swift under Sources/SwiftSyntaxMacroExpansion and Tests/SwiftSyntaxMacroExpansionTest.

**Why study it:** Understand how SwiftSyntax discovers attached and freestanding macro uses, dispatches them by role, rewrites the syntax tree, preserves context and trivia, and turns expansion failures into diagnostics. A short macro and syntax-tree primer is sufficient; the path teaches expert protocol and generic dispatch, existential types, syntax rewriting, recursive expansion, context propagation, diagnostics, source fidelity, compatibility policy, and adversarial transformation tests.

**What you can learn:**

- Study these transferable Swift mechanisms in `Sources/SwiftSyntaxMacroExpansion/MacroSystem.swift`: generic `some` and existential `any` protocol APIs, runtime metatype dispatch across macro roles, and SyntaxProtocol rewriting and typed-node conversion.
- Trace these states and branches through the selected implementation: registered macro lookup, attached and freestanding role selection, detached input and lexical context creation, recursive rewrite and generated-node insertion, formatting and trivia restoration, diagnostics, and recursive-expansion rejection.
- Identify these architectural responsibilities in the path: public expansion facade, role-specific expansion helpers, tree rewriter and application state, macro context and diagnostics, and focused expression, attached-role, lexical-context, recursive, and failure tests.
- Study these change constraints: generated Swift must remain syntactically valid and source-accurate, each role must attach output at the correct structural location, context and diagnostics must point back to original source, recursion must terminate, and package behavior must remain aligned with Swift toolchain releases.

**Prerequisites:**

- Be fluent with Swift protocols, generics, metatypes, existentials, enums with associated values, throwing APIs, builders, value semantics, and visitor or rewriter patterns.
- A Swift macro receives a typed syntax node at compile time and returns new syntax; freestanding and attached roles determine where generated declarations, expressions, members, accessors, peers, extensions, or bodies may be inserted.

**Coding relevance:**

A short macro and syntax-tree primer is sufficient; the path teaches expert protocol and generic dispatch, existential types, syntax rewriting, recursive expansion, context propagation, diagnostics, source fidelity, compatibility policy, and adversarial transformation tests.

Required domain context:

- A Swift macro receives a typed syntax node at compile time and returns new syntax; freestanding and attached roles determine where generated declarations, expressions, members, accessors, peers, extensions, or bodies may be inserted.

**Learning path:**

- **Goal:** Understand how SwiftSyntax discovers attached and freestanding macro uses, dispatches them by role, rewrites the syntax tree, preserves context and trivia, and turns expansion failures into diagnostics.
- **Start here:** [`Sources/SwiftSyntaxMacroExpansion/MacroSystem.swift`](https://github.com/swiftlang/swift-syntax/blob/dfd70da7d018493ed39721e7312f707d3f59ed2c/Sources/SwiftSyntaxMacroExpansion/MacroSystem.swift) — Begin with the public SyntaxProtocol.expand facade and MacroApplication rewriter because they expose registration, discovery, role dispatch, recursive traversal, insertion, and failure handling in one path.
- **Then read:**
  - [`Sources/SwiftSyntaxMacroExpansion/MacroExpansion.swift`](https://github.com/swiftlang/swift-syntax/blob/dfd70da7d018493ed39721e7312f707d3f59ed2c/Sources/SwiftSyntaxMacroExpansion/MacroExpansion.swift)
  - [`Sources/SwiftSyntaxMacroExpansion/BasicMacroExpansionContext.swift`](https://github.com/swiftlang/swift-syntax/blob/dfd70da7d018493ed39721e7312f707d3f59ed2c/Sources/SwiftSyntaxMacroExpansion/BasicMacroExpansionContext.swift)
  - [`Sources/SwiftSyntaxMacroExpansion/MacroSpec.swift`](https://github.com/swiftlang/swift-syntax/blob/dfd70da7d018493ed39721e7312f707d3f59ed2c/Sources/SwiftSyntaxMacroExpansion/MacroSpec.swift)
  - [`Sources/SwiftSyntaxMacroExpansion/IndentationUtils.swift`](https://github.com/swiftlang/swift-syntax/blob/dfd70da7d018493ed39721e7312f707d3f59ed2c/Sources/SwiftSyntaxMacroExpansion/IndentationUtils.swift)
  - [`Tests/SwiftSyntaxMacroExpansionTest/ExpressionMacroTests.swift`](https://github.com/swiftlang/swift-syntax/blob/dfd70da7d018493ed39721e7312f707d3f59ed2c/Tests/SwiftSyntaxMacroExpansionTest/ExpressionMacroTests.swift)
  - [`Tests/SwiftSyntaxMacroExpansionTest/MultiRoleMacroTests.swift`](https://github.com/swiftlang/swift-syntax/blob/dfd70da7d018493ed39721e7312f707d3f59ed2c/Tests/SwiftSyntaxMacroExpansionTest/MultiRoleMacroTests.swift)
  - [`Tests/SwiftSyntaxMacroExpansionTest/LexicalContextTests.swift`](https://github.com/swiftlang/swift-syntax/blob/dfd70da7d018493ed39721e7312f707d3f59ed2c/Tests/SwiftSyntaxMacroExpansionTest/LexicalContextTests.swift)
  - [`Tests/SwiftSyntaxMacroExpansionTest/StringInterpolationErrorTests.swift`](https://github.com/swiftlang/swift-syntax/blob/dfd70da7d018493ed39721e7312f707d3f59ed2c/Tests/SwiftSyntaxMacroExpansionTest/StringInterpolationErrorTests.swift)
- **Trace:** Start at SyntaxProtocol.expand, build MacroSystem and MacroApplication, follow the rewriter as it resolves a macro specification and role, creates a context, detaches and folds the input node, calls the role protocol's expansion, formats and reindents generated syntax, inserts it at the correct tree position, recursively expands generated uses, and records diagnostics on failure; close with expression, multi-role, lexical-context, interpolation-error, and recursive-expansion tests.

**Why this level:**

- **Language technique 5:** Several advanced Swift type-system and metaprogramming mechanisms interact pervasively throughout ordinary expansion behavior.
- **Behavioral reasoning 5:** Multiple transformation state machines and source-context concerns interact nonlocally, making expert behavioral reasoning unavoidable.
- **Design span 4:** Many significant components participate, while parser generation, compiler plugin transport, and the full SwiftSyntax tree implementation remain outside the selected path.
- **Constraint burden 5:** A local expansion change can violate syntax validity, source mapping, diagnostics, termination, role semantics, or toolchain compatibility elsewhere in the path.
- **Placement:** The four scores 5/5/4/5 sum to 19; their arithmetic mean is 4.75 and rounds half-up to Level 5, with three dimensions scored 5. The published result is Level 5.

**Quality-gate evidence:**

- **Source quality:** The selected handwritten implementation partitions registration, role dispatch, rewriting, context, formatting, and diagnostics despite the inherent breadth; focused tests exercise every macro role, recursion, malformed expansions, context, indentation, and source-location behavior.
- **Architecture:** MacroSystem.swift exposes the public facade and application rewriter, MacroExpansion.swift owns role-specific calls and diagnostics, BasicMacroExpansionContext owns lexical and location state, and dedicated tests isolate each transformation contract.
- **Naming and idiom:** MacroRole, MacroSpec, MacroApplication, expandAttachedMacro, expandFreestandingMacro, lexicalContext, detach, rewrite, and formattedExpansion communicate the transformation model while demonstrating expert Swift protocol and syntax-builder idioms.
- **Tests:** Expression, multi-role, lexical-context, and interpolation-error suites assert successful insertions, nested and recursive behavior, role combinations, contextual names, indentation and trivia, diagnostics, malformed output, and failure containment.
- **Documentation:** README.md and public API comments orient syntax trees and macro expansion; the Swift language's macro documentation supplies the short role model needed to read the implementation without requiring compiler theory.
- **Traceability:** A learner can follow SyntaxProtocol.expand into MacroSystem, MacroApplication, role-specific helpers, context generation, formatting, insertion, recursion, and direct expected-source and diagnostic assertions.
- **Maintainability:** Responsibilities are localized, error cases become explicit diagnostics, recursion is guarded, compatibility imports are isolated, and comprehensive role-specific tests protect the source-accurate transformation contract.
- **Educational value:** The bounded handwritten subsystem is a rare production example of Swift metaprogramming infrastructure where advanced type machinery, transformation state, source fidelity, and testing all remain observable.

**Inspection record:** commit `dfd70da7d018493ed39721e7312f707d3f59ed2c`, reviewed 2026-08-29 by Codex, Codex cold self-review. Files sampled: `README.md`, `Sources/SwiftSyntaxMacroExpansion/MacroSystem.swift`, `Sources/SwiftSyntaxMacroExpansion/MacroExpansion.swift`, `Sources/SwiftSyntaxMacroExpansion/BasicMacroExpansionContext.swift`, `Sources/SwiftSyntaxMacroExpansion/MacroSpec.swift`, `Sources/SwiftSyntaxMacroExpansion/IndentationUtils.swift`, `Tests/SwiftSyntaxMacroExpansionTest/ExpressionMacroTests.swift`, `Tests/SwiftSyntaxMacroExpansionTest/MultiRoleMacroTests.swift`, `Tests/SwiftSyntaxMacroExpansionTest/LexicalContextTests.swift`, `Tests/SwiftSyntaxMacroExpansionTest/StringInterpolationErrorTests.swift`, `LICENSE.txt`. GitHub Linguist label: Swift.

**License:** Apache-2.0 ([evidence 1](https://github.com/swiftlang/swift-syntax/blob/dfd70da7d018493ed39721e7312f707d3f59ed2c/LICENSE.txt))

_Generated from `catalog/swift.json`; do not edit by hand._

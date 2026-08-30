# Swift

6 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

**Source legend:** Production software is built primarily for real users or systems. Educational exemplars are complete teaching-oriented software and may appear only at Levels 1 and 2.

[← All languages](../README.md)

## Level 1 — First real code

No qualified learning path has been published at this level. An empty Level 1 means Exempla has not yet found a path gentle enough to publish here; learners are not being told to jump to Level 2.

## Level 2 — Guided real-world patterns

No qualified learning path has been published at this level. Standards are not lowered to fill a slot.

## Level 3 — Intermediate production software

### [pointfreeco/swift-tagged](https://github.com/pointfreeco/swift-tagged)

**Language 4 / Behavior 1 / Design 1 / Constraints 3 → Level 3**

**Source:** Production software

A tiny generic wrapper that gives otherwise identical raw values distinct compile-time identities.

**Why study it:** Understand how Swift can give identical raw values distinct compile-time identities without adding a second runtime state machine. The tag idea needs one brief explanation; the selected path is programming-led and teaches generic wrappers, conditional conformances, dynamic-member forwarding, literal and Codable forwarding, mapping, and explicit coercion.

**Short context:**

- A phantom Tag parameter distinguishes values with the same RawValue at compile time while the runtime representation remains one wrapped value.

**Prerequisites:**

- Swift generic structs, protocols, extensions, key paths, literal protocols, and basic `Codable` use.
- A generic type can include a type parameter that distinguishes values even when that parameter stores no runtime data.

**Concepts this path develops:**

- Phantom tags that create distinct compile-time identities over one raw representation.
- Conditional conformances that forward only capabilities supported by `RawValue`.
- Dynamic-member, literal, serialization, and explicit coercion behavior that preserves raw-value semantics.

**What you can learn:**

- Study these transferable Swift mechanisms in `Sources/Tagged/Tagged.swift`: phantom generic tag parameter, conditional protocol conformances, and dynamic-member, literal, and Codable forwarding.
- Trace these states and branches from `Sources/Tagged/Tagged.swift` through its selected supporting files: one wrapped raw value, local forwarding operations, and no independent runtime lifecycle.
- Identify these architectural responsibilities in the path beginning at `Sources/Tagged/Tagged.swift`: one core wrapper abstraction and one direct test suite.
- Study these change constraints for the path beginning at `Sources/Tagged/Tagged.swift`: operations exist only when RawValue satisfies matching constraints, type identity must not alter raw representation, and encoding and literal behavior must preserve RawValue semantics.

**Learning path:**

- **Goal:** Understand how Swift can give identical raw values distinct compile-time identities without adding a second runtime state machine.
- **Start here:** [`Sources/Tagged/Tagged.swift`](https://github.com/pointfreeco/swift-tagged/blob/6a8517578035408b6c14ccba00ee990a1435515c/Sources/Tagged/Tagged.swift) — Begin with `Sources/Tagged/Tagged.swift` because it exposes how Swift can give identical raw values distinct compile-time identities without adding a second runtime state machine.
- **Then read:**
  - [`Tests/TaggedTests/TaggedTests.swift`](https://github.com/pointfreeco/swift-tagged/blob/6a8517578035408b6c14ccba00ee990a1435515c/Tests/TaggedTests/TaggedTests.swift)
- **Trace:** Start with Tagged's Tag and RawValue parameters and single rawValue field, then follow mapping and dynamic-member lookup into the recurring conditional conformances; close with tests that show which operations are forwarded, encoded, compared, or deliberately coerced.

**Why this level:**

- **Language technique 4:** Advanced generic constraints, conditional conformances, dynamic-member lookup, and isolated unsafe representation coercions recur across the wrapper's public behavior.
- **Behavioral reasoning 1:** The main trace has one local value state, so compile-time sophistication does not raise runtime behavior above the Level 1 anchor.
- **Design span 1:** The lesson is intentionally contained in one production type and its tests.
- **Constraint burden 3:** Several type-safety and representation constraints recur, but they are compiler-enforced and locally visible.
- **Placement:** The four scores 4/1/1/3 sum to 9 and have a mean of 2.25; the score-4 guardrail raises the published result from the rounded Level 2 to Level 3.

**License:** MIT ([evidence 1](https://github.com/pointfreeco/swift-tagged/blob/6a8517578035408b6c14ccba00ee990a1435515c/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository publishes Swift packages used by applications to prevent identifier and domain-value mixups without runtime overhead.

**Language evidence:** The generic tag wrapper, conditional conformances, literal support, serialization, identifiers, money, and time helpers are implemented in Swift under Sources/.

**Coding relevance:**

The tag idea needs one brief explanation; the selected path is programming-led and teaches generic wrappers, conditional conformances, dynamic-member forwarding, literal and Codable forwarding, mapping, and explicit coercion.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Tagged.swift keeps the representation and conditional protocol extensions in one documented source file, while TaggedTests.swift directly covers construction, mapping, dynamic members, comparison, literals, encoding, numeric behavior, and coercion.
- **Architecture:** The audited architecture of the path beginning at `Sources/Tagged/Tagged.swift` has these boundaries: one core wrapper abstraction and one direct test suite.
- **Naming and idiom:** `Tagged`, `Tag`, and `RawValue` expose the phantom-identity model directly; conditional conformances, dynamic-member lookup, and the small isolated coercions use recognizable Swift type-system idioms.
- **Tests:** Direct tests in `Tests/TaggedTests/TaggedTests.swift` cover these states and branches in the selected path: one wrapped raw value, local forwarding operations, and no independent runtime lifecycle.
- **Documentation:** `Sources/Tagged/Tagged.swift` and its selected supporting material document the contracts needed to understand how Swift can give identical raw values distinct compile-time identities without adding a second runtime state machine.
- **Traceability:** Start with Tagged's Tag and RawValue parameters and single rawValue field, then follow mapping and dynamic-member lookup into the recurring conditional conformances; close with tests that show which operations are forwarded, encoded, compared, or deliberately coerced.
- **Maintainability:** Changes to the path beginning at `Sources/Tagged/Tagged.swift` are constrained by these audited guarantees: operations exist only when RawValue satisfies matching constraints, type identity must not alter raw representation, and encoding and literal behavior must preserve RawValue semantics.
- **Educational value:** Understand how Swift can give identical raw values distinct compile-time identities without adding a second runtime state machine. The tag idea needs one brief explanation; the selected path is programming-led and teaches generic wrappers, conditional conformances, dynamic-member forwarding, literal and Codable forwarding, mapping, and explicit coercion.

**Inspection record:** commit `6a8517578035408b6c14ccba00ee990a1435515c`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `Sources/Tagged/Tagged.swift`, `Tests/TaggedTests/TaggedTests.swift`, `LICENSE`. GitHub Linguist label: Swift.

</details>

### [vapor/vapor](https://github.com/vapor/vapor)

**Language 3 / Behavior 3 / Design 3 / Constraints 3 → Level 3**

**Source:** Production software

A server-side Swift web framework built on SwiftNIO with routing, middleware, content, authentication, sessions, clients, and operational integrations.

**Why study it:** Understand how Vapor builds an ordered middleware chain around a terminal responder and preserves request, response, and error flow. HTTP request and response vocabulary is brief; the path is programming-led and teaches protocol composition, responder wrapping, ordered configuration, type erasure, error propagation, and direct integration testing.

**Short context:**

- Middleware wraps an HTTP Responder so request handling can be composed as an ordered chain.

**Prerequisites:**

- Basic familiarity with Swift structs and classes, protocols, generics, closures, optionals, errors, asynchronous basics, and XCTest.
- Middleware wraps an HTTP Responder so request handling can be composed as an ordered chain.

**Concepts this path develops:**

- Protocol-based middleware and responder contracts.
- Ordered before and after behavior.
- Configured order must be preserved.

**What you can learn:**

- Study these transferable Swift mechanisms in `Sources/Vapor/Middleware/Middleware.swift`: protocol-based middleware and responder contracts, closure and type-erased composition, and asynchronous response values.
- Trace these states and branches from `Sources/Vapor/Middleware/Middleware.swift` through its selected supporting files: ordered before and after behavior, continue, transform, short-circuit, and error branches, and terminal responder completion.
- Identify these architectural responsibilities in the path beginning at `Sources/Vapor/Middleware/Middleware.swift`: middleware extension point, ordered configuration, and application assembly and terminal responder.
- Study these change constraints for the path beginning at `Sources/Vapor/Middleware/Middleware.swift`: configured order must be preserved, each layer must invoke or intentionally bypass the next responder, and responses and errors must propagate through the chain.

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

**License:** MIT ([evidence 1](https://github.com/vapor/vapor/blob/86ab4300efa1b3e270eeba2ca4b253998b734669/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository publishes the Vapor package used to build and run production HTTP and WebSocket services in Swift.

**Language evidence:** Application lifecycle, routing, requests and responses, middleware, content coding, authentication, sessions, clients, servers, WebSockets, validation, views, caching, tracing, metrics, and testing are Swift under Sources/.

**Coding relevance:**

HTTP request and response vocabulary is brief; the path is programming-led and teaches protocol composition, responder wrapping, ordered configuration, type erasure, error propagation, and direct integration testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Middleware.swift defines the extension contract, MiddlewareConfiguration owns ordering, Application+Middleware connects configured middleware to the application, Responder defines the terminal boundary, and MiddlewareTests verifies order, short-circuiting, errors, and composition.
- **Architecture:** The audited architecture of the path beginning at `Sources/Vapor/Middleware/Middleware.swift` has these boundaries: middleware extension point, ordered configuration, and application assembly and terminal responder.
- **Naming and idiom:** `Sources/Vapor/Middleware/Middleware.swift` and its supporting files use these characteristic Swift mechanisms: protocol-based middleware and responder contracts, closure and type-erased composition, and asynchronous response values.
- **Tests:** Direct tests in `Tests/VaporTests/MiddlewareTests.swift` cover these states and branches in the selected path: ordered before and after behavior, continue, transform, short-circuit, and error branches, and terminal responder completion.
- **Documentation:** `Sources/Vapor/Middleware/Middleware.swift` and its selected supporting material document the contracts needed to understand how Vapor builds an ordered middleware chain around a terminal responder and preserves request, response, and error flow.
- **Traceability:** Start with Middleware.respond(to:chainingTo:), follow configuration order as middleware wraps the next Responder, then trace the application-built chain into its terminal responder; close with tests for execution order, transformed responses, short circuits, and propagated failures.
- **Maintainability:** Changes to the path beginning at `Sources/Vapor/Middleware/Middleware.swift` are constrained by these audited guarantees: configured order must be preserved, each layer must invoke or intentionally bypass the next responder, and responses and errors must propagate through the chain.
- **Educational value:** Understand how Vapor builds an ordered middleware chain around a terminal responder and preserves request, response, and error flow. HTTP request and response vocabulary is brief; the path is programming-led and teaches protocol composition, responder wrapping, ordered configuration, type erasure, error propagation, and direct integration testing.

**Inspection record:** commit `86ab4300efa1b3e270eeba2ca4b253998b734669`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `Sources/Vapor/Middleware/Middleware.swift`, `Sources/Vapor/Middleware/MiddlewareConfiguration.swift`, `Sources/Vapor/Middleware/Application+Middleware.swift`, `Sources/Vapor/HTTP/Responder.swift`, `Tests/VaporTests/MiddlewareTests.swift`, `LICENSE`. GitHub Linguist label: Swift.

</details>

## Level 4 — Advanced

### [Alamofire/Alamofire](https://github.com/Alamofire/Alamofire)

**Language 3 / Behavior 4 / Design 4 / Constraints 4 → Level 4**

**Source:** Production software

An HTTP networking library for Apple platforms built over URLSession with fluent, async, Combine, streaming, and WebSocket APIs.

**Why study it:** Understand how Alamofire coordinates one request's task completion, interceptor decision, retry, cancellation, and final cleanup. HTTP and URLSession context is brief; the bounded path teaches synchronized mutable state, callback-to-task coordination, adapter and retrier boundaries, cancellation, completion ordering, and cleanup.

**Short context:**

- A Request owns a URLSession task lifecycle and may consult a RequestInterceptor before retrying a completed attempt.

**Prerequisites:**

- Working familiarity with Swift structs and classes, protocols, generics, closures, optionals, errors, asynchronous basics, and XCTest, plus experience tracing behavior across several production files.
- A Request owns a URLSession task lifecycle and may consult a RequestInterceptor before retrying a completed attempt.

**Concepts this path develops:**

- Closure and protocol-based interceptor callbacks.
- Created, resumed, suspended, cancelled, completed, and retried states.
- Callbacks must serialize state transitions.

**What you can learn:**

- Study these transferable Swift mechanisms in `Source/Core/Request.swift`: closure and protocol-based interceptor callbacks, synchronized mutable request state, and typed request and task coordination.
- Trace these states and branches from `Source/Core/Request.swift` through its selected supporting files: created, resumed, suspended, cancelled, completed, and retried states, delegate callback and interceptor decision ordering, and success, failure, retry, cancellation, and invalidation branches.
- Identify these architectural responsibilities in the path beginning at `Source/Core/Request.swift`: Request state owner, Session task coordinator, task map and delegate bridge, and interceptor extension point and integration tests.
- Study these change constraints for the path beginning at `Source/Core/Request.swift`: callbacks must serialize state transitions, retry must not leak or duplicate URLSession tasks, and cancellation, invalidation, and completion cleanup must remain ordered.

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

**License:** MIT ([evidence 1](https://github.com/Alamofire/Alamofire/blob/0455bfb650893e86ad07ace16e5f2d36dadf46f4/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository releases Alamofire through Swift Package Manager and CocoaPods for production iOS, macOS, tvOS, watchOS, and visionOS applications.

**Language evidence:** Session management, requests, uploads, downloads, streams, WebSockets, serialization, validation, authentication, retries, trust evaluation, reachability, and event monitoring are Swift under Source/.

**Coding relevance:**

HTTP and URLSession context is brief; the bounded path teaches synchronized mutable state, callback-to-task coordination, adapter and retrier boundaries, cancellation, completion ordering, and cleanup.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Request.swift documents and centralizes request state, completion, cancellation, and retry; Session, RequestTaskMap, SessionDelegate, and RequestInterceptor expose the coordinating boundaries, and SessionTests exercises task creation, completion, cancellation, retry, invalidation, and cleanup.
- **Architecture:** The audited architecture of the path beginning at `Source/Core/Request.swift` has these boundaries: Request state owner, Session task coordinator, task map and delegate bridge, and interceptor extension point and integration tests.
- **Naming and idiom:** `Source/Core/Request.swift` and its supporting files use these characteristic Swift mechanisms: closure and protocol-based interceptor callbacks, synchronized mutable request state, and typed request and task coordination.
- **Tests:** Direct tests in `Tests/SessionTests.swift` cover these states and branches in the selected path: created, resumed, suspended, cancelled, completed, and retried states, delegate callback and interceptor decision ordering, and success, failure, retry, cancellation, and invalidation branches.
- **Documentation:** `Source/Core/Request.swift` and its selected supporting material document the contracts needed to understand how Alamofire coordinates one request's task completion, interceptor decision, retry, cancellation, and final cleanup.
- **Traceability:** Start at Request completion and retry handling, follow state changes and interceptor decisions into Session task creation, RequestTaskMap ownership, and SessionDelegate callbacks, then return through retry or terminal cleanup; close with Session tests for successful completion, cancellation, retry, invalidation, and task-map removal.
- **Maintainability:** Changes to the path beginning at `Source/Core/Request.swift` are constrained by these audited guarantees: callbacks must serialize state transitions, retry must not leak or duplicate URLSession tasks, and cancellation, invalidation, and completion cleanup must remain ordered.
- **Educational value:** Understand how Alamofire coordinates one request's task completion, interceptor decision, retry, cancellation, and final cleanup. HTTP and URLSession context is brief; the bounded path teaches synchronized mutable state, callback-to-task coordination, adapter and retrier boundaries, cancellation, completion ordering, and cleanup.

**Inspection record:** commit `0455bfb650893e86ad07ace16e5f2d36dadf46f4`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `Source/Core/Request.swift`, `Source/Core/Session.swift`, `Source/Core/RequestTaskMap.swift`, `Source/Core/SessionDelegate.swift`, `Source/Features/RequestInterceptor.swift`, `Tests/SessionTests.swift`, `LICENSE`. GitHub Linguist label: Swift.

</details>

### [realm/SwiftLint](https://github.com/realm/SwiftLint)

**Language 4 / Behavior 3 / Design 3 / Constraints 4 → Level 4**

**Source:** Production software

A configurable Swift style and static-analysis tool with hundreds of rules, autocorrection, baselines, reporters, and build integrations.

**Why study it:** Understand how one SwiftLint rule detects and safely corrects unsorted import blocks while preserving source structure and configuration. Lint-rule vocabulary is brief and the code remains programming-led; the path teaches SwiftSyntax visitors and rewriters, macros, configurable comparison, source trivia preservation, disabled-region handling, correction accounting, generated tests, and reusable test helpers.

**Short context:**

- The sorted_imports rule groups adjacent Swift import declarations, reports inversions, and rewrites each block into configured order.

**Prerequisites:**

- Working familiarity with Swift structs and classes, protocols, generics, closures, optionals, errors, asynchronous basics, and XCTest, plus experience tracing behavior across several production files.
- The sorted_imports rule groups adjacent Swift import declarations, reports inversions, and rewrites each block into configured order.

**Concepts this path develops:**

- SwiftSyntax visitor and rewriter subclasses.
- Collect, group, compare, report, and rewrite phases.
- Sorting must respect configured grouping and case behavior.

**What you can learn:**

- Study these transferable Swift mechanisms in `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift`: SwiftSyntax visitor and rewriter subclasses, macro-generated rule conformance, and typed syntax and trivia transformations.
- Trace these states and branches from `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift` through its selected supporting files: collect, group, compare, report, and rewrite phases, adjacent, conditional-compilation, disabled-region, and trivia branches, and violation and correction outcomes.
- Identify these architectural responsibilities in the path beginning at `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift`: built-in rule implementation, shared visitor and correction protocols, and macro integration and generated test harness.
- Study these change constraints for the path beginning at `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift`: sorting must respect configured grouping and case behavior, comments, trivia, conditional blocks, and disabled regions must survive correction, and reported positions and correction counts must remain stable.

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

**License:** MIT ([evidence 1](https://github.com/realm/SwiftLint/blob/29d5c2b0484c9cf52d9745402160e59b7741b1db/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository releases the SwiftLint command, frameworks, package plugins, and build-tool integrations used by Swift projects and CI systems.

**Language evidence:** Rule protocols and implementations, SwiftSyntax and SourceKit analysis, configuration, corrections, baselines, caching, reporters, file discovery, command execution, plugins, and macros are Swift under Source/ and Plugins/.

**Coding relevance:**

Lint-rule vocabulary is brief and the code remains programming-led; the path teaches SwiftSyntax visitors and rewriters, macros, configurable comparison, source trivia preservation, disabled-region handling, correction accounting, generated tests, and reusable test helpers.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** SortedImportsRule.swift contains a focused visitor and rewriter, its examples and configuration define observable contracts, the core visitor and correctable-rule protocols plus macro expose integration mechanics, and generated tests and TestHelpers close the rule's violation and correction path.
- **Architecture:** The audited architecture of the path beginning at `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift` has these boundaries: built-in rule implementation, shared visitor and correction protocols, and macro integration and generated test harness.
- **Naming and idiom:** `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift` and its supporting files use these characteristic Swift mechanisms: SwiftSyntax visitor and rewriter subclasses, macro-generated rule conformance, and typed syntax and trivia transformations.
- **Tests:** `Tests/GeneratedTests/GeneratedTests_08.swift` runs the sorted-imports examples as violation and correction cases, while `Tests/TestHelpers/TestHelpers.swift` supplies the shared harness rather than an independent rule suite.
- **Documentation:** `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift` and its selected supporting material document the contracts needed to understand how one SwiftLint rule detects and safely corrects unsorted import blocks while preserving source structure and configuration.
- **Traceability:** Start with the rule's visitor collecting adjacent ImportDeclSyntax nodes and reporting inversions, then follow the rewriter's block sorting, configuration, disabled regions, trivia preservation, and correction count through shared visitor and macro machinery; close with examples and generated rule tests.
- **Maintainability:** Changes to the path beginning at `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift` are constrained by these audited guarantees: sorting must respect configured grouping and case behavior, comments, trivia, conditional blocks, and disabled regions must survive correction, and reported positions and correction counts must remain stable.
- **Educational value:** Understand how one SwiftLint rule detects and safely corrects unsorted import blocks while preserving source structure and configuration. Lint-rule vocabulary is brief and the code remains programming-led; the path teaches SwiftSyntax visitors and rewriters, macros, configurable comparison, source trivia preservation, disabled-region handling, correction accounting, generated tests, and reusable test helpers.

**Inspection record:** commit `29d5c2b0484c9cf52d9745402160e59b7741b1db`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRule.swift`, `Source/SwiftLintBuiltInRules/Rules/Style/SortedImportsRuleExamples.swift`, `Source/SwiftLintBuiltInRules/Rules/RuleConfigurations/SortedImportsConfiguration.swift`, `Source/SwiftLintCore/Protocols/SwiftSyntaxCorrectableRule.swift`, `Source/SwiftLintCore/Visitors/ViolationsSyntaxVisitor.swift`, `Source/SwiftLintCoreMacros/SwiftSyntaxRule.swift`, `Tests/GeneratedTests/GeneratedTests_08.swift`, `Tests/TestHelpers/TestHelpers.swift`, `LICENSE`. GitHub Linguist label: Swift.

</details>

## Level 5 — Expert

### [apple/swift-nio](https://github.com/apple/swift-nio)

**Language 5 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

**Source:** Production software

A cross-platform high-performance event-driven networking framework for building protocol servers and clients in Swift.

**Why study it:** Understand how SwiftNIO completes, transforms, combines, and bridges futures while preserving event-loop affinity and callback ordering. Event-loop vocabulary is explained once; the path teaches advanced generic future and promise APIs, callback scheduling, event-loop affinity, cascading, aggregation, cancellation and failure propagation, async interoperation, and concurrency invariants.

**Short context:**

- EventLoopFuture represents a result whose callbacks and transformations are confined to an EventLoop.

**Prerequisites:**

- Strong working familiarity with Swift structs and classes, protocols, generics, closures, optionals, errors, asynchronous basics, and XCTest, plus experience tracing state, resources, or asynchronous control flow across many production files.
- EventLoopFuture represents a result whose callbacks and transformations are confined to an EventLoop.

**Concepts this path develops:**

- Deep generic future and promise composition.
- Pending and completed success or failure states.
- Callbacks must execute on the owning event loop.

**What you can learn:**

- Study these transferable Swift mechanisms in `Sources/NIOCore/EventLoopFuture.swift`: deep generic future and promise composition, Sendable and concurrency-aware callback APIs, and async-await bridging with performance-sensitive specialization.
- Trace these states and branches from `Sources/NIOCore/EventLoopFuture.swift` through its selected supporting files: pending and completed success or failure states, scheduled callback, cascade, aggregate, and cancellation behavior, and cross-thread submission and event-loop-affine execution.
- Identify these architectural responsibilities in the path beginning at `Sources/NIOCore/EventLoopFuture.swift`: future and promise core, EventLoop execution contract, async compatibility policy, and large focused regression suite.
- Study these change constraints for the path beginning at `Sources/NIOCore/EventLoopFuture.swift`: callbacks must execute on the owning event loop, completion must be exactly once with ordered propagation, and thread safety, cancellation, failure, and allocation costs must remain controlled.

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

**License:** Apache-2.0 ([evidence 1](https://github.com/apple/swift-nio/blob/a931f2c1de8dd49381ce3bf2e279d033f68d8865/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The project publishes the core SwiftNIO packages that underpin production server frameworks, protocol libraries, and network clients across the Swift ecosystem.

**Language evidence:** Event loops, channels and pipelines, futures, byte buffers, sockets, selectors, bootstraps, HTTP/1, WebSockets, TLS abstractions, async sequences, and filesystem APIs are primarily Swift under Sources/.

**Coding relevance:**

Event-loop vocabulary is explained once; the path teaches advanced generic future and promise APIs, callback scheduling, event-loop affinity, cascading, aggregation, cancellation and failure propagation, async interoperation, and concurrency invariants.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** EventLoopFuture.swift and EventLoop.swift carry extensive contracts for affinity, completion, callback ordering, and thread safety; EventLoopFutureTest covers transformations, combination, cascading, failure, scheduling, and edge cases, while the public async API guide explains compatibility boundaries.
- **Architecture:** The audited architecture of the path beginning at `Sources/NIOCore/EventLoopFuture.swift` has these boundaries: future and promise core, EventLoop execution contract, async compatibility policy, and large focused regression suite.
- **Naming and idiom:** `Sources/NIOCore/EventLoopFuture.swift` and its supporting files use these characteristic Swift mechanisms: deep generic future and promise composition, Sendable and concurrency-aware callback APIs, and async-await bridging with performance-sensitive specialization.
- **Tests:** Direct tests in `Tests/NIOPosixTests/EventLoopFutureTest.swift` cover these states and branches in the selected path: pending and completed success or failure states, scheduled callback, cascade, aggregate, and cancellation behavior, and cross-thread submission and event-loop-affine execution.
- **Documentation:** `Sources/NIOCore/EventLoopFuture.swift` and its selected supporting material document the contracts needed to understand how SwiftNIO completes, transforms, combines, and bridges futures while preserving event-loop affinity and callback ordering.
- **Traceability:** Begin with EventLoopFuture and Promise completion, follow map, flatMap, cascade, and aggregate operations through event-loop scheduling and callback queues, then examine failure and async-await bridges; close with the focused future tests and the public async API compatibility guidance.
- **Maintainability:** Changes to the path beginning at `Sources/NIOCore/EventLoopFuture.swift` are constrained by these audited guarantees: callbacks must execute on the owning event loop, completion must be exactly once with ordered propagation, and thread safety, cancellation, failure, and allocation costs must remain controlled.
- **Educational value:** Understand how SwiftNIO completes, transforms, combines, and bridges futures while preserving event-loop affinity and callback ordering. Event-loop vocabulary is explained once; the path teaches advanced generic future and promise APIs, callback scheduling, event-loop affinity, cascading, aggregation, cancellation and failure propagation, async interoperation, and concurrency invariants.

**Inspection record:** commit `a931f2c1de8dd49381ce3bf2e279d033f68d8865`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `Sources/NIOCore/EventLoopFuture.swift`, `Sources/NIOCore/EventLoop.swift`, `Tests/NIOPosixTests/EventLoopFutureTest.swift`, `docs/public-async-nio-apis.md`, `LICENSE.txt`. GitHub Linguist label: Swift.

</details>

### [swiftlang/swift-syntax](https://github.com/swiftlang/swift-syntax)

**Language 5 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

**Source:** Production software

Swift's source-accurate syntax-tree libraries, parser tooling, refactoring support, and macro-expansion infrastructure.

**Why study it:** Understand how SwiftSyntax discovers attached and freestanding macro uses, dispatches them by role, rewrites the syntax tree, preserves context and trivia, and turns expansion failures into diagnostics. A short macro and syntax-tree primer is sufficient; the path teaches expert protocol and generic dispatch, existential types, syntax rewriting, recursive expansion, context propagation, diagnostics, source fidelity, compatibility policy, and adversarial transformation tests.

**Short context:**

- A Swift macro receives a typed syntax node at compile time and returns new syntax; freestanding and attached roles determine where generated declarations, expressions, members, accessors, peers, extensions, or bodies may be inserted.

**Prerequisites:**

- Be fluent with Swift protocols, generics, metatypes, existentials, enums with associated values, throwing APIs, builders, value semantics, and visitor or rewriter patterns.
- A Swift macro receives a typed syntax node at compile time and returns new syntax; freestanding and attached roles determine where generated declarations, expressions, members, accessors, peers, extensions, or bodies may be inserted.

**Concepts this path develops:**

- Interacting generic, opaque, and existential protocol APIs.
- Attached and freestanding role-specific insertion lifecycles.
- Source-accurate syntax, trivia, indentation, and diagnostic locations.

**What you can learn:**

- Study these transferable Swift mechanisms in `Sources/SwiftSyntaxMacroExpansion/MacroSystem.swift`: generic `some` and existential `any` protocol APIs, runtime metatype dispatch across macro roles, and SyntaxProtocol rewriting and typed-node conversion.
- Trace these states and branches through the selected implementation: registered macro lookup, attached and freestanding role selection, detached input and lexical context creation, recursive rewrite and generated-node insertion, formatting and trivia restoration, diagnostics, and recursive-expansion rejection.
- Identify these architectural responsibilities in the path: public expansion facade, role-specific expansion helpers, tree rewriter and application state, macro context and diagnostics, and focused expression, attached-role, lexical-context, recursive, and failure tests.
- Study these change constraints: generated Swift must remain syntactically valid and source-accurate, each role must attach output at the correct structural location, context and diagnostics must point back to original source, recursion must terminate, and package behavior must remain aligned with Swift toolchain releases.

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

**License:** Apache-2.0 ([evidence 1](https://github.com/swiftlang/swift-syntax/blob/dfd70da7d018493ed39721e7312f707d3f59ed2c/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The package publishes the SwiftSyntax libraries used by Swift macros, source tooling, formatting, refactoring, and compiler-adjacent developer tools across supported platforms.

**Language evidence:** The selected macro-expansion system, syntax rewriter, role dispatch, expansion context, diagnostics, formatting, and direct behavioral tests are handwritten first-party Swift under Sources/SwiftSyntaxMacroExpansion and Tests/SwiftSyntaxMacroExpansionTest.

**Coding relevance:**

A short macro and syntax-tree primer is sufficient; the path teaches expert protocol and generic dispatch, existential types, syntax rewriting, recursive expansion, context propagation, diagnostics, source fidelity, compatibility policy, and adversarial transformation tests.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The selected handwritten implementation partitions registration, role dispatch, rewriting, context, formatting, and diagnostics despite the inherent breadth; focused tests exercise every macro role, recursion, malformed expansions, context, indentation, and source-location behavior.
- **Architecture:** MacroSystem.swift exposes the public facade and application rewriter, MacroExpansion.swift owns role-specific calls and diagnostics, BasicMacroExpansionContext owns lexical and location state, and dedicated tests isolate each transformation contract.
- **Naming and idiom:** MacroRole, MacroSpec, MacroApplication, expandAttachedMacro, expandFreestandingMacro, lexicalContext, detach, rewrite, and formattedExpansion communicate the transformation model while demonstrating expert Swift protocol and syntax-builder idioms.
- **Tests:** Expression, multi-role, lexical-context, and interpolation-error suites assert successful insertions, nested and recursive behavior, role combinations, contextual names, indentation and trivia, diagnostics, malformed output, and failure containment.
- **Documentation:** README.md and public API comments orient syntax trees and macro expansion; the Swift language's macro documentation supplies the short role model needed to read the implementation without requiring compiler theory.
- **Traceability:** A learner can follow SyntaxProtocol.expand into MacroSystem, MacroApplication, role-specific helpers, context generation, formatting, insertion, recursion, and direct expected-source and diagnostic assertions.
- **Maintainability:** Responsibilities are localized, error cases become explicit diagnostics, recursion is guarded, compatibility imports are isolated, and comprehensive role-specific tests protect the source-accurate transformation contract.
- **Educational value:** The bounded handwritten subsystem is a rare production example of Swift metaprogramming infrastructure where advanced type machinery, transformation state, source fidelity, and testing all remain observable.

**Inspection record:** commit `dfd70da7d018493ed39721e7312f707d3f59ed2c`, inspected 2026-08-29. Review passes: Codex primary pass; Codex cold verification pass. Files inspected: `README.md`, `Sources/SwiftSyntaxMacroExpansion/MacroSystem.swift`, `Sources/SwiftSyntaxMacroExpansion/MacroExpansion.swift`, `Sources/SwiftSyntaxMacroExpansion/BasicMacroExpansionContext.swift`, `Sources/SwiftSyntaxMacroExpansion/MacroSpec.swift`, `Sources/SwiftSyntaxMacroExpansion/IndentationUtils.swift`, `Tests/SwiftSyntaxMacroExpansionTest/ExpressionMacroTests.swift`, `Tests/SwiftSyntaxMacroExpansionTest/MultiRoleMacroTests.swift`, `Tests/SwiftSyntaxMacroExpansionTest/LexicalContextTests.swift`, `Tests/SwiftSyntaxMacroExpansionTest/StringInterpolationErrorTests.swift`, `LICENSE.txt`. GitHub Linguist label: Swift.

</details>

_Generated from `catalog/swift.json`; do not edit by hand._

# Objective-C

8 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

[← All languages](../README.md)

## Level 1

No qualified learning path has been published at this level. Standards are not lowered to fill a slot.

## Level 2

### [mirego/MCUIViewLayout](https://github.com/mirego/MCUIViewLayout)

**Language 2 / Behavior 2 / Design 1 / Constraints 3 → Level 2**

A small UIView layout library for sizing and positioning views against superviews and siblings with explicit geometry helpers.

**Why study it:** It turns repetitive frame arithmetic into a bounded vocabulary while leaving every CGRect calculation, margin rule, display-scale rounding choice, and category method visible.

**Prerequisites:**

- Objective-C methods and categories, UIKit views and frames, C structs and bitmasks, coordinate systems, floating-point rounding, and XCTest.

**Concepts this path develops:**

- Objective-C categories over UIKit classes.
- Parent-relative and sibling-relative coordinate cases.
- Coordinate-system and margin semantics must remain exact.

**What you can learn:**

- Objective-C categories, NS_OPTIONS bitmasks, CGRect arithmetic, sibling and superview coordinates, display-scale rounding, compatibility, and geometry tests.

**Learning path:**

- **Goal:** Understand how a small Objective-C category library turns composable layout options into exact, scale-aware view frames.
- **Start here:** [`Sources/MCUIViewLayoutObjC/UIView+MCLayoutCalculation.m`](https://github.com/mirego/MCUIViewLayout/blob/987cb7ee525f03aeae81db7e3ad639080e23bc46/Sources/MCUIViewLayoutObjC/UIView%2BMCLayoutCalculation.m) — The calculation category expresses the geometry rules without mutation; the public category then applies returned rectangles to views.
- **Then read:**
  - [`Sources/MCUIViewLayoutObjC/MCUIViewLayoutPosition.m`](https://github.com/mirego/MCUIViewLayout/blob/987cb7ee525f03aeae81db7e3ad639080e23bc46/Sources/MCUIViewLayoutObjC/MCUIViewLayoutPosition.m)
  - [`Sources/MCUIViewLayoutObjC/UIView+MCLayout.m`](https://github.com/mirego/MCUIViewLayout/blob/987cb7ee525f03aeae81db7e3ad639080e23bc46/Sources/MCUIViewLayoutObjC/UIView%2BMCLayout.m)
  - [`MCUIViewLayoutExample/UIViewLayoutExampleTests/UIView_MCLayoutCalculationsTest.m`](https://github.com/mirego/MCUIViewLayout/blob/987cb7ee525f03aeae81db7e3ad639080e23bc46/MCUIViewLayoutExample/UIViewLayoutExampleTests/UIView_MCLayoutCalculationsTest.m)
  - [`README.md`](https://github.com/mirego/MCUIViewLayout/blob/987cb7ee525f03aeae81db7e3ad639080e23bc46/README.md)
  - [`LICENSE.md`](https://github.com/mirego/MCUIViewLayout/blob/987cb7ee525f03aeae81db7e3ad639080e23bc46/LICENSE.md)
- **Trace:** Start with the pure mc_getRect calculation entry points, follow superview and sibling coordinate selection, combined fitting options, margins, and delegation into MCUIViewLayoutPosition's scale-rounded arithmetic, then see UIView+MCLayout apply the calculated frame and close representative CGRect contracts in the direct calculation suite.

**Why this level:**

- **Language technique 2:** Several ordinary Objective-C and UIKit idioms materially shape the API without advanced language machinery.
- **Behavioral reasoning 2:** Several explicit geometric cases recur, but all reasoning stays synchronous and local.
- **Design span 1:** One small cohesive library contains the design.
- **Constraint burden 3:** Several precision, composition, and compatibility guarantees constrain ordinary changes.
- **Placement:** The four scores 2/2/1/3 sum to 8; their arithmetic mean is 2.00 and rounds half-up to Level 2. The published result is Level 2.

**License:** BSD-3-Clause ([evidence 1](https://github.com/mirego/MCUIViewLayout/blob/987cb7ee525f03aeae81db7e3ad639080e23bc46/LICENSE.md))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The repository distributes Objective-C and Swift package products and documents UIKit use through Swift Package Manager and CocoaPods.

**Language evidence:** The original and still-shipped geometry model, UIView calculation categories, frame mutation methods, compatibility facade, and XCTest suite are Objective-C.

**Coding relevance:**

That short user-interface geometry primer is subordinate to transferable lessons in category design, bitmask options, pure calculations before mutation, coordinate translation, composition of fitting and positioning operations, display-scale rounding, compatibility facades, and exhaustive boundary tests.

Required domain context:

- UIKit represents a view's position and size with CGRect values in superview and sibling coordinate systems.

**Eight-part quality gate:**

- **Source quality:** Pure calculation methods separate geometry from frame mutation, combinations are explicit, and scale-aware rounding avoids blurred half-pixel placement.
- **Architecture:** A position model and calculation category define geometry; a public UIView category applies it; a deprecated facade isolates compatibility.
- **Naming and idiom:** mc_setPosition, relativeToView, withMargins, sizeToFit, mc_width, mc_origin, and MCUIViewLayoutPosition state layout intent directly.
- **Tests:** Nine XCTest files cover base dimensions, all superview alignments, sibling relationships, fitting, combined operations, missing parents, unequal margins, and display-scale rounding.
- **Documentation:** The README walks through z-order, sizing, absolute, parent-relative, and sibling-relative layout with diagrams and examples.
- **Traceability:** A position option can be followed from its bitmask through a calculation helper into frame mutation and an exact CGRect assertion.
- **Maintainability:** The Objective-C implementation is compact, calculation logic is reusable, compatibility code is isolated, and geometry cases are enumerated in focused suites.
- **Educational value:** It demonstrates how a small convenience API can improve call-site language while preserving transparent, testable arithmetic.

**Inspection record:** commit `987cb7ee525f03aeae81db7e3ad639080e23bc46`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `Sources/MCUIViewLayoutObjC/UIView+MCLayoutCalculation.m`, `Sources/MCUIViewLayoutObjC/MCUIViewLayoutPosition.m`, `Sources/MCUIViewLayoutObjC/UIView+MCLayout.m`, `MCUIViewLayoutExample/UIViewLayoutExampleTests/UIView_MCLayoutCalculationsTest.m`, `README.md`, `LICENSE.md`. GitHub Linguist label: Objective-C.

</details>

### [shinyfrog/TextBundle](https://github.com/shinyfrog/TextBundle)

**Language 2 / Behavior 2 / Design 1 / Constraints 3 → Level 2**

A compact framework for reading, creating, and writing TextBundle document packages with metadata, text, and optional assets.

**Why study it:** A few files expose the complete path from an on-disk directory package through NSFileWrapper, JSON metadata, text type selection, attachments, validation, and atomic persistence.

**Prerequisites:**

- Objective-C classes and properties, Foundation collections and data, files and URLs, JSON, nullable errors, and document packages.

**Concepts this path develops:**

- Objective-C properties and nullable NSError conventions.
- Read and write transformations between a package tree and object state.
- Required package members and metadata keys must remain valid.

**What you can learn:**

- Objective-C properties, NSFileWrapper packages, JSON serialization, Uniform Type Identifiers, NSError conventions, metadata preservation, asset filenames, and fixture tests.

**Learning path:**

- **Goal:** Understand how a compact Objective-C model validates, reads, mutates, and writes a directory-based document package without losing metadata or assets.
- **Start here:** [`TextBundle/TextBundleWrapper.m`](https://github.com/shinyfrog/TextBundle/blob/eb0e2c75afec3817cf6817548179fe679ba565ee/TextBundle/TextBundleWrapper.m) — The implementation can be read end to end, from defaults through file-wrapper construction, parsing, validation, assets, and filename generation.
- **Then read:**
  - [`TextBundle/TextBundleWrapper.h`](https://github.com/shinyfrog/TextBundle/blob/eb0e2c75afec3817cf6817548179fe679ba565ee/TextBundle/TextBundleWrapper.h)
  - [`TextBundleTests/TextBundleTests.m`](https://github.com/shinyfrog/TextBundle/blob/eb0e2c75afec3817cf6817548179fe679ba565ee/TextBundleTests/TextBundleTests.m)
  - [`TextBundleTests/Sample TextBundles/text plus attachments.textbundle/info.json`](https://github.com/shinyfrog/TextBundle/blob/eb0e2c75afec3817cf6817548179fe679ba565ee/TextBundleTests/Sample%20TextBundles/text%20plus%20attachments.textbundle/info.json)
  - [`README.md`](https://github.com/shinyfrog/TextBundle/blob/eb0e2c75afec3817cf6817548179fe679ba565ee/README.md)
  - [`LICENSE`](https://github.com/shinyfrog/TextBundle/blob/eb0e2c75afec3817cf6817548179fe679ba565ee/LICENSE)
- **Trace:** Start with initialization and readFromURL, follow NSFileWrapper validation into info.json decoding, text filename and type selection, metadata properties, and optional assets, then reverse the flow through fileWrapper, textFilenameForType, asset collision handling, and writeToURL before closing the format and error cases in TextBundleTests.

**Why this level:**

- **Language technique 2:** Several ordinary Objective-C and Foundation idioms shape the path, without advanced runtime or language machinery.
- **Behavioral reasoning 2:** The behavior has several cases but remains synchronous and locally traceable in one class.
- **Design span 1:** One unit contains nearly the complete design.
- **Constraint burden 3:** Several format, persistence, and data-preservation guarantees constrain otherwise ordinary changes.
- **Placement:** The four scores 2/2/1/3 sum to 8; their arithmetic mean is 2.00 and rounds half-up to Level 2. The published result is Level 2.

**License:** MIT ([evidence 1](https://github.com/shinyfrog/TextBundle/blob/eb0e2c75afec3817cf6817548179fe679ba565ee/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The framework implements the TextBundle interchange format used by writing applications and ships macOS and iOS targets.

**Language evidence:** TextBundle package reading and writing, metadata projection, Uniform Type Identifier handling, asset collision handling, errors, and tests are Objective-C.

**Coding relevance:**

That short format primer is subordinate to transferable file-format engineering: Foundation object modeling, directory-package validation, JSON metadata projection, filename and Uniform Type Identifier mapping, attachment ownership, collision handling, errors, and round-trip tests.

Required domain context:

- A TextBundle is a directory package whose info.json names a text file and optional assets for interchange between writing applications.

**Eight-part quality gate:**

- **Source quality:** Required-file checks, metadata extraction, asset deduplication, package construction, and errors are visible in short methods over Foundation values.
- **Architecture:** One shared wrapper contains the format behavior while thin macOS and iOS targets expose it.
- **Naming and idiom:** info.json, textFilenameForType, fileWrapper, metadata, assetsFileWrapper, readFromURL, and writeToURL mirror the package vocabulary.
- **Tests:** Fixtures cover text-only and attachment packages, missing members, invalid input, creation, writing, and asset collisions; one write-to-new-URL test mistakenly reloads its source fixture, so it is not a complete persistence round trip.
- **Documentation:** The README explains the TextBundle format, platform targets, installation, and wrapper role.
- **Traceability:** A bundle can be followed from NSFileWrapper through info.json and text selection into properties, then back through fileWrapper and writeToURL.
- **Maintainability:** Format constants and transformations are centralized, the surface is narrow, and representative packages live beside the tests.
- **Educational value:** It is an approachable first study of mapping a real document format onto Foundation without a framework-sized abstraction.

**Inspection record:** commit `eb0e2c75afec3817cf6817548179fe679ba565ee`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `TextBundle/TextBundleWrapper.m`, `TextBundle/TextBundleWrapper.h`, `TextBundleTests/TextBundleTests.m`, `TextBundleTests/Sample TextBundles/text plus attachments.textbundle/info.json`, `README.md`, `LICENSE`. GitHub Linguist label: Objective-C.

</details>

## Level 3

### [pinterest/PINOperation](https://github.com/pinterest/PINOperation)

**Language 3 / Behavior 4 / Design 2 / Constraints 4 → Level 3**

A thread-safe operation queue with priorities, dynamic concurrency limits, cancellation, data coalescing, completions, and operation groups.

**Why study it:** Its small surface reveals recursive locks, serial and concurrent lanes, semaphores, dispatch groups, priority queues, weak reference maps, duplicate-work coalescing, and nested work.

**Prerequisites:**

- Comfortable Objective-C, blocks, Foundation collections, Grand Central Dispatch, mutexes and semaphores, race conditions, cancellation, and asynchronous tests.

**Concepts this path develops:**

- Objective-C blocks and protocol-typed operation references.
- Priority-ordered serial and concurrent lanes.
- Group enter and leave, reference lifetime, and completion counts must balance exactly.

**What you can learn:**

- Grand Central Dispatch queues, groups, and semaphores, pthread mutexes, bounded concurrency, priorities, cancellation, coalescing, completion fan-out, and asynchronous XCTest.

**Learning path:**

- **Goal:** Understand how an Objective-C operation queue preserves priority, cancellation, coalescing, completion, and bounded-concurrency invariants across serial and concurrent work.
- **Start here:** [`Source/PINOperationQueue.m`](https://github.com/pinterest/PINOperation/blob/a74f978733bdaf982758bfa23d70a189f4b4c1b6/Source/PINOperationQueue.m) — The queue connects registration, priority buckets, locking, serial and concurrent dispatch, cancellation, coalescing, dynamic limits, and completion accounting.
- **Then read:**
  - [`Source/PINOperationQueue.h`](https://github.com/pinterest/PINOperation/blob/a74f978733bdaf982758bfa23d70a189f4b4c1b6/Source/PINOperationQueue.h)
  - [`Source/PINOperationGroup.m`](https://github.com/pinterest/PINOperation/blob/a74f978733bdaf982758bfa23d70a189f4b4c1b6/Source/PINOperationGroup.m)
  - [`Tests/PINOperationQueueTests.m`](https://github.com/pinterest/PINOperation/blob/a74f978733bdaf982758bfa23d70a189f4b4c1b6/Tests/PINOperationQueueTests.m)
  - [`Tests/PINOperationGroupTests.m`](https://github.com/pinterest/PINOperation/blob/a74f978733bdaf982758bfa23d70a189f4b4c1b6/Tests/PINOperationGroupTests.m)
  - [`README.md`](https://github.com/pinterest/PINOperation/blob/a74f978733bdaf982758bfa23d70a189f4b4c1b6/README.md)
  - [`LICENSE.txt`](https://github.com/pinterest/PINOperation/blob/a74f978733bdaf982758bfa23d70a189f4b4c1b6/LICENSE.txt)
- **Trace:** Start with scheduleOperation and reference allocation, follow recursive-lock protection into priority sets and identifier-based coalescing, then trace dispatch-group entry, serial or semaphore-bounded concurrent execution, cancellation and completion fan-out, runtime limit changes, group completion, and nested waiting before closing each invariant in the queue and group suites.

**Why this level:**

- **Language technique 3:** Substantial Objective-C and platform concurrency mechanisms materially shape the scheduler without expert runtime machinery.
- **Behavioral reasoning 4:** Advanced nonlocal scheduling, ownership, and event-order reasoning recurs across asynchronous callbacks.
- **Design span 2:** A few clear units contain the complete design.
- **Constraint burden 4:** Multiple strict concurrency, lifecycle, ordering, and liveness guarantees interact.
- **Placement:** The four scores 3/4/2/4 sum to 13; their arithmetic mean is 3.25 and rounds half-up to Level 3. The published result is Level 3.

**License:** Apache-2.0 ([evidence 1](https://github.com/pinterest/PINOperation/blob/a74f978733bdaf982758bfa23d70a189f4b4c1b6/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Pinterest maintains and releases PINOperation as an Apple-platform library through Swift Package Manager and CocoaPods.

**Language evidence:** Priority scheduling, serial and bounded-concurrent execution, cancellation, coalescing, grouped operations, synchronization, and tests are Objective-C over Grand Central Dispatch and pthread mutexes.

**Coding relevance:**

That familiar concurrency vocabulary is subordinate to transferable scheduler engineering: recursive mutex ownership, priority ordering, serial and concurrent lanes, semaphore-based dynamic limits, dispatch-group accounting, cancellation races, work coalescing, completion fan-out, reference lifetime, nested work, and asynchronous contract tests.

Required domain context:

- An operation queue schedules blocks for serial or bounded-concurrent execution and may expose priorities, cancellation, and groups.

**Eight-part quality gate:**

- **Source quality:** Lock boundaries, queue membership, dispatch-group accounting, completion ownership, semaphore changes, and cancellation results are explicit.
- **Architecture:** PINOperationQueue owns scheduling and references; an internal record holds work; PINOperationGroup batches operations and completion under separate synchronization.
- **Naming and idiom:** scheduleOperation, withPriority, coalescingData, cancelOperation, waitUntilAllOperationsAreFinished, operationReference, and completion expose scheduler semantics.
- **Tests:** Tests cover execution and release, nested waiting without deadlock, concurrency limits including one, priority, cancellation, priority changes, coalesced data and completions, groups, and runtime limit changes.
- **Documentation:** The README explains serial and concurrent behavior, priority, cancellation, coalescing, groups, installation, and the public API.
- **Traceability:** A block can be followed from reference allocation into a priority set, dispatch lane, completion, group leave, and a synchronization-focused assertion.
- **Maintainability:** A narrow API, two synchronized components, invariant-preserving private helpers, and regression tests constrain a concurrency-heavy implementation.
- **Educational value:** It is a compact bridge from basic dispatch queues to designing and testing a reusable concurrent scheduler.

**Inspection record:** commit `a74f978733bdaf982758bfa23d70a189f4b4c1b6`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `Source/PINOperationQueue.m`, `Source/PINOperationQueue.h`, `Source/PINOperationGroup.m`, `Tests/PINOperationQueueTests.m`, `Tests/PINOperationGroupTests.m`, `README.md`, `LICENSE.txt`. GitHub Linguist label: Objective-C.

</details>

### [sparkle-project/Sparkle](https://github.com/sparkle-project/Sparkle)

**Language 3 / Behavior 3 / Design 3 / Constraints 4 → Level 3**

A secure macOS software-update framework with signed appcasts, background downloads, delta updates, sandbox support, privilege-separated installation, phased rollouts, resumable updates, and customizable UI.

**Why study it:** Sparkle's appcast-selection path is a bounded policy engine for filtering and ordering update candidates without requiring the security and installation pipeline.

**Prerequisites:**

- Readers should know Objective-C models and delegates, comparators, filtering, dates, and the basic idea of an update feed containing versions, channels, system bounds, and rollout metadata.

**Concepts this path develops:**

- Objective-C models, protocols, predicates, and nullable policy values.
- Layered deterministic filter and ranking pipeline.
- Version order, operating-system bounds, channels, and minimum autoupdate rules must compose exactly.

**What you can learn:**

- Trace feed items through operating-system, channel, version, skipped-update, autoupdate, phased-rollout, delegate, primary, secondary, and no-update decisions.

**Learning path:**

- **Goal:** Understand how Sparkle filters an appcast and selects the best applicable update while preserving version, channel, skipped-update, system-bound, and phased-rollout policy.
- **Start here:** [`Sparkle/SUAppcastDriver.m`](https://github.com/sparkle-project/Sparkle/blob/164f2fd30f7b6feb60596246322648a784dd308c/Sparkle/SUAppcastDriver.m) — The reviewed trace begins in SUAppcastDriver.m because it owns the ordered filters, candidate comparison, delegate policy, and final primary or secondary selection.
- **Then read:**
  - [`Sparkle/SUAppcast.m`](https://github.com/sparkle-project/Sparkle/blob/164f2fd30f7b6feb60596246322648a784dd308c/Sparkle/SUAppcast.m)
  - [`Sparkle/SUAppcastItem.m`](https://github.com/sparkle-project/Sparkle/blob/164f2fd30f7b6feb60596246322648a784dd308c/Sparkle/SUAppcastItem.m)
  - [`Sparkle/SPUAppcastItemStateResolver.m`](https://github.com/sparkle-project/Sparkle/blob/164f2fd30f7b6feb60596246322648a784dd308c/Sparkle/SPUAppcastItemStateResolver.m)
  - [`Sparkle/SUStandardVersionComparator.m`](https://github.com/sparkle-project/Sparkle/blob/164f2fd30f7b6feb60596246322648a784dd308c/Sparkle/SUStandardVersionComparator.m)
  - [`Tests/SUAppcastTest.swift`](https://github.com/sparkle-project/Sparkle/blob/164f2fd30f7b6feb60596246322648a784dd308c/Tests/SUAppcastTest.swift)
  - [`Tests/SUVersionComparisonTest.m`](https://github.com/sparkle-project/Sparkle/blob/164f2fd30f7b6feb60596246322648a784dd308c/Tests/SUVersionComparisonTest.m)
  - [`README.markdown`](https://github.com/sparkle-project/Sparkle/blob/164f2fd30f7b6feb60596246322648a784dd308c/README.markdown)
  - [`LICENSE`](https://github.com/sparkle-project/Sparkle/blob/164f2fd30f7b6feb60596246322648a784dd308c/LICENSE)
- **Trace:** Start where a loaded appcast is filtered for macOS and allowed channels, follow system and minimum-autoupdate requirements, skipped versions, phased-rollout groups and dates, state resolution, injected or standard version comparison, delegate candidate overrides, primary and secondary selection, and no-update diagnostics, then close parsing, filtering, and version-order behavior in the appcast and comparator suites.

**Why this level:**

- **Language technique 3:** Substantial Objective-C framework abstractions shape the path without advanced runtime machinery.
- **Behavioral reasoning 3:** Multi-stage policy and state reasoning recurs, while remaining synchronous and inspectable.
- **Design span 3:** Several meaningful updater-selection layers cooperate in a bounded path.
- **Constraint burden 4:** Multiple strict selection, version, rollout, extension, and compatibility guarantees recur.
- **Placement:** The four scores 3/3/3/4 sum to 13; their arithmetic mean is 3.25 and rounds half-up to Level 3. The published result is Level 3.

**License:** MIT AND BSD-2-Clause AND Zlib ([evidence 1](https://github.com/sparkle-project/Sparkle/blob/164f2fd30f7b6feb60596246322648a784dd308c/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Sparkle is released as a framework, Swift package, command-line tool, and supporting services used by independently distributed macOS applications.

**Language evidence:** Updater scheduling and drivers, appcast parsing, signature and code-signing validation, downloading, extraction and installation, XPC services, UI, version comparison, CLI integration, and core tests are predominantly Objective-C.

**Coding relevance:**

That short updater-feed primer is subordinate to transferable selection engineering: immutable item modeling, layered filtering, injectable comparators and delegate policy, version ordering, skipped updates, channels, phased rollout timing, primary and secondary candidates, fallback explanations, and deterministic tests. The security and installation pipeline is deliberately outside this bounded path.

Required domain context:

- A Sparkle appcast is an update feed whose items carry application versions, operating-system bounds, channels, rollout information, and optional delta relationships.

**Eight-part quality gate:**

- **Source quality:** SUAppcastDriver.m separates system, channel, skipped-version, rollout, delegate, and selection decisions; item-state resolution and version comparison remain in named collaborators.
- **Architecture:** Parsed appcast items become immutable candidates, layered filters reduce them, injected policy resolves applicability and ordering, and the driver reports an update or a specific no-update reason.
- **Naming and idiom:** SUAppcastDriver, SUAppcastItem, SPUAppcastItemStateResolver, SUStandardVersionComparator, channels, and phased rollout preserve feed and policy intent.
- **Tests:** SUAppcastTest.swift and SUVersionComparisonTest.m cover feed parsing, filtering, version order, channels, rollout dates, system bounds, deltas, and edge cases.
- **Documentation:** README.markdown and public Sparkle guidance orient appcasts, versions, channels, and update selection.
- **Traceability:** A loaded feed item can be followed through each driver filter and comparator to a primary, secondary, or rejected result asserted by the appcast and version suites.
- **Maintainability:** Policy stages and comparator injection are explicit, and the selected tests protect ordering and applicability without coupling the lesson to installation or signature verification.
- **Educational value:** The path demonstrates how several individually simple policies interact in a production selection engine while remaining locally teachable.

**Inspection record:** commit `164f2fd30f7b6feb60596246322648a784dd308c`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `Sparkle/SUAppcastDriver.m`, `Sparkle/SUAppcast.m`, `Sparkle/SUAppcastItem.m`, `Sparkle/SPUAppcastItemStateResolver.m`, `Sparkle/SUStandardVersionComparator.m`, `Tests/SUAppcastTest.swift`, `Tests/SUVersionComparisonTest.m`, `README.markdown`, `LICENSE`. GitHub Linguist label: Objective-C.

</details>

## Level 4

### [SBJson/SBJson](https://github.com/SBJson/SBJson)

**Language 4 / Behavior 4 / Design 3 / Constraints 4 → Level 4**

A streaming Objective-C JSON parser and writer that accepts chunks, emits complete values or array elements, and supports bounded depth and deterministic formatting.

**Why study it:** SBJson's streaming path is a production parser lesson in preserving lexical and structural state when tokens and nested values cross arbitrary input chunks.

**Prerequisites:**

- Readers should know Objective-C classes and blocks, C bytes and lengths, state machines, UTF-8 at a high level, and JSON objects, arrays, strings, numbers, booleans, and null.

**Concepts this path develops:**

- Objective-C class hierarchy for parser states.
- Lexical state persists across arbitrary chunk boundaries.
- JSON grammar and token boundaries must remain exact for every chunk split.

**What you can learn:**

- Trace retained bytes through incremental token states, UTF-8 and escape validation, nested object and array states, depth limits, callbacks, completion, and errors.

**Learning path:**

- **Goal:** Understand how a streaming Objective-C JSON parser preserves lexical and structural state when tokens and nested values cross arbitrary input-chunk boundaries.
- **Start here:** [`Classes/SBJson5StreamTokeniser.m`](https://github.com/SBJson/SBJson/blob/93e4ca5c274488fb745429977308d85929c5f13a/Classes/SBJson5StreamTokeniser.m) — The reviewed trace begins in SBJson5StreamTokeniser.m because every chunk first enters its retained-buffer and lexical-state machinery before structural parsing.
- **Then read:**
  - [`Classes/SBJson5StreamParser.m`](https://github.com/SBJson/SBJson/blob/93e4ca5c274488fb745429977308d85929c5f13a/Classes/SBJson5StreamParser.m)
  - [`Tests/JsonStreamTokeniserTest.m`](https://github.com/SBJson/SBJson/blob/93e4ca5c274488fb745429977308d85929c5f13a/Tests/JsonStreamTokeniserTest.m)
  - [`Tests/StreamSuite.m`](https://github.com/SBJson/SBJson/blob/93e4ca5c274488fb745429977308d85929c5f13a/Tests/StreamSuite.m)
  - [`Tests/MainSuite.m`](https://github.com/SBJson/SBJson/blob/93e4ca5c274488fb745429977308d85929c5f13a/Tests/MainSuite.m)
  - [`TestData/jsonchecker/README`](https://github.com/SBJson/SBJson/blob/93e4ca5c274488fb745429977308d85929c5f13a/TestData/jsonchecker/README)
  - [`TestData/kuhn/utf8.in`](https://github.com/SBJson/SBJson/blob/93e4ca5c274488fb745429977308d85929c5f13a/TestData/kuhn/utf8.in)
  - [`README.md`](https://github.com/SBJson/SBJson/blob/93e4ca5c274488fb745429977308d85929c5f13a/README.md)
  - [`LICENSE`](https://github.com/SBJson/SBJson/blob/93e4ca5c274488fb745429977308d85929c5f13a/LICENSE)
- **Trace:** Start with getToken's retained byte range and lexical-state dispatch, follow partial strings, escapes, UTF-8, numbers, keywords, whitespace, and errors into SBJson5StreamParser's named object and array states, state stack, depth checks, Foundation value assembly, callback delivery, waiting and complete statuses, then close chunk-boundary, malformed-input, Unicode, nesting, and completion behavior in the tokeniser and stream suites.

**Why this level:**

- **Language technique 4:** Advanced Objective-C and low-level byte techniques recur across tokenization and structural parsing.
- **Behavioral reasoning 4:** Advanced nonlocal state-machine and incremental-input reasoning recurs throughout the trace.
- **Design span 3:** Several meaningful parsing layers cooperate while remaining locally understandable.
- **Constraint burden 4:** Multiple strict syntax, encoding, incremental-state, safety, and compatibility guarantees recur.
- **Placement:** The four scores 4/4/3/4 sum to 15; their arithmetic mean is 3.75 and rounds half-up to Level 4. The published result is Level 4.

**License:** BSD-3-Clause ([evidence 1](https://github.com/SBJson/SBJson/blob/93e4ca5c274488fb745429977308d85929c5f13a/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** SBJson ships a versioned CocoaPod and framework API for applications needing incremental JSON processing or compatibility with its long-lived interface.

**Language evidence:** Incremental UTF-8 tokenization, parser and writer state machines, Objective-C value construction, streaming callbacks, formatting, errors, and tests are Objective-C.

**Coding relevance:**

That short grammar primer is subordinate to transferable parser engineering: retained byte chunks, strict UTF-8 and surrogate validation, incremental lexical states, token lifetimes, nested structural state stacks, depth limits, partial-input status, callback delivery, error offsets, and conformance tests.

Required domain context:

- JSON's grammar distinguishes objects, arrays, strings, numbers, booleans, and null; streaming input may split any token across chunks.

**Eight-part quality gate:**

- **Source quality:** SBJson5StreamTokeniser.m makes offsets, partial buffers, byte availability, token states, encoding checks, and errors explicit; SBJson5StreamParser.m names structural transitions.
- **Architecture:** An incremental tokeniser emits lexical units to a structural parser that maintains an object and array state stack, assembles Foundation values, and invokes callbacks.
- **Naming and idiom:** StreamTokeniser, StreamParser, token states, object and array parser states, waiting, complete, and error statuses expose the incremental design through Objective-C and C idioms.
- **Tests:** JsonStreamTokeniserTest.m, StreamSuite.m, MainSuite.m, JSONChecker data, and Unicode fixtures exercise chunk splits, malformed syntax and encoding, nesting, roots, completion, and error locations.
- **Documentation:** README.md documents streaming modes, while the JSONChecker and UTF-8 fixture documentation identify conformance inputs.
- **Traceability:** A byte chunk can be followed through lexical state and retained data into a structural transition, callback, or precise error and then closed by focused streaming tests.
- **Maintainability:** Lexical and structural state are separated, buffers are bounded explicitly, and conformance suites protect syntax, encoding, depth, and chunk-boundary behavior.
- **Educational value:** The path exposes why incremental parsing is more than ordinary recursive descent while remaining bounded to tokenizer and stream-parser behavior.

**Inspection record:** commit `93e4ca5c274488fb745429977308d85929c5f13a`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `Classes/SBJson5StreamTokeniser.m`, `Classes/SBJson5StreamParser.m`, `Tests/JsonStreamTokeniserTest.m`, `Tests/StreamSuite.m`, `Tests/MainSuite.m`, `TestData/jsonchecker/README`, `TestData/kuhn/utf8.in`, `README.md`, `LICENSE`. GitHub Linguist label: Objective-C.

</details>

### [SDWebImage/SDWebImage](https://github.com/SDWebImage/SDWebImage)

**Language 3 / Behavior 4 / Design 4 / Constraints 5 → Level 4**

An asynchronous image loading and caching framework for Apple platforms with codecs, progressive and animated images, transformations, prefetching, and extensible cache and loader pipelines.

**Why study it:** SDWebImage's manager path shows how a mature Objective-C library coordinates cache, network, decoding, transformation, cancellation, storage, and callback ownership for one request.

**Prerequisites:**

- Readers should know Objective-C blocks and protocols, Grand Central Dispatch, URL loading, operation cancellation, caches, and the basic role of image decoding and transformation.

**Concepts this path develops:**

- Objective-C blocks, protocols, categories, and operation tokens.
- Asynchronous cache-query, download, decode, transform, store, and callback chain.
- Cache-key identity, source and store policy, decoded and transformed variants, and callback queues must agree.

**What you can learn:**

- Follow an image URL through cache-key lookup, layered cache queries, loader dispatch, progressive and final decoding, cancellation, transformation, storage, and callback delivery.

**Learning path:**

- **Goal:** Understand how SDWebImage coordinates cache lookup, network loading, decoding, transformation, storage, cancellation, and callback delivery for one image request.
- **Start here:** [`SDWebImage/Core/SDWebImageManager.m`](https://github.com/SDWebImage/SDWebImage/blob/c3ad5e1a9bf55c9b76d4c362430b5fcded96c502/SDWebImage/Core/SDWebImageManager.m) — The reviewed trace begins in SDWebImageManager.m because loadImageWithURL creates the combined operation and coordinates every selected cache, loader, transform, and completion branch.
- **Then read:**
  - [`SDWebImage/Core/SDWebImageDownloaderOperation.m`](https://github.com/SDWebImage/SDWebImage/blob/c3ad5e1a9bf55c9b76d4c362430b5fcded96c502/SDWebImage/Core/SDWebImageDownloaderOperation.m)
  - [`SDWebImage/Core/SDImageCache.m`](https://github.com/SDWebImage/SDWebImage/blob/c3ad5e1a9bf55c9b76d4c362430b5fcded96c502/SDWebImage/Core/SDImageCache.m)
  - [`Tests/Tests/SDWebImageManagerTests.m`](https://github.com/SDWebImage/SDWebImage/blob/c3ad5e1a9bf55c9b76d4c362430b5fcded96c502/Tests/Tests/SDWebImageManagerTests.m)
  - [`Tests/Tests/SDWebImageDownloaderTests.m`](https://github.com/SDWebImage/SDWebImage/blob/c3ad5e1a9bf55c9b76d4c362430b5fcded96c502/Tests/Tests/SDWebImageDownloaderTests.m)
  - [`Tests/Tests/SDImageCacheTests.m`](https://github.com/SDWebImage/SDWebImage/blob/c3ad5e1a9bf55c9b76d4c362430b5fcded96c502/Tests/Tests/SDImageCacheTests.m)
  - [`README.md`](https://github.com/SDWebImage/SDWebImage/blob/c3ad5e1a9bf55c9b76d4c362430b5fcded96c502/README.md)
  - [`LICENSE`](https://github.com/SDWebImage/SDWebImage/blob/c3ad5e1a9bf55c9b76d4c362430b5fcded96c502/LICENSE)
- **Trace:** Start with loadImageWithURL and its combined operation, follow option and context normalization into cache-key lookup, original and transformed cache queries, loader dispatch, progressive and final decode results, cancellation and error branches, transformation, memory and disk storage, and callback-queue completion; then close deduplication, cancellation, cache, network, custom-component, and transformation contracts in the direct suites.

**Why this level:**

- **Language technique 3:** Substantial Objective-C framework techniques recur, without expert runtime or metaprogramming machinery.
- **Behavioral reasoning 4:** Advanced nonlocal lifecycle, race, and event-order reasoning recurs across asynchronous boundaries.
- **Design span 4:** Several major subsystems and external boundaries cooperate in one representative request path.
- **Constraint burden 5:** Several system-wide correctness, resource, concurrency, compatibility, and performance guarantees interact, meeting the expert change-discipline anchor.
- **Placement:** The four scores 3/4/4/5 sum to 16; their arithmetic mean is 4.00 and rounds half-up to Level 4. The published result is Level 4.

**License:** MIT ([evidence 1](https://github.com/SDWebImage/SDWebImage/blob/c3ad5e1a9bf55c9b76d4c362430b5fcded96c502/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** SDWebImage is released through Swift Package Manager, CocoaPods, and Carthage for production UI integrations across Apple platforms.

**Language evidence:** Image orchestration, downloader operations, memory and disk caches, coder and loader protocols, animated playback, transformations, UIKit and AppKit categories, prefetching, and tests are Objective-C.

**Coding relevance:**

That short media primer is subordinate to transferable systems lessons in asynchronous operation ownership, request deduplication, cancellation, callback queues, layered caches, loader and coder protocols, progressive results, transformations, key identity, memory pressure, persistence policy, error propagation, and race-focused integration tests.

Required domain context:

- An image-loading framework resolves a URL through cache and network sources, decodes image bytes, and returns a platform image to a caller.

**Eight-part quality gate:**

- **Source quality:** SDWebImageManager.m keeps options, context, cache type, operation tokens, cancellation, decode, transform, storage, errors, and callback queues explicit; downloader and cache files own their layers.
- **Architecture:** The manager composes cache and loader protocols, delegates transport to SDWebImageDownloaderOperation, delegates memory and disk policy to SDImageCache, and returns through a controlled callback queue.
- **Naming and idiom:** SDWebImageManager, combined operations, image cache, downloader operation, context, cache type, and completion blocks reveal the asynchronous Objective-C pipeline.
- **Tests:** Manager, downloader, and cache test suites cover duplicate URLs, custom components, cancellation races, progress, failures, decoding, transformations, expiry, memory pressure, and storage.
- **Documentation:** README.md documents the loading API, while linked project guidance explains options and extension points used by the selected path.
- **Traceability:** One URL can be followed from manager normalization through cache or loader, decode and transform, storage, and callback completion into direct component tests.
- **Maintainability:** Protocol boundaries isolate cache, loader, coder, and transform concerns, and focused suites protect their lifecycle integration.
- **Educational value:** The path is a realistic study of asynchronous orchestration in which ownership and cancellation are as important as the successful result.

**Inspection record:** commit `c3ad5e1a9bf55c9b76d4c362430b5fcded96c502`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `SDWebImage/Core/SDWebImageManager.m`, `SDWebImage/Core/SDWebImageDownloaderOperation.m`, `SDWebImage/Core/SDImageCache.m`, `Tests/Tests/SDWebImageManagerTests.m`, `Tests/Tests/SDWebImageDownloaderTests.m`, `Tests/Tests/SDImageCacheTests.m`, `README.md`, `LICENSE`. GitHub Linguist label: Objective-C.

</details>

## Level 5

### [gnachman/iTerm2](https://github.com/gnachman/iTerm2)

**Language 4 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

A full macOS terminal emulator with VT protocols, high-performance grids and rendering, sessions and process control, tmux and shell integration, automation APIs, restoration, search, transfers, profiles, and modern application features.

**Why study it:** iTerm2's state-restoration database is an expert path through cyclic graph encoding, delta persistence, transactions, identity, integrity checks, and recovery after failure.

**Prerequisites:**

- Readers should know advanced Objective-C, object graphs and cycles, stable identity, SQLite transactions, asynchronous ownership, rollback, deep copies, and state-restoration concepts.

**Concepts this path develops:**

- Objective-C graph-encodable protocols, blocks, categories, and typed records.
- Cyclic graph identity, generations, prior revision, and delta propagation.
- Object identity, cycles, generations, row IDs, graph reachability, and previous revisions must remain coherent.

**What you can learn:**

- Trace restorable state into graph records, stable identifiers and generations, prior-revision deltas, transactional SQLite rows, root publication, garbage collection, rollback, and bounded recovery.

**Learning path:**

- **Goal:** Understand how iTerm2 encodes a restorable object graph, persists only graph changes transactionally in SQLite, and recovers a consistent baseline after save or database failure.
- **Start here:** [`sources/StateRestoration/iTermGraphDatabase.m`](https://github.com/gnachman/iTerm2/blob/095009a6793f8a8c7ea7f4b8fd7fb1f3f1f834a4/sources/StateRestoration/iTermGraphDatabase.m) — The reviewed trace begins in iTermGraphDatabase.m because the database owns loading, transactional persistence, row publication, integrity, garbage collection, and recovery around encoded graph records.
- **Then read:**
  - [`sources/StateRestoration/iTermGraphEncoder.m`](https://github.com/gnachman/iTerm2/blob/095009a6793f8a8c7ea7f4b8fd7fb1f3f1f834a4/sources/StateRestoration/iTermGraphEncoder.m)
  - [`sources/StateRestoration/iTermGraphDeltaEncoder.m`](https://github.com/gnachman/iTerm2/blob/095009a6793f8a8c7ea7f4b8fd7fb1f3f1f834a4/sources/StateRestoration/iTermGraphDeltaEncoder.m)
  - [`sources/StateRestoration/iTermEncoderGraphRecord.m`](https://github.com/gnachman/iTerm2/blob/095009a6793f8a8c7ea7f4b8fd7fb1f3f1f834a4/sources/StateRestoration/iTermEncoderGraphRecord.m)
  - [`sources/StateRestoration/iTermGraphTableTransformer.m`](https://github.com/gnachman/iTerm2/blob/095009a6793f8a8c7ea7f4b8fd7fb1f3f1f834a4/sources/StateRestoration/iTermGraphTableTransformer.m)
  - [`sources/StateRestoration/iTermRestorableStateSQLite.m`](https://github.com/gnachman/iTerm2/blob/095009a6793f8a8c7ea7f4b8fd7fb1f3f1f834a4/sources/StateRestoration/iTermRestorableStateSQLite.m)
  - [`ModernTests/iTermGraphDatabaseTests.swift`](https://github.com/gnachman/iTerm2/blob/095009a6793f8a8c7ea7f4b8fd7fb1f3f1f834a4/ModernTests/iTermGraphDatabaseTests.swift)
  - [`ModernTests/iTermGraphDeltaEncoderTests.swift`](https://github.com/gnachman/iTerm2/blob/095009a6793f8a8c7ea7f4b8fd7fb1f3f1f834a4/ModernTests/iTermGraphDeltaEncoderTests.swift)
  - [`ModernTests/iTermGraphDatabaseRecoveryTests.m`](https://github.com/gnachman/iTerm2/blob/095009a6793f8a8c7ea7f4b8fd7fb1f3f1f834a4/ModernTests/iTermGraphDatabaseRecoveryTests.m)
  - [`README.md`](https://github.com/gnachman/iTerm2/blob/095009a6793f8a8c7ea7f4b8fd7fb1f3f1f834a4/README.md)
  - [`COPYING`](https://github.com/gnachman/iTerm2/blob/095009a6793f8a8c7ea7f4b8fd7fb1f3f1f834a4/COPYING)
- **Trace:** Start with graph-database initialization and load, follow state encoding into scalar and child records, stable identifiers and generations, delta comparison against the prior revision, table transformation and one SQLite transaction, row-id publication and garbage collection; then force a failed save through bounded recovery, fresh full encoding, deep-copy isolation and integrity assertions before closing persistence, delta, corruption, rollback, and recovery behavior in the modern suites.

**Why this level:**

- **Language technique 4:** Advanced Objective-C and interoperability techniques recur across encoding, persistence, and recovery.
- **Behavioral reasoning 5:** Expert nonlocal graph, persistence, lifecycle, failure, and recovery reasoning is pervasive.
- **Design span 4:** Several major subsystems and external boundaries cooperate in one bounded state-restoration slice.
- **Constraint burden 5:** Several system-wide integrity, durability, failure-recovery, security, compatibility, and performance guarantees interact.
- **Placement:** The four scores 4/5/4/5 sum to 18; their arithmetic mean is 4.50 and rounds half-up to Level 5. The published result is Level 5.

**License:** GPL-2.0-or-later ([evidence 1](https://github.com/gnachman/iTerm2/blob/095009a6793f8a8c7ea7f4b8fd7fb1f3f1f834a4/COPYING), [evidence 2](https://github.com/gnachman/iTerm2/blob/095009a6793f8a8c7ea7f4b8fd7fb1f3f1f834a4/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The repository builds and releases the iTerm2 desktop application used as a terminal replacement on macOS, plus scripting, helper, companion, and integration surfaces.

**Language evidence:** The still-dominant terminal core—byte streams, VT100 parsers and state machines, grids, screens, line buffers, sessions, process integration, selection, search, drawing, and much of the UI—is Objective-C and Objective-C++, with a substantial modern Swift layer.

**Coding relevance:**

That short application primer is subordinate to transferable expert engineering in cyclic graph encoding, stable identity and generations, delta detection, append-only transactional records, relational graph transformation, asynchronous database ownership, integrity assertions, rollback, recovery after failed saves, deep copying, garbage collection, encryption boundaries, compatibility, and real recovery tests.

Required domain context:

- State restoration serializes an application's object graph so windows and sessions can be reconstructed after relaunch; iTerm2 persists graph records in SQLite.

**Eight-part quality gate:**

- **Source quality:** iTermGraphDatabase.m exposes transaction and recovery steps, while graph encoder, delta encoder, record, transformer, and SQLite wrapper files isolate representation and persistence concerns.
- **Architecture:** An encoder turns application state into graph records, a delta encoder compares revisions, a transformer writes relational rows in one transaction, and the database publishes or recovers a consistent root.
- **Naming and idiom:** GraphDatabase, GraphEncoder, GraphDeltaEncoder, EncoderGraphRecord, GraphTableTransformer, generations, revisions, and recovery preserve the persistence model explicitly.
- **Tests:** iTermGraphDatabaseTests.swift, iTermGraphDeltaEncoderTests.swift, and iTermGraphDatabaseRecoveryTests.m exercise round trips, deltas, cycles, identity, failures, corruption, rollback, repair, and recovery.
- **Documentation:** README.md provides repository orientation, while the explicitly separated graph components make transaction, identity, integrity, rollback, and recovery responsibilities visible beside the implementation.
- **Traceability:** A restorable object can be followed through graph encoding and delta computation into a SQLite transaction, then through reload or recovery into focused modern tests.
- **Maintainability:** Encoding, change detection, table transformation, persistence, and recovery have separate boundaries, with integrity assertions and failure tests guarding cross-layer changes.
- **Educational value:** The path makes durability and recovery obligations visible in a real application subsystem without requiring the terminal emulator's unrelated breadth.

**Inspection record:** commit `095009a6793f8a8c7ea7f4b8fd7fb1f3f1f834a4`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `sources/StateRestoration/iTermGraphDatabase.m`, `sources/StateRestoration/iTermGraphEncoder.m`, `sources/StateRestoration/iTermGraphDeltaEncoder.m`, `sources/StateRestoration/iTermEncoderGraphRecord.m`, `sources/StateRestoration/iTermGraphTableTransformer.m`, `sources/StateRestoration/iTermRestorableStateSQLite.m`, `ModernTests/iTermGraphDatabaseTests.swift`, `ModernTests/iTermGraphDeltaEncoderTests.swift`, `ModernTests/iTermGraphDatabaseRecoveryTests.m`, `README.md`, `COPYING`, `LICENSE`. GitHub Linguist label: Objective-C.

</details>

### [gnustep/libs-base](https://github.com/gnustep/libs-base)

**Language 5 / Behavior 5 / Design 3 / Constraints 5 → Level 5**

GNUstep's cross-platform implementation of the non-graphical OpenStep and Cocoa Foundation APIs, from root objects and collections through run loops, networking, serialization, localization, processes, and distributed objects.

**Why study it:** GNUstep's notification center is an expert Foundation-compatible implementation of wildcard registration, weak observer identity, reentrant callbacks, and thread-safe removal.

**Prerequisites:**

- Readers should know advanced Objective-C runtime dispatch, selectors and blocks, weak references, hash tables, locks, callback reentrancy, and the observer notification pattern.

**Concepts this path develops:**

- Manual Objective-C runtime selector dispatch and weak observer identity.
- Wildcard, name, object, observer, selector, and block matching across several indexes.
- Wildcard matching, duplicate registration, scoped removal, callback order, and Foundation compatibility must remain exact.

**What you can learn:**

- Trace selector and block observers into wildcard indexes and locks, then follow snapshot-based synchronous posting, reentrant mutation, queued delivery, exceptions, removal, and lifetime races.

**Learning path:**

- **Goal:** Understand how GNUstep implements a reentrant, thread-safe Foundation-compatible notification center with exact wildcard, observer-lifetime, selector, and block-delivery semantics.
- **Start here:** [`Source/NSNotificationCenter.m`](https://github.com/gnustep/libs-base/blob/795e88205b20cf372296af5b4d727aa68718fb6a/Source/NSNotificationCenter.m) — The reviewed trace begins in NSNotificationCenter.m because it contains observation storage, registration indexes, posting snapshots, callback delivery, and removal synchronization.
- **Then read:**
  - [`Source/NSNotification.m`](https://github.com/gnustep/libs-base/blob/795e88205b20cf372296af5b4d727aa68718fb6a/Source/NSNotification.m)
  - [`Headers/Foundation/NSNotification.h`](https://github.com/gnustep/libs-base/blob/795e88205b20cf372296af5b4d727aa68718fb6a/Headers/Foundation/NSNotification.h)
  - [`Tests/base/NSNotification/basic.m`](https://github.com/gnustep/libs-base/blob/795e88205b20cf372296af5b4d727aa68718fb6a/Tests/base/NSNotification/basic.m)
  - [`Tests/base/NSNotification/general.m`](https://github.com/gnustep/libs-base/blob/795e88205b20cf372296af5b4d727aa68718fb6a/Tests/base/NSNotification/general.m)
  - [`Tests/base/NSNotification/dynamic.m`](https://github.com/gnustep/libs-base/blob/795e88205b20cf372296af5b4d727aa68718fb6a/Tests/base/NSNotification/dynamic.m)
  - [`README.md`](https://github.com/gnustep/libs-base/blob/795e88205b20cf372296af5b4d727aa68718fb6a/README.md)
  - [`COPYING.LIB`](https://github.com/gnustep/libs-base/blob/795e88205b20cf372296af5b4d727aa68718fb6a/COPYING.LIB)
  - [`COPYING`](https://github.com/gnustep/libs-base/blob/795e88205b20cf372296af5b4d727aa68718fb6a/COPYING)
- **Trace:** Start with the observation record and notification tables, follow addObserver into wildcard, name, object, receiver and selector indexes under recursive and striped locks, then trace postNotification through matching-list snapshots, unlock-before-callback delivery, selector or queued block invocation, reentrant mutation, exception and cleanup paths; finish with scoped and total removal, observer lifetime, nested posting, wildcard, mutation, and threading contracts in the three focused suites.

**Why this level:**

- **Language technique 5:** Multiple expert Objective-C runtime, ownership, data-structure, callback, and synchronization mechanisms interact pervasively.
- **Behavioral reasoning 5:** Expert nonlocal identity, matching, event-order, reentrancy, ownership, and concurrency reasoning is pervasive.
- **Design span 3:** Several meaningful runtime-library units cooperate, while the path remains one bounded Foundation subsystem.
- **Constraint burden 5:** Several system-wide correctness, lifetime, concurrency, reentrancy, compatibility, portability, and performance guarantees interact.
- **Placement:** The four scores 5/5/3/5 sum to 18; their arithmetic mean is 4.50 and rounds half-up to Level 5. The published result is Level 5.

**License:** LGPL-2.0-or-later AND GPL-2.0-only ([evidence 1](https://github.com/gnustep/libs-base/blob/795e88205b20cf372296af5b4d727aa68718fb6a/README.md), [evidence 2](https://github.com/gnustep/libs-base/blob/795e88205b20cf372296af5b4d727aa68718fb6a/COPYING.LIB), [evidence 3](https://github.com/gnustep/libs-base/blob/795e88205b20cf372296af5b4d727aa68718fb6a/COPYING))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** GNUstep Base is a released runtime library used by GNUstep applications and command-line software to provide Foundation-style APIs across Unix-like systems and Windows.

**Language evidence:** The Foundation-compatible object model, strings and collections, coding, dates and locales, files, processes and threads, run loops, notifications, predicates, XML, networking, URL loading, distributed objects, and public headers are predominantly Objective-C with supporting C.

**Coding relevance:**

That short framework primer is subordinate to transferable expert library engineering in Objective-C runtime dispatch, weak observer identity, selector and block APIs, wildcard indexing, custom allocation, striped and recursive locking, snapshotting before callbacks, reentrant add and remove, deallocation races, queued delivery, exception safety, compatibility, and concurrency tests.

Required domain context:

- A notification center registers observers by optional notification name and object and synchronously dispatches matching notifications; nil names or objects act as wildcards.

**Eight-part quality gate:**

- **Source quality:** NSNotificationCenter.m makes wildcard dimensions, custom observation records, indexes, striped and recursive locks, snapshots, deferred release, and callback paths explicit.
- **Architecture:** Registrations enter name, object, receiver, selector, or block indexes; posting snapshots matching observations under locks and invokes callbacks after unlocking; removal updates the same structures safely.
- **Naming and idiom:** NSNotificationCenter, NSNotification, addObserver, postNotification, removeObserver, selector, object, and name mirror Foundation contracts while exposing GNUstep internals.
- **Tests:** basic.m, general.m, and dynamic.m cover construction, selectors, blocks, wildcard combinations, duplicates, scoped removal, mutation during posting, nested posts, lifetimes, threads, and compatibility.
- **Documentation:** NSNotification.h documents the public notification contract, and README.md provides the GNUstep Base context needed to compare the implementation with Foundation behavior.
- **Traceability:** An observer registration can be followed into indexes and locks, through a posting snapshot and callback, and into removal and direct compatibility tests.
- **Maintainability:** Observation records and indexes centralize policy, lock boundaries are explicit, and focused suites exercise reentrancy and lifetime cases that ordinary tests often miss.
- **Educational value:** The path reveals the concurrency and ownership engineering required to reproduce a deceptively simple observer API faithfully.

**Inspection record:** commit `795e88205b20cf372296af5b4d727aa68718fb6a`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `Source/NSNotificationCenter.m`, `Source/NSNotification.m`, `Headers/Foundation/NSNotification.h`, `Tests/base/NSNotification/basic.m`, `Tests/base/NSNotification/general.m`, `Tests/base/NSNotification/dynamic.m`, `README.md`, `COPYING.LIB`, `COPYING`. GitHub Linguist label: Objective-C.

</details>

_Generated from `catalog/objective-c.json`; do not edit by hand._

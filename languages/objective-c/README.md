# Objective-C

10 qualified repositories. Scores assume the learner described in [the SDC rubric](../../docs/sdc.md).

[← All languages](../README.md)

## SDC 1

### [mirego/MCUIViewLayout](https://github.com/mirego/MCUIViewLayout)

**S1 / D2 / C1 → SDC 1**

A small UIView layout library for sizing and positioning views against superviews and siblings with explicit geometry helpers.

**Real-world evidence:** The repository distributes Objective-C and Swift package products and documents UIKit use through Swift Package Manager and CocoaPods.

**Language evidence:** The original and still-shipped geometry model, UIView calculation categories, frame mutation methods, compatibility facade, and XCTest suite are Objective-C.

**Why study it:** It turns repetitive frame arithmetic into a bounded vocabulary while leaving every CGRect calculation, margin rule, display-scale rounding choice, and category method visible.

**What you can learn:**

- Objective-C categories, NS_OPTIONS bitmasks, CGRect arithmetic, sibling and superview coordinates, display-scale rounding, compatibility, and geometry tests.

**Prerequisites:**

- Objective-C methods and categories, UIKit views and frames, C structs and bitmasks, coordinate systems, floating-point rounding, and XCTest.

**Start here:** [`Sources/MCUIViewLayoutObjC/UIView+MCLayoutCalculation.m`](https://github.com/mirego/MCUIViewLayout/blob/987cb7ee525f03aeae81db7e3ad639080e23bc46/Sources/MCUIViewLayoutObjC/UIView+MCLayoutCalculation.m) — The calculation category expresses the geometry rules without mutation; the public category then applies returned rectangles to views.

**Why this level:**

- **S1:** 716 meaningful implementation LOC measured with tokei 14.0.0. Count covers all production Objective-C and public headers under Sources/MCUIViewLayoutObjC, excluding the parallel Swift implementation.
- **D2:** Geometry combinations and pixel rounding need precision, but each rule is deterministic and uses familiar UIKit primitives.
- **C1:** The library has one in-process responsibility and a short path from a position request to a frame.
- **Placement:** S1/D2/C1 averages to 1.33, making MCUIViewLayout an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** Pure calculation methods separate geometry from frame mutation, combinations are explicit, and scale-aware rounding avoids blurred half-pixel placement.
- **Architecture:** A position model and calculation category define geometry; a public UIView category applies it; a deprecated facade isolates compatibility.
- **Naming and idiom:** mc_setPosition, relativeToView, withMargins, sizeToFit, mc_width, mc_origin, and MCUIViewLayoutPosition state layout intent directly.
- **Tests:** Nine XCTest files cover base dimensions, all superview alignments, sibling relationships, fitting, combined operations, missing parents, unequal margins, and display-scale rounding.
- **Documentation:** The README walks through z-order, sizing, absolute, parent-relative, and sibling-relative layout with diagrams and examples.
- **Traceability:** A position option can be followed from its bitmask through a calculation helper into frame mutation and an exact CGRect assertion.
- **Maintainability:** The Objective-C implementation is compact, calculation logic is reusable, compatibility code is isolated, and geometry cases are enumerated in focused suites.
- **Educational value:** It demonstrates how a small convenience API can improve call-site language while preserving transparent, testable arithmetic.

**Inspection record:** commit `987cb7ee525f03aeae81db7e3ad639080e23bc46`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Sources/MCUIViewLayoutObjC/MCUIViewLayoutPosition.m`, `Sources/MCUIViewLayoutObjC/UIView+MCLayoutCalculation.m`, `Sources/MCUIViewLayoutObjC/UIView+MCLayout.m`, `MCUIViewLayoutExample/UIViewLayoutExampleTests/UIView_MCLayoutCalculationsTest.m`, `LICENSE.md`. GitHub Linguist label: Objective-C. LOC exclusions: Sources/MCUIViewLayout/, MCUIViewLayoutExample/, documentation and package metadata.

**License:** [BSD-3-Clause](https://github.com/mirego/MCUIViewLayout/blob/987cb7ee525f03aeae81db7e3ad639080e23bc46/LICENSE.md)

### [shinyfrog/TextBundle](https://github.com/shinyfrog/TextBundle)

**S1 / D2 / C1 → SDC 1**

A compact framework for reading, creating, and writing TextBundle document packages with metadata, text, and optional assets.

**Real-world evidence:** The framework implements the TextBundle interchange format used by writing applications and ships macOS and iOS targets.

**Language evidence:** TextBundle package reading and writing, metadata projection, Uniform Type Identifier handling, asset collision handling, errors, and tests are Objective-C.

**Why study it:** A few files expose the complete path from an on-disk directory package through NSFileWrapper, JSON metadata, text type selection, attachments, validation, and atomic persistence.

**What you can learn:**

- Objective-C properties, NSFileWrapper packages, JSON serialization, Uniform Type Identifiers, NSError conventions, metadata preservation, asset filenames, and fixture tests.

**Prerequisites:**

- Objective-C classes and properties, Foundation collections and data, files and URLs, JSON, nullable errors, and document packages.

**Start here:** [`TextBundle/TextBundleWrapper.m`](https://github.com/shinyfrog/TextBundle/blob/eb0e2c75afec3817cf6817548179fe679ba565ee/TextBundle/TextBundleWrapper.m) — The implementation can be read end to end, from defaults through file-wrapper construction, parsing, validation, assets, and filename generation.

**Why this level:**

- **S1:** 246 meaningful implementation LOC measured with tokei 14.0.0. Count covers the shared Objective-C implementation and public headers used by both platform targets.
- **D2:** Serialization and filesystem edges require care, but Foundation supplies the storage machinery and transformations remain direct.
- **C1:** One cohesive class owns a small format without asynchronous, service, plugin, or process coordination.
- **Placement:** S1/D2/C1 averages to 1.33, making TextBundle an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** Required-file checks, metadata extraction, asset deduplication, package construction, and errors are visible in short methods over Foundation values.
- **Architecture:** One shared wrapper contains the format behavior while thin macOS and iOS targets expose it.
- **Naming and idiom:** info.json, textFilenameForType, fileWrapper, metadata, assetsFileWrapper, readFromURL, and writeToURL mirror the package vocabulary.
- **Tests:** Fixtures cover text-only and attachment packages, missing members, invalid input, creation, writing, and asset collisions; one write-to-new-URL test mistakenly reloads its source fixture, so it is not a complete persistence round trip.
- **Documentation:** The README explains the TextBundle format, platform targets, installation, and wrapper role.
- **Traceability:** A bundle can be followed from NSFileWrapper through info.json and text selection into properties, then back through fileWrapper and writeToURL.
- **Maintainability:** Format constants and transformations are centralized, the surface is narrow, and representative packages live beside the tests.
- **Educational value:** It is an approachable first study of mapping a real document format onto Foundation without a framework-sized abstraction.

**Inspection record:** commit `eb0e2c75afec3817cf6817548179fe679ba565ee`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `TextBundle/TextBundleWrapper.h`, `TextBundle/TextBundleWrapper.m`, `TextBundleTests/TextBundleTests.m`, `TextBundleTests/Sample TextBundles/text plus attachments.textbundle/info.json`, `LICENSE`. GitHub Linguist label: Objective-C. LOC exclusions: TextBundleTests/, example applications, framework wrappers, resources, documentation, and project metadata.

**License:** [MIT](https://github.com/shinyfrog/TextBundle/blob/eb0e2c75afec3817cf6817548179fe679ba565ee/LICENSE)

## SDC 2

### [pinterest/PINOperation](https://github.com/pinterest/PINOperation)

**S1 / D3 / C2 → SDC 2**

A thread-safe operation queue with priorities, dynamic concurrency limits, cancellation, data coalescing, completions, and operation groups.

**Real-world evidence:** Pinterest maintains and releases PINOperation as an Apple-platform library through Swift Package Manager and CocoaPods.

**Language evidence:** Priority scheduling, serial and bounded-concurrent execution, cancellation, coalescing, grouped operations, synchronization, and tests are Objective-C over Grand Central Dispatch and pthread mutexes.

**Why study it:** Its small surface reveals recursive locks, serial and concurrent lanes, semaphores, dispatch groups, priority queues, weak reference maps, duplicate-work coalescing, and nested work.

**What you can learn:**

- Grand Central Dispatch queues, groups, and semaphores, pthread mutexes, bounded concurrency, priorities, cancellation, coalescing, completion fan-out, and asynchronous XCTest.

**Prerequisites:**

- Comfortable Objective-C, blocks, Foundation collections, Grand Central Dispatch, mutexes and semaphores, race conditions, cancellation, and asynchronous tests.

**Start here:** [`Source/PINOperationQueue.m`](https://github.com/pinterest/PINOperation/blob/a74f978733bdaf982758bfa23d70a189f4b4c1b6/Source/PINOperationQueue.m) — The queue connects registration, priority buckets, locking, serial and concurrent dispatch, cancellation, coalescing, dynamic limits, and completion accounting.

**Why this level:**

- **S1:** 586 meaningful implementation LOC measured with tokei 14.0.0. Count covers every production implementation and public header under Source.
- **D3:** Correctness depends on ordering and shared-state invariants, but the scheduler uses a small set of explicit queues and lock-protected collections.
- **C2:** Several lifecycle paths interact inside one in-process scheduling library with two principal classes.
- **Placement:** S1/D3/C2 averages to 2.00, making PINOperation an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** Lock boundaries, queue membership, dispatch-group accounting, completion ownership, semaphore changes, and cancellation results are explicit.
- **Architecture:** PINOperationQueue owns scheduling and references; an internal record holds work; PINOperationGroup batches operations and completion under separate synchronization.
- **Naming and idiom:** scheduleOperation, withPriority, coalescingData, cancelOperation, waitUntilAllOperationsAreFinished, operationReference, and completion expose scheduler semantics.
- **Tests:** Tests cover execution and release, nested waiting without deadlock, concurrency limits including one, priority, cancellation, priority changes, coalesced data and completions, groups, and runtime limit changes.
- **Documentation:** The README explains serial and concurrent behavior, priority, cancellation, coalescing, groups, installation, and the public API.
- **Traceability:** A block can be followed from reference allocation into a priority set, dispatch lane, completion, group leave, and a synchronization-focused assertion.
- **Maintainability:** A narrow API, two synchronized components, invariant-preserving private helpers, and regression tests constrain a concurrency-heavy implementation.
- **Educational value:** It is a compact bridge from basic dispatch queues to designing and testing a reusable concurrent scheduler.

**Inspection record:** commit `a74f978733bdaf982758bfa23d70a189f4b4c1b6`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Source/PINOperationQueue.h`, `Source/PINOperationQueue.m`, `Source/PINOperationGroup.m`, `Tests/PINOperationQueueTests.m`, `Tests/PINOperationGroupTests.m`, `LICENSE.txt`. GitHub Linguist label: Objective-C. LOC exclusions: Tests/, Example/, docs/.

**License:** [Apache-2.0](https://github.com/pinterest/PINOperation/blob/a74f978733bdaf982758bfa23d70a189f4b4c1b6/LICENSE.txt)

### [SBJson/SBJson](https://github.com/SBJson/SBJson)

**S1 / D3 / C2 → SDC 2**

A streaming Objective-C JSON parser and writer that accepts chunks, emits complete values or array elements, and supports bounded depth and deterministic formatting.

**Real-world evidence:** SBJson ships a versioned CocoaPod and framework API for applications needing incremental JSON processing or compatibility with its long-lived interface.

**Language evidence:** Incremental UTF-8 tokenization, parser and writer state machines, Objective-C value construction, streaming callbacks, formatting, errors, and tests are Objective-C.

**Why study it:** Every layer of streaming serialization is inspectable: retained chunks, strict UTF-8 validation, lexical tokens, nested parser states, Foundation value assembly, writer states, formatting, and delegate output.

**What you can learn:**

- Incremental tokenization, UTF-8 and surrogate validation, parser state, chunk boundaries, block callbacks, streaming JSON generation, deterministic sorting, error locations, and corpus tests.

**Prerequisites:**

- Objective-C and Foundation collections, bytes and encodings, JSON grammar, finite-state machines, callbacks, recursion and stacks, numeric conversion, and unit testing.

**Start here:** [`Classes/SBJson5StreamTokeniser.m`](https://github.com/SBJson/SBJson/blob/93e4ca5c274488fb745429977308d85929c5f13a/Classes/SBJson5StreamTokeniser.m) — The tokeniser shows how partial buffers, strings, escapes, Unicode, numbers, literals, whitespace, and error offsets feed higher parser states.

**Why this level:**

- **S1:** 1,702 meaningful implementation LOC measured with tokei 14.0.0. Count covers all production Objective-C and public headers in Classes.
- **D3:** Streaming and encoding correctness create subtle transitions, but lexical, structural, value, and writing concerns are separated.
- **C2:** Several cohesive components implement one data format without network, process, or plugin topology.
- **Placement:** S1/D3/C2 averages to 2.00, making SBJson an SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** Consumed offsets, partial buffers, byte availability, Unicode legality, depth, parser completion states, and writer errors are explicit and guarded.
- **Architecture:** A tokeniser feeds a structural parser; adapters assemble Foundation values or unwrap arrays; a separate writer state machine emits bytes through a delegate.
- **Naming and idiom:** WaitingForData, Complete, multiRootParser, unwrapRootArrayParser, getToken, stateStack, errorHandler, humanReadable, and sortKeys describe the contract.
- **Tests:** Thirty-six test methods drive large conformance fixtures for syntax, UTF-8, chunk streams, round trips, writer states, formatting, decimals, proxies, and error text; the repository also documents fuzzing.
- **Documentation:** The README explains chunk parsing, multiple roots, root-array unwrapping, type mapping, depth, formatting, compatibility, installation, limitations, and fuzzing.
- **Traceability:** Bytes can be followed through token recognition, parser state, Foundation construction, callback delivery, writer state, and fixture comparison.
- **Maintainability:** Versioned symbols, separated states, bounded buffers and depth, standard corpora, and stable-package maintenance protect a compact parser.
- **Educational value:** It is a small but substantive study of production parsing where chunk boundaries and encodings cannot be hand-waved.

**Inspection record:** commit `93e4ca5c274488fb745429977308d85929c5f13a`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Classes/SBJson5StreamTokeniser.m`, `Classes/SBJson5StreamParser.m`, `Classes/SBJson5StreamWriter.m`, `Tests/MainSuite.m`, `Tests/JsonStreamTokeniserTest.m`, `LICENSE`. GitHub Linguist label: Objective-C. LOC exclusions: Tests/, TestData/, SBJson5_iOSTests/, SBJson5_macOSTests/, sbjson/.

**License:** [BSD-3-Clause](https://github.com/SBJson/SBJson/blob/93e4ca5c274488fb745429977308d85929c5f13a/LICENSE)

## SDC 3

### [openid/AppAuth-iOS](https://github.com/openid/AppAuth-iOS)

**S2 / D4 / C3 → SDC 3**

A standards-oriented OAuth 2.0 and OpenID Connect client SDK for native Apple applications, including PKCE, discovery, refresh, registration, logout, and device authorization.

**Real-world evidence:** The OpenID Foundation project releases AppAuth through CocoaPods, Swift Package Manager, Carthage, and framework targets for production iOS, macOS, Catalyst, and tvOS clients.

**Language evidence:** OAuth and OpenID Connect models, discovery, PKCE, token exchange and refresh, authorization state, external user agents, loopback redirects, tvOS device flow, secure coding, and tests are Objective-C.

**Why study it:** It maps security protocols onto explicit request and response objects, browser handoff, redirect validation, token state, freshness coordination, persistence, discovery, and platform adapters without hiding the standards.

**What you can learn:**

- OAuth 2.0 and OpenID Connect, PKCE, native browser authorization, request and response models, query encoding, discovery, refresh coalescing, ID tokens, secure persistence, redirects, device flow, and protocol tests.

**Prerequisites:**

- Comfortable Objective-C, blocks and asynchronous APIs, HTTP and URLs, OAuth 2.0 and OpenID Connect, hashes and randomness, secure coding, browser redirects, and network-model testing.

**Start here:** [`Sources/AppAuthCore/OIDAuthState.m`](https://github.com/openid/AppAuth-iOS/blob/a972daac82d449d58ab119e91c68153e29ddac33/Sources/AppAuthCore/OIDAuthState.m) — OIDAuthState ties authorization and token responses to expiration, refresh exchange, pending action coalescing, error state, delegates, and secure serialization.

**Why this level:**

- **S2:** 6,462 meaningful implementation LOC measured with tokei 14.0.0. Count covers all production Objective-C and public headers under Sources.
- **D4:** Correctness depends on several security standards and platform lifecycle rules, even though the implementation mirrors protocol concepts deliberately.
- **C3:** Multiple flows and platform boundaries cooperate within one client SDK while retaining a common model layer.
- **Placement:** S2/D4/C3 averages to 3.00, making AppAuth an SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** Protocol fields, required parameters, extensions, redirect and issuer checks, PKCE material, expiry tolerance, pending refresh actions, secure coding, and error domains are explicit.
- **Architecture:** AppAuthCore models standards and exchanges; OIDAuthState owns continuity; platform modules implement external agents and redirects; AppAuthTV adds device flow.
- **Naming and idiom:** OIDAuthorizationRequest, OIDTokenResponse, OIDAuthState, performActionWithFreshTokens, additionalParameters, externalUserAgent, and serviceDiscovery preserve standards vocabulary.
- **Tests:** Suites cover every request and response model, query encoding, discovery, registration, scopes, grant and response types, token utilities, auth-state persistence and refresh, URL-session injection, tvOS flow, Swift bridging, and regressions.
- **Documentation:** The README teaches standards, platforms, security posture, configuration, discovery, authorization, redirects, persistence, refresh, logout, device flow, and installation; DESIGN.md records scope.
- **Traceability:** A native authorization can be followed from configuration and PKCE through browser redirect into token exchange, OIDAuthState persistence, refresh, and exact model tests.
- **Maintainability:** Near-one-to-one models, field mapping, explicit scope, platform isolation, extension dictionaries, and comprehensive tests reduce provider-specific hacks.
- **Educational value:** It teaches how a security protocol becomes a usable SDK without erasing the checks and state transitions applications rely on.

**Inspection record:** commit `a972daac82d449d58ab119e91c68153e29ddac33`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `DESIGN.md`, `Sources/AppAuthCore/OIDAuthState.m`, `Sources/AppAuthCore/OIDAuthorizationService.m`, `Sources/AppAuthCore/OIDAuthorizationRequest.m`, `UnitTests/OIDAuthStateTests.m`, `LICENSE`. GitHub Linguist label: Objective-C. LOC exclusions: UnitTests/, Examples/, framework wrapper targets.

**License:** [Apache-2.0](https://github.com/openid/AppAuth-iOS/blob/a972daac82d449d58ab119e91c68153e29ddac33/LICENSE)

### [SDWebImage/SDWebImage](https://github.com/SDWebImage/SDWebImage)

**S3 / D3 / C3 → SDC 3**

An asynchronous image loading and caching framework for Apple platforms with codecs, progressive and animated images, transformations, prefetching, and extensible cache and loader pipelines.

**Real-world evidence:** SDWebImage is released through Swift Package Manager, CocoaPods, and Carthage for production UI integrations across Apple platforms.

**Language evidence:** Image orchestration, downloader operations, memory and disk caches, coder and loader protocols, animated playback, transformations, UIKit and AppKit categories, prefetching, and tests are Objective-C.

**Why study it:** It connects a simple image-view call to request deduplication, cancellation, progress, decoding, memory and disk policy, cache keys, transformations, animated frames, platform drawing, and UI lifecycle safety.

**What you can learn:**

- Asynchronous operations, URLSession downloading, request deduplication, cancellation, memory and disk caching, image codecs and metadata, progressive decoding, animated playback, transformations, prefetching, extension protocols, and UI categories.

**Prerequisites:**

- Advanced Objective-C, blocks and queues, URLSession, UIKit or AppKit images, files and caches, image formats, cancellation, protocols, memory pressure, and integration testing.

**Start here:** [`SDWebImage/Core/SDWebImageManager.m`](https://github.com/SDWebImage/SDWebImage/blob/c3ad5e1a9bf55c9b76d4c362430b5fcded96c502/SDWebImage/Core/SDWebImageManager.m) — The manager computes keys, queries original and transformed images, delegates loading, decodes and transforms results, stores them, tracks operations, and handles cancellation.

**Why this level:**

- **S3:** 15,357 meaningful implementation LOC measured with tokei 14.0.0. Count covers production Objective-C and public headers in SDWebImage and SDWebImageMapKit.
- **D3:** Concurrency and media behavior recur, but components expose strong protocols and operation boundaries.
- **C3:** Several substantial subsystems cooperate through one image-loading lifecycle.
- **Placement:** S3/D3/C3 makes SDWebImage a balanced SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** Cache type, source, decode options, transformation keys, cancellation, callback queues, errors, metadata, and platform branches use explicit values and guarded transitions.
- **Architecture:** SDWebImageManager composes cache and loader protocols; downloader operations own transport; coder managers own formats; caches implement policy; categories and prefetchers provide application surfaces.
- **Naming and idiom:** loadImageWithURL, queryCacheOperation, cacheType, cacheKey, imageLoader, imageCoder, transformer, progressiveLoad, context, and completedBlock define the pipeline.
- **Tests:** Large suites cover downloads, authentication, HTTP failures, cancellation races, duplicate URLs, progressive formats, cache expiry, memory pressure, custom components, transformations, codecs, animation, prefetching, UI reuse, transitions, and regressions.
- **Documentation:** The README and wiki document integrations, loaders, caches, coders, animated images, transformers, options, context, platforms, installation, migration, and extensions.
- **Traceability:** An image-view URL can be followed through its category, manager, cache, downloader, coder, transformation, storage, operation token, and a focused async test.
- **Maintainability:** Protocol boundaries, immutable configuration copies, operation objects, private helpers, option typing, platform macros, and broad regression suites contain a mature compatibility surface.
- **Educational value:** It reveals the systems work hidden behind a familiar UI convenience API while remaining a single inspectable framework.

**Inspection record:** commit `c3ad5e1a9bf55c9b76d4c362430b5fcded96c502`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `SDWebImage/Core/SDWebImageManager.m`, `SDWebImage/Core/SDWebImageDownloaderOperation.m`, `SDWebImage/Core/SDImageCache.m`, `Tests/Tests/SDWebImageManagerTests.m`, `Tests/Tests/SDWebImageDownloaderTests.m`, `LICENSE`. GitHub Linguist label: Objective-C. LOC exclusions: Tests/, Examples/, WebImage/, Docs/.

**License:** [MIT](https://github.com/SDWebImage/SDWebImage/blob/c3ad5e1a9bf55c9b76d4c362430b5fcded96c502/LICENSE)

## SDC 4

### [kstenerud/KSCrash](https://github.com/kstenerud/KSCrash)

**S3 / D5 / C4 → SDC 4**

An Apple-platform crash-reporting framework that records Mach exceptions, signals, C++ and Objective-C exceptions, hangs, resource terminations, thread and binary-image state, and durable reports.

**Real-world evidence:** KSCrash is released as modular Swift Package Manager and CocoaPods products for on-device crash capture, report storage, processing, diagnosis, and delivery.

**Language evidence:** The public framework, installation, reports and stores, filters and sinks, Apple-platform monitors, and substantial low-level recorder portions are Objective-C, supported by first-party C and a smaller Swift model layer.

**Why study it:** It confronts corrupted processes, suspended threads, signal safety, Mach state, unwinding, Objective-C runtime inspection, sidecar durability, symbolication, report repair, and post-crash delivery.

**What you can learn:**

- Crash-handler architecture, Mach exceptions and signals, async-signal safety, machine contexts and unwinding, runtime inspection, binary images and symbols, watchdog hangs, lifecycle sidecars, crash-safe JSON, report stores, filters, sinks, and concurrency tests.

**Prerequisites:**

- Advanced Objective-C and C, Apple process and thread internals, signals and Mach APIs, stack concepts, atomics and locks, files and memory mapping, runtime metadata, JSON, and postmortem debugging.

**Start here:** [`Sources/KSCrashRecordingCore/KSCrashMonitor.c`](https://github.com/kstenerud/KSCrash/blob/8649e0727ef4506f3cf910453eb0f2481321e8ab/Sources/KSCrashRecordingCore/KSCrashMonitor.c) — The monitor registry shows how crash sources are installed, gated for debugger and async safety, supplied callbacks, and routed into common capture.

**Why this level:**

- **S3:** 31,188 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production Objective-C, C, C++, Swift, and headers under Sources.
- **D5:** The recorder must extract trustworthy state while ordinary allocation, locking, and runtime operations may be unsafe, and errors can destroy the only evidence.
- **C4:** Many modules cooperate across crash time and later processing, but remain a modular in-application framework.
- **Placement:** S3/D5/C4 averages to 4.00; the D5 floor also requires at least SDC 4.

**Quality-gate evidence:**

- **Source quality:** Crash-time and normal-time APIs are separated, capabilities and IDs are explicit, unsafe operations are isolated, sidecar formats are versioned, and report results preserve partial failures.
- **Architecture:** RecordingCore owns low-level capture and monitors; Recording exposes configuration and stores; models, filters, installations, sinks, profilers, and optional monitors layer around it.
- **Naming and idiom:** KSCrashMonitorAPI, machineContext, stackCursor, binaryImage, reportWriter, runSidecar, crashedLastLaunch, reportStore, filter, sink, and installation define the domain.
- **Tests:** Roughly 1,450 named tests and benchmarks cover monitors, signals, Mach state, threads, unwinding, symbols, JSON, files, key-value durability, corrupt sidecars, lifecycle stitching, hangs, reports, stores, filters, concurrency, Swift models, and regressions.
- **Documentation:** The README documents configuration, monitors, hangs, resource terminations, CPU and memory tracking, user data, reports, delivery, modules, deprecations, and platform caveats; headers explain safety contracts.
- **Traceability:** A signal or Mach exception can be followed from its monitor through context capture and stack cursor into the crash-safe writer, stored report, next-launch stitching, model, sink, and a targeted test.
- **Maintainability:** Fine-grained modules, C APIs at crash-time boundaries, plugin registration, versioned sidecars, destructive fixtures, benchmarks, and migration shims contain exceptional platform risk.
- **Educational value:** It is a deep systems example of engineering for the moment when the process itself can no longer be trusted.

**Inspection record:** commit `8649e0727ef4506f3cf910453eb0f2481321e8ab`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Sources/KSCrashRecording/include/KSCrash.h`, `Sources/KSCrashRecording/KSCrash.m`, `Sources/KSCrashRecordingCore/KSCrashMonitor.c`, `Sources/KSCrashRecordingCore/include/KSCrashMonitor.h`, `Tests/KSCrashRecordingTests/KSCrashMonitor_Signal_Tests.m`, `LICENSE`. GitHub Linguist label: Objective-C. LOC exclusions: Tests/, Benchmarks/, Samples/, Sources/KSCrashTestTools/.

**License:** [MIT](https://github.com/kstenerud/KSCrash/blob/8649e0727ef4506f3cf910453eb0f2481321e8ab/LICENSE)

### [sparkle-project/Sparkle](https://github.com/sparkle-project/Sparkle)

**S3 / D5 / C4 → SDC 4**

A secure macOS software-update framework with signed appcasts, background downloads, delta updates, sandbox support, privilege-separated installation, phased rollouts, resumable updates, and customizable UI.

**Real-world evidence:** Sparkle is released as a framework, Swift package, command-line tool, and supporting services used by independently distributed macOS applications.

**Language evidence:** Updater scheduling and drivers, appcast parsing, signature and code-signing validation, downloading, extraction and installation, XPC services, UI, version comparison, CLI integration, and core tests are predominantly Objective-C.

**Why study it:** It shows an end-to-end security-sensitive lifecycle across untrusted feeds and archives, signatures, code identities, processes, XPC protocols, installation plans, atomic replacement, relaunch, scheduling, and recovery.

**What you can learn:**

- Secure updater threat models, EdDSA and code signing, privilege separation, XPC and secure coding, appcasts and version policy, download and extraction, atomic installation, sandboxing, delta updates, resumability, drivers, and failure recovery.

**Prerequisites:**

- Advanced Objective-C and Cocoa, macOS bundles and code signing, signature concepts, XPC and launchd, sandboxing and privileges, atomic files, networking, state machines, and security testing.

**Start here:** [`Sparkle/SPUUpdater.m`](https://github.com/sparkle-project/Sparkle/blob/164f2fd30f7b6feb60596246322648a784dd308c/Sparkle/SPUUpdater.m) — SPUUpdater validates host configuration and policy, selects drivers, coordinates schedules and sessions, resumes work, exposes state, and bridges the host to installation.

**Why this level:**

- **S3:** 20,735 meaningful implementation LOC measured with tokei 14.0.0. Count covers the framework, updater agents, downloader and installer services, connection and status services, and sparkle-cli.
- **D5:** A mistake can turn remote update input or a privilege boundary into code execution or application loss, requiring adversarial reasoning across macOS security mechanisms.
- **C4:** Many components and modes form a production updater, though they remain one product rather than a multi-service platform.
- **Placement:** S3/D5/C4 averages to 4.00; the D5 floor also requires at least SDC 4.

**Quality-gate evidence:**

- **Source quality:** Configuration preconditions, thread rules, public keys, transport warnings, code identities, secure decoding classes, XPC availability, states, invalidation, and recovery are explicit and contextual.
- **Architecture:** SPUUpdater and protocol-based drivers orchestrate work; downloader and installer services separate privileges; agents handle progress and installation; validators bind feeds, archives, signatures, and host identity.
- **Naming and idiom:** SPUUpdater, UpdateDriver, UserDriver, appcast, resumableUpdate, SUUpdateValidator, InstallerLauncher, SecureCoding, allowedChannels, and phased rollout expose roles.
- **Tests:** Core suites contain 184 named tests across appcasts, binary deltas, code signing, feed and archive signatures, files, installation, unarchiving, validation, updater behavior, and version comparison.
- **Documentation:** The README and security, installation, design-practices, and API documents explain setup and the reasons behind process, trust, lifecycle, and extensibility boundaries.
- **Traceability:** An update can be followed from check through appcast selection, download, signature and code validation, extraction, installer communication, atomic replacement, relaunch, and security tests.
- **Maintainability:** Protocol composition, explicit invalidation, restricted exports, feature flags, privilege-separated targets, stable APIs, and validation tests isolate a high-risk system.
- **Educational value:** It is a rare approachable codebase for studying desktop updates while treating feeds, archives, processes, and privileges as hostile boundaries.

**Inspection record:** commit `164f2fd30f7b6feb60596246322648a784dd308c`, reviewed 2026-08-28 by Codex. Files sampled: `README.markdown`, `Documentation/Security.md`, `Documentation/Design Practices.md`, `Sparkle/SPUUpdater.m`, `Sparkle/SUUpdateValidator.m`, `Tests/SUCodeSigningVerifierTest.m`, `LICENSE`. GitHub Linguist label: Objective-C. LOC exclusions: Tests/, UITests/, TestApplication/, TestAppHelper/, Vendor/, BinaryDelta/, generate_appcast/, generate_keys/, sign_update/.

**License:** [MIT AND BSD-2-Clause AND Zlib](https://github.com/sparkle-project/Sparkle/blob/164f2fd30f7b6feb60596246322648a784dd308c/LICENSE)

## SDC 5

### [gnachman/iTerm2](https://github.com/gnachman/iTerm2)

**S5 / D5 / C5 → SDC 5**

A full macOS terminal emulator with VT protocols, high-performance grids and rendering, sessions and process control, tmux and shell integration, automation APIs, restoration, search, transfers, profiles, and modern application features.

**Real-world evidence:** The repository builds and releases the iTerm2 desktop application used as a terminal replacement on macOS, plus scripting, helper, companion, and integration surfaces.

**Language evidence:** The still-dominant terminal core—byte streams, VT100 parsers and state machines, grids, screens, line buffers, sessions, process integration, selection, search, drawing, and much of the UI—is Objective-C and Objective-C++, with a substantial modern Swift layer.

**Why study it:** It carries terminal bytes through parsers, tokens, grids, scrollback, rendering, sessions, process and window lifecycles, persistence, tmux, shell protocols, accessibility, automation, and a large Objective-C and Swift boundary.

**What you can learn:**

- Terminal protocols and state machines, byte parsing, Unicode and bidirectional text, screen grids and scrollback, PTYs and processes, rendering and Metal, sessions and windows, selection and search, tmux and shell integration, persistence, automation, interoperability, and large-application evolution.

**Prerequisites:**

- Expert Objective-C plus working Swift, C, and C++, terminal and VT protocols, Unicode, processes and pseudo-terminals, AppKit, concurrency, graphics, persistence, networking, security, and large-codebase navigation.

**Start here:** [`sources/VT100/VT100Parser.m`](https://github.com/gnachman/iTerm2/blob/095009a6793f8a8c7ea7f4b8fd7fb1f3f1f834a4/sources/VT100/VT100Parser.m) — The parser turns incoming bytes into tokens and exposes partial input, control delegation, encoding, nested SSH and tmux streams, saved state, performance paths, and signaling.

**Why this level:**

- **S5:** 539,073 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production code and shipped templates under sources plus interface resources, excluding tests, generated code, third parties, companion products, tools, documentation, and project metadata.
- **D5:** Correctness spans mature specifications and OS subsystems, with visible corruption or data loss possible from subtle parsing, coordinate, lifecycle, or synchronization errors.
- **C5:** A long-lived desktop product coordinates many complex subsystems, languages, processes, protocols, state migrations, and delivery targets.
- **Placement:** S5/D5/C5 is an SDC 5 system; two dimensions at score 5 independently require level 5.

**Quality-gate evidence:**

- **Source quality:** Hot parsing and grid paths use explicit C structures and invariants, application layers name lifecycle state, project assertions preserve field diagnostics, modern modules add Swift types, and compatibility behavior is localized.
- **Architecture:** Application coordination leads through windows and tabs to PTYSession; byte-stream and VT100 parsers emit tokens into screen and grid state; line buffers retain history; AppKit and Metal render; feature modules attach through controllers, delegates, and services.
- **Naming and idiom:** PTYSession, VT100Parser, VT100Token, VT100Screen, VT100Grid, LineBuffer, PseudoTerminal, PTYTextView, shell integration, trigger, profile, and restoration form a durable vocabulary.
- **Tests:** More than 5,400 named Objective-C and Swift tests cover parsers, grids, screens, line buffers, selection, Unicode, bidirectional text, rendering, sessions, tmux, search, layout, restoration, browser and shell integrations, persistence, APIs, safety gates, regressions, and performance paths.
- **Documentation:** The README covers product architecture and builds, project guides record development invariants, the public website documents user and scripting behavior, and protocol modules carry explanatory comments and fixtures.
- **Traceability:** A PTY byte can be followed through VT100ByteStream and parser states into a token, terminal action, screen grid, line-buffer history, renderer, accessibility and selection behavior, and parser or screen tests.
- **Maintainability:** Feature-oriented folders, explicit bridging, generated-code boundaries, project assertion and logging APIs, extensive regression suites, and compatibility policies support continuous evolution.
- **Educational value:** It provides a complete advanced study of a protocol-driven desktop application whose core abstractions remain visible despite decades of growth.

**Inspection record:** commit `095009a6793f8a8c7ea7f4b8fd7fb1f3f1f834a4`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `AGENTS.md`, `CLAUDE.md`, `sources/VT100/VT100Parser.m`, `sources/VT100/VT100StateMachine.m`, `sources/PTYSession/PTYSession.m`, `iTerm2XCTests/VT100CSIParserTest.m`, `LICENSE`. GitHub Linguist label: Objective-C. LOC exclusions: iTerm2XCTests/, ModernTests/, tests/, sources/iTermTests/, sources/CoreDataGeneratedFiles/, sources/proto/, ThirdParty/, submodules/.

**License:** [GPL-2.0-only](https://github.com/gnachman/iTerm2/blob/095009a6793f8a8c7ea7f4b8fd7fb1f3f1f834a4/LICENSE)

### [gnustep/libs-base](https://github.com/gnustep/libs-base)

**S5 / D5 / C5 → SDC 5**

GNUstep's cross-platform implementation of the non-graphical OpenStep and Cocoa Foundation APIs, from root objects and collections through run loops, networking, serialization, localization, processes, and distributed objects.

**Real-world evidence:** GNUstep Base is a released runtime library used by GNUstep applications and command-line software to provide Foundation-style APIs across Unix-like systems and Windows.

**Language evidence:** The Foundation-compatible object model, strings and collections, coding, dates and locales, files, processes and threads, run loops, notifications, predicates, XML, networking, URL loading, distributed objects, and public headers are predominantly Objective-C with supporting C.

**Why study it:** It implements the substrate most Objective-C programs consume: NSObject behavior, memory management, collections, KVC and KVO, coding, run loops, timers, files, sockets, HTTP, locales, text, XML, processes, and portability.

**What you can learn:**

- Objective-C runtime foundations, ownership compatibility, class clusters, collections and strings, archives, KVC and KVO, run loops and timers, threads and locks, files and processes, URL loading over libcurl, distributed objects, localization, portability, and framework compatibility.

**Prerequisites:**

- Expert Objective-C and C, runtime messaging and forwarding, ownership, data structures, encodings, files and processes, threads, sockets and HTTP, event loops, serialization, build portability, and API compatibility.

**Start here:** [`Source/NSObject.m`](https://github.com/gnustep/libs-base/blob/795e88205b20cf372296af5b4d727aa68718fb6a/Source/NSObject.m) — The root object establishes allocation, identity, introspection, forwarding, copying, coding, description, synchronization, and runtime conventions used throughout the library.

**Why this level:**

- **S5:** 223,325 meaningful implementation LOC measured with tokei 14.0.0. Count covers the LGPL library implementation and public headers under Source and Headers, excluding tests, GPL tools, generated tables and templates, resources, configuration, and build metadata.
- **D5:** The library must reproduce a broad foundational API across runtimes and OSes while preserving behavioral, memory, concurrency, serialization, and compatibility contracts.
- **C5:** Many foundational subsystems and portability layers form a runtime-scale library beneath entire applications.
- **Placement:** S5/D5/C5 is an SDC 5 system; two dimensions at score 5 independently require level 5.

**Quality-gate evidence:**

- **Source quality:** Public contracts and private concrete classes are separated, ownership macros make runtime modes explicit, platform branches are localized, synchronization is named, error behavior is deliberate, and new subsystems document threading.
- **Architecture:** Public Foundation and GNUstepBase headers define compatibility; Source provides class clusters and private implementations; run-loop, networking, coding, distributed-object, text, and platform modules integrate through internal contracts.
- **Naming and idiom:** NSObject, NSString, GSString, NSRunLoop, GSTimedPerformer, NSURLSession, GSURLSessionWorkThread, NSKeyValueObserving, NSCoder, NSConnection, and GSPrivate expose public and internal roles.
- **Tests:** More than 7,000 assertion sites across hundreds of fixtures cover objects, collections, strings, numbers, dates, KVC, KVO, coding, secure archives, run loops, threads, files, processes, sockets, URL loading, cookies, TLS, XML, predicates, notifications, distributed objects, portability, and regressions.
- **Documentation:** The README explains scope, licensing, installation, and framework role; class documentation, manuals, standards notes, release history, coding standards, and compatibility analyses cover behavior.
- **Traceability:** A Foundation call can be followed from its public header into a class cluster or platform implementation, internal ownership path, external boundary where applicable, and a focused compatibility test.
- **Maintainability:** Stable headers, internal prefixes, generic templates, compile-time feature selection, platform directories, compatibility tests, multi-OS CI, and explicit library-versus-tool licensing support long-term evolution.
- **Educational value:** It is a capstone for understanding what Objective-C application code rests on: the object framework, event machinery, portability work, and contracts normally supplied by the platform.

**Inspection record:** commit `795e88205b20cf372296af5b4d727aa68718fb6a`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Headers/Foundation/NSObject.h`, `Source/NSObject.m`, `Source/NSString.m`, `Source/NSRunLoop.m`, `Source/NSURLSession.m`, `Tests/base/NSString/basic.m`, `COPYING.LIB`. GitHub Linguist label: Objective-C. LOC exclusions: Tests/, Tools/, Examples/, Documentation/, Source/Additions/unicode/, Source/tzdb.h, generated character-set data and template sources.

**License:** [LGPL-2.1-or-later](https://github.com/gnustep/libs-base/blob/795e88205b20cf372296af5b4d727aa68718fb6a/COPYING.LIB)

_Generated from `catalog/objective-c.json`; do not edit by hand._

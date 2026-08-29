# Learning-level calibration

The learner-centered rubric received a deliberately small smoke test on
2026-08-28 before the full catalog re-review. This test checked the anchors and
guardrails; it did not grandfather any repository into the rebuilt catalog.
Each path was read at the pinned commit, including its implementation and a
corresponding test or observable boundary. The repositories and commits still
resolved publicly and none was archived when checked.

Scores appear in this order: language technique, behavioral reasoning, design
span, and constraint burden. A dash means the path failed the coding-relevance
gate and was not scored.

| Repository and selected path | Pinned commit | Gate | Scores → level | Observed reason |
| --- | --- | --- | --- | --- |
| `webmozarts/assert`: `notNull()` from `src/Assert.php` into `tests/AssertTest.php` | `2ccb7c2e821038c03a3e6e1700c570c158c55f70` | Pass | `1 / 1 / 1 / 2` → Level 1 | One direct guard, one explicit exception contract, and focused tests require only ordinary PHP and routine API safeguards. |
| `sindresorhus/p-limit`: enqueue a promise-returning task in `index.js`, then verify concurrency and error behavior in `test.js` | `df476048d023ff868cd45b35ee47f5fb0ca2b25a` | Pass | `2 / 3 / 1 / 3` → Level 2 | Closures and promise composition are familiar professional idioms, while queue state, microtask order, async-context preservation, and error propagation require nontrivial behavioral reasoning. |
| `ardalis/GuardClauses`: `Guard.Against.Null()` from `src/GuardClauses/GuardAgainstNullExtensions.cs` into `test/GuardClauses.UnitTests/GuardAgainstNull.cs` | `7d55fa5397d73c0fe4e86a2dcab0230d1db57870` | Pass | `3 / 1 / 1 / 2` → Level 2 | Generic overloads, nullable-flow annotations, and caller-argument expressions materially shape a path whose runtime branch and test contract remain local and direct. |
| `DaveGamble/cJSON`: parse and own an object tree in `cJSON.c`, then follow object cases in `tests/parse_object.c` | `fb16e5cf358798aabb049655975cde8427101056` | Pass | `4 / 3 / 2 / 4` → Level 3 | Pointer arithmetic, allocation hooks, recursive ownership, offsets, format rules, ABI stability, locale handling, and failure cleanup recur in a compact two-module design. |
| `nikic/FastRoute`: parse placeholders in `src/RouteParser/Std.php`, carry compiled groups into `src/Dispatcher/GroupCountBased.php`, and verify dispatch results | `1c961398bef1ff6ecd8b273bef651d7afe90312b` | Pass | `2 / 3 / 3 / 3` → Level 3 | Conventional PHP interfaces contain a nontrivial parser-to-dispatch trace whose regex capture accounting, optional segments, ambiguity errors, and API compatibility span several clear boundaries. |
| `axios/axios`: follow `Axios._request()` through `lib/core/dispatchRequest.js` into an adapter result and the focused core tests | `fede1d1562e308077da7994305d63fb7722b66ac` | Pass | `2 / 3 / 3 / 4` → Level 3 | Class and promise composition are conventional, but interceptor order, synchronous versus asynchronous branches, cancellation, transforms, adapter boundaries, safe configuration handling, and cross-runtime HTTP compatibility interact. |
| `tidyverse/ggplot2`: build and inherit a `ggproto` object in `R/ggproto.R`, connect it to the production `Geom` extension point in `R/geom-.R`, and verify inheritance in `tests/testthat/test-ggproto.R` | `6870419aa6e106c3580c45c81d5b688cb31758bd` | Pass | `4 / 2 / 2 / 3` → Level 3 | R environments, delayed parent capture, dynamic method binding, and object-system interoperability are advanced language machinery, but this representative extension path needs only a short explanation of plot components rather than statistics or graphics theory. |
| `caddyserver/caddy`: load a replacement configuration in `caddy.go`, provision and start its apps, swap current state, clean up the old context, and exercise reload behavior | `502691f5182123ef30f463d7f132e7c2fe55e2bf` | Pass | `3 / 4 / 4 / 4` → Level 4 | Interface-driven module provisioning crosses raw configuration, contexts, app lifecycles, persistence, service notifications, metrics, locks, rollback, resource cleanup, and live-state replacement. |
| `prettier/prettier`: follow `coreFormat()` in `src/main/core.js` through parsing, AST-to-document conversion, printing, and cursor preservation into fixture tests | `0283c8848ecb541c7ea0601ff274799bce1b39e5` | Pass | `3 / 4 / 4 / 4` → Level 4 | Higher-order asynchronous composition coordinates parser plugins, AST normalization, document rendering, ranges, cursor diffing, comments, line endings, syntax compatibility, and deterministic output. |
| `opencv/opencv`: trace `cv::Mat` construction, allocation, header finalization, copy/release behavior, and matrix tests from `modules/core/src/matrix.cpp` | `397e70d0447d7d5a5ada6dfe3302ee78856eae6b` | Pass | `4 / 4 / 3 / 5` → Level 4 | The chosen core path is representative and needs only matrix shape and channel context, while advanced C++, reference-counted ownership, strides, allocator behavior, overflow, ABI, alignment, portability, and performance guarantees dominate the programming lesson. |
| `apple/swift-nio`: follow channel operations into an event loop, promise completion, and custom-channel tests across `Sources/NIOCore/Channel.swift`, `Sources/NIOCore/EventLoop.swift`, and `Tests/NIOCoreTests/CustomChannelTests.swift` | `a931f2c1de8dd49381ce3bf2e279d033f68d8865` | Pass | `5 / 5 / 4 / 5` → Level 5 | Advanced protocols, generics, sendability, and type erasure interact with thread confinement, scheduled work, I/O lifecycles, backpressure, resource ownership, portability, and performance constraints. |
| `Kong/kong`: build the request-phase plugin iterator in `kong/runloop/plugins_iterator.lua`, execute it through `kong/runloop/handler.lua`, and observe proxy integration behavior | `fa9c3b695af72668f135cb17bbb84a8b4dc511d2` | Pass | `4 / 5 / 5 / 5` → Level 5 | A short Nginx-phase map supplies the domain context; the hard work is transferable extension dispatch, workspace and configuration state, cache consistency, request isolation, recovery, security boundaries, latency, and multi-process control/data-plane coordination. |
| `spring-projects/spring-framework`: resolve a bean through `DefaultListableBeanFactory`, `AbstractBeanFactory.doGetBean()`, singleton and circular-reference handling, dependency resolution, and focused bean-factory tests | `1b56f58999046051d76a653922c3ab72b4db9cf7` | Pass | `5 / 5 / 5 / 5` → Level 5 | Generics, reflection, annotations, type descriptors, caches, factories, lazy proxies, extension hooks, lifecycles, concurrency, circular dependencies, and compatibility guarantees interact pervasively in a platform-scale programming path. |
| `nimble-dev/nimble`: build a model from `packages/nimble/R/BUGS_model.R` and the corresponding model tests | `0181166733112cdaaf4edf7d7b0817a8f03cbdac` | **Fail** | — | The path materially depends on Bayesian distributions, graphical-model semantics, stochastic versus deterministic nodes, and model-specific calculations. Advanced statistical theory explains the behavior and its correctness better than programming skill does. Reconsider only if a representative production path can be understood and judged without probabilistic-model expertise. |
| `testssl/testssl.sh`: drive protocol and cipher probes from `testssl.sh` into its baseline integration test | `853850e3f4433c7717035a84cfe873dd0e63dfd3` | **Fail** | — | TLS handshakes, cipher suites, certificate trust and revocation, vulnerability probes, OpenSSL behavior, and cryptographic interpretation dominate the program logic. Reconsider only if a representative path emerges whose correctness does not require specialist TLS or cryptographic knowledge. |

## Smoke-test decision

The anchors distinguish the intended programming growth without adjustment:

- Level 1 remains reachable for direct real-world code with one small contract.
- Asynchronous behavior raises behavioral reasoning without making a compact
  module look advanced in every dimension.
- A single expert burden cannot publish below Level 4, as the OpenCV matrix path
  demonstrates.
- Level 5 remains reachable only when several expert programming burdens
  interact, as in SwiftNIO, Kong, and Spring's bean-resolution path.
- A large specialist repository can pass through a genuine representative path
  when the specialist context is subordinate, as with `cv::Mat`; it cannot pass
  when external theory still explains the real difficulty, as with NIMBLE and
  testssl.sh.
- No dimension swallowed the other three, and no score was adjusted to preserve
  an old SDC placement.

**Decision:** retain the four anchors, formula, both guardrails, domain gate,
and lower-score borderline rule exactly as published. Calibration stops here.
A completed-corpus consistency pass will be appended after the rebuild.

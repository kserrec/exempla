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
| `webmozarts/assert`: `notNull()` from `src/Assert.php` into `tests/AssertTest.php` | `2ccb7c2e821038c03a3e6e1700c570c158c55f70` | Pass | `2 / 1 / 1 / 1` → Level 1 | One direct guard and focused tests keep behavior and constraints local; the PHPDoc/Psalm assertion convention is a common professional PHP idiom developed by the path. |
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
- A score of 4 denotes advanced machinery, reasoning, span, or constraints and
  therefore cannot publish below Level 3; the corpus-wide pass made this floor
  explicit when the full catalog exposed an edge case absent from the small
  smoke sample.
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

**Smoke-test decision:** retain the four anchors, arithmetic formula, score-5
floor, Level-5 guardrail, domain gate, and lower-score borderline rule. The
smoke test established qualitative separation; it was not statistical
validation and did not replace a completed-corpus consistency pass.

## Novice-accessibility calibration — 2026-08-30

The lower-rung refinement was calibrated before catalog migration against the
required current paths at their cataloged commits. Each review read the pinned
start file and the recorded implementation tests. “Rubric” below is the
unchanged four-score result; “floor” is the separate novice-accessibility
judgment; “final” is their maximum.

| Repository and path | Rubric → floor → final | Central and incidental concepts | Novice-perspective justification |
| --- | --- | --- | --- |
| `webmozarts/assert` — `not-null-guard` | `1 → 1 → 1` | Central: strict null validation, unchanged success value, and a direct failure. Incidental: a lazy message callback and PHPDoc/Psalm annotations. | `src/Assert.php` contains one strict branch and return, while `tests/AssertTest.php` proves that false and zero pass and null fails. A novice can predict every result from ordinary values, branching, and exceptions; the annotations can be explained locally without becoming the lesson. This remains the Level 1 anchor. |
| `sindresorhus/slash` | `1 → 1 → 1` | Central: changing ordinary Windows separators and preserving one special prefix. Incidental: the regular-expression literal meaning “every backslash.” | `index.js` has one prefix guard and one replacement, and `test.js` shows the ordinary and protected cases. The README explains the path goal before specialist terms appear; a one-sentence explanation of the literal is enough to predict the tests. This remains a Level 1 anchor. |
| `sindresorhus/escape-string-regexp` | `1 → 3 → 3` | Central: regular-expression metacharacters, replacement escaping, hexadecimal escaping, and PCRE/Unicode compatibility. Incidental: the input type check. | Both replacements in `index.js` exist specifically because of regular-expression grammar, and every case in `test.js` checks that grammar or its compatibility boundaries. A novice cannot explain why the output is correct without first learning metacharacters, replacement tokens, character classes, and Unicode-pattern restrictions. Its tiny function therefore rises to Level 3. |
| `mafintosh/pump` | `2 → 3 → 3` | Central: Node.js stream events, exactly-once completion, failure fan-out, resource teardown, and stream compatibility behavior. Incidental: small type predicates. | `index.js` coordinates `close`, end-of-stream callbacks, destruction, abort behavior, file streams, and the last writable; the Node and browser scripts verify competing lifecycle events. The learner needs a real stream lifecycle and event-order model before the control flow makes sense, so a short primer is not enough. |
| `sindresorhus/p-limit` | `2 → 3 → 3` | Central: promise adoption, queue admission, concurrency state, microtask timing, error propagation, and asynchronous-context preservation. Incidental: ordinary argument validation. | `index.js` deliberately queues promise resolution, catches only to avoid unhandled rejection, and uses a microtask when concurrency changes; `test.js` checks timing, errors, counters, clearing, and `AsyncLocalStorage`. Understanding why those tests pass requires event-loop and promise-scheduling background beyond a short Level 2 primer. |
| `alexreardon/tiny-invariant` | `2 → 3 → 3` | Central: TypeScript assertion signatures, truthiness, lazy diagnostics, build-time environment replacement, and production dead-code removal. Incidental: the direct throw itself. | `src/tiny-invariant.ts` couples runtime behavior to `asserts condition`, while the focused suites separately verify narrowing and generated Rollup output. Because advanced type narrowing and bundler optimization are both part of the promised behavior, the learner must acquire two post-baseline mental models before the whole path is intelligible. |
| `developit/mitt` | `2 → 3 → 3` | Central: event subscription and dispatch plus generic event maps, indexed payload types, overloads, and a conditional emit signature. Incidental: the `Map` and copied handler arrays. | `src/index.ts` makes advanced generic relationships part of every public method, and `test/test-types-compilation.ts` treats rejected type combinations as essential behavior. A novice may grasp the runtime emitter quickly but cannot understand the selected typed path without a separate TypeScript type-system lesson. |
| `dbader/schedule` | `2 → 3 → 3` | Central: recurring job state, due-job selection, missed-run policy, cancellation, time zones, daylight-saving gaps and folds, and rescheduling. Incidental: fluent method chaining by itself. | `schedule/__init__.py` computes and normalizes wall-clock times and stores a mutable job lifecycle; `test_schedule.py` devotes extensive cases to deadlines, time zones, and daylight-saving transitions. A learner needs a scheduling and civil-time model before predicting results, so this is not a gentle Level 2 introduction. |
| `pallets/itsdangerous` | `2 → 3 → 3` | Central: HMAC signatures, key derivation, salts, constant-time verification, key rotation, and trust boundaries. Incidental: byte conversion helpers and exception plumbing. | `signer.py` derives keys, delegates a signing algorithm, compares signatures safely, and tries rotated secrets; the signer tests make mutation, derivation modes, and rotation essential. The path cannot be understood correctly without meaningful cryptographic background and therefore receives floor 3. |
| `rust-cli/anstyle` | `2 → 3 → 3` | Central: ANSI escape-sequence encoding, effect bit sets, exact foreground/background/reset bytes, fixed buffers, and allocation-free rendering. Incidental: ordinary immutable builders. | The style, color, and effect modules map value types to terminal protocol bytes, while the tests verify exact encoded output. The selected path also includes feature-gated I/O and a bounded unsafe conversion. Those interacting post-baseline ideas exceed a short primer even though the API reads cleanly. |
| `typelevel/case-insensitive` | `2 → 3 → 3` | Central: lawful equality/hash/order consistency, Unicode case behavior, Cats type classes, interpolation, extraction, and wildcard matching. Incidental: simple string wrapper methods. | `CIString.scala` and `package.scala` combine a cached normalization contract with type-class instances and a custom extractor algorithm; the suites check algebraic laws and Unicode edge cases. Several specialized Scala and text-semantics concepts interact, so the path needs substantial preparation. |
| `microsoft/GSL` — `final-action-stores-a-cleanup-callable-invokes-it-once-at` | `2 → 2 → 2` | Central: a scope-exit cleanup action, generic callable storage, destruction, and transfer of responsibility during a move. Incidental: compiler diagnostic pragmas. | `include/gsl/util` expresses the full lifecycle in one small class and helper, while `tests/utils_tests.cpp` shows the callback before and after scope exit and after a move. RAII and move ownership are common professional C++ ideas that one short primer can make traceable, so Level 2 remains appropriate. |
| `tidwall/match` | `2 → 2 → 2` | Central: a fully stated wildcard grammar, rune-aware scanning, star backtracking, escaping, and a bounded search option. Incidental: the internal result enum. | `match.go` documents the complete `*`, `?`, literal, and escape grammar directly above the entry point; `match_test.go` supplies predictable examples before edge cases. The grammar is tiny and self-contained, and a short explanation of backtracking and runes is enough to begin, so the path remains Level 2. |
| `ralfstx/minimal-json` | `2 → 3 → 3` | Central: JSON grammar, recursive parser states, handler events, capture across buffers, nesting limits, and source-location errors. Incidental: ordinary Java constructors and collection values. | `JsonParser.java` dispatches every JSON production and maintains input, capture, nesting, line, and column state; `JsonParser_Test.java` checks valid grammar, malformed input, buffer boundaries, and deep nesting. Parser theory and JSON grammar are the lesson rather than a local implementation detail, requiring separate preparation. |
| `ruby/pathname` — `pathname-cleanpath-normalizes-a-path-lexically-while-preserving-roots-and` | `2 → 2 → 2` | Central: lexical component normalization, relative and absolute roots, aggressive versus conservative handling, and cross-platform separators. Incidental: local separator regular expressions. | `lib/pathname_builtin.rb` uses a visible component list and two named branches, and `test/pathname/test_pathname.rb` presents direct input/output matrices. One plain-language note explains why conservative mode preserves components around possible symbolic links; the learner can then predict representative cases without a separate course. |

### Frozen lower-rung decision

Calibration supported the published definitions without changing the four
dimensions or their formula. Level 1 means first real code whose central ideas
are already in the novice baseline; Level 2 permits a small, locally teachable
set of common professional ideas; floor 3 applies when a central concept needs
meaningful separate background or several post-baseline concepts interact.
Central concepts determine purpose and correctness; incidental concepts are
local tools explainable in one or two sentences. The five accessibility tests
and `max(rubric level, floor)` rule are frozen for the corpus audit. They will
not be tuned to recover a desired number of low-level entries.

## Superseded corpus-wide consistency pass — 2026-08-29

The post-rerun pass reviewed the completed 151-path corpus as paths rather than
whole repositories. It enforced globally unique `(repository, path_slug)`
identities, a two-path maximum per repository, no repeated repository within a
language/Level bucket, the arithmetic formula, all score floors, and explicit
separation between prior knowledge and concepts developed. Twelve neighboring-
level comparisons covered three paths at each Level boundary; additional checks
covered unusual language distributions and matching score profiles across
languages.

The four dimension anchors did not change. One new consistency guardrail did:
any score of 4 now forces at least Level 3, because an advanced burden in even
one dimension should not be presented as a beginner or ordinary intermediate
path. This moved `pointfreeco/swift-tagged` from Level 2 to Level 3. The source
audit separately found that `r-lib/pkgconfig` does not use the previously
claimed advanced R metaprogramming mechanisms; correcting its language score
from 4 to 3 left it at Level 2. The distinct Webmozart `notNull()` path was
accepted at Level 1 after the Level 1 follow-up, while Swift Log was retained as
a qualified Level 3 capacity alternate rather than moving any path to fit a
slot. Final integration also preserved APISIX's independently completed Level 5
configuration-propagation path and reran the corpus checks under schema version
3.

The [2026-08-29 learner-centered audit](../research/learner-centered-audit.json)
records that historical distribution, 14 invariant checks, comparisons,
corrections, and known gaps. It ended `pass-with-documented-gaps` with 151 of
200 possible paths. The later
[novice-accessibility audit](../research/novice-accessibility-audit.json)
supersedes its current counts and lower-rung placement conclusions while
preserving the earlier evidence as history. Future placement changes still
require new path-specific evidence rather than tuning the corpus toward a
desired distribution.

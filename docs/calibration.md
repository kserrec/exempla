# SDC calibration

Calibration was performed on 2026-08-28 before catalog scoring. It used 12
deliberately varied real repositories, each pinned to the commit shown below.
This was a rubric check, not automatic admission to the catalog; accepted
entries still need the full quality gate.

Implementation LOC was measured with `tokei 14.0.0`. Tests, fixtures,
benchmarks, examples, documentation, vendored/generated source, build output,
caches, and dotenv naming variants were excluded. Counts include the primary
implementation language and directly supporting first-party implementation
languages such as C headers in a C system.

| Repository | Pinned commit | LOC | S / D / C | Level | Calibration reason |
| --- | --- | ---: | --- | ---: | --- |
| `sindresorhus/p-limit` | `df476048d023ff868cd45b35ee47f5fb0ca2b25a` | 745 | S1 / D2 / C1 | 1 | Tiny single-purpose module; promise scheduling is nuanced but the whole path fits in one file. |
| `dbader/schedule` | `82a43db1b938d8fdf60103bd41f329e06c8d3651` | 1,978 | S1 / D2 / C1 | 1 | One-module scheduler with explicit jobs and timing behavior; date/time edge cases add modest difficulty. |
| `nikic/FastRoute` | `1c961398bef1ff6ecd8b273bef651d7afe90312b` | 1,243 | S1 / D3 / C2 | 2 | Very small, but route parsing, regular-expression construction, and dispatch grouping are substantive algorithms. |
| `ardalis/GuardClauses` | `7d55fa5397d73c0fe4e86a2dcab0230d1db57870` | 1,374 | S1 / D1 / C1 | 1 | Direct extension methods, explicit contracts, and one-to-one unit tests make the behavior locally traceable. |
| `DaveGamble/cJSON` | `fb16e5cf358798aabb049655975cde8427101056` | 4,294 | S2 / D3 / C1 | 2 | Compact architecture, but recursive parsing, manual allocation, buffer bounds, and C error paths raise code difficulty. |
| `sharkdp/hyperfine` | `f12f3d9f86f3643b3b7deace5e160b1f0f44d2b7` | 3,034 | S2 / D3 / C2 | 2 | Process execution, timing calibration, statistics, and cross-platform behavior fit a small, clearly separated CLI design. |
| `tidyverse/ggplot2` | `6870419aa6e106c3580c45c81d5b688cb31758bd` | 25,338 | S3 / D4 / C3 | 3 | The grammar-of-graphics domain, delayed evaluation, S3/S7/ggproto dispatch, and layered plot pipeline are conceptually demanding. |
| `caddyserver/caddy` | `502691f5182123ef30f463d7f132e7c2fe55e2bf` | 74,762 | S4 / D3 / C4 | 4 | Idiomatic Go contains difficulty, while config adaptation, modules, admin APIs, lifecycle, TLS, and HTTP subsystems create broad system complexity. |
| `apple/swift-nio` | `a931f2c1de8dd49381ce3bf2e279d033f68d8865` | 161,021 | S4 / D5 / C4 | 4 | Event loops, futures, thread confinement, pipeline propagation, buffers, sockets, and platform shims demand expert concurrency knowledge. |
| `Kong/kong` | `fa9c3b695af72668f135cb17bbb84a8b4dc511d2` | 77,326 | S4 / D5 / C5 | 5 | OpenResty execution phases, plugins, routing, balancing, persistence, caching, migrations, and control/data-plane clustering interact across a large runtime. |
| `spring-projects/spring-framework` | `1b56f58999046051d76a653922c3ab72b4db9cf7` | 391,522 | S5 / D4 / C5 | 5 | Bean lifecycles, reflection, proxies, application contexts, eventing, web stacks, transactions, and many modules form a platform-scale architecture. |
| `torvalds/linux` | `548e7bcd0c5460ddcbca9600cea603ebeebf4da7` | 29,938,973 | S5 / D5 / C5 | 5 | Architecture ports, scheduling, memory, filesystems, drivers, synchronization, security hooks, and hardware boundaries require expert systems knowledge. |

## Source paths inspected

The review sampled entry points, core behavior, boundaries, and corresponding
tests rather than relying on LOC alone. Representative paths included:

- `p-limit`: `index.js`, `test.js`, `index.d.ts`.
- `schedule`: `schedule/__init__.py`, `test_schedule.py`, `README.rst`.
- `FastRoute`: `src/RouteParser/Std.php`,
  `src/DataGenerator/RegexBasedAbstract.php`, `src/Dispatcher.php`.
- `GuardClauses`: `src/GuardClauses/Guard.cs`,
  `src/GuardClauses/GuardAgainstNullExtensions.cs`,
  `test/GuardClauses.UnitTests/GuardAgainstNull.cs`.
- `cJSON`: `cJSON.c`, `cJSON.h`, `tests/parse_value.c`.
- `hyperfine`: `src/main.rs`, `src/command.rs`,
  `src/benchmark/executor.rs`.
- `ggplot2`: `R/layer.R`, `R/geom-.R`,
  `tests/testthat/test-aes-delayed-eval.R`.
- `Caddy`: `caddy.go`, `admin.go`, `modules/caddyhttp/app.go`,
  `caddyconfig/caddyfile/dispenser_test.go`.
- `SwiftNIO`: `Sources/NIOCore/EventLoop.swift`,
  `Sources/NIOCore/ChannelPipeline.swift`,
  `Tests/NIOCoreTests/CustomChannelTests.swift`.
- `Kong`: `kong/init.lua`, `kong/runloop/handler.lua`,
  `kong/clustering/control_plane.lua`, `spec/01-unit/16-runloop_handler_spec.lua`.
- `Spring Framework`: `spring-beans/src/main/java/org/springframework/beans/factory/support/DefaultListableBeanFactory.java`,
  `spring-context/src/main/java/org/springframework/context/support/AbstractApplicationContext.java`,
  and the corresponding context tests.
- `Linux`: `fs/open.c`, `kernel/sched/core.c`, `include/linux/sched.h`,
  `tools/testing/kunit/kunit.py`.

## Findings and decision

The ordering broadly makes sense and exposes no obvious absurdity:

- Size does not dominate: FastRoute is smaller than several SDC-1 projects but
  lands higher because parsing raises D; ggplot2 remains SDC 3 despite D4
  because its codebase and system topology are bounded.
- Straightforward volume does not automatically mean expert difficulty: Caddy's
  S4 contributes to SDC 4, while its idiomatic implementation stays at D3.
- Extreme difficulty is not hidden by size: the guardrail keeps SwiftNIO at SDC
  4 despite an arithmetic result that would otherwise risk understating D5.
- Platform-scale repositories with multiple extreme dimensions land at SDC 5.
- The 2,000 / 10,000 / 50,000 / 200,000 LOC bands separate this varied sample
  usefully; the 1,978-line scheduler near the first boundary is not an obvious
  misclassification.

**Decision:** retain the original thresholds, anchors, formula, and guardrails
without adjustment. Calibration stops here. The completed corpus will receive
one later consistency pass, as specified in the plan.

## Completed-corpus consistency pass

The promised later pass was completed on 2026-08-28 after all 200 entries were
accepted. It compared every S/D/C profile, all neighboring public levels, size
bands, formula results, and the exceptional placements produced by the two
guardrails.

| Level | Entries | Minimum LOC | Median LOC | Maximum LOC | Mean S | Mean D | Mean C |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 40 | 48 | 408 | 3,671 | 1.050 | 1.850 | 1.000 |
| 2 | 40 | 265 | 1,716.5 | 10,834 | 1.500 | 2.700 | 2.025 |
| 3 | 40 | 2,616 | 8,405 | 43,804 | 2.400 | 3.350 | 2.975 |
| 4 | 40 | 13,771 | 46,931.5 | 516,827 | 3.575 | 4.125 | 4.000 |
| 5 | 40 | 37,979 | 450,844.5 | 6,754,140 | 4.750 | 4.700 | 5.000 |

The progression is monotonic in median LOC and in the mean of every dimension.
Boundary overlap is expected because size never assigns the public level by
itself. Compact algorithmic projects such as FastRoute can sit above larger
direct libraries; very large but internally regular libraries such as
Protocol Buffers can remain at SDC 4; and LuaLS and Pode reach SDC 5 through
the published two-extreme-dimensions guardrail despite S3 size.

The pass found no unexplained level inversion and changed no S/D/C judgment or
public placement. It made one measurement normalization: Kong now records
77,326 first-party Lua lines after consistently removing bundled Resty modules,
external protocol definitions, and attributed copied helpers. Its size band
and SDC 5 placement are unchanged. No decimal public ranking was introduced.

**Final decision:** retain the thresholds, anchors, formula, guardrails, and all
200 placements.

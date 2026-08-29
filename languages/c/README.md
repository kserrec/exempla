# C

10 qualified repositories. Scores assume the learner described in [the SDC rubric](../../docs/sdc.md).

[← All languages](../README.md)

## SDC 1

### [likle/cwalk](https://github.com/likle/cwalk)

**S1 / D2 / C1 → SDC 1**

A lightweight cross-platform library for lexical filesystem path manipulation in C and C++ programs.

**Real-world evidence:** The repository ships an embeddable C library tested on Linux, FreeBSD, macOS, and Windows and packaged by multiple C ecosystems.

**Language evidence:** Path parsing, joining, normalization, relative-path calculation, segment iteration, and Unix and Windows rules are implemented in C under src/ with a C public header.

**Why study it:** One source file turns raw strings into a coherent path model while exposing buffer sizing, in-place output, iteration, roots, and platform conventions.

**What you can learn:**

- Pointer-based string scanning, bounded output, path segments, normalization, relative paths, Unix and Windows roots, in-place transformation, and portable C APIs.

**Prerequisites:**

- C pointers and arrays, null-terminated strings, structs, enums, size_t, buffers, and basic filesystem path conventions.

**Start here:** [`src/cwalk.c`](https://github.com/likle/cwalk/blob/e98d23f68807208952c179b49e4fd1813f31298d/src/cwalk.c) — The single implementation file begins with bounded output and segment traversal, then builds the public path operations from those primitives.

**Why this level:**

- **S1:** 904 meaningful implementation LOC measured with tokei 14.0.0. Count covers the complete production source and public header, excluding tests, generated documentation, examples, and build metadata.
- **D2:** Pointer and buffer care matter, but the algorithms are iterative, documented, and built from a small set of helpers.
- **C1:** A single component provides pure path transformations without filesystem I/O, services, or extension machinery.
- **Placement:** S1/D2/C1 averages to 1.33, placing libcwalk at SDC 1.

**Quality-gate evidence:**

- **Source quality:** Buffer writes return theoretical lengths, termination is centralized, and segment state makes pointer traversal explicit.
- **Architecture:** Private output, root, and segment primitives support a flat public API for joining, normalizing, resolving, and inspecting paths.
- **Naming and idiom:** cwk_path_get_first_segment, normalize, join, relative, root, basename, dirname, and extension match the domain directly.
- **Tests:** Focused test files cover every operation, small output buffers, overlapping inputs, empty paths, excessive parent traversal, Unix behavior, and Windows drive and UNC paths.
- **Documentation:** The README links complete building, embedding, testing, and API reference documentation and states the platform matrix.
- **Traceability:** A normalization case can be followed from segment iteration through dot and parent filtering, bounded output, termination, and a focused test.
- **Maintainability:** One implementation unit, a stable header, explicit platform style, and operation-specific tests make changes easy to isolate.
- **Educational value:** It demonstrates safe string and buffer design in a complete useful library small enough to read in one sitting.

**Inspection record:** commit `e98d23f68807208952c179b49e4fd1813f31298d`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `CMakeLists.txt`, `include/cwalk.h`, `src/cwalk.c`, `test/normalize_test.c`, `LICENSE.md`. GitHub Linguist label: C. LOC exclusions: test/, docs/.

**License:** [MIT](https://github.com/likle/cwalk/blob/e98d23f68807208952c179b49e4fd1813f31298d/LICENSE.md)

### [zserge/jsmn](https://github.com/zserge/jsmn)

**S1 / D2 / C1 → SDC 1**

A minimal allocation-free JSON tokenizer designed for embedded and resource-constrained C programs.

**Real-world evidence:** The repository distributes a portable single-header parser intended to be embedded directly into C applications.

**Language evidence:** The incremental JSON tokenizer, token model, validation, error reporting, and optional parent-link behavior are implemented entirely in the C header jsmn.h.

**Why study it:** A two-function API exposes a full single-pass state machine, zero-copy token representation, caller-owned memory, incremental parsing, and strictness tradeoffs.

**What you can learn:**

- Finite-state parsing, zero-copy token spans, caller-owned allocation, incremental input, nested structures, compile-time options, error codes, and header-only C distribution.

**Prerequisites:**

- C structs and enums, pointers and arrays, loops and switches, string indexing, preprocessor conditionals, and JSON syntax.

**Start here:** [`jsmn.h`](https://github.com/zserge/jsmn/blob/25647e692c7906b96ffd2b05ca54c097948e879c/jsmn.h) — The whole parser is here; read token allocation and primitive and string parsing before following the main jsmn_parse loop.

**Why this level:**

- **S1:** 353 meaningful implementation LOC measured with tokei 14.0.0. Count covers the complete production header, excluding tests, examples, documentation, and build metadata.
- **D2:** Parsing introduces state and edge cases, but the token model and main loop remain compact and plainly structured.
- **C1:** One component tokenizes JSON without allocation, I/O, object construction, or external dependencies.
- **Placement:** S1/D2/C1 averages to 1.33, making jsmn an SDC 1 project.

**Quality-gate evidence:**

- **Source quality:** Token allocation, span filling, rollback on incomplete input, strict-mode behavior, and parent tracking are explicit in short functions.
- **Architecture:** A parser-state struct advances through caller input and fills a caller-owned flat token array that refers back to source spans.
- **Naming and idiom:** jsmn_parser, jsmntok_t, toksuper, parse_primitive, parse_string, NOMEM, INVAL, and PART reveal the state machine.
- **Tests:** The suite covers primitives, strings and escapes, arrays, objects, nested and partial input, token counting, insufficient storage, invalid JSON, and optional parent links.
- **Documentation:** The README explains philosophy, token representation, embedding, compile-time modes, incremental use, examples, and every error result.
- **Traceability:** A JSON string token can be followed through escape validation, span assignment, parent sizing, return count, and exact token-boundary assertions.
- **Maintainability:** No dependencies or heap ownership, one source artifact, and exhaustive parser cases minimize integration and regression risk.
- **Educational value:** It is an unusually clear introduction to production parsing because representation and control flow both fit on one page at a time.

**Inspection record:** commit `25647e692c7906b96ffd2b05ca54c097948e879c`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Makefile`, `jsmn.h`, `test/tests.c`, `LICENSE`. GitHub Linguist label: C. LOC exclusions: test/, example/.

**License:** [MIT](https://github.com/zserge/jsmn/blob/25647e692c7906b96ffd2b05ca54c097948e879c/LICENSE)

## SDC 2

### [DaveGamble/cJSON](https://github.com/DaveGamble/cJSON)

**S2 / D2 / C2 → SDC 2**

An ultralightweight JSON parser, tree model, printer, and manipulation library written in portable ANSI C.

**Real-world evidence:** The repository ships installable and embeddable C libraries used to parse and generate JSON in native applications.

**Language evidence:** JSON parsing, tree ownership, printing, mutation, comparison, JSON Pointer, Patch, Merge Patch, and sorting are C in cJSON.c and cJSON_Utils.c.

**Why study it:** It grows a familiar recursive data format into explicit allocation hooks, owned trees, parsing and printing, mutation, reference nodes, and standards-based utilities.

**What you can learn:**

- Recursive-descent parsing, linked tree representation, ownership and reference nodes, allocation hooks, dynamic printing, numeric conversion, JSON Pointer and Patch, and ABI-conscious C APIs.

**Prerequisites:**

- C pointers and structs, dynamic memory, linked lists, recursion, string and numeric conversion, error handling, and JSON syntax.

**Start here:** [`cJSON.c`](https://github.com/DaveGamble/cJSON/blob/fb16e5cf358798aabb049655975cde8427101056/cJSON.c) — Begin with the cJSON node and allocation hooks, then follow parse_value and print_value into their object, array, string, and number helpers.

**Why this level:**

- **S2:** 3,878 meaningful implementation LOC measured with tokei 14.0.0. Count covers the two production source and public header pairs, excluding tests, the bundled Unity framework, fuzzing, examples, documentation, and build metadata.
- **D2:** Memory ownership and recursion require care, but data structures and algorithms are conventional and extensively named.
- **C2:** Two cohesive libraries implement one data format and its transformation utilities without runtime services.
- **Placement:** S2/D2/C2 makes cJSON a balanced SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** Allocation hooks, parse bounds, ownership flags, error positions, and print-buffer growth are explicit and guarded throughout the core.
- **Architecture:** A doubly linked tagged tree connects recursive parsing and printing, while a separate utilities module adds pointer, patch, merge, and sorting operations.
- **Naming and idiom:** parse_value, print_value, child, next, prev, valueint, valuestring, hooks, detach, and replace expose representation and ownership.
- **Tests:** Unit suites cover every JSON type, malformed inputs, allocation failures, printing, mutation, comparison, pointer and patch standards, locales, depth, and README examples.
- **Documentation:** The README documents building, data representation, ownership rules, parsing, printing, manipulation, caveats, and utilities with examples.
- **Traceability:** An object property can be followed from parse_string through node allocation and child linking, lookup or mutation, printing, deletion, and focused tests.
- **Maintainability:** A stable small API, explicit compatibility policy, sanitizer and fuzz coverage, and boundary-focused tests constrain manual-memory risks.
- **Educational value:** It is a practical next step after a tokenizer because it shows the costs and benefits of building an owned object model.

**Inspection record:** commit `fb16e5cf358798aabb049655975cde8427101056`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `CMakeLists.txt`, `cJSON.c`, `cJSON_Utils.c`, `tests/parse_object.c`, `LICENSE`. GitHub Linguist label: C. LOC exclusions: tests/, fuzzing/.

**License:** [MIT](https://github.com/DaveGamble/cJSON/blob/fb16e5cf358798aabb049655975cde8427101056/LICENSE)

### [libcheck/check](https://github.com/libcheck/check)

**S2 / D3 / C2 → SDC 2**

A unit testing framework for C with fork-based isolation, fixtures, timeouts, diagnostics, and multiple output formats.

**Real-world evidence:** The project publishes the Check library and checkmk tool used to build and run isolated native test suites.

**Language evidence:** Test registration, fixtures, isolated execution, timeout and signal handling, result transport, logging, and the checkmk generator are implemented principally in C.

**Why study it:** Its assertion macros lead into suites, cases, fixtures, process isolation, signals, timeouts, result messaging, logging, and portable fallbacks.

**What you can learn:**

- Test registration, macro APIs, fixtures, fork isolation, signals and timeouts, interprocess result transport, logging formats, portable compatibility, and self-testing frameworks.

**Prerequisites:**

- C macros and function pointers, processes, signals, pipes, dynamic memory, linked collections, build systems, and unit-testing concepts.

**Start here:** [`src/check.c`](https://github.com/libcheck/check/blob/35d9cc011faa0545bf56d5062ae90bbc2688eba7/src/check.c) — The core constructors and test-case model connect the public macros to suites, cases, fixtures, result objects, and runner handoff.

**Why this level:**

- **S2:** 7,688 meaningful implementation LOC measured with tokei 14.0.0. Count covers the production framework, compatibility library, and checkmk generator, excluding self-tests, documentation, examples, generated files, and build metadata.
- **D3:** Process behavior and result transport add systems depth, while the framework keeps responsibilities in recognizable modules.
- **C2:** Several cooperating modules serve one local test-runner concern and a bounded portability surface.
- **Placement:** S2/D3/C2 averages to 2.33, placing Check at SDC 2.

**Quality-gate evidence:**

- **Source quality:** Test lifecycle, fork modes, result types, timeout policy, fixture ordering, and error paths use explicit enums, structs, and helpers.
- **Architecture:** Suite and case registration feed a runner that selects execution mode, captures results, aggregates statistics, and delegates to log backends.
- **Naming and idiom:** Suite, TCase, SRunner, SFun, fixture, CK_FORK, TestResult, check_msg, and check_log expose framework roles.
- **Tests:** The framework tests itself across assertions, fixtures, signals, timeouts, fork and no-fork modes, messaging, logs, XML, TAP, memory failures, and checkmk.
- **Documentation:** The README and maintained manual cover installation, test construction, fixtures, execution modes, output, build integration, and advanced behavior.
- **Traceability:** A START_TEST macro can be followed through registration, runner dispatch, child execution or direct call, result serialization, aggregation, log output, and self-tests.
- **Maintainability:** Execution, messaging, collections, logging, compatibility, and generation are separate modules protected by a self-hosted regression suite.
- **Educational value:** It reveals the operating-system machinery hidden behind a friendly unit-test macro API.

**Inspection record:** commit `35d9cc011faa0545bf56d5062ae90bbc2688eba7`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `CMakeLists.txt`, `src/check.c`, `src/check_run.c`, `tests/check_check_main.c`, `COPYING.LESSER`. GitHub Linguist label: C. LOC exclusions: tests/, checkmk/test/, doc/.

**License:** [LGPL-2.1-or-later](https://github.com/libcheck/check/blob/35d9cc011faa0545bf56d5062ae90bbc2688eba7/COPYING.LESSER)

## SDC 3

### [akheron/jansson](https://github.com/akheron/jansson)

**S3 / D3 / C2 → SDC 3**

A C library for encoding, decoding, and manipulating JSON with a rich value API and strict error handling.

**Real-world evidence:** The repository releases a stable native library and command-line utility used to handle JSON in production C applications.

**Language evidence:** JSON values, reference counting, hash tables, UTF-8 validation, parsers, dumpers, packing, unpacking, iteration, and memory hooks are C under src/.

**Why study it:** It expands JSON into a mature library design with reference counting, hash tables, stream callbacks, format-driven construction, canonical output, and compatibility guarantees.

**What you can learn:**

- Reference-counted values, hash tables, recursive parsing and dumping, UTF-8 validation, streaming callbacks, variadic pack and unpack formats, custom allocators, and API stability.

**Prerequisites:**

- Comfortable C, ownership and reference counting, hash tables, callbacks, variadic functions, parsing, encodings, and library API design.

**Start here:** [`src/value.c`](https://github.com/akheron/jansson/blob/851a2145e3256f2e67e5dfe24b0e456bf198b741/src/value.c) — Value construction, reference ownership, arrays, objects, hash iteration, mutation, and equality establish the model used by loading and dumping.

**Why this level:**

- **S3:** 10,281 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production C under src, excluding tests, fuzzers, examples, documentation, generated configuration, and build metadata.
- **D3:** Several nontrivial concerns recur across the library, but implementations use conventional data structures and clear invariants.
- **C2:** Multiple cohesive modules implement one serialization domain without services or process orchestration.
- **Placement:** S3/D3/C2 averages to 2.67, which rounds to SDC 3.

**Quality-gate evidence:**

- **Source quality:** Ownership transfers, reference counts, parse positions, depth limits, UTF-8 checks, allocation failures, and hash invariants are explicit and consistently guarded.
- **Architecture:** A reference-counted value model and hash table support loader, dumper, pack and unpack interpreter, streaming callbacks, and allocator hooks.
- **Naming and idiom:** json_t, incref, decref, json_load, json_dump, pack, unpack, error_t, hashtable, and iterator form a stable domain API.
- **Tests:** API, encoding, decoding, number, UTF-8, allocator, depth, pack and unpack, callback, regression, fuzz, and command-line suites cover success and failure paths.
- **Documentation:** A maintained reference and tutorial document values, ownership, decoding, encoding, streaming, formats, customization, portability, and changes.
- **Traceability:** An object from input can be followed through lexical parsing, value allocation and hash insertion, reference ownership, mutation, dumping, cleanup, and API tests.
- **Maintainability:** Small modules, stable public headers, centralized allocators and errors, versioned releases, and exhaustive failure tests protect a low-level API.
- **Educational value:** It teaches how a compact C library can add mature ownership and extensibility without becoming a framework.

**Inspection record:** commit `851a2145e3256f2e67e5dfe24b0e456bf198b741`, reviewed 2026-08-28 by Codex. Files sampled: `README.rst`, `CMakeLists.txt`, `src/value.c`, `src/load.c`, `test/suites/api/test_load.c`, `LICENSE`. GitHub Linguist label: C. LOC exclusions: test/, examples/, doc/.

**License:** [MIT](https://github.com/akheron/jansson/blob/851a2145e3256f2e67e5dfe24b0e456bf198b741/LICENSE)

### [libevent/libevent](https://github.com/libevent/libevent)

**S3 / D4 / C3 → SDC 3**

A portable asynchronous event-notification library with event loops, buffered streams, networking protocols, and threading support.

**Real-world evidence:** The project releases a native library used by network servers and clients to multiplex I/O across operating-system backends.

**Language evidence:** Event loops, platform polling backends, buffered I/O, listeners, DNS, HTTP, RPC, TLS adapters, threading, timers, and utilities are C across the repository root and include/.

**Why study it:** It connects the event abstraction to epoll, kqueue, poll, select, IOCP, timers, signals, deferred callbacks, watermarks, locks, DNS, HTTP, and TLS.

**What you can learn:**

- Reactor event loops, readiness backends, timers and signals, buffered asynchronous I/O, deferred callbacks, watermarks, thread safety, DNS and HTTP, TLS adapters, and portability.

**Prerequisites:**

- Advanced C, sockets and nonblocking I/O, operating-system polling APIs, callbacks, queues and heaps, threads and locks, networking protocols, and build portability.

**Start here:** [`event.c`](https://github.com/libevent/libevent/blob/335349b9b60c860289c6c47eadadadf18dc58211/event.c) — The event base, backend selection, event registration, timeout queues, activation, callback dispatch, and loop lifecycle establish the core reactor.

**Why this level:**

- **S3:** 43,804 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production C and headers, excluding tests, samples, documentation, generated build support, historical code, and packaging metadata.
- **D4:** Correctness depends on subtle readiness, timing, ownership, and concurrency behavior across multiple operating systems.
- **C3:** Several substantial subsystems and adapters cooperate inside one native networking library.
- **Placement:** S3/D4/C3 averages to 3.33, placing Libevent at SDC 3.

**Quality-gate evidence:**

- **Source quality:** Backend contracts, event states, reference counts, lock boundaries, callback deferral, watermarks, and timeout invariants are explicit in private structures and helpers.
- **Architecture:** An event base selects a readiness backend; events and timeout queues drive callbacks; bufferevents, listeners, DNS, HTTP, RPC, and TLS build on that core.
- **Naming and idiom:** event_base, event_add, active queue, bufferevent, evbuffer, evconnlistener, evdns, evhttp, defer, watermark, and backend expose runtime roles.
- **Tests:** Large regression suites cover backends, timers, signals, threads, buffers, listeners, DNS, HTTP, RPC, TLS, WebSockets, memory hooks, failures, and platform behavior.
- **Documentation:** The README, generated API reference, book-style programming guide, examples, and release notes explain both core and protocol layers.
- **Traceability:** A socket read event can be followed from backend readiness through active queues and priority dispatch into a bufferevent callback, watermark handling, and regression tests.
- **Maintainability:** Backend operation tables, internal headers, reference counting, feature flags, and broad cross-platform CI isolate variation behind stable APIs.
- **Educational value:** It is a bounded but deep systems project for learning the machinery beneath asynchronous networking frameworks.

**Inspection record:** commit `335349b9b60c860289c6c47eadadadf18dc58211`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `CMakeLists.txt`, `event.c`, `bufferevent.c`, `test/regress.c`, `LICENSE`. GitHub Linguist label: C. LOC exclusions: test/, sample/, docs/, cmake/, m4/, WIN32-Code/.

**License:** [BSD-3-Clause](https://github.com/libevent/libevent/blob/335349b9b60c860289c6c47eadadadf18dc58211/LICENSE)

## SDC 4

### [curl/curl](https://github.com/curl/curl)

**S4 / D4 / C4 → SDC 4**

A command-line data transfer tool and reusable library supporting URL-based communication across many protocols and platforms.

**Real-world evidence:** The repository builds curl and libcurl, widely deployed for command-line transfers and embedded network clients across operating systems and devices.

**Language evidence:** Protocol engines, connection reuse, DNS, proxies, TLS adapters, HTTP versions, the multi state machine, URL API, and command-line tool are C under lib/ and src/.

**Why study it:** One easy command rests on URL parsing, connection caching, protocol state machines, proxies, authentication, DNS, TLS, multiplexing, retries, streaming callbacks, and extreme portability.

**What you can learn:**

- Protocol state machines, connection pooling, event-driven multi transfers, URL parsing, DNS, proxies and authentication, TLS backend abstraction, HTTP/2 and HTTP/3, streaming, command-line design, and portability.

**Prerequisites:**

- Advanced C, sockets and nonblocking I/O, HTTP and other Internet protocols, TLS, callbacks, state machines, concurrency, build portability, and large-library navigation.

**Start here:** [`lib/multi.c`](https://github.com/curl/curl/blob/c2a04c080d79e1eb5d99bc0a73fd71710aa6d345/lib/multi.c) — The multi state machine shows how transfers advance through setup, resolving, connecting, protocol work, completion, retries, multiplexing, and socket and timer callbacks.

**Why this level:**

- **S4:** 152,242 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party libcurl, curl tool, and public headers, excluding tests, documentation, packaging, platform project files, generated content, and build metadata.
- **D4:** Network correctness, compatibility, and lifetime rules recur across protocol, connection, callback, and backend boundaries.
- **C4:** Many modular backends cooperate through a mature transfer engine, while remaining one client library and tool suite.
- **Placement:** S4/D4/C4 makes curl an SDC 4 project.

**Quality-gate evidence:**

- **Source quality:** Transfer states, ownership, callback contracts, connection reuse rules, protocol capabilities, error codes, and feature guards are explicit throughout the core.
- **Architecture:** Easy and URL APIs feed the multi engine; connection and protocol handlers compose resolver, proxy, authentication, TLS, HTTP-version, and platform backends; the CLI layers policy above libcurl.
- **Naming and idiom:** CURL, Curl_easy, Curl_multi, connectdata, Curl_handler, multi_runsingle, conncache, resolver, transfer, and CURLE codes form a consistent model.
- **Tests:** A very large harness covers protocols, APIs, servers, proxies, TLS backends, DNS, authentication, malformed input, unit behavior, fuzzing, memory checks, platforms, and regressions.
- **Documentation:** Man pages, API references, protocol and internals documentation, examples, security advisories, release notes, and contributor guides are maintained with the code.
- **Traceability:** A URL transfer can be followed from option parsing or easy setup into the multi state machine, DNS and connection reuse, protocol handler, callbacks, completion, cleanup, and protocol tests.
- **Maintainability:** Handler tables, backend interfaces, feature flags, compatibility policy, generated option metadata, and exhaustive CI contain an unusually broad portability surface.
- **Educational value:** It is an advanced masterclass in evolving a stable C API across decades of protocols and platforms.

**Inspection record:** commit `c2a04c080d79e1eb5d99bc0a73fd71710aa6d345`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `CMakeLists.txt`, `lib/url.c`, `lib/multi.c`, `tests/unit/unit1300.c`, `COPYING`. GitHub Linguist label: C. LOC exclusions: tests/, docs/, packages/, projects/.

**License:** [curl](https://github.com/curl/curl/blob/c2a04c080d79e1eb5d99bc0a73fd71710aa6d345/COPYING)

### [redis/redis](https://github.com/redis/redis)

**S4 / D4 / C4 → SDC 4**

An in-memory data structure server providing key-value storage, rich data types, persistence, replication, clustering, scripting, and messaging.

**Real-world evidence:** The repository builds the Redis server and command-line tools deployed as caches, databases, queues, streams, and real-time data services.

**Language evidence:** The server, event processing, command execution, data structures, persistence, replication, clustering, transactions, scripting, memory management, and CLI are C under src/.

**Why study it:** The single-threaded command path is approachable, yet it opens into specialized data structures, an event loop, expirations, persistence, replication, cluster consensus, scripts, modules, and operations.

**What you can learn:**

- Event-driven servers, command dispatch, compact data structures, expiration and eviction, snapshots and append-only persistence, replication, clustering and failover, transactions, scripting, modules, and observability.

**Prerequisites:**

- Advanced C, sockets and event loops, memory ownership, data structures and algorithms, files and process management, distributed systems, replication, persistence, concurrency, and operational debugging.

**Start here:** [`src/server.c`](https://github.com/redis/redis/blob/e1d7d50f9c244ce52f724b279fcb19773fffa98c/src/server.c) — Server initialization and the command-processing path connect configuration, clients, lookup, permissions, execution, propagation, persistence, replication, and statistics.

**Why this level:**

- **S4:** 180,210 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party Redis server and tool implementation under src, excluding tests, bundled dependencies, example modules, documentation, generated command data, and build metadata.
- **D4:** Low-level performance and distributed-state invariants recur across central server paths, though architecture remains deliberately direct.
- **C4:** Many integrated subsystems form a production data server, but the core deployment and request model are more compact than a multi-service platform.
- **Placement:** S4/D4/C4 makes Redis a balanced SDC 4 system.

**Quality-gate evidence:**

- **Source quality:** Command, client, object, persistence, replication, and cluster state are explicit in structs and functions, with comments around performance and consistency invariants.
- **Architecture:** An event loop feeds client protocol parsing and a command table; shared object and data-type modules connect to expiration, persistence, replication, cluster, scripting, and module subsystems.
- **Naming and idiom:** redisServer, client, robj, processCommand, call, propagate, dirty, expire, RDB, AOF, replication backlog, and cluster state reveal the server model.
- **Tests:** Tcl integration suites, unit tests, module tests, cluster and Sentinel tests, fuzzers, sanitizer runs, and failure injection cover commands, persistence, networking, replication, failover, and regressions.
- **Documentation:** The README and official command, data type, persistence, replication, clustering, module, administration, and contributor documentation provide deep context.
- **Traceability:** A client command can be followed from networking input through RESP parsing, command lookup and validation, execution against an object type, propagation to AOF and replicas, reply buffering, and integration tests.
- **Maintainability:** Central tables and shared primitives keep behavior discoverable, while subsystem-specific files and an extensive integration harness protect cross-cutting state transitions.
- **Educational value:** It is a rare advanced database whose direct C architecture still lets a reader trace a request without a framework maze.

**Inspection record:** commit `e1d7d50f9c244ce52f724b279fcb19773fffa98c`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Makefile`, `src/server.c`, `src/networking.c`, `tests/unit/networking.tcl`, `LICENSE.txt`. GitHub Linguist label: C. LOC exclusions: tests/, deps/, src/modules/.

**License:** [AGPL-3.0-only OR SSPL-1.0 OR LicenseRef-RSALv2](https://github.com/redis/redis/blob/e1d7d50f9c244ce52f724b279fcb19773fffa98c/LICENSE.txt)

## SDC 5

### [git/git](https://github.com/git/git)

**S5 / D5 / C5 → SDC 5**

The distributed version control system implementing content-addressed history, branches, merging, network protocols, and repository maintenance.

**Real-world evidence:** The repository builds the Git command suite used to create, exchange, review, and maintain source histories across the software industry.

**Language evidence:** Object storage, index and working-tree operations, revision traversal, diff and merge algorithms, refs, transports, protocols, commands, and repository maintenance are principally C across the root and builtin/.

**Why study it:** It joins compact immutable objects to graph algorithms, index and filesystem state, diff and merge engines, refs, packing and compression, transports, protocols, configuration, and a vast porcelain command surface.

**What you can learn:**

- Content-addressed storage, Merkle DAGs, indexes and working trees, revision walking, diff and merge algorithms, packfiles, refs and transactions, distributed protocols, partial clones, command dispatch, compatibility, and repository recovery.

**Prerequisites:**

- Expert C, filesystems and atomic updates, graphs and compression, hashing, networking and protocols, concurrency, shell, security, performance engineering, and navigating long-lived codebases.

**Start here:** [`git.c`](https://github.com/git/git/blob/c73e85354c275c9d409b26445089bc16940fc527/git.c) — The main dispatcher shows setup, alias and option handling, built-in command registration, external command fallback, repository context, and process exit behavior.

**Why this level:**

- **S5:** 325,816 meaningful implementation LOC measured with tokei 14.0.0. Count covers meaningful first-party Git command and library implementation, excluding tests, documentation, contrib tools, translations, templates, separate GUI projects, bundled SHA-1 code, generated files, and build metadata.
- **D5:** Deep algorithms and subtle persistence, concurrency, security, and backward-compatibility invariants are central throughout the system.
- **C5:** Git is a multi-process distributed system with many durable representations and cross-cutting workflows that must interoperate across versions and platforms.
- **Placement:** S5/D5/C5 requires SDC 5.

**Quality-gate evidence:**

- **Source quality:** Durable formats, lock and transaction rules, ownership, repository context, algorithm invariants, compatibility branches, and error paths are made explicit in focused modules.
- **Architecture:** Shared plumbing libraries implement objects, indexes, refs, revisions, diffs, merges, packs, configuration, and transport; built-in commands compose them, with helper processes at protocol and credential boundaries.
- **Naming and idiom:** object_id, repository, index_state, ref_transaction, rev_info, diff_options, unpack_trees_options, transport, refspec, and builtin expose Git's internal model.
- **Tests:** Thousands of shell, unit, integration, protocol, interoperability, fuzz, performance, leak, and platform tests cover commands, formats, crashes, security boundaries, and historical regressions.
- **Documentation:** Reference manuals, technical design documents, format and protocol specifications, tutorials, release notes, and contributor process are versioned in the repository.
- **Traceability:** A commit can be followed from builtin option handling through index refresh and tree writing, commit-object creation, ref transaction and reflog update, hooks, output, and end-to-end tests.
- **Maintainability:** Stable file formats and protocols are protected by compatibility tests, while subsystem libraries, repository-context migration, technical docs, and disciplined review support incremental evolution.
- **Educational value:** It is a definitive expert study of a distributed system whose foundational data model is simple but whose real-world guarantees are profound.

**Inspection record:** commit `c73e85354c275c9d409b26445089bc16940fc527`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Makefile`, `git.c`, `repository.c`, `builtin/commit.c`, `t/t0001-init.sh`, `COPYING`. GitHub Linguist label: C. LOC exclusions: t/, Documentation/, contrib/, po/, templates/, git-gui/, gitk-git/, sha1dc/.

**License:** [GPL-2.0-only](https://github.com/git/git/blob/c73e85354c275c9d409b26445089bc16940fc527/COPYING)

### [postgres/postgres](https://github.com/postgres/postgres)

**S5 / D5 / C5 → SDC 5**

A complete relational database system with SQL, extensible types and indexes, transactions, crash recovery, replication, security, and operational tooling.

**Real-world evidence:** The repository builds the PostgreSQL database server, client libraries, command-line tools, procedural-language support, and bundled extensions deployed worldwide.

**Language evidence:** The SQL frontend, planner and optimizer, executor, storage engines, transactions, write-ahead logging, replication, catalog, server processes, client libraries, tools, and extensions are principally C under src/ and contrib/.

**Why study it:** It exposes nearly every database topic in production form: parsing and planning, cost estimation, execution, MVCC, indexes, transactions, locking, WAL, recovery, replication, catalogs, extension hooks, and operations.

**What you can learn:**

- SQL parsing and rewriting, cost-based optimization, execution plans, storage and buffer management, MVCC, indexes, transactions and locks, WAL and crash recovery, replication, catalogs and types, extensions, security, and database operations.

**Prerequisites:**

- Expert C, relational theory and SQL, compilers and optimization, data structures and storage engines, concurrency control, operating systems, networking, distributed replication, security, performance analysis, and very large-codebase navigation.

**Start here:** [`src/backend/tcop/postgres.c`](https://github.com/postgres/postgres/blob/6c5f1d6074208146930b67c2054509c3e82f6f7f/src/backend/tcop/postgres.c) — The backend main loop and simple-query path connect protocol messages to parsing, rewriting, planning, portals, execution, transactions, errors, statistics, and client responses.

**Why this level:**

- **S5:** 1,615,105 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party server, client, utility, procedural-language, and bundled-extension implementation under src and contrib, excluding tests, regression inputs, test tooling, documentation, generated or vendored content, and build metadata.
- **D5:** Multiple deep computer-science and systems domains are fundamental, and their correctness depends on subtle concurrency and durable-state guarantees.
- **C5:** The system spans protocols, shared memory, durable storage, background processes, replication topologies, extensions, tools, and decades of compatibility constraints.
- **Placement:** S5/D5/C5 requires SDC 5.

**Quality-gate evidence:**

- **Source quality:** Subsystem interfaces, memory contexts, snapshots, locks, error recovery, transaction states, WAL rules, planner contracts, and durable formats are extensively documented alongside implementation.
- **Architecture:** Frontend protocol and traffic-cop code drive parser, analyzer, rewriter, planner, portals, and executor; storage, buffer, access methods, transactions, WAL, recovery, replication, catalogs, and background processes provide the database engine.
- **Naming and idiom:** QueryDesc, PlannedStmt, Portal, EState, Relation, TupleTableSlot, Snapshot, Buffer, XLogRecPtr, ResourceOwner, MemoryContext, and catalog vocabulary expose database internals.
- **Tests:** Regression, isolation, TAP, recovery, replication, authentication, extension, client, upgrade, fuzz, sanitizer, and platform suites cover SQL behavior and internal guarantees.
- **Documentation:** The comprehensive manual includes SQL and API references, internals, storage and concurrency chapters, extension guides, administration, replication, security, release notes, and developer conventions.
- **Traceability:** A SELECT can be followed from protocol input through parse, analyze and rewrite, planner path selection, Portal and Executor lifecycle, access methods and buffers, MVCC visibility, destination output, transaction completion, and regression tests.
- **Maintainability:** Strict subsystem conventions, hooks, memory and resource ownership systems, versioned catalogs and WAL, broad regression infrastructure, and long-form design comments support sustained evolution.
- **Educational value:** It is one of the richest available expert codebases for studying a complete database rather than isolated textbook components.

**Inspection record:** commit `6c5f1d6074208146930b67c2054509c3e82f6f7f`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `configure.ac`, `src/backend/tcop/postgres.c`, `src/backend/executor/execMain.c`, `src/test/regress/sql/select.sql`, `COPYRIGHT`. GitHub Linguist label: C. LOC exclusions: **/test/, **/regress/, **/isolation/, doc/, src/tools/, generated/, vendor/.

**License:** [PostgreSQL](https://github.com/postgres/postgres/blob/6c5f1d6074208146930b67c2054509c3e82f6f7f/COPYRIGHT)

_Generated from `catalog/c.json`; do not edit by hand._

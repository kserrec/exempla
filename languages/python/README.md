# Python

10 qualified repositories. Scores assume the learner described in [the SDC rubric](../../docs/sdc.md).

[← All languages](../README.md)

## SDC 1

### [dbader/schedule](https://github.com/dbader/schedule)

**S1 / D2 / C1 → SDC 1**

An in-process job scheduler with a fluent API for running Python callables at human-readable intervals.

**Real-world evidence:** The repository publishes a maintained scheduling package intended for recurring application jobs rather than an instructional toy.

**Language evidence:** The scheduler, jobs, interval calculations, decorators, and public API live in the Python module schedule/__init__.py.

**Why study it:** Its single main module demonstrates a complete domain model, fluent interface, time arithmetic, cancellation, and testable clock-dependent behavior.

**What you can learn:**

- Fluent APIs, datetime scheduling, ordering, cancellation sentinels, decorators, and deterministic tests around time.

**Prerequisites:**

- Python functions and classes, decorators, datetime arithmetic, exceptions, and sorting.

**Start here:** [`schedule/__init__.py`](https://github.com/dbader/schedule/blob/82a43db1b938d8fdf60103bd41f329e06c8d3651/schedule/__init__.py) — The Scheduler and Job classes expose the entire domain model and the calculation that turns fluent configuration into run times.

**Why this level:**

- **S1:** 1,978 meaningful implementation LOC measured with tokei 14.0.0. Count covers the schedule package, excluding the test suite, documentation, examples, and packaging files.
- **D2:** Time zones, missed intervals, deadlines, and randomized ranges add edge cases, but the implementation uses familiar Python constructs.
- **C1:** Scheduler owns a list of Jobs and each Job owns its next-run calculation; there are no workers, queues, or persistent stores.
- **Placement:** The entire useful scheduler remains readable as one local object model, so it belongs at SDC 1.

**Quality-gate evidence:**

- **Source quality:** Validation and next-run calculations are explicit, with domain errors and cancellation behavior kept close to their use sites.
- **Architecture:** Scheduler coordinates jobs while Job owns interval configuration and execution, producing a clean two-object model.
- **Naming and idiom:** The every, at, until, do, run_pending, and next_run vocabulary mirrors how users describe recurring work.
- **Tests:** A broad single-file suite covers units, tags, time zones, deadlines, missed runs, random intervals, cancellation, and failure cases.
- **Documentation:** The README provides executable examples, limitations, API patterns, and guidance for background execution.
- **Traceability:** A fluent statement can be traced through Job configuration, scheduling, due checks, execution, and rescheduling in one file.
- **Maintainability:** No hidden thread or persistence layer exists, and the clock can be replaced in tests through a small seam.
- **Educational value:** It is a rare production library whose complete behavioral model fits into an introductory repository reading.

**Inspection record:** commit `82a43db1b938d8fdf60103bd41f329e06c8d3651`, reviewed 2026-08-28 by Codex. Files sampled: `README.rst`, `schedule/__init__.py`, `test_schedule.py`, `docs/timezones.rst`. GitHub Linguist label: Python. LOC exclusions: test_schedule.py, docs.

**License:** [MIT](https://github.com/dbader/schedule/blob/82a43db1b938d8fdf60103bd41f329e06c8d3651/LICENSE.txt)

### [pallets/itsdangerous](https://github.com/pallets/itsdangerous)

**S1 / D2 / C1 → SDC 1**

A compact library for signing and timestamping data so tampering can be detected without encrypting the payload.

**Real-world evidence:** Pallets publishes ItsDangerous as the signing layer used by Flask and other production Python applications.

**Language evidence:** The signing, serialization, timestamp, encoding, and exception modules under src/itsdangerous are implemented in Python.

**Why study it:** A small codebase shows how a security-sensitive contract can remain explicit through focused abstractions, key derivation, serializers, and precise failure modes.

**What you can learn:**

- Message authentication, key derivation, constant-time comparison, serializer composition, timestamp validation, and exception design.

**Prerequisites:**

- Python classes and bytes, hashing and MAC concepts, serialization, and exceptions.

**Start here:** [`src/itsdangerous/signer.py`](https://github.com/pallets/itsdangerous/blob/672971d66a2ef9f85151e53283113f33d642dabd/src/itsdangerous/signer.py) — Signer contains the core key derivation, signature, verification, and unsigning contract used by the higher-level serializers.

**Why this level:**

- **S1:** 890 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party Python under src, excluding tests, documentation, and build metadata.
- **D2:** The cryptographic primitives and encoding rules need care, but the library delegates algorithms and keeps each transformation local.
- **C1:** A few classes layer serializers and timestamps over one signing abstraction without services, plugins, or persistence.
- **Placement:** Its compact topology and traceable data path make it SDC 1 despite the importance of its cryptographic boundary.

**Quality-gate evidence:**

- **Source quality:** Security-relevant operations are short, documented, and built on standard cryptographic primitives rather than homemade algorithms.
- **Architecture:** Signers, serializers, timestamps, encoding helpers, and exceptions form a small progression of responsibilities.
- **Naming and idiom:** Names such as derive_key, get_signature, unsign, and BadSignature make success and failure semantics visible.
- **Tests:** Focused tests cover key rotation, derivation methods, malformed signatures, fallback signers, timestamps, and serialization behavior.
- **Documentation:** The README and narrative documentation explain the trust model, use cases, API layers, and non-encryption boundary.
- **Traceability:** A payload can be followed from serializer through signer and digest comparison into a specific exception path.
- **Maintainability:** The narrow surface, typed code, isolated encoding helpers, and explicit compatibility hooks limit change impact.
- **Educational value:** It teaches production integrity checks without burying the learner in a full authentication framework.

**Inspection record:** commit `672971d66a2ef9f85151e53283113f33d642dabd`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/itsdangerous/signer.py`, `src/itsdangerous/serializer.py`, `tests/test_itsdangerous/test_signer.py`. GitHub Linguist label: Python. LOC exclusions: tests, docs.

**License:** [BSD-3-Clause](https://github.com/pallets/itsdangerous/blob/672971d66a2ef9f85151e53283113f33d642dabd/LICENSE.txt)

## SDC 2

### [pallets/click](https://github.com/pallets/click)

**S3 / D2 / C2 → SDC 2**

A composable command-line toolkit that maps decorators and command objects onto parsing, validation, help, invocation, and shell completion.

**Real-world evidence:** Pallets publishes Click as production CLI infrastructure used directly and by frameworks such as Flask.

**Language evidence:** Command parsing, parameter types, decorators, terminal helpers, and shell completion under src/click are Python.

**Why study it:** Its public decorators reveal a disciplined object model underneath, making it useful for studying API ergonomics, contexts, parsing, and extension points.

**What you can learn:**

- Decorator APIs, command trees, context propagation, parsing state machines, parameter conversion, help rendering, and shell completion.

**Prerequisites:**

- Decorators, callables, classes, iterators, terminal conventions, and command-line argument syntax.

**Start here:** [`src/click/core.py`](https://github.com/pallets/click/blob/36baa15ff831b939a22bc527cd76ce653ef6f66d/src/click/core.py) — Context, Command, Group, Parameter, Option, and Argument define the domain model that decorators construct.

**Why this level:**

- **S3:** 10,038 meaningful implementation LOC measured with tokei 14.0.0. Count covers Python under src/click, excluding tests, documentation, examples, and generated shell-completion artifacts.
- **D2:** The library has many behaviors, but individual mechanisms are idiomatic and the public abstraction maps cleanly to its core objects.
- **C2:** Several focused modules support one command invocation pipeline without external services or persistence.
- **Placement:** Its size reaches S3, but conventional mechanisms and a cohesive command pipeline yield SDC 2 under the published averaging rule.

**Quality-gate evidence:**

- **Source quality:** Parsing, conversion, help formatting, and context cleanup are factored into named units with detailed behavioral docstrings.
- **Architecture:** Core command objects coordinate parsing, types, decorators, formatting, terminal utilities, and completion through clear seams.
- **Naming and idiom:** Command, Group, Context, Option, Argument, Parameter, and ResultCallback form a consistent CLI vocabulary.
- **Tests:** The suite exercises commands, contexts, decorators, types, prompting, terminals, completion, deprecations, and compatibility.
- **Documentation:** Tutorials, API references, patterns, testing guidance, and examples explain both routine and advanced use.
- **Traceability:** A decorated function can be followed into a Command object, parser state, parameter processing, context invocation, and result handling.
- **Maintainability:** Public abstractions are stable while platform-specific terminal and completion behavior stays in dedicated modules.
- **Educational value:** It teaches how a polished declarative API can be implemented with explicit, inspectable runtime objects.

**Inspection record:** commit `36baa15ff831b939a22bc527cd76ce653ef6f66d`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/click/core.py`, `src/click/decorators.py`, `tests/test_commands.py`. GitHub Linguist label: Python. LOC exclusions: tests, docs, examples.

**License:** [BSD-3-Clause](https://github.com/pallets/click/blob/36baa15ff831b939a22bc527cd76ce653ef6f66d/LICENSE.txt)

### [psf/requests](https://github.com/psf/requests)

**S2 / D2 / C2 → SDC 2**

A synchronous HTTP client that turns URLs, headers, authentication, cookies, redirects, and connection pools into a small Python API.

**Real-world evidence:** Requests is released by the Python Software Foundation for production HTTP clients and maintains broad compatibility behavior.

**Language evidence:** The public API, sessions, models, authentication, cookies, adapters, and utilities under src/requests are Python.

**Why study it:** It shows how a friendly public API can sit over protocol details, stateful sessions, transport adapters, and disciplined exception translation.

**What you can learn:**

- API layering, request preparation, sessions, adapter boundaries, redirect policy, authentication, cookies, and exception normalization.

**Prerequisites:**

- HTTP fundamentals, context managers, Python mappings and classes, exceptions, and basic TLS concepts.

**Start here:** [`src/requests/sessions.py`](https://github.com/psf/requests/blob/5460f467b02e49471c0fd6cfc9ca0adab6351f98/src/requests/sessions.py) — Session.prepare_request and Session.send connect user configuration, persistent state, redirects, hooks, and the selected transport adapter.

**Why this level:**

- **S2:** 4,951 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party Python under src/requests, excluding tests, documentation, vendored certificates, and packaging files.
- **D2:** HTTP edge cases are substantive, but Requests deliberately presents them through conventional classes and readable control flow.
- **C2:** A request crosses several modules, yet the dependency boundary and preparation-to-send flow are stable and easy to identify.
- **Placement:** Moderate size and a clear layered request path make Requests an instructive SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** Input normalization, redirect rules, cookie handling, and transport exceptions are explicit and supported by narrow helpers.
- **Architecture:** API helpers feed Sessions and prepared Models, with adapters isolating the urllib3 transport implementation.
- **Naming and idiom:** PreparedRequest, Session, Response, Adapter, hooks, and merge_setting consistently describe the HTTP client lifecycle.
- **Tests:** The suite covers HTTP verbs, redirects, authentication, proxies, cookies, encodings, streaming, hooks, and regression cases.
- **Documentation:** README and guides document quick starts, advanced sessions, authentication, SSL, streaming, hooks, and exceptions.
- **Traceability:** A call to requests.get can be followed through api.request, Session.request, preparation, send, adapter, and response construction.
- **Maintainability:** Stable public objects and a distinct adapter boundary contain protocol and third-party transport changes.
- **Educational value:** It demonstrates the engineering behind an API that feels simpler than the protocol it represents.

**Inspection record:** commit `5460f467b02e49471c0fd6cfc9ca0adab6351f98`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/requests/api.py`, `src/requests/sessions.py`, `tests/test_requests.py`. GitHub Linguist label: Python. LOC exclusions: tests, docs, ext.

**License:** [Apache-2.0](https://github.com/psf/requests/blob/5460f467b02e49471c0fd6cfc9ca0adab6351f98/LICENSE)

## SDC 3

### [encode/httpx](https://github.com/encode/httpx)

**S2 / D3 / C3 → SDC 3**

A modern HTTP client with matching synchronous and asynchronous APIs, streaming, redirects, authentication, proxies, and pluggable transports.

**Real-world evidence:** Encode publishes HTTPX for production Python clients, with maintained protocol behavior and integrations built on HTTP Core.

**Language evidence:** Synchronous and asynchronous clients, models, authentication, decoders, URLs, and transports in the httpx package are Python.

**Why study it:** Its paired sync/async design makes resource lifetime, transport abstraction, exception translation, and API symmetry concrete.

**What you can learn:**

- Sync/async API parity, transport adapters, streaming lifecycles, exception mapping, redirects, authentication, and client state machines.

**Prerequisites:**

- HTTP, context managers, async iteration, type hints, exceptions, and TLS/proxy basics.

**Start here:** [`httpx/_client.py`](https://github.com/encode/httpx/blob/b5addb64f0161ff6bfe94c124ef76f6a1fba5254/httpx/_client.py) — Client and AsyncClient show request construction, state, redirects, authentication, event hooks, streaming, and transport delegation.

**Why this level:**

- **S2:** 7,308 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party Python in httpx, excluding tests, documentation, scripts, and package metadata.
- **D3:** Streaming ownership, redirects, authentication, timeouts, and paired concurrency styles require careful lifecycle reasoning.
- **C3:** Behavior crosses client state, models, authentication, decoders, URL logic, and sync/async transports, but boundaries are explicit.
- **Placement:** Moderate size with meaningful concurrency and transport architecture puts HTTPX squarely at SDC 3.

**Quality-gate evidence:**

- **Source quality:** State checks, default resolution, stream wrappers, and exception mapping make ownership and failure behavior explicit.
- **Architecture:** Clients build models and delegate I/O through a narrow transport interface, with parallel synchronous and asynchronous implementations.
- **Naming and idiom:** ClientState, Request, Response, ByteStream, Transport, Timeout, and Auth consistently describe the HTTP domain.
- **Tests:** Focused suites cover clients, transports, models, authentication, URLs, proxies, streaming, timeouts, and sync/async parity.
- **Documentation:** Quickstarts, advanced guides, API references, compatibility notes, and transport documentation explain the full surface.
- **Traceability:** A client call can be followed through request building, authentication, redirects, transport handling, streaming, and response closure.
- **Maintainability:** The HTTP Core boundary isolates protocol engines while transport interfaces make testing and custom I/O straightforward.
- **Educational value:** It provides a clean study of one API expressed over both synchronous and asynchronous resource models.

**Inspection record:** commit `b5addb64f0161ff6bfe94c124ef76f6a1fba5254`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `httpx/_client.py`, `httpx/_transports/default.py`, `tests/client/test_client.py`. GitHub Linguist label: Python. LOC exclusions: tests, docs, scripts.

**License:** [BSD-3-Clause](https://github.com/encode/httpx/blob/b5addb64f0161ff6bfe94c124ef76f6a1fba5254/LICENSE.md)

### [pallets/flask](https://github.com/pallets/flask)

**S2 / D3 / C3 → SDC 3**

A web application framework that composes routing, request contexts, templating, sessions, error handling, and extensions over Werkzeug.

**Real-world evidence:** Pallets maintains and publishes Flask as a production web framework with a mature extension ecosystem.

**Language evidence:** Application, blueprint, context, helper, session, CLI, and templating integration modules under src/flask are Python.

**Why study it:** Flask keeps the web lifecycle visible while demonstrating context-local state, decorators, extension hooks, blueprints, and separation from lower-level HTTP machinery.

**What you can learn:**

- WSGI request dispatch, application and request contexts, blueprints, hooks, error resolution, sessions, and dependency boundaries.

**Prerequisites:**

- HTTP and WSGI basics, decorators, context managers, mappings, exceptions, and template concepts.

**Start here:** [`src/flask/app.py`](https://github.com/pallets/flask/blob/d318b683471101618febed18996405ad26462110/src/flask/app.py) — Flask dispatch, hooks, errors, response finalization, and WSGI entry points meet in the application class.

**Why this level:**

- **S2:** 7,660 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party Python under src/flask, excluding tests, documentation, examples, and project metadata.
- **D3:** Correctness depends on nested contexts, hook ordering, error selection, and response conversion across synchronous and asynchronous views.
- **C3:** A request crosses several framework components and an important Werkzeug boundary, though each responsibility remains identifiable.
- **Placement:** Framework lifecycle reasoning balances its moderate code size, making Flask a representative SDC 3 project.

**Quality-gate evidence:**

- **Source quality:** Lifecycle stages are named, documented, and wrapped in controlled context cleanup and error handling.
- **Architecture:** Application, blueprints, contexts, helpers, sessions, templating, and CLI integration have explicit responsibilities over Werkzeug.
- **Naming and idiom:** before_request, dispatch_request, make_response, teardown_request, and context names mirror the web lifecycle.
- **Tests:** Extensive tests cover dispatch, contexts, blueprints, sessions, templates, CLI behavior, signals, errors, and regressions.
- **Documentation:** Quickstarts, tutorials, patterns, API references, extension guidance, and deployment material support multiple learning depths.
- **Traceability:** A WSGI call can be traced through context creation, preprocessing, dispatch, response processing, and teardown.
- **Maintainability:** The Werkzeug/Jinja boundaries and extension hooks are explicit, while shared lifecycle logic stays centralized.
- **Educational value:** It exposes the machinery of a real web framework without the breadth of a batteries-included platform.

**Inspection record:** commit `d318b683471101618febed18996405ad26462110`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `src/flask/app.py`, `src/flask/ctx.py`, `tests/test_basic.py`. GitHub Linguist label: Python. LOC exclusions: tests, docs, examples.

**License:** [BSD-3-Clause](https://github.com/pallets/flask/blob/d318b683471101618febed18996405ad26462110/LICENSE.txt)

## SDC 4

### [pytest-dev/pytest](https://github.com/pytest-dev/pytest)

**S3 / D4 / C4 → SDC 4**

An extensible testing framework that discovers tests, resolves fixtures, rewrites assertions, runs lifecycle hooks, and reports results.

**Real-world evidence:** pytest is released as production test infrastructure and supports a large plugin ecosystem across Python projects.

**Language evidence:** Collection, fixtures, assertion rewriting, hooks, configuration, execution, reports, and terminal output under src/_pytest are Python.

**Why study it:** It demonstrates a mature plugin architecture whose dynamic behavior still has explicit collection nodes, hook contracts, fixture graphs, and execution phases.

**What you can learn:**

- Plugin hooks, collection trees, fixture dependency resolution, AST assertion rewriting, setup/call/teardown phases, and structured reports.

**Prerequisites:**

- Python import machinery, decorators and generators, AST concepts, dependency graphs, exceptions, and testing fundamentals.

**Start here:** [`src/_pytest/main.py`](https://github.com/pytest-dev/pytest/blob/fdba12e1708313f56e9cf713d260c029764ca2b7/src/_pytest/main.py) — Session startup, collection, failure policy, and the run loop provide the map needed before entering fixtures or assertion rewriting.

**Why this level:**

- **S3:** 32,506 meaningful implementation LOC measured with tokei 14.0.0. Count covers production Python under src, excluding the test suite, documentation, benchmarks, examples, and generated files.
- **D4:** Core behavior repeatedly depends on metaprogramming, import state, hook dispatch, scoped dependency resolution, and exception-aware phases.
- **C4:** A test run crosses configuration, discovery, nodes, plugins, fixtures, assertion rewriting, runners, capture, warnings, and reporters.
- **Placement:** Advanced mechanisms and a multi-subsystem execution pipeline raise this S3-sized codebase to SDC 4.

**Quality-gate evidence:**

- **Source quality:** Dense mechanisms are backed by strong type hints, explicit hook specifications, structured nodes and reports, and carefully scoped helpers.
- **Architecture:** Configuration and plugins drive a collection tree, fixture manager, phased runner, assertion engine, capture services, and reporters.
- **Naming and idiom:** Collector, Item, Session, FixtureDef, CallInfo, TestReport, and hook names provide a shared execution vocabulary.
- **Tests:** A large self-hosting suite covers collection, fixtures, hooks, assertions, capture, terminal output, configuration, and regressions.
- **Documentation:** User guides, how-to material, references, examples, plugin guidance, and contributor documentation cover both consumers and extenders.
- **Traceability:** A test can be traced from discovery through node collection, fixture setup, runtest phases, report construction, and plugin reporting.
- **Maintainability:** Hook contracts and structured domain objects let independent plugins evolve around a stable lifecycle.
- **Educational value:** It is an unusually transparent example of extensible developer tooling, metaprogramming, and framework self-testing.

**Inspection record:** commit `fdba12e1708313f56e9cf713d260c029764ca2b7`, reviewed 2026-08-28 by Codex. Files sampled: `README.rst`, `src/_pytest/main.py`, `src/_pytest/python.py`, `testing/test_collection.py`. GitHub Linguist label: Python. LOC exclusions: testing, doc, bench.

**License:** [MIT](https://github.com/pytest-dev/pytest/blob/fdba12e1708313f56e9cf713d260c029764ca2b7/LICENSE)

### [scrapy/scrapy](https://github.com/scrapy/scrapy)

**S3 / D4 / C4 → SDC 4**

An asynchronous web-crawling framework coordinating spiders, request scheduling, downloading, scraping, pipelines, extensions, and signals.

**Real-world evidence:** Scrapy is released as a production crawling and extraction framework with maintained middleware and extension ecosystems.

**Language evidence:** Crawler orchestration, engine, scheduler, downloader, scraper, spiders, middleware, pipelines, and extensions in the scrapy package are Python.

**Why study it:** Its event-driven engine makes backpressure, lifecycle ownership, pluggable stages, settings, signals, and concurrency coordination visible in Python.

**What you can learn:**

- Asynchronous engines, schedulers, middleware chains, backpressure, signals, extension loading, settings precedence, and lifecycle state.

**Prerequisites:**

- Async Python, deferred/future concepts, HTTP crawling, queues, callbacks, dependency injection, and framework configuration.

**Start here:** [`scrapy/core/engine.py`](https://github.com/scrapy/scrapy/blob/53eb8d60bcd0160633f6513478f958ed5a457363/scrapy/core/engine.py) — ExecutionEngine coordinates scheduler, downloader, scraper, spider input, backpressure, startup, idleness, and shutdown.

**Why this level:**

- **S3:** 25,936 meaningful implementation LOC measured with tokei 14.0.0. Count covers production Python in scrapy, excluding tests, typing tests, documentation, examples, and packaging files.
- **D4:** Deferred/coroutine bridging, reactor selection, concurrent slots, cancellation, and signal ordering recur through core lifecycle code.
- **C4:** Crawling crosses settings, add-ons, signals, scheduler, downloader, scraper, spiders, item pipelines, stats, and process orchestration.
- **Placement:** Its advanced asynchronous lifecycle and interconnected plugin pipeline make Scrapy SDC 4 despite a mid-sized source count.

**Quality-gate evidence:**

- **Source quality:** Lifecycle flags, late-bound attributes, error translation, and shutdown paths are explicit in the engine and crawler orchestration.
- **Architecture:** The engine mediates distinct scheduler, downloader, scraper, spider, middleware, pipeline, signal, and extension components.
- **Naming and idiom:** Crawler, Spider, Scheduler, Downloader, Scraper, Request, Response, Item, and Signal consistently model the crawl pipeline.
- **Tests:** Extensive unit and integration tests cover reactors, crawlers, engines, middleware, protocols, pipelines, commands, and regressions.
- **Documentation:** Tutorials, topic guides, API references, extension docs, architecture explanations, and deployment guidance are comprehensive.
- **Traceability:** A request can be followed from spider output through scheduling, downloading, response handling, item processing, and idle detection.
- **Maintainability:** Protocols and component loaders isolate replaceable implementations while settings and signals provide controlled extension surfaces.
- **Educational value:** It is a concrete production example of an asynchronous pipeline framework rather than a thin wrapper around an event loop.

**Inspection record:** commit `53eb8d60bcd0160633f6513478f958ed5a457363`, reviewed 2026-08-28 by Codex. Files sampled: `README.rst`, `scrapy/crawler.py`, `scrapy/core/engine.py`, `tests/test_crawler.py`. GitHub Linguist label: Python. LOC exclusions: tests, tests_typing, docs.

**License:** [BSD-3-Clause](https://github.com/scrapy/scrapy/blob/53eb8d60bcd0160633f6513478f958ed5a457363/LICENSE)

## SDC 5

### [apache/airflow](https://github.com/apache/airflow)

**S5 / D4 / C5 → SDC 5**

A workflow-orchestration platform that defines directed task graphs and schedules, executes, retries, observes, and persists their runs.

**Real-world evidence:** Apache Airflow is an actively released Apache project used to operate production data and automation workflows.

**Language evidence:** The scheduler, DAG and task models, executors, APIs, providers, serialization, jobs, and operational services are predominantly Python.

**Why study it:** It exposes the engineering of a distributed control plane: durable workflow state, transactional scheduling, executors, serialization, APIs, plugins, and deployment boundaries.

**What you can learn:**

- Distributed scheduling, DAG models, transactional locking, concurrency limits, executors, durable state machines, serialization, plugins, and service boundaries.

**Prerequisites:**

- Advanced Python, SQL and transactions, distributed systems, queues, concurrency, web APIs, and deployment architecture.

**Start here:** [`airflow-core/src/airflow/jobs/scheduler_job_runner.py`](https://github.com/apache/airflow/blob/ff601cb5b75e77c1f28aaf014914f4e9d5cb0947/airflow-core/src/airflow/jobs/scheduler_job_runner.py) — The scheduler loop and executable-task selection reveal how persisted DAG state, locks, priorities, pools, and concurrency limits become work.

**Why this level:**

- **S5:** 469,511 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party Python across Airflow core, providers, SDKs, and operational packages, excluding tests, documentation, generated output, and vendored dependencies.
- **D4:** Correctness repeatedly depends on database isolation, locks, idempotence, concurrency limits, serialization, retries, and distributed worker state.
- **C5:** Workflow behavior spans many deployable processes, databases, executors, APIs, task SDKs, providers, security boundaries, and operational tooling.
- **Placement:** Extreme size plus platform-scale architecture and advanced distributed behavior make Airflow an unambiguous SDC 5 repository.

**Quality-gate evidence:**

- **Source quality:** Critical scheduling code documents lock scope, starvation filters, concurrency maps, transactional assumptions, and failure handling.
- **Architecture:** Core models and jobs connect schedulers, executors, APIs, task SDKs, providers, serialization, security, UI, and deployment packages.
- **Naming and idiom:** DAG, DagRun, TaskInstance, SchedulerJobRunner, Executor, Pool, Bundle, and Provider form a precise operational vocabulary.
- **Tests:** Large unit, integration, system, provider, serialization, API, and end-to-end suites exercise the platform and its database backends.
- **Documentation:** Architecture, administration, operations, security, provider, API, tutorial, and contributor documentation is extensive.
- **Traceability:** A scheduled task can be traced from serialized DAG state through DagRun and TaskInstance selection, locking, executor dispatch, and state reconciliation.
- **Maintainability:** Public interfaces, provider boundaries, database models, service packages, and compatibility policies constrain a very large change surface.
- **Educational value:** It rewards advanced readers with a real distributed orchestration control plane whose tradeoffs are visible in source.

**Inspection record:** commit `ff601cb5b75e77c1f28aaf014914f4e9d5cb0947`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `airflow-core/src/airflow/models/dag.py`, `airflow-core/src/airflow/jobs/scheduler_job_runner.py`, `airflow-core/tests/unit/models/test_dag.py`. GitHub Linguist label: Python. LOC exclusions: tests, docs, generated, third-party front-end dependencies.

**License:** [Apache-2.0](https://github.com/apache/airflow/blob/ff601cb5b75e77c1f28aaf014914f4e9d5cb0947/LICENSE)

### [home-assistant/core](https://github.com/home-assistant/core)

**S5 / D4 / C5 → SDC 5**

A home-automation runtime that coordinates devices, integrations, events, services, entity state, configuration, storage, and user automations.

**Real-world evidence:** Home Assistant Core is continuously released as the production engine behind deployed home-automation installations.

**Language evidence:** The automation runtime, state machine, services, event bus, configuration entries, integrations, and coordinators are implemented in Python.

**Why study it:** Its huge integration surface is organized around a coherent event loop, state and service models, lifecycle contracts, typed configuration entries, and strict concurrency rules.

**What you can learn:**

- Event-driven architecture, state machines, service registries, async task ownership, integration lifecycles, configuration migrations, persistence, and compatibility policy.

**Prerequisites:**

- Advanced asyncio, event-driven systems, typed Python, dependency injection, device protocols, persistence, and large-project navigation.

**Start here:** [`homeassistant/core.py`](https://github.com/home-assistant/core/blob/471f2c28e285c268cc4ca67ad80ff4044b365d70/homeassistant/core.py) — HomeAssistant, EventBus, ServiceRegistry, StateMachine, jobs, and core lifecycle states define the shared runtime every integration enters.

**Why this level:**

- **S5:** 1,266,444 meaningful implementation LOC measured with tokei 14.0.0. Count covers production Python under homeassistant, excluding tests, type stubs, maintenance scripts, generated metadata, and deployment assets.
- **D4:** Correct behavior relies on async ownership, thread-safety rules, staged setup and teardown, migrations, retries, and many external protocols.
- **C5:** Core services connect an enormous integration graph, entity platform, automation engine, storage, authentication, networking, and deployment lifecycle.
- **Placement:** Million-line scale and ecosystem-wide runtime coordination make Home Assistant Core decisively SDC 5.

**Quality-gate evidence:**

- **Source quality:** Core concurrency contracts, lifecycle states, immutable configuration data, and failure paths are explicit and increasingly type checked.
- **Architecture:** A central event bus, state machine, service registry, configuration-entry manager, entity model, and integration loader coordinate domain packages.
- **Naming and idiom:** HomeAssistant, EventBus, StateMachine, ServiceRegistry, ConfigEntry, Entity, and coordinator vocabulary is consistent across integrations.
- **Tests:** A vast suite covers core services, state, configuration, integrations, protocols, migrations, concurrency rules, and regressions.
- **Documentation:** Developer architecture, integration quality rules, APIs, testing guidance, user documentation, and contributor standards are extensive.
- **Traceability:** A device update can be traced from an integration coordinator through entity state writing, event dispatch, service behavior, and tests.
- **Maintainability:** Manifest contracts, integration boundaries, shared helpers, code ownership, strict linting, typing tiers, and quality scales govern the large surface.
- **Educational value:** It is a demanding but unusually well-governed case study in sustaining an async platform with thousands of real hardware integrations.

**Inspection record:** commit `471f2c28e285c268cc4ca67ad80ff4044b365d70`, reviewed 2026-08-28 by Codex. Files sampled: `README.rst`, `homeassistant/core.py`, `homeassistant/config_entries.py`, `tests/test_core.py`. GitHub Linguist label: Python. LOC exclusions: tests, stubs, script, generated metadata.

**License:** [Apache-2.0](https://github.com/home-assistant/core/blob/471f2c28e285c268cc4ca67ad80ff4044b365d70/LICENSE.md)

_Generated from `catalog/python.json`; do not edit by hand._

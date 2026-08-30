# Python

6 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

[← All languages](../README.md)

## Level 1 — First real code

No qualified learning path has been published at this level. An empty Level 1 means Exempla has not yet found a path gentle enough to publish here; learners are not being told to jump to Level 2.

## Level 2 — Guided real-world code

No qualified learning path has been published at this level. Standards are not lowered to fill a slot.

## Level 3 — Intermediate

### [pallets/click](https://github.com/pallets/click)

**Language 3 / Behavior 3 / Design 3 / Constraints 3 → Level 3**

A composable command-line toolkit that maps decorators and command objects onto parsing, validation, help, invocation, and shell completion.

**Why study it:** Starting with Click's decorators connects a polished declarative API to the command objects, parser state, managed contexts, callbacks, errors, and cleanup that implement it.

**Short context:**

- A command-line program converts argument tokens into typed parameters, invokes a callback within a context, and reports usage or errors to a terminal.

**Prerequisites:**

- Basic familiarity with Python functions and classes, collections, exceptions, decorators, context managers, generators and asynchronous basics, and focused tests.

**Concepts this path develops:**

- Overloaded higher-order decorators.
- Parser and parameter-processing state.
- Stable declarative API.

**What you can learn:**

- Use `src/click/decorators.py` to study the following transferable techniques and behaviors: Higher-order decorators, dynamic declaration metadata, command construction, parameter parsing, context propagation, nested invocation, usage errors, return values, and deterministic teardown.

**Learning path:**

- **Goal:** Understand how a decorated Python callback becomes a command, parses arguments into parameters, invokes inside a managed context, and produces a result or usage error.
- **Start here:** [`src/click/decorators.py`](https://github.com/pallets/click/blob/36baa15ff831b939a22bc527cd76ce653ef6f66d/src/click/decorators.py) — decorators.py is where user functions and parameter declarations become Command objects, so it establishes the public contract before the trace enters parsing and invocation internals.
- **Then read:**
  - [`src/click/core.py`](https://github.com/pallets/click/blob/36baa15ff831b939a22bc527cd76ce653ef6f66d/src/click/core.py)
  - [`src/click/parser.py`](https://github.com/pallets/click/blob/36baa15ff831b939a22bc527cd76ce653ef6f66d/src/click/parser.py)
  - [`tests/test_commands.py`](https://github.com/pallets/click/blob/36baa15ff831b939a22bc527cd76ce653ef6f66d/tests/test_commands.py)
- **Trace:** Start at @command and parameter decorators as they create a Command and attach declaration metadata; continue through Command.main, make_context, parser construction, argument processing, and Context.invoke into the original callback and context cleanup; correlate invocation, nested command, default, error, return-value, and teardown behavior in test_commands.py.

**Why this level:**

- **Language technique 3:** Decorators, overloads, higher-order construction, dynamic metadata, and managed contexts materially shape the public-to-runtime path.
- **Behavioral reasoning 3:** Token consumption, defaults, context state, nested invocation, error translation, and cleanup create nontrivial behavior across one command run.
- **Design span 3:** The trace crosses several framework abstractions whose responsibilities remain explicit and independently testable.
- **Constraint burden 3:** Several material public, lifecycle, and cross-platform CLI guarantees constrain implementation changes.
- **Placement:** The four scores 3/3/3/3 sum to 12; their arithmetic mean is 3.00 and rounds half-up to Level 3. The published result is Level 3.

**License:** BSD-3-Clause ([evidence 1](https://github.com/pallets/click/blob/36baa15ff831b939a22bc527cd76ce653ef6f66d/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Pallets publishes Click as production CLI infrastructure used directly and by frameworks such as Flask.

**Language evidence:** Command parsing, parameter types, decorators, terminal helpers, and shell completion under src/click are Python.

**Coding relevance:**

The README and familiar command-line conventions provide sufficient context; the path primarily teaches declarative API construction, parsing, context propagation, invocation, cleanup, and compatibility.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The decorators preserve callback metadata and declarations in focused constructors, while core command and context methods document parsing, invocation, error, and cleanup behavior.
- **Architecture:** Decorator construction, Command and Context objects, the parser, parameter conversion, callback invocation, and terminal behavior are separated by clear seams.
- **Naming and idiom:** command, option, argument, Context, make_context, invoke, result callback, and usage error form a consistent command-line vocabulary.
- **Tests:** tests/test_commands.py covers decorated commands, defaults, nested groups, invocation, return values, usage failures, context behavior, and teardown relevant to the trace.
- **Documentation:** Tutorials, API references, patterns, testing guidance, and examples explain both decorator use and the command and context lifecycle underneath it.
- **Traceability:** A decorated callback can be followed through Command construction, parser creation, argument processing, Context.invoke, result handling, and context cleanup, with direct assertions for each stage.
- **Maintainability:** Stable public decorators build explicit runtime objects, allowing parsing, contexts, parameters, terminals, and completion behavior to evolve behind documented contracts.
- **Educational value:** This path makes the implementation cost of a declarative Python API visible without losing the approachable call site that motivates it.

**Inspection record:** commit `36baa15ff831b939a22bc527cd76ce653ef6f66d`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/click/decorators.py`, `src/click/core.py`, `src/click/parser.py`, `tests/test_commands.py`, `LICENSE.txt`. GitHub Linguist label: Python.

</details>

### [psf/requests](https://github.com/psf/requests)

**Language 2 / Behavior 3 / Design 3 / Constraints 4 → Level 3**

A synchronous HTTP client that turns URLs, headers, authentication, cookies, redirects, and connection pools into a small Python API.

**Why study it:** Beginning with requests.get and api.request shows how a deliberately small convenience API creates and cleans up a Session while preserving preparation, redirect, transport, streaming, and security policy.

**Short context:**

- An HTTP client prepares a request, sends it through a connection-pool adapter, and may follow redirects while preserving or removing method, body, cookies, and credentials according to HTTP and security rules.

**Prerequisites:**

- Basic familiarity with Python functions and classes, collections, exceptions, decorators, context managers, generators and asynchronous basics, and focused tests.

**Concepts this path develops:**

- Layering a convenience API over persistent session preparation and adapter dispatch.
- Redirect history, method rewriting, cookies, credentials, and replayable request bodies.
- Ownership and cleanup of streamed responses across success, redirect, and exception paths.

**What you can learn:**

- Use `src/requests/api.py` to study the following transferable techniques and behaviors: API layering, temporary and persistent sessions, request preparation, adapter dispatch, redirect state, cookie and credential policy, streamed-response ownership, hooks, and exception cleanup.

**Learning path:**

- **Goal:** Understand how requests.get becomes a prepared request, passes through a persistent Session and adapter, follows redirects safely, and returns or closes a streamed response.
- **Start here:** [`src/requests/api.py`](https://github.com/psf/requests/blob/5460f467b02e49471c0fd6cfc9ca0adab6351f98/src/requests/api.py) — api.py contains the familiar request and verb helpers and immediately exposes their temporary-Session lifetime, making it the clearest entrance to the selected public-API-to-transport trace.
- **Then read:**
  - [`src/requests/sessions.py`](https://github.com/psf/requests/blob/5460f467b02e49471c0fd6cfc9ca0adab6351f98/src/requests/sessions.py)
  - [`src/requests/models.py`](https://github.com/psf/requests/blob/5460f467b02e49471c0fd6cfc9ca0adab6351f98/src/requests/models.py)
  - [`src/requests/adapters.py`](https://github.com/psf/requests/blob/5460f467b02e49471c0fd6cfc9ca0adab6351f98/src/requests/adapters.py)
  - [`tests/test_requests.py`](https://github.com/psf/requests/blob/5460f467b02e49471c0fd6cfc9ca0adab6351f98/tests/test_requests.py)
- **Trace:** Begin at api.request and its temporary Session, then follow Session.request through Request and PreparedRequest construction, cookie, authentication, hook, and environment merging; continue through Session.send to the selected adapter and Response, then through redirect method, body, credential, cookie, rewind, and connection-release policy, correlating the focused redirect, streaming, authentication, cookie, hook, and failure tests.

**Why this level:**

- **Language technique 2:** The path is built from conventional professional Python object, iterator, callback, and context-manager idioms.
- **Behavioral reasoning 3:** Redirect transitions, mutable session state, hooks, stream ownership, and error cleanup materially affect the request over time.
- **Design span 3:** The trace crosses several meaningful but locally understandable layers from convenience API to model and transport.
- **Constraint burden 4:** Security, HTTP compatibility, persistent state, and resource-lifetime guarantees interact throughout normal redirect handling.
- **Placement:** The four scores 2/3/3/4 sum to 12; their arithmetic mean is 3.00 and rounds half-up to Level 3. The published result is Level 3.

**License:** Apache-2.0 ([evidence 1](https://github.com/psf/requests/blob/5460f467b02e49471c0fd6cfc9ca0adab6351f98/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Requests is released by the Python Software Foundation for production HTTP clients and maintains broad compatibility behavior.

**Language evidence:** The public API, sessions, models, authentication, cookies, adapters, and utilities under src/requests are Python.

**Coding relevance:**

Ordinary HTTP concepts and the repository documentation are sufficient; the difficult work is transferable API layering, state management, adapter design, resource cleanup, compatibility, and security policy.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The API helper is intentionally small, while Session and adapter code make request normalization, redirects, stream ownership, and cleanup branches explicit.
- **Architecture:** Public API helpers feed Session, Request, PreparedRequest, Response, and transport-adapter layers with recognizable ownership boundaries.
- **Naming and idiom:** request, Session, PreparedRequest, Response, hooks, adapters, redirect history, and merge settings consistently describe the HTTP client lifecycle.
- **Tests:** tests/test_requests.py directly covers verbs, redirects, authentication, cookies, hooks, streaming, rewind behavior, transport failures, and response cleanup used by this path.
- **Documentation:** The quick start and advanced guides explain sessions, authentication, SSL, streaming, hooks, redirects, and exceptions at the level this trace requires.
- **Traceability:** A requests.get call can be followed from api.request through Session.request, preparation, adapter send, Response construction, redirect rebuilding, and connection release into focused tests.
- **Maintainability:** The narrow public helpers and stable model and adapter boundaries isolate convenience API, persistent state, redirect policy, and third-party transport changes.
- **Educational value:** The path demonstrates how a friendly API remains small by delegating difficult state, security, compatibility, and resource-lifetime work to explicit layers.

**Inspection record:** commit `5460f467b02e49471c0fd6cfc9ca0adab6351f98`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/requests/api.py`, `src/requests/sessions.py`, `src/requests/models.py`, `src/requests/adapters.py`, `tests/test_requests.py`, `LICENSE`. GitHub Linguist label: Python.

</details>

## Level 4 — Advanced

### [pallets/flask](https://github.com/pallets/flask)

**Language 3 / Behavior 4 / Design 3 / Constraints 4 → Level 4**

A web application framework that composes routing, request contexts, templating, sessions, error handling, and extensions over Werkzeug.

**Why study it:** The Flask request path shows one complete WSGI lifecycle through scoped context binding, routing, hooks, view dispatch, error handling, response finalization, and guaranteed teardown.

**Short context:**

- WSGI presents one HTTP request as an environment and response callback; Flask binds application and request context to the active execution before routing and dispatch.

**Prerequisites:**

- Working familiarity with Python functions and classes, collections, exceptions, decorators, context managers, generators and asynchronous basics, and focused tests, plus experience tracing behavior across several production files.

**Concepts this path develops:**

- Decorator and framework idioms.
- Nested application and request context ownership.
- WSGI and HTTP response semantics.

**What you can learn:**

- Use `src/flask/app.py` to study the following transferable techniques and behaviors: WSGI application entry, RequestContext ownership, ContextVar-backed globals, route matching, before and after hooks, sync-to-async adaptation, error handlers, response conversion, and teardown ordering.

**Learning path:**

- **Goal:** Understand one complete Flask request from WSGI entry through context binding, routing, hooks, dispatch, error handling, response finalization, and teardown.
- **Start here:** [`src/flask/app.py`](https://github.com/pallets/flask/blob/d318b683471101618febed18996405ad26462110/src/flask/app.py) — src/flask/app.py owns Flask.wsgi_app and full_dispatch_request, which coordinate the selected lifecycle before delegating context storage to ctx.py and globals.py.
- **Then read:**
  - [`src/flask/ctx.py`](https://github.com/pallets/flask/blob/d318b683471101618febed18996405ad26462110/src/flask/ctx.py)
  - [`src/flask/globals.py`](https://github.com/pallets/flask/blob/d318b683471101618febed18996405ad26462110/src/flask/globals.py)
  - [`tests/test_basic.py`](https://github.com/pallets/flask/blob/d318b683471101618febed18996405ad26462110/tests/test_basic.py)
- **Trace:** Follow Flask.wsgi_app as it creates and pushes RequestContext, uses context-backed globals, matches the route, runs full_dispatch_request, preprocessors, the view, error handlers, make_response and process_response, then pops contexts and runs teardown even after failure; correlate ordering, short-circuit, exception, response, and teardown tests.

**Why this level:**

- **Language technique 3:** Substantial framework abstractions and scoped-context machinery recur throughout the request path without requiring expert Python metaprogramming.
- **Behavioral reasoning 4:** Hook propagation, exception resolution, nested contexts, response finalization, and guaranteed teardown must be held together across the lifecycle.
- **Design span 3:** The trace crosses several meaningful framework and dependency boundaries while retaining locally clear responsibilities.
- **Constraint burden 4:** Multiple strict protocol, resource, isolation, error, and compatibility guarantees interact throughout normal dispatch.
- **Placement:** The four scores 3/4/3/4 sum to 14; their arithmetic mean is 3.50 and rounds half-up to Level 4. The published result is Level 4.

**License:** BSD-3-Clause ([evidence 1](https://github.com/pallets/flask/blob/d318b683471101618febed18996405ad26462110/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Pallets maintains and publishes Flask as a production web framework with a mature extension ecosystem.

**Language evidence:** Application, blueprint, context, helper, session, CLI, and templating integration modules under src/flask are Python.

**Coding relevance:**

A short HTTP, WSGI, and context prerequisite is enough; the path's difficulty comes from transferable lifecycle staging, scoped state, hook ordering, exception handling, cleanup, and dependency boundaries.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Named application methods separate WSGI entry, request preprocessing, view dispatch, error handling, response processing, and teardown.
- **Architecture:** Flask application orchestration, RequestContext ownership, ContextVar-backed globals, Werkzeug routing, and response construction meet at explicit boundaries.
- **Naming and idiom:** wsgi_app, full_dispatch_request, preprocess_request, dispatch_request, handle_exception, process_response, and teardown_request state lifecycle order.
- **Tests:** tests/test_basic.py covers hook ordering, early returns, view and error behavior, response construction, nested contexts, and teardown after success or failure.
- **Documentation:** Flask's request-context, application-context, lifecycle, error-handling, and asynchronous-callback documentation explains the contracts visible in this trace.
- **Traceability:** A WSGI request can be followed from wsgi_app through context push, route match, hooks, view or handler, response processing, and context pop into focused lifecycle assertions.
- **Maintainability:** Explicit Flask and Werkzeug boundaries plus guaranteed context cleanup isolate extension hooks without obscuring request ownership.
- **Educational value:** The path turns a framework request into an observable sequence of context, dispatch, response, and cleanup decisions suitable for advanced study.

**Inspection record:** commit `d318b683471101618febed18996405ad26462110`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/flask/app.py`, `src/flask/ctx.py`, `src/flask/globals.py`, `tests/test_basic.py`, `LICENSE.txt`. GitHub Linguist label: Python.

</details>

### [pytest-dev/pytest](https://github.com/pytest-dev/pytest)

**Language 4 / Behavior 4 / Design 4 / Constraints 4 → Level 4**

An extensible testing framework that discovers tests, resolves fixtures, rewrites assertions, runs lifecycle hooks, and reports results.

**Why study it:** The collection path shows how pytest converts command-line paths into a deterministic extensible tree while coordinating imports, plugin hooks, reflection, parametrization, duplicate policy, and failures.

**Short context:**

- Test collection turns command-line paths and Python objects into a tree of Collector and Item nodes while plugins may observe or replace stages through hooks.

**Prerequisites:**

- Working familiarity with Python functions and classes, collections, exceptions, decorators, context managers, generators and asynchronous basics, and focused tests, plus experience tracing behavior across several production files.

**Concepts this path develops:**

- Reflection and dynamic Python-object discovery.
- Recursive collection-tree expansion.
- Plugin and node API compatibility.

**What you can learn:**

- Use `src/_pytest/main.py` to study the following transferable techniques and behaviors: Recursive collector trees, filesystem hook proxies, dynamic imports, reflective Python discovery, plugin dispatch, cached collectors, parametrized item generation, node identifiers, duplicate handling, and collection reports.

**Learning path:**

- **Goal:** Understand how pytest converts command-line paths into a deterministic collection tree of Python test items while honoring plugin hooks, imports, parametrization, duplicates, and collection failures.
- **Start here:** [`src/_pytest/main.py`](https://github.com/pytest-dev/pytest/blob/fdba12e1708313f56e9cf713d260c029764ca2b7/src/_pytest/main.py) — src/_pytest/main.py contains Session.perform_collect and recursive item generation, providing the session-level entrance before src/_pytest/python.py handles Python-specific discovery.
- **Then read:**
  - [`src/_pytest/python.py`](https://github.com/pytest-dev/pytest/blob/fdba12e1708313f56e9cf713d260c029764ca2b7/src/_pytest/python.py)
  - [`testing/test_collection.py`](https://github.com/pytest-dev/pytest/blob/fdba12e1708313f56e9cf713d260c029764ca2b7/testing/test_collection.py)
- **Trace:** Follow Session.perform_collect through argument resolution and overlap normalization, filesystem hook proxies, collector creation, cached recursive genitems, and collection reports; continue into Python module import, reflective object discovery, function and parametrized-item generation, then correlate hook order, node IDs, duplicate and overlap semantics, import modes, symlinks, failures, and parametrized ordering in test_collection.py.

**Why this level:**

- **Language technique 4:** Reflection, import machinery, plugin-hook indirection, dynamic node construction, and advanced type modeling recur in essential collection behavior, satisfying the advanced-language-machinery anchor rather than the lower abstraction anchor.
- **Behavioral reasoning 4:** Tree state, hook propagation, cached collectors, duplicate policy, parametrization, and error reporting require advanced nonlocal reasoning across collection.
- **Design span 4:** Many modules and pervasive extension points contribute directly to the selected collection behavior.
- **Constraint burden 4:** Multiple strict compatibility, portability, determinism, extension, and error-reporting guarantees interact throughout the path.
- **Placement:** The four scores 4/4/4/4 sum to 16; their arithmetic mean is 4.00 and rounds half-up to Level 4. The published result is Level 4.

**License:** MIT ([evidence 1](https://github.com/pytest-dev/pytest/blob/fdba12e1708313f56e9cf713d260c029764ca2b7/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** pytest is released as production test infrastructure and supports a large plugin ecosystem across Python projects.

**Language evidence:** Collection, fixtures, assertion rewriting, hooks, configuration, execution, reports, and terminal output under src/_pytest are Python.

**Coding relevance:**

The README and familiar testing/import concepts provide sufficient context; the path primarily teaches transferable plugin architecture, tree traversal, reflection, import handling, deterministic ordering, compatibility, and error reporting.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Session, Collector, Item, Module, Function, hook, and report types make a dense dynamic collection mechanism explicit.
- **Architecture:** Session orchestration, plugin hooks, filesystem collectors, Python collectors, import handling, item factories, and reports have recognizable responsibilities.
- **Naming and idiom:** perform_collect, collect, genitems, Collector, Item, Module, Function, nodeid, hookproxy, and CollectReport preserve the collection model.
- **Tests:** testing/test_collection.py covers hook order, node identifiers, duplicate and overlapping paths, import modes, symlinks, failures, and parametrized ordering.
- **Documentation:** Pytest's collection, plugin, hook, import-mode, parametrization, and node documentation defines the extension contracts followed by this path.
- **Traceability:** A command-line path can be followed through argument normalization, hook proxies, cached collectors, recursive genitems, Python object discovery, item construction, and collection reports.
- **Maintainability:** Typed node boundaries, explicit hook contracts, stable identifiers, and self-hosting collection tests constrain changes to extensible discovery behavior.
- **Educational value:** The path demonstrates how reflection and plugins can remain deterministic when their tree, ordering, identity, and failure contracts are made explicit.

**Inspection record:** commit `fdba12e1708313f56e9cf713d260c029764ca2b7`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/_pytest/main.py`, `src/_pytest/python.py`, `testing/test_collection.py`, `LICENSE`. GitHub Linguist label: Python.

</details>

## Level 5 — Expert

### [apache/airflow](https://github.com/apache/airflow)

**Language 3 / Behavior 5 / Design 5 / Constraints 5 → Level 5**

A workflow-orchestration platform that defines directed task graphs and schedules, executes, retries, observes, and persists their runs.

**Why study it:** The scheduler-job path exposes how Airflow converts persisted due workflows into queued executor work while enforcing transactional claims, capacity, priority, fairness, and crash recovery.

**Short context:**

- A DAG contains task instances and dependencies; scheduler processes persist runs, use database row locks to claim work, enforce pools and concurrency limits, and submit queued workloads to executors.

**Prerequisites:**

- Strong working familiarity with Python functions and classes, collections, exceptions, decorators, context managers, generators and asynchronous basics, and focused tests, plus experience tracing state, resources, or asynchronous control flow across many production files.

**Concepts this path develops:**

- SQLAlchemy expression and ORM model DSL.
- Concurrent durable scheduler state.
- Atomicity and duplicate-scheduling prevention.

**What you can learn:**

- Use `airflow-core/src/airflow/jobs/scheduler_job_runner.py` to study the following transferable techniques and behaviors: SQLAlchemy query construction, row locking, DAG-run creation, task-instance state transitions, pool and concurrency limits, priority selection, atomic queueing, executor dispatch, event reconciliation, and orphan recovery.

**Learning path:**

- **Goal:** Understand how Airflow turns persisted due DAGs into queued executor work while preventing duplicate scheduling, enforcing capacity and priority, and recovering tasks from failed schedulers.
- **Start here:** [`airflow-core/src/airflow/jobs/scheduler_job_runner.py`](https://github.com/apache/airflow/blob/ff601cb5b75e77c1f28aaf014914f4e9d5cb0947/airflow-core/src/airflow/jobs/scheduler_job_runner.py) — airflow-core/src/airflow/jobs/scheduler_job_runner.py coordinates due-DAG processing, executable-task selection, atomic queueing, executor submission, event reconciliation, and orphan adoption.
- **Then read:**
  - [`airflow-core/src/airflow/models/dag.py`](https://github.com/apache/airflow/blob/ff601cb5b75e77c1f28aaf014914f4e9d5cb0947/airflow-core/src/airflow/models/dag.py)
  - [`airflow-core/src/airflow/models/pool.py`](https://github.com/apache/airflow/blob/ff601cb5b75e77c1f28aaf014914f4e9d5cb0947/airflow-core/src/airflow/models/pool.py)
  - [`airflow-core/src/airflow/models/taskinstance.py`](https://github.com/apache/airflow/blob/ff601cb5b75e77c1f28aaf014914f4e9d5cb0947/airflow-core/src/airflow/models/taskinstance.py)
  - [`airflow-core/src/airflow/executors/base_executor.py`](https://github.com/apache/airflow/blob/ff601cb5b75e77c1f28aaf014914f4e9d5cb0947/airflow-core/src/airflow/executors/base_executor.py)
  - [`airflow-core/tests/unit/models/test_dag.py`](https://github.com/apache/airflow/blob/ff601cb5b75e77c1f28aaf014914f4e9d5cb0947/airflow-core/tests/unit/models/test_dag.py)
  - [`airflow-core/tests/unit/jobs/test_scheduler_job.py`](https://github.com/apache/airflow/blob/ff601cb5b75e77c1f28aaf014914f4e9d5cb0947/airflow-core/tests/unit/jobs/test_scheduler_job.py)
- **Trace:** Follow DagModel.dags_needing_dagruns as it filters and row-locks due schedule- and asset-triggered DAGs, then SchedulerJobRunner as it creates DagRuns, schedules their task instances, selects executable work under pool, DAG, task, run, team, priority, and executor limits, atomically marks tasks queued, submits workloads to BaseExecutor, reconciles executor events, and adopts or resets orphaned tasks; correlate due-DAG, query-count, pool, priority, concurrency, critical-section, multi-executor, and orphan-recovery tests.

**Why this level:**

- **Language technique 3:** Substantial framework abstractions and type modeling recur, while the expert difficulty comes more from system behavior and architecture than Python language machinery itself.
- **Behavioral reasoning 5:** Distributed scheduling, state machines, database coordination, resource limits, recovery, and event reconciliation interact pervasively.
- **Design span 5:** The path coordinates several major subsystems, processes, persistence models, executors, and pervasive policy mechanisms at platform scale.
- **Constraint burden 5:** Several system-wide correctness, performance, compatibility, liveness, and recovery guarantees interact so that a local scheduling change can fail elsewhere in the path.
- **Placement:** The four scores 3/5/5/5 sum to 18; their arithmetic mean is 4.50 and rounds half-up to Level 5. The published result is Level 5.

**License:** Apache-2.0 ([evidence 1](https://github.com/apache/airflow/blob/ff601cb5b75e77c1f28aaf014914f4e9d5cb0947/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Apache Airflow is an actively released Apache project used to operate production data and automation workflows.

**Language evidence:** The scheduler, DAG and task models, executors, APIs, providers, serialization, jobs, and operational services are predominantly Python.

**Coding relevance:**

The repository explains this general workflow-orchestration model, and no specialist data domain is needed; the hard parts are transferable distributed scheduling, durable state, transactional coordination, fairness, recovery, performance, and extension architecture.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Critical sections, lock scope, concurrency maps, starvation filters, task states, and executor boundaries use precise names and explanatory comments.
- **Architecture:** DagModel, DagRun, TaskInstance, Pool, SchedulerJobRunner, BaseExecutor, persistence, and workload services contribute through explicit subsystem boundaries.
- **Naming and idiom:** dags_needing_dagruns, SchedulerJobRunner, executable task instances, critical section, queued state, executor events, and orphan adoption expose scheduling intent.
- **Tests:** The selected DAG and scheduler-job suites cover due-DAG queries, query bounds, pools, priority, concurrency, critical sections, multiple executors, and orphan recovery.
- **Documentation:** Airflow's scheduler, DAG-run, task-instance, pool, executor, and high-availability documentation explains the operational contracts exercised by the selected path.
- **Traceability:** A due persisted DAG can be followed through row locking, DagRun creation, task selection, atomic queued-state updates, BaseExecutor submission, event reconciliation, and failed-scheduler recovery.
- **Maintainability:** Transaction boundaries, typed state transitions, explicit resource policies, executor seams, query-count tests, and recovery tests constrain platform-scale scheduler changes.
- **Educational value:** The path provides an expert study of durable distributed scheduling where correctness, capacity, performance, and liveness must be reasoned about together.

**Inspection record:** commit `ff601cb5b75e77c1f28aaf014914f4e9d5cb0947`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `airflow-core/src/airflow/jobs/scheduler_job_runner.py`, `airflow-core/src/airflow/models/dag.py`, `airflow-core/src/airflow/models/pool.py`, `airflow-core/src/airflow/models/taskinstance.py`, `airflow-core/src/airflow/executors/base_executor.py`, `airflow-core/tests/unit/models/test_dag.py`, `airflow-core/tests/unit/jobs/test_scheduler_job.py`, `LICENSE`. GitHub Linguist label: Python.

</details>

### [home-assistant/core](https://github.com/home-assistant/core)

**Language 4 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

A home-automation runtime that coordinates devices, integrations, events, services, entity state, configuration, storage, and user automations.

**Why study it:** The configuration-entry lifecycle is a bounded view of Home Assistant's hardest transferable engineering: asynchronous state transitions, migration, retries, locking, persistence, unload cleanup, and shutdown cancellation.

**Short context:**

- A Home Assistant config entry is a persisted instance of a device or service integration that must migrate, load, retry when temporarily unavailable, unload, and survive concurrent reload or shutdown.

**Prerequisites:**

- Strong working familiarity with Python functions and classes, collections, exceptions, decorators, context managers, generators and asynchronous basics, and focused tests, plus experience tracing state, resources, or asynchronous control flow across many production files.

**Concepts this path develops:**

- PEP 695 generics and overloaded callable APIs.
- Asynchronous config-entry state machine.
- Race-free setup, reload, and unload.

**What you can learn:**

- Use `homeassistant/config_entries.py` to study the following transferable techniques and behaviors: Typed asynchronous state machines, per-entry locking, integration loading, schema migration, exponential retry, concurrent reload, runtime-data ownership, persistence notifications, unload callbacks, and shutdown cancellation.

**Learning path:**

- **Goal:** Understand how Home Assistant safely loads, migrates, retries, reloads, unloads, and persists a configuration entry across concurrent operations and runtime shutdown.
- **Start here:** [`homeassistant/config_entries.py`](https://github.com/home-assistant/core/blob/471f2c28e285c268cc4ca67ad80ff4044b365d70/homeassistant/config_entries.py) — config_entries.py owns the persisted entry model and its setup, migration, retry, reload, unload, and state-transition methods, so it contains the selected lifecycle rather than the platform-wide core runtime.
- **Then read:**
  - [`homeassistant/core.py`](https://github.com/home-assistant/core/blob/471f2c28e285c268cc4ca67ad80ff4044b365d70/homeassistant/core.py)
  - [`homeassistant/loader.py`](https://github.com/home-assistant/core/blob/471f2c28e285c268cc4ca67ad80ff4044b365d70/homeassistant/loader.py)
  - [`homeassistant/setup.py`](https://github.com/home-assistant/core/blob/471f2c28e285c268cc4ca67ad80ff4044b365d70/homeassistant/setup.py)
  - [`tests/test_core.py`](https://github.com/home-assistant/core/blob/471f2c28e285c268cc4ca67ad80ff4044b365d70/tests/test_core.py)
  - [`tests/test_config_entries.py`](https://github.com/home-assistant/core/blob/471f2c28e285c268cc4ca67ad80ff4044b365d70/tests/test_config_entries.py)
- **Trace:** Follow ConfigEntries.async_setup as it finds the entry and acquires its setup lock, then ConfigEntry.async_setup through integration loading, config-flow import, version migration, component setup, typed state transitions, authentication and fatal failures, ConfigEntryNotReady exponential retry through HomeAssistant jobs and events, and successful load; continue through concurrent reload, unload callbacks, runtime-data cleanup, persistence notifications, and shutdown cancellation, correlating setup-race, backoff, invalid-state, lock, concurrent-reload, event-loop thread, unload, migration, storage, and shutdown tests.

**Why this level:**

- **Language technique 4:** Advanced generic typing, overloads, immutable runtime models, context state, and callable introspection recur across entry and job lifecycle behavior.
- **Behavioral reasoning 5:** Concurrency, durable state, retries, event scheduling, recovery, resource lifetimes, and shutdown interact pervasively and demand expert nonlocal reasoning.
- **Design span 4:** Many modules, extension points, lifecycle services, and cross-cutting policies contribute directly, satisfying the broad-architecture anchor.
- **Constraint burden 5:** Several system-wide correctness, compatibility, persistence, concurrency, and reliability guarantees interact so a local lifecycle change can corrupt state or break integrations elsewhere.
- **Placement:** The four scores 4/5/4/5 sum to 18; their arithmetic mean is 4.50 and rounds half-up to Level 5. The published result is Level 5.

**License:** Apache-2.0 ([evidence 1](https://github.com/home-assistant/core/blob/471f2c28e285c268cc4ca67ad80ff4044b365d70/LICENSE.md))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Home Assistant Core is continuously released as the production engine behind deployed home-automation installations.

**Language evidence:** The automation runtime, state machine, services, event bus, configuration entries, integrations, and coordinators are implemented in Python.

**Coding relevance:**

This generic plugin-lifecycle model is short and documented, and the selected path requires no device-protocol expertise; its difficulty is transferable async state-machine, locking, retry, migration, persistence, cleanup, and compatibility engineering.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Config-entry states, locks, immutable mappings, retry handles, failure reasons, runtime data, and unload callbacks are explicit and strongly typed throughout the lifecycle.
- **Architecture:** The entry and manager coordinate with the integration loader, component setup, core jobs and events, dispatcher, and storage through recognizable boundaries.
- **Naming and idiom:** ConfigEntry, ConfigEntries, async_setup, async_migrate, ConfigEntryNotReady, runtime_data, unload, reload, and state names expose lifecycle intent.
- **Tests:** Focused core and config-entry tests cover setup races, locks, invalid transitions, migration, exponential backoff, authentication failures, concurrent reload, unload, persistence, thread ownership, and shutdown.
- **Documentation:** Developer architecture and integration guidance explain configuration entries, setup, migration, availability failures, unloading, and concurrency rules needed for the path.
- **Traceability:** A persisted entry can be followed from manager lookup and locking through loading, migration, component setup, retries and state events into successful load, reload, unload, storage updates, and shutdown cancellation.
- **Maintainability:** Typed states, per-entry synchronization, loader and setup boundaries, explicit retry ownership, and focused lifecycle tests constrain changes in this high-concurrency path.
- **Educational value:** The selected slice teaches expert asynchronous plugin lifecycle design without requiring knowledge of any particular device protocol or the entire Home Assistant platform.

**Inspection record:** commit `471f2c28e285c268cc4ca67ad80ff4044b365d70`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `homeassistant/config_entries.py`, `homeassistant/core.py`, `homeassistant/loader.py`, `homeassistant/setup.py`, `tests/test_core.py`, `tests/test_config_entries.py`, `LICENSE.md`. GitHub Linguist label: Python.

</details>

_Generated from `catalog/python.json`; do not edit by hand._

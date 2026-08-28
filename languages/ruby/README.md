# Ruby

10 qualified repositories. Scores assume the learner described in [the SDC rubric](../../docs/sdc.md).

[← All languages](../README.md)

## SDC 1

### [ruby/pathname](https://github.com/ruby/pathname)

**S1 / D2 / C1 → SDC 1**

An immutable object-oriented representation of filesystem paths from Ruby's standard library.

**Real-world evidence:** The repository publishes Ruby's pathname default gem and implements the Pathname API used throughout Ruby tooling and applications.

**Language evidence:** The path value object and nearly all path and filesystem behavior are Ruby under lib/, with a small C extension for selected primitives.

**Why study it:** It wraps familiar filesystem operations in an immutable value object, making delegation, path algorithms, platform rules, and API consistency easy to trace.

**What you can learn:**

- Immutable value objects, path normalization, traversal, filesystem delegation, enumerators, platform path rules, and Ruby C-extension boundaries.

**Prerequisites:**

- Ruby objects and modules, strings, enumerators, file and directory APIs, regular expressions, and basic C reading for the optional extension.

**Start here:** [`lib/pathname.rb`](https://github.com/ruby/pathname/blob/f0217bbd486b2f7d5c7de1ff3951c7422d42c761/lib/pathname.rb) — The main file introduces the value-object invariants, path transformations, traversal, and delegated filesystem operations in API order.

**Why this level:**

- **S1:** 625 meaningful implementation LOC measured with tokei 14.0.0. Count covers production Ruby and the small native extension, excluding tests, documentation, and build metadata.
- **D2:** Path corner cases and a narrow C boundary add modest depth while most methods remain short and conventional.
- **C1:** One class family models paths and delegates to Ruby's existing file and directory facilities.
- **Placement:** S1/D2/C1 averages to 1.33, placing Pathname at SDC 1.

**Quality-gate evidence:**

- **Source quality:** Transformations preserve immutable string state, edge cases are guarded close to their algorithms, and delegated calls remain visible.
- **Architecture:** A single value object layers lexical path operations and filesystem calls over Ruby core APIs, with selected helpers in C.
- **Naming and idiom:** ascend, descend, cleanpath, relative_path_from, children, entries, and each_line follow Ruby collection and filesystem vocabulary.
- **Tests:** The suite exercises Unix and Windows forms, normalization, relative paths, traversal, filesystem delegation, encoding, and exceptions.
- **Documentation:** The README and extensive method comments pair examples with the path and filesystem contracts.
- **Traceability:** A relative path calculation can be followed through cleanpath, component comparison, reconstruction, and targeted assertions.
- **Maintainability:** The narrow model, stable core dependencies, and exhaustive edge-case tests constrain changes despite a broad method list.
- **Educational value:** It is a readable lesson in turning primitive strings into a coherent domain type.

**Inspection record:** commit `f0217bbd486b2f7d5c7de1ff3951c7422d42c761`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `pathname.gemspec`, `lib/pathname.rb`, `ext/pathname/pathname.c`, `test/pathname/test_pathname.rb`, `COPYING`. GitHub Linguist label: Ruby. LOC exclusions: test/.

**License:** [Ruby OR BSD-2-Clause](https://github.com/ruby/pathname/blob/f0217bbd486b2f7d5c7de1ff3951c7422d42c761/COPYING)

### [ruby/tempfile](https://github.com/ruby/tempfile)

**S1 / D2 / C1 → SDC 1**

Ruby's standard temporary-file library, providing secure creation plus explicit and automatic cleanup lifecycles.

**Real-world evidence:** The repository publishes the tempfile default gem used by Ruby applications and the Ruby standard library.

**Language evidence:** Temporary-file creation, permissions, cleanup, delegation, and lifecycle behavior are implemented in Ruby under lib/.

**Why study it:** A learner can read the entire implementation while seeing how a tiny API handles ownership, cleanup, garbage collection, permissions, and exceptional paths.

**What you can learn:**

- Delegation, resource ownership, temporary-file security, explicit versus automatic cleanup, finalizers, exceptions, and standard-library packaging.

**Prerequisites:**

- Ruby classes and modules, blocks, file I/O, exceptions, garbage collection basics, and tests.

**Start here:** [`lib/tempfile.rb`](https://github.com/ruby/tempfile/blob/344da5e29e3215691209223249ebd64e66dff6b8/lib/tempfile.rb) — The one production file moves from secure creation helpers into Tempfile's lifecycle, delegation, close, unlink, and block APIs.

**Why this level:**

- **S1:** 201 meaningful implementation LOC measured with tokei 14.0.0. Count covers the complete production library and excludes tests, documentation, and packaging metadata.
- **D2:** File ownership and cleanup require care, but the implementation uses direct Ruby objects and a small public surface.
- **C1:** One cohesive component owns creation, delegation, closing, and deletion without services or extension subsystems.
- **Placement:** S1/D2/C1 averages to 1.33, making Tempfile a compact SDC 1 study.

**Quality-gate evidence:**

- **Source quality:** The code makes ownership and cleanup state explicit and keeps security-sensitive creation in small named helpers.
- **Architecture:** A delegating Tempfile object wraps a securely created File and centralizes cleanup in an explicit lifecycle.
- **Naming and idiom:** create, open, close, unlink, anonymous, Remover, and size express Ruby's file and block idioms directly.
- **Tests:** The suite covers creation, modes, permissions, encodings, paths, unlinking, finalization, anonymous files, blocks, and failure cleanup.
- **Documentation:** API comments and the README explain each lifecycle choice, including when automatic deletion is appropriate.
- **Traceability:** A block-based temporary file can be followed from creation through yielding, ensure cleanup, and a focused test.
- **Maintainability:** One implementation file, standard-library primitives, and lifecycle-focused tests keep behavioral changes reviewable.
- **Educational value:** It shows that even a tiny wrapper can teach real resource-safety design without hiding the mechanics.

**Inspection record:** commit `344da5e29e3215691209223249ebd64e66dff6b8`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `tempfile.gemspec`, `lib/tempfile.rb`, `test/test_tempfile.rb`, `COPYING`. GitHub Linguist label: Ruby. LOC exclusions: test/.

**License:** [Ruby OR BSD-2-Clause](https://github.com/ruby/tempfile/blob/344da5e29e3215691209223249ebd64e66dff6b8/COPYING)

## SDC 2

### [redis/redis-rb](https://github.com/redis/redis-rb)

**S2 / D2 / C2 → SDC 2**

The official Ruby client for Redis, exposing Redis commands through an idiomatic synchronous API.

**Real-world evidence:** The repository releases the redis gem for application access to Redis servers and maintains protocol and server compatibility.

**Language evidence:** The public client, command families, pipelining, pub/sub, Sentinel integration, error mapping, and compatibility behavior are Ruby under lib/.

**Why study it:** It connects an approachable command API to connection policy, error translation, pipelining, pub/sub, Sentinel discovery, protocol fallback, and thread safety.

**What you can learn:**

- Client facades, command modules, protocol negotiation, pipelining, pub/sub, error translation, synchronization, failover configuration, and compatibility layers.

**Prerequisites:**

- Ruby modules and delegation, blocks, exceptions, threads and monitors, TCP clients, and Redis command concepts.

**Start here:** [`lib/redis.rb`](https://github.com/redis/redis-rb/blob/55a1cd8d120dd80d47a8db634ec90429dead8adc/lib/redis.rb) — The main Redis class shows construction, synchronization, client delegation, pipelining, lifecycle, protocol fallback, and public compatibility behavior.

**Why this level:**

- **S2:** 6,395 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production Ruby under lib, excluding tests, benchmarks, documentation, and packaging metadata.
- **D2:** Networking policies matter, but much of the code is explicit command shaping and delegation to redis-client.
- **C2:** Several cohesive client modes share one in-process API and a common transport abstraction.
- **Placement:** S2/D2/C2 is a balanced SDC 2 project.

**Quality-gate evidence:**

- **Source quality:** Connection state, retry boundaries, synchronization, command transformation, and error classes are explicit and locally documented.
- **Architecture:** A public Redis facade composes command modules and delegates transport to redis-client, with specialized pub/sub, cluster, and Sentinel paths.
- **Naming and idiom:** pipelined, multi, subscribe, synchronize, reconnect_attempts, CommandError, and Sentinel mirror the Redis and Ruby domains.
- **Tests:** The suite covers command families, clients, pipelines, transactions, pub/sub, distributed and Sentinel behavior, errors, URLs, and protocol variants.
- **Documentation:** The README documents connection forms, command use, pooling, pipelining, pub/sub, Sentinel, clustering, timeouts, and protocol support.
- **Traceability:** A command can be followed from the public module through argument normalization, synchronized client dispatch, response transformation, and a focused test.
- **Maintainability:** Command families are separated from transport and compatibility code, and integration tests protect server-facing contracts.
- **Educational value:** It is a manageable production client that exposes protocol concerns without requiring a learner to implement the wire parser first.

**Inspection record:** commit `55a1cd8d120dd80d47a8db634ec90429dead8adc`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `redis.gemspec`, `lib/redis.rb`, `lib/redis/client.rb`, `test/redis/client_test.rb`, `LICENSE`. GitHub Linguist label: Ruby. LOC exclusions: test/, bench/.

**License:** [MIT](https://github.com/redis/redis-rb/blob/55a1cd8d120dd80d47a8db634ec90429dead8adc/LICENSE)

### [ruby/net-http](https://github.com/ruby/net-http)

**S2 / D3 / C2 → SDC 2**

Ruby's standard HTTP client library for constructing requests and managing HTTP and HTTPS sessions.

**Real-world evidence:** The repository publishes the net-http default gem that backs HTTP communication across Ruby programs and libraries.

**Language evidence:** HTTP requests, responses, headers, connection reuse, proxy handling, TLS setup, streaming, decoding, and retry behavior are Ruby under lib/.

**Why study it:** A familiar request API opens into protocol framing, persistent connections, TLS, proxies, streaming bodies, compression, retries, and careful resource cleanup.

**What you can learn:**

- HTTP request and response framing, persistent connections, TLS configuration, proxies, body streaming, compression, retries, timeouts, and resource cleanup.

**Prerequisites:**

- Ruby classes and inheritance, sockets, streams, exceptions, URI structure, HTTP semantics, and basic TLS concepts.

**Start here:** [`lib/net/http.rb`](https://github.com/ruby/net-http/blob/23e859e92e10e43cad520fcacac3fd43640dba7b/lib/net/http.rb) — Net::HTTP contains the session lifecycle and request path that connect public calls to sockets, TLS, responses, retries, and cleanup.

**Why this level:**

- **S2:** 2,283 meaningful implementation LOC measured with tokei 14.0.0. Count covers production Ruby under lib, excluding tests, signatures, documentation, and packaging metadata.
- **D3:** Correct protocol and socket behavior recur, but the implementation remains compact and follows recognizable request-session phases.
- **C2:** A small family of cooperating classes implements one network protocol client within a process.
- **Placement:** S2/D3/C2 averages to 2.33, placing Net::HTTP at SDC 2.

**Quality-gate evidence:**

- **Source quality:** Session state, retry conditions, socket ownership, header rules, body modes, and protocol errors are made explicit near the affected flow.
- **Architecture:** Request subclasses and header logic feed a session object that owns transport, TLS, response parsing, streaming, and persistence.
- **Naming and idiom:** start, request, transport_request, begin_transport, end_transport, read_body, and keep_alive expose the protocol lifecycle.
- **Tests:** The suite covers methods, headers, bodies, chunking, compression, proxies, TLS, timeouts, retries, persistence, malformed responses, and regressions.
- **Documentation:** Extensive API documentation provides request patterns, session use, streaming, TLS, proxies, and timeout behavior.
- **Traceability:** A GET can be followed from request construction through transport setup, header write, response read, body decode, persistence decision, and tests.
- **Maintainability:** Protocol roles are split into focused classes while a broad compatibility suite guards edge cases across Ruby and servers.
- **Educational value:** It is small enough to map but deep enough to teach why production HTTP clients are more than opening a socket.

**Inspection record:** commit `23e859e92e10e43cad520fcacac3fd43640dba7b`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `net-http.gemspec`, `lib/net/http.rb`, `lib/net/http/generic_request.rb`, `test/net/http/test_http.rb`, `COPYING`. GitHub Linguist label: Ruby. LOC exclusions: test/, test_sig/.

**License:** [Ruby OR BSD-2-Clause](https://github.com/ruby/net-http/blob/23e859e92e10e43cad520fcacac3fd43640dba7b/COPYING)

## SDC 3

### [jekyll/jekyll](https://github.com/jekyll/jekyll)

**S2 / D3 / C3 → SDC 3**

A static-site generator that transforms Markdown, Liquid templates, data, assets, and configuration into a deployable website.

**Real-world evidence:** The repository publishes the Jekyll gem and command-line tool used for blogs, documentation, and GitHub Pages workflows.

**Language evidence:** Site discovery, collections, front matter, rendering, plugins, incremental regeneration, destination writing, and CLI behavior are Ruby under lib/.

**Why study it:** Its build pipeline is tangible: discover content, classify it, run generators, render Liquid and markup, track dependencies, write output, and clean stale files.

**What you can learn:**

- Build pipelines, content models, front matter, template and markup conversion, plugin registries, dependency tracking, incremental builds, configuration, and filesystem safety.

**Prerequisites:**

- Ruby objects and modules, files and paths, YAML, Markdown and templating concepts, plugins, dependency graphs, and command-line applications.

**Start here:** [`lib/jekyll/site.rb`](https://github.com/jekyll/jekyll/blob/74d751339d3e534aa51d5d7b0640e9bd743509e4/lib/jekyll/site.rb) — Site is the orchestration center: reset, read, generate, render, cleanup, and write reveal the complete build before deeper components.

**Why this level:**

- **S2:** 8,088 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production Ruby under lib, excluding tests, acceptance fixtures, documentation, examples, and packaging metadata.
- **D3:** Parsing and rendering are delegated to libraries, while Jekyll's main challenge is coordinating mutable content and build phases safely.
- **C3:** Many cohesive subsystems participate in a build and expose extension points, though execution remains a local application pipeline.
- **Placement:** S2/D3/C3 averages to 2.67, which rounds to SDC 3.

**Quality-gate evidence:**

- **Source quality:** Build phases are short named methods, source and destination invariants are guarded, and rendering errors preserve document context.
- **Architecture:** Site orchestrates readers, collections, generators, converters, renderers, dependency tracking, cleaners, and writers through registries and hooks.
- **Naming and idiom:** Site, Document, Collection, Generator, Converter, Renderer, Regenerator, payload, frontmatter, and permalink reflect the static-site domain.
- **Tests:** Unit and acceptance suites cover configuration, content discovery, rendering, plugins, themes, incremental builds, drafts, permalinks, security boundaries, and CLI behavior.
- **Documentation:** The project maintains user guides, configuration references, plugin APIs, deployment guidance, tutorials, and contributor documentation.
- **Traceability:** A Markdown post can be followed from Reader into a Collection, through Renderer and converters, dependency recording, destination writing, and site tests.
- **Maintainability:** Pipeline stages and extension contracts are separated, while fixtures protect the large matrix of content and configuration behavior.
- **Educational value:** It provides a visible end-to-end transformation system whose artifacts make architecture easy to test and understand.

**Inspection record:** commit `74d751339d3e534aa51d5d7b0640e9bd743509e4`, reviewed 2026-08-28 by Codex. Files sampled: `README.markdown`, `jekyll.gemspec`, `lib/jekyll/site.rb`, `lib/jekyll/renderer.rb`, `test/test_site.rb`, `LICENSE`. GitHub Linguist label: Ruby. LOC exclusions: test/, features/, docs/.

**License:** [MIT](https://github.com/jekyll/jekyll/blob/74d751339d3e534aa51d5d7b0640e9bd743509e4/LICENSE)

### [sidekiq/sidekiq](https://github.com/sidekiq/sidekiq)

**S2 / D4 / C3 → SDC 3**

A multithreaded background-job processor for Ruby applications backed by Redis.

**Real-world evidence:** The project publishes the Sidekiq gem and executable used to run durable asynchronous work for Ruby applications.

**Language evidence:** Job fetching, execution, middleware, retries, scheduling, capsules, Redis coordination, process lifecycle, and the monitoring UI are Ruby under lib/ and web/.

**Why study it:** It turns a simple perform method into queue polling, thread lifecycle, middleware, retries, shutdown, scheduling, observability, and Redis coordination.

**What you can learn:**

- Worker pools, thread lifecycle, Redis queues, reliable fetching, retries and dead jobs, middleware chains, scheduling, signals, shutdown, and operational telemetry.

**Prerequisites:**

- Ruby threads and synchronization, exceptions, process signals, Redis data structures, background-job semantics, Rack, and testing.

**Start here:** [`lib/sidekiq/processor.rb`](https://github.com/sidekiq/sidekiq/blob/1bb4aa06e5aa178a114a5e855f9f3d5c24f6c61b/lib/sidekiq/processor.rb) — Processor follows one fetched job through decoding, middleware, execution, acknowledgment, retry handling, and shutdown interaction.

**Why this level:**

- **S2:** 7,135 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production code under lib, excluding tests, examples, the sample application, documentation, and packaging metadata.
- **D4:** Concurrency and failure semantics are central, and correctness depends on coordinating process, Redis, middleware, and user-code boundaries.
- **C3:** Several runtime subsystems cooperate across Redis and application boundaries but remain one deployable worker service.
- **Placement:** S2/D4/C3 averages exactly to SDC 3.

**Quality-gate evidence:**

- **Source quality:** Job ownership, acknowledgment, retry, termination, and thread state are named explicitly, with narrow rescue and ensure boundaries.
- **Architecture:** Capsules configure queues and concurrency; managers own processors; fetchers reserve jobs; middleware surrounds execution; retry and scheduling subsystems handle failure and time.
- **Naming and idiom:** Processor, Manager, Capsule, fetch, acknowledge, requeue, dead, quiet, and terminate match worker operations.
- **Tests:** The suite covers execution, retries, crashes, shutdown, scheduling, queue weighting, middleware, Redis failures, metrics, CLI behavior, and the web UI.
- **Documentation:** The README and wiki document job semantics, deployment, reliability, configuration, middleware, errors, testing, and operational practices.
- **Traceability:** A job can be followed from Redis reservation into Processor, server middleware, user code, acknowledgment or retry, and processor tests.
- **Maintainability:** Runtime responsibilities are separated behind small interfaces and deterministic tests exercise exceptional lifecycle transitions.
- **Educational value:** It is a strong bridge from ordinary application code to concurrency and distributed work semantics.

**Inspection record:** commit `1bb4aa06e5aa178a114a5e855f9f3d5c24f6c61b`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `sidekiq.gemspec`, `lib/sidekiq/processor.rb`, `lib/sidekiq/manager.rb`, `test/processor_test.rb`, `LICENSE.txt`. GitHub Linguist label: Ruby. LOC exclusions: test/, examples/, myapp/.

**License:** [LGPL-3.0-only](https://github.com/sidekiq/sidekiq/blob/1bb4aa06e5aa178a114a5e855f9f3d5c24f6c61b/LICENSE.txt)

## SDC 4

### [rails/rails](https://github.com/rails/rails)

**S4 / D4 / C4 → SDC 4**

A full-stack web application framework spanning HTTP, MVC, persistence, jobs, mail, WebSockets, storage, and application tooling.

**Real-world evidence:** The repository releases the Rails framework gems used to build and operate production web applications.

**Language evidence:** The MVC framework, ORM, routing, jobs, mail, WebSockets, storage, rendering, support libraries, generators, and application lifecycle are Ruby across the framework components.

**Why study it:** It is a mature framework monorepo where conventions emerge from explicit component contracts, lifecycle hooks, query construction, routing, rendering, background work, and generators.

**What you can learn:**

- Framework boot and configuration, MVC request flow, routing, ORM and query composition, callbacks, jobs, mail, WebSockets, storage, code generation, and compatibility design.

**Prerequisites:**

- Advanced Ruby and metaprogramming, HTTP and MVC, relational databases and SQL, asynchronous work, caching, concurrency, security, and large-repository navigation.

**Start here:** [`railties/lib/rails/application.rb`](https://github.com/rails/rails/blob/0ca2c2c4cfbe7f0a709bca0589d2d74c1853ef27/railties/lib/rails/application.rb) — Application explains how configuration, engines, routes, initializers, reloading, tasks, generators, and request handling become one Rails process.

**Why this level:**

- **S4:** 118,826 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production framework components, excluding tests, guides, task automation, templates, examples, generated files, and vendored code.
- **D4:** Advanced Ruby mechanisms and framework invariants recur across persistence, requests, lifecycle, and extension code.
- **C4:** Many framework subsystems cooperate through public contracts, but they form one application platform rather than a distributed product deployment.
- **Placement:** S4/D4/C4 makes Rails a balanced SDC 4 system.

**Quality-gate evidence:**

- **Source quality:** Public contracts are documented close to implementation, lifecycle phases use named hooks, and framework invariants have focused error types and tests.
- **Architecture:** Railties composes independent framework gems for support, models, records, controllers, views, jobs, mail, channels, text, storage, and application boot.
- **Naming and idiom:** Application, Engine, Railtie, Relation, Controller, Job, Mailer, Channel, callback, scope, and concern define the framework vocabulary.
- **Tests:** Each component has extensive unit and integration suites covering adapters, requests, rendering, persistence, generators, security, reloading, concurrency, and regressions.
- **Documentation:** API documentation and maintained guides cover framework concepts, components, security, deployment, extension, testing, and contribution.
- **Traceability:** A database-backed request can be traced from route recognition into a controller, model Relation and adapter, rendering, response middleware, and component integration tests.
- **Maintainability:** Gem boundaries, shared support primitives, deprecation machinery, changelogs, and exhaustive compatibility tests let a large framework evolve deliberately.
- **Educational value:** It is a premier advanced study of how a language's idioms can scale into a coherent application platform.

**Inspection record:** commit `0ca2c2c4cfbe7f0a709bca0589d2d74c1853ef27`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Gemfile`, `railties/lib/rails/application.rb`, `activerecord/lib/active_record/relation.rb`, `railties/test/application/configuration_test.rb`, `MIT-LICENSE`. GitHub Linguist label: Ruby. LOC exclusions: **/test/, guides/, tasks/, templates/.

**License:** [MIT](https://github.com/rails/rails/blob/0ca2c2c4cfbe7f0a709bca0589d2d74c1853ef27/MIT-LICENSE)

### [rubocop/rubocop](https://github.com/rubocop/rubocop)

**S4 / D3 / C4 → SDC 4**

A configurable Ruby static analyzer and formatter built around independently selectable cops.

**Real-world evidence:** The repository publishes the RuboCop gem and executable used to lint, format, and enforce Ruby project conventions.

**Language evidence:** Configuration, target discovery, AST inspection, cop dispatch, offense reporting, autocorrection, caching, formatters, and CLI orchestration are Ruby under lib/ and exe/.

**Why study it:** It demonstrates how a large rule engine turns source into AST events, selects and coordinates checks, merges corrections, caches results, preserves output order, and supports extensions.

**What you can learn:**

- AST event dispatch, rule registries, configuration inheritance, diagnostics, source rewriting, conflict resolution, parallel processing, caching, formatters, and plugin APIs.

**Prerequisites:**

- Ruby metaprogramming, ASTs and source ranges, visitors or event dispatch, configuration systems, parallel processes, testing, and static-analysis concepts.

**Start here:** [`lib/rubocop/runner.rb`](https://github.com/rubocop/rubocop/blob/8b85bafb041debc1f3a955663a99fa384a9d24f6/lib/rubocop/runner.rb) — Runner connects file discovery, configuration, parallel or serial inspection, correction iterations, caching, reporting, and exit status.

**Why this level:**

- **S4:** 60,814 meaningful implementation LOC measured with tokei 14.0.0. Count covers first-party production Ruby under lib and exe, excluding tests, task automation, documentation, generated configuration, and packaging metadata.
- **D3:** Static analysis and rewriting require specialized concepts, but RuboCop delegates parsing and organizes behavior into regular Ruby objects.
- **C4:** Many extensible subsystems and rule families interact across configuration, inspection, correction, output, and compatibility boundaries.
- **Placement:** S4/D3/C4 averages to 3.67, which rounds to SDC 4.

**Quality-gate evidence:**

- **Source quality:** Inspection phases, correction loops, ordered parallel reporting, configuration decisions, and extension hooks use explicit state and named helpers.
- **Architecture:** Runner orchestrates targets and output; Team mobilizes cops and forces; Commissioner dispatches AST events; correctors merge edits; registries and plugins supply extensions.
- **Naming and idiom:** Cop, offense, correction, Commissioner, Team, Force, Registry, department, and target finder form a consistent analysis vocabulary.
- **Tests:** A large RSpec suite covers individual cops, corrections, configuration, plugins, caching, parallelism, formatters, CLI behavior, regressions, and platform cases.
- **Documentation:** Versioned documentation covers every cop, configuration and suppression, autocorrection safety, extensions, plugins, formatters, and development.
- **Traceability:** A source offense can be followed from file discovery through processed AST, Team dispatch, cop callback, correction merge, formatter output, and focused specs.
- **Maintainability:** Rule isolation, shared analysis forces, generated documentation, explicit compatibility policy, and extensive examples keep a broad analyzer evolvable.
- **Educational value:** It is a substantial but navigable study of a plugin-oriented static-analysis platform written in the language it analyzes.

**Inspection record:** commit `8b85bafb041debc1f3a955663a99fa384a9d24f6`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `rubocop.gemspec`, `lib/rubocop/runner.rb`, `lib/rubocop/cop/team.rb`, `spec/rubocop/runner_spec.rb`, `LICENSE.txt`. GitHub Linguist label: Ruby. LOC exclusions: spec/, tasks/.

**License:** [MIT](https://github.com/rubocop/rubocop/blob/8b85bafb041debc1f3a955663a99fa384a9d24f6/LICENSE.txt)

## SDC 5

### [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot)

**S5 / D4 / C5 → SDC 5**

A multichannel customer-support platform combining shared inboxes, live chat, messaging integrations, automation, reporting, and agent collaboration.

**Real-world evidence:** The repository is the deployable open-source Chatwoot product used to run customer-support operations across web and messaging channels.

**Language evidence:** The customer-conversation domain, channel APIs, automation, assignments, inboxes, reporting, jobs, integrations, and core application services are primarily Ruby under app/ and lib/.

**Why study it:** It provides a second large-product lens: a conversation-centered Rails domain integrated with external channels, event delivery, automation, queues, permissions, reporting, and a Vue client.

**What you can learn:**

- SaaS domain modeling, multitenancy, channel adapters, webhook and event processing, assignments, automation, background jobs, notifications, reporting, real-time UI, and integration boundaries.

**Prerequisites:**

- Advanced Ruby and Rails, SQL and multitenancy, JavaScript and Vue, queues, webhooks, OAuth and external APIs, caching, security, operations, and large-system navigation.

**Start here:** [`app/models/conversation.rb`](https://github.com/chatwoot/chatwoot/blob/7f029b65eb787a1b68167338a63151beedd33a25/app/models/conversation.rb) — Conversation is the domain hub for inboxes, contacts, assignees, teams, messages, state, unread counts, bots, notifications, and lifecycle events.

**Why this level:**

- **S5:** 240,881 meaningful implementation LOC measured with tokei 14.0.0. Count covers the MIT-licensed first-party core under app and lib, excluding the separately licensed enterprise directory, tests, fixtures, translations, generated or vendored content, large data files, documentation, and dependency trees.
- **D4:** Central flows must remain correct across accounts, channel capabilities, callbacks, external providers, jobs, bots, and human-agent state.
- **C5:** The product spans many runtime components and third-party systems while coordinating shared conversation state across agents and customers.
- **Placement:** S5/D4/C5 has two dimensions at 5 and therefore requires SDC 5.

**Quality-gate evidence:**

- **Source quality:** Domain state, callbacks, services, authorization, events, and provider boundaries are named explicitly, with high-traffic optimizations documented near their invariants.
- **Architecture:** Account-scoped Rails models and APIs compose service objects, jobs, events, channel adapters, integrations, Action Cable, storage, and a modular Vue application.
- **Naming and idiom:** Conversation, Inbox, ContactInbox, Message, Assignee, AgentBot, Campaign, SLA, channel, and webhook form a consistent support-domain model.
- **Tests:** Server and client suites cover models, requests, services, jobs, policies, channels, integrations, automation, reporting, UI state, and regressions.
- **Documentation:** Deployment, developer, API, integration, self-hosting, and contributor documentation accompany inline descriptions of domain and operational behavior.
- **Traceability:** An incoming channel message can be followed through its adapter, contact and conversation resolution, message persistence, events and jobs, notifications, API serialization, client state, and specs.
- **Maintainability:** Account scoping, service boundaries, channel abstractions, event dispatch, feature flags, background jobs, and broad tests contain a fast-growing integration surface.
- **Educational value:** It is an expert study in keeping a large integration-heavy product centered on a legible domain model.

**Inspection record:** commit `7f029b65eb787a1b68167338a63151beedd33a25`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Gemfile`, `app/controllers/api/v1/accounts/conversations_controller.rb`, `app/models/conversation.rb`, `spec/models/conversation_spec.rb`, `LICENSE`. GitHub Linguist label: Ruby. LOC exclusions: enterprise/, **/test/, **/spec/, fixtures/, locales/, vendor/, node_modules/, generated/, *.json.

**License:** [MIT](https://github.com/chatwoot/chatwoot/blob/7f029b65eb787a1b68167338a63151beedd33a25/LICENSE)

### [discourse/discourse](https://github.com/discourse/discourse)

**S5 / D4 / C5 → SDC 5**

A complete community discussion platform with forums, trust and moderation, search, notifications, real-time updates, administration, and plugins.

**Real-world evidence:** The repository is the deployable Discourse product used to operate public and private online communities.

**Language evidence:** Forum domain models, HTTP APIs, moderation, trust, notifications, search, jobs, plugins, administration, and server-side rendering are principally Ruby across app/, lib/, config/, and bundled plugins.

**Why study it:** It shows how a mature Rails product encodes a rich social domain while coordinating policy, moderation, trust, plugins, background work, search, notifications, and a large client.

**What you can learn:**

- Large Rails domain modeling, authorization and moderation, trust systems, background jobs, search, notifications, real-time events, caching, plugins, migrations, operations, and product evolution.

**Prerequisites:**

- Advanced Ruby and Rails, SQL and data modeling, JavaScript application architecture, queues, caching, search, security and abuse prevention, operations, and monorepo navigation.

**Start here:** [`app/models/post.rb`](https://github.com/discourse/discourse/blob/58f18d48d66d5ab9bfbfb35cde4c0ef932aea5b9/app/models/post.rb) — Post sits at the product's center and exposes relationships to topics, users, revisions, moderation, notifications, search, uploads, and lifecycle callbacks.

**Why this level:**

- **S5:** 563,529 meaningful implementation LOC measured with tokei 14.0.0. Count covers meaningful first-party server, client, configuration, and bundled-plugin implementation, excluding tests, fixtures, translations, generated or vendored content, large data files, documentation, and dependency trees.
- **D4:** Correctness depends on interacting product, security, data, and asynchronous invariants throughout the central domain.
- **C5:** The deployed product spans many processes, stores, protocols, extension points, and operational modes with substantial cross-feature coupling.
- **Placement:** S5/D4/C5 has two dimensions at 5 and therefore requires SDC 5.

**Quality-gate evidence:**

- **Source quality:** Core domain flows use explicit services, guardians, policies, transactions, jobs, and events, with comments concentrated around product invariants and compatibility.
- **Architecture:** Rails models and controllers compose service objects, Guardian authorization, Sidekiq jobs, serializers, search, caching, MessageBus events, an Ember client, and a first-class plugin API.
- **Naming and idiom:** Topic, Post, Guardian, trust_level, flag, reviewable, badge, notification, cooked content, and plugin outlet express the community domain consistently.
- **Tests:** Extensive server and client suites cover models, services, requests, policies, plugins, migrations, jobs, UI behavior, security, performance, and regressions.
- **Documentation:** Developer guides, plugin APIs, setup documentation, architecture notes, and the live community provide deep operational and extension context.
- **Traceability:** Creating a post can be followed from the topic endpoint through authorization and PostCreator, transactions and callbacks, jobs, search and notifications, serialization, client rendering, and specs.
- **Maintainability:** Domain services, policy objects, plugin boundaries, migrations, feature flags, and broad tests provide structure for continuous product change at large scale.
- **Educational value:** It is an expert-level source for studying the full lifecycle of a long-lived community product rather than an isolated framework.

**Inspection record:** commit `58f18d48d66d5ab9bfbfb35cde4c0ef932aea5b9`, reviewed 2026-08-28 by Codex. Files sampled: `README.md`, `Gemfile`, `app/controllers/topics_controller.rb`, `app/models/post.rb`, `spec/models/post_spec.rb`, `LICENSE.txt`. GitHub Linguist label: Ruby. LOC exclusions: **/test/, **/spec/, fixtures/, locales/, vendor/, node_modules/, generated/, *.json.

**License:** [GPL-2.0-only](https://github.com/discourse/discourse/blob/58f18d48d66d5ab9bfbfb35cde4c0ef932aea5b9/LICENSE.txt)

_Generated from `catalog/ruby.json`; do not edit by hand._

# Ruby

10 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

**Source legend:** Production software is built primarily for real users or systems. Educational exemplars are complete teaching-oriented software and may appear only at Levels 1 and 2.

**You are not expected to understand the whole repository.** Follow the exact starting lines and focused tests in one entry; everything else can wait.

[← All languages](../README.md)

## Level 1 — First real code

### [ruby/abbrev](https://github.com/ruby/abbrev)

**Recommended first path**

**Source:** Production software

A Ruby default gem that builds all unambiguous word prefixes and removes a prefix as soon as a collision appears.

**Just start:** Read lines 74–107 of `abbrev.rb`, then compare them with `test_abbrev.rb`.

**Start with: 34 lines of source.** [Open `lib/abbrev.rb`, lines 74–107.](https://github.com/ruby/abbrev/blob/138820c087d1fccc776eb7665634ac6bca602faf/lib/abbrev.rb#L74-L107)

**Why study it:** Trace a small production algorithm whose hashes make both successful prefixes and collisions visible, then predict the exact abbreviation table.

**Prerequisites:**

- The global novice Ruby baseline: methods, arrays, strings, hashes, loops, modules, and focused tests.
- The selected path uses the default unfiltered call; the nearby optional pattern branch can be skipped on a first reading.

**Concepts this path develops:**

- Tracking candidate uniqueness with occurrence counts.
- Deleting a previously valid result when a collision appears.
- Building a deterministic lookup table from ordinary strings.

**Learning path:**

- **Goal:** Understand how Abbrev turns words into a hash of every unambiguous prefix without losing full-word lookups.
- **Start here:** [`lib/abbrev.rb`, lines 74–107](https://github.com/ruby/abbrev/blob/138820c087d1fccc776eb7665634ac6bca602faf/lib/abbrev.rb#L74-L107) — The abbrev method contains the complete prefix loop, collision count, deletion rule, and final full-word pass.
- **Then read:**
  - [`test/test_abbrev.rb`](https://github.com/ruby/abbrev/blob/138820c087d1fccc776eb7665634ac6bca602faf/test/test_abbrev.rb)
  - [`README.md`](https://github.com/ruby/abbrev/blob/138820c087d1fccc776eb7665634ac6bca602faf/README.md)
- **Trace:** For each nonempty word, walk prefix lengths downward, increment seen, add the first occurrence, delete the second, and stop after later collisions; then restore each full word and compare the resulting hash with the direct summer, winter, win, ruby, and rules assertion.

**Why this level:**

**Level 1:** The central algorithm uses familiar loops, strings, hashes, and branches; the optional filter and delegation can be skipped without hiding the selected behavior.

**License:** Ruby OR BSD-2-Clause ([evidence 1](https://github.com/ruby/abbrev/blob/138820c087d1fccc776eb7665634ac6bca602faf/LICENSE.txt))

<details>
<summary>Detailed Level, learning, quality, and review evidence</summary>

**What you can learn:**

- Generate progressively shorter prefixes for each input word.
- Use one hash to count sightings and another to retain only unambiguous results.
- Explain why full words remain valid even when their shorter prefixes collide.

**Language 1 / Behavior 2 / Design 1 / Constraints 1 → Level 1**

- **Language technique 1:** The selected unfiltered path uses basic Ruby collections, iteration, slicing, and branching.
- **Behavioral reasoning 2:** A small amount of local mutable state distinguishes unique and colliding prefixes, but remains easy to simulate.
- **Design span 1:** One source method and its direct assertions contain the complete selected behavior.
- **Constraint burden 1:** The contract consists of two local deterministic rules without wider compatibility constraints.
- **Novice accessibility floor 1:** The central algorithm uses familiar loops, strings, hashes, and branches; the optional filter and delegation can be skipped without hiding the selected behavior.
  - **Central concepts:** string prefixes; hash-based occurrence counts; collision removal
  - **Incidental concepts:** the optional regular-expression filter; the Array convenience extension
- **Placement:** The four scores 1/2/1/1 produce rubric Level 1. Novice accessibility floor 1 preserves published Level 1.

**Purpose evidence:** The repository packages and releases abbrev as an installable Ruby default gem with a documented public API and direct regression tests.

**Language evidence:** The default gem's abbreviation algorithm, Array convenience method, documentation, and direct Test::Unit suite are first-party Ruby; GitHub labels the repository Ruby.

**Coding relevance:**

Prefix generation, collision tracking, and deterministic map construction are broadly transferable programming techniques.

No specialist domain context is required.

**Eight-part quality gate:**

- **Source quality:** The algorithm exposes its two state hashes and collision cases directly, with examples adjacent to the public method.
- **Architecture:** One module function owns the algorithm and one thin Array method delegates to it without duplication.
- **Naming and idiom:** table, seen, word, len, and abbrev communicate the evolving prefix state with conventional Ruby iteration.
- **Tests:** The direct suite checks collisions, retained full words, prefix filtering, delegation, and strings containing a line break.
- **Documentation:** The README and method documentation explain the mapping contract with several exact output hashes.
- **Traceability:** Every expected prefix can be followed through one count and the corresponding add, delete, or restore action.
- **Maintainability:** The small public surface, deterministic algorithm, and exact result maps make regressions easy to locate.
- **Educational value:** It is a substantial but approachable first production algorithm built entirely from novice-baseline Ruby tools.

**Inspection record:** commit `138820c087d1fccc776eb7665634ac6bca602faf`, inspected 2026-08-30. Review passes: Codex lower-level expansion pass. Files inspected: `lib/abbrev.rb`, `test/test_abbrev.rb`, `README.md`, `abbrev.gemspec`, `LICENSE.txt`. GitHub Linguist label: Ruby.

</details>

## Level 2 — Guided real-world patterns

_Ordered from gentler to more demanding within this Level._

### [sinatra/sinatra](https://github.com/sinatra/sinatra)

**Source:** Educational exemplar

Sinatra's complete hello-world example declares one route with a Ruby block and verifies its response body in the README test suite.

**Just start:** Read lines 6–30 of `README.md`, then compare them with `readme_test.rb`.

**Start with: 25 lines of source.** [Open `README.md`, lines 6–30.](https://github.com/sinatra/sinatra/blob/cb22afd7902b566b6eaba6c4ea89739494a65d12/README.md#L6-L30)

**Why study it:** Read a whole web application small enough to hold in memory while learning how a route block becomes an externally checked response.

Levels 1–2 may use intentionally instructive software when it provides a gentler path into reading good source code.

**Short context:**

- Only the basic GET request, path, and response-body model stated in the prerequisites is needed.

**Prerequisites:**

- The global novice Ruby baseline: methods, strings, blocks, require, and focused tests.
- An HTTP GET request names a path, and a route block returns the body for matching requests.

**Concepts this path develops:**

- Using a small domain-specific language to register application behavior.
- Connecting a request route to a returned body.
- Testing documented examples as observable application behavior.

**Learning path:**

- **Goal:** Understand how Sinatra's complete minimal application maps GET / to Hello world and verifies that documentation example in code.
- **Start here:** [`README.md`, lines 6–30](https://github.com/sinatra/sinatra/blob/cb22afd7902b566b6eaba6c4ea89739494a65d12/README.md#L6-L30) — The opening example contains the complete application and immediately explains how to install, run, and view it.
- **Then read:**
  - [`test/readme_test.rb`](https://github.com/sinatra/sinatra/blob/cb22afd7902b566b6eaba6c4ea89739494a65d12/test/readme_test.rb)
  - [`sinatra.gemspec`](https://github.com/sinatra/sinatra/blob/cb22afd7902b566b6eaba6c4ea89739494a65d12/sinatra.gemspec)
- **Trace:** Require Sinatra, register GET / with a block returning Hello world, then follow ReadmeTest as it constructs the same route, performs GET /, and checks the exact body.

**Why this level:**

**Level 2:** A short route-and-response primer makes the example and its test predictable; framework internals are not required for the selected behavior.

**License:** MIT ([evidence 1](https://github.com/sinatra/sinatra/blob/cb22afd7902b566b6eaba6c4ea89739494a65d12/LICENSE))

<details>
<summary>Detailed Level, learning, quality, and review evidence</summary>

**What you can learn:**

- Declare an HTTP method and path with Sinatra's route syntax.
- Return a response body from the route's Ruby block.
- Execute the route in a test and assert the exact body a caller receives.

**Language 2 / Behavior 2 / Design 1 / Constraints 1 → Level 2**

- **Language technique 2:** Blocks and the route DSL are common professional Ruby idioms that remain direct in this example.
- **Behavioral reasoning 2:** One framework dispatch step is central, but the matching route and result remain locally predictable.
- **Design span 1:** The application behavior and its verification each fit in one small visible block.
- **Constraint burden 1:** The exemplar has one ordinary observable contract and no interacting production constraints.
- **Novice accessibility floor 2:** A short route-and-response primer makes the example and its test predictable; framework internals are not required for the selected behavior.
  - **Central concepts:** route declaration; request dispatch; response-body verification
  - **Incidental concepts:** Sinatra's internal routing implementation
- **Placement:** The four scores 2/2/1/1 produce rubric Level 2. Novice accessibility floor 2 preserves published Level 2.

**Purpose evidence:** Sinatra presents this finished four-line application as the first runnable example in its primary README and maintains an executable ReadmeTest that asserts the example's exact result.

**Language evidence:** The documented hello-world application and the test that executes its route are first-party Ruby in README.md and test/readme_test.rb; GitHub labels the repository Ruby.

**Coding relevance:**

The complete example teaches transferable callback routing and behavior verification without requiring HTTP protocol internals.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The checked-in example is complete, direct, and contains no placeholder or omitted application step.
- **Architecture:** A single route is proportionate to the artifact, while the README test keeps verification separate.
- **Naming and idiom:** require, get, the root path, and a returned string use Sinatra's standard minimal style.
- **Tests:** ReadmeTest constructs the documented route, performs a request, and asserts the exact response body.
- **Documentation:** The primary README begins with the complete source, installation, run command, viewing address, and route explanation.
- **Traceability:** The example's only route corresponds directly to the first executable README test.
- **Maintainability:** Testing the documentation prevents the canonical first example from silently drifting away from framework behavior.
- **Educational value:** The artifact introduces a real framework pattern through a complete program rather than a disconnected statement.

**Inspection record:** commit `cb22afd7902b566b6eaba6c4ea89739494a65d12`, inspected 2026-08-30. Review passes: Codex lower-level expansion pass. Files inspected: `README.md`, `test/readme_test.rb`, `sinatra.gemspec`, `LICENSE`. GitHub Linguist label: Ruby.

</details>

### [ruby/observer](https://github.com/ruby/observer)

**Source:** Production software

Ruby's Observer default gem stores subscribers and notifies their chosen methods only after the observable marks itself changed.

**Just start:** Read lines 138–229 of `observer.rb`, then compare them with `test_observer.rb`.

**Start with: 92 lines of source.** [Open `lib/observer.rb`, lines 138–229.](https://github.com/ruby/observer/blob/ebf1653465ee6854bdf35c8f2b794713068daa26/lib/observer.rb#L138-L229)

**Why study it:** Follow a compact publish-and-subscribe lifecycle from registration through change gating, callback dispatch, reset, and removal.

**Prerequisites:**

- The global novice Ruby baseline: classes, modules, hashes, instance variables, methods, symbols, and focused tests.
- A callback is a method saved now so another object can invoke it when an event occurs.

**Concepts this path develops:**

- Maintaining a collection of subscribers and callback names.
- Using explicit state to prevent accidental notifications.
- Dispatching event arguments and updating subscriptions safely.

**Learning path:**

- **Goal:** Understand how Ruby Observable registers subscribers, gates events on changed state, dispatches arguments, and removes subscriptions.
- **Start here:** [`lib/observer.rb`, lines 138–229](https://github.com/ruby/observer/blob/ebf1653465ee6854bdf35c8f2b794713068daa26/lib/observer.rb#L138-L229) — The Observable module contains registration, removal, state, count, and notification behavior in one readable unit.
- **Then read:**
  - [`test/test_observer.rb`](https://github.com/ruby/observer/blob/ebf1653465ee6854bdf35c8f2b794713068daa26/test/test_observer.rb)
  - [`README.md`](https://github.com/ruby/observer/blob/ebf1653465ee6854bdf35c8f2b794713068daa26/README.md)
- **Trace:** Add each watcher and callback to @observer_peers, call changed before notify_observers, dispatch the event arguments with __send__, reset @observer_state, then follow the direct test as watchers join, receive different event histories, and are removed.

**Why this level:**

**Level 2:** The README supplies a cohesive publish-and-subscribe primer, after which the direct test makes each state transition and event history predictable.

**License:** Ruby OR BSD-2-Clause ([evidence 1](https://github.com/ruby/observer/blob/ebf1653465ee6854bdf35c8f2b794713068daa26/COPYING), [evidence 2](https://github.com/ruby/observer/blob/ebf1653465ee6854bdf35c8f2b794713068daa26/BSDL))

<details>
<summary>Detailed Level, learning, quality, and review evidence</summary>

**What you can learn:**

- Register objects and the callback method each should receive.
- Gate notifications behind an explicit changed state and reset that state afterward.
- Use a behavior test to track which subscribers receive each event after additions and removals.

**Language 2 / Behavior 3 / Design 1 / Constraints 2 → Level 2**

- **Language technique 2:** Mixins and callbacks are common professional Ruby patterns that materially shape the implementation.
- **Behavioral reasoning 3:** Event delivery and subscription state are central, although the complete lifecycle remains compact and synchronous.
- **Design span 1:** One component and its test contain registration, notification, and removal.
- **Constraint burden 2:** Several routine lifecycle guarantees matter, but they are explicit and local.
- **Novice accessibility floor 2:** The README supplies a cohesive publish-and-subscribe primer, after which the direct test makes each state transition and event history predictable.
  - **Central concepts:** subscriber registration; callback dispatch; change-gated event state
  - **Incidental concepts:** __send__ as the dynamic callback operation
- **Placement:** The four scores 2/3/1/2 produce rubric Level 2. Novice accessibility floor 2 preserves published Level 2.

**Purpose evidence:** The repository packages and releases observer as an installable Ruby default gem implementing the application-facing Observable API.

**Language evidence:** The default gem's Observable module, documentation, and direct Test::Unit suite are first-party Ruby; GitHub labels the repository Ruby.

**Coding relevance:**

Subscriber management, change gating, callback dispatch, and direct lifecycle tests are transferable object-design practices.

No specialist domain context is required.

**Eight-part quality gate:**

- **Source quality:** Each lifecycle operation is short, named, and keeps state changes adjacent to the behavior they control.
- **Architecture:** A reusable mixin owns subscriber state while observable and watcher classes retain their own domain responsibilities.
- **Naming and idiom:** add_observer, changed, notify_observers, update, and count_observers expose the pattern's vocabulary directly.
- **Tests:** The direct suite asserts counts and exact notification histories across registration, later registration, single removal, and clearing all observers.
- **Documentation:** The README explains the mechanism, the required changed/notify sequence, callback contract, and a complete worked example.
- **Traceability:** Every lifecycle mutation in the test maps to one Observable method and an exact resulting history.
- **Maintainability:** A small API, explicit state, and end-to-end lifecycle assertions make regressions in delivery or removal visible.
- **Educational value:** It presents a recognizable design pattern in compact production Ruby with enough state to be meaningful but still locally traceable.

**Inspection record:** commit `ebf1653465ee6854bdf35c8f2b794713068daa26`, inspected 2026-08-30. Review passes: Codex lower-level expansion pass. Files inspected: `lib/observer.rb`, `test/test_observer.rb`, `README.md`, `observer.gemspec`, `COPYING`, `BSDL`. GitHub Linguist label: Ruby.

</details>

### [ruby/pathname](https://github.com/ruby/pathname)

**Source:** Production software

A Ruby path method that removes redundant path pieces without reading the filesystem.

**Just start:** Read lines 395–500 of `pathname_builtin.rb`, then compare them with `test_pathname.rb`.

**Start with: 106 lines of source.** [Open `lib/pathname_builtin.rb`, lines 395–500.](https://github.com/ruby/pathname/blob/f0217bbd486b2f7d5c7de1ff3951c7422d42c761/lib/pathname_builtin.rb#L395-L500)

**Why study it:** Follow path components through a small stack that removes dots, handles parent steps, preserves roots, and offers a conservative mode for symbolic links.

**Short context:**

- Lexical path normalization removes redundant separators and dot components without consulting the filesystem, while a conservative mode must avoid assumptions that could change symbolic-link meaning.

**Prerequisites:**

- The global novice Ruby baseline, including classes, arrays, iteration, strings, and table-driven tests.
- Lexical cleanup changes only path text; conservative mode keeps pieces whose removal could change meaning when symbolic links exist.

**Concepts this path develops:**

- Normalizing a path as a sequence of components.
- Using a stack to handle dot and parent pieces.
- Preserving roots and choosing conservative behavior when needed.

**Learning path:**

- **Goal:** Understand how Pathname.cleanpath normalizes a path lexically while preserving roots and optionally retaining components needed for symbolic-link safety.
- **Start here:** [`lib/pathname_builtin.rb`, lines 395–500](https://github.com/ruby/pathname/blob/f0217bbd486b2f7d5c7de1ff3951c7422d42c761/lib/pathname_builtin.rb#L395-L500) — Begin with `lib/pathname_builtin.rb` because it exposes how Pathname.cleanpath normalizes a path lexically while preserving roots and optionally retaining components needed for symbolic-link safety.
- **Then read:**
  - [`lib/pathname.rb`](https://github.com/ruby/pathname/blob/f0217bbd486b2f7d5c7de1ff3951c7422d42c761/lib/pathname.rb)
  - [`test/pathname/test_pathname.rb`](https://github.com/ruby/pathname/blob/f0217bbd486b2f7d5c7de1ff3951c7422d42c761/test/pathname/test_pathname.rb)
- **Trace:** Start at Pathname#cleanpath in lib/pathname_builtin.rb, branch into cleanpath_aggressive or cleanpath_conservative, follow component-stack, prefix, root, and separator handling, then close the behavior with the aggressive and conservative defassert matrices. Read lib/pathname.rb only for loading and the small additional APIs; the catalog's original loader was not the promised normalization implementation.

**Why this level:**

**Level 2:** A short path-components primer makes the local normalization stack predictable; portability cases stretch the lesson but do not require a separate course.

**License:** Ruby OR BSD-2-Clause ([evidence 1](https://github.com/ruby/pathname/blob/f0217bbd486b2f7d5c7de1ff3951c7422d42c761/COPYING), [evidence 2](https://github.com/ruby/pathname/blob/f0217bbd486b2f7d5c7de1ff3951c7422d42c761/BSDL))

<details>
<summary>Detailed Level, learning, quality, and review evidence</summary>

**What you can learn:**

- Trace ordinary, dot, parent, rooted, and trailing-separator examples.
- Compare aggressive and conservative cleanup modes.
- Use the test matrix to understand platform and boundary cases.

**Language 2 / Behavior 2 / Design 1 / Constraints 3 → Level 2**

- **Language technique 2:** The path uses common professional Ruby collection, object, and helper idioms without recurring metaprogramming.
- **Behavioral reasoning 2:** Meaningful branches and local mutable state remain easy to trace in one normalization routine.
- **Design span 1:** The behavior stays within a few methods in one focused implementation unit.
- **Constraint burden 3:** Several material compatibility and portability guarantees shape otherwise local normalization.
- **Novice accessibility floor 2:** A short path-components primer makes the local normalization stack predictable; portability cases stretch the lesson but do not require a separate course.
  - **Central concepts:** lexical path normalization; component-stack handling of dot and parent pieces; conservative symbolic-link behavior
  - **Incidental concepts:** regular-expression helpers; Windows drive and UNC cases
- **Placement:** The four structural scores 2/2/1/3 produce rubric Level 2 under the documented formula and guardrails. Novice accessibility floor 2 produces published Level 2.

**Purpose evidence:** The repository publishes Ruby's pathname default gem and implements the Pathname API used throughout Ruby tooling and applications.

**Language evidence:** The path value object and nearly all path and filesystem behavior are Ruby under lib/, with a small C extension for selected primitives.

**Coding relevance:**

Path components, roots, separators, and symbolic-link preservation are familiar and self-contained; the path teaches transferable immutable value objects, normalization algorithms, platform compatibility, boundary-case design, and table-driven testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The immutable Pathname implementation separates aggressive and conservative normalization into small named methods, documents their filesystem-free contract, and closes it with an exhaustive assertion matrix covering empty, relative, rooted, dot, dot-dot, trailing-separator, drive, and UNC cases; the corrected implementation path is direct and maintainable.
- **Architecture:** The audited architecture of the path beginning at `lib/pathname_builtin.rb` has these boundaries: one lexical normalization component and one direct assertion matrix.
- **Naming and idiom:** `lib/pathname_builtin.rb` and its supporting files use these characteristic Ruby mechanisms: immutable value-object methods, component iteration and regular-expression helpers, and conventional private helper composition.
- **Tests:** Direct tests in `test/pathname/test_pathname.rb` cover these states and branches in the selected path: aggressive and conservative branches, localized component-stack state, and root and trailing-separator edge paths.
- **Documentation:** `lib/pathname_builtin.rb` and its selected supporting material document the contracts needed to understand how Pathname.cleanpath normalizes a path lexically while preserving roots and optionally retaining components needed for symbolic-link safety.
- **Traceability:** Start at Pathname#cleanpath in lib/pathname_builtin.rb, branch into cleanpath_aggressive or cleanpath_conservative, follow component-stack, prefix, root, and separator handling, then close the behavior with the aggressive and conservative defassert matrices. Read lib/pathname.rb only for loading and the small additional APIs; the catalog's original loader was not the promised normalization implementation.
- **Maintainability:** Changes to the path beginning at `lib/pathname_builtin.rb` are constrained by these audited guarantees: relative and absolute root preservation, symbolic-link-safe conservative semantics, Unix, drive-letter, and UNC portability, and stable lexical output contracts.
- **Educational value:** Understand how Pathname.cleanpath normalizes a path lexically while preserving roots and optionally retaining components needed for symbolic-link safety. Path components, roots, separators, and symbolic-link preservation are familiar and self-contained; the path teaches transferable immutable value objects, normalization algorithms, platform compatibility, boundary-case design, and table-driven testing.

**Inspection record:** commit `f0217bbd486b2f7d5c7de1ff3951c7422d42c761`, inspected 2026-08-30. Review passes: Codex primary pass; independent Codex verification pass; Codex novice-accessibility audit. Files inspected: `lib/pathname_builtin.rb`, `lib/pathname.rb`, `test/pathname/test_pathname.rb`, `COPYING`, `BSDL`. GitHub Linguist label: Ruby.

</details>

## Level 3 — Intermediate production software

_Ordered from gentler to more demanding within this Level._

### [jekyll/jekyll](https://github.com/jekyll/jekyll)

**Language 3 / Behavior 3 / Design 3 / Constraints 4 → Level 3**

**Source:** Production software

A static-site generator that transforms Markdown, Liquid templates, data, assets, and configuration into a deployable website.

**Why study it:** Understand how Jekyll transforms one source document through Liquid, converters, hooks, nested layouts, and incremental dependency recording into generated output. Markdown, Liquid, front matter, and layouts need only a short orientation; the selected renderer path teaches transferable staged pipelines, strategy selection, hooks, mutable transformation state, cycle protection, dependency tracking, error propagation, and integration testing.

**Short context:**

- A static-site document may pass through a template engine, one or more markup converters, nested layouts, hooks, and an incremental-build dependency tracker before being written.

**Prerequisites:**

- Basic familiarity with Ruby classes and modules, blocks, collections, exceptions, enumerators, and unit tests.
- A static-site document may pass through a template engine, one or more markup converters, nested layouts, hooks, and an incremental-build dependency tracker before being written.

**Concepts this path develops:**

- Converter strategy and reduction pipeline.
- Ordered mutable render phases.
- Template and converter plugin compatibility.

**What you can learn:**

- Study these transferable Ruby mechanisms in `lib/jekyll/renderer.rb`: converter strategy and reduction pipeline, hook and plugin framework idioms, and Liquid payload and document abstractions.
- Trace these states and branches from `lib/jekyll/renderer.rb` through its selected supporting files: ordered mutable render phases, hook and converter error propagation, nested layout state and cycle detection, and incremental dependency updates.
- Identify these architectural responsibilities in the path beginning at `lib/jekyll/renderer.rb`: document and Convertible boundary, Renderer pipeline, Liquid and converter plugins, and layout and Regenerator boundaries.
- Study these change constraints for the path beginning at `lib/jekyll/renderer.rb`: template and converter plugin compatibility, strict Liquid options and error reporting, layout-cycle and data-merging correctness, and output extension and incremental rebuild consistency.

**Learning path:**

- **Goal:** Understand how Jekyll transforms one source document through Liquid, converters, hooks, nested layouts, and incremental dependency recording into generated output.
- **Start here:** [`jekyll/renderer.rb`](https://github.com/jekyll/jekyll/blob/74d751339d3e534aa51d5d7b0640e9bd743509e4/lib/jekyll/renderer.rb) — Begin with `lib/jekyll/renderer.rb` because it exposes how Jekyll transforms one source document through Liquid, converters, hooks, nested layouts, and incremental dependency recording into generated output.
- **Then read:**
  - [`lib/jekyll/convertible.rb`](https://github.com/jekyll/jekyll/blob/74d751339d3e534aa51d5d7b0640e9bd743509e4/lib/jekyll/convertible.rb)
  - [`lib/jekyll/regenerator.rb`](https://github.com/jekyll/jekyll/blob/74d751339d3e534aa51d5d7b0640e9bd743509e4/lib/jekyll/regenerator.rb)
  - [`test/test_document.rb`](https://github.com/jekyll/jekyll/blob/74d751339d3e534aa51d5d7b0640e9bd743509e4/test/test_document.rb)
  - [`test/test_generated_site.rb`](https://github.com/jekyll/jekyll/blob/74d751339d3e534aa51d5d7b0640e9bd743509e4/test/test_generated_site.rb)
  - [`test/test_site.rb`](https://github.com/jekyll/jekyll/blob/74d751339d3e534aa51d5d7b0640e9bd743509e4/test/test_site.rb)
- **Trace:** Start at Renderer#run, follow payload preparation and pre-render hooks into render_document, then follow optional Liquid rendering, ordered converter reduction, post-convert hooks, nested layout rendering with cycle detection, and Regenerator dependency recording; connect Convertible#do_layout to the public document lifecycle and close with document, generated-site, and site integration tests. The catalog's Site#process start was a broader composition root, and there is no pinned test/test_renderer.rb.

**Why this level:**

- **Language technique 3:** Framework callbacks, plugin strategies, and higher-order composition materially shape the Ruby path.
- **Behavioral reasoning 3:** A nontrivial staged lifecycle with hooks, mutable output, cycles, and incremental state remains locally traceable.
- **Design span 3:** The path crosses several meaningful interfaces whose responsibilities remain clear.
- **Constraint burden 4:** Multiple compatibility, correctness, cycle, and incremental-build guarantees interact across the renderer.
- **Placement:** The four scores 3/3/3/4 sum to 13; their arithmetic mean is 3.25 and rounds half-up to Level 3. The published result is Level 3.

**License:** MIT ([evidence 1](https://github.com/jekyll/jekyll/blob/74d751339d3e534aa51d5d7b0640e9bd743509e4/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository publishes the Jekyll gem and command-line tool used for blogs, documentation, and GitHub Pages workflows.

**Language evidence:** Site discovery, collections, front matter, rendering, plugins, incremental regeneration, destination writing, and CLI behavior are Ruby under lib/.

**Coding relevance:**

Markdown, Liquid, front matter, and layouts need only a short orientation; the selected renderer path teaches transferable staged pipelines, strategy selection, hooks, mutable transformation state, cycle protection, dependency tracking, error propagation, and integration testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Renderer methods expose each transformation phase directly, Convertible supplies a clear public bridge, and Regenerator records incremental dependencies; document, generated-site, and site tests observe template data, converter output, layouts, destinations, hooks, and generated files, while the README and code comments orient the learner. No test/test_renderer.rb exists at the pin, so only verified integration tests close the path.
- **Architecture:** The audited architecture of the path beginning at `lib/jekyll/renderer.rb` has these boundaries: document and Convertible boundary, Renderer pipeline, Liquid and converter plugins, and layout and Regenerator boundaries.
- **Naming and idiom:** `lib/jekyll/renderer.rb` and its supporting files use these characteristic Ruby mechanisms: converter strategy and reduction pipeline, hook and plugin framework idioms, and Liquid payload and document abstractions.
- **Tests:** Direct tests in `test/test_document.rb`, `test/test_generated_site.rb`, and `test/test_site.rb` cover these states and branches in the selected path: ordered mutable render phases, hook and converter error propagation, nested layout state and cycle detection, and incremental dependency updates.
- **Documentation:** `lib/jekyll/renderer.rb` and its selected supporting material document the contracts needed to understand how Jekyll transforms one source document through Liquid, converters, hooks, nested layouts, and incremental dependency recording into generated output.
- **Traceability:** Start at Renderer#run, follow payload preparation and pre-render hooks into render_document, then follow optional Liquid rendering, ordered converter reduction, post-convert hooks, nested layout rendering with cycle detection, and Regenerator dependency recording; connect Convertible#do_layout to the public document lifecycle and close with document, generated-site, and site integration tests. The catalog's Site#process start was a broader composition root, and there is no pinned test/test_renderer.rb.
- **Maintainability:** Changes to the path beginning at `lib/jekyll/renderer.rb` are constrained by these audited guarantees: template and converter plugin compatibility, strict Liquid options and error reporting, layout-cycle and data-merging correctness, and output extension and incremental rebuild consistency.
- **Educational value:** Understand how Jekyll transforms one source document through Liquid, converters, hooks, nested layouts, and incremental dependency recording into generated output. Markdown, Liquid, front matter, and layouts need only a short orientation; the selected renderer path teaches transferable staged pipelines, strategy selection, hooks, mutable transformation state, cycle protection, dependency tracking, error propagation, and integration testing.

**Inspection record:** commit `74d751339d3e534aa51d5d7b0640e9bd743509e4`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `lib/jekyll/renderer.rb`, `lib/jekyll/convertible.rb`, `lib/jekyll/regenerator.rb`, `test/test_document.rb`, `test/test_generated_site.rb`, `test/test_site.rb`, `LICENSE`. GitHub Linguist label: Ruby.

</details>

### [ruby/tempfile](https://github.com/ruby/tempfile)

**Language 2 / Behavior 3 / Design 2 / Constraints 4 → Level 3**

**Source:** Production software

Ruby's standard temporary-file library, providing secure creation plus explicit and automatic cleanup lifecycles.

**Why study it:** Understand how Tempfile.create securely opens a temporary file and guarantees deterministic close and unlink behavior around a caller block. Temporary-file permissions and unlink behavior need only a short explanation; the selected block-based path teaches transferable resource ownership, secure creation, exception-safe cleanup, cross-platform fallback, API design, and focused behavioral testing.

**Short context:**

- A temporary file must be created without a name race, opened with restrictive permissions, and removed after its owner finishes using it.

**Prerequisites:**

- Basic familiarity with Ruby classes and modules, blocks, collections, exceptions, enumerators, and unit tests.
- A temporary file must be created without a name race, opened with restrictive permissions, and removed after its owner finishes using it.

**Concepts this path develops:**

- Block-scoped resource ownership.
- Create, yield, close, and unlink lifecycle.
- Race-resistant name creation and restrictive permissions.

**What you can learn:**

- Study these transferable Ruby mechanisms in `lib/tempfile.rb`: block-scoped resource ownership, keyword forwarding and conventional exception cleanup, and ordinary class and file composition.
- Trace these states and branches from `lib/tempfile.rb` through its selected supporting files: create, yield, close, and unlink lifecycle, cleanup after normal return or exception, and anonymous and platform-specific fallback branches.
- Identify these architectural responsibilities in the path beginning at `lib/tempfile.rb`: one public temporary-file component, standard-library name-generation and File boundaries, and one direct behavioral test suite.
- Study these change constraints for the path beginning at `lib/tempfile.rb`: race-resistant name creation and restrictive permissions, exception-safe close and unlink guarantees, Windows, POSIX, and anonymous-file differences, and stable public cleanup semantics.

**Learning path:**

- **Goal:** Understand how Tempfile.create securely opens a temporary file and guarantees deterministic close and unlink behavior around a caller block.
- **Start here:** [`lib/tempfile.rb`](https://github.com/ruby/tempfile/blob/344da5e29e3215691209223249ebd64e66dff6b8/lib/tempfile.rb) — Begin with `lib/tempfile.rb` because it exposes how Tempfile.create securely opens a temporary file and guarantees deterministic close and unlink behavior around a caller block.
- **Then read:**
  - [`test/test_tempfile.rb`](https://github.com/ruby/tempfile/blob/344da5e29e3215691209223249ebd64e66dff6b8/test/test_tempfile.rb)
- **Trace:** Start at Tempfile.create, follow Dir::Tmpname.create into restrictive File.open, then follow the yielded File through the ensure branch that closes and unlinks it; close with block, traversal, anonymous-file, permission, and cleanup tests. Compare FinalizerManager only as the fallback used by the older object lifecycle, not as machinery required by the main block-and-ensure trace.

**Why this level:**

- **Language technique 2:** The selected path uses common professional Ruby block, object, and ensure idioms; finalizer machinery is a fallback comparison rather than recurring main-path evidence.
- **Behavioral reasoning 3:** A real resource lifecycle and its failure cleanup materially shape the trace without creating expert nonlocal reasoning.
- **Design span 2:** A few clear collaborators contain the complete behavior.
- **Constraint burden 4:** Security, resource cleanup, compatibility, and cross-platform guarantees interact throughout temporary-file creation.
- **Placement:** The four scores 2/3/2/4 sum to 11; their arithmetic mean is 2.75 and rounds half-up to Level 3. The published result is Level 3.

**License:** Ruby OR BSD-2-Clause ([evidence 1](https://github.com/ruby/tempfile/blob/344da5e29e3215691209223249ebd64e66dff6b8/COPYING), [evidence 2](https://github.com/ruby/tempfile/blob/344da5e29e3215691209223249ebd64e66dff6b8/BSDL))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository publishes the tempfile default gem used by Ruby applications and the Ruby standard library.

**Language evidence:** Temporary-file creation, permissions, cleanup, delegation, and lifecycle behavior are implemented in Ruby under lib/.

**Coding relevance:**

Temporary-file permissions and unlink behavior need only a short explanation; the selected block-based path teaches transferable resource ownership, secure creation, exception-safe cleanup, cross-platform fallback, API design, and focused behavioral testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The compact implementation names creation and cleanup responsibilities directly, documents explicit versus automatic cleanup, and has focused tests for block success and failure, restrictive permissions, path traversal, anonymous files, unlink behavior, platform differences, and finalizer fallback; the main Tempfile.create trace remains readable from public API through ensure cleanup to a direct test.
- **Architecture:** The audited architecture of the path beginning at `lib/tempfile.rb` has these boundaries: one public temporary-file component, standard-library name-generation and File boundaries, and one direct behavioral test suite.
- **Naming and idiom:** `lib/tempfile.rb` and its supporting files use these characteristic Ruby mechanisms: block-scoped resource ownership, keyword forwarding and conventional exception cleanup, and ordinary class and file composition.
- **Tests:** Direct tests in `test/test_tempfile.rb` cover these states and branches in the selected path: create, yield, close, and unlink lifecycle, cleanup after normal return or exception, and anonymous and platform-specific fallback branches.
- **Documentation:** `lib/tempfile.rb` and its selected supporting material document the contracts needed to understand how Tempfile.create securely opens a temporary file and guarantees deterministic close and unlink behavior around a caller block.
- **Traceability:** Start at Tempfile.create, follow Dir::Tmpname.create into restrictive File.open, then follow the yielded File through the ensure branch that closes and unlinks it; close with block, traversal, anonymous-file, permission, and cleanup tests. Compare FinalizerManager only as the fallback used by the older object lifecycle, not as machinery required by the main block-and-ensure trace.
- **Maintainability:** Changes to the path beginning at `lib/tempfile.rb` are constrained by these audited guarantees: race-resistant name creation and restrictive permissions, exception-safe close and unlink guarantees, Windows, POSIX, and anonymous-file differences, and stable public cleanup semantics.
- **Educational value:** Understand how Tempfile.create securely opens a temporary file and guarantees deterministic close and unlink behavior around a caller block. Temporary-file permissions and unlink behavior need only a short explanation; the selected block-based path teaches transferable resource ownership, secure creation, exception-safe cleanup, cross-platform fallback, API design, and focused behavioral testing.

**Inspection record:** commit `344da5e29e3215691209223249ebd64e66dff6b8`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `lib/tempfile.rb`, `test/test_tempfile.rb`, `COPYING`, `BSDL`. GitHub Linguist label: Ruby.

</details>

## Level 4 — Advanced

_Ordered from gentler to more demanding within this Level._

### [rubocop/rubocop](https://github.com/rubocop/rubocop)

**Language 4 / Behavior 4 / Design 4 / Constraints 5 → Level 4**

**Source:** Production software

A configurable Ruby static analyzer and formatter built around independently selectable cops.

**Why study it:** Understand how RuboCop inspects one Ruby file, dispatches AST callbacks to configured cops, combines corrections, and repeats autocorrection safely until the source stabilizes or a cycle is detected. AST nodes, source ranges, and lint rules need only a short programming-oriented explanation; the path teaches transferable visitor dispatch, runtime callback generation, plugin lifecycles, edit collation, conflict detection, fixed-point iteration, caching, error isolation, and contract testing.

**Short context:**

- A lint cop receives callbacks while an abstract syntax tree is visited, reports source-range offenses, and may propose edits that must be combined and repeatedly applied until stable.

**Prerequisites:**

- Working familiarity with Ruby classes and modules, blocks, collections, exceptions, enumerators, and unit tests, plus experience tracing behavior across several production files.
- A lint cop receives callbacks while an abstract syntax tree is visited, reports source-range offenses, and may propose edits that must be combined and repeatedly applied until stable.

**Concepts this path develops:**

- Runtime class_eval generation of AST callback methods.
- AST event propagation through many cops.
- Exact source ranges, encodings, and syntax preservation.

**What you can learn:**

- Study these transferable Ruby mechanisms in `lib/rubocop/runner.rb`: runtime class_eval generation of AST callback methods, reflection and callback discovery, cop DSL and plugin framework conventions, and dynamic dispatch over node and restriction maps.
- Trace these states and branches from `lib/rubocop/runner.rb` through its selected supporting files: AST event propagation through many cops, repeated autocorrection to a fixed point, overlap, conflict, and cycle handling, and cop error isolation and cache paths.
- Identify these architectural responsibilities in the path beginning at `lib/rubocop/runner.rb`: Runner orchestration and reporting, Team cop coordination, Commissioner visitor dispatch, Base extension lifecycle and Corrector edits, and configuration, cache, and formatter policies.
- Study these change constraints for the path beginning at `lib/rubocop/runner.rb`: exact source ranges, encodings, and syntax preservation, overlapping-edit and semantic-correction safety, termination and infinite-cycle detection, and configuration, plugin, target-Ruby, cache, and formatter compatibility.

**Learning path:**

- **Goal:** Understand how RuboCop inspects one Ruby file, dispatches AST callbacks to configured cops, combines corrections, and repeats autocorrection safely until the source stabilizes or a cycle is detected.
- **Start here:** [`rubocop/runner.rb`](https://github.com/rubocop/rubocop/blob/8b85bafb041debc1f3a955663a99fa384a9d24f6/lib/rubocop/runner.rb) — Begin with `lib/rubocop/runner.rb` because it exposes how RuboCop inspects one Ruby file, dispatches AST callbacks to configured cops, combines corrections, and repeats autocorrection safely until the source stabilizes or a cycle is detected.
- **Then read:**
  - [`lib/rubocop/cop/team.rb`](https://github.com/rubocop/rubocop/blob/8b85bafb041debc1f3a955663a99fa384a9d24f6/lib/rubocop/cop/team.rb)
  - [`lib/rubocop/cop/commissioner.rb`](https://github.com/rubocop/rubocop/blob/8b85bafb041debc1f3a955663a99fa384a9d24f6/lib/rubocop/cop/commissioner.rb)
  - [`lib/rubocop/cop/base.rb`](https://github.com/rubocop/rubocop/blob/8b85bafb041debc1f3a955663a99fa384a9d24f6/lib/rubocop/cop/base.rb)
  - [`lib/rubocop/cop/corrector.rb`](https://github.com/rubocop/rubocop/blob/8b85bafb041debc1f3a955663a99fa384a9d24f6/lib/rubocop/cop/corrector.rb)
  - [`spec/rubocop/runner_spec.rb`](https://github.com/rubocop/rubocop/blob/8b85bafb041debc1f3a955663a99fa384a9d24f6/spec/rubocop/runner_spec.rb)
  - [`spec/rubocop/cop/team_spec.rb`](https://github.com/rubocop/rubocop/blob/8b85bafb041debc1f3a955663a99fa384a9d24f6/spec/rubocop/cop/team_spec.rb)
- **Trace:** Start at Runner#process_file and file_offenses, follow the correction loop into Team#investigate, Commissioner-generated node callbacks, Base offense registration, and Corrector edits, then return through Team's corrector collation and conflict handling to Runner's convergence or infinite-loop result; close with Runner and Team specs.

**Why this level:**

- **Language technique 4:** Generated callbacks, reflection, metaprogramming, and framework DSL behavior recur materially, meeting the advanced anchor without multiple pervasive expert mechanisms for 5.
- **Behavioral reasoning 4:** Event dispatch, correction state, convergence, caching, and failure isolation require advanced nonlocal reasoning.
- **Design span 4:** Many modules, extension points, and cross-cutting policies contribute to inspection and correction.
- **Constraint burden 5:** Several system-wide source-safety, convergence, compatibility, and cache guarantees interact so a local correction change can fail elsewhere.
- **Placement:** The four scores 4/4/4/5 sum to 17; their arithmetic mean is 4.25 and rounds half-up to Level 4. The published result is Level 4.

**License:** MIT ([evidence 1](https://github.com/rubocop/rubocop/blob/8b85bafb041debc1f3a955663a99fa384a9d24f6/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository publishes the RuboCop gem and executable used to lint, format, and enforce Ruby project conventions.

**Language evidence:** Configuration, target discovery, AST inspection, cop dispatch, offense reporting, autocorrection, caching, formatters, and CLI orchestration are Ruby under lib/ and exe/.

**Coding relevance:**

AST nodes, source ranges, and lint rules need only a short programming-oriented explanation; the path teaches transferable visitor dispatch, runtime callback generation, plugin lifecycles, edit collation, conflict detection, fixed-point iteration, caching, error isolation, and contract testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Runner, Team, Commissioner, Base, and Corrector expose recognizable orchestration, dispatch, extension, and edit responsibilities; direct specs cover offenses, cop errors, callback lifecycles, overlapping corrections, conflicting cops, infinite correction cycles, caching, formatter behavior, syntax failures, and autocorrect output, while project documentation explains purpose and configuration.
- **Architecture:** The audited architecture of the path beginning at `lib/rubocop/runner.rb` has these boundaries: Runner orchestration and reporting, Team cop coordination, Commissioner visitor dispatch, Base extension lifecycle and Corrector edits, and configuration, cache, and formatter policies.
- **Naming and idiom:** `lib/rubocop/runner.rb` and its supporting files use these characteristic Ruby mechanisms: runtime class_eval generation of AST callback methods, reflection and callback discovery, cop DSL and plugin framework conventions, and dynamic dispatch over node and restriction maps.
- **Tests:** Direct tests in `spec/rubocop/runner_spec.rb` and `spec/rubocop/cop/team_spec.rb` cover these states and branches in the selected path: AST event propagation through many cops, repeated autocorrection to a fixed point, overlap, conflict, and cycle handling, and cop error isolation and cache paths.
- **Documentation:** `lib/rubocop/runner.rb` and its selected supporting material document the contracts needed to understand how RuboCop inspects one Ruby file, dispatches AST callbacks to configured cops, combines corrections, and repeats autocorrection safely until the source stabilizes or a cycle is detected.
- **Traceability:** Start at Runner#process_file and file_offenses, follow the correction loop into Team#investigate, Commissioner-generated node callbacks, Base offense registration, and Corrector edits, then return through Team's corrector collation and conflict handling to Runner's convergence or infinite-loop result; close with Runner and Team specs.
- **Maintainability:** Changes to the path beginning at `lib/rubocop/runner.rb` are constrained by these audited guarantees: exact source ranges, encodings, and syntax preservation, overlapping-edit and semantic-correction safety, termination and infinite-cycle detection, and configuration, plugin, target-Ruby, cache, and formatter compatibility.
- **Educational value:** Understand how RuboCop inspects one Ruby file, dispatches AST callbacks to configured cops, combines corrections, and repeats autocorrection safely until the source stabilizes or a cycle is detected. AST nodes, source ranges, and lint rules need only a short programming-oriented explanation; the path teaches transferable visitor dispatch, runtime callback generation, plugin lifecycles, edit collation, conflict detection, fixed-point iteration, caching, error isolation, and contract testing.

**Inspection record:** commit `8b85bafb041debc1f3a955663a99fa384a9d24f6`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `lib/rubocop/runner.rb`, `lib/rubocop/cop/team.rb`, `lib/rubocop/cop/commissioner.rb`, `lib/rubocop/cop/base.rb`, `lib/rubocop/cop/corrector.rb`, `spec/rubocop/runner_spec.rb`, `spec/rubocop/cop/team_spec.rb`, `LICENSE.txt`. GitHub Linguist label: Ruby.

</details>

### [sidekiq/sidekiq](https://github.com/sidekiq/sidekiq)

**Language 3 / Behavior 5 / Design 4 / Constraints 5 → Level 4**

**Source:** Production software

A multithreaded background-job processor for Ruby applications backed by Redis.

**Why study it:** Understand how Sidekiq owns one fetched job through middleware and execution, records retryable failure, acknowledges completed work, and preserves unfinished work during shutdown. Queue and at-least-once semantics need only a short explanation; the path teaches transferable threaded processing, ownership, middleware, retries, acknowledgement, shutdown coordination, failure recovery, observability, and concurrency testing.

**Short context:**

- A background worker fetches a job, may execute it at least once, records failure for retry, acknowledges completed work, and must preserve in-progress work during shutdown.

**Prerequisites:**

- Working familiarity with Ruby classes and modules, blocks, collections, exceptions, enumerators, and unit tests, plus experience tracing behavior across several production files.
- A background worker fetches a job, may execute it at least once, records failure for retry, acknowledges completed work, and must preserve in-progress work during shutdown.

**Concepts this path develops:**

- Middleware block composition.
- Concurrent processor and fetched-work ownership.
- At-least-once delivery and no-loss shutdown.

**What you can learn:**

- Study these transferable Ruby mechanisms in `lib/sidekiq/processor.rb`: middleware block composition, dynamic worker class resolution and framework conventions, and exception wrapper and configuration abstractions.
- Trace these states and branches from `lib/sidekiq/processor.rb` through its selected supporting files: concurrent processor and fetched-work ownership, global and local retry recovery, middleware and worker failure timing, acknowledgement versus preservation, and quiet and forced-shutdown coordination.
- Identify these architectural responsibilities in the path beginning at `lib/sidekiq/processor.rb`: processor and fetch boundary, retry and dead-job lifecycle, middleware extension chain, manager shutdown coordination, and Redis-backed job state and observability.
- Study these change constraints for the path beginning at `lib/sidekiq/processor.rb`: at-least-once delivery and no-loss shutdown; duplicate-tolerant acknowledgement semantics; retry payload, original-argument, and scheduling compatibility; and thread safety, deadlines, middleware, and error reporting.

**Learning path:**

- **Goal:** Understand how Sidekiq owns one fetched job through middleware and execution, records retryable failure, acknowledges completed work, and preserves unfinished work during shutdown.
- **Start here:** [`sidekiq/processor.rb`](https://github.com/sidekiq/sidekiq/blob/1bb4aa06e5aa178a114a5e855f9f3d5c24f6c61b/lib/sidekiq/processor.rb) — Begin with `lib/sidekiq/processor.rb` because it exposes how Sidekiq owns one fetched job through middleware and execution, records retryable failure, acknowledges completed work, and preserves unfinished work during shutdown.
- **Then read:**
  - [`lib/sidekiq/job_retry.rb`](https://github.com/sidekiq/sidekiq/blob/1bb4aa06e5aa178a114a5e855f9f3d5c24f6c61b/lib/sidekiq/job_retry.rb)
  - [`lib/sidekiq/middleware/chain.rb`](https://github.com/sidekiq/sidekiq/blob/1bb4aa06e5aa178a114a5e855f9f3d5c24f6c61b/lib/sidekiq/middleware/chain.rb)
  - [`lib/sidekiq/manager.rb`](https://github.com/sidekiq/sidekiq/blob/1bb4aa06e5aa178a114a5e855f9f3d5c24f6c61b/lib/sidekiq/manager.rb)
  - [`test/processor_test.rb`](https://github.com/sidekiq/sidekiq/blob/1bb4aa06e5aa178a114a5e855f9f3d5c24f6c61b/test/processor_test.rb)
  - [`test/manager_test.rb`](https://github.com/sidekiq/sidekiq/blob/1bb4aa06e5aa178a114a5e855f9f3d5c24f6c61b/test/manager_test.rb)
  - [`docs/internals.md`](https://github.com/sidekiq/sidekiq/blob/1bb4aa06e5aa178a114a5e855f9f3d5c24f6c61b/docs/internals.md)
- **Trace:** Start at Processor#process_one and the fetched unit of work, follow dispatch through global and local JobRetry wrappers, the server middleware chain, worker resolution and execution, then follow the completed flag into acknowledgement or preservation; use Manager shutdown to see deadlines and in-flight ownership, and close with processor and manager tests plus the internals contract.

**Why this level:**

- **Language technique 3:** Substantial Ruby framework idioms shape the path, but advanced reflection or multiple expert language mechanisms do not recur enough for 4.
- **Behavioral reasoning 5:** Threaded execution, retry scheduling, failure recovery, job ownership, and shutdown interact pervasively, making expert nonlocal reasoning unavoidable.
- **Design span 4:** Many modules, extension points, and cross-cutting execution policies contribute to one job lifecycle.
- **Constraint burden 5:** Several system-wide reliability, compatibility, concurrency, and recovery guarantees interact so a local change can lose or duplicate work.
- **Placement:** The four scores 3/5/4/5 sum to 17; their arithmetic mean is 4.25 and rounds half-up to Level 4. The published result is Level 4.

**License:** LGPL-3.0-only ([evidence 1](https://github.com/sidekiq/sidekiq/blob/1bb4aa06e5aa178a114a5e855f9f3d5c24f6c61b/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The project publishes the Sidekiq gem and executable used to run durable asynchronous work for Ruby applications.

**Language evidence:** Job fetching, execution, middleware, retries, scheduling, capsules, Redis coordination, process lifecycle, and the monitoring UI are Ruby under lib/ and web/.

**Coding relevance:**

Queue and at-least-once semantics need only a short explanation; the path teaches transferable threaded processing, ownership, middleware, retries, acknowledgement, shutdown coordination, failure recovery, observability, and concurrency testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Processor, retry, middleware, and manager responsibilities are explicit and documented in the internals guide; direct tests cover fetch and execution exceptions, middleware before and after failures, skip behavior, acknowledgement, original argument preservation, retry delegation, shutdown deadlines, quieting, and work recovery, making the production lifecycle traceable despite its nonlocal guarantees.
- **Architecture:** The audited architecture of the path beginning at `lib/sidekiq/processor.rb` has these boundaries: processor and fetch boundary, retry and dead-job lifecycle, middleware extension chain, manager shutdown coordination, and Redis-backed job state and observability.
- **Naming and idiom:** `lib/sidekiq/processor.rb` and its supporting files use these characteristic Ruby mechanisms: middleware block composition, dynamic worker class resolution and framework conventions, and exception wrapper and configuration abstractions.
- **Tests:** Direct tests in `test/processor_test.rb` and `test/manager_test.rb` cover these states and branches in the selected path: concurrent processor and fetched-work ownership, global and local retry recovery, middleware and worker failure timing, acknowledgement versus preservation, and quiet and forced-shutdown coordination.
- **Documentation:** `lib/sidekiq/processor.rb` and its selected supporting material document the contracts needed to understand how Sidekiq owns one fetched job through middleware and execution, records retryable failure, acknowledges completed work, and preserves unfinished work during shutdown.
- **Traceability:** Start at Processor#process_one and the fetched unit of work, follow dispatch through global and local JobRetry wrappers, the server middleware chain, worker resolution and execution, then follow the completed flag into acknowledgement or preservation; use Manager shutdown to see deadlines and in-flight ownership, and close with processor and manager tests plus the internals contract.
- **Maintainability:** Changes to the path beginning at `lib/sidekiq/processor.rb` are constrained by these audited guarantees: at-least-once delivery and no-loss shutdown, duplicate-tolerant acknowledgement semantics, retry payload, original arguments, and scheduling compatibility, and thread safety, deadlines, middleware, and error reporting.
- **Educational value:** Understand how Sidekiq owns one fetched job through middleware and execution, records retryable failure, acknowledges completed work, and preserves unfinished work during shutdown. Queue and at-least-once semantics need only a short explanation; the path teaches transferable threaded processing, ownership, middleware, retries, acknowledgement, shutdown coordination, failure recovery, observability, and concurrency testing.

**Inspection record:** commit `1bb4aa06e5aa178a114a5e855f9f3d5c24f6c61b`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `lib/sidekiq/processor.rb`, `lib/sidekiq/job_retry.rb`, `lib/sidekiq/middleware/chain.rb`, `lib/sidekiq/manager.rb`, `test/processor_test.rb`, `test/manager_test.rb`, `docs/internals.md`, `LICENSE.txt`. GitHub Linguist label: Ruby.

</details>

## Level 5 — Expert

_Ordered from gentler to more demanding within this Level._

### [ruby-concurrency/concurrent-ruby](https://github.com/ruby-concurrency/concurrent-ruby)

**Language 4 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

**Source:** Production software

A production concurrency toolkit whose promise framework composes asynchronous tasks, dependency graphs, executors, and single-assignment results.

**Why study it:** Understand how one concurrent-ruby future is scheduled, fulfilled or rejected exactly once, and propagated through dependent then or rescue work to callbacks and waiting callers. Futures and executors need only a short concurrency primer; the path teaches transferable asynchronous state machines, atomic single assignment, callback races, executor handoff, dependency graphs, error recovery, timeouts, and blocking boundaries.

**Short context:**

- A future represents one eventual fulfillment or rejection; an executor runs dependent work, and atomic single assignment prevents two competing resolutions from both winning.

**Prerequisites:**

- Strong working familiarity with Ruby classes and modules, blocks, collections, exceptions, enumerators, and unit tests, plus experience tracing state, resources, or asynchronous control flow across many production files.
- A future represents one eventual fulfillment or rejection; an executor runs dependent work, and atomic single assignment prevents two competing resolutions from both winning.

**Concepts this path develops:**

- Blocks and mixins as asynchronous APIs.
- Pending, reserved, fulfilled, and rejected resolution.
- Exactly-once resolution.

**What you can learn:**

- Study these transferable Ruby mechanisms in `lib/concurrent-ruby/concurrent/promises.rb`: blocks and mixins as asynchronous APIs, private state and promise subclasses, and atomic accessors, callbacks, aliases, and executor dispatch.
- Trace these states and branches from `lib/concurrent-ruby/concurrent/promises.rb` through its selected supporting files: pending, reserved, fulfilled, and rejected resolution, then versus rescue propagation, callback registration racing with resolution, and delayed graph touch and blocking wait paths.
- Identify these architectural responsibilities in the path beginning at `lib/concurrent-ruby/concurrent/promises.rb`: public factories and Future API, immutable result-state objects, blocked promise graph, executor boundary, and atomic and blocking synchronization boundary.
- Study these change constraints for the path beginning at `lib/concurrent-ruby/concurrent/promises.rb`: exactly-once resolution, callback visibility under races, rejection and non-StandardError propagation, executor inheritance, timeout and spurious-wakeup correctness, and multiple Ruby runtime backends.

**Learning path:**

- **Goal:** Understand how one concurrent-ruby future is scheduled, fulfilled or rejected exactly once, and propagated through dependent then or rescue work to callbacks and waiting callers.
- **Start here:** [`concurrent/promises.rb`](https://github.com/ruby-concurrency/concurrent-ruby/blob/0b88d5ff75f69b3740c8f0868e76f833cb2fd45d/lib/concurrent-ruby/concurrent/promises.rb) — Begin with `lib/concurrent-ruby/concurrent/promises.rb` because it exposes the complete public factory, dependency, resolution, callback, and observation path.
- **Then read:**
  - [`lib/concurrent-ruby/concurrent/configuration.rb`](https://github.com/ruby-concurrency/concurrent-ruby/blob/0b88d5ff75f69b3740c8f0868e76f833cb2fd45d/lib/concurrent-ruby/concurrent/configuration.rb)
  - [`lib/concurrent-ruby/concurrent/synchronization/object.rb`](https://github.com/ruby-concurrency/concurrent-ruby/blob/0b88d5ff75f69b3740c8f0868e76f833cb2fd45d/lib/concurrent-ruby/concurrent/synchronization/object.rb)
  - [`lib/concurrent-ruby/concurrent/collection/lock_free_stack.rb`](https://github.com/ruby-concurrency/concurrent-ruby/blob/0b88d5ff75f69b3740c8f0868e76f833cb2fd45d/lib/concurrent-ruby/concurrent/collection/lock_free_stack.rb)
  - [`lib/concurrent-ruby/concurrent/atomic/atomic_reference.rb`](https://github.com/ruby-concurrency/concurrent-ruby/blob/0b88d5ff75f69b3740c8f0868e76f833cb2fd45d/lib/concurrent-ruby/concurrent/atomic/atomic_reference.rb)
  - [`lib/concurrent-ruby/concurrent/atomic_reference/mutex_atomic.rb`](https://github.com/ruby-concurrency/concurrent-ruby/blob/0b88d5ff75f69b3740c8f0868e76f833cb2fd45d/lib/concurrent-ruby/concurrent/atomic_reference/mutex_atomic.rb)
  - [`spec/concurrent/promises_spec.rb`](https://github.com/ruby-concurrency/concurrent-ruby/blob/0b88d5ff75f69b3740c8f0868e76f833cb2fd45d/spec/concurrent/promises_spec.rb)
  - [`docs-source/promises-main.md`](https://github.com/ruby-concurrency/concurrent-ruby/blob/0b88d5ff75f69b3740c8f0868e76f833cb2fd45d/docs-source/promises-main.md)
  - [`docs-source/promises.in.md`](https://github.com/ruby-concurrency/concurrent-ruby/blob/0b88d5ff75f69b3740c8f0868e76f833cb2fd45d/docs-source/promises.in.md)
- **Trace:** Start at Promises.future and Future#then or #rescue, follow BlockedPromise dependency registration into ThenPromise or RescuePromise executor posting, then follow evaluate_to into the CAS-backed fulfilled or rejected state, callback draining, and wait or value! observation; close with direct promise specs for arguments, executors, callbacks, timeouts, branching, delay, rejection, reservation, duplicate assignment, and spurious wakeups. Mutex-backed atomic fallbacks and blocking waits mean the selected path must not be described as universally lock-free.

**Why this level:**

- **Language technique 4:** Advanced Ruby object, block, mixin, callback, and generated atomic-accessor techniques recur, without enough pervasive expert metaprogramming for 5.
- **Behavioral reasoning 5:** Concurrent resolution, dependency graphs, executor timing, callbacks, failure, delay, and blocking observation interact nonlocally.
- **Design span 4:** Several strong concurrency boundaries collaborate across one bounded promise framework.
- **Constraint burden 5:** Atomicity, visibility, scheduling, failure, timeout, and cross-runtime guarantees interact so a local change can break distant consumers.
- **Placement:** The four scores 4/5/4/5 sum to 18; their arithmetic mean is 4.50 and rounds half-up to Level 5. Behavioral reasoning and constraint burden both score 5, satisfying the Level 5 guardrail. The published result is Level 5.

**License:** MIT ([evidence 1](https://github.com/ruby-concurrency/concurrent-ruby/blob/0b88d5ff75f69b3740c8f0868e76f833cb2fd45d/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository publishes the concurrent-ruby gem used by Ruby applications for futures, promises, executors, atomic primitives, and other concurrency abstractions.

**Language evidence:** The selected promise graph, executor handoff, atomic state, fallback synchronization, documentation, and direct behavioral specs are first-party Ruby; optional native atomic backends are not required by this path.

**Coding relevance:**

Futures and executors need only a short concurrency primer; the path teaches transferable asynchronous state machines, atomic single assignment, callback races, executor handoff, dependency graphs, error recovery, timeouts, and blocking boundaries.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The large promises implementation is dense but deliberately partitioned into public futures, immutable states, blocked promise types, and resolution helpers; direct specs close its core races and lifecycle. CamelCase final ivars are an explicit synchronization convention rather than ordinary Ruby style.
- **Architecture:** The audited architecture of the path beginning at `lib/concurrent-ruby/concurrent/promises.rb` has these boundaries: public factories and Future API, immutable result-state objects, blocked promise graph, executor boundary, and atomic and blocking synchronization boundary.
- **Naming and idiom:** `lib/concurrent-ruby/concurrent/promises.rb` and its supporting files use these characteristic Ruby mechanisms: blocks and mixins as asynchronous APIs, private state and promise subclasses, and atomic accessors, callbacks, aliases, and executor dispatch.
- **Tests:** Direct specs in `spec/concurrent/promises_spec.rb` cover these states and branches in the selected path: pending, reserved, fulfilled, and rejected resolution, then versus rescue propagation, callback registration racing with resolution, and delayed graph touch and blocking wait paths.
- **Documentation:** The promise guide documents states, graphs, error paths, executor selection, callbacks, and blocking observation; its broad lock-free wording must be read with the source's mutex-backed atomic fallbacks and explicit Mutex/ConditionVariable waits.
- **Traceability:** Start at Promises.future and Future#then or #rescue, follow BlockedPromise dependency registration into ThenPromise or RescuePromise executor posting, then follow evaluate_to into the CAS-backed fulfilled or rejected state, callback draining, and wait or value! observation; close with direct promise specs for arguments, executors, callbacks, timeouts, branching, delay, rejection, reservation, duplicate assignment, and spurious wakeups. Mutex-backed atomic fallbacks and blocking waits mean the selected path must not be described as universally lock-free.
- **Maintainability:** Changes to the path beginning at `lib/concurrent-ruby/concurrent/promises.rb` are constrained by these audited guarantees: exactly-once resolution, callback visibility under races, rejection and non-StandardError propagation, executor inheritance, timeout and spurious-wakeup correctness, and multiple Ruby runtime backends. The 2,184-line core file and runtime backend selection increase review scope.
- **Educational value:** Understand how one concurrent-ruby future is scheduled, fulfilled or rejected exactly once, and propagated through dependent then or rescue work to callbacks and waiting callers. Futures and executors need only a short concurrency primer; the path teaches transferable asynchronous state machines, atomic single assignment, callback races, executor handoff, dependency graphs, error recovery, timeouts, and blocking boundaries.

**Inspection record:** commit `0b88d5ff75f69b3740c8f0868e76f833cb2fd45d`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `lib/concurrent-ruby/concurrent/promises.rb`, `lib/concurrent-ruby/concurrent/configuration.rb`, `lib/concurrent-ruby/concurrent/synchronization/object.rb`, `lib/concurrent-ruby/concurrent/collection/lock_free_stack.rb`, `lib/concurrent-ruby/concurrent/atomic/atomic_reference.rb`, `lib/concurrent-ruby/concurrent/atomic_reference/mutex_atomic.rb`, `lib/concurrent-ruby/concurrent/atomic/atomic_fixnum.rb`, `lib/concurrent-ruby/concurrent/atomic/mutex_atomic_fixnum.rb`, `spec/concurrent/promises_spec.rb`, `docs-source/promises-main.md`, `docs-source/promises.in.md`, `LICENSE.txt`. GitHub Linguist label: Ruby.

</details>

### [socketry/async](https://github.com/socketry/async)

**Language 4 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

**Source:** Production software

A composable fiber-based asynchronous I/O framework with structured task trees, cancellation, timeouts, and Ruby's Fiber scheduler integration.

**Why study it:** Understand how Async creates a Fiber-backed child task, schedules and suspends it, propagates result or failure, and tears down its task tree under cancellation or timeout. Fibers, schedulers, and cooperative cancellation need only a short concurrency primer; the path teaches transferable structured concurrency, lifecycle state machines, promise resolution, exception injection, timeout cleanup, ownership, resource lifetime, and shutdown testing.

**Short context:**

- Ruby's Fiber scheduler cooperatively suspends tasks around blocking operations; child tasks form an ownership tree, and cancellation is delivered at interruption points rather than preemptively killing arbitrary work.

**Prerequisites:**

- Strong working familiarity with Ruby classes and modules, blocks, collections, exceptions, enumerators, and unit tests, plus experience tracing state, resources, or asynchronous control flow across many production files.
- Ruby's Fiber scheduler cooperatively suspends tasks around blocking operations; child tasks form an ownership tree, and cancellation is delivered at interruption points rather than preemptively killing arbitrary work.

**Concepts this path develops:**

- Fiber scheduler integration.
- Initialized, running, completed, failed, and cancelled tasks.
- Task-tree integrity and reparenting.

**What you can learn:**

- Study these transferable Ruby mechanisms in `lib/async/task.rb`: Fiber scheduler integration, exception-based cooperative cancellation, block-scoped task construction, and Promise and task-tree abstractions.
- Trace these states and branches from `lib/async/task.rb` through its selected supporting files: initialized, running, completed, failed, and cancelled tasks, hierarchical and deferred cancellation, suspension, resumption, timeout injection, and transient-child lifetime.
- Identify these architectural responsibilities in the path beginning at `lib/async/task.rb`: public Async entry and Reactor, hierarchical Task and Node ownership, Scheduler and selector boundary, Promise result boundary, and cancellation and timeout operations.
- Study these change constraints for the path beginning at `lib/async/task.rb`: task-tree integrity and reparenting, one-shot result propagation, cancellation-cause preservation, interruption-point semantics, timer cleanup and stale-wakeup avoidance, and selector, worker, and user-resource shutdown.

**Learning path:**

- **Goal:** Understand how Async creates a Fiber-backed child task, schedules and suspends it, propagates result or failure, and tears down its task tree under cancellation or timeout.
- **Start here:** [`async/task.rb`](https://github.com/socketry/async/blob/e8ecf5804802143f58983dc3f8c519c287d9dd9b/lib/async/task.rb) — Begin with `lib/async/task.rb` because it exposes the task state machine, Fiber execution, child creation, result propagation, cancellation, and finish lifecycle.
- **Then read:**
  - [`lib/kernel/async.rb`](https://github.com/socketry/async/blob/e8ecf5804802143f58983dc3f8c519c287d9dd9b/lib/kernel/async.rb)
  - [`lib/async/reactor.rb`](https://github.com/socketry/async/blob/e8ecf5804802143f58983dc3f8c519c287d9dd9b/lib/async/reactor.rb)
  - [`lib/async/scheduler.rb`](https://github.com/socketry/async/blob/e8ecf5804802143f58983dc3f8c519c287d9dd9b/lib/async/scheduler.rb)
  - [`lib/async/node.rb`](https://github.com/socketry/async/blob/e8ecf5804802143f58983dc3f8c519c287d9dd9b/lib/async/node.rb)
  - [`lib/async/promise.rb`](https://github.com/socketry/async/blob/e8ecf5804802143f58983dc3f8c519c287d9dd9b/lib/async/promise.rb)
  - [`lib/async/cancel.rb`](https://github.com/socketry/async/blob/e8ecf5804802143f58983dc3f8c519c287d9dd9b/lib/async/cancel.rb)
  - [`lib/async/timeout.rb`](https://github.com/socketry/async/blob/e8ecf5804802143f58983dc3f8c519c287d9dd9b/lib/async/timeout.rb)
  - [`test/async/task.rb`](https://github.com/socketry/async/blob/e8ecf5804802143f58983dc3f8c519c287d9dd9b/test/async/task.rb)
  - [`test/async/scheduler.rb`](https://github.com/socketry/async/blob/e8ecf5804802143f58983dc3f8c519c287d9dd9b/test/async/scheduler.rb)
  - [`test/async/reactor.rb`](https://github.com/socketry/async/blob/e8ecf5804802143f58983dc3f8c519c287d9dd9b/test/async/reactor.rb)
  - [`test/async/timeout.rb`](https://github.com/socketry/async/blob/e8ecf5804802143f58983dc3f8c519c287d9dd9b/test/async/timeout.rb)
  - [`guides/tasks/readme.md`](https://github.com/socketry/async/blob/e8ecf5804802143f58983dc3f8c519c287d9dd9b/guides/tasks/readme.md)
  - [`guides/scheduler/readme.md`](https://github.com/socketry/async/blob/e8ecf5804802143f58983dc3f8c519c287d9dd9b/guides/scheduler/readme.md)
- **Trace:** Start at the public Async entry, follow Reactor and Scheduler binding into Task#run, greedy Fiber scheduling and suspension, then follow completion or failure into Promise resolution and task-tree consumption; branch through hierarchical or deferred cancellation and timeout injection, and close with task, scheduler, reactor, and timeout tests for causes, transient children, stale wakeups, interrupts, cleanup, and shutdown. Cancellation remains cooperative, timeout is delivered at an interruption point, io-event owns selector internals, and user-owned sockets or files still require ensure cleanup.

**Why this level:**

- **Language technique 4:** Advanced Fiber, scheduler, exception, block, and ensure mechanics recur, without enough distinct expert metaprogramming or reflection for 5.
- **Behavioral reasoning 5:** Scheduling, task and promise state, suspension, cancellation, timeout, reparenting, interruption, and teardown interact nonlocally.
- **Design span 4:** Multiple strong subsystem boundaries collaborate within one bounded cooperative-concurrency framework.
- **Constraint burden 5:** Lifecycle, scheduling, interruption, ownership, cleanup, and resource guarantees interact so local changes can fail across the task tree.
- **Placement:** The four scores 4/5/4/5 sum to 18; their arithmetic mean is 4.50 and rounds half-up to Level 5. Behavioral reasoning and constraint burden both score 5, satisfying the Level 5 guardrail. The published result is Level 5.

**License:** MIT ([evidence 1](https://github.com/socketry/async/blob/e8ecf5804802143f58983dc3f8c519c287d9dd9b/license.md))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository publishes the async gem and core runtime used by the Socketry ecosystem for cooperative concurrent services and I/O clients.

**Language evidence:** Task lifecycle, Fiber scheduling, promise state, cancellation, timeout behavior, tree ownership, and their direct tests are substantive first-party Ruby; io-event supplies selector internals outside the selected path.

**Coding relevance:**

Fibers, schedulers, and cooperative cancellation need only a short concurrency primer; the path teaches transferable structured concurrency, lifecycle state machines, promise resolution, exception injection, timeout cleanup, ownership, resource lifetime, and shutdown testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Task, Node, Promise, Scheduler, cancellation, and timeout responsibilities make lifecycle invariants explicit, and direct tests cover hard interruption and teardown cases. Two stale Task annotations describe a finished-to-cancelled transition and `:complete` status that implementation and tests correctly treat as a no-op and `:completed`; those annotations are excluded from the learning trace.
- **Architecture:** The audited architecture of the path beginning at `lib/async/task.rb` has these boundaries: public Async entry and Reactor, hierarchical Task and Node ownership, Scheduler and selector boundary, Promise result boundary, and cancellation and timeout operations.
- **Naming and idiom:** `lib/async/task.rb` and its supporting files use these characteristic Ruby mechanisms: Fiber scheduler integration, exception-based cooperative cancellation, block-scoped task construction, and Promise and task-tree abstractions.
- **Tests:** Direct tests in `test/async/task.rb`, `test/async/scheduler.rb`, `test/async/reactor.rb`, and `test/async/timeout.rb` cover these states and branches in the selected path: initialized, running, completed, failed, and cancelled tasks, hierarchical and deferred cancellation, suspension, resumption, timeout injection, and transient-child lifetime.
- **Documentation:** Task and scheduler guides explain the public lifecycle and cooperative model; the selected trace follows source and tests rather than the two stale Task status annotations, and cross-thread interruption retains a documented missed-wakeup window before scheduler sleep.
- **Traceability:** Start at the public Async entry, follow Reactor and Scheduler binding into Task#run, greedy Fiber scheduling and suspension, then follow completion or failure into Promise resolution and task-tree consumption; branch through hierarchical or deferred cancellation and timeout injection, and close with task, scheduler, reactor, and timeout tests for causes, transient children, stale wakeups, interrupts, cleanup, and shutdown. Cancellation remains cooperative, timeout is delivered at an interruption point, io-event owns selector internals, and user-owned sockets or files still require ensure cleanup.
- **Maintainability:** Changes to the path beginning at `lib/async/task.rb` are constrained by these audited guarantees: task-tree integrity and reparenting, one-shot result propagation, cancellation-cause preservation, interruption-point semantics, timer cleanup and stale-wakeup avoidance, and selector, worker, and user-resource shutdown.
- **Educational value:** Understand how Async creates a Fiber-backed child task, schedules and suspends it, propagates result or failure, and tears down its task tree under cancellation or timeout. Fibers, schedulers, and cooperative cancellation need only a short concurrency primer; the path teaches transferable structured concurrency, lifecycle state machines, promise resolution, exception injection, timeout cleanup, ownership, resource lifetime, and shutdown testing.

**Inspection record:** commit `e8ecf5804802143f58983dc3f8c519c287d9dd9b`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `lib/kernel/async.rb`, `lib/async/task.rb`, `lib/async/node.rb`, `lib/async/promise.rb`, `lib/async/cancel.rb`, `lib/async/timeout.rb`, `lib/async/scheduler.rb`, `lib/async/reactor.rb`, `test/async/task.rb`, `test/async/scheduler.rb`, `test/async/reactor.rb`, `test/async/timeout.rb`, `guides/tasks/readme.md`, `guides/scheduler/readme.md`, `license.md`. GitHub Linguist label: Ruby.

</details>

_Generated from `catalog/ruby.json`; do not edit by hand._

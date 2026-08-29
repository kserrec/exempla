# Ruby

5 qualified repositories. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

[← All languages](../README.md)

## Level 1

No qualified repository has been published at this level. Standards are not lowered to fill a slot.

## Level 2

### [ruby/pathname](https://github.com/ruby/pathname)

**Language 2 / Behavior 2 / Design 1 / Constraints 3 → Level 2**

An immutable object-oriented representation of filesystem paths from Ruby's standard library.

**Real-world evidence:** The repository publishes Ruby's pathname default gem and implements the Pathname API used throughout Ruby tooling and applications.

**Language evidence:** The path value object and nearly all path and filesystem behavior are Ruby under lib/, with a small C extension for selected primitives.

**Why study it:** Understand how Pathname.cleanpath normalizes a path lexically while preserving roots and optionally retaining components needed for symbolic-link safety. Path components, roots, separators, and symbolic-link preservation are familiar and self-contained; the path teaches transferable immutable value objects, normalization algorithms, platform compatibility, boundary-case design, and table-driven testing.

**What you can learn:**

- Study these transferable Ruby mechanisms in `lib/pathname_builtin.rb`: immutable value-object methods, component iteration and regular-expression helpers, and conventional private helper composition.
- Trace these states and branches from `lib/pathname_builtin.rb` through its selected supporting files: aggressive and conservative branches, localized component-stack state, and root and trailing-separator edge paths.
- Identify these architectural responsibilities in the path beginning at `lib/pathname_builtin.rb`: one lexical normalization component and one direct assertion matrix.
- Study these change constraints for the path beginning at `lib/pathname_builtin.rb`: relative and absolute root preservation, symbolic-link-safe conservative semantics, Unix, drive-letter, and UNC portability, and stable lexical output contracts.

**Prerequisites:**

- Before reading `lib/pathname_builtin.rb`, be comfortable with these mechanisms: immutable value-object methods, component iteration and regular-expression helpers, and conventional private helper composition.
- Lexical path normalization removes redundant separators and dot components without consulting the filesystem, while a conservative mode must avoid assumptions that could change symbolic-link meaning.

**Coding relevance:**

Path components, roots, separators, and symbolic-link preservation are familiar and self-contained; the path teaches transferable immutable value objects, normalization algorithms, platform compatibility, boundary-case design, and table-driven testing.

Required domain context:

- Lexical path normalization removes redundant separators and dot components without consulting the filesystem, while a conservative mode must avoid assumptions that could change symbolic-link meaning.

**Learning path:**

- **Goal:** Understand how Pathname.cleanpath normalizes a path lexically while preserving roots and optionally retaining components needed for symbolic-link safety.
- **Start here:** [`lib/pathname_builtin.rb`](https://github.com/ruby/pathname/blob/f0217bbd486b2f7d5c7de1ff3951c7422d42c761/lib/pathname_builtin.rb) — Begin with `lib/pathname_builtin.rb` because it exposes how Pathname.cleanpath normalizes a path lexically while preserving roots and optionally retaining components needed for symbolic-link safety.
- **Then read:**
  - [`lib/pathname.rb`](https://github.com/ruby/pathname/blob/f0217bbd486b2f7d5c7de1ff3951c7422d42c761/lib/pathname.rb)
  - [`test/pathname/test_pathname.rb`](https://github.com/ruby/pathname/blob/f0217bbd486b2f7d5c7de1ff3951c7422d42c761/test/pathname/test_pathname.rb)
- **Trace:** Start at Pathname#cleanpath in lib/pathname_builtin.rb, branch into cleanpath_aggressive or cleanpath_conservative, follow component-stack, prefix, root, and separator handling, then close the behavior with the aggressive and conservative defassert matrices. Read lib/pathname.rb only for loading and the small additional APIs; the catalog's original loader was not the promised normalization implementation.

**Why this level:**

- **Language technique 2:** The path uses common professional Ruby collection, object, and helper idioms without recurring metaprogramming.
- **Behavioral reasoning 2:** Meaningful branches and local mutable state remain easy to trace in one normalization routine.
- **Design span 1:** The behavior stays within a few methods in one focused implementation unit.
- **Constraint burden 3:** Several material compatibility and portability guarantees shape otherwise local normalization.
- **Placement:** The four scores 2/2/1/3 sum to 8; their arithmetic mean is 2.00 and rounds half-up to Level 2. The published result is Level 2.

**Quality-gate evidence:**

- **Source quality:** The immutable Pathname implementation separates aggressive and conservative normalization into small named methods, documents their filesystem-free contract, and closes it with an exhaustive assertion matrix covering empty, relative, rooted, dot, dot-dot, trailing-separator, drive, and UNC cases; the corrected implementation path is direct and maintainable.
- **Architecture:** The audited architecture of the path beginning at `lib/pathname_builtin.rb` has these boundaries: one lexical normalization component and one direct assertion matrix.
- **Naming and idiom:** `lib/pathname_builtin.rb` and its supporting files use these characteristic Ruby mechanisms: immutable value-object methods, component iteration and regular-expression helpers, and conventional private helper composition.
- **Tests:** Direct tests in `test/pathname/test_pathname.rb` cover these states and branches in the selected path: aggressive and conservative branches, localized component-stack state, and root and trailing-separator edge paths.
- **Documentation:** `lib/pathname_builtin.rb` and its selected supporting material document the contracts needed to understand how Pathname.cleanpath normalizes a path lexically while preserving roots and optionally retaining components needed for symbolic-link safety.
- **Traceability:** Start at Pathname#cleanpath in lib/pathname_builtin.rb, branch into cleanpath_aggressive or cleanpath_conservative, follow component-stack, prefix, root, and separator handling, then close the behavior with the aggressive and conservative defassert matrices. Read lib/pathname.rb only for loading and the small additional APIs; the catalog's original loader was not the promised normalization implementation.
- **Maintainability:** Changes to the path beginning at `lib/pathname_builtin.rb` are constrained by these audited guarantees: relative and absolute root preservation, symbolic-link-safe conservative semantics, Unix, drive-letter, and UNC portability, and stable lexical output contracts.
- **Educational value:** Understand how Pathname.cleanpath normalizes a path lexically while preserving roots and optionally retaining components needed for symbolic-link safety. Path components, roots, separators, and symbolic-link preservation are familiar and self-contained; the path teaches transferable immutable value objects, normalization algorithms, platform compatibility, boundary-case design, and table-driven testing.

**Inspection record:** commit `f0217bbd486b2f7d5c7de1ff3951c7422d42c761`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `lib/pathname_builtin.rb`, `lib/pathname.rb`, `test/pathname/test_pathname.rb`, `COPYING`, `BSDL`. GitHub Linguist label: Ruby.

**License:** Ruby OR BSD-2-Clause ([evidence 1](https://github.com/ruby/pathname/blob/f0217bbd486b2f7d5c7de1ff3951c7422d42c761/COPYING), [evidence 2](https://github.com/ruby/pathname/blob/f0217bbd486b2f7d5c7de1ff3951c7422d42c761/BSDL))

## Level 3

### [jekyll/jekyll](https://github.com/jekyll/jekyll)

**Language 3 / Behavior 3 / Design 3 / Constraints 4 → Level 3**

A static-site generator that transforms Markdown, Liquid templates, data, assets, and configuration into a deployable website.

**Real-world evidence:** The repository publishes the Jekyll gem and command-line tool used for blogs, documentation, and GitHub Pages workflows.

**Language evidence:** Site discovery, collections, front matter, rendering, plugins, incremental regeneration, destination writing, and CLI behavior are Ruby under lib/.

**Why study it:** Understand how Jekyll transforms one source document through Liquid, converters, hooks, nested layouts, and incremental dependency recording into generated output. Markdown, Liquid, front matter, and layouts need only a short orientation; the selected renderer path teaches transferable staged pipelines, strategy selection, hooks, mutable transformation state, cycle protection, dependency tracking, error propagation, and integration testing.

**What you can learn:**

- Study these transferable Ruby mechanisms in `lib/jekyll/renderer.rb`: converter strategy and reduction pipeline, hook and plugin framework idioms, and Liquid payload and document abstractions.
- Trace these states and branches from `lib/jekyll/renderer.rb` through its selected supporting files: ordered mutable render phases, hook and converter error propagation, nested layout state and cycle detection, and incremental dependency updates.
- Identify these architectural responsibilities in the path beginning at `lib/jekyll/renderer.rb`: document and Convertible boundary, Renderer pipeline, Liquid and converter plugins, and layout and Regenerator boundaries.
- Study these change constraints for the path beginning at `lib/jekyll/renderer.rb`: template and converter plugin compatibility, strict Liquid options and error reporting, layout-cycle and data-merging correctness, and output extension and incremental rebuild consistency.

**Prerequisites:**

- Before reading `lib/jekyll/renderer.rb`, be comfortable with these mechanisms: converter strategy and reduction pipeline, hook and plugin framework idioms, and Liquid payload and document abstractions.
- A static-site document may pass through a template engine, one or more markup converters, nested layouts, hooks, and an incremental-build dependency tracker before being written.

**Coding relevance:**

Markdown, Liquid, front matter, and layouts need only a short orientation; the selected renderer path teaches transferable staged pipelines, strategy selection, hooks, mutable transformation state, cycle protection, dependency tracking, error propagation, and integration testing.

Required domain context:

- A static-site document may pass through a template engine, one or more markup converters, nested layouts, hooks, and an incremental-build dependency tracker before being written.

**Learning path:**

- **Goal:** Understand how Jekyll transforms one source document through Liquid, converters, hooks, nested layouts, and incremental dependency recording into generated output.
- **Start here:** [`lib/jekyll/renderer.rb`](https://github.com/jekyll/jekyll/blob/74d751339d3e534aa51d5d7b0640e9bd743509e4/lib/jekyll/renderer.rb) — Begin with `lib/jekyll/renderer.rb` because it exposes how Jekyll transforms one source document through Liquid, converters, hooks, nested layouts, and incremental dependency recording into generated output.
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

**Quality-gate evidence:**

- **Source quality:** Renderer methods expose each transformation phase directly, Convertible supplies a clear public bridge, and Regenerator records incremental dependencies; document, generated-site, and site tests observe template data, converter output, layouts, destinations, hooks, and generated files, while the README and code comments orient the learner. No test/test_renderer.rb exists at the pin, so only verified integration tests close the path.
- **Architecture:** The audited architecture of the path beginning at `lib/jekyll/renderer.rb` has these boundaries: document and Convertible boundary, Renderer pipeline, Liquid and converter plugins, and layout and Regenerator boundaries.
- **Naming and idiom:** `lib/jekyll/renderer.rb` and its supporting files use these characteristic Ruby mechanisms: converter strategy and reduction pipeline, hook and plugin framework idioms, and Liquid payload and document abstractions.
- **Tests:** Direct tests in `test/test_document.rb`, `test/test_generated_site.rb`, and `test/test_site.rb` cover these states and branches in the selected path: ordered mutable render phases, hook and converter error propagation, nested layout state and cycle detection, and incremental dependency updates.
- **Documentation:** `lib/jekyll/renderer.rb` and its selected supporting material document the contracts needed to understand how Jekyll transforms one source document through Liquid, converters, hooks, nested layouts, and incremental dependency recording into generated output.
- **Traceability:** Start at Renderer#run, follow payload preparation and pre-render hooks into render_document, then follow optional Liquid rendering, ordered converter reduction, post-convert hooks, nested layout rendering with cycle detection, and Regenerator dependency recording; connect Convertible#do_layout to the public document lifecycle and close with document, generated-site, and site integration tests. The catalog's Site#process start was a broader composition root, and there is no pinned test/test_renderer.rb.
- **Maintainability:** Changes to the path beginning at `lib/jekyll/renderer.rb` are constrained by these audited guarantees: template and converter plugin compatibility, strict Liquid options and error reporting, layout-cycle and data-merging correctness, and output extension and incremental rebuild consistency.
- **Educational value:** Understand how Jekyll transforms one source document through Liquid, converters, hooks, nested layouts, and incremental dependency recording into generated output. Markdown, Liquid, front matter, and layouts need only a short orientation; the selected renderer path teaches transferable staged pipelines, strategy selection, hooks, mutable transformation state, cycle protection, dependency tracking, error propagation, and integration testing.

**Inspection record:** commit `74d751339d3e534aa51d5d7b0640e9bd743509e4`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `lib/jekyll/renderer.rb`, `lib/jekyll/convertible.rb`, `lib/jekyll/regenerator.rb`, `test/test_document.rb`, `test/test_generated_site.rb`, `test/test_site.rb`, `LICENSE`. GitHub Linguist label: Ruby.

**License:** MIT ([evidence 1](https://github.com/jekyll/jekyll/blob/74d751339d3e534aa51d5d7b0640e9bd743509e4/LICENSE))

### [ruby/tempfile](https://github.com/ruby/tempfile)

**Language 2 / Behavior 3 / Design 2 / Constraints 4 → Level 3**

Ruby's standard temporary-file library, providing secure creation plus explicit and automatic cleanup lifecycles.

**Real-world evidence:** The repository publishes the tempfile default gem used by Ruby applications and the Ruby standard library.

**Language evidence:** Temporary-file creation, permissions, cleanup, delegation, and lifecycle behavior are implemented in Ruby under lib/.

**Why study it:** Understand how Tempfile.create securely opens a temporary file and guarantees deterministic close and unlink behavior around a caller block. Temporary-file permissions and unlink behavior need only a short explanation; the selected block-based path teaches transferable resource ownership, secure creation, exception-safe cleanup, cross-platform fallback, API design, and focused behavioral testing.

**What you can learn:**

- Study these transferable Ruby mechanisms in `lib/tempfile.rb`: block-scoped resource ownership, keyword forwarding and conventional exception cleanup, and ordinary class and file composition.
- Trace these states and branches from `lib/tempfile.rb` through its selected supporting files: create, yield, close, and unlink lifecycle, cleanup after normal return or exception, and anonymous and platform-specific fallback branches.
- Identify these architectural responsibilities in the path beginning at `lib/tempfile.rb`: one public temporary-file component, standard-library name-generation and File boundaries, and one direct behavioral test suite.
- Study these change constraints for the path beginning at `lib/tempfile.rb`: race-resistant name creation and restrictive permissions, exception-safe close and unlink guarantees, Windows, POSIX, and anonymous-file differences, and stable public cleanup semantics.

**Prerequisites:**

- Before reading `lib/tempfile.rb`, be comfortable with these mechanisms: block-scoped resource ownership, keyword forwarding and conventional exception cleanup, and ordinary class and file composition.
- A temporary file must be created without a name race, opened with restrictive permissions, and removed after its owner finishes using it.

**Coding relevance:**

Temporary-file permissions and unlink behavior need only a short explanation; the selected block-based path teaches transferable resource ownership, secure creation, exception-safe cleanup, cross-platform fallback, API design, and focused behavioral testing.

Required domain context:

- A temporary file must be created without a name race, opened with restrictive permissions, and removed after its owner finishes using it.

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

**Quality-gate evidence:**

- **Source quality:** The compact implementation names creation and cleanup responsibilities directly, documents explicit versus automatic cleanup, and has focused tests for block success and failure, restrictive permissions, path traversal, anonymous files, unlink behavior, platform differences, and finalizer fallback; the main Tempfile.create trace remains readable from public API through ensure cleanup to a direct test.
- **Architecture:** The audited architecture of the path beginning at `lib/tempfile.rb` has these boundaries: one public temporary-file component, standard-library name-generation and File boundaries, and one direct behavioral test suite.
- **Naming and idiom:** `lib/tempfile.rb` and its supporting files use these characteristic Ruby mechanisms: block-scoped resource ownership, keyword forwarding and conventional exception cleanup, and ordinary class and file composition.
- **Tests:** Direct tests in `test/test_tempfile.rb` cover these states and branches in the selected path: create, yield, close, and unlink lifecycle, cleanup after normal return or exception, and anonymous and platform-specific fallback branches.
- **Documentation:** `lib/tempfile.rb` and its selected supporting material document the contracts needed to understand how Tempfile.create securely opens a temporary file and guarantees deterministic close and unlink behavior around a caller block.
- **Traceability:** Start at Tempfile.create, follow Dir::Tmpname.create into restrictive File.open, then follow the yielded File through the ensure branch that closes and unlinks it; close with block, traversal, anonymous-file, permission, and cleanup tests. Compare FinalizerManager only as the fallback used by the older object lifecycle, not as machinery required by the main block-and-ensure trace.
- **Maintainability:** Changes to the path beginning at `lib/tempfile.rb` are constrained by these audited guarantees: race-resistant name creation and restrictive permissions, exception-safe close and unlink guarantees, Windows, POSIX, and anonymous-file differences, and stable public cleanup semantics.
- **Educational value:** Understand how Tempfile.create securely opens a temporary file and guarantees deterministic close and unlink behavior around a caller block. Temporary-file permissions and unlink behavior need only a short explanation; the selected block-based path teaches transferable resource ownership, secure creation, exception-safe cleanup, cross-platform fallback, API design, and focused behavioral testing.

**Inspection record:** commit `344da5e29e3215691209223249ebd64e66dff6b8`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `lib/tempfile.rb`, `test/test_tempfile.rb`, `COPYING`, `BSDL`. GitHub Linguist label: Ruby.

**License:** Ruby OR BSD-2-Clause ([evidence 1](https://github.com/ruby/tempfile/blob/344da5e29e3215691209223249ebd64e66dff6b8/COPYING), [evidence 2](https://github.com/ruby/tempfile/blob/344da5e29e3215691209223249ebd64e66dff6b8/BSDL))

## Level 4

### [rubocop/rubocop](https://github.com/rubocop/rubocop)

**Language 4 / Behavior 4 / Design 4 / Constraints 5 → Level 4**

A configurable Ruby static analyzer and formatter built around independently selectable cops.

**Real-world evidence:** The repository publishes the RuboCop gem and executable used to lint, format, and enforce Ruby project conventions.

**Language evidence:** Configuration, target discovery, AST inspection, cop dispatch, offense reporting, autocorrection, caching, formatters, and CLI orchestration are Ruby under lib/ and exe/.

**Why study it:** Understand how RuboCop inspects one Ruby file, dispatches AST callbacks to configured cops, combines corrections, and repeats autocorrection safely until the source stabilizes or a cycle is detected. AST nodes, source ranges, and lint rules need only a short programming-oriented explanation; the path teaches transferable visitor dispatch, runtime callback generation, plugin lifecycles, edit collation, conflict detection, fixed-point iteration, caching, error isolation, and contract testing.

**What you can learn:**

- Study these transferable Ruby mechanisms in `lib/rubocop/runner.rb`: runtime class_eval generation of AST callback methods, reflection and callback discovery, cop DSL and plugin framework conventions, and dynamic dispatch over node and restriction maps.
- Trace these states and branches from `lib/rubocop/runner.rb` through its selected supporting files: AST event propagation through many cops, repeated autocorrection to a fixed point, overlap, conflict, and cycle handling, and cop error isolation and cache paths.
- Identify these architectural responsibilities in the path beginning at `lib/rubocop/runner.rb`: Runner orchestration and reporting, Team cop coordination, Commissioner visitor dispatch, Base extension lifecycle and Corrector edits, and configuration, cache, and formatter policies.
- Study these change constraints for the path beginning at `lib/rubocop/runner.rb`: exact source ranges, encodings, and syntax preservation, overlapping-edit and semantic-correction safety, termination and infinite-cycle detection, and configuration, plugin, target-Ruby, cache, and formatter compatibility.

**Prerequisites:**

- Before reading `lib/rubocop/runner.rb`, be comfortable with these mechanisms: runtime class_eval generation of AST callback methods, reflection and callback discovery, cop DSL and plugin framework conventions, and dynamic dispatch over node and restriction maps.
- A lint cop receives callbacks while an abstract syntax tree is visited, reports source-range offenses, and may propose edits that must be combined and repeatedly applied until stable.

**Coding relevance:**

AST nodes, source ranges, and lint rules need only a short programming-oriented explanation; the path teaches transferable visitor dispatch, runtime callback generation, plugin lifecycles, edit collation, conflict detection, fixed-point iteration, caching, error isolation, and contract testing.

Required domain context:

- A lint cop receives callbacks while an abstract syntax tree is visited, reports source-range offenses, and may propose edits that must be combined and repeatedly applied until stable.

**Learning path:**

- **Goal:** Understand how RuboCop inspects one Ruby file, dispatches AST callbacks to configured cops, combines corrections, and repeats autocorrection safely until the source stabilizes or a cycle is detected.
- **Start here:** [`lib/rubocop/runner.rb`](https://github.com/rubocop/rubocop/blob/8b85bafb041debc1f3a955663a99fa384a9d24f6/lib/rubocop/runner.rb) — Begin with `lib/rubocop/runner.rb` because it exposes how RuboCop inspects one Ruby file, dispatches AST callbacks to configured cops, combines corrections, and repeats autocorrection safely until the source stabilizes or a cycle is detected.
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

**Quality-gate evidence:**

- **Source quality:** Runner, Team, Commissioner, Base, and Corrector expose recognizable orchestration, dispatch, extension, and edit responsibilities; direct specs cover offenses, cop errors, callback lifecycles, overlapping corrections, conflicting cops, infinite correction cycles, caching, formatter behavior, syntax failures, and autocorrect output, while project documentation explains purpose and configuration.
- **Architecture:** The audited architecture of the path beginning at `lib/rubocop/runner.rb` has these boundaries: Runner orchestration and reporting, Team cop coordination, Commissioner visitor dispatch, Base extension lifecycle and Corrector edits, and configuration, cache, and formatter policies.
- **Naming and idiom:** `lib/rubocop/runner.rb` and its supporting files use these characteristic Ruby mechanisms: runtime class_eval generation of AST callback methods, reflection and callback discovery, cop DSL and plugin framework conventions, and dynamic dispatch over node and restriction maps.
- **Tests:** Direct tests in `spec/rubocop/runner_spec.rb` and `spec/rubocop/cop/team_spec.rb` cover these states and branches in the selected path: AST event propagation through many cops, repeated autocorrection to a fixed point, overlap, conflict, and cycle handling, and cop error isolation and cache paths.
- **Documentation:** `lib/rubocop/runner.rb` and its selected supporting material document the contracts needed to understand how RuboCop inspects one Ruby file, dispatches AST callbacks to configured cops, combines corrections, and repeats autocorrection safely until the source stabilizes or a cycle is detected.
- **Traceability:** Start at Runner#process_file and file_offenses, follow the correction loop into Team#investigate, Commissioner-generated node callbacks, Base offense registration, and Corrector edits, then return through Team's corrector collation and conflict handling to Runner's convergence or infinite-loop result; close with Runner and Team specs.
- **Maintainability:** Changes to the path beginning at `lib/rubocop/runner.rb` are constrained by these audited guarantees: exact source ranges, encodings, and syntax preservation, overlapping-edit and semantic-correction safety, termination and infinite-cycle detection, and configuration, plugin, target-Ruby, cache, and formatter compatibility.
- **Educational value:** Understand how RuboCop inspects one Ruby file, dispatches AST callbacks to configured cops, combines corrections, and repeats autocorrection safely until the source stabilizes or a cycle is detected. AST nodes, source ranges, and lint rules need only a short programming-oriented explanation; the path teaches transferable visitor dispatch, runtime callback generation, plugin lifecycles, edit collation, conflict detection, fixed-point iteration, caching, error isolation, and contract testing.

**Inspection record:** commit `8b85bafb041debc1f3a955663a99fa384a9d24f6`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `lib/rubocop/runner.rb`, `lib/rubocop/cop/team.rb`, `lib/rubocop/cop/commissioner.rb`, `lib/rubocop/cop/base.rb`, `lib/rubocop/cop/corrector.rb`, `spec/rubocop/runner_spec.rb`, `spec/rubocop/cop/team_spec.rb`, `LICENSE.txt`. GitHub Linguist label: Ruby.

**License:** MIT ([evidence 1](https://github.com/rubocop/rubocop/blob/8b85bafb041debc1f3a955663a99fa384a9d24f6/LICENSE.txt))

### [sidekiq/sidekiq](https://github.com/sidekiq/sidekiq)

**Language 3 / Behavior 5 / Design 4 / Constraints 5 → Level 4**

A multithreaded background-job processor for Ruby applications backed by Redis.

**Real-world evidence:** The project publishes the Sidekiq gem and executable used to run durable asynchronous work for Ruby applications.

**Language evidence:** Job fetching, execution, middleware, retries, scheduling, capsules, Redis coordination, process lifecycle, and the monitoring UI are Ruby under lib/ and web/.

**Why study it:** Understand how Sidekiq owns one fetched job through middleware and execution, records retryable failure, acknowledges completed work, and preserves unfinished work during shutdown. Queue and at-least-once semantics need only a short explanation; the path teaches transferable threaded processing, ownership, middleware, retries, acknowledgement, shutdown coordination, failure recovery, observability, and concurrency testing.

**What you can learn:**

- Study these transferable Ruby mechanisms in `lib/sidekiq/processor.rb`: middleware block composition, dynamic worker class resolution and framework conventions, and exception wrapper and configuration abstractions.
- Trace these states and branches from `lib/sidekiq/processor.rb` through its selected supporting files: concurrent processor and fetched-work ownership, global and local retry recovery, middleware and worker failure timing, acknowledgement versus preservation, and quiet and forced-shutdown coordination.
- Identify these architectural responsibilities in the path beginning at `lib/sidekiq/processor.rb`: processor and fetch boundary, retry and dead-job lifecycle, middleware extension chain, manager shutdown coordination, and Redis-backed job state and observability.
- Study these change constraints for the path beginning at `lib/sidekiq/processor.rb`: at-least-once delivery and no-loss shutdown; duplicate-tolerant acknowledgement semantics; retry payload, original-argument, and scheduling compatibility; and thread safety, deadlines, middleware, and error reporting.

**Prerequisites:**

- Before reading `lib/sidekiq/processor.rb`, be comfortable with these mechanisms: middleware block composition, dynamic worker class resolution and framework conventions, and exception wrapper and configuration abstractions.
- A background worker fetches a job, may execute it at least once, records failure for retry, acknowledges completed work, and must preserve in-progress work during shutdown.

**Coding relevance:**

Queue and at-least-once semantics need only a short explanation; the path teaches transferable threaded processing, ownership, middleware, retries, acknowledgement, shutdown coordination, failure recovery, observability, and concurrency testing.

Required domain context:

- A background worker fetches a job, may execute it at least once, records failure for retry, acknowledges completed work, and must preserve in-progress work during shutdown.

**Learning path:**

- **Goal:** Understand how Sidekiq owns one fetched job through middleware and execution, records retryable failure, acknowledges completed work, and preserves unfinished work during shutdown.
- **Start here:** [`lib/sidekiq/processor.rb`](https://github.com/sidekiq/sidekiq/blob/1bb4aa06e5aa178a114a5e855f9f3d5c24f6c61b/lib/sidekiq/processor.rb) — Begin with `lib/sidekiq/processor.rb` because it exposes how Sidekiq owns one fetched job through middleware and execution, records retryable failure, acknowledges completed work, and preserves unfinished work during shutdown.
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

**Quality-gate evidence:**

- **Source quality:** Processor, retry, middleware, and manager responsibilities are explicit and documented in the internals guide; direct tests cover fetch and execution exceptions, middleware before and after failures, skip behavior, acknowledgement, original argument preservation, retry delegation, shutdown deadlines, quieting, and work recovery, making the production lifecycle traceable despite its nonlocal guarantees.
- **Architecture:** The audited architecture of the path beginning at `lib/sidekiq/processor.rb` has these boundaries: processor and fetch boundary, retry and dead-job lifecycle, middleware extension chain, manager shutdown coordination, and Redis-backed job state and observability.
- **Naming and idiom:** `lib/sidekiq/processor.rb` and its supporting files use these characteristic Ruby mechanisms: middleware block composition, dynamic worker class resolution and framework conventions, and exception wrapper and configuration abstractions.
- **Tests:** Direct tests in `test/processor_test.rb` and `test/manager_test.rb` cover these states and branches in the selected path: concurrent processor and fetched-work ownership, global and local retry recovery, middleware and worker failure timing, acknowledgement versus preservation, and quiet and forced-shutdown coordination.
- **Documentation:** `lib/sidekiq/processor.rb` and its selected supporting material document the contracts needed to understand how Sidekiq owns one fetched job through middleware and execution, records retryable failure, acknowledges completed work, and preserves unfinished work during shutdown.
- **Traceability:** Start at Processor#process_one and the fetched unit of work, follow dispatch through global and local JobRetry wrappers, the server middleware chain, worker resolution and execution, then follow the completed flag into acknowledgement or preservation; use Manager shutdown to see deadlines and in-flight ownership, and close with processor and manager tests plus the internals contract.
- **Maintainability:** Changes to the path beginning at `lib/sidekiq/processor.rb` are constrained by these audited guarantees: at-least-once delivery and no-loss shutdown, duplicate-tolerant acknowledgement semantics, retry payload, original arguments, and scheduling compatibility, and thread safety, deadlines, middleware, and error reporting.
- **Educational value:** Understand how Sidekiq owns one fetched job through middleware and execution, records retryable failure, acknowledges completed work, and preserves unfinished work during shutdown. Queue and at-least-once semantics need only a short explanation; the path teaches transferable threaded processing, ownership, middleware, retries, acknowledgement, shutdown coordination, failure recovery, observability, and concurrency testing.

**Inspection record:** commit `1bb4aa06e5aa178a114a5e855f9f3d5c24f6c61b`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `lib/sidekiq/processor.rb`, `lib/sidekiq/job_retry.rb`, `lib/sidekiq/middleware/chain.rb`, `lib/sidekiq/manager.rb`, `test/processor_test.rb`, `test/manager_test.rb`, `docs/internals.md`, `LICENSE.txt`. GitHub Linguist label: Ruby.

**License:** LGPL-3.0-only ([evidence 1](https://github.com/sidekiq/sidekiq/blob/1bb4aa06e5aa178a114a5e855f9f3d5c24f6c61b/LICENSE.txt))

## Level 5

No qualified repository has been published at this level. Standards are not lowered to fill a slot.

_Generated from `catalog/ruby.json`; do not edit by hand._

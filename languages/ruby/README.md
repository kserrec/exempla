# Ruby

8 qualified repositories. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

[← All languages](../README.md)

## Level 1

No qualified repository has been published at this level. Standards are not lowered to fill a slot.

## Level 2

### [ruby/base64](https://github.com/ruby/base64)

**Language 1 / Behavior 2 / Design 1 / Constraints 3 → Level 2**

Ruby's standard Base64 library for printable encoding of binary data, including strict and URL-safe variants.

**Real-world evidence:** The repository publishes the base64 default gem used by Ruby applications and the Ruby standard library.

**Language evidence:** The published encoding and decoding APIs, URL-safe adaptation, padding repair, and direct behavioral tests are first-party Ruby in lib/ and test/.

**Why study it:** Understand how Ruby's Base64 wrappers turn one binary string into MIME, strict, or URL-safe text and decode permissive, strict, or padding-repaired input. Base64 needs only a short byte-to-text explanation; the path teaches transferable standard-library delegation, API variants, input policy, padding normalization, character translation, compatibility constraints, and boundary testing.

**What you can learn:**

- Study these transferable Ruby mechanisms in `lib/base64.rb`: module-function APIs, Array and String pack/unpack delegation, and keyword arguments with localized string transformation.
- Trace these states and branches from `lib/base64.rb` through its selected supporting files: MIME versus strict behavior, padded versus unpadded URL-safe encoding, and URL-safe decoding with conditional padding repair.
- Identify these architectural responsibilities in the path beginning at `lib/base64.rb`: one focused public module, Ruby's binary pack/unpack primitive boundary, and one direct behavioral test suite.
- Study these change constraints for the path beginning at `lib/base64.rb`: RFC-2045 and RFC-4648 alphabet differences, strict versus permissive input, exact padding and newline contracts, and binary-string round trips.

**Prerequisites:**

- Before reading `lib/base64.rb`, be comfortable with these mechanisms: module-function APIs, Array and String pack/unpack delegation, and keyword arguments with localized string transformation.
- Base64 maps each group of three input bytes to four printable characters; variants differ in alphabet, padding, newlines, and whether malformed input is rejected.

**Coding relevance:**

Base64 needs only a short byte-to-text explanation; the path teaches transferable standard-library delegation, API variants, input policy, padding normalization, character translation, compatibility constraints, and boundary testing.

Required domain context:

- Base64 maps each group of three input bytes to four printable characters; variants differ in alphabet, padding, newlines, and whether malformed input is rejected.

**Learning path:**

- **Goal:** Understand how Ruby's Base64 wrappers turn one binary string into MIME, strict, or URL-safe text and decode permissive, strict, or padding-repaired input.
- **Start here:** [`lib/base64.rb`](https://github.com/ruby/base64/blob/9a0eb5cada60ae4b044aae8c5a7cad0ae6d131e6/lib/base64.rb) — Begin with `lib/base64.rb` because it contains the complete MIME, strict, and URL-safe encoding and decoding path.
- **Then read:**
  - [`test/base64/test_base64.rb`](https://github.com/ruby/base64/blob/9a0eb5cada60ae4b044aae8c5a7cad0ae6d131e6/test/base64/test_base64.rb)
  - [`README.md`](https://github.com/ruby/base64/blob/9a0eb5cada60ae4b044aae8c5a7cad0ae6d131e6/README.md)
  - [`sig/base64.rbs`](https://github.com/ruby/base64/blob/9a0eb5cada60ae4b044aae8c5a7cad0ae6d131e6/sig/base64.rbs)
  - [`test_sig/test_base64.rb`](https://github.com/ruby/base64/blob/9a0eb5cada60ae4b044aae8c5a7cad0ae6d131e6/test_sig/test_base64.rb)
- **Trace:** Start with strict_encode64 and strict_decode64 at Ruby's pack/unpack boundary, compare encode64 and decode64's MIME newline and permissive-input policy, then follow urlsafe_encode64 through optional padding removal and alphabet translation and urlsafe_decode64 through conditional padding repair, reverse translation, and strict decoding; close with the direct empty, binary, malformed-padding, and unpadded URL-safe tests. The repository wraps Ruby's runtime codec rather than implementing bit-level Base64, and urlsafe_decode64 accepts valid-length standard `+` and `/` alphabet input despite stronger wording in its RDoc.

**Why this level:**

- **Language technique 1:** The complete path uses ordinary Ruby functions and string operations around a standard primitive boundary.
- **Behavioral reasoning 2:** Several visible variants and boundary branches must be compared, but state remains local and linear.
- **Design span 1:** The behavior is deliberately concentrated in six small methods and one direct test file.
- **Constraint burden 3:** Multiple externally visible encoding, padding, newline, and malformed-input contracts shape otherwise tiny methods.
- **Placement:** The four scores 1/2/1/3 sum to 7; their arithmetic mean is 1.75 and rounds half-up to Level 2. The published result is Level 2.

**Quality-gate evidence:**

- **Source quality:** Six compact methods delegate the bit-level transform to Ruby's documented pack/unpack primitives and keep URL-safe alphabet and padding policy explicit; direct tests cover empty input, binary bytes, strict malformed input, padded and unpadded variants, and round trips.
- **Architecture:** The audited architecture of the path beginning at `lib/base64.rb` has these boundaries: one focused public module, Ruby's binary pack/unpack primitive boundary, and one direct behavioral test suite.
- **Naming and idiom:** `lib/base64.rb` and its supporting files use these characteristic Ruby mechanisms: module-function APIs, Array and String pack/unpack delegation, and keyword arguments with localized string transformation.
- **Tests:** Direct tests in `test/base64/test_base64.rb` cover these states and branches in the selected path: MIME versus strict behavior, padded versus unpadded URL-safe encoding, and URL-safe decoding with conditional padding repair.
- **Documentation:** Inline API documentation, type signatures, and README examples distinguish the three method pairs, padding, newlines, and malformed-input behavior. The URL-safe decoder RDoc overstates alphabet rejection: valid-length standard `+` and `/` input is accepted, as source and tests show.
- **Traceability:** Start with strict_encode64 and strict_decode64 at Ruby's pack/unpack boundary, compare encode64 and decode64's MIME newline and permissive-input policy, then follow urlsafe_encode64 through optional padding removal and alphabet translation and urlsafe_decode64 through conditional padding repair, reverse translation, and strict decoding; close with the direct empty, binary, malformed-padding, and unpadded URL-safe tests. The repository wraps Ruby's runtime codec rather than implementing bit-level Base64, and urlsafe_decode64 accepts valid-length standard `+` and `/` alphabet input despite stronger wording in its RDoc.
- **Maintainability:** Changes to the path beginning at `lib/base64.rb` are constrained by these audited guarantees: RFC-2045 and RFC-4648 alphabet differences, strict versus permissive input, exact padding and newline contracts, and binary-string round trips.
- **Educational value:** Understand how Ruby's Base64 wrappers turn one binary string into MIME, strict, or URL-safe text and decode permissive, strict, or padding-repaired input. Base64 needs only a short byte-to-text explanation; the path teaches transferable standard-library delegation, API variants, input policy, padding normalization, character translation, compatibility constraints, and boundary testing.

**Inspection record:** commit `9a0eb5cada60ae4b044aae8c5a7cad0ae6d131e6`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `lib/base64.rb`, `test/base64/test_base64.rb`, `README.md`, `sig/base64.rbs`, `test_sig/test_base64.rb`, `COPYING`, `BSDL`. GitHub Linguist label: Ruby.

**License:** Ruby OR BSD-2-Clause ([evidence 1](https://github.com/ruby/base64/blob/9a0eb5cada60ae4b044aae8c5a7cad0ae6d131e6/COPYING), [evidence 2](https://github.com/ruby/base64/blob/9a0eb5cada60ae4b044aae8c5a7cad0ae6d131e6/BSDL))

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

### [ruby-concurrency/concurrent-ruby](https://github.com/ruby-concurrency/concurrent-ruby)

**Language 4 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

A production concurrency toolkit whose promise framework composes asynchronous tasks, dependency graphs, executors, and single-assignment results.

**Real-world evidence:** The repository publishes the concurrent-ruby gem used by Ruby applications for futures, promises, executors, atomic primitives, and other concurrency abstractions.

**Language evidence:** The selected promise graph, executor handoff, atomic state, fallback synchronization, documentation, and direct behavioral specs are first-party Ruby; optional native atomic backends are not required by this path.

**Why study it:** Understand how one concurrent-ruby future is scheduled, fulfilled or rejected exactly once, and propagated through dependent then or rescue work to callbacks and waiting callers. Futures and executors need only a short concurrency primer; the path teaches transferable asynchronous state machines, atomic single assignment, callback races, executor handoff, dependency graphs, error recovery, timeouts, and blocking boundaries.

**What you can learn:**

- Study these transferable Ruby mechanisms in `lib/concurrent-ruby/concurrent/promises.rb`: blocks and mixins as asynchronous APIs, private state and promise subclasses, and atomic accessors, callbacks, aliases, and executor dispatch.
- Trace these states and branches from `lib/concurrent-ruby/concurrent/promises.rb` through its selected supporting files: pending, reserved, fulfilled, and rejected resolution, then versus rescue propagation, callback registration racing with resolution, and delayed graph touch and blocking wait paths.
- Identify these architectural responsibilities in the path beginning at `lib/concurrent-ruby/concurrent/promises.rb`: public factories and Future API, immutable result-state objects, blocked promise graph, executor boundary, and atomic and blocking synchronization boundary.
- Study these change constraints for the path beginning at `lib/concurrent-ruby/concurrent/promises.rb`: exactly-once resolution, callback visibility under races, rejection and non-StandardError propagation, executor inheritance, timeout and spurious-wakeup correctness, and multiple Ruby runtime backends.

**Prerequisites:**

- Before reading `lib/concurrent-ruby/concurrent/promises.rb`, be comfortable with these mechanisms: blocks and mixins as asynchronous APIs, private state and promise subclasses, and atomic accessors, callbacks, aliases, and executor dispatch.
- A future represents one eventual fulfillment or rejection; an executor runs dependent work, and atomic single assignment prevents two competing resolutions from both winning.

**Coding relevance:**

Futures and executors need only a short concurrency primer; the path teaches transferable asynchronous state machines, atomic single assignment, callback races, executor handoff, dependency graphs, error recovery, timeouts, and blocking boundaries.

Required domain context:

- A future represents one eventual fulfillment or rejection; an executor runs dependent work, and atomic single assignment prevents two competing resolutions from both winning.

**Learning path:**

- **Goal:** Understand how one concurrent-ruby future is scheduled, fulfilled or rejected exactly once, and propagated through dependent then or rescue work to callbacks and waiting callers.
- **Start here:** [`lib/concurrent-ruby/concurrent/promises.rb`](https://github.com/ruby-concurrency/concurrent-ruby/blob/0b88d5ff75f69b3740c8f0868e76f833cb2fd45d/lib/concurrent-ruby/concurrent/promises.rb) — Begin with `lib/concurrent-ruby/concurrent/promises.rb` because it exposes the complete public factory, dependency, resolution, callback, and observation path.
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

**Quality-gate evidence:**

- **Source quality:** The large promises implementation is dense but deliberately partitioned into public futures, immutable states, blocked promise types, and resolution helpers; direct specs close its core races and lifecycle. CamelCase final ivars are an explicit synchronization convention rather than ordinary Ruby style.
- **Architecture:** The audited architecture of the path beginning at `lib/concurrent-ruby/concurrent/promises.rb` has these boundaries: public factories and Future API, immutable result-state objects, blocked promise graph, executor boundary, and atomic and blocking synchronization boundary.
- **Naming and idiom:** `lib/concurrent-ruby/concurrent/promises.rb` and its supporting files use these characteristic Ruby mechanisms: blocks and mixins as asynchronous APIs, private state and promise subclasses, and atomic accessors, callbacks, aliases, and executor dispatch.
- **Tests:** Direct specs in `spec/concurrent/promises_spec.rb` cover these states and branches in the selected path: pending, reserved, fulfilled, and rejected resolution, then versus rescue propagation, callback registration racing with resolution, and delayed graph touch and blocking wait paths.
- **Documentation:** The promise guide documents states, graphs, error paths, executor selection, callbacks, and blocking observation; its broad lock-free wording must be read with the source's mutex-backed atomic fallbacks and explicit Mutex/ConditionVariable waits.
- **Traceability:** Start at Promises.future and Future#then or #rescue, follow BlockedPromise dependency registration into ThenPromise or RescuePromise executor posting, then follow evaluate_to into the CAS-backed fulfilled or rejected state, callback draining, and wait or value! observation; close with direct promise specs for arguments, executors, callbacks, timeouts, branching, delay, rejection, reservation, duplicate assignment, and spurious wakeups. Mutex-backed atomic fallbacks and blocking waits mean the selected path must not be described as universally lock-free.
- **Maintainability:** Changes to the path beginning at `lib/concurrent-ruby/concurrent/promises.rb` are constrained by these audited guarantees: exactly-once resolution, callback visibility under races, rejection and non-StandardError propagation, executor inheritance, timeout and spurious-wakeup correctness, and multiple Ruby runtime backends. The 2,184-line core file and runtime backend selection increase review scope.
- **Educational value:** Understand how one concurrent-ruby future is scheduled, fulfilled or rejected exactly once, and propagated through dependent then or rescue work to callbacks and waiting callers. Futures and executors need only a short concurrency primer; the path teaches transferable asynchronous state machines, atomic single assignment, callback races, executor handoff, dependency graphs, error recovery, timeouts, and blocking boundaries.

**Inspection record:** commit `0b88d5ff75f69b3740c8f0868e76f833cb2fd45d`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `lib/concurrent-ruby/concurrent/promises.rb`, `lib/concurrent-ruby/concurrent/configuration.rb`, `lib/concurrent-ruby/concurrent/synchronization/object.rb`, `lib/concurrent-ruby/concurrent/collection/lock_free_stack.rb`, `lib/concurrent-ruby/concurrent/atomic/atomic_reference.rb`, `lib/concurrent-ruby/concurrent/atomic_reference/mutex_atomic.rb`, `lib/concurrent-ruby/concurrent/atomic/atomic_fixnum.rb`, `lib/concurrent-ruby/concurrent/atomic/mutex_atomic_fixnum.rb`, `spec/concurrent/promises_spec.rb`, `docs-source/promises-main.md`, `docs-source/promises.in.md`, `LICENSE.txt`. GitHub Linguist label: Ruby.

**License:** MIT ([evidence 1](https://github.com/ruby-concurrency/concurrent-ruby/blob/0b88d5ff75f69b3740c8f0868e76f833cb2fd45d/LICENSE.txt))

### [socketry/async](https://github.com/socketry/async)

**Language 4 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

A composable fiber-based asynchronous I/O framework with structured task trees, cancellation, timeouts, and Ruby's Fiber scheduler integration.

**Real-world evidence:** The repository publishes the async gem and core runtime used by the Socketry ecosystem for cooperative concurrent services and I/O clients.

**Language evidence:** Task lifecycle, Fiber scheduling, promise state, cancellation, timeout behavior, tree ownership, and their direct tests are substantive first-party Ruby; io-event supplies selector internals outside the selected path.

**Why study it:** Understand how Async creates a Fiber-backed child task, schedules and suspends it, propagates result or failure, and tears down its task tree under cancellation or timeout. Fibers, schedulers, and cooperative cancellation need only a short concurrency primer; the path teaches transferable structured concurrency, lifecycle state machines, promise resolution, exception injection, timeout cleanup, ownership, resource lifetime, and shutdown testing.

**What you can learn:**

- Study these transferable Ruby mechanisms in `lib/async/task.rb`: Fiber scheduler integration, exception-based cooperative cancellation, block-scoped task construction, and Promise and task-tree abstractions.
- Trace these states and branches from `lib/async/task.rb` through its selected supporting files: initialized, running, completed, failed, and cancelled tasks, hierarchical and deferred cancellation, suspension, resumption, timeout injection, and transient-child lifetime.
- Identify these architectural responsibilities in the path beginning at `lib/async/task.rb`: public Async entry and Reactor, hierarchical Task and Node ownership, Scheduler and selector boundary, Promise result boundary, and cancellation and timeout operations.
- Study these change constraints for the path beginning at `lib/async/task.rb`: task-tree integrity and reparenting, one-shot result propagation, cancellation-cause preservation, interruption-point semantics, timer cleanup and stale-wakeup avoidance, and selector, worker, and user-resource shutdown.

**Prerequisites:**

- Before reading `lib/async/task.rb`, be comfortable with these mechanisms: Fiber scheduler integration, exception-based cooperative cancellation, block-scoped task construction, and Promise and task-tree abstractions.
- Ruby's Fiber scheduler cooperatively suspends tasks around blocking operations; child tasks form an ownership tree, and cancellation is delivered at interruption points rather than preemptively killing arbitrary work.

**Coding relevance:**

Fibers, schedulers, and cooperative cancellation need only a short concurrency primer; the path teaches transferable structured concurrency, lifecycle state machines, promise resolution, exception injection, timeout cleanup, ownership, resource lifetime, and shutdown testing.

Required domain context:

- Ruby's Fiber scheduler cooperatively suspends tasks around blocking operations; child tasks form an ownership tree, and cancellation is delivered at interruption points rather than preemptively killing arbitrary work.

**Learning path:**

- **Goal:** Understand how Async creates a Fiber-backed child task, schedules and suspends it, propagates result or failure, and tears down its task tree under cancellation or timeout.
- **Start here:** [`lib/async/task.rb`](https://github.com/socketry/async/blob/e8ecf5804802143f58983dc3f8c519c287d9dd9b/lib/async/task.rb) — Begin with `lib/async/task.rb` because it exposes the task state machine, Fiber execution, child creation, result propagation, cancellation, and finish lifecycle.
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

**Quality-gate evidence:**

- **Source quality:** Task, Node, Promise, Scheduler, cancellation, and timeout responsibilities make lifecycle invariants explicit, and direct tests cover hard interruption and teardown cases. Two stale Task annotations describe a finished-to-cancelled transition and `:complete` status that implementation and tests correctly treat as a no-op and `:completed`; those annotations are excluded from the learning trace.
- **Architecture:** The audited architecture of the path beginning at `lib/async/task.rb` has these boundaries: public Async entry and Reactor, hierarchical Task and Node ownership, Scheduler and selector boundary, Promise result boundary, and cancellation and timeout operations.
- **Naming and idiom:** `lib/async/task.rb` and its supporting files use these characteristic Ruby mechanisms: Fiber scheduler integration, exception-based cooperative cancellation, block-scoped task construction, and Promise and task-tree abstractions.
- **Tests:** Direct tests in `test/async/task.rb`, `test/async/scheduler.rb`, `test/async/reactor.rb`, and `test/async/timeout.rb` cover these states and branches in the selected path: initialized, running, completed, failed, and cancelled tasks, hierarchical and deferred cancellation, suspension, resumption, timeout injection, and transient-child lifetime.
- **Documentation:** Task and scheduler guides explain the public lifecycle and cooperative model; the selected trace follows source and tests rather than the two stale Task status annotations, and cross-thread interruption retains a documented missed-wakeup window before scheduler sleep.
- **Traceability:** Start at the public Async entry, follow Reactor and Scheduler binding into Task#run, greedy Fiber scheduling and suspension, then follow completion or failure into Promise resolution and task-tree consumption; branch through hierarchical or deferred cancellation and timeout injection, and close with task, scheduler, reactor, and timeout tests for causes, transient children, stale wakeups, interrupts, cleanup, and shutdown. Cancellation remains cooperative, timeout is delivered at an interruption point, io-event owns selector internals, and user-owned sockets or files still require ensure cleanup.
- **Maintainability:** Changes to the path beginning at `lib/async/task.rb` are constrained by these audited guarantees: task-tree integrity and reparenting, one-shot result propagation, cancellation-cause preservation, interruption-point semantics, timer cleanup and stale-wakeup avoidance, and selector, worker, and user-resource shutdown.
- **Educational value:** Understand how Async creates a Fiber-backed child task, schedules and suspends it, propagates result or failure, and tears down its task tree under cancellation or timeout. Fibers, schedulers, and cooperative cancellation need only a short concurrency primer; the path teaches transferable structured concurrency, lifecycle state machines, promise resolution, exception injection, timeout cleanup, ownership, resource lifetime, and shutdown testing.

**Inspection record:** commit `e8ecf5804802143f58983dc3f8c519c287d9dd9b`, reviewed 2026-08-29 by Codex, independent Codex reviewer. Files sampled: `lib/kernel/async.rb`, `lib/async/task.rb`, `lib/async/node.rb`, `lib/async/promise.rb`, `lib/async/cancel.rb`, `lib/async/timeout.rb`, `lib/async/scheduler.rb`, `lib/async/reactor.rb`, `test/async/task.rb`, `test/async/scheduler.rb`, `test/async/reactor.rb`, `test/async/timeout.rb`, `guides/tasks/readme.md`, `guides/scheduler/readme.md`, `license.md`. GitHub Linguist label: Ruby.

**License:** MIT ([evidence 1](https://github.com/socketry/async/blob/e8ecf5804802143f58983dc3f8c519c287d9dd9b/license.md))

_Generated from `catalog/ruby.json`; do not edit by hand._

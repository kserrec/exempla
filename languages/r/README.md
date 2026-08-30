# R

8 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

**Source legend:** Production software is built primarily for real users or systems. Educational exemplars are complete teaching-oriented software and may appear only at Levels 1 and 2.

[← All languages](../README.md)

## Level 1 — First real code

### [r-lib/scales](https://github.com/r-lib/scales)

**Language 1 / Behavior 1 / Design 1 / Constraints 1 → Level 1**

**Source:** Production software

The production scales package replaces negative and positive infinity with the two ends of a supplied range while preserving finite values and missing values.

**Why study it:** Read a small vectorized R function whose two logical selections correspond exactly to two assignments and one mixed-input test.

**Prerequisites:**

- The global novice R baseline: functions, default arguments, vectors, logical indexing, assignment, Inf, NA, and focused testthat expectations.
- force(range) evaluates the supplied range before the two assignments; it does not alter the replacement rule.

**Concepts this path develops:**

- Using logical masks for targeted vector replacement.
- Treating negative and positive infinity as two distinct boundary cases.
- Preserving unrelated and missing values during vectorized mutation.

**What you can learn:**

- Select vector positions by comparing values with negative or positive infinity.
- Replace the two selected groups with the corresponding range endpoints.
- Verify that ordinary finite values and NA remain unchanged.

**Learning path:**

- **Goal:** Understand how scales replaces only infinite values with explicit lower and upper limits.
- **Start here:** [`R/bounds.R`](https://github.com/r-lib/scales/blob/04fc3331af14da0d5ca1919f37c6c35d6fc512bb/R/bounds.R) — The documentation and complete oob_squish_infinite implementation appear together in this file.
- **Then read:**
  - [`tests/testthat/test-bounds.R`](https://github.com/r-lib/scales/blob/04fc3331af14da0d5ca1919f37c6c35d6fc512bb/tests/testthat/test-bounds.R)
  - [`man/oob.Rd`](https://github.com/r-lib/scales/blob/04fc3331af14da0d5ca1919f37c6c35d6fc512bb/man/oob.Rd)
  - [`README.md`](https://github.com/r-lib/scales/blob/04fc3331af14da0d5ca1919f37c6c35d6fc512bb/README.md)
  - [`DESCRIPTION`](https://github.com/r-lib/scales/blob/04fc3331af14da0d5ca1919f37c6c35d6fc512bb/DESCRIPTION)
  - [`LICENSE.md`](https://github.com/r-lib/scales/blob/04fc3331af14da0d5ca1919f37c6c35d6fc512bb/LICENSE.md)
- **Trace:** Evaluate range, select entries equal to -Inf and assign range[1], select entries equal to Inf and assign range[2], return x, then compare every element of the mixed test vector with its expected result.

**Why this level:**

- **Language technique 1:** The path uses standard novice R vector selection and replacement with a default argument.
- **Behavioral reasoning 1:** Two visible masks fully determine the local synchronous result.
- **Design span 1:** One source function and one focused test expectation contain the complete contract.
- **Constraint burden 1:** The function has two explicit exceptional values and otherwise preserves its input vector.
- **Novice accessibility floor 1:** All selected behavior is standard novice vector manipulation; force needs one local sentence and can be ignored when predicting the outputs.
  - **Central concepts:** vectors; logical comparisons; indexed replacement; infinite and missing values
  - **Incidental concepts:** eagerly evaluating range with force
- **Placement:** The four scores 1/1/1/1 produce rubric Level 1. Novice accessibility floor 1 preserves published Level 1.

**License:** MIT ([evidence 1](https://github.com/r-lib/scales/blob/04fc3331af14da0d5ca1919f37c6c35d6fc512bb/LICENSE.md))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** scales is a maintained R package for mapping data to perceptual properties, and its documented out-of-bounds functions are installed public APIs.

**Language evidence:** oob_squish_infinite, its package documentation, and the direct testthat expectation are first-party R; GitHub labels the repository R.

**Coding relevance:**

Logical indexing, selective replacement, boundary values, and mixed-input tests are general R data-processing techniques.

No specialist domain context is required.

**Eight-part quality gate:**

- **Source quality:** The two masks and assignments expose the complete behavior directly, without loops or helper indirection.
- **Architecture:** The function lives with the package's related out-of-bounds policies and remains independently readable.
- **Naming and idiom:** oob_squish_infinite and range communicate the policy, while logical indexing is idiomatic vectorized R.
- **Tests:** One direct expectation covers -Inf, finite values below and above the range, an interior value, both endpoints, NA, and Inf.
- **Documentation:** Roxygen source documentation and the generated oob manual page distinguish this function from the package's other out-of-bounds policies.
- **Traceability:** The first and final expected elements exercise the two assignments; every middle element verifies preservation.
- **Maintainability:** The two replacement rules are separate and symmetrical, making changes to either boundary easy to isolate.
- **Educational value:** The path demonstrates useful production vectorization through a seven-element example a novice can predict by hand.

**Inspection record:** commit `04fc3331af14da0d5ca1919f37c6c35d6fc512bb`, inspected 2026-08-30. Review passes: Codex 85% Level 1 investigation; Codex resumed-session source verification. Files inspected: `R/bounds.R`, `tests/testthat/test-bounds.R`, `man/oob.Rd`, `README.md`, `DESCRIPTION`, `LICENSE.md`. GitHub Linguist label: R.

</details>

## Level 2 — Guided real-world patterns

### [r-lib/scales](https://github.com/r-lib/scales)

**Language 2 / Behavior 2 / Design 1 / Constraints 2 → Level 2**

**Source:** Production software

A public scales transformation that maps numeric vectors into a requested output range, preserves missing values, and gives constant inputs the output midpoint.

**Why study it:** Follow a compact S3 generic into one numeric method that combines vector arithmetic with explicit missing-value and zero-range behavior.

**Short context:**

- Rescaling changes numeric values from one minimum-and-maximum interval to another; no plotting theory is needed for the selected path.

**Prerequisites:**

- The global novice R baseline: vectors, functions, default arguments, indexing, missing values, and testthat expectations.
- An S3 generic chooses a method from the input class; linear rescaling subtracts the input minimum, divides by input width, then applies the output width and minimum.

**Concepts this path develops:**

- Separating a public S3 generic from its numeric implementation.
- Expressing an interval transformation through vectorized arithmetic.
- Defining stable missing-value and zero-width-range outcomes.

**What you can learn:**

- Dispatch a public operation to a type-specific S3 method.
- Map every numeric value from one interval into another with vectorized arithmetic.
- Protect constant and missing inputs with an explicit midpoint branch.

**Learning path:**

- **Goal:** Understand how scales rescale maps numeric vectors between intervals while preserving NA and defining constant-input output.
- **Start here:** [`R/bounds.R`](https://github.com/r-lib/scales/blob/04fc3331af14da0d5ca1919f37c6c35d6fc512bb/R/bounds.R) — The generic and numeric method show dispatch, default input range, the zero-range branch, and the complete transformation formula together.
- **Then read:**
  - [`tests/testthat/test-bounds.R`](https://github.com/r-lib/scales/blob/04fc3331af14da0d5ca1919f37c6c35d6fc512bb/tests/testthat/test-bounds.R)
  - [`man/rescale.Rd`](https://github.com/r-lib/scales/blob/04fc3331af14da0d5ca1919f37c6c35d6fc512bb/man/rescale.Rd)
  - [`README.md`](https://github.com/r-lib/scales/blob/04fc3331af14da0d5ca1919f37c6c35d6fc512bb/README.md)
- **Trace:** Call rescale, dispatch through UseMethod to rescale.numeric, derive the finite input range, return output midpoints for a zero-width input or output while preserving NA, otherwise apply the interval formula, then match ordinary mixed-sign, missing, and constant-input expectations in test-bounds.R.

**Why this level:**

- **Language technique 2:** S3 dispatch and vectorized transformations are common professional R idioms central to the public API.
- **Behavioral reasoning 2:** Several input classes of outcome matter, but the complete numeric behavior stays in one short method.
- **Design span 1:** The selected numeric contract is contained in a public generic-method pair and direct tests.
- **Constraint burden 2:** Routine numerical API edge guarantees shape the method without requiring specialist mathematics or plotting architecture.
- **Novice accessibility floor 2:** A short S3 and interval-formula primer makes the numeric examples and edge cases predictable; no separate statistics or graphics course is required.
  - **Central concepts:** S3 generic dispatch; linear interval rescaling; zero-range and missing-value policy
  - **Incidental concepts:** other Date, time, integer64, and AsIs methods outside the selected numeric trace
- **Placement:** The four scores 2/2/1/2 produce rubric Level 2. Novice accessibility floor 2 preserves published Level 2.

**License:** MIT ([evidence 1](https://github.com/r-lib/scales/blob/04fc3331af14da0d5ca1919f37c6c35d6fc512bb/LICENSE.md))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** scales is a maintained R package for mapping data to perceptual properties, and rescale is a documented installed API used by plotting and data applications.

**Language evidence:** The rescale generic, numeric method, package documentation, and direct testthat cases are first-party R; GitHub labels the repository R.

**Coding relevance:**

Type dispatch, vector transformations, degenerate-input policy, and direct boundary tests transfer to ordinary data and application code.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The method states its exceptional branch and transformation formula directly, with no hidden mutation or generated code.
- **Architecture:** A small public generic delegates to type methods, while one focused test file specifies the shared behavior.
- **Naming and idiom:** x, to, from, zero_range, and rescale.numeric match established R and interval vocabulary.
- **Tests:** Direct numeric cases cover a mixed-sign vector, NA preservation, and constant inputs; adjacent cases verify additional type methods outside the selected numeric trace.
- **Documentation:** Generated package documentation defines both ranges, gives runnable examples, and identifies every published method.
- **Traceability:** The ordinary formula, zero-range return, and NA branch each map to explicit testthat expectations.
- **Maintainability:** The generic-method split and concentrated boundary cases make type extensions and numerical changes easy to review.
- **Educational value:** The path introduces idiomatic R dispatch through a familiar numeric transformation with concrete edge policy.

**Inspection record:** commit `04fc3331af14da0d5ca1919f37c6c35d6fc512bb`, inspected 2026-08-30. Review passes: Codex Level 2 language-breadth investigation; Codex pinned-source verification. Files inspected: `R/bounds.R`, `tests/testthat/test-bounds.R`, `man/rescale.Rd`, `README.md`, `DESCRIPTION`, `LICENSE.md`. GitHub Linguist label: R.

</details>

## Level 3 — Intermediate production software

### [r-lib/withr](https://github.com/r-lib/withr)

**Language 4 / Behavior 3 / Design 2 / Constraints 3 → Level 3**

**Source:** Production software

A library for running code with temporary changes to global process state and reliably restoring that state afterward.

**Why study it:** Understand how withr generates scoped wrappers that evaluate code under temporary state and reliably restore the previous state. Temporary-state vocabulary is familiar; the bounded generated-wrapper path teaches substitute and eval, delayed cleanup, dynamic wrapper generation, option capture, error-safe restoration, and nested scope behavior.

**Short context:**

- A with_* wrapper temporarily changes process or session state, evaluates user code, and restores the previous value on exit.

**Prerequisites:**

- Basic familiarity with R functions, vectors and lists, environments, S3 objects at a basic level, conditions, and testthat tests.
- A with_* wrapper temporarily changes process or session state, evaluates user code, and restores the previous value on exit.

**Concepts this path develops:**

- Substitute and caller-environment evaluation.
- Captured, changed, evaluating, restoring, and restored states.
- Prior state must restore on success and error.

**What you can learn:**

- Study these transferable R mechanisms in `R/with_.R`: substitute and caller-environment evaluation, programmatic wrapper generation, and deferred cleanup callbacks.
- Trace these states and branches from `R/with_.R` through its selected supporting files: captured, changed, evaluating, restoring, and restored states, normal, nested, and error exits, and visible and invisible result propagation.
- Identify these architectural responsibilities in the path beginning at `R/with_.R`: wrapper generator, representative option implementation, and direct restoration tests.
- Study these change constraints for the path beginning at `R/with_.R`: prior state must restore on success and error, nested scopes must restore in stack order, and evaluation environment and result visibility must remain correct.

**Learning path:**

- **Goal:** Understand how withr generates scoped wrappers that evaluate code under temporary state and reliably restore the previous state.
- **Start here:** [`R/with_.R`](https://github.com/r-lib/withr/blob/d82e4bc2d69a34f044ad205210e26207bfb8f3e0/R/with_.R) — Begin with `R/with_.R` because it exposes how withr generates scoped wrappers that evaluate code under temporary state and reliably restore the previous state.
- **Then read:**
  - [`R/options.R`](https://github.com/r-lib/withr/blob/d82e4bc2d69a34f044ad205210e26207bfb8f3e0/R/options.R)
  - [`tests/testthat/test-with.R`](https://github.com/r-lib/withr/blob/d82e4bc2d69a34f044ad205210e26207bfb8f3e0/tests/testthat/test-with.R)
- **Trace:** Start with the wrapper generator capturing expressions and cleanup callbacks, follow a representative option change through deferred restoration and evaluation in the caller environment, then examine nesting and error exits; close with focused tests for generated wrappers and restoration.

**Why this level:**

- **Language technique 4:** Advanced R metaprogramming recurs throughout generated with_* wrappers.
- **Behavioral reasoning 3:** Several related scoped-state transitions recur within a bounded restoration lifecycle.
- **Design span 2:** A small set of cohesive pieces covers generated wrappers and cleanup.
- **Constraint burden 3:** Restoration and evaluation guarantees recur, but remain locally contained.
- **Placement:** The four scores 4/3/2/3 sum to 12; their arithmetic mean is 3.00 and rounds half-up to Level 3. The published result is Level 3.

**License:** MIT ([evidence 1](https://github.com/r-lib/withr/blob/d82e4bc2d69a34f044ad205210e26207bfb8f3e0/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository publishes the withr CRAN package used by packages, tests, scripts, and tools that must scope side effects safely.

**Language evidence:** Temporary state setters, dynamic function construction, deferred cleanup, resource helpers, and integrations are implemented in R.

**Coding relevance:**

Temporary-state vocabulary is familiar; the bounded generated-wrapper path teaches substitute and eval, delayed cleanup, dynamic wrapper generation, option capture, error-safe restoration, and nested scope behavior.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** R/with_.R defines the wrapper generator and restoration structure, options.R supplies a representative state family, and test-with.R directly checks generated wrappers, nesting, errors, visibility, environments, and restoration.
- **Architecture:** The audited architecture of the path beginning at `R/with_.R` has these boundaries: wrapper generator, representative option implementation, and direct restoration tests.
- **Naming and idiom:** `R/with_.R` and its supporting files use these characteristic R mechanisms: substitute and caller-environment evaluation, programmatic wrapper generation, and deferred cleanup callbacks.
- **Tests:** Direct tests in `tests/testthat/test-with.R` cover these states and branches in the selected path: captured, changed, evaluating, restoring, and restored states, normal, nested, and error exits, and visible and invisible result propagation.
- **Documentation:** `R/with_.R` and its selected supporting material document the contracts needed to understand how withr generates scoped wrappers that evaluate code under temporary state and reliably restore the previous state.
- **Traceability:** Start with the wrapper generator capturing expressions and cleanup callbacks, follow a representative option change through deferred restoration and evaluation in the caller environment, then examine nesting and error exits; close with focused tests for generated wrappers and restoration.
- **Maintainability:** Changes to the path beginning at `R/with_.R` are constrained by these audited guarantees: prior state must restore on success and error, nested scopes must restore in stack order, and evaluation environment and result visibility must remain correct.
- **Educational value:** Understand how withr generates scoped wrappers that evaluate code under temporary state and reliably restore the previous state. Temporary-state vocabulary is familiar; the bounded generated-wrapper path teaches substitute and eval, delayed cleanup, dynamic wrapper generation, option capture, error-safe restoration, and nested scope behavior.

**Inspection record:** commit `d82e4bc2d69a34f044ad205210e26207bfb8f3e0`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `R/with_.R`, `R/options.R`, `tests/testthat/test-with.R`, `LICENSE`. GitHub Linguist label: R.

</details>

### [tidyverse/ggplot2](https://github.com/tidyverse/ggplot2)

**Language 4 / Behavior 2 / Design 2 / Constraints 3 → Level 3**

**Source:** Production software

A declarative graphics system that implements a layered grammar of data, aesthetics, scales, statistics, geometry, coordinates, faceting, guides, and themes.

**Why study it:** Understand how ggplot2 implements prototype inheritance and bound methods in R and uses that system for extensible plot components. Plot-component vocabulary is brief; the replacement path teaches prototype inheritance, parent-method dispatch, environment-backed objects, cloning, method binding, extension contracts, and direct tests without the full plot-build pipeline.

**Short context:**

- ggproto provides inheritance and method dispatch for ggplot2 components such as Geom prototypes.

**Prerequisites:**

- Basic familiarity with R functions, vectors and lists, environments, S3 objects at a basic level, conditions, and testthat tests.
- ggproto provides inheritance and method dispatch for ggplot2 components such as Geom prototypes.

**Concepts this path develops:**

- Environment-backed prototype objects.
- Local and inherited lookup.
- Lookup and parent dispatch must preserve receiver identity.

**What you can learn:**

- Study these transferable R mechanisms in `R/ggproto.R`: environment-backed prototype objects, dynamic method binding and parent dispatch, and custom printing, lookup, and cloning behavior.
- Trace these states and branches from `R/ggproto.R` through its selected supporting files: local and inherited lookup, field and method outcomes, and construction, copy, and error branches.
- Identify these architectural responsibilities in the path beginning at `R/ggproto.R`: ggproto core, representative Geom consumer, and direct object and layer tests.
- Study these change constraints for the path beginning at `R/ggproto.R`: lookup and parent dispatch must preserve receiver identity, methods and fields must remain distinguishable, and copying and extension contracts must avoid accidental shared mutation.

**Learning path:**

- **Goal:** Understand how ggplot2 implements prototype inheritance and bound methods in R and uses that system for extensible plot components.
- **Start here:** [`R/ggproto.R`](https://github.com/tidyverse/ggplot2/blob/6870419aa6e106c3580c45c81d5b688cb31758bd/R/ggproto.R) — Begin with `R/ggproto.R` because it exposes how ggplot2 implements prototype inheritance and bound methods in R and uses that system for extensible plot components.
- **Then read:**
  - [`R/geom-.R`](https://github.com/tidyverse/ggplot2/blob/6870419aa6e106c3580c45c81d5b688cb31758bd/R/geom-.R)
  - [`tests/testthat/test-ggproto.R`](https://github.com/tidyverse/ggplot2/blob/6870419aa6e106c3580c45c81d5b688cb31758bd/tests/testthat/test-ggproto.R)
  - [`tests/testthat/test-layer.R`](https://github.com/tidyverse/ggplot2/blob/6870419aa6e106c3580c45c81d5b688cb31758bd/tests/testthat/test-layer.R)
- **Trace:** Start with ggproto object construction and parent links, follow field lookup and bound method dispatch including parent-method calls, then inspect Geom as a representative extension contract; close with ggproto and layer tests for inheritance, copying, dispatch, errors, and integration.

**Why this level:**

- **Language technique 4:** Advanced R object-system and metaprogramming techniques recur across ggproto.
- **Behavioral reasoning 2:** A few related dispatch states recur without the nonlocal behavior of a full plot build.
- **Design span 2:** A compact core and one extension consumer form the bounded lesson.
- **Constraint burden 3:** Several inheritance and extension guarantees recur but remain locally testable.
- **Placement:** The four scores 4/2/2/3 sum to 11; their arithmetic mean is 2.75 and rounds half-up to Level 3. The published result is Level 3.

**License:** MIT ([evidence 1](https://github.com/tidyverse/ggplot2/blob/6870419aa6e106c3580c45c81d5b688cb31758bd/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository publishes the ggplot2 CRAN package used to create static visualizations and as a platform for a large extension ecosystem.

**Language evidence:** The grammar, plot object, build pipeline, layers, scales, coordinates, facets, guides, themes, geoms, stats, positions, and extension system are implemented in R.

**Coding relevance:**

Plot-component vocabulary is brief; the replacement path teaches prototype inheritance, parent-method dispatch, environment-backed objects, cloning, method binding, extension contracts, and direct tests without the full plot-build pipeline.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** R/ggproto.R contains the prototype system and dispatch helpers, geom-.R shows a representative extension consumer, and test-ggproto.R plus test-layer.R verify inheritance, parent calls, fields, methods, copying, errors, and integration with layers.
- **Architecture:** The audited architecture of the path beginning at `R/ggproto.R` has these boundaries: ggproto core, representative Geom consumer, and direct object and layer tests.
- **Naming and idiom:** `R/ggproto.R` and its supporting files use these characteristic R mechanisms: environment-backed prototype objects, dynamic method binding and parent dispatch, and custom printing, lookup, and cloning behavior.
- **Tests:** Direct tests in `tests/testthat/test-ggproto.R` and `tests/testthat/test-layer.R` cover these states and branches in the selected path: local and inherited lookup, field and method outcomes, and construction, copy, and error branches.
- **Documentation:** `R/ggproto.R` and its selected supporting material document the contracts needed to understand how ggplot2 implements prototype inheritance and bound methods in R and uses that system for extensible plot components.
- **Traceability:** Start with ggproto object construction and parent links, follow field lookup and bound method dispatch including parent-method calls, then inspect Geom as a representative extension contract; close with ggproto and layer tests for inheritance, copying, dispatch, errors, and integration.
- **Maintainability:** Changes to the path beginning at `R/ggproto.R` are constrained by these audited guarantees: lookup and parent dispatch must preserve receiver identity, methods and fields must remain distinguishable, and copying and extension contracts must avoid accidental shared mutation.
- **Educational value:** Understand how ggplot2 implements prototype inheritance and bound methods in R and uses that system for extensible plot components. Plot-component vocabulary is brief; the replacement path teaches prototype inheritance, parent-method dispatch, environment-backed objects, cloning, method binding, extension contracts, and direct tests without the full plot-build pipeline.

**Inspection record:** commit `6870419aa6e106c3580c45c81d5b688cb31758bd`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `R/ggproto.R`, `R/geom-.R`, `tests/testthat/test-ggproto.R`, `tests/testthat/test-layer.R`, `LICENSE`. GitHub Linguist label: R.

</details>

## Level 4 — Advanced

### [r-lib/testthat](https://github.com/r-lib/testthat)

**Language 4 / Behavior 4 / Design 3 / Constraints 4 → Level 4**

**Source:** Production software

R's xUnit-style testing framework, with expressive expectations, reporters, snapshots, package integration, and parallel execution.

**Why study it:** Understand how testthat evaluates one test block, turns expectations into structured conditions, and reports passing, failure, error, and skip outcomes. Testing vocabulary is familiar; the path teaches captured evaluation, condition signaling, expectation objects, reporter callbacks, nested contexts, failure and skip policy, and self-tests.

**Short context:**

- test_that evaluates a test block, records expectation conditions, and reports structured outcomes.

**Prerequisites:**

- Working familiarity with R functions, vectors and lists, environments, S3 objects at a basic level, conditions, and testthat tests, plus experience tracing behavior across several production files.
- test_that evaluates a test block, records expectation conditions, and reports structured outcomes.

**Concepts this path develops:**

- Captured expressions and caller environments.
- Starting, evaluating, expecting, reporting, and completing states.
- Conditions must be classified without swallowing unexpected errors.

**What you can learn:**

- Study these transferable R mechanisms in `R/test-that.R`: captured expressions and caller environments, custom condition signaling and handling, and R6-style reporter callback protocols.
- Trace these states and branches from `R/test-that.R` through its selected supporting files: starting, evaluating, expecting, reporting, and completing states, pass, failure, error, warning, skip, and cleanup branches, and nested block and reporter event ordering.
- Identify these architectural responsibilities in the path beginning at `R/test-that.R`: test block runner, expectation condition model, and reporter boundary and focused self-tests.
- Study these change constraints for the path beginning at `R/test-that.R`: conditions must be classified without swallowing unexpected errors, reporter events and nested contexts must remain ordered, and skip, failure, cleanup, and result visibility contracts must hold.

**Learning path:**

- **Goal:** Understand how testthat evaluates one test block, turns expectations into structured conditions, and reports passing, failure, error, and skip outcomes.
- **Start here:** [`R/test-that.R`](https://github.com/r-lib/testthat/blob/9b6f12b9f50c297b4b5f485f728a2a19305770eb/R/test-that.R) — Begin with `R/test-that.R` because it exposes how testthat evaluates one test block, turns expectations into structured conditions, and reports passing, failure, error, and skip outcomes.
- **Then read:**
  - [`R/expectation.R`](https://github.com/r-lib/testthat/blob/9b6f12b9f50c297b4b5f485f728a2a19305770eb/R/expectation.R)
  - [`R/reporter.R`](https://github.com/r-lib/testthat/blob/9b6f12b9f50c297b4b5f485f728a2a19305770eb/R/reporter.R)
  - [`tests/testthat/test-test-that.R`](https://github.com/r-lib/testthat/blob/9b6f12b9f50c297b4b5f485f728a2a19305770eb/tests/testthat/test-test-that.R)
  - [`tests/testthat/test-expectation.R`](https://github.com/r-lib/testthat/blob/9b6f12b9f50c297b4b5f485f728a2a19305770eb/tests/testthat/test-expectation.R)
- **Trace:** Start at test_that and its block evaluation, follow expectation signaling and condition capture into reporter lifecycle callbacks, then trace success, failure, error, skip, and cleanup outcomes; close with focused self-tests for blocks and expectation objects.

**Why this level:**

- **Language technique 4:** Advanced R evaluation and condition techniques recur across test execution.
- **Behavioral reasoning 4:** Several coupled execution and outcome states recur throughout a test block.
- **Design span 3:** A few cohesive components cover execution through observable reporting.
- **Constraint burden 4:** Condition, ordering, compatibility, and cleanup guarantees recur in ordinary test execution.
- **Placement:** The four scores 4/4/3/4 sum to 15; their arithmetic mean is 3.75 and rounds half-up to Level 4. The published result is Level 4.

**License:** MIT ([evidence 1](https://github.com/r-lib/testthat/blob/9b6f12b9f50c297b4b5f485f728a2a19305770eb/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository publishes the testthat CRAN package used to run and report automated tests for R packages and applications.

**Language evidence:** Test discovery and execution, expectations, conditions and restarts, reporters, snapshots, mocking, parallel workers, and package integration are implemented primarily in R.

**Coding relevance:**

Testing vocabulary is familiar; the path teaches captured evaluation, condition signaling, expectation objects, reporter callbacks, nested contexts, failure and skip policy, and self-tests.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** R/test-that.R is the actual block execution entry, expectation.R defines structured success and failure conditions, reporter.R exposes lifecycle callbacks, and direct test-that and expectation suites cover passing, failure, errors, skips, warnings, snapshots of results, and reporter interaction.
- **Architecture:** The audited architecture of the path beginning at `R/test-that.R` has these boundaries: test block runner, expectation condition model, and reporter boundary and focused self-tests.
- **Naming and idiom:** `R/test-that.R` and its supporting files use these characteristic R mechanisms: captured expressions and caller environments, custom condition signaling and handling, and R6-style reporter callback protocols.
- **Tests:** The direct suites `tests/testthat/test-test-that.R` and `tests/testthat/test-expectation.R` cover passing blocks, failures, errors, skips, warnings, result snapshots, and reporter interaction; `R/test-that.R` is the implementation under test, not a test file.
- **Documentation:** `R/test-that.R` and its selected supporting material document the contracts needed to understand how testthat evaluates one test block, turns expectations into structured conditions, and reports passing, failure, error, and skip outcomes.
- **Traceability:** Start at test_that and its block evaluation, follow expectation signaling and condition capture into reporter lifecycle callbacks, then trace success, failure, error, skip, and cleanup outcomes; close with focused self-tests for blocks and expectation objects.
- **Maintainability:** Changes to the path beginning at `R/test-that.R` are constrained by these audited guarantees: conditions must be classified without swallowing unexpected errors, reporter events and nested contexts must remain ordered, and skip, failure, cleanup, and result visibility contracts must hold.
- **Educational value:** Understand how testthat evaluates one test block, turns expectations into structured conditions, and reports passing, failure, error, and skip outcomes. Testing vocabulary is familiar; the path teaches captured evaluation, condition signaling, expectation objects, reporter callbacks, nested contexts, failure and skip policy, and self-tests.

**Inspection record:** commit `9b6f12b9f50c297b4b5f485f728a2a19305770eb`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `R/test-that.R`, `R/expectation.R`, `R/reporter.R`, `tests/testthat/test-test-that.R`, `tests/testthat/test-expectation.R`, `LICENSE`. GitHub Linguist label: R.

</details>

### [tidyverse/glue](https://github.com/tidyverse/glue)

**Language 4 / Behavior 3 / Design 3 / Constraints 4 → Level 4**

**Source:** Production software

A dependency-light string interpolation library that evaluates expressions inside customizable delimiters.

**Why study it:** Understand how glue_data scans an interpolation template, evaluates embedded R expressions, transforms values, and produces vectorized output. Interpolation vocabulary is immediate; the path teaches captured evaluation environments, parser callbacks, delimiter and escape state, transformer extension, vector recycling, missing values, and a C scanning boundary.

**Short context:**

- Glue scans template text, evaluates expressions between delimiters, transforms values, and combines vectorized output.

**Prerequisites:**

- Working familiarity with R functions, vectors and lists, environments, S3 objects at a basic level, conditions, and testthat tests, plus experience tracing behavior across several production files.
- Glue scans template text, evaluates expressions between delimiters, transforms values, and combines vectorized output.

**Concepts this path develops:**

- Captured environments and expression evaluation.
- Literal, expression, escaped delimiter, and quoted states.
- Escaping and delimiter state must remain exact.

**What you can learn:**

- Study these transferable R mechanisms in `R/glue.R`: captured environments and expression evaluation, transformer callback extension, and R-to-C scanner interface.
- Trace these states and branches from `R/glue.R` through its selected supporting files: literal, expression, escaped delimiter, and quoted states, evaluated, missing, null, vector, and error outcomes, and transform and output assembly phases.
- Identify these architectural responsibilities in the path beginning at `R/glue.R`: public R facade, transformer and utility layer, and native scanner and focused tests.
- Study these change constraints for the path beginning at `R/glue.R`: escaping and delimiter state must remain exact, evaluation must occur in the promised data and environment scope, and vector recycling, missing values, and errors must preserve output contracts.

**Learning path:**

- **Goal:** Understand how glue_data scans an interpolation template, evaluates embedded R expressions, transforms values, and produces vectorized output.
- **Start here:** [`R/glue.R`](https://github.com/tidyverse/glue/blob/da9c73f7a3de6a27f3103cb5bb2355820a4c3a6a/R/glue.R) — Begin with `R/glue.R` because it exposes how glue_data scans an interpolation template, evaluates embedded R expressions, transforms values, and produces vectorized output.
- **Then read:**
  - [`R/transformer.R`](https://github.com/tidyverse/glue/blob/da9c73f7a3de6a27f3103cb5bb2355820a4c3a6a/R/transformer.R)
  - [`R/utils.R`](https://github.com/tidyverse/glue/blob/da9c73f7a3de6a27f3103cb5bb2355820a4c3a6a/R/utils.R)
  - [`src/glue.c`](https://github.com/tidyverse/glue/blob/da9c73f7a3de6a27f3103cb5bb2355820a4c3a6a/src/glue.c)
  - [`tests/testthat/test-glue.R`](https://github.com/tidyverse/glue/blob/da9c73f7a3de6a27f3103cb5bb2355820a4c3a6a/tests/testthat/test-glue.R)
- **Trace:** Start at glue_data's data and environment setup, follow delimiters and callbacks into the transformer and C scanner, then trace value conversion, recycling, missing-value policy, trimming, and output construction; close with the focused glue tests.

**Why this level:**

- **Language technique 4:** Advanced R evaluation and native-boundary techniques recur across interpolation.
- **Behavioral reasoning 3:** Nontrivial parser and evaluation states recur, but remain bounded rather than advanced nonlocal Behavior 4.
- **Design span 3:** A few cohesive components cover template input through evaluated output.
- **Constraint burden 4:** Parsing, evaluation, vectorization, and extension guarantees recur in ordinary use.
- **Placement:** The four scores 4/3/3/4 sum to 14; their arithmetic mean is 3.50 and rounds half-up to Level 4. The published result is Level 4.

**License:** MIT ([evidence 1](https://github.com/tidyverse/glue/blob/da9c73f7a3de6a27f3103cb5bb2355820a4c3a6a/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository publishes the glue CRAN package for applications and packages that construct text, messages, SQL, and data-aware strings.

**Language evidence:** Expression capture and evaluation, transformers, quoting, SQL support, vector recycling, and the interpolation parser are implemented in R and C.

**Coding relevance:**

Interpolation vocabulary is immediate; the path teaches captured evaluation environments, parser callbacks, delimiter and escape state, transformer extension, vector recycling, missing values, and a C scanning boundary.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** R/glue.R defines glue_data and the public evaluation contract, transformer.R isolates expression evaluation, utils.R handles recycling and cleanup, src/glue.c implements the scanner state machine, and test-glue.R broadly covers delimiters, escapes, evaluation, vectors, missing values, transformers, and errors.
- **Architecture:** The audited architecture of the path beginning at `R/glue.R` has these boundaries: public R facade, transformer and utility layer, and native scanner and focused tests.
- **Naming and idiom:** `R/glue.R` and its supporting files use these characteristic R mechanisms: captured environments and expression evaluation, transformer callback extension, and R-to-C scanner interface.
- **Tests:** Direct tests in `tests/testthat/test-glue.R` cover these states and branches in the selected path: literal, expression, escaped delimiter, and quoted states, evaluated, missing, null, vector, and error outcomes, and transform and output assembly phases.
- **Documentation:** `R/glue.R` and its selected supporting material document the contracts needed to understand how glue_data scans an interpolation template, evaluates embedded R expressions, transforms values, and produces vectorized output.
- **Traceability:** Start at glue_data's data and environment setup, follow delimiters and callbacks into the transformer and C scanner, then trace value conversion, recycling, missing-value policy, trimming, and output construction; close with the focused glue tests.
- **Maintainability:** Changes to the path beginning at `R/glue.R` are constrained by these audited guarantees: escaping and delimiter state must remain exact, evaluation must occur in the promised data and environment scope, and vector recycling, missing values, and errors must preserve output contracts.
- **Educational value:** Understand how glue_data scans an interpolation template, evaluates embedded R expressions, transforms values, and produces vectorized output. Interpolation vocabulary is immediate; the path teaches captured evaluation environments, parser callbacks, delimiter and escape state, transformer extension, vector recycling, missing values, and a C scanning boundary.

**Inspection record:** commit `da9c73f7a3de6a27f3103cb5bb2355820a4c3a6a`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `R/glue.R`, `R/transformer.R`, `R/utils.R`, `src/glue.c`, `tests/testthat/test-glue.R`, `LICENSE`. GitHub Linguist label: R.

</details>

## Level 5 — Expert

### [nimble-dev/nimble](https://github.com/nimble-dev/nimble)

**Language 5 / Behavior 4 / Design 5 / Constraints 5 → Level 5**

**Source:** Production software

A programmable hierarchical-modeling system that compiles BUGS-style models and model-generic algorithms from R into customized C++.

**Why study it:** Understand how NIMBLE turns a typed arithmetic nimbleFunction into generated C++, compiles it within a project, and exposes the native result through an R interface. The selected compiler path needs typed arithmetic and native-interface vocabulary, not Bayesian or statistical expertise; it teaches custom AST and type processing, project compilation state, code generation, native registration, reflection, specialization, and R/C++ interoperability.

**Short context:**

- A nimbleFunction declares typed setup and run code that NIMBLE specializes, generates as C++, compiles, and exposes back to R.

**Prerequisites:**

- Strong working familiarity with R functions, vectors and lists, environments, S3 objects at a basic level, conditions, and testthat tests, plus experience tracing state, resources, or asynchronous control flow across many production files.
- A nimbleFunction declares typed setup and run code that NIMBLE specializes, generates as C++, compiles, and exposes back to R.

**Concepts this path develops:**

- Captured R code and custom type specialization.
- Declared, specialized, generated, compiling, loaded, callable, and failed states.
- R semantics and inferred types must map coherently to generated C++.

**What you can learn:**

- Study these transferable R mechanisms in `packages/nimble/R/nimbleFunction_core.R`: captured R code and custom type specialization, AST transformation and generated C++, and reflection and native R/C++ interface construction.
- Trace these states and branches from `packages/nimble/R/nimbleFunction_core.R` through its selected supporting files: declared, specialized, generated, compiling, loaded, callable, and failed states, setup and run separation, and type, code-generation, compiler, loading, and interface branches.
- Identify these architectural responsibilities in the path beginning at `packages/nimble/R/nimbleFunction_core.R`: nimbleFunction language surface, project and compilation coordinator, type and code-generation pipeline, native interface layer, and end-to-end interface tests.
- Study these change constraints for the path beginning at `packages/nimble/R/nimbleFunction_core.R`: R semantics and inferred types must map coherently to generated C++, generated declarations, compiled symbols, and R interfaces must agree, and project caching, compilation failure, loading, ownership, and cleanup must remain safe.

**Learning path:**

- **Goal:** Understand how NIMBLE turns a typed arithmetic nimbleFunction into generated C++, compiles it within a project, and exposes the native result through an R interface.
- **Start here:** [`packages/nimble/R/nimbleFunction_core.R`](https://github.com/nimble-dev/nimble/blob/0181166733112cdaaf4edf7d7b0817a8f03cbdac/packages/nimble/R/nimbleFunction_core.R) — Begin with `packages/nimble/R/nimbleFunction_core.R` because it exposes how NIMBLE turns a typed arithmetic nimbleFunction into generated C++, compiles it within a project, and exposes the native result through an R interface.
- **Then read:**
  - [`packages/nimble/R/nimbleProject.R`](https://github.com/nimble-dev/nimble/blob/0181166733112cdaaf4edf7d7b0817a8f03cbdac/packages/nimble/R/nimbleProject.R)
  - [`packages/nimble/R/nimbleFunction_compile.R`](https://github.com/nimble-dev/nimble/blob/0181166733112cdaaf4edf7d7b0817a8f03cbdac/packages/nimble/R/nimbleFunction_compile.R)
  - [`packages/nimble/R/genCpp_generateCpp.R`](https://github.com/nimble-dev/nimble/blob/0181166733112cdaaf4edf7d7b0817a8f03cbdac/packages/nimble/R/genCpp_generateCpp.R)
  - [`packages/nimble/R/cppInterfaces_nimbleFunctions.R`](https://github.com/nimble-dev/nimble/blob/0181166733112cdaaf4edf7d7b0817a8f03cbdac/packages/nimble/R/cppInterfaces_nimbleFunctions.R)
  - [`packages/nimble/tests/testthat/test-nimbleFunctionInterfaces.R`](https://github.com/nimble-dev/nimble/blob/0181166733112cdaaf4edf7d7b0817a8f03cbdac/packages/nimble/tests/testthat/test-nimbleFunctionInterfaces.R)
- **Trace:** Start with nimbleFunction setup and typed run declarations, follow specialization and type information into nimbleProject compilation state and generated C++, then trace compilation and native interface creation back to callable R objects; close with interface tests using typed arithmetic and ordinary compiled functions, without Bayesian model evidence.

**Why this level:**

- **Language technique 5:** Multiple expert R metaprogramming, compiler, and interoperation mechanisms recur throughout the path.
- **Behavioral reasoning 4:** Several advanced compiler lifecycle states recur, though the typed arithmetic trace is bounded below broad expert runtime behavior.
- **Design span 5:** Multiple major compiler and runtime-interface components coordinate end to end.
- **Constraint burden 5:** Expert semantic, type, generation, native ABI, lifecycle, and failure constraints recur throughout compilation.
- **Placement:** The four scores 5/4/5/5 sum to 19; their arithmetic mean is 4.75 and rounds half-up to Level 5. The published result is Level 5.

**License:** BSD-3-Clause OR GPL-2.0-or-later ([evidence 1](https://github.com/nimble-dev/nimble/blob/0181166733112cdaaf4edf7d7b0817a8f03cbdac/packages/nimble/DESCRIPTION), [evidence 2](https://github.com/nimble-dev/nimble/blob/0181166733112cdaaf4edf7d7b0817a8f03cbdac/packages/nimble/LICENSE), [evidence 3](https://github.com/nimble-dev/nimble/blob/0181166733112cdaaf4edf7d7b0817a8f03cbdac/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository publishes the NIMBLE CRAN package used to build and fit hierarchical models with MCMC, particle filtering, Laplace approximation, and custom statistical algorithms.

**Language evidence:** The BUGS-compatible modeling language, graph construction, algorithm DSL, MCMC configuration, compiler and C++ generation pipeline, and R interfaces are implemented in substantial first-party R alongside the generated-code runtime in C++.

**Coding relevance:**

The selected compiler path needs typed arithmetic and native-interface vocabulary, not Bayesian or statistical expertise; it teaches custom AST and type processing, project compilation state, code generation, native registration, reflection, specialization, and R/C++ interoperability.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** nimbleFunction_core.R defines the user-authored function abstraction, nimbleProject.R owns compilation state, nimbleFunction_compile.R and genCpp_generateCpp.R perform specialization and C++ generation, cppInterfaces_nimbleFunctions.R exposes compiled objects, and test-nimbleFunctionInterfaces.R closes the typed arithmetic compiler and interface trace. The repository contains substantial first-party R despite GitHub's C++ label, and relevant files carry a BSD-3-Clause or GPL-2.0-or-later mixture rather than one uniform whole-tree license.
- **Architecture:** The audited architecture of the path beginning at `packages/nimble/R/nimbleFunction_core.R` has these boundaries: nimbleFunction language surface, project and compilation coordinator, type and code-generation pipeline, native interface layer, and end-to-end interface tests.
- **Naming and idiom:** `packages/nimble/R/nimbleFunction_core.R` and its supporting files use these characteristic R mechanisms: captured R code and custom type specialization, AST transformation and generated C++, and reflection and native R/C++ interface construction.
- **Tests:** Direct tests in `packages/nimble/tests/testthat/test-nimbleFunctionInterfaces.R` cover these states and branches in the selected path: declared, specialized, generated, compiling, loaded, callable, and failed states, setup and run separation, and type, code-generation, compiler, loading, and interface branches.
- **Documentation:** `packages/nimble/R/nimbleFunction_core.R` and its selected supporting material document the contracts needed to understand how NIMBLE turns a typed arithmetic nimbleFunction into generated C++, compiles it within a project, and exposes the native result through an R interface.
- **Traceability:** Start with nimbleFunction setup and typed run declarations, follow specialization and type information into nimbleProject compilation state and generated C++, then trace compilation and native interface creation back to callable R objects; close with interface tests using typed arithmetic and ordinary compiled functions, without Bayesian model evidence.
- **Maintainability:** Changes to the path beginning at `packages/nimble/R/nimbleFunction_core.R` are constrained by these audited guarantees: R semantics and inferred types must map coherently to generated C++, generated declarations, compiled symbols, and R interfaces must agree, and project caching, compilation failure, loading, ownership, and cleanup must remain safe.
- **Educational value:** Understand how NIMBLE turns a typed arithmetic nimbleFunction into generated C++, compiles it within a project, and exposes the native result through an R interface. The selected compiler path needs typed arithmetic and native-interface vocabulary, not Bayesian or statistical expertise; it teaches custom AST and type processing, project compilation state, code generation, native registration, reflection, specialization, and R/C++ interoperability.

**Inspection record:** commit `0181166733112cdaaf4edf7d7b0817a8f03cbdac`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `packages/nimble/R/nimbleFunction_core.R`, `packages/nimble/R/nimbleProject.R`, `packages/nimble/R/nimbleFunction_compile.R`, `packages/nimble/R/genCpp_generateCpp.R`, `packages/nimble/R/cppInterfaces_nimbleFunctions.R`, `packages/nimble/tests/testthat/test-nimbleFunctionInterfaces.R`, `packages/nimble/DESCRIPTION`, `packages/nimble/LICENSE`, `LICENSE`. GitHub Linguist label: C++.

</details>

### [wch/r-source](https://github.com/wch/r-source)

**Language 5 / Behavior 4 / Design 4 / Constraints 5 → Level 5**

**Source:** Production software

The R language implementation, runtime, garbage collector, standard and recommended packages, graphics, statistics, compiler, build system, and platform ports.

**Why study it:** Understand how R's R-authored compiler turns functions and expressions into byte code while preserving lexical scope, control flow, constants, and evaluation semantics. Compiler vocabulary is introduced directly; the R-authored path teaches language-object traversal, lexical environment analysis, constant handling, control-flow compilation, instruction emission, optimization, byte-code objects, and compiler self-tests.

**Short context:**

- R's compiler transforms R expressions and functions into byte-code instructions executed by the R runtime.

**Prerequisites:**

- Strong working familiarity with R functions, vectors and lists, environments, S3 objects at a basic level, conditions, and testthat tests, plus experience tracing state, resources, or asynchronous control flow across many production files.
- R's compiler transforms R expressions and functions into byte-code instructions executed by the R runtime.

**Concepts this path develops:**

- Recursive manipulation of R language objects.
- Parsed, analyzed, optimized, emitted, assembled, and compiled states.
- Compiled code must preserve interpreted R semantics and lexical scope.

**What you can learn:**

- Study these transferable R mechanisms in `src/library/compiler/noweb/compiler.nw`: recursive manipulation of R language objects, lexical environment and closure analysis, and instruction construction, dispatch tables, and compiler metaprogramming.
- Trace these states and branches from `src/library/compiler/noweb/compiler.nw` through its selected supporting files: parsed, analyzed, optimized, emitted, assembled, and compiled states, literal, call, branch, loop, closure, environment, and fallback paths, and compile and evaluation error behavior.
- Identify these architectural responsibilities in the path beginning at `src/library/compiler/noweb/compiler.nw`: literate compiler source, generated shipped R implementation, public compile API documentation, and semantic compiler test families.
- Study these change constraints for the path beginning at `src/library/compiler/noweb/compiler.nw`: compiled code must preserve interpreted R semantics and lexical scope, control flow, constants, promises, environments, and fallbacks must emit valid byte code, and optimization and instruction changes must remain compatible with runtime expectations.

**Learning path:**

- **Goal:** Understand how R's R-authored compiler turns functions and expressions into byte code while preserving lexical scope, control flow, constants, and evaluation semantics.
- **Start here:** [`src/library/compiler/noweb/compiler.nw`](https://github.com/wch/r-source/blob/780021752eb83a71e2198019acf069ba8741103b/src/library/compiler/noweb/compiler.nw) — Begin with `src/library/compiler/noweb/compiler.nw` because it exposes how R's R-authored compiler turns functions and expressions into byte code while preserving lexical scope, control flow, constants, and evaluation semantics.
- **Then read:**
  - [`src/library/compiler/R/cmp.R`](https://github.com/wch/r-source/blob/780021752eb83a71e2198019acf069ba8741103b/src/library/compiler/R/cmp.R)
  - [`src/library/compiler/man/compile.Rd`](https://github.com/wch/r-source/blob/780021752eb83a71e2198019acf069ba8741103b/src/library/compiler/man/compile.Rd)
  - [`src/library/compiler/tests/basics.R`](https://github.com/wch/r-source/blob/780021752eb83a71e2198019acf069ba8741103b/src/library/compiler/tests/basics.R)
  - [`src/library/compiler/tests/loop.R`](https://github.com/wch/r-source/blob/780021752eb83a71e2198019acf069ba8741103b/src/library/compiler/tests/loop.R)
  - [`src/library/compiler/tests/envir.R`](https://github.com/wch/r-source/blob/780021752eb83a71e2198019acf069ba8741103b/src/library/compiler/tests/envir.R)
  - [`src/library/compiler/tests/const.R`](https://github.com/wch/r-source/blob/780021752eb83a71e2198019acf069ba8741103b/src/library/compiler/tests/const.R)
- **Trace:** Start in the literate compiler at expression and function compilation, follow lexical environment and constant analysis through control-flow and instruction emission into the generated cmp.R implementation, then compare the documented compile API; close with basic, loop, environment, and constant tests.

**Why this level:**

- **Language technique 5:** Multiple expert R language and compiler techniques recur throughout the implementation.
- **Behavioral reasoning 4:** Several advanced compiler states and branches recur, while the selected trace remains bounded to byte-code compilation.
- **Design span 4:** Several major pieces cover source, generated artifact, API, and semantic verification without mixing in the C runtime.
- **Constraint burden 5:** Expert semantic-preservation, scope, control-flow, compatibility, and optimization constraints recur across compilation.
- **Placement:** The four scores 5/4/4/5 sum to 18; their arithmetic mean is 4.50 and rounds half-up to Level 5. The published result is Level 5.

**License:** GPL-2.0-only OR GPL-3.0-only ([evidence 1](https://github.com/wch/r-source/blob/780021752eb83a71e2198019acf069ba8741103b/doc/COPYRIGHTS), [evidence 2](https://github.com/wch/r-source/blob/780021752eb83a71e2198019acf069ba8741103b/COPYING), [evidence 3](https://github.com/wch/r-source/blob/780021752eb83a71e2198019acf069ba8741103b/share/licenses/GPL-3))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** This read-only mirror tracks the upstream R source tree used to build the R language and standard software distribution.

**Language evidence:** The repository is the R language implementation itself: its evaluator and runtime are written in C, its base and standard packages substantially in R, and numerical kernels in C and Fortran.

**Coding relevance:**

Compiler vocabulary is introduced directly; the R-authored path teaches language-object traversal, lexical environment analysis, constant handling, control-flow compilation, instruction emission, optimization, byte-code objects, and compiler self-tests.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** compiler.nw is the literate R source of the compiler, generated cmp.R is the shipped implementation, compile.Rd documents the public contract, and basics, loop, environment, and constant tests exercise expression, closure, control-flow, scope, and constant compilation. Pinned copyright evidence supports GPL-2.0-only OR GPL-3.0-only, correcting the catalog's later-version claim.
- **Architecture:** The audited architecture of the path beginning at `src/library/compiler/noweb/compiler.nw` has these boundaries: literate compiler source, generated shipped R implementation, public compile API documentation, and semantic compiler test families.
- **Naming and idiom:** `src/library/compiler/noweb/compiler.nw` and its supporting files use these characteristic R mechanisms: recursive manipulation of R language objects, lexical environment and closure analysis, and instruction construction, dispatch tables, and compiler metaprogramming.
- **Tests:** Direct tests in `src/library/compiler/tests/basics.R`, `src/library/compiler/tests/loop.R`, `src/library/compiler/tests/envir.R`, and `src/library/compiler/tests/const.R` cover these states and branches in the selected path: parsed, analyzed, optimized, emitted, assembled, and compiled states, literal, call, branch, loop, closure, environment, and fallback paths, and compile and evaluation error behavior.
- **Documentation:** `src/library/compiler/noweb/compiler.nw` and its selected supporting material document the contracts needed to understand how R's R-authored compiler turns functions and expressions into byte code while preserving lexical scope, control flow, constants, and evaluation semantics.
- **Traceability:** Start in the literate compiler at expression and function compilation, follow lexical environment and constant analysis through control-flow and instruction emission into the generated cmp.R implementation, then compare the documented compile API; close with basic, loop, environment, and constant tests.
- **Maintainability:** Changes to the path beginning at `src/library/compiler/noweb/compiler.nw` are constrained by these audited guarantees: compiled code must preserve interpreted R semantics and lexical scope, control flow, constants, promises, environments, and fallbacks must emit valid byte code, and optimization and instruction changes must remain compatible with runtime expectations.
- **Educational value:** Understand how R's R-authored compiler turns functions and expressions into byte code while preserving lexical scope, control flow, constants, and evaluation semantics. Compiler vocabulary is introduced directly; the R-authored path teaches language-object traversal, lexical environment analysis, constant handling, control-flow compilation, instruction emission, optimization, byte-code objects, and compiler self-tests.

**Inspection record:** commit `780021752eb83a71e2198019acf069ba8741103b`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/library/compiler/noweb/compiler.nw`, `src/library/compiler/R/cmp.R`, `src/library/compiler/man/compile.Rd`, `src/library/compiler/tests/basics.R`, `src/library/compiler/tests/loop.R`, `src/library/compiler/tests/envir.R`, `src/library/compiler/tests/const.R`, `doc/COPYRIGHTS`, `COPYING`, `share/licenses/GPL-3`. GitHub Linguist label: R.

</details>

_Generated from `catalog/r.json`; do not edit by hand._

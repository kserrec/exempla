# PHP

7 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

[← All languages](../README.md)

## Level 1

### [webmozarts/assert](https://github.com/webmozarts/assert)

**Language 2 / Behavior 1 / Design 1 / Constraints 1 → Level 1**

A focused guard clause that rejects only null, returns every accepted value unchanged, and exposes the narrowed contract to static analysis.

**Why study it:** The path is a small complete production guard clause: it distinguishes null from other falsy values, avoids evaluating a lazy message on success, returns the accepted value, and aligns that runtime contract with PHPDoc and Psalm annotations.

**Prerequisites:**

- Basic PHP functions and static methods, strict comparison, `null`, exceptions, union types, callables, and reading a PHPUnit data provider.

**Concepts this path develops:**

- A precise null guard that preserves valid falsy values and returns the accepted input.
- Lazy diagnostic construction that runs only on the failure branch.
- Agreement between a runtime guard and static-analysis narrowing annotations.

**What you can learn:**

- Trace a non-null value through the strict null comparison to the unchanged return value, then trace null through lazy message resolution to `InvalidArgumentException`.
- Compare false, zero, and null in the shared data provider to see why a null guard must not use a general truthiness check.
- Relate the runtime return contract to `@template T`, `@param T|null`, `@return T`, and `@psalm-assert !null` without treating those annotations as prerequisites.

**Learning path:**

- **Goal:** Understand how `Assert::notNull()` rejects exactly null, preserves other falsy values, resolves diagnostics lazily, and communicates the narrowed return type.
- **Start here:** [`src/Assert.php`](https://github.com/webmozarts/assert/blob/2ccb7c2e821038c03a3e6e1700c570c158c55f70/src/Assert.php) — Read the `notNull()` method and the nearby `resolveMessage()` and `reportInvalidArgument()` helpers; together they contain the complete production behavior.
- **Then read:**
  - [`tests/AssertTest.php`](https://github.com/webmozarts/assert/blob/2ccb7c2e821038c03a3e6e1700c570c158c55f70/tests/AssertTest.php)
  - [`README.md`](https://github.com/webmozarts/assert/blob/2ccb7c2e821038c03a3e6e1700c570c158c55f70/README.md)
- **Trace:** Start at `notNull()` with a mixed value; follow the strict `null === $value` branch to lazy message resolution and the exception helper, or follow the success branch to the unchanged return value. Close the trace in the shared tests for false, zero, null, return identity, custom messages, and one-time lazy-message evaluation, then confirm the public contract in the README.

**Why this level:**

- **Language technique 2:** The runtime body uses basic PHP; a small, locally stated static-analysis convention adds one common professional technique without recurring advanced machinery.
- **Behavioral reasoning 1:** The entire runtime trace is local, synchronous, and directly observable.
- **Design span 1:** One focused source unit and its direct tests contain the complete lesson.
- **Constraint burden 1:** These are small local correctness requirements with direct examples and no interacting compatibility system.
- **Placement:** The four scores 2/1/1/1 sum to 5; their arithmetic mean is 1.25 and rounds half-up to Level 1. No score floor applies.

**License:** MIT ([evidence 1](https://github.com/webmozarts/assert/blob/2ccb7c2e821038c03a3e6e1700c570c158c55f70/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Webmozart Assert is a maintained Composer package used by PHP applications and libraries for runtime precondition checks with stable default and custom error behavior.

**Language evidence:** The public assertion API, message resolution, exception boundary, generated mixins, and direct test suite are first-party PHP.

**Coding relevance:**

The behavior is a general-purpose precondition and type-narrowing boundary with no specialist domain knowledge.

No specialist domain context is required.

**Eight-part quality gate:**

- **Source quality:** The guard and its two shared helpers are short, explicit, and free of hidden state; each branch has one responsibility.
- **Architecture:** The selected behavior stays inside the public assertion class and closes in one shared behavior test suite.
- **Naming and idiom:** `notNull`, `resolveMessage`, and `reportInvalidArgument` state the guard, diagnostic, and failure responsibilities directly while using strict comparison and conventional annotations.
- **Tests:** The parameterized tests cover false, zero, and null, assert return identity or failure, verify custom messages, and count lazy-message callback execution on both branches.
- **Documentation:** The README describes the library purpose, the `notNull` public contract, exception behavior, lazy messages, and static-analysis support.
- **Traceability:** Every claim follows from the `notNull()` branch into one of two adjacent helpers and closes in named rows and shared assertions in `AssertTest.php`.
- **Maintainability:** The method shares stable message and exception helpers but otherwise has no coupling, mutable state, or generated-code dependency.
- **Educational value:** The path turns a familiar guard clause into a complete lesson about precise falsy handling, lazy diagnostics, returned-value contracts, tests, and static-analysis narrowing.

**Inspection record:** commit `2ccb7c2e821038c03a3e6e1700c570c158c55f70`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/Assert.php`, `tests/AssertTest.php`, `README.md`, `LICENSE`. GitHub Linguist label: PHP.

</details>

## Level 2

### [doctrine/lexer](https://github.com/doctrine/lexer)

**Language 3 / Behavior 2 / Design 1 / Constraints 2 → Level 2**

A small reusable base for tokenizing strings for top-down recursive-descent parsers and domain-specific languages.

**Why study it:** The AbstractLexer path shows how a reusable PHP template method turns one input string into typed tokens while preserving cursor, lookahead, peeking, offset, Unicode, and invalid-input contracts.

**Prerequisites:**

- Basic familiarity with PHP classes, interfaces and traits, arrays, callables, exceptions, type declarations, and unit tests.

**Concepts this path develops:**

- PHPDoc templates for token value and token type.
- Localized token-array and cursor state.
- Regex capture and byte-offset accuracy.

**What you can learn:**

- Use `src/AbstractLexer.php` to study the following transferable techniques and behaviors: Regular-expression tokenization, captured byte offsets, abstract pattern and type hooks, generic token values, cursor movement, lookahead, peeking, reset, skipping, Unicode input, and enum token types.

**Learning path:**

- **Goal:** Understand how Doctrine's reusable lexer scans an input string into typed tokens and maintains lookahead, peeking, and cursor invariants for subclasses.
- **Start here:** [`src/AbstractLexer.php`](https://github.com/doctrine/lexer/blob/e96fe45e92a54233726014a7cc7340abf29bb14c/src/AbstractLexer.php) — src/AbstractLexer.php contains setInput, scan, the subclass hooks, and every cursor operation, so it exposes the full reusable lexer contract in one implementation.
- **Then read:**
  - [`src/Token.php`](https://github.com/doctrine/lexer/blob/e96fe45e92a54233726014a7cc7340abf29bb14c/src/Token.php)
  - [`tests/AbstractLexerTest.php`](https://github.com/doctrine/lexer/blob/e96fe45e92a54233726014a7cc7340abf29bb14c/tests/AbstractLexerTest.php)
- **Trace:** Follow setInput through the composed regular expression, preg_split capture offsets, scan, and the subclass getType hook into Token values; then follow moveNext, peek, glimpse, skipUntil, reset, and token checks while correlating movement, position, Unicode, enum-type, locale, and invalid-input tests in AbstractLexerTest.

**Why this level:**

- **Language technique 3:** Generic type relationships and a typed template-method API materially shape the extension contract, satisfying substantial abstraction without advanced runtime machinery.
- **Behavioral reasoning 2:** Meaningful mutable state and branches require care but remain synchronous and localized in one lexer.
- **Design span 1:** The complete behavior stays in one focused unit with two narrow subclass hooks.
- **Constraint burden 2:** Input validation, offsets, explicit errors, and a small stable API impose routine production safeguards rather than several interacting guarantees.
- **Placement:** The four scores 3/2/1/2 sum to 8; their arithmetic mean is 2.00 and rounds half-up to Level 2. The published result is Level 2.

**License:** MIT ([evidence 1](https://github.com/doctrine/lexer/blob/e96fe45e92a54233726014a7cc7340abf29bb14c/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Doctrine publishes the package as lexer infrastructure used by its annotation, query, and persistence tooling.

**Language evidence:** The generic lexer state, token value object, and extension hooks under src are implemented in strict PHP.

**Coding relevance:**

The lexer vocabulary and regular-expression model fit in a short prerequisite paragraph; the selected path primarily teaches generic template APIs, token construction, mutable cursor state, validation, and precise source offsets.

Required domain context:

- A lexer splits an input string into typed tokens and exposes a cursor with lookahead for a parser to consume.

**Eight-part quality gate:**

- **Source quality:** The composed pattern, preg_split captures, token conversion, cursor state, and invalid-input branch are direct and compact.
- **Architecture:** AbstractLexer owns scanning and navigation, Token holds immutable value, type, and position data, and two narrow subclass hooks supply grammar-specific behavior.
- **Naming and idiom:** setInput, scan, getCatchablePatterns, getNonCatchablePatterns, getType, moveNext, lookahead, peek, glimpse, and reset describe the lexer contract.
- **Tests:** AbstractLexerTest covers movement, peeking, skipping, resets, positions, enum types, invalid input, Unicode, and locale-sensitive cases.
- **Documentation:** Class and method documentation explains the generic template parameters, subclass hooks, token positions, and cursor operations used by the selected path.
- **Traceability:** An input can be followed from setInput through the composed regular expression and captured offsets into Token objects, then through each navigation method and its focused assertions.
- **Maintainability:** One scanning component, one value object, stable extension hooks, and boundary-focused tests keep grammar reuse separate from cursor policy.
- **Educational value:** The path demonstrates a small but complete reusable lexer whose abstraction, state, Unicode, and error obligations remain visible.

**Inspection record:** commit `e96fe45e92a54233726014a7cc7340abf29bb14c`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/AbstractLexer.php`, `src/Token.php`, `tests/AbstractLexerTest.php`, `LICENSE`. GitHub Linguist label: PHP.

</details>

### [schmittjoh/php-option](https://github.com/schmittjoh/php-option)

**Language 2 / Behavior 2 / Design 2 / Constraints 3 → Level 2**

An Option type for representing present and absent values with eager, lazy, mapping, filtering, folding, and fallback operations.

**Why study it:** The factory-to-lazy-resolution path shows how a compact PHP API normalizes existing values, callables, and Option instances while preserving a strict absence sentinel, identity, deferred work, successful-result memoization, and explicit failure behavior.

**Prerequisites:**

- Basic familiarity with PHP classes, interfaces and traits, arrays, callables, exceptions, type declarations, and unit tests.

**Concepts this path develops:**

- Abstract class with covariant PHPDoc templates.
- Strict configurable absence sentinel.
- Strict sentinel identity.

**What you can learn:**

- Use `src/PhpOption/Option.php` to study the following transferable techniques and behaviors: Abstract option contracts, PHPDoc covariance and templates, strict sentinel comparison, eager and lazy factory methods, callable normalization, identity preservation, deferred delegation, successful-result memoization, and invalid-callback or invalid-result errors.

**Learning path:**

- **Goal:** Understand how php-option turns eager values, callables, and existing Option objects into a consistent eager or lazy Option while preserving strict absence and resolution behavior.
- **Start here:** [`src/PhpOption/Option.php`](https://github.com/schmittjoh/php-option/blob/67b192b6a42ec03944b972d6e633ddec78ad2c6d/src/PhpOption/Option.php) — Option.php defines fromValue, fromReturn, and ensure alongside the abstract contract, so it exposes every selected normalization decision before the lazy wrapper delegates operations.
- **Then read:**
  - [`src/PhpOption/LazyOption.php`](https://github.com/schmittjoh/php-option/blob/67b192b6a42ec03944b972d6e633ddec78ad2c6d/src/PhpOption/LazyOption.php)
  - [`src/PhpOption/Some.php`](https://github.com/schmittjoh/php-option/blob/67b192b6a42ec03944b972d6e633ddec78ad2c6d/src/PhpOption/Some.php)
  - [`src/PhpOption/None.php`](https://github.com/schmittjoh/php-option/blob/67b192b6a42ec03944b972d6e633ddec78ad2c6d/src/PhpOption/None.php)
  - [`tests/PhpOption/Tests/OptionTest.php`](https://github.com/schmittjoh/php-option/blob/67b192b6a42ec03944b972d6e633ddec78ad2c6d/tests/PhpOption/Tests/OptionTest.php)
  - [`tests/PhpOption/Tests/LazyOptionTest.php`](https://github.com/schmittjoh/php-option/blob/67b192b6a42ec03944b972d6e633ddec78ad2c6d/tests/PhpOption/Tests/LazyOptionTest.php)
- **Trace:** Follow Option.fromValue as strict equality chooses None or Some, then compare fromReturn and ensure as they capture callables or preserve an existing Option; continue into LazyOption.option as it validates, resolves, stores a successful Option, and delegates reads and transforms, while correlating sentinel, callable, identity, fallback, delegation, and invalid-result cases in OptionTest and LazyOptionTest.

**Why this level:**

- **Language technique 2:** Conventional inheritance, callbacks, closure capture, and documented generic relationships materially shape the API without advanced runtime language machinery.
- **Behavioral reasoning 2:** Meaningful branching and lazy state require care but remain synchronous and localized in two small classes.
- **Design span 2:** A few cohesive types contain the complete normalization and resolution behavior.
- **Constraint burden 3:** Several API guarantees interact across eager and lazy construction, including strict absence semantics, object identity, deferred work, reuse of a successful result, and explicit invalid-input failures.
- **Placement:** The four scores 2/2/2/3 sum to 9; their arithmetic mean is 2.25 and rounds half-up to Level 2. The published result is Level 2.

**License:** Apache-2.0 ([evidence 1](https://github.com/schmittjoh/php-option/blob/67b192b6a42ec03944b972d6e633ddec78ad2c6d/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The project publishes phpoption/phpoption through Composer as a reusable production library consumed by other PHP packages and applications.

**Language evidence:** The Option abstraction, eager Some and None implementations, lazy wrapper, and focused tests under src and tests are implemented in PHP.

**Coding relevance:**

The presence-versus-absence model needs only a short primer; the path primarily teaches transferable factory design, higher-order functions, strict comparison, lazy evaluation, delegation, memoization, and error contracts.

Required domain context:

- An Option represents either a present value as Some or absence as None, avoiding a raw sentinel value in the rest of a program.

**Eight-part quality gate:**

- **Source quality:** The three factory branches, lazy state, delegation, validation, and successful-result assignment are compact and explicit.
- **Architecture:** Option owns normalization and the abstract contract, Some and None model the two eager cases, and LazyOption isolates deferred resolution before delegating to a resolved Option.
- **Naming and idiom:** fromValue, fromReturn, ensure, Some, None, LazyOption, isDefined, isEmpty, getOrElse, map, and flatMap state the presence and transformation vocabulary directly.
- **Tests:** OptionTest covers default and custom sentinels, eager factories, lazy return conversion, alternatives, and lifting; LazyOptionTest covers construction, arguments, repeated delegated reads, None behavior, invalid callbacks, invalid results, and delegated operations. The selected tests do not directly count callback invocations, so no exact-once execution claim is made.
- **Documentation:** Class and method documentation explains strict sentinel behavior, factory normalization, callable expectations, laziness, and the Option operations used by the selected path.
- **Traceability:** A value or callable can be followed from one of three factories into Some, None, or LazyOption, through successful resolution or an explicit error, and into focused factory and delegation assertions.
- **Maintainability:** Small implementations, one lazy-resolution seam, strict comparisons, stable abstract operations, and focused tests keep changes locally reviewable.
- **Educational value:** The path demonstrates how a production PHP library replaces raw absence sentinels with a typed, composable, and optionally lazy API without hiding its control flow.

**Inspection record:** commit `67b192b6a42ec03944b972d6e633ddec78ad2c6d`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/PhpOption/Option.php`, `src/PhpOption/LazyOption.php`, `src/PhpOption/Some.php`, `src/PhpOption/None.php`, `tests/PhpOption/Tests/OptionTest.php`, `tests/PhpOption/Tests/LazyOptionTest.php`, `README.md`, `composer.json`, `LICENSE`. GitHub Linguist label: PHP.

</details>

## Level 3

### [nikic/FastRoute](https://github.com/nikic/FastRoute)

**Language 2 / Behavior 3 / Design 3 / Constraints 3 → Level 3**

A fast HTTP request router that compiles static and variable routes into compact dispatch data and matched parameters.

**Why study it:** The FastRoute path shows how route declarations become validated static or combined-regular-expression data and then one of three explicit HTTP dispatch results.

**Prerequisites:**

- Basic familiarity with PHP classes, interfaces and traits, arrays, callables, exceptions, type declarations, and unit tests.

**Concepts this path develops:**

- Interfaces and abstract strategy bases.
- Route syntax expansion and validation.
- Optional-segment and placeholder grammar.

**What you can learn:**

- Use `src/RouteParser/Std.php` to study the following transferable techniques and behaviors: Optional route-segment expansion, placeholder parsing, capture-group rejection, static and variable route validation, combined regular expressions, group-count dispatch, method fallback, and typed dispatch results.

**Learning path:**

- **Goal:** Understand how FastRoute turns a route declaration into compiled static or regular-expression dispatch data and returns the correct dispatch result for an HTTP method and URI.
- **Start here:** [`src/RouteParser/Std.php`](https://github.com/nikic/FastRoute/blob/1c961398bef1ff6ecd8b273bef651d7afe90312b/src/RouteParser/Std.php) — src/RouteParser/Std.php defines the route grammar and expands optional suffixes before declarations enter collection, compiled data generation, and dispatch.
- **Then read:**
  - [`src/RouteCollector.php`](https://github.com/nikic/FastRoute/blob/1c961398bef1ff6ecd8b273bef651d7afe90312b/src/RouteCollector.php)
  - [`src/DataGenerator/RegexBasedAbstract.php`](https://github.com/nikic/FastRoute/blob/1c961398bef1ff6ecd8b273bef651d7afe90312b/src/DataGenerator/RegexBasedAbstract.php)
  - [`src/DataGenerator/GroupCountBased.php`](https://github.com/nikic/FastRoute/blob/1c961398bef1ff6ecd8b273bef651d7afe90312b/src/DataGenerator/GroupCountBased.php)
  - [`src/Dispatcher/RegexBasedAbstract.php`](https://github.com/nikic/FastRoute/blob/1c961398bef1ff6ecd8b273bef651d7afe90312b/src/Dispatcher/RegexBasedAbstract.php)
  - [`src/Dispatcher/GroupCountBased.php`](https://github.com/nikic/FastRoute/blob/1c961398bef1ff6ecd8b273bef651d7afe90312b/src/Dispatcher/GroupCountBased.php)
  - [`test/RouteParser/StdTest.php`](https://github.com/nikic/FastRoute/blob/1c961398bef1ff6ecd8b273bef651d7afe90312b/test/RouteParser/StdTest.php)
  - [`test/Dispatcher/GroupCountBasedTest.php`](https://github.com/nikic/FastRoute/blob/1c961398bef1ff6ecd8b273bef651d7afe90312b/test/Dispatcher/GroupCountBasedTest.php)
  - [`test/Dispatcher/DispatcherTestCase.php`](https://github.com/nikic/FastRoute/blob/1c961398bef1ff6ecd8b273bef651d7afe90312b/test/Dispatcher/DispatcherTestCase.php)
- **Trace:** Follow Std.parse through optional suffix expansion, placeholder extraction, and capturing-group rejection; continue through RouteCollector into RegexBasedAbstract's static and variable route validation and GroupCountBased's combined regular expressions, then through the regex dispatcher into Matched, NotMatched, or MethodNotAllowed while correlating parser cases and the inherited shared dispatcher contract tests.

**Why this level:**

- **Language technique 2:** Interfaces, callbacks, inheritance, and ecosystem conventions shape the path without generics, reflection, or other advanced language machinery.
- **Behavioral reasoning 3:** The staged parser-to-compiled-data-to-dispatch trace has nontrivial state and interactions beyond localized branching.
- **Design span 3:** The trace crosses several meaningful, locally understandable components and interfaces.
- **Constraint burden 3:** Syntax, regular-expression safety, route precedence, HTTP semantics, and compatibility impose several material guarantees.
- **Placement:** The four scores 2/3/3/3 sum to 11; their arithmetic mean is 2.75 and rounds half-up to Level 3. The published result is Level 3.

**License:** BSD-3-Clause ([evidence 1](https://github.com/nikic/FastRoute/blob/1c961398bef1ff6ecd8b273bef651d7afe90312b/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** FastRoute is a published production routing library used by PHP web frameworks and applications.

**Language evidence:** Route parsing, regex data generation, dispatch strategies, caching, and URI generation under src are PHP.

**Coding relevance:**

The route syntax and three dispatch outcomes need only a short primer; the path primarily teaches staged parsing and compilation, regular-expression construction, strategy boundaries, data modeling, validation, and deterministic dispatch.

Required domain context:

- An HTTP router parses static and parameterized route declarations, compiles them into dispatch data, and returns matched, not-matched, or method-not-allowed results for a method and URI.

**Eight-part quality gate:**

- **Source quality:** The parser, collector, regex data generator, and dispatcher express each transformation and rejection branch as a distinct stage.
- **Architecture:** Std parses declarations, RouteCollector registers them, RegexBasedAbstract validates them, GroupCountBased compiles them, and the dispatcher returns explicit result objects.
- **Naming and idiom:** RouteParser, RouteCollector, addStaticRoute, addVariableRoute, DataGenerator, Dispatcher, Matched, NotMatched, and MethodNotAllowed preserve routing vocabulary.
- **Tests:** The selected parser and dispatcher suites cover optional segments, placeholders, invalid captures, duplicates, shadowed routes, method behavior, variables, and result contracts.
- **Documentation:** The README and public API documentation explain route syntax, registration, dispatch results, and method handling corresponding to the selected stages.
- **Traceability:** A route string can be followed through Std.parse, collector validation, grouped regex generation, URI matching, and explicit dispatch results into focused parser and shared dispatcher tests.
- **Maintainability:** Strategy interfaces and staged compiled data isolate grammar, validation, regex layout, and request dispatch while tests protect their shared contracts.
- **Educational value:** The path makes router implementation concrete as a small compiler pipeline followed by a deterministic runtime matcher.

**Inspection record:** commit `1c961398bef1ff6ecd8b273bef651d7afe90312b`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/RouteParser/Std.php`, `src/RouteCollector.php`, `src/DataGenerator/RegexBasedAbstract.php`, `src/DataGenerator/GroupCountBased.php`, `src/Dispatcher/RegexBasedAbstract.php`, `src/Dispatcher/GroupCountBased.php`, `test/RouteParser/StdTest.php`, `test/Dispatcher/GroupCountBasedTest.php`, `test/Dispatcher/DispatcherTestCase.php`, `LICENSE`. GitHub Linguist label: PHP.

</details>

### [webmozarts/assert](https://github.com/webmozarts/assert)

**Language 4 / Behavior 2 / Design 2 / Constraints 4 → Level 3**

A defensive-programming library providing typed assertions for method inputs, outputs, values, collections, files, classes, and objects.

**Why study it:** The MixinGenerator path shows how reflection and source generation can extend a repetitive validation API while preserving native signatures, static-analysis contracts, defaults, messages, and runtime behavior.

**Prerequisites:**

- Basic familiarity with PHP classes, interfaces and traits, arrays, callables, exceptions, type declarations, and unit tests.

**Concepts this path develops:**

- ReflectionClass and ReflectionMethod introspection.
- Deterministic method-family generation.
- Native signature and default-value fidelity.

**What you can learn:**

- Use `bin/src/MixinGenerator.php` to study the following transferable techniques and behaviors: ReflectionClass and ReflectionMethod, deterministic PHP generation, union and intersection type rewriting, PHPDoc assertion transformation, default-value rendering, generated method families, and compatibility testing.

**Learning path:**

- **Goal:** Understand how Webmozart Assert reflects over its base assertions and generates type-preserving nullOr, all, and allNullOr runtime variants.
- **Start here:** [`bin/src/MixinGenerator.php`](https://github.com/webmozarts/assert/blob/2ccb7c2e821038c03a3e6e1700c570c158c55f70/bin/src/MixinGenerator.php) — MixinGenerator.php contains the hand-written reflection and transformation rules that produce nullOr, all, and allNullOr methods, so it is the source of truth rather than the deliberately repetitive generated trait.
- **Then read:**
  - [`bin/generate.php`](https://github.com/webmozarts/assert/blob/2ccb7c2e821038c03a3e6e1700c570c158c55f70/bin/generate.php)
  - [`src/Assert.php`](https://github.com/webmozarts/assert/blob/2ccb7c2e821038c03a3e6e1700c570c158c55f70/src/Assert.php)
  - [`src/Mixin.php`](https://github.com/webmozarts/assert/blob/2ccb7c2e821038c03a3e6e1700c570c158c55f70/src/Mixin.php)
  - [`tests/AssertTest.php`](https://github.com/webmozarts/assert/blob/2ccb7c2e821038c03a3e6e1700c570c158c55f70/tests/AssertTest.php)
- **Trace:** Begin with bin/generate.php, follow MixinGenerator as ReflectionClass and ReflectionMethod enumerate Assert methods, reduce native union and intersection types, transform PHPDoc assertions, defaults, return types, and method bodies, and emit the Mixin trait; then correlate the generated nullOr, all, and allNullOr methods with the parameterized success, failure, lazy-message, and custom-message cases in AssertTest.

**Why this level:**

- **Language technique 4:** Reflection, metaprogramming, and code generation recur throughout the selected behavior and require advanced PHP machinery.
- **Behavioral reasoning 2:** The generator has many cases but its synchronous transformation state remains locally traceable.
- **Design span 2:** A few clear modules contain the generator-to-runtime behavior.
- **Constraint burden 4:** Runtime behavior, native types, PHPDoc types, static-analyser limitations, defaults, messages, and backward-compatible method families interact across the path.
- **Placement:** The four scores 4/2/2/4 sum to 12; their arithmetic mean is 3.00 and rounds half-up to Level 3. The published result is Level 3.

**License:** MIT ([evidence 1](https://github.com/webmozarts/assert/blob/2ccb7c2e821038c03a3e6e1700c570c158c55f70/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** The package is released through Composer as reusable validation infrastructure across production PHP libraries and applications.

**Language evidence:** The assertion API, generated mixin variants, static-analysis plugin, and exception type under src are PHP.

**Coding relevance:**

The assertion and generated-API context is self-contained; the path primarily teaches reflection, code generation, signature and PHPDoc transformation, compatibility policy, and testing generated behavior.

Required domain context:

- An assertion library validates runtime values, while its generated mixin adds nullOr, all, and allNullOr variants of the base assertion methods.

**Eight-part quality gate:**

- **Source quality:** The generator names method enumeration, skips, type reduction, PHPDoc rewriting, defaults, signatures, bodies, and output assembly as separate deterministic transformations.
- **Architecture:** A small generation entry point invokes MixinGenerator over the base Assert API to produce the runtime Mixin trait, whose behavior is exercised through the public assertion tests.
- **Naming and idiom:** MixinGenerator, generate, Assert, Mixin, nullOr, all, allNullOr, reportInvalidArgument, and lazy messages preserve the package's validation vocabulary.
- **Tests:** AssertTest broadly checks base and generated variants, success and failure values, lazy and custom messages, collection behavior, and errors across all three method families.
- **Documentation:** The README documents generated variants, extension, public assertions, messages, and static-analysis use, providing context for each emitted API family.
- **Traceability:** A learner can follow bin/generate.php into reflected Assert methods, signature and documentation transformations, emitted Mixin code, and parameterized runtime assertions.
- **Maintainability:** Keeping generation rules hand-written and output reproducible prevents manual drift among three large method families while preserving a stable public API.
- **Educational value:** This path demonstrates disciplined metaprogramming used to remove duplication without treating generated source as unexplained magic.

**Inspection record:** commit `2ccb7c2e821038c03a3e6e1700c570c158c55f70`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `bin/src/MixinGenerator.php`, `bin/generate.php`, `src/Assert.php`, `src/Mixin.php`, `tests/AssertTest.php`, `LICENSE`. GitHub Linguist label: PHP.

</details>

## Level 4

### [Seldaek/monolog](https://github.com/Seldaek/monolog)

**Language 3 / Behavior 4 / Design 3 / Constraints 4 → Level 4**

A logging library that routes structured records through processors, formatters, filters, buffers, groups, files, sockets, databases, and web services.

**Why study it:** The Logger path shows how Monolog builds one immutable record, delays processing until needed, propagates it through bubbling handlers, contains failures, and prevents recursive logging per Fiber.

**Prerequisites:**

- Working familiarity with PHP classes, interfaces and traits, arrays, callables, exceptions, type declarations, and unit tests, plus experience tracing behavior across several production files.

**Concepts this path develops:**

- Typed immutable LogRecord and Level enum.
- Fiber-local recursive logging state.
- PSR-3 and legacy level compatibility.

**What you can learn:**

- Use `src/Monolog/Logger.php` to study the following transferable techniques and behaviors: Immutable log records, level normalization, callable processors, handler bubbling, once-only processing, exception routing, Fiber-local WeakMap state, recursive-call detection, reset and close lifecycles, and finally-based cleanup.

**Learning path:**

- **Goal:** Understand how Monolog creates and processes one log record, propagates it through bubbling handlers, contains processor or handler failures, and detects recursive logging independently in each Fiber.
- **Start here:** [`src/Monolog/Logger.php`](https://github.com/Seldaek/monolog/blob/2a50ae6f387a6da963bf2e2662803a01517a58ca/src/Monolog/Logger.php) — src/Monolog/Logger.php owns addRecord, where level normalization, recursion depth, record construction, lazy processors, handler bubbling, exception handling, and cleanup meet.
- **Then read:**
  - [`src/Monolog/LogRecord.php`](https://github.com/Seldaek/monolog/blob/2a50ae6f387a6da963bf2e2662803a01517a58ca/src/Monolog/LogRecord.php)
  - [`src/Monolog/Handler/HandlerInterface.php`](https://github.com/Seldaek/monolog/blob/2a50ae6f387a6da963bf2e2662803a01517a58ca/src/Monolog/Handler/HandlerInterface.php)
  - [`src/Monolog/Handler/ProcessableHandlerTrait.php`](https://github.com/Seldaek/monolog/blob/2a50ae6f387a6da963bf2e2662803a01517a58ca/src/Monolog/Handler/ProcessableHandlerTrait.php)
  - [`src/Monolog/Handler/AbstractProcessingHandler.php`](https://github.com/Seldaek/monolog/blob/2a50ae6f387a6da963bf2e2662803a01517a58ca/src/Monolog/Handler/AbstractProcessingHandler.php)
  - [`tests/Monolog/LoggerTest.php`](https://github.com/Seldaek/monolog/blob/2a50ae6f387a6da963bf2e2662803a01517a58ca/tests/Monolog/LoggerTest.php)
- **Trace:** Follow Logger.addRecord as it normalizes the level, increments global or Fiber-local recursion depth, constructs LogRecord, delays processors until a handler accepts the record, clones and propagates it until bubbling stops, routes exceptions, and decrements depth in finally; connect the handler pipeline to ProcessableHandlerTrait and AbstractProcessingHandler and correlate ordering, processor, exception, recursive, Fiber, close, and reset tests.

**Why this level:**

- **Language technique 3:** Framework idioms, higher-order processors, traits, enums, and nontrivial type modeling materially shape the path without several pervasive expert mechanisms.
- **Behavioral reasoning 4:** Reentrancy, event propagation, failure containment, resource lifecycle, and cross-cutting cleanup recur and require advanced nonlocal reasoning.
- **Design span 3:** The trace crosses several meaningful, locally understandable interfaces and components without spanning the entire handler ecosystem.
- **Constraint burden 4:** Compatibility, ordering, recursive safety, failure behavior, lifecycle reuse, and resource cleanup interact throughout the logging path.
- **Placement:** The four scores 3/4/3/4 sum to 14; their arithmetic mean is 3.50 and rounds half-up to Level 4. The published result is Level 4.

**License:** MIT ([evidence 1](https://github.com/Seldaek/monolog/blob/2a50ae6f387a6da963bf2e2662803a01517a58ca/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Monolog is a production PSR-3 logging implementation used by major PHP applications and frameworks.

**Language evidence:** Logger channels, immutable records, handlers, formatters, processors, error integration, and reset contracts under src/Monolog are PHP.

**Coding relevance:**

Logging levels, processors, and handlers are familiar and documented; the path primarily teaches typed pipeline design, lazy initialization, event propagation, Fiber-local reentrancy state, exception routing, resource lifecycle, and cleanup.

Required domain context:

- A logger creates a record, optionally processes it, offers it to ordered handlers until bubbling stops, and must prevent recursive logging from becoming an infinite loop.

**Eight-part quality gate:**

- **Source quality:** Logger.addRecord makes handler selection, delayed processor execution, record cloning, bubbling, failure routing, recursion depth, and finally cleanup explicit.
- **Architecture:** Logger orchestrates, LogRecord carries immutable data, HandlerInterface defines propagation, ProcessableHandlerTrait applies processors, and AbstractProcessingHandler joins formatting to output.
- **Naming and idiom:** addRecord, LogRecord, Level, handlers, processors, bubbling, handleException, detectCycles, Fiber, close, and reset consistently expose pipeline behavior.
- **Tests:** LoggerTest covers handler selection and order, processor-once behavior, cloned records, exceptions, recursion, Fiber isolation, reset, close, and cleanup.
- **Documentation:** Monolog's usage, handler, processor, bubbling, and lifecycle documentation explains the public behavior implemented by this selected pipeline.
- **Traceability:** A log call can be followed through addRecord, LogRecord creation, first accepting handler, delayed processors, bubbling or failure, Fiber-local depth cleanup, and focused tests.
- **Maintainability:** Immutable records, stable handler and processor contracts, explicit reentrancy state, and lifecycle regressions localize changes across a large handler ecosystem.
- **Educational value:** The path demonstrates how an extensible logging pipeline preserves ordering, isolation, reentrancy safety, and cleanup without obscuring its control flow.

**Inspection record:** commit `2a50ae6f387a6da963bf2e2662803a01517a58ca`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/Monolog/Logger.php`, `src/Monolog/LogRecord.php`, `src/Monolog/Handler/HandlerInterface.php`, `src/Monolog/Handler/ProcessableHandlerTrait.php`, `src/Monolog/Handler/AbstractProcessingHandler.php`, `tests/Monolog/LoggerTest.php`, `LICENSE`. GitHub Linguist label: PHP.

</details>

### [symfony/symfony](https://github.com/symfony/symfony)

**Language 3 / Behavior 4 / Design 4 / Constraints 4 → Level 4**

A component framework spanning dependency injection, HTTP kernels, console tools, events, routing, security, messaging, forms, validation, and integrations.

**Why study it:** The HttpKernel path shows how Symfony transforms one Request into a Response through ordered resolver and event extensions while preserving nested and streamed request context and recovering from exceptions.

**Prerequisites:**

- Working familiarity with PHP classes, interfaces and traits, arrays, callables, exceptions, type declarations, and unit tests, plus experience tracing behavior across several production files.

**Concepts this path develops:**

- Interface-driven controller and argument resolution.
- Ordered event propagation and short circuits.
- Strict event and resolver ordering.

**What you can learn:**

- Use `src/Symfony/Component/HttpKernel/HttpKernel.php` to study the following transferable techniques and behaviors: RequestStack ownership, ordered event dispatch, controller and argument resolution, short circuits, callable invocation, view conversion, response filtering, exception recovery, streamed callbacks, finish events, termination, and cleanup.

**Learning path:**

- **Goal:** Understand how Symfony HttpKernel transforms one Request into a Response through resolver and event extension points while preserving nested-request context and recovering from exceptions.
- **Start here:** [`src/Symfony/Component/HttpKernel/HttpKernel.php`](https://github.com/symfony/symfony/blob/c69a0a62bc6cff4c25ae9447e16f52960dba71af/src/Symfony/Component/HttpKernel/HttpKernel.php) — src/Symfony/Component/HttpKernel/HttpKernel.php owns handle and handleRaw, which expose every selected request, controller, view, response, exception, finish, and terminate transition.
- **Then read:**
  - [`src/Symfony/Component/HttpKernel/HttpKernelInterface.php`](https://github.com/symfony/symfony/blob/c69a0a62bc6cff4c25ae9447e16f52960dba71af/src/Symfony/Component/HttpKernel/HttpKernelInterface.php)
  - [`src/Symfony/Component/HttpKernel/Controller/ControllerResolver.php`](https://github.com/symfony/symfony/blob/c69a0a62bc6cff4c25ae9447e16f52960dba71af/src/Symfony/Component/HttpKernel/Controller/ControllerResolver.php)
  - [`src/Symfony/Component/HttpKernel/Event/RequestEvent.php`](https://github.com/symfony/symfony/blob/c69a0a62bc6cff4c25ae9447e16f52960dba71af/src/Symfony/Component/HttpKernel/Event/RequestEvent.php)
  - [`src/Symfony/Component/HttpKernel/Event/ControllerEvent.php`](https://github.com/symfony/symfony/blob/c69a0a62bc6cff4c25ae9447e16f52960dba71af/src/Symfony/Component/HttpKernel/Event/ControllerEvent.php)
  - [`src/Symfony/Component/HttpKernel/Event/ControllerArgumentsEvent.php`](https://github.com/symfony/symfony/blob/c69a0a62bc6cff4c25ae9447e16f52960dba71af/src/Symfony/Component/HttpKernel/Event/ControllerArgumentsEvent.php)
  - [`src/Symfony/Component/HttpKernel/Event/ViewEvent.php`](https://github.com/symfony/symfony/blob/c69a0a62bc6cff4c25ae9447e16f52960dba71af/src/Symfony/Component/HttpKernel/Event/ViewEvent.php)
  - [`src/Symfony/Component/HttpKernel/Event/ResponseEvent.php`](https://github.com/symfony/symfony/blob/c69a0a62bc6cff4c25ae9447e16f52960dba71af/src/Symfony/Component/HttpKernel/Event/ResponseEvent.php)
  - [`src/Symfony/Component/HttpKernel/Event/ExceptionEvent.php`](https://github.com/symfony/symfony/blob/c69a0a62bc6cff4c25ae9447e16f52960dba71af/src/Symfony/Component/HttpKernel/Event/ExceptionEvent.php)
  - [`src/Symfony/Component/HttpKernel/Event/FinishRequestEvent.php`](https://github.com/symfony/symfony/blob/c69a0a62bc6cff4c25ae9447e16f52960dba71af/src/Symfony/Component/HttpKernel/Event/FinishRequestEvent.php)
  - [`src/Symfony/Component/HttpKernel/Event/TerminateEvent.php`](https://github.com/symfony/symfony/blob/c69a0a62bc6cff4c25ae9447e16f52960dba71af/src/Symfony/Component/HttpKernel/Event/TerminateEvent.php)
  - [`src/Symfony/Component/HttpKernel/Tests/HttpKernelTest.php`](https://github.com/symfony/symfony/blob/c69a0a62bc6cff4c25ae9447e16f52960dba71af/src/Symfony/Component/HttpKernel/Tests/HttpKernelTest.php)
- **Trace:** Follow HttpKernel.handle as it pushes the RequestStack and dispatches RequestEvent, resolves and filters the controller and arguments, invokes the controller, converts a non-Response through ViewEvent, filters the Response, or recovers through ExceptionEvent; then follow streamed-response context restoration, FinishRequestEvent, stack cleanup, and termination while correlating each lifecycle branch in HttpKernelTest.

**Why this level:**

- **Language technique 3:** Framework idioms, event types, callbacks, and substantial interface composition materially shape the path without pervasive advanced language machinery.
- **Behavioral reasoning 4:** Event propagation, nested lifecycle state, recovery, callback context, and cleanup recur and require advanced nonlocal reasoning.
- **Design span 4:** Many framework modules and extension points contribute directly to one request lifecycle.
- **Constraint burden 4:** Ordering, extension compatibility, context integrity, recovery, response correctness, and cleanup guarantees interact throughout the kernel.
- **Placement:** The four scores 3/4/4/4 sum to 15; their arithmetic mean is 3.75 and rounds half-up to Level 4. The published result is Level 4.

**License:** MIT ([evidence 1](https://github.com/symfony/symfony/blob/c69a0a62bc6cff4c25ae9447e16f52960dba71af/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Real-world evidence:** Symfony is actively released production infrastructure used directly and as a foundation for major PHP applications and frameworks.

**Language evidence:** The framework's dependency injection, HTTP, console, event, routing, security, messaging, persistence bridges, and component implementations are PHP.

**Coding relevance:**

The HTTP request-response lifecycle and event names are documented and familiar; the path primarily teaches staged framework orchestration, extension events, nested request context, exception recovery, cleanup, and strict lifecycle contracts.

Required domain context:

- An HTTP kernel turns a Request into a Response by dispatching request, controller, arguments, view, response, exception, and finish events around controller resolution and invocation.

**Eight-part quality gate:**

- **Source quality:** HttpKernel names each lifecycle transition and keeps early responses, resolver failures, exception recovery, streamed callbacks, and final cleanup explicit.
- **Architecture:** HttpKernel orchestrates RequestStack, ControllerResolver, the event dispatcher, typed lifecycle events, Response handling, and termination through stable interfaces.
- **Naming and idiom:** handle, handleRaw, RequestEvent, ControllerEvent, ControllerArgumentsEvent, ViewEvent, ResponseEvent, ExceptionEvent, FinishRequestEvent, and TerminateEvent state event order.
- **Tests:** HttpKernelTest covers request short circuits, controller and argument resolution, view conversion, response filtering, exceptions, streamed responses, nested requests, finish, and termination.
- **Documentation:** Symfony's HttpKernel and event documentation explains the request lifecycle, resolver contracts, subrequests, exception handling, response events, and termination used here.
- **Traceability:** A Request can be followed from stack push through each typed event, resolver, controller or view conversion, response filtering, exception recovery, finish cleanup, and termination assertions.
- **Maintainability:** Typed events, resolver interfaces, explicit stack ownership, and lifecycle tests let extensions evolve without weakening ordering or context guarantees.
- **Educational value:** The path provides a compact example of event-driven framework orchestration in which every short circuit, recovery branch, and cleanup step is observable.

**Inspection record:** commit `c69a0a62bc6cff4c25ae9447e16f52960dba71af`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/Symfony/Component/HttpKernel/HttpKernel.php`, `src/Symfony/Component/HttpKernel/HttpKernelInterface.php`, `src/Symfony/Component/HttpKernel/Controller/ControllerResolver.php`, `src/Symfony/Component/HttpKernel/Event/RequestEvent.php`, `src/Symfony/Component/HttpKernel/Event/ControllerEvent.php`, `src/Symfony/Component/HttpKernel/Event/ControllerArgumentsEvent.php`, `src/Symfony/Component/HttpKernel/Event/ViewEvent.php`, `src/Symfony/Component/HttpKernel/Event/ResponseEvent.php`, `src/Symfony/Component/HttpKernel/Event/ExceptionEvent.php`, `src/Symfony/Component/HttpKernel/Event/FinishRequestEvent.php`, `src/Symfony/Component/HttpKernel/Event/TerminateEvent.php`, `src/Symfony/Component/HttpKernel/Tests/HttpKernelTest.php`, `LICENSE`. GitHub Linguist label: PHP.

</details>

## Level 5

No qualified learning path has been published at this level. Standards are not lowered to fill a slot.

_Generated from `catalog/php.json`; do not edit by hand._

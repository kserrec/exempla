# C#

10 qualified learning paths. Scores assume the learner described in [the learning-level rubric](../../docs/learning-levels.md).

**Source legend:** Production software is built primarily for real users or systems. Educational exemplars are complete teaching-oriented software and may appear only at Levels 1 and 2.

[← All languages](../README.md)

## Level 1 — First real code

### [dotnet/runtime](https://github.com/dotnet/runtime)

**Language 1 / Behavior 2 / Design 1 / Constraints 1 → Level 1**

**Source:** Production software

The .NET integer Clamp overload returns the nearest inclusive bound, preserves in-range values, and rejects a minimum greater than the maximum.

**Why study it:** Trace a familiar numeric operation through explicit validation and three direct returns, then compare signed boundary rows and the invalid-range test.

**Prerequisites:**

- The global novice C# baseline: static methods, integers, conditionals, exceptions, classes, and focused tests.
- AggressiveInlining is only a runtime optimization hint; it does not change the method's visible behavior.

**Concepts this path develops:**

- Checking a precondition before ordinary control flow.
- Expressing an inclusive clamp with three obvious outcomes.
- Reusing table data across numeric overload tests.

**What you can learn:**

- Reject a numeric interval whose minimum exceeds its maximum.
- Return the lower bound, upper bound, or original value with direct branches.
- Use shared test data to cover negative, interior, boundary, and out-of-range integers.

**Learning path:**

- **Goal:** Understand how .NET Math.Clamp keeps an int inside inclusive bounds and reports a reversed interval.
- **Start here:** [`src/libraries/System.Private.CoreLib/src/System/Math.cs`](https://github.com/dotnet/runtime/blob/aa036afce592ad80e938a35bd376222fb232cba9/src/libraries/System.Private.CoreLib/src/System/Math.cs) — The int overload contains the full validation and three-result control flow.
- **Then read:**
  - [`src/libraries/System.Runtime/tests/System.Runtime.Extensions.Tests/System/Math.cs`](https://github.com/dotnet/runtime/blob/aa036afce592ad80e938a35bd376222fb232cba9/src/libraries/System.Runtime/tests/System.Runtime.Extensions.Tests/System/Math.cs)
  - [`README.md`](https://github.com/dotnet/runtime/blob/aa036afce592ad80e938a35bd376222fb232cba9/README.md)
- **Trace:** Enter the int Clamp overload, call the shared exception helper when min exceeds max, otherwise return min for a low value, max for a high value, or the original value, then map those branches to Clamp_SignedInt_TestData, Clamp_Int, and the reversed-range fact.

**Why this level:**

- **Language technique 1:** The selected overload uses only basic C# method, branch, integer, and exception-call syntax.
- **Behavioral reasoning 2:** A few meaningful local branches cover the complete behavior without nonlocal state.
- **Design span 1:** The selected contract stays in one implementation file and one focused test area.
- **Constraint burden 1:** A small local numeric contract and expected output dominate the path.
- **Novice accessibility floor 1:** The control flow is entirely within the novice C# baseline; the attribute and shared throw helper can each be explained locally without another topic.
  - **Central concepts:** input validation; inclusive numeric bounds; direct conditional returns
  - **Incidental concepts:** an inlining attribute; a shared helper that throws the range exception
- **Placement:** The four scores 1/2/1/1 produce rubric Level 1. Novice accessibility floor 1 preserves published Level 1.

**License:** MIT ([evidence 1](https://github.com/dotnet/runtime/blob/aa036afce592ad80e938a35bd376222fb232cba9/LICENSE.TXT))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** dotnet/runtime is the production implementation of .NET, and Math.Clamp is a public standard-library API used by C# applications.

**Language evidence:** The System.Math implementation and its xUnit theory are first-party C# in the official .NET runtime repository; GitHub labels the repository C#.

**Coding relevance:**

Precondition checks, numeric boundary handling, direct branches, and table-driven tests transfer to everyday application code.

No specialist domain context is required.

**Eight-part quality gate:**

- **Source quality:** The implementation exposes validation and each result branch directly without arithmetic tricks or hidden state.
- **Architecture:** The standard-library overload and shared numeric test table have a narrow, explicit relationship.
- **Naming and idiom:** value, min, max, Clamp, and ThrowMinMaxException state both the ordinary contract and error plainly.
- **Tests:** The signed table covers both bounds, an interior value, values below and above, while a separate fact verifies the reversed-range exception for int and other overloads.
- **Documentation:** The public API is documented by .NET reference source comments and repository documentation, with parameter names matching the implementation.
- **Traceability:** Every validation and return branch maps to a row or exception assertion in the direct Math tests.
- **Maintainability:** Straight-line branches, shared error handling, and reusable boundary data make overload behavior easy to compare and change.
- **Educational value:** The path is a first serious C# reading that shows production clarity and exact boundary testing inside the runtime itself.

**Inspection record:** commit `aa036afce592ad80e938a35bd376222fb232cba9`, inspected 2026-08-30. Review passes: Codex follow-up lower-level investigation; Codex resumed-session source verification. Files inspected: `src/libraries/System.Private.CoreLib/src/System/Math.cs`, `src/libraries/System.Runtime/tests/System.Runtime.Extensions.Tests/System/Math.cs`, `README.md`, `LICENSE.TXT`. GitHub Linguist label: C#.

</details>

## Level 2 — Guided real-world patterns

### [dotnet/samples](https://github.com/dotnet/samples)

**Language 3 / Behavior 2 / Design 2 / Constraints 2 → Level 2**

**Source:** Educational exemplar

Microsoft's completed unit-testing sample checks a small prime-number service with boundary, positive, and negative xUnit data sets.

**Why study it:** Follow one small class into organized boundary and representative data sets, seeing how test names and failure messages explain the intended contract.

Levels 1–2 may use intentionally instructive software when it provides a gentler path into reading good source code.

**Short context:**

- A prime integer is at least two and has no whole-number divisor other than one and itself; that elementary definition is sufficient for the path.

**Prerequisites:**

- The global novice C# baseline: classes, methods, integers, conditionals, loops, namespaces, and focused tests.
- A theory is one test method repeated for each InlineData row; the supplied value becomes the method argument.

**Concepts this path develops:**

- Partitioning test data around a public contract's meaningful cases.
- Keeping production and test dependencies in separate projects.
- Writing diagnostic assertions that include the failing input.

**What you can learn:**

- Separate a library project from a project that tests its public behavior.
- Use data rows to cover boundary values, representative successes, and representative failures.
- Trace an early return and divisor loop into exact boolean assertions.

**Learning path:**

- **Goal:** Understand how a complete .NET sample organizes and runs data-driven tests for a small C# prime-checking service.
- **Start here:** [`core/getting-started/unit-testing-using-dotnet-test/PrimeService/PrimeService.cs`](https://github.com/dotnet/samples/blob/86ff8487361a6f32549d9c9ab8b14dde55c643cf/core/getting-started/unit-testing-using-dotnet-test/PrimeService/PrimeService.cs) — The file contains the complete early-boundary and divisor-loop behavior checked by the sample.
- **Then read:**
  - [`core/getting-started/unit-testing-using-dotnet-test/PrimeService.Tests/PrimeService_IsPrimeShould.cs`](https://github.com/dotnet/samples/blob/86ff8487361a6f32549d9c9ab8b14dde55c643cf/core/getting-started/unit-testing-using-dotnet-test/PrimeService.Tests/PrimeService_IsPrimeShould.cs)
  - [`core/getting-started/unit-testing-using-dotnet-test/README.md`](https://github.com/dotnet/samples/blob/86ff8487361a6f32549d9c9ab8b14dde55c643cf/core/getting-started/unit-testing-using-dotnet-test/README.md)
  - [`core/getting-started/unit-testing-using-dotnet-test/PrimeService.Tests/PrimeService.Tests.csproj`](https://github.com/dotnet/samples/blob/86ff8487361a6f32549d9c9ab8b14dde55c643cf/core/getting-started/unit-testing-using-dotnet-test/PrimeService.Tests/PrimeService.Tests.csproj)
- **Trace:** Start at IsPrime's less-than-two return, follow candidates through the divisor loop and success return, then group the InlineData rows into boundary, prime, and composite cases and connect their xUnit assertions to the configured test project.

**Why this level:**

- **Language technique 3:** Attributes materially control test discovery and input injection, while the implementation language remains basic C#.
- **Behavioral reasoning 2:** A few local branches determine the result, and representative cases remain easy to simulate by hand.
- **Design span 2:** Two small, explicit project roles contain the complete implementation-to-test path.
- **Constraint burden 2:** Routine correctness and test-runner safeguards matter without broader production constraints.
- **Novice accessibility floor 2:** A short primer on theories, InlineData, and project references is sufficient; the elementary loop and every expected result remain directly predictable.
  - **Central concepts:** data-driven xUnit tests; test-case partitioning; library and test project separation
  - **Incidental concepts:** the square-root loop bound; MSBuild package references
- **Placement:** The four scores 3/2/2/2 produce rubric Level 2. Novice accessibility floor 2 preserves published Level 2.

**License:** CC-BY-4.0 ([evidence 1](https://github.com/dotnet/samples/blob/86ff8487361a6f32549d9c9ab8b14dde55c643cf/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The subproject README identifies this complete artifact as the sample for Microsoft's unit-testing tutorial, documents restore and test commands, and includes both implementation and configured test projects.

**Language evidence:** The selected service, xUnit tests, and project definitions are first-party C# and MSBuild files in Microsoft's .NET samples repository; GitHub labels the repository C#.

**Coding relevance:**

The mathematics is elementary and subordinate to reusable lessons in test partitioning, project boundaries, loops, early returns, and diagnostics.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The implementation is complete, readable, and uses a bounded loop rather than placeholder or exercise code.
- **Architecture:** The sample cleanly separates the service library, tests, and their project dependency.
- **Naming and idiom:** IsPrime, candidate, divisor, expected test classes, and xUnit attributes state intent conventionally.
- **Tests:** Eleven InlineData cases cover below-boundary values, small primes, and small composites with input-specific messages.
- **Documentation:** The README states the tutorial purpose, project behavior, restore process, and exact test command.
- **Traceability:** Each data row reaches one method call and one boolean assertion through a short visible implementation.
- **Maintainability:** A narrow API and explicit test project keep changes bounded; current package references remain in the checked-in project.
- **Educational value:** The artifact teaches meaningful professional test organization while keeping the application logic transparent.

**Inspection record:** commit `86ff8487361a6f32549d9c9ab8b14dde55c643cf`, inspected 2026-08-30. Review passes: Codex lower-level expansion pass. Files inspected: `core/getting-started/unit-testing-using-dotnet-test/PrimeService/PrimeService.cs`, `core/getting-started/unit-testing-using-dotnet-test/PrimeService.Tests/PrimeService_IsPrimeShould.cs`, `core/getting-started/unit-testing-using-dotnet-test/README.md`, `core/getting-started/unit-testing-using-dotnet-test/PrimeService/PrimeService.csproj`, `core/getting-started/unit-testing-using-dotnet-test/PrimeService.Tests/PrimeService.Tests.csproj`, `LICENSE`. GitHub Linguist label: C#.

</details>

### [ardalis/GuardClauses](https://github.com/ardalis/GuardClauses)

**Language 3 / Behavior 2 / Design 1 / Constraints 2 → Level 2**

**Source:** Production software

A small C# library that checks arguments and returns an accepted value so calling code can continue safely.

**Why study it:** See how one null check becomes a reusable guard while compiler annotations make the successful non-null result available to later code.

**Prerequisites:**

- The global novice C# baseline, including classes, simple generics, nullable values, exceptions, and focused tests.
- A nullability attribute informs the compiler after a successful guard; caller-expression capture supplies the original argument text for an error name.

**Concepts this path develops:**

- Turning one null check into a reusable guard method.
- Returning the accepted value with a non-null compiler contract.
- Preserving useful parameter names and predictable exceptions.

**What you can learn:**

- Trace reference-type and nullable-value inputs through the same two outcomes.
- See how compiler-facing annotations match the runtime guard.
- Use direct tests to compare default and custom exception behavior.

**Learning path:**

- **Goal:** Understand how GuardClauses rejects null arguments while returning a compiler-narrowed value and preserving the caller's argument name and exception contract.
- **Start here:** [`src/GuardClauses/GuardAgainstNullExtensions.cs`](https://github.com/ardalis/GuardClauses/blob/7d55fa5397d73c0fe4e86a2dcab0230d1db57870/src/GuardClauses/GuardAgainstNullExtensions.cs) — src/GuardClauses/GuardAgainstNullExtensions.cs contains the reference- and value-type Null overloads and exposes every selected type-system and exception behavior directly.
- **Then read:**
  - [`src/GuardClauses/Guard.cs`](https://github.com/ardalis/GuardClauses/blob/7d55fa5397d73c0fe4e86a2dcab0230d1db57870/src/GuardClauses/Guard.cs)
  - [`test/GuardClauses.UnitTests/GuardAgainstNull.cs`](https://github.com/ardalis/GuardClauses/blob/7d55fa5397d73c0fe4e86a2dcab0230d1db57870/test/GuardClauses.UnitTests/GuardAgainstNull.cs)
- **Trace:** Begin with the reference- and value-type Null extension overloads, follow their generic constraints, nullable annotations, CallerArgumentExpression parameter capture, and optional exception factory into ArgumentNullException, then correlate default and custom names, messages, factories, non-null returns, and nullable value narrowing in GuardAgainstNull tests.

**Why this level:**

- **Language technique 3:** Generics, constraints, compiler flow annotations, and caller-expression capture materially shape the small public API.
- **Behavioral reasoning 2:** Validation and error behavior require care but remain synchronous and local to the guard call.
- **Design span 1:** The complete behavior remains in one focused unit with a minimal public marker boundary.
- **Constraint burden 2:** The path preserves routine public-API, diagnostic, and compiler-analysis safeguards without several interacting production constraints.
- **Novice accessibility floor 2:** A short primer can explain the two compiler-facing attributes; after that, the null and accepted-value branches are direct and predictable.
  - **Central concepts:** reusable null guard; generic reference- and value-type overloads; compiler non-null flow narrowing
  - **Incidental concepts:** automatic caller-expression capture; optional custom exception factory
- **Placement:** The four structural scores 3/2/1/2 produce rubric Level 2 under the documented formula and guardrails. Novice accessibility floor 2 produces published Level 2.

**License:** MIT ([evidence 1](https://github.com/ardalis/GuardClauses/blob/7d55fa5397d73c0fe4e86a2dcab0230d1db57870/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** The repository publishes a NuGet package used to enforce method preconditions in production .NET applications.

**Language evidence:** The guard entry point and validation extension methods under src/GuardClauses are implemented in C#.

**Coding relevance:**

The selected behavior is entirely about transferable argument validation, generic nullable-flow contracts, exception construction, and caller-expression capture.

No specialist domain context is required.

**Eight-part quality gate:**

- **Source quality:** The two overload families state their generic constraints, nullable contracts, captured argument name, optional message, custom factory, and return value explicitly.
- **Architecture:** A minimal Guard marker API hosts one focused extension unit, while the compiler and ArgumentNullException supply the flow and diagnostic boundaries.
- **Naming and idiom:** Guard, Against, Null, input, parameterName, message, exceptionCreator, NotNull, and CallerArgumentExpression state the guard contract directly.
- **Tests:** GuardAgainstNull tests cover null and non-null references and nullable values, default and custom names, messages, factories, returned values, and compiler narrowing.
- **Documentation:** XML documentation and the public guard-clause guidance explain the value-returning null contract, automatic parameter names, and customization points.
- **Traceability:** A Guard.Against.Null call can be followed through overload selection, compiler-supplied argument text, the null branch, optional exception factory, and focused assertions.
- **Maintainability:** The narrow extension surface and direct compiler-contract tests make changes to nullability, diagnostics, and exception compatibility easy to review.
- **Educational value:** The path demonstrates how a few modern C# features can make a conventional runtime guard improve static flow analysis and caller diagnostics.

**Inspection record:** commit `7d55fa5397d73c0fe4e86a2dcab0230d1db57870`, inspected 2026-08-30. Review passes: Codex primary pass; independent Codex verification pass; Codex novice-accessibility audit. Files inspected: `src/GuardClauses/GuardAgainstNullExtensions.cs`, `src/GuardClauses/Guard.cs`, `test/GuardClauses.UnitTests/GuardAgainstNull.cs`, `LICENSE`. GitHub Linguist label: C#.

</details>

### [Humanizr/Humanizer](https://github.com/Humanizr/Humanizer)

**Language 2 / Behavior 1 / Design 2 / Constraints 2 → Level 2**

**Source:** Production software

A C# string helper that shortens long text to a requested length and can keep either the beginning or the end.

**Why study it:** Follow a familiar string operation through overloads, one strategy boundary, left-or-right slicing, an optional marker, and a table of concrete boundary cases.

**Short context:**

- Truncation shortens text that exceeds a maximum length; a marker such as an ellipsis can show where text was removed.

**Prerequisites:**

- The global novice C# baseline, including strings, extension methods, interfaces, nullable values, slicing, and focused tests.
- A truncation strategy is an object that decides which part of overlong text to keep; this path uses the direct fixed-length strategy.

**Concepts this path develops:**

- Delegating friendly overloads to one complete operation.
- Separating a public string helper from a replaceable truncation strategy.
- Preserving a maximum result length while choosing the kept side and optional marker.

**What you can learn:**

- Trace simple extension-method overloads into one fixed-length truncation strategy.
- Compare unchanged, right-truncated, and left-truncated strings with and without a marker.
- See how nullable input and a compiler-facing non-null return annotation agree.
- Use table-driven tests to identify the exact maximum-length contract and its documented UTF-16 code-unit limit.

**Learning path:**

- **Goal:** Understand how a C# helper shortens a string to a fixed maximum length from either side.
- **Start here:** [`src/Humanizer/TruncateExtensions.cs`](https://github.com/Humanizr/Humanizer/blob/ffc2b77c0f30d2fb176875841424379319d0ae9b/src/Humanizer/TruncateExtensions.cs) — Begin with the public overloads and follow them into the one overload that validates the strategy and delegates the work.
- **Then read:**
  - [`src/Humanizer/Truncation/ITruncator.cs`](https://github.com/Humanizr/Humanizer/blob/ffc2b77c0f30d2fb176875841424379319d0ae9b/src/Humanizer/Truncation/ITruncator.cs)
  - [`src/Humanizer/Truncation/FixedLengthTruncator.cs`](https://github.com/Humanizr/Humanizer/blob/ffc2b77c0f30d2fb176875841424379319d0ae9b/src/Humanizer/Truncation/FixedLengthTruncator.cs)
  - [`src/Humanizer/Truncation/Truncator.cs`](https://github.com/Humanizr/Humanizer/blob/ffc2b77c0f30d2fb176875841424379319d0ae9b/src/Humanizer/Truncation/Truncator.cs)
  - [`src/Humanizer/TruncateFrom.cs`](https://github.com/Humanizr/Humanizer/blob/ffc2b77c0f30d2fb176875841424379319d0ae9b/src/Humanizer/TruncateFrom.cs)
  - [`tests/Humanizer.Tests/TruncatorTests.cs`](https://github.com/Humanizr/Humanizer/blob/ffc2b77c0f30d2fb176875841424379319d0ae9b/tests/Humanizer.Tests/TruncatorTests.cs)
  - [`website/docs/api/Humanizer.TruncateExtensions.md`](https://github.com/Humanizr/Humanizer/blob/ffc2b77c0f30d2fb176875841424379319d0ae9b/website/docs/api/Humanizer.TruncateExtensions.md)
- **Trace:** Start with the simplest Truncate overload, follow overload delegation and strategy validation into FixedLengthTruncator, compare null, already-short, missing-marker, left, and right branches, then close with the direct data-driven cases and the documented UTF-16 code-unit boundary.

**Why this level:**

- **Language technique 2:** Several common professional C# techniques shape the small API, but each is conventional and locally visible.
- **Behavioral reasoning 1:** Each call follows a short deterministic branch and has no lifecycle or hidden state.
- **Design span 2:** A few cohesive types form the complete public-to-strategy path.
- **Constraint burden 2:** Routine public-API and boundary guarantees constrain the helper without forming a wider compatibility system.
- **Novice accessibility floor 2:** One short strategy primer makes every selected branch predictable; the Unicode limitation is stated as a boundary rather than expanded into a separate text-processing lesson.
  - **Central concepts:** fixed-length string truncation; overload delegation to a strategy; left-versus-right slicing with an optional marker
  - **Incidental concepts:** nullable-flow annotation; UTF-16 code-unit rather than grapheme boundaries
- **Placement:** The four structural scores 2/1/2/2 produce rubric Level 2 under the documented formula and guardrails. Novice accessibility floor 2 produces published Level 2.

**License:** MIT ([evidence 1](https://github.com/Humanizr/Humanizer/blob/ffc2b77c0f30d2fb176875841424379319d0ae9b/license.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** Humanizer publishes a maintained .NET package whose production string APIs include documented and directly tested truncation strategies used by applications.

**Language evidence:** The selected extension methods, truncation strategy interface, fixed-length implementation, direction enum, and direct tests are implemented in C# under src/Humanizer and tests/Humanizer.Tests.

**Coding relevance:**

The context is familiar and fully defined above; the selected path teaches reusable overload delegation, strategy interfaces, validation, slicing, null contracts, symmetry, and boundary testing.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The public overloads delegate to a narrow strategy interface and the fixed-length implementation expresses all selected branches directly; extensive table cases cover null, short, exact, long, marker, and direction behavior.
- **Architecture:** The selected path has three clear boundaries: public extension overloads, one truncation-strategy interface, and one fixed-length implementation with direct tests.
- **Naming and idiom:** Names such as Truncate, FixedLengthTruncator, truncationString, length, and TruncateFrom expose the contract, while extension methods, nullable annotations, interfaces, and ranges are idiomatic C#.
- **Tests:** TruncatorTests directly exercises null and empty values, exact and overlong text, custom and absent markers, multiple strategies, and left and right directions; the audit does not claim grapheme-safe behavior or omitted negative-length coverage.
- **Documentation:** XML comments and the generated API page define maximum length, markers, direction, null behavior, defaults, exceptions, and examples.
- **Traceability:** A learner can follow the simplest overload through one final overload into FixedLengthTruncator and close the same branches in one data-driven test class.
- **Maintainability:** Overload delegation prevents duplicated behavior, the interface localizes strategy changes, and direct tests protect the stable maximum-length and direction contract.
- **Educational value:** The path turns a familiar string operation into a compact lesson in overloads, interfaces, nullable contracts, slicing, direction symmetry, and boundary testing without hiding its UTF-16 limitation.

**Inspection record:** commit `ffc2b77c0f30d2fb176875841424379319d0ae9b`, inspected 2026-08-30. Review passes: Codex exact-pin gap research; independent Codex reviewer; Codex novice-accessibility re-review. Files inspected: `src/Humanizer/TruncateExtensions.cs`, `src/Humanizer/Truncation/ITruncator.cs`, `src/Humanizer/Truncation/FixedLengthTruncator.cs`, `src/Humanizer/Truncation/Truncator.cs`, `src/Humanizer/TruncateFrom.cs`, `tests/Humanizer.Tests/TruncatorTests.cs`, `website/docs/api/Humanizer.TruncateExtensions.md`, `readme.md`, `license.txt`. GitHub Linguist label: C#.

</details>

## Level 3 — Intermediate production software

### [FluentValidation/FluentValidation](https://github.com/FluentValidation/FluentValidation)

**Language 4 / Behavior 3 / Design 3 / Constraints 3 → Level 3**

**Source:** Production software

A strongly typed validation framework that turns fluent expression-based rules into synchronous or asynchronous validation pipelines.

**Why study it:** The validator path shows how a typed RuleFor expression becomes an authored asynchronous property-rule pipeline with conditions, cascades, dependent rules, cancellation, and structured failures.

**Short context:**

- A validator builds typed property rules, then evaluates their selectors, conditions, validator components, cascade policy, and dependent rules into validation failures.

**Prerequisites:**

- Basic familiarity with C# classes and interfaces, generics, delegates, nullable values, exceptions, asynchronous basics, and unit tests.

**Concepts this path develops:**

- Generic fluent rule-builder interfaces.
- Ordered async rule evaluation.
- Sync and async parity.

**What you can learn:**

- Use `src/FluentValidation/AbstractValidator.cs` to study the following transferable techniques and behaviors: Generic fluent builders, expression-tree property capture, cached accessors, validation contexts and selectors, ordered asynchronous components, conditions, class and rule cascades, dependent rules, cancellation, and sync-async parity.

**Learning path:**

- **Goal:** Understand how FluentValidation turns a typed RuleFor expression into an authored asynchronous property-rule pipeline with conditions, cascade behavior, dependent rules, cancellation, and failures.
- **Start here:** [`src/FluentValidation/AbstractValidator.cs`](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/src/FluentValidation/AbstractValidator.cs) — src/FluentValidation/AbstractValidator.cs contains RuleFor and ValidateInternalAsync, connecting typed rule declaration to selection, cancellation, class-level cascade, and rule execution.
- **Then read:**
  - [`src/FluentValidation/Internal/PropertyRule.cs`](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/src/FluentValidation/Internal/PropertyRule.cs)
  - [`src/FluentValidation/Internal/RuleBase.cs`](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/src/FluentValidation/Internal/RuleBase.cs)
  - [`src/FluentValidation/Internal/RuleBuilder.cs`](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/src/FluentValidation/Internal/RuleBuilder.cs)
  - [`src/FluentValidation.Tests/AbstractValidatorTester.cs`](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/src/FluentValidation.Tests/AbstractValidatorTester.cs)
  - [`src/FluentValidation.Tests/ConditionTests.cs`](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/src/FluentValidation.Tests/ConditionTests.cs)
  - [`src/FluentValidation.Tests/CascadingFailuresTester.cs`](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/src/FluentValidation.Tests/CascadingFailuresTester.cs)
  - [`src/FluentValidation.Tests/SyncAsyncParityTests.cs`](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/src/FluentValidation.Tests/SyncAsyncParityTests.cs)
- **Trace:** Follow RuleFor as it captures a typed expression and builds PropertyRule and RuleBuilder, then follow ValidateInternalAsync through cancellation and class-level cascade into PropertyRule.ValidateAsync, selector and condition checks, lazy accessor evaluation, validator components, failure creation, rule-level cascade, and dependent rules; use the focused tests to verify conditions, cascades, failures, and sync/async parity without treating generated output as the teaching source.

**Why this level:**

- **Language technique 4:** Expression processing and code generation materially shape the API and maintenance model alongside pervasive generic abstractions.
- **Behavioral reasoning 3:** Meaningful async, conditional, and cascade behavior recurs, but it remains a linear per-validation pipeline rather than an advanced distributed or concurrent state machine.
- **Design span 3:** Several meaningful framework boundaries contribute directly to one property validation.
- **Constraint burden 3:** Several material API, correctness, and reliability guarantees constrain changes, but they do not rise to interacting system-wide expert constraints in this bounded path.
- **Placement:** The four scores 4/3/3/3 sum to 13; their arithmetic mean is 3.25 and rounds half-up to Level 3. The published result is Level 3.

**License:** Apache-2.0 ([evidence 1](https://github.com/FluentValidation/FluentValidation/blob/daa00b795450881c233253488e3ddeb362f59f56/License.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** FluentValidation is released as production validation infrastructure used in .NET services and applications.

**Language evidence:** Validator composition, rule components, expression parsing, selectors, conditions, async execution, messages, and results are C#.

**Coding relevance:**

The validation vocabulary is short and programming-led; the selected authored async path teaches expression-based APIs, generic fluent builders, cached accessors, callbacks, cancellation, conditions, and ordered rule composition.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The authored asynchronous implementation explicitly separates validator orchestration, property rules, rule components, conditions, cascades, failures, and dependencies.
- **Architecture:** AbstractValidator owns the rule set, PropertyRule evaluates one property, RuleBase stores shared policy, RuleBuilder composes validators, and context and selector abstractions control execution.
- **Naming and idiom:** RuleFor, ValidateInternalAsync, PropertyRule, RuleBuilder, ValidationContext, selector, cascade, dependent rules, and ValidationFailure state pipeline intent.
- **Tests:** The selected validator, condition, cascade, and sync-async-parity suites cover selection, conditions, short circuits, dependencies, cancellation, failures, and generated counterpart agreement.
- **Documentation:** FluentValidation's rules, conditions, cascade, dependent-rule, asynchronous-validation, and error documentation explains the selected public and runtime contracts.
- **Traceability:** A RuleFor expression can be followed through PropertyRule and RuleBuilder construction into ValidateInternalAsync, selector and condition checks, component evaluation, failures, cascades, and dependencies.
- **Maintainability:** Strong generic boundaries, an inspectable authored async source, generated parity checks, and focused policy tests constrain changes across the fluent API.
- **Educational value:** The path shows how a declarative type-safe API becomes an ordered cancellable runtime without treating generated synchronous code as the teaching source.

**Inspection record:** commit `daa00b795450881c233253488e3ddeb362f59f56`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/FluentValidation/AbstractValidator.cs`, `src/FluentValidation/Internal/PropertyRule.cs`, `src/FluentValidation/Internal/RuleBase.cs`, `src/FluentValidation/Internal/RuleBuilder.cs`, `src/FluentValidation.Tests/AbstractValidatorTester.cs`, `src/FluentValidation.Tests/ConditionTests.cs`, `src/FluentValidation.Tests/CascadingFailuresTester.cs`, `src/FluentValidation.Tests/SyncAsyncParityTests.cs`, `License.txt`. GitHub Linguist label: C#.

</details>

### [serilog/serilog](https://github.com/serilog/serilog)

**Language 3 / Behavior 3 / Design 3 / Constraints 4 → Level 3**

**Source:** Production software

A structured logging core that turns message templates and properties into immutable events routed through enrichers, filters, and sinks.

**Why study it:** The Logger path shows how Serilog parses and caches a message template, binds structured properties, enriches and filters one event, emits it to sinks, and contains extension failures.

**Short context:**

- A structured log event combines a parsed message template, bound properties, a level, timestamp, exception, and optional trace identifiers before enrichers, filters, and sinks process it.

**Prerequisites:**

- Basic familiarity with C# classes and interfaces, generics, delegates, nullable values, exceptions, asynchronous basics, and unit tests.

**Concepts this path develops:**

- Interface-composed enrichers, filters, and sinks.
- Message-template cache state.
- Stable message-template and property semantics.

**What you can learn:**

- Use `src/Serilog/Core/Logger.cs` to study the following transferable techniques and behaviors: Message-template tokenization, template caching, property binding, immutable log events, contextual enrichment, filtering, sink dispatch, dynamic levels, trace context, failure isolation, and synchronous and asynchronous disposal.

**Learning path:**

- **Goal:** Understand how Serilog parses and caches a message template, binds one structured event, enriches and filters it, emits it to sinks, and contains extension failures.
- **Start here:** [`src/Serilog/Core/Logger.cs`](https://github.com/serilog/serilog/blob/49b5339ce85385dc52d4d8e8f2b8308becf23506/src/Serilog/Core/Logger.cs) — src/Serilog/Core/Logger.cs owns Write, where level checks, message-template lookup, property binding, LogEvent creation, enrichment, filtering, and sink emission form one complete trace.
- **Then read:**
  - [`src/Serilog/LoggerConfiguration.cs`](https://github.com/serilog/serilog/blob/49b5339ce85385dc52d4d8e8f2b8308becf23506/src/Serilog/LoggerConfiguration.cs)
  - [`src/Serilog/Core/Pipeline/MessageTemplateCache.cs`](https://github.com/serilog/serilog/blob/49b5339ce85385dc52d4d8e8f2b8308becf23506/src/Serilog/Core/Pipeline/MessageTemplateCache.cs)
  - [`src/Serilog/Parsing/MessageTemplateParser.cs`](https://github.com/serilog/serilog/blob/49b5339ce85385dc52d4d8e8f2b8308becf23506/src/Serilog/Parsing/MessageTemplateParser.cs)
  - [`src/Serilog/Events/LogEvent.cs`](https://github.com/serilog/serilog/blob/49b5339ce85385dc52d4d8e8f2b8308becf23506/src/Serilog/Events/LogEvent.cs)
  - [`test/Serilog.Tests/Core/LoggerTests.cs`](https://github.com/serilog/serilog/blob/49b5339ce85385dc52d4d8e8f2b8308becf23506/test/Serilog.Tests/Core/LoggerTests.cs)
  - [`test/Serilog.Tests/Parsing/MessageTemplateParserTests.cs`](https://github.com/serilog/serilog/blob/49b5339ce85385dc52d4d8e8f2b8308becf23506/test/Serilog.Tests/Parsing/MessageTemplateParserTests.cs)
- **Trace:** Follow Logger.Write from level checking through MessageTemplateCache and MessageTemplateParser, property binding, LogEvent construction, enrichment, filtering, and sink emission; then correlate parser tokenization, property precedence, enricher-failure containment, dynamic level switches, trace context, binding, disposal, and async-disposal tests.

**Why this level:**

- **Language technique 3:** Substantial framework abstraction and typed pipeline idioms recur without reflection, unsafe code, or pervasive code generation.
- **Behavioral reasoning 3:** Caching, contextual state, events, failure paths, and cleanup materially affect the trace without expert concurrent scheduling.
- **Design span 3:** Several meaningful framework boundaries contribute directly to one structured event.
- **Constraint burden 4:** Several interacting compatibility, reliability, extension, and resource guarantees constrain pipeline changes.
- **Placement:** The four scores 3/3/3/4 sum to 13; their arithmetic mean is 3.25 and rounds half-up to Level 3. The published result is Level 3.

**License:** Apache-2.0 ([evidence 1](https://github.com/serilog/serilog/blob/49b5339ce85385dc52d4d8e8f2b8308becf23506/LICENSE))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** Serilog is maintained and released as the core event pipeline for a production logging ecosystem of sinks and framework integrations.

**Language evidence:** Logger pipelines, structured events, message-template parsing, enrichment, filtering, sinks, configuration, and level switching are C#.

**Coding relevance:**

The logging model is concise and familiar; the path primarily teaches parser and cache design, interface-driven pipelines, contextual enrichment, fault containment, resource cleanup, and stable extension contracts.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** Logger.Write names each pipeline stage and makes disabled levels, binding failures, extension failures, filtering, and disposal behavior explicit.
- **Architecture:** LoggerConfiguration assembles the Logger, MessageTemplateCache and MessageTemplateParser produce templates, LogEvent carries data, and enricher, filter, and sink interfaces extend processing.
- **Naming and idiom:** Write, IsEnabled, MessageTemplateCache, MessageTemplateParser, BindMessageTemplate, LogEvent, Enrich, Filter, and sink preserve structured-logging vocabulary.
- **Tests:** LoggerTests and MessageTemplateParserTests cover tokenization, binding, cache-facing behavior, contextual properties, enrichers, filters, dynamic levels, trace capture, failures, and disposal.
- **Documentation:** Serilog's message-template, enrichment, filtering, sink, level, and lifecycle documentation explains the contracts implemented by this selected event path.
- **Traceability:** A Write call can be followed through level gating, cached parsing, property binding, LogEvent creation, enrichment, filtering, sink emission, and corresponding parser and logger assertions.
- **Maintainability:** Stable event and extension interfaces, a bounded template cache, explicit failure containment, and disposal tests localize pipeline changes.
- **Educational value:** The path demonstrates how a production structured logger turns text-like input into a typed extensible event while preserving reliability at every extension seam.

**Inspection record:** commit `49b5339ce85385dc52d4d8e8f2b8308becf23506`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/Serilog/Core/Logger.cs`, `src/Serilog/LoggerConfiguration.cs`, `src/Serilog/Core/Pipeline/MessageTemplateCache.cs`, `src/Serilog/Parsing/MessageTemplateParser.cs`, `src/Serilog/Events/LogEvent.cs`, `test/Serilog.Tests/Core/LoggerTests.cs`, `test/Serilog.Tests/Parsing/MessageTemplateParserTests.cs`, `LICENSE`. GitHub Linguist label: C#.

</details>

## Level 4 — Advanced

### [DapperLib/Dapper](https://github.com/DapperLib/Dapper)

**Language 4 / Behavior 3 / Design 3 / Constraints 4 → Level 4**

**Source:** Production software

A lightweight object mapper that extends database connections with fast SQL execution and row-to-object materialization.

**Why study it:** The type-deserializer path shows how Dapper converts a data-reader row into a typed object by caching generated IL while preserving constructor, member, null, conversion, tuple, and type-handler contracts.

**Short context:**

- An ADO.NET data reader exposes typed columns for the current database row, which Dapper maps into a requested object constructor and members.

**Prerequisites:**

- Working familiarity with C# classes and interfaces, generics, delegates, nullable values, exceptions, asynchronous basics, and unit tests, plus experience tracing behavior across several production files.

**Concepts this path develops:**

- Reflection-driven constructor and member selection.
- Typed deserializer caching.
- Provider and runtime compatibility.

**What you can learn:**

- Use `Dapper/SqlMapper.TypeDeserializerCache.cs` to study the following transferable techniques and behaviors: Reflection-driven mapping, typed deserializer caches, DynamicMethod and ILGenerator, constructor selection, member binding, column conversion, null handling, tuple materialization, custom type handlers, and hot-path performance.

**Learning path:**

- **Goal:** Understand how Dapper converts one data-reader row into a typed object by caching a generated deserializer and honoring constructor, member, conversion, null, and type-handler contracts.
- **Start here:** [`Dapper/SqlMapper.TypeDeserializerCache.cs`](https://github.com/DapperLib/Dapper/blob/6d48ef664acc7298c649e2d449d903b3360d5a90/Dapper/SqlMapper.TypeDeserializerCache.cs) — Dapper/SqlMapper.TypeDeserializerCache.cs owns the row-shape and target-type cache that supplies generated materializer delegates, making it the clearest entrance before IL emission and type mapping.
- **Then read:**
  - [`Dapper/SqlMapper.cs`](https://github.com/DapperLib/Dapper/blob/6d48ef664acc7298c649e2d449d903b3360d5a90/Dapper/SqlMapper.cs)
  - [`Dapper/DefaultTypeMap.cs`](https://github.com/DapperLib/Dapper/blob/6d48ef664acc7298c649e2d449d903b3360d5a90/Dapper/DefaultTypeMap.cs)
  - [`tests/Dapper.Tests/ConstructorTests.cs`](https://github.com/DapperLib/Dapper/blob/6d48ef664acc7298c649e2d449d903b3360d5a90/tests/Dapper.Tests/ConstructorTests.cs)
  - [`tests/Dapper.Tests/TypeHandlerTests.cs`](https://github.com/DapperLib/Dapper/blob/6d48ef664acc7298c649e2d449d903b3360d5a90/tests/Dapper.Tests/TypeHandlerTests.cs)
- **Trace:** Follow TypeDeserializerCache as it keys and reuses row-reader delegates, then follow SqlMapper.GetTypeDeserializer and GenerateDeserializerFromMap as they inspect columns, select constructors or members through DefaultTypeMap, and emit conversion, null, tuple, and type-handler IL; correlate constructor selection and custom-handler behavior in the focused tests.

**Why this level:**

- **Language technique 4:** Reflection and runtime code generation are central rather than incidental to the materialization path.
- **Behavioral reasoning 3:** Cache state and numerous mapping branches materially affect behavior, but the bounded row conversion remains synchronous and lacks advanced nonlocal scheduling.
- **Design span 3:** Several meaningful framework boundaries contribute directly to one row materialization.
- **Constraint burden 4:** Several interacting correctness, compatibility, extensibility, and performance guarantees constrain changes to the emitted materializer.
- **Placement:** The four scores 4/3/3/4 sum to 14; their arithmetic mean is 3.50 and rounds half-up to Level 4. The published result is Level 4.

**License:** Apache-2.0 ([evidence 1](https://github.com/DapperLib/Dapper/blob/6d48ef664acc7298c649e2d449d903b3360d5a90/License.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** Dapper is released as production data-access infrastructure and is used by large .NET applications, including its original Stack Overflow use case.

**Language evidence:** SQL execution, parameter handling, mapping, caching, async operations, type handlers, and AOT support are implemented in C#.

**Coding relevance:**

This row-mapping context fits in a short paragraph; the selected path teaches reflection, dynamic IL generation, typed caches, constructor and member selection, conversion, null handling, and extensibility rather than database theory.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The bounded materializer path names cache lookup, type-map selection, constructor and member branches, conversion, null handling, tuple logic, and type-handler emission despite intricate IL.
- **Architecture:** TypeDeserializerCache stores delegates, SqlMapper emits materializers, DefaultTypeMap selects constructors and members, and type handlers provide an explicit extension point.
- **Naming and idiom:** TypeDeserializerCache, GetReader, GetTypeDeserializer, GenerateDeserializerFromMap, DefaultTypeMap, FindConstructor, members, and type handlers expose row materialization.
- **Tests:** ConstructorTests and TypeHandlerTests cover constructor selection, member mapping, null and conversion behavior, custom handlers, error cases, and cache-facing compatibility.
- **Documentation:** The README, API examples, and package documentation provide the mapping and type-handler context needed to follow the selected generated materializer.
- **Traceability:** A reader shape can be followed through TypeDeserializerCache into GetTypeDeserializer, DefaultTypeMap selection, emitted load and conversion IL, and constructor or type-handler tests.
- **Maintainability:** Named cache and type-map seams plus compatibility tests constrain changes to generated code that sits on a performance-critical public boundary.
- **Educational value:** The path demonstrates how reflection and runtime code generation can produce a fast typed mapping API while retaining explicit extension and compatibility rules.

**Inspection record:** commit `6d48ef664acc7298c649e2d449d903b3360d5a90`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `Dapper/SqlMapper.TypeDeserializerCache.cs`, `Dapper/SqlMapper.cs`, `Dapper/DefaultTypeMap.cs`, `tests/Dapper.Tests/ConstructorTests.cs`, `tests/Dapper.Tests/TypeHandlerTests.cs`, `License.txt`. GitHub Linguist label: C#.

</details>

### [dotnet/aspnetcore](https://github.com/dotnet/aspnetcore)

**Language 4 / Behavior 3 / Design 3 / Constraints 4 → Level 4**

**Source:** Production software

The ASP.NET Core web platform, including HTTP servers, middleware, routing, hosting, MVC, Razor, Blazor, SignalR, security, and deployment integrations.

**Why study it:** The ApplicationBuilder path shows how ASP.NET Core folds middleware into an ordered request-delegate pipeline and adapts both conventional and factory-created components with dependency injection and reliable release.

**Short context:**

- An ASP.NET Core request pipeline is an ordered nesting of middleware delegates; each component can perform work before and after calling the next component or short-circuit the request.

**Prerequisites:**

- Working familiarity with C# classes and interfaces, generics, delegates, nullable values, exceptions, asynchronous basics, and unit tests, plus experience tracing behavior across several production files.

**Concepts this path develops:**

- Higher-order RequestDelegate composition.
- Ordered nested async execution and short circuiting.
- Middleware signature and DI compatibility.

**What you can learn:**

- Use `src/Http/Http/src/Builder/ApplicationBuilder.cs` to study the following transferable techniques and behaviors: Higher-order RequestDelegate composition, reverse pipeline folding, asynchronous ordering and short circuits, reflection-based Invoke discovery, expression compilation, AOT-compatible fallback, injected and keyed services, per-request activation, and finally-based release.

**Learning path:**

- **Goal:** Understand how ASP.NET Core composes an ordered request-delegate pipeline and adapts conventional or factory-created middleware with dependency injection and reliable per-request release.
- **Start here:** [`src/Http/Http/src/Builder/ApplicationBuilder.cs`](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/src/Http/Http/src/Builder/ApplicationBuilder.cs) — ApplicationBuilder.cs contains Use and Build, which reveal how middleware factories are stored and folded around a terminal RequestDelegate before adaptation details are introduced.
- **Then read:**
  - [`src/Http/Http.Abstractions/src/IApplicationBuilder.cs`](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/src/Http/Http.Abstractions/src/IApplicationBuilder.cs)
  - [`src/Http/Http.Abstractions/src/Extensions/UseMiddlewareExtensions.cs`](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/src/Http/Http.Abstractions/src/Extensions/UseMiddlewareExtensions.cs)
  - [`src/Http/Http.Abstractions/src/IMiddleware.cs`](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/src/Http/Http.Abstractions/src/IMiddleware.cs)
  - [`src/Http/Http.Abstractions/src/IMiddlewareFactory.cs`](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/src/Http/Http.Abstractions/src/IMiddlewareFactory.cs)
  - [`src/Http/Http/src/MiddlewareFactory.cs`](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/src/Http/Http/src/MiddlewareFactory.cs)
  - [`src/Http/Http/test/ApplicationBuilderTests.cs`](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/src/Http/Http/test/ApplicationBuilderTests.cs)
  - [`src/Http/Http.Abstractions/test/UseMiddlewareTest.cs`](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/src/Http/Http.Abstractions/test/UseMiddlewareTest.cs)
- **Trace:** Follow ApplicationBuilder.Use as it stores middleware factories and Build as it folds them in reverse around the terminal delegate, then follow UseMiddlewareExtensions as it validates Invoke or InvokeAsync, chooses compiled-expression or reflection fallback service injection, or creates IMiddleware per request and releases it in finally; correlate ordering, terminal, endpoint, signature, service, factory, and release tests.

**Why this level:**

- **Language technique 4:** Reflection, expression compilation, and sophisticated delegate composition are central to middleware adaptation.
- **Behavioral reasoning 3:** Async ordering, lifecycle, and fallback behavior materially affect requests, but the bounded pipeline does not require advanced protocol or distributed state reasoning.
- **Design span 3:** Several meaningful framework boundaries contribute directly to one middleware invocation.
- **Constraint burden 4:** Several interacting compatibility, reliability, extensibility, and resource guarantees constrain the pipeline.
- **Placement:** The four scores 4/3/3/4 sum to 14; their arithmetic mean is 3.50 and rounds half-up to Level 4. The published result is Level 4.

**License:** MIT ([evidence 1](https://github.com/dotnet/aspnetcore/blob/8c1a406592b06b954acac509fa4725ca560b2e53/LICENSE.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** Microsoft ships ASP.NET Core as the production web framework and server stack for modern .NET applications.

**Language evidence:** HTTP abstractions, Kestrel, hosting, routing, middleware, MVC, Razor, Blazor, SignalR, authentication, and data protection are predominantly C# with first-party web client code.

**Coding relevance:**

The middleware model fits in a short prerequisite paragraph; this corrected path teaches delegate composition, reflection and expression compilation, dependency injection, per-request activation and release, async control flow, and runtime fallback rather than HTTP protocol rules.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** ApplicationBuilder and UseMiddlewareExtensions make ordering, terminal behavior, signature validation, invocation branches, service resolution, and release paths explicit.
- **Architecture:** IApplicationBuilder defines composition, ApplicationBuilder builds delegates, UseMiddlewareExtensions supplies conventional and interface binders, and IMiddlewareFactory owns per-request activation and release.
- **Naming and idiom:** Use, Build, RequestDelegate, UseMiddleware, Invoke, InvokeAsync, IMiddleware, IMiddlewareFactory, Create, and Release expose the pipeline contract.
- **Tests:** ApplicationBuilderTests and UseMiddlewareTest cover ordering, terminal and endpoint mistakes, signature validation, dependency and keyed-service injection, dynamic-code fallback, factory failures, and release.
- **Documentation:** Source documentation for ApplicationBuilder, UseMiddlewareExtensions, the middleware interfaces, and MiddlewareFactory explains composition, invocation, dependency injection, activation, and release contracts.
- **Traceability:** A Use call can be followed into reverse Build folding, conventional reflection or compiled binding, interface-factory creation, asynchronous invocation, and finally release with direct tests.
- **Maintainability:** Stable delegate and factory interfaces, explicit binder branches, AOT fallback coverage, and lifecycle tests isolate middleware extensibility from pipeline composition.
- **Educational value:** The path demonstrates how a compact higher-order pipeline supports reflection, dependency injection, per-request ownership, and ahead-of-time constraints without losing traceability.

**Inspection record:** commit `8c1a406592b06b954acac509fa4725ca560b2e53`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/Http/Http/src/Builder/ApplicationBuilder.cs`, `src/Http/Http.Abstractions/src/IApplicationBuilder.cs`, `src/Http/Http.Abstractions/src/Extensions/UseMiddlewareExtensions.cs`, `src/Http/Http.Abstractions/src/IMiddleware.cs`, `src/Http/Http.Abstractions/src/IMiddlewareFactory.cs`, `src/Http/Http/src/MiddlewareFactory.cs`, `src/Http/Http/test/ApplicationBuilderTests.cs`, `src/Http/Http.Abstractions/test/UseMiddlewareTest.cs`, `LICENSE.txt`. GitHub Linguist label: C#.

</details>

## Level 5 — Expert

### [dotnet/roslyn](https://github.com/dotnet/roslyn)

**Language 5 / Behavior 5 / Design 5 / Constraints 5 → Level 5**

**Source:** Production software

The open-source C# and Visual Basic compiler platform that exposes syntax, semantic, diagnostic, compilation, and emit APIs used by the .NET toolchain.

**Why study it:** The compilation-to-emit path shows how a platform-scale C# system turns immutable syntax, references, and options into diagnostics or deterministic PE and PDB output while coordinating binding, flow analysis, concurrent method compilation, lowering, IL generation, metadata, compatibility, and cleanup.

**Short context:**

- A compiler parses source into syntax, declares and binds symbols, analyzes and lowers method bodies, generates intermediate-language instructions, and serializes an assembly plus optional debug information.

**Prerequisites:**

- Strong working familiarity with C# classes and interfaces, generics, delegates, nullable values, exceptions, asynchronous basics, and unit tests, plus experience tracing state, resources, or asynchronous control flow across many production files.

**Concepts this path develops:**

- Recursive generic symbol, visitor, builder, and CCI adapter hierarchies.
- Staged parse, declaration, bind, flow, lower, codegen, and serialization state.
- C# language and CLR metadata correctness.

**What you can learn:**

- Use `src/Compilers/Core/Portable/Compilation/Compilation.cs` to study the following transferable techniques and behaviors: Public stream and option validation, immutable compilation snapshots, staged diagnostics, module-builder specialization, concurrent symbol traversal, binding and flow analysis, lowering and instrumentation, IL generation, entry-point selection, deterministic PE and PDB serialization, cancellation, pooled resources, and compatibility-preserving APIs.

**Learning path:**

- **Goal:** Understand how Roslyn validates an emit request and turns one immutable CSharpCompilation into either stable diagnostics or deterministic PE and PDB output.
- **Start here:** [`src/Compilers/Core/Portable/Compilation/Compilation.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/Core/Portable/Compilation/Compilation.cs) — Compilation.cs owns the public Emit boundary, validates streams and options, creates the language-specific module builder, invokes compilation, generates resources and documentation, gates serialization on diagnostics, and returns EmitResult.
- **Then read:**
  - [`src/Compilers/CSharp/Portable/Compilation/CSharpCompilation.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Portable/Compilation/CSharpCompilation.cs)
  - [`src/Compilers/CSharp/Portable/Compiler/MethodCompiler.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Portable/Compiler/MethodCompiler.cs)
  - [`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter.cs)
  - [`src/Compilers/CSharp/Portable/CodeGen/CodeGenerator.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Portable/CodeGen/CodeGenerator.cs)
  - [`src/Compilers/CSharp/Portable/Emitter/Model/PEModuleBuilder.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Portable/Emitter/Model/PEModuleBuilder.cs)
  - [`src/Compilers/Core/Portable/Emit/CommonPEModuleBuilder.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/Core/Portable/Emit/CommonPEModuleBuilder.cs)
  - [`src/Compilers/Core/Portable/PEWriter/PeWriter.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/Core/Portable/PEWriter/PeWriter.cs)
  - [`src/Compilers/CSharp/Test/Emit/Emit/CompilationEmitTests.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Test/Emit/Emit/CompilationEmitTests.cs)
  - [`src/Compilers/CSharp/Test/Emit/Emit/EntryPointTests.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Test/Emit/Emit/EntryPointTests.cs)
  - [`src/Compilers/CSharp/Test/Emit/Emit/DeterministicTests.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Test/Emit/Emit/DeterministicTests.cs)
  - [`src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncMainTests.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncMainTests.cs)
  - [`src/Compilers/CSharp/Test/Emit2/PDB/CSharpDeterministicBuildCompilationTests.cs`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/src/Compilers/CSharp/Test/Emit2/PDB/CSharpDeterministicBuildCompilationTests.cs)
  - [`docs/wiki/Roslyn-Overview.md`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/docs/wiki/Roslyn-Overview.md)
  - [`docs/compilers/README.md`](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/docs/compilers/README.md)
- **Trace:** Follow Compilation.Emit through stream and option checks into CheckOptionsAndCreateModuleBuilder, then into CSharpCompilation.CreateModuleBuilder and CompileMethods; trace parse and declaration diagnostics into MethodCompiler's concurrent symbol traversal, binding, flow analysis, LocalRewriter transformations, CodeGenerator IL construction, async entry-point synthesis, and PEModuleBuilder metadata; follow stored method bodies and entry point through CommonPEModuleBuilder into PeWriter and return to Compilation.SerializeToPeStream for deterministic PE and optional PDB output, then correlate staged errors, entry-point rules, executed async Main, emitted artifacts, platform changes, and repeatable PE, MVID, and supported PDB data in the selected tests.

**Why this level:**

- **Language technique 5:** Several advanced C# mechanisms interact pervasively: recursive generic and visitor hierarchies, language-specific adapters, synthesized symbols, nullable and pattern-based modeling, task concurrency, pooled ownership, immutable snapshots, and low-level metadata and IL builders.
- **Behavioral reasoning 5:** Concurrency, staged transformation state, diagnostics, synthesized code, failure containment, cancellation, and resource lifecycles interact pervasively and require expert nonlocal reasoning.
- **Design span 5:** The representative behavior coordinates several major compiler and runtime-format subsystems through shared abstractions and language-specific implementations.
- **Constraint burden 5:** Language semantics, emitted-runtime correctness, stable diagnostics, concurrency, determinism, compatibility, performance, resources, and platform-specific output guarantees constrain changes across the entire path.
- **Placement:** The four scores 5/5/5/5 sum to 20; their arithmetic mean is 5.00. Four expert dimensions satisfy the Level 5 guardrail, so the published result is Level 5.

**License:** MIT ([evidence 1](https://github.com/dotnet/roslyn/blob/8323a94cb432bbffad016d4f6d7e04ee0f8419f2/License.txt))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** Roslyn supplies the production C# and Visual Basic compilers and code-analysis APIs shipped through the .NET SDK, Visual Studio, and Microsoft.CodeAnalysis packages.

**Language evidence:** The selected public compilation API, C# compiler pipeline, lowering, IL generation, emitter model, and focused compiler tests are implemented in first-party C#; GitHub also reports C# as the repository's primary language.

**Coding relevance:**

The compiler vocabulary fits in a bounded primer and is documented by the project; the selected path primarily teaches transferable immutable modeling, staged pipelines, concurrency, diagnostics, transformation passes, serialization, deterministic builds, compatibility, and resource discipline.

The learner-facing short context appears above.

**Eight-part quality gate:**

- **Source quality:** The emit boundary, diagnostic stages, fork-join strategy, per-method failure isolation, lowering handoff, serialization gates, and cleanup are explicit and carry unusually detailed invariant comments.
- **Architecture:** Common Compilation orchestrates the lifecycle, CSharpCompilation specializes language diagnostics and module creation, MethodCompiler binds and lowers symbols, LocalRewriter transforms bound trees, CodeGenerator produces IL, and PEModuleBuilder exposes metadata to the serializer.
- **Naming and idiom:** Compilation, Emit, CreateModuleBuilder, CompileMethods, MethodCompiler, BindMethodBody, FlowAnalysisPass, LowerBodyOrInitializer, CodeGenerator, PEModuleBuilder, diagnostics, and EmitResult preserve compiler-stage vocabulary.
- **Tests:** CompilationEmitTests directly checks staged errors and emitted stream behavior, EntryPointTests exercises executable entry-point selection and diagnostics, CodeGenAsyncMainTests executes async entry points and verifies synthesized forwarding IL, DeterministicTests compares module identifiers and emitted bytes, and the deterministic-build PDB suite checks embedded PDB options and reference metadata. Coverage of the complete platform is intentionally distributed across many suites.
- **Documentation:** The repository overview, compiler support guide, and source documentation explain the public compiler pipeline, immutable compilation model, diagnostics, emit semantics, compatibility overloads, concurrency invariants, platform support, and major representation boundaries.
- **Traceability:** A public Emit call can be followed through option validation, language-specific module construction, diagnostics, method compilation, lowering, IL and metadata production, PE and PDB serialization, EmitResult, and end-to-end assertions.
- **Maintainability:** Stable phase boundaries, immutable public models, deterministic tests, per-method diagnostic bags, cancellation checks, pooled-resource cleanup, compatibility annotations, and explicit finish hooks make cross-cutting changes reviewable despite the platform scale.
- **Educational value:** The path is a rare production example of a complete compiler backend and public platform API in which concurrency, transformation passes, diagnostics, compatibility, deterministic output, and failure discipline remain observable.

**Inspection record:** commit `8323a94cb432bbffad016d4f6d7e04ee0f8419f2`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/Compilers/Core/Portable/Compilation/Compilation.cs`, `src/Compilers/CSharp/Portable/Compilation/CSharpCompilation.cs`, `src/Compilers/CSharp/Portable/Compiler/MethodCompiler.cs`, `src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter.cs`, `src/Compilers/CSharp/Portable/CodeGen/CodeGenerator.cs`, `src/Compilers/CSharp/Portable/Emitter/Model/PEModuleBuilder.cs`, `src/Compilers/Core/Portable/Emit/CommonPEModuleBuilder.cs`, `src/Compilers/Core/Portable/PEWriter/PeWriter.cs`, `src/Compilers/CSharp/Test/Emit/Emit/CompilationEmitTests.cs`, `src/Compilers/CSharp/Test/Emit/Emit/EntryPointTests.cs`, `src/Compilers/CSharp/Test/Emit/Emit/DeterministicTests.cs`, `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncMainTests.cs`, `src/Compilers/CSharp/Test/Emit2/PDB/CSharpDeterministicBuildCompilationTests.cs`, `docs/wiki/Roslyn-Overview.md`, `docs/compilers/README.md`, `README.md`, `License.txt`. GitHub Linguist label: C#.

</details>

### [dotnet/runtime](https://github.com/dotnet/runtime)

**Language 4 / Behavior 5 / Design 4 / Constraints 5 → Level 5**

**Source:** Production software

The cross-platform .NET runtime, including the CLR, JIT, garbage collector, type system, core libraries, interop, diagnostics, and native hosting.

**Why study it:** The TaskAwaiter path exposes how .NET registers and runs an await continuation while preserving contexts, scheduler policy, race safety, inlining rules, fault behavior, and forced asynchronous execution.

**Prerequisites:**

- Strong working familiarity with C# classes and interfaces, generics, delegates, nullable values, exceptions, asynchronous basics, and unit tests, plus experience tracing state, resources, or asynchronous control flow across many production files.

**Concepts this path develops:**

- Awaiter and async-state-machine interfaces.
- Lock-free registration versus completion races.
- Memory ordering and exactly-once continuation execution.

**What you can learn:**

- Use `src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/TaskAwaiter.cs` to study the following transferable techniques and behaviors: Awaiter and async-state-machine interfaces, Task continuation registration, SynchronizationContext and TaskScheduler capture, ExecutionContext flow, lock-free completion races, inline versus queued execution, ThreadPool scheduling, cancellation, faults, and exactly-once guarantees.

**Learning path:**

- **Goal:** Understand how an awaited Task registers and eventually runs a continuation while preserving execution context, scheduler and synchronization-context policy, race safety, inlining rules, and asynchronous-continuation guarantees.
- **Start here:** [`src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/TaskAwaiter.cs`](https://github.com/dotnet/runtime/blob/c4eee2b76e574b0dd6cfe3387220a905ba69aca6/src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/TaskAwaiter.cs) — TaskAwaiter.cs contains OnCompletedInternal, the compiler-facing handoff that turns an await into Task continuation registration with explicit context and scheduling policy.
- **Then read:**
  - [`src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/Task.cs`](https://github.com/dotnet/runtime/blob/c4eee2b76e574b0dd6cfe3387220a905ba69aca6/src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/Task.cs)
  - [`src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/TaskContinuation.cs`](https://github.com/dotnet/runtime/blob/c4eee2b76e574b0dd6cfe3387220a905ba69aca6/src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/TaskContinuation.cs)
  - [`src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/ThreadPoolTaskScheduler.cs`](https://github.com/dotnet/runtime/blob/c4eee2b76e574b0dd6cfe3387220a905ba69aca6/src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/ThreadPoolTaskScheduler.cs)
  - [`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/System.Runtime.CompilerServices/TaskAwaiterTests.cs`](https://github.com/dotnet/runtime/blob/c4eee2b76e574b0dd6cfe3387220a905ba69aca6/src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/System.Runtime.CompilerServices/TaskAwaiterTests.cs)
  - [`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/RunContinuationsAsynchronouslyTests.cs`](https://github.com/dotnet/runtime/blob/c4eee2b76e574b0dd6cfe3387220a905ba69aca6/src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/RunContinuationsAsynchronouslyTests.cs)
  - [`src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/ExecutionContextFlowTest.cs`](https://github.com/dotnet/runtime/blob/c4eee2b76e574b0dd6cfe3387220a905ba69aca6/src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/ExecutionContextFlowTest.cs)
- **Trace:** Follow TaskAwaiter.OnCompletedInternal into Task.SetContinuationForAwait as it chooses a SynchronizationContext, non-default TaskScheduler, ExecutionContext-capturing continuation, or direct state-machine registration; follow AddTaskContinuation's completion race and FinishContinuations into AwaitTaskContinuation inlining or ThreadPoolTaskScheduler queuing, then correlate scheduler/context capture, ConfigureAwait, forced asynchronous continuations, execution-context lifetime, and race behavior in the focused tests.

**Why this level:**

- **Language technique 4:** Advanced async, generic, low-level synchronization, and runtime-specific C# techniques are central, while the bounded path does not require multiple pervasive Level 5 language mechanisms.
- **Behavioral reasoning 5:** Multiple expert concurrency, scheduling, lifecycle, and nonlocal state concerns are pervasive and tightly coupled.
- **Design span 4:** The trace crosses broad runtime architecture and many core subsystems while remaining bounded to continuation execution.
- **Constraint burden 5:** System-wide runtime safety, correctness, compatibility, observability, and performance guarantees interact throughout the path.
- **Placement:** The four scores 4/5/4/5 sum to 18; their arithmetic mean is 4.50 and rounds half-up to Level 5. The published result is Level 5.

**License:** MIT ([evidence 1](https://github.com/dotnet/runtime/blob/c4eee2b76e574b0dd6cfe3387220a905ba69aca6/LICENSE.TXT))

<details>
<summary>Quality and review evidence</summary>

**Purpose evidence:** Microsoft ships this repository as the production runtime and standard libraries underlying .NET applications across operating systems and architectures.

**Language evidence:** Core libraries are C#, while the CLR, garbage collector, JIT, native hosting, interop, and platform layers use C++, C, and assembly as first-party runtime implementation.

**Coding relevance:**

The selected all-C# path is core transferable runtime programming: await continuation registration, captured execution context, synchronization and scheduler choice, lock-free completion, inlining, queuing, cancellation, and error behavior.

No specialist domain context is required.

**Eight-part quality gate:**

- **Source quality:** TaskAwaiter, Task, continuation, and scheduler code documents registration, completion races, context capture, inlining, queuing, cancellation, and debugger invariants extensively.
- **Architecture:** The compiler awaiter boundary delegates to Task state, specialized continuation objects, SynchronizationContext, TaskScheduler, ExecutionContext, and ThreadPoolTaskScheduler.
- **Naming and idiom:** OnCompletedInternal, SetContinuationForAwait, AddTaskContinuation, FinishContinuations, AwaitTaskContinuation, RunContinuationsAsynchronously, and scheduler names expose the lifecycle.
- **Tests:** The selected TaskAwaiter, RunContinuationsAsynchronously, and ExecutionContextFlow suites cover scheduler and context capture, ConfigureAwait, races, forced queuing, context lifetime, faults, and platform cases.
- **Documentation:** Extensive invariants in the TaskAwaiter, Task, continuation, and scheduler source comments document context capture, continuation scheduling, race handling, and exactly-once execution for this path.
- **Traceability:** An await can be followed from TaskAwaiter.OnCompletedInternal through continuation selection and race-safe registration into completion-time inlining or ThreadPoolTaskScheduler queuing and focused tests.
- **Maintainability:** Documented invariants, specialized continuation types, low-level synchronization boundaries, and targeted concurrency tests protect a performance-critical runtime contract.
- **Educational value:** The path gives expert learners a concrete account of async continuation semantics beneath the language syntax, including the races and context policies ordinary code depends on.

**Inspection record:** commit `c4eee2b76e574b0dd6cfe3387220a905ba69aca6`, inspected 2026-08-29. Review passes: Codex primary pass; independent Codex verification pass. Files inspected: `src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/TaskAwaiter.cs`, `src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/Task.cs`, `src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/TaskContinuation.cs`, `src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/ThreadPoolTaskScheduler.cs`, `src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/System.Runtime.CompilerServices/TaskAwaiterTests.cs`, `src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/RunContinuationsAsynchronouslyTests.cs`, `src/libraries/System.Runtime/tests/System.Threading.Tasks.Tests/Task/ExecutionContextFlowTest.cs`, `LICENSE.TXT`. GitHub Linguist label: C#.

</details>

_Generated from `catalog/c-sharp.json`; do not edit by hand._

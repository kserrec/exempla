# Initial language selection

## Source and rule

The baseline is the
[RedMonk Programming Language Rankings: January 2026](https://redmonk.com/sogrady/2026/04/14/language-rankings-1-26/),
published April 14, 2026. RedMonk correlates GitHub pull-request activity with
Stack Overflow discussion. It explicitly describes the result as a view of
code and discussion traction rather than a statistically universal usage
measure, which is the appropriate caveat for this catalog.

Exempla takes RedMonk's top 20, removes CSS because it is a stylesheet language
rather than a general programming or scripting language, and adds Lua. Lua is
the replacement because the
[2025 Stack Overflow Developer Survey](https://survey.stackoverflow.co/2025/technology)
reported substantial recent developer use and its open-source ecosystem offers
real, source-readable applications and libraries across a broad learning range.

The selection is a dated scope boundary, not a claim that these are the
objectively “best” or universally most-used languages.

## The 20 languages

| Catalog order | Language | Baseline evidence |
| ---: | --- | --- |
| 1 | JavaScript | RedMonk 1 |
| 2 | Python | RedMonk 2 |
| 3 | Java | RedMonk 3 |
| 4 | PHP | RedMonk tied 4 |
| 5 | C# | RedMonk tied 4 |
| 6 | TypeScript | RedMonk 6 |
| 7 | C++ | RedMonk tied 7 |
| 8 | Ruby | RedMonk 9 |
| 9 | C | RedMonk 10 |
| 10 | Swift | RedMonk 11 |
| 11 | Go | RedMonk 12 |
| 12 | R | RedMonk 13 |
| 13 | Shell | RedMonk tied 14 |
| 14 | Kotlin | RedMonk tied 14 |
| 15 | Scala | RedMonk tied 14 |
| 16 | PowerShell | RedMonk 17 |
| 17 | Dart | RedMonk tied 18 |
| 18 | Objective-C | RedMonk tied 18 |
| 19 | Rust | RedMonk 20 |
| 20 | Lua | Stack Overflow 2025 replacement |

## Ambiguous cases

- **HTML and CSS:** Excluded. They are essential web technologies, but their
  primary artifacts describe document structure and presentation. Repositories
  primarily classified as either generally do not offer the transferable
  programming behavior this catalog ranks. JavaScript and TypeScript cover web
  programming directly.
- **SQL:** Not present in the RedMonk top 20 and omitted from this snapshot.
  SQL is a programming language, but public repositories classified primarily
  as SQL are often schema/data collections subordinate to software written in
  another language. It can be proposed in a future scope refresh with a
  qualification strategy suited to database artifacts.
- **Shell:** Included because shell scripts implement real automation, package
  managers, installers, and operational tools with executable control flow.
- **PowerShell:** Kept separate from POSIX-family shell because it is a distinct
  object-oriented language and ecosystem with its own real-world corpus.
- **C, C++, C#, Objective-C:** Kept separate. Similar names do not make their
  language semantics, ecosystems, or learning paths interchangeable.
- **Sparse levels:** No language receives relaxed coding-relevance, quality, or
  score thresholds to force two entries into a Level. A visible gap is an
  honest catalog result.

## Refresh policy

Revisit the list annually or when a clearly newer RedMonk release is available.
A scope refresh is a reviewed catalog change: preserve the old source and date
in Git history, explain additions/removals, and do not silently recategorize
existing entries.

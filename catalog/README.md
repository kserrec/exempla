# Catalog source data

`languages.json` is the separate schema-version-1 registry for the ordered
language scope. Every other language JSON file is schema version 4 and is the
canonical source for accepted learning paths.

Each path is identified globally by `(repository, path_slug)`. A repository may
contribute at most two materially distinct paths and never two paths in the
same language/Level bucket. `prerequisites` records knowledge needed before the
path; `concepts_developed` records what studying the path teaches.

Do not edit Markdown under `../languages/` directly; regenerate it with:

```console
python3 scripts/catalog.py generate
```

Ordinary `python3 scripts/catalog.py validate` is the normal gate while honest
gaps exist. `--complete` additionally requires exactly two qualified entries
at every Level for every language and must be used only when that is literally
true. `schema.json` documents the record format; `scripts/catalog.py` enforces
it without external Python packages and generates only from schema version 4.

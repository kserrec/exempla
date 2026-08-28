# Catalog source data

`languages.json` defines the ordered language scope. Each other JSON file is
the canonical source for one language's accepted repositories. Do not edit the
Markdown under `../languages/` directly; regenerate it with:

```console
python3 scripts/catalog.py generate
```

Validate an in-progress catalog with `python3 scripts/catalog.py validate` and
the release-sized corpus with `python3 scripts/catalog.py validate --complete`.
The record format is documented by `schema.json` and enforced without external
Python packages by `scripts/catalog.py`.

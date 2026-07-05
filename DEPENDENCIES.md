<!-- this_file: DEPENDENCIES.md -->

# Dependencies

Why each runtime dependency was chosen. Development-only tools (ruff, black,
mypy, pytest, pre-commit) are omitted.

## Runtime

| Package | Why |
|---|---|
| `mkdocs>=1.6.0` | The host application. The plugin registers against MkDocs' `on_page_read_source` and `on_post_build` event hooks. Pinned to `>=1.6` for the stable plugin event API; CI additionally smoke-tests against the `1.5.x` line. |
| `beautifulsoup4>=4.12.0` | HTML extraction. The plugin parses each rendered page and pulls out one or more elements by CSS selector. See the parser note below. |
| `pyyaml>=6.0` | Reads YAML frontmatter from source Markdown and re-serialises it into the cousin file. `safe_load` / `safe_dump` only. |
| `loguru>=0.7.0` | Structured, contextual logging with zero configuration. Used for the optional `verbose` diagnostics. |

## BeautifulSoup4 parser choice

The plugin constructs `BeautifulSoup(html_content, "html.parser")` — the parser
built into the Python standard library.

- **Why `html.parser` and not `lxml`/`html5lib`:** it ships with CPython, so it
  adds no compiled-extension dependency and behaves identically across Linux,
  macOS, and Windows (which the CI matrix exercises). For the plugin's job —
  selecting an existing, well-formed element out of MkDocs-rendered output — the
  small speed advantage of `lxml` does not justify the extra wheel and the
  platform-specific build surface.
- **Trade-off:** `html.parser` is more lenient and slightly slower than `lxml`.
  MkDocs output is already valid HTML, so leniency is not a concern here.

`beautifulsoup4` adds roughly 1 MB installed. A lighter tag-only extractor such
as `selectolax` was considered, but BeautifulSoup's full CSS-selector support
(`html_element` accepts arbitrary selectors like `div[role="main"]` or
`.content`) is a user-facing feature, so the weight is accepted deliberately.

# Configuration

Configure the plugin under `plugins` in `mkdocs.yml`. All options are optional.

```yaml
plugins:
  - output-as-input:
      stage_dir: stage
      html_element: main
      target_tag: article
      include_frontmatter: true
      preserve_links: false
      minify: false
      prettify: false
      verbose: false
```

The block above lists every option with its default value.

## Options

| Option | Type | Default | Effect |
|--------|------|---------|--------|
| `stage_dir` | string | `stage` | Directory for cousin files, relative to the parent of `docs_dir` |
| `html_element` | string or list of strings | `main` | CSS selector or selectors for the content to extract |
| `target_tag` | string | `article` | Tag name for the extracted element in the output |
| `include_frontmatter` | boolean | `true` | Write the source page's YAML front matter at the top of the cousin file |
| `preserve_links` | boolean | `false` | Prefix root-relative `href` and `src` values with `.` |
| `minify` | boolean | `false` | Remove line breaks and whitespace between tags |
| `prettify` | boolean | `false` | Indent the HTML with BeautifulSoup's `prettify()` |
| `verbose` | boolean | `false` | Log extra details about each page |

MkDocs checks the type of each option when it loads the configuration and stops if a value has the wrong type.

## `stage_dir`

The plugin creates the stage directory at `<parent of docs_dir>/<stage_dir>`. With the usual layout, where `mkdocs.yml` and `docs/` sit side by side, the stage directory is a sibling of `docs/` and `site/`.

```yaml
plugins:
  - output-as-input:
      stage_dir: processed
```

The plugin creates only the last directory in the path. A nested value such as `build/markdown` works only if `build/` already exists; otherwise the build stops with `FileNotFoundError`. See [Troubleshooting](troubleshooting.md#filenotfounderror-for-the-stage-directory).

The plugin does not empty the stage directory before writing. Files from earlier builds stay there until you delete them.

## `html_element`

A CSS selector, or a list of CSS selectors, that picks the content to extract from each rendered page. Selectors are evaluated with BeautifulSoup's `select()`. If a selector matches nothing, the plugin tries it once more as a plain tag name with `find()`.

```yaml
plugins:
  - output-as-input:
      html_element: article.md-content__inner
```

```yaml
plugins:
  - output-as-input:
      html_element:
        - h1
        - div.md-content
```

What ends up in the output depends on how many elements match in total:

- **One element.** It is written as-is. If `html_element` is a single string, the element's tag is renamed to `target_tag` unless `html_element` already equals `target_tag`. The element's attributes are kept. If `html_element` is a list, the element keeps its original tag.
- **Several elements.** This happens when a list has more than one matching selector, or when one selector matches several elements. The plugin creates a new, attribute-free `target_tag` element and moves all matches into it, in selector order.
- **No elements.** The plugin logs `No matching elements found` and writes no cousin file for that page.

Because the rename rule compares the option value with `target_tag`, a single string selector such as `.content` or `div[role=main]` is also renamed. `html_element: article` with the default `target_tag: article` keeps the tag unchanged.

## `target_tag`

The tag name used for the renamed element or for the wrapper around several elements.

```yaml
plugins:
  - output-as-input:
      html_element: main
      target_tag: section
```

With this configuration, `<main class="md-main">…</main>` becomes `<section class="md-main">…</section>`.

## `include_frontmatter`

When `true`, the cousin file starts with the source page's front matter, followed by a blank line. When `false`, the cousin file contains only the HTML.

The plugin recognises front matter only when the source file starts with a line that is exactly `---` and the block ends with another line that is exactly `---`. It parses the block with `yaml.safe_load` and writes it back with `yaml.safe_dump`. As a result:

- Keys are written in alphabetical order.
- Lists and mappings are written in block style.
- Comments and the original formatting are not kept.

If the block is not valid YAML, the plugin logs `Failed to parse frontmatter` and treats the page as having no front matter. A page with no front matter, or with an empty block, gets no front matter in its cousin file.

## `preserve_links`

When `true`, the plugin looks at every `<a>`, `<img>`, `<link>` and `<script>` element inside the extracted content. Any `href` or `src` value that starts with `/` but not with `//` gets a `.` prefix, so `/guide/` becomes `./guide/`. Protocol-relative URLs (`//example.com/…`), absolute URLs and relative URLs are not changed.

MkDocs normally writes relative links, so this option only changes links that are root-relative in the rendered HTML, for example links written as `/path` in raw HTML inside your Markdown.

## `minify` and `prettify`

These options change the formatting of the HTML part of the cousin file:

- `minify: true` removes all line breaks, collapses each run of whitespace to one space and removes whitespace between a `>` and the next `<`.
- `prettify: true` passes the element through BeautifulSoup's `prettify()`, which puts each tag and text node on its own indented line.
- With both `false`, the HTML is written as BeautifulSoup serialises it, which is close to what the theme produced.

You cannot enable both. If you do, the plugin raises `ValueError: Cannot use both 'minify' and 'prettify' options` when the build starts, in the `on_config` step, and the build stops.

## `verbose`

When `true`, the plugin logs `Plugin initialized` with the site and docs directories, the resolved configuration, one `Captured source file` message per page with its front matter keys, and one `Created cousin file` message per written file.

The plugin logs through `loguru`, which writes to standard error in its own format, separate from MkDocs' own log lines.

## Configuration example for a pipeline

```yaml
plugins:
  - search
  - output-as-input:
      stage_dir: content
      html_element: article.md-content__inner
      target_tag: div
      include_frontmatter: true
      prettify: true
```

This writes one Markdown file per page into `content/`, each with the original front matter and an indented `<div>` holding the Material theme's article body.

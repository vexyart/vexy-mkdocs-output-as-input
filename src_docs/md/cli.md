# Command-line tool

The `mkdocs-output-as-input` command applies the plugin's extraction to one HTML file, without running MkDocs. Use it to test a selector against a page you already built, or to convert single files in a script.

## Synopsis

```text
mkdocs-output-as-input [-h] [--version] {process} ...

mkdocs-output-as-input process [-h] [--html-element HTML_ELEMENT]
                               [--target-tag TARGET_TAG]
                               [--no-frontmatter] [--preserve-links]
                               [--minify] [--prettify] [-v]
                               input output
```

The tool has one subcommand, `process`. Running the tool without a subcommand prints the help text and exits with status 1.

## `process` arguments

| Argument | Default | Effect |
|----------|---------|--------|
| `input` | required | Path to the HTML file to read |
| `output` | required | Path of the Markdown file to write; missing parent directories are created |
| `--html-element HTML_ELEMENT` | `main` | CSS selector for the content to extract; repeat the option to give several selectors |
| `--target-tag TARGET_TAG` | `article` | Tag name for the renamed element or for the wrapper around several elements |
| `--no-frontmatter` | off | Do not look for front matter and do not write any |
| `--preserve-links` | off | Prefix root-relative `href` and `src` values with `.` |
| `--minify` | off | Remove line breaks and double spaces from the HTML |
| `--prettify` | off | Indent the HTML with BeautifulSoup's `prettify()` |
| `-v`, `--verbose` | off | Log at debug level, with module, function and line number |

Global options:

| Option | Effect |
|--------|--------|
| `-h`, `--help` | Show help and exit |
| `--version` | Print `mkdocs-output-as-input <version>` and exit |

## Where the front matter comes from

An HTML file has no YAML front matter of its own. The `process` command looks for a Markdown file with the same path as `input` but with the `.md` extension. For `site/guide/index.html` it checks `site/guide/index.md`. If that file exists and starts with a front matter block, the block is copied into the output. If the file does not exist, the output has no front matter.

## Example

Prerequisites: an HTML page built by MkDocs with the built-in `mkdocs` theme, `page.html`, and next to it `page.md` with this content:

```markdown
---
title: My Page
---
# x
```

1. Run the command with a selector that matches the theme's content area:

    ```bash
    mkdocs-output-as-input process page.html out.md --html-element 'div[role=main]'
    ```

    The tool logs `Processing file` and `Successfully wrote output file`.

2. Read the result:

    ```markdown
    ---
    title: My Page
    ---

    <div class="col-md-9" role="main">
    <h1 id="my-page">My Page</h1>
    ...
    ```

The front matter came from `page.md`; the HTML came from `page.html`.

## Differences from the plugin

The command shares its approach with the plugin but is a separate implementation. Three details differ:

- **Renaming a single element.** The command renames the element to `--target-tag` only when the selector is a plain tag name that equals the element's own tag, for example `--html-element main` on a `<main>` element. In the example above the selector `div[role=main]` is not a tag name, so the `<div>` keeps its tag. The plugin renames in that case.
- **Minifying.** `--minify` removes line breaks and replaces double spaces with single spaces. The plugin's `minify` option also removes whitespace between tags.
- **Front matter source.** The command reads the `.md` file next to the HTML file. The plugin reads the original source page from `docs_dir`.

Several matched elements are wrapped in one `--target-tag` element, as in the plugin.

## Exit status

| Status | Meaning |
|--------|---------|
| `0` | The output file was written |
| `1` | No subcommand was given, `--minify` and `--prettify` were both given, no element matched, or reading or writing a file failed |

On failure the tool logs the reason, for example `No elements found` followed by `Command failed`.

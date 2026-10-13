# How it works

The plugin class is `OutputAsInputPlugin` in `mkdocs_output_as_input/plugin.py`. It subclasses MkDocs' `BasePlugin` and uses three MkDocs events. Front matter and rendered HTML exist at different times during a build, so the plugin collects them in separate steps and combines them at the end.

## 1. `on_config`: remember the directories

When the build starts, the plugin stores `site_dir` and `docs_dir` from the MkDocs configuration. It then checks that `minify` and `prettify` are not both enabled and raises `ValueError` if they are.

## 2. `on_page_read_source`: capture the front matter

MkDocs calls this event once per page, before it reads the page's Markdown. The plugin:

1. Opens the source file at the page's absolute source path and reads it as UTF-8.
2. If the text starts with `---` followed by a line break, looks for the next line that is exactly `---` and parses the text between them with `yaml.safe_load`.
3. Stores the parsed front matter and the source path in a dictionary keyed by the page's path relative to `docs_dir`, for example `guide/setup.md`.
4. Returns `None`, so MkDocs reads and renders the page normally.

The plugin does not change the page content. The rendered HTML does not exist yet at this point.

## 3. `on_post_build`: write the cousin files

MkDocs calls this event once, after it has written every page into `site_dir`. The plugin creates the stage directory, `<parent of docs_dir>/<stage_dir>`, and then handles each recorded page.

### Finding the HTML file

For a source path such as `guide/setup.md`, the plugin tries these files in `site_dir`, in order:

| Source path | First try | Second try |
|-------------|-----------|------------|
| `guide/setup.md` | `guide/setup/index.html` | `guide/setup.html` |
| `index.md` | `index/index.html` | `index.html` |
| `README.md` at the root of `docs_dir`, any case | `index.html` | `README.html` |

The first column of tries matches `use_directory_urls: true`, the MkDocs default; the second matches `use_directory_urls: false` and `index.md` pages. If neither file exists, the plugin logs `No HTML output found` and skips the page.

### Extracting the content

1. The HTML file is parsed with BeautifulSoup's built-in `html.parser`.
2. Each selector from `html_element` is run with `select()`. If it matches nothing, the plugin tries `find()` with the selector as a tag name.
3. All matches are collected. One match is used directly and renamed to `target_tag` when `html_element` is a single string. Several matches are moved into a new `target_tag` element.
4. If `preserve_links` is on, root-relative `href` and `src` values get a `.` prefix.

### Writing the output

The cousin file path is `<stage_dir>/<source path>`, so `guide/setup.md` becomes `stage/guide/setup.md`. Missing subdirectories inside the stage directory are created. The file contains, in this order:

1. If `include_frontmatter` is on and the page had front matter: a `---` line, the front matter written by `yaml.safe_dump`, another `---` line and a blank line.
2. The extracted HTML, minified, prettified or as serialised by BeautifulSoup.
3. A final line break.

### Errors and the summary line

An error while processing one page is logged as `Failed to process file` and counted. The plugin moves on to the next page; one bad page does not stop the build. After the last page, the plugin logs `Post-build processing complete` with the counts `processed`, `failed` and `total`, and the elapsed time.

Pages that were skipped because no HTML file or no matching element was found are counted as processed, because skipping is not an error.

## Pages the plugin sees

The plugin only knows about pages that pass through `on_page_read_source`. These are the Markdown pages MkDocs builds. Static files that MkDocs copies unchanged, such as images or HTML files in `docs_dir`, get no cousin file.

## Logging

Both the plugin and the CLI log with `loguru`. The plugin uses `loguru`'s default sink, which writes to standard error. Its messages appear alongside, but separately from, MkDocs' own `INFO` and `WARNING` lines. Messages that `loguru` logs as warnings are not MkDocs warnings, so `mkdocs build --strict` does not fail because of them.

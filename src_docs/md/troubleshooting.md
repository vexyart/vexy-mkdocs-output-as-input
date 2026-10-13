# Troubleshooting

The plugin logs through `loguru` to standard error. Turn on `verbose: true` for one message per captured page and per written file. The messages quoted below are the exact texts the plugin logs.

## `No matching elements found`

**Cause.** None of the selectors in `html_element` matched anything in the rendered page, so no cousin file was written for that page. The most common case is the default selector `main` with the built-in `mkdocs` theme, which has no `<main>` element.

**Fix.**

1. Open one page from `site/` in a browser or text editor and find the element that wraps the content.
2. Set `html_element` to a selector for it, for example `div[role=main]` for the built-in theme or `article.md-content__inner` for Material.
3. Test the selector on that page with `mkdocs-output-as-input process site/index.html /tmp/test.md --html-element "<selector>"`.
4. Run `mkdocs build` again.

These messages do not fail `mkdocs build --strict`, because `loguru` messages are not MkDocs warnings. Check the build output for them, or count the cousin files.

## `No HTML output found`

**Cause.** The plugin could not find the HTML file for a page. It looks for `<page>/index.html` and then `<page>.html` in `site_dir`. A plugin or theme that writes pages to other locations, or a page whose path contains `.md` more than once, can cause this.

**Fix.** Run with `verbose: true`, note the `expected_path` in the message, and compare it with the files in `site/`.

## `FileNotFoundError` for the stage directory

**Cause.** `stage_dir` has more than one path component, for example `build/markdown`, and the parent directory `build/` does not exist. The plugin creates only the last directory of the path.

**Fix.** Create the parent directory before the build, or use a single directory name:

```bash
mkdir -p build
mkdocs build
```

## `ValueError: Cannot use both 'minify' and 'prettify' options`

**Cause.** Both options are `true`. The plugin checks this when the build starts.

**Fix.** Set at least one of them to `false`.

## The cousin file has no front matter

Check these in order:

1. `include_frontmatter` is not set to `false`.
2. The source file starts with `---` on the very first line, with nothing before it, not even a blank line or a byte-order mark.
3. The block ends with a line that is exactly `---`.
4. The block is valid YAML. If it is not, the plugin logs `Failed to parse frontmatter`.
5. The block is not empty.

## The front matter looks different from the source

The plugin parses the block and writes it again with `yaml.safe_dump`. Keys are sorted alphabetically, comments are dropped and formatting is normalised. The values are the same.

## Old files remain in the stage directory

The plugin overwrites cousin files but never deletes files. If you delete or rename a source page, its old cousin file stays. Remove the stage directory before a clean build:

```bash
rm -rf stage
mkdocs build
```

## The extracted element has the wrong tag

With a single string in `html_element`, the plugin renames the matched element to `target_tag`, even when the selector is a class or attribute selector. Set `target_tag` to the tag you want to keep, for example `target_tag: div`. With a list in `html_element` and one match, the element keeps its own tag.

## Links point to the wrong place

The HTML in a cousin file is the HTML from `site/`, so relative links are relative to the page's location in `site/`, for example `../../` for `guide/setup/index.html`. They are not relative to the cousin file in the stage directory. `preserve_links` only changes links that start with a single `/`.

## Getting help

Search or open an issue at [github.com/vexyart/vexy-mkdocs-output-as-input/issues](https://github.com/vexyart/vexy-mkdocs-output-as-input/issues). Include your `mkdocs.yml`, the theme, and the output of a build with `verbose: true`.

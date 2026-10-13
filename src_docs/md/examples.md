# Examples

Each example shows a configuration and the result it produces. The selectors were checked against MkDocs 1.6.1 with the built-in `mkdocs` theme and with Material for MkDocs.

## Built-in `mkdocs` theme

The built-in theme puts page content in `<div class="col-md-9" role="main">` and has no `<main>` element.

```yaml
site_name: Demo
plugins:
  - output-as-input:
      html_element: "div[role=main]"
```

Result for a page with the heading `# Setup`:

```html
<article class="col-md-9" role="main">
<h1 id="setup">Setup</h1>
...
</article>
```

The `<div>` is renamed to `<article>` because `target_tag` defaults to `article`. To keep it a `<div>`, set `target_tag: div`.

## Material for MkDocs: article body only

```yaml
site_name: Demo
theme: material
plugins:
  - output-as-input:
      html_element: article.md-content__inner
      target_tag: section
      stage_dir: out
```

Result in `out/index.md` for a page with `title` and `author` in its front matter:

```markdown
---
author: Jane Doe
title: My Page
---

<section class="md-content__inner md-typeset">
<h1 id="my-page">My Page</h1>
<p>This is my content with <strong>markdown</strong>.</p>
</section>
```

With Material and the default `html_element: main`, the plugin extracts `<main class="md-main">`, which contains the navigation and table-of-contents sidebars as well as the article. Use `article.md-content__inner` when you only want the page body.

## Several selectors in one file

```yaml
plugins:
  - output-as-input:
      html_element:
        - h1
        - div.admonition
      target_tag: div
```

For each page, every `<h1>` and every element with the class `admonition` is moved into one new `<div>`, headings first, then admonitions. The wrapper has no attributes. If a page has only one match in total, that element is written on its own and keeps its original tag.

## HTML only, no front matter

```yaml
plugins:
  - output-as-input:
      html_element: article.md-content__inner
      include_frontmatter: false
      minify: true
```

Each cousin file holds a single line of HTML with no front matter block. This suits tools that read HTML fragments and ignore the file extension.

## Readable HTML for review

```yaml
plugins:
  - output-as-input:
      html_element: article.md-content__inner
      prettify: true
```

Every tag and text node is placed on its own indented line, which makes diffs between builds easier to read. Do not combine `prettify` with `minify`.

## Feeding another site generator

The plugin writes plain files and runs nothing else, so you chain the next tool after `mkdocs build`:

```bash
mkdocs build
ls stage/
```

Point the next tool at the stage directory. To write straight into another project's content folder, set `stage_dir` to a path relative to the parent of `docs_dir`, for example `../other-site/content`. The parent folder, `../other-site`, must already exist; the plugin creates only the last directory.

The cousin files keep the `.md` extension but contain HTML after the front matter. Most Markdown processors pass raw HTML through unchanged; check that your target tool does.

## Testing a selector with the CLI

Before you change `mkdocs.yml`, try a selector on one built page:

```bash
mkdocs build
mkdocs-output-as-input process site/index.html /tmp/index-test.md \
  --html-element article.md-content__inner --target-tag section
cat /tmp/index-test.md
```

If the selector matches nothing, the command logs `No elements found` and exits with status 1. The CLI and the plugin differ in how they rename a single element; see [Command-line tool](cli.md#differences-from-the-plugin).

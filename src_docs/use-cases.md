---
title: Use Cases
description: Three concrete pipelines that consume the cousin Markdown + HTML output
---

# Use Cases

`output-as-input` turns a finished MkDocs build into a directory of "cousin"
files — one per page, each holding the page's original YAML frontmatter followed
by its rendered HTML. That output is designed to be *input* for some other tool.
Here are three concrete pipelines.

Each example assumes the plugin is enabled in `mkdocs.yml`. The relevant
`plugins:` block is shown per use case; everything else in your config stays as
it is.

## 1. MkDocs → Webflow CMS import

Push an existing MkDocs knowledge base into a Webflow CMS collection, where each
CMS item wants clean body HTML plus structured fields (title, tags) from
frontmatter.

```yaml
# mkdocs.yml
plugins:
  - output-as-input:
      stage_dir: webflow-import      # cousins land in ./webflow-import/
      html_element: 'article'        # extract the semantic article body
      target_tag: 'div'              # Webflow rich-text wants a plain container
      include_frontmatter: true      # keep title/tags for CMS fields
      preserve_links: false          # Webflow rewrites internal links itself
```

Each cousin file's frontmatter maps onto CMS fields and the HTML body becomes
the rich-text field. Because the HTML is already rendered, code blocks,
admonitions, and tables arrive fully formed — no Markdown-to-HTML step in your
importer.

## 2. MkDocs → Docusaurus migration

Migrating off MkDocs onto Docusaurus, but you want to preserve the *rendered*
output of MkDocs-specific extensions (e.g. `pymdownx` superfences) rather than
re-processing raw Markdown under a different Markdown engine.

```yaml
# mkdocs.yml
plugins:
  - output-as-input:
      stage_dir: docusaurus/docs     # mirror straight into the new site tree
      html_element: 'main'           # Docusaurus MDX accepts inline HTML
      target_tag: 'article'
      include_frontmatter: true      # Docusaurus reads frontmatter too
      preserve_links: true           # keep relative links working post-move
```

The cousin `.md` files are valid MDX: frontmatter on top, HTML below. Point
Docusaurus at `docusaurus/docs` and the content renders without a lossy
Markdown round-trip through a second parser.

## 3. MkDocs → plain HTML archive

Produce a flat, dependency-free HTML snapshot of the docs for long-term
archival or full-text indexing, stripped of the theme chrome (nav, sidebar,
search) but keeping the article content and its metadata.

```yaml
# mkdocs.yml
plugins:
  - output-as-input:
      stage_dir: archive             # cousins in ./archive/
      html_element: 'div[role="main"]'  # default MkDocs theme content wrapper
      target_tag: 'article'
      include_frontmatter: true      # metadata header for each archived page
      prettify: true                 # human-readable, diff-friendly HTML
```

Each archived file is self-describing: the frontmatter records what the page
was, and the prettified `<article>` holds just the content. Feed the directory
to a search indexer or hand it to `pandoc` for further conversion.

## Notes

- `html_element` is a **CSS selector**, not only a tag name — `.content`,
  `#main`, and `div[role="main"]` all work. Pass a list to extract several
  regions into one `target_tag` container.
- `minify` and `prettify` are mutually exclusive; enabling both raises an error
  at config time.
- The stage directory is created next to your `docs_dir` (i.e. at
  `<docs_dir>/../<stage_dir>`) and mirrors the source tree.

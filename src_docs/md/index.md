# vexy-mkdocs-output-as-input

`vexy-mkdocs-output-as-input` is an MkDocs plugin. After MkDocs has built your site, the plugin reads each rendered HTML page, cuts out the part you choose, and writes it to a new Markdown file together with the YAML front matter of the original source page. These new files are called *cousin files*. They live in a separate directory, `stage/` by default, and mirror the layout of your `docs/` directory.

The package also installs a command-line tool, `mkdocs-output-as-input`, that applies the same extraction to a single HTML file outside of an MkDocs build.

## What goes in and what comes out

Take one source page, `docs/index.md`:

```markdown
---
title: My Page
author: Jane Doe
---

# My Page

This is my content with **markdown**.
```

With the Material theme and this configuration:

```yaml
plugins:
  - output-as-input:
      html_element: article.md-content__inner
      target_tag: section
```

`mkdocs build` writes the normal site into `site/`. The plugin then writes `stage/index.md`:

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

The front matter comes from the source file. The body is the HTML that MkDocs and the theme produced, after every Markdown extension and plugin ran. The extracted `<article>` element was renamed to `<section>`; its attributes were kept.

## When to use it

- You want to feed MkDocs-rendered content into another static site generator or a CMS that reads Markdown files with front matter.
- You want the page body without the theme's header, navigation and footer.
- You want a copy of each page's rendered HTML next to its metadata, for archiving or further processing.

## Where to go next

- [Installation](installation.md): requirements and install commands.
- [Quickstart](quickstart.md): enable the plugin and inspect the first cousin file.
- [Configuration](configuration.md): every plugin option and its default.
- [Command-line tool](cli.md): process one HTML file without MkDocs.
- [How it works](how-it-works.md): the two MkDocs hooks, path resolution and output format.
- [Examples](examples.md): configurations for common themes and pipelines.
- [Troubleshooting](troubleshooting.md): warnings and errors, and what they mean.
- [Contributing](contributing.md): development setup, tests and releases.

The release history is in [`CHANGELOG.md`](https://github.com/vexyart/vexy-mkdocs-output-as-input/blob/main/CHANGELOG.md). The project is licensed under the [MIT License](https://github.com/vexyart/vexy-mkdocs-output-as-input/blob/main/LICENSE).

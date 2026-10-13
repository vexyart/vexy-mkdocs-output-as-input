# Quickstart

This walk-through enables the plugin on a small MkDocs project and checks the result.

## Prerequisites

- The package is installed in the environment that runs MkDocs. See [Installation](installation.md).
- You have an MkDocs project with `mkdocs.yml` at its root and pages in `docs/`.

## Steps

1. Find out which HTML element holds the page content in your theme. The default selector is `main`, which does not suit every theme:

    | Theme | Selector for the page content |
    |-------|-------------------------------|
    | `mkdocs` (the built-in default) | `div[role=main]` |
    | `material` | `article.md-content__inner` |

    The built-in `mkdocs` theme has no `<main>` element, so with the default selector the plugin finds nothing. In Material, `main` matches `<main class="md-main">`, which also contains the navigation sidebars.

2. Add the plugin to `mkdocs.yml`. For the built-in theme:

    ```yaml
    site_name: Demo
    plugins:
      - search
      - output-as-input:
          html_element: "div[role=main]"
    ```

    Keep any plugins you already use. When you list `plugins:` yourself, MkDocs no longer adds `search` automatically, so list it if you want it.

3. Build the site:

    ```bash
    mkdocs build
    ```

    MkDocs writes `site/` as usual. The plugin then logs `Creating stage directory` and, at the end, `Post-build processing complete` with the number of processed and failed pages.

4. Look at the cousin files. They are in `stage/`, next to `docs/`:

    ```text
    my-project/
    ├── docs/
    │   ├── index.md
    │   └── guide/
    │       └── setup.md
    ├── site/
    ├── stage/
    │   ├── index.md
    │   └── guide/
    │       └── setup.md
    └── mkdocs.yml
    ```

    Each file in `stage/` has the same relative path as its source page.

## What a cousin file contains

Source `docs/guide/setup.md`:

```markdown
# Setup

See [home](../index.md).
```

Cousin file `stage/guide/setup.md`, built with the `mkdocs` theme and `html_element: "div[role=main]"`:

```html
<article class="col-md-9" role="main">
<h1 id="setup">Setup</h1>
<p>See <a href="../../">home</a>.</p></article>
```

The source has no front matter, so the cousin file has none. The `<div>` was renamed to `<article>`, the default `target_tag`. The link is the rendered link that MkDocs wrote into `site/`, relative to the page's HTML location, not to the source Markdown.

## Next steps

- Change the output directory, the element and the output tag in [Configuration](configuration.md).
- Add `stage/` to your `.gitignore` if you do not want to commit the cousin files.

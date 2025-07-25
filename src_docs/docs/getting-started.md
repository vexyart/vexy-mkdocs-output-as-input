---
title: Getting Started
description: Quick start guide for the MkDocs Output as Input plugin
---

# Getting Started

This guide will help you get up and running with the MkDocs Output as Input plugin in minutes.

## Prerequisites

- Python 3.8 or higher
- MkDocs 1.4.0 or higher
- Basic familiarity with MkDocs

## Installation

### From PyPI

The easiest way to install the plugin is from PyPI:

```bash
pip install mkdocs-output-as-input
```

### From Source

For development or to get the latest features:

```bash
git clone https://github.com/vexyart/vexy-mkdocs-output-as-input.git
cd vexy-mkdocs-output-as-input
pip install -e .
```

## Basic Configuration

Add the plugin to your `mkdocs.yml`:

```yaml
plugins:
  - output-as-input
```

This uses the default configuration:
- Output directory: `stage/`
- HTML element to extract: `<main>`
- Wrapper tag: `<article>`

## Your First Build

1. Create a simple MkDocs project:

```bash
mkdocs new my-project
cd my-project
```

2. Add some frontmatter to `docs/index.md`:

```markdown
---
title: Home
date: 2024-01-20
tags: [intro, welcome]
---

# Welcome to My Docs

This is a test page.
```

3. Configure the plugin in `mkdocs.yml`:

```yaml
site_name: My Docs
plugins:
  - output-as-input:
      verbose: true
```

4. Build your site:

```bash
mkdocs build
```

5. Check the output in `stage/index.md`:

```markdown
---
title: Home
date: 2024-01-20
tags: [intro, welcome]
---

<article>
<h1>Welcome to My Docs</h1>
<p>This is a test page.</p>
</article>
```

## What Happens During Build?

1. **Source Reading**: The plugin captures each Markdown file and its frontmatter
2. **HTML Generation**: MkDocs renders your Markdown to HTML as usual
3. **HTML Extraction**: The plugin extracts the specified HTML element from each page
4. **File Creation**: Cousin files are created in the stage directory with:
   - Original YAML frontmatter
   - Extracted HTML wrapped in your target tag

## Common Use Cases

### Post-Processing with Hugo

```yaml
# mkdocs.yml
plugins:
  - output-as-input:
      stage_dir: ../hugo-site/content
      target_tag: div
```

### Creating Print-Ready Documents

```yaml
plugins:
  - output-as-input:
      html_element: article
      stage_dir: print-ready
```

### Extracting for API Documentation

```yaml
plugins:
  - output-as-input:
      html_element: ".api-content"
      target_tag: section
```

## Next Steps

- Learn about all [Configuration Options](configuration.md)
- See more [Examples](examples.md)
- Read the [API Reference](api.md) for advanced usage
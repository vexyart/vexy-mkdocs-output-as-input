---
title: MkDocs Output as Input
description: Capture HTML output and create cousin Markdown files
---

# MkDocs Output as Input Plugin

Welcome to the documentation for the MkDocs Output as Input plugin! This plugin enables powerful post-processing workflows by capturing MkDocs HTML output and creating new Markdown files that preserve your original frontmatter.

## What does it do?

This plugin creates a bridge between MkDocs and other static site generators or processing pipelines:

```mermaid
graph LR
    A[Source Markdown<br/>with Frontmatter] --> B[MkDocs Build]
    B --> C[HTML Output]
    C --> D[Plugin Extracts<br/>Content]
    D --> E[Cousin Markdown<br/>with HTML + Frontmatter]
    E --> F[Further Processing]
```

## Quick Example

=== "Input (source.md)"

    ```markdown
    ---
    title: My Article
    date: 2025-01-14
    tags: [tutorial, mkdocs]
    ---
    
    # My Article
    
    This is my content with **Markdown** formatting.
    ```

=== "Output (stage/source.md)"

    ```markdown
    ---
    title: My Article
    date: 2025-01-14
    tags: [tutorial, mkdocs]
    ---
    
    <article class="md-content">
      <h1>My Article</h1>
      <p>This is my content with <strong>Markdown</strong> formatting.</p>
    </article>
    ```

## Key Features

- 🎯 **Preserves Frontmatter**: All your YAML metadata is maintained
- 🔍 **Selective Extraction**: Choose which HTML element to extract
- 🏷️ **Tag Transformation**: Convert extracted elements to different tags
- 📁 **Flexible Output**: Configure where cousin files are created
- 🐛 **Debug Support**: Verbose logging for troubleshooting

## Installation

```bash
pip install vexy-mkdocs-output-as-input
```

Then add to your `mkdocs.yml`:

```yaml
plugins:
  - output-as-input
```

## Next Steps

- [Getting Started](getting-started.md) - Set up your first configuration
- [Configuration](configuration.md) - Explore all options
- [Examples](examples.md) - See real-world use cases
- [API Reference](api.md) - Detailed plugin documentation
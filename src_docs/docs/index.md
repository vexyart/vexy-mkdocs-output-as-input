---
title: MkDocs Output as Input Plugin
description: A powerful MkDocs plugin that captures rendered HTML output and creates cousin Markdown files for post-processing workflows
---

# MkDocs Output as Input Plugin

Welcome to the **MkDocs Output as Input Plugin** documentation! This plugin enables advanced documentation workflows by capturing rendered HTML output from MkDocs and creating "cousin" Markdown files that combine original YAML frontmatter with extracted HTML content.

## What is Output as Input?

The Output as Input plugin bridges the gap between MkDocs and other static site generators by:

- 📄 **Capturing rendered HTML** from your MkDocs build
- 🔄 **Preserving YAML frontmatter** from source Markdown files  
- 📁 **Creating cousin files** in a staging directory for further processing
- 🛠️ **Enabling post-processing workflows** with other tools

## Key Features

- **Flexible HTML extraction** - Target specific HTML elements (main, article, div, etc.)
- **Frontmatter preservation** - Maintains all YAML metadata from source files
- **Configurable output** - Customize staging directory and wrapper tags
- **Error resilience** - Graceful handling of parsing errors and edge cases
- **Debug support** - Verbose logging for troubleshooting

## Quick Start

Install the plugin:

```bash
pip install mkdocs-output-as-input
```

Add to your `mkdocs.yml`:

```yaml
plugins:
  - output-as-input:
      stage_dir: stage
      html_element: main
      target_tag: article
```

Build your documentation:

```bash
mkdocs build
```

Find your cousin files in the `stage/` directory!

## Next Steps

- [Getting Started](getting-started.md) - Installation and basic usage
- [Configuration](configuration.md) - All plugin options explained
- [Examples](examples.md) - Real-world use cases and workflows
- [API Reference](api.md) - Technical documentation

## Support

- [GitHub Issues](https://github.com/vexyart/vexy-mkdocs-output-as-input/issues)
- [Discussions](https://github.com/vexyart/vexy-mkdocs-output-as-input/discussions)
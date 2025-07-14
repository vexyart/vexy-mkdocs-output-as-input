---
title: Getting Started
description: Quick start guide for the MkDocs Output as Input plugin
---

# Getting Started

This guide will help you get up and running with the MkDocs Output as Input plugin.

## Installation

### From PyPI

```bash
pip install vexy-mkdocs-output-as-input
```

### From Source

```bash
git clone https://github.com/vexyart/vexy-mkdocs-output-as-input
cd vexy-mkdocs-output-as-input
pip install -e .
```

## Basic Configuration

Add the plugin to your `mkdocs.yml` file:

```yaml
plugins:
  - search  # Keep your existing plugins
  - output-as-input
```

## Your First Build

1. **Create a simple Markdown file** with frontmatter:

   ```markdown
   ---
   title: My First Page
   author: Your Name
   date: 2025-01-14
   ---
   
   # My First Page
   
   This is some **markdown** content.
   ```

2. **Run MkDocs build**:

   ```bash
   mkdocs build
   ```

3. **Check the stage directory**:

   ```bash
   ls stage/
   ```

   You should see a cousin file with the same name as your source file.

## Verifying the Output

The cousin file will contain:

- **Original frontmatter** preserved exactly
- **Processed HTML content** extracted from the built site
- **Configurable HTML tag** wrapping the content

## Next Steps

- Learn about [configuration options](configuration.md)
- Explore [usage examples](examples.md)
- Check the [API reference](api.md)

## Troubleshooting

### Plugin Not Found

If you get an error about the plugin not being found:

```bash
pip install vexy-mkdocs-output-as-input
```

### No Output Files

Enable verbose mode to see what's happening:

```yaml
plugins:
  - output-as-input:
      verbose: true
```

### Permission Errors

Make sure you have write permissions in your project directory, or specify a different output directory:

```yaml
plugins:
  - output-as-input:
      stage_dir: /path/to/writable/directory
```

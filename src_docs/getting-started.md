---
title: Getting Started
description: Quick start guide for MkDocs Output as Input plugin
---

# Getting Started

This guide will help you get up and running with the MkDocs Output as Input plugin in just a few minutes.

## Prerequisites

Before installing the plugin, ensure you have:

- **Python 3.8+** installed on your system
- **MkDocs 1.4+** installed (`pip install mkdocs`)
- A working MkDocs project (or create one with `mkdocs new my-project`)

## Installation

### Using pip (Recommended)

The simplest way to install the plugin is via pip:

```bash
pip install vexy-mkdocs-output-as-input
```

### Using uv

If you're using the [uv](https://github.com/astral-sh/uv) package manager:

```bash
uv pip install vexy-mkdocs-output-as-input
```

### From Source

For development or to get the latest features:

```bash
git clone https://github.com/vexyart/vexy-mkdocs-output-as-input
cd vexy-mkdocs-output-as-input
pip install -e .
```

### Installing the CLI Tool

The installation automatically includes a CLI tool:

```bash
mkdocs-output-as-input --version
```

## Basic Configuration

### 1. Enable the Plugin

Add the plugin to your `mkdocs.yml` file:

```yaml
site_name: My Documentation
theme:
  name: material  # or any theme you prefer

plugins:
  - search  # Keep your existing plugins
  - output-as-input  # Add this line
```

### 2. Build Your Site

Run the standard MkDocs build command:

```bash
mkdocs build
```

### 3. Find Your Output

After building, you'll find your processed files in the `stage/` directory (relative to your project root):

```
my-project/
├── docs/
│   ├── index.md
│   └── guide.md
├── site/          # Standard MkDocs output
├── stage/         # Output as Input files
│   ├── index.md   # Processed version
│   └── guide.md   # Processed version
└── mkdocs.yml
```

## Your First Processed File

Let's see the plugin in action with a simple example.

### Source File (docs/example.md)

```markdown
---
title: Example Page
author: Jane Doe
date: 2024-01-20
tags: [tutorial, example]
---

# Example Page

This is a simple example with **bold text** and a [link](https://example.com).

## Features

- Item 1
- Item 2
- Item 3
```

### After MkDocs Processing

MkDocs converts this to HTML with your theme's styling:

```html
<main class="md-content">
  <h1 id="example-page">Example Page</h1>
  <p>This is a simple example with <strong>bold text</strong> and 
     <a href="https://example.com">link</a>.</p>
  <h2 id="features">Features</h2>
  <ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
  </ul>
</main>
```

### Output File (stage/example.md)

The plugin creates this cousin file:

```markdown
---
title: Example Page
author: Jane Doe
date: 2024-01-20
tags: [tutorial, example]
---

<article class="md-content">
  <h1 id="example-page">Example Page</h1>
  <p>This is a simple example with <strong>bold text</strong> and 
     <a href="https://example.com">link</a>.</p>
  <h2 id="features">Features</h2>
  <ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
  </ul>
</article>
```

Note how:
- ✅ The YAML frontmatter is preserved
- ✅ The HTML is fully rendered
- ✅ The `<main>` tag is transformed to `<article>` (configurable)

## Common Configuration Options

Here are the most commonly used configuration options:

### Change Output Directory

```yaml
plugins:
  - output-as-input:
      stage_dir: output  # Default is "stage"
```

### Extract Different Elements

```yaml
plugins:
  - output-as-input:
      html_element: article  # Default is "main"
```

### Use CSS Selectors

```yaml
plugins:
  - output-as-input:
      html_element: .content  # Extract by class
```

### Enable Verbose Logging

```yaml
plugins:
  - output-as-input:
      verbose: true  # See what's happening
```

## Verifying Installation

To verify the plugin is working correctly:

1. **Check the Logs**

   With verbose mode enabled, you should see:
   ```
   INFO    -  OutputAsInput: Creating stage directory at stage
   INFO    -  OutputAsInput: Captured source docs/index.md
   INFO    -  OutputAsInput: Created cousin file stage/index.md
   ```

2. **Examine Output Files**

   ```bash
   ls -la stage/
   cat stage/index.md
   ```

3. **Validate Structure**

   Each cousin file should have:
   - Original YAML frontmatter (if present)
   - Extracted HTML content
   - Proper file structure matching your source

## Next Steps

Now that you have the plugin working:

- 📖 Read the [Configuration Guide](configuration.md) for all available options
- 🎯 Check out [Examples](examples.md) for real-world use cases
- 🔧 Learn about [Troubleshooting](troubleshooting.md) common issues
- 🚀 Explore [advanced workflows](examples.md#advanced-workflows) for complex pipelines

## Getting Help

If you run into issues:

1. Check the [Troubleshooting Guide](troubleshooting.md)
2. Search [existing issues](https://github.com/vexyart/vexy-mkdocs-output-as-input/issues)
3. Ask in [Discussions](https://github.com/vexyart/vexy-mkdocs-output-as-input/discussions)
4. Report a [new issue](https://github.com/vexyart/vexy-mkdocs-output-as-input/issues/new) if needed

Happy documenting! 🎉
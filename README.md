# vexy-mkdocs-output-as-input

[![PyPI version](https://badge.fury.io/py/vexy-mkdocs-output-as-input.svg)](https://pypi.org/project/vexy-mkdocs-output-as-input/)
[![CI](https://github.com/vexyart/vexy-mkdocs-output-as-input/workflows/CI/badge.svg)](https://github.com/vexyart/vexy-mkdocs-output-as-input/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/vexyart/vexy-mkdocs-output-as-input/branch/main/graph/badge.svg)](https://codecov.io/gh/vexyart/vexy-mkdocs-output-as-input)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python versions](https://img.shields.io/pypi/pyversions/vexy-mkdocs-output-as-input.svg)](https://pypi.org/project/vexy-mkdocs-output-as-input/)

A MkDocs plugin that captures HTML output and creates "cousin" Markdown files with original frontmatter and extracted HTML content.

## Features

This plugin enables powerful post-processing workflows by:

1. ✅ Preserving your original Markdown structure and frontmatter
2. ✅ Capturing the fully-rendered HTML output from MkDocs
3. ✅ Creating new Markdown files that combine original metadata with processed HTML
4. ✅ Enabling further processing by other static site generators

## Installation

Install from PyPI:

```bash
pip install vexy-mkdocs-output-as-input
```

Or install from source:

```bash
git clone https://github.com/vexyart/vexy-mkdocs-output-as-input
cd vexy-mkdocs-output-as-input
pip install -e .
```

## Quick Start

Add the plugin to your `mkdocs.yml`:

```yaml
plugins:
  - search  # Other plugins
  - output-as-input
```

Build your site:

```bash
mkdocs build
```

Find your processed files in the `stage/` directory (relative to your MkDocs project root).

## Configuration

All configuration options with their defaults:

```yaml
plugins:
  - output-as-input:
      stage_dir: stage          # Output directory name (default: 'stage')
      html_element: main        # HTML element to extract (default: 'main')
      target_tag: article       # Tag to use in output (default: 'article')
      verbose: false            # Enable verbose logging (default: false)
```

### Options Explained

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `stage_dir` | string | `"stage"` | Directory name for output files (relative to project root) |
| `html_element` | string | `"main"` | CSS selector for the HTML element to extract |
| `target_tag` | string | `"article"` | HTML tag to use in the output (replaces extracted element's tag) |
| `verbose` | boolean | `false` | Enable detailed logging for debugging |

## How It Works

### Input → Process → Output

1. **Input**: Your source Markdown with frontmatter
   ```markdown
   ---
   title: My Page
   author: Jane Doe
   ---
   
   # My Page
   
   This is my content with **markdown**.
   ```

2. **MkDocs Processing**: Renders to HTML as usual
   ```html
   <main class="md-content">
     <h1>My Page</h1>
     <p>This is my content with <strong>markdown</strong>.</p>
   </main>
   ```

3. **Output**: Cousin file with preserved frontmatter + extracted HTML
   ```markdown
   ---
   title: My Page
   author: Jane Doe
   ---
   
   <article class="md-content">
     <h1>My Page</h1>
     <p>This is my content with <strong>markdown</strong>.</p>
   </article>
   ```

## Use Cases

### 🔄 Multi-Stage Documentation Pipeline

Process documentation through MkDocs first, then feed to another SSG:

```yaml
# mkdocs.yml
plugins:
  - output-as-input:
      stage_dir: hugo/content

# Then run:
# mkdocs build && hugo build
```

### 📝 Content Extraction

Extract just the article content without theme wrapper:

```yaml
plugins:
  - output-as-input:
      html_element: article
      target_tag: div
```

### 🎨 Custom Post-Processing

Preserve MkDocs rendering while preparing for custom templates:

```yaml
plugins:
  - output-as-input:
      stage_dir: _includes
      html_element: main
      target_tag: section
```

## Examples

### Basic Example

```yaml
# mkdocs.yml
site_name: My Documentation
plugins:
  - output-as-input
```

### Advanced Example

```yaml
# mkdocs.yml
site_name: My Documentation
theme:
  name: material

plugins:
  - search
  - output-as-input:
      stage_dir: processed
      html_element: article.md-content__inner
      target_tag: main
      verbose: true

# Process specific content area from Material theme
```

### Integration Example

Using with other tools in a documentation pipeline:

```bash
#!/bin/bash
# build.sh

# Stage 1: Build with MkDocs + plugins
mkdocs build

# Stage 2: Process staged output
python post_process.py stage/

# Stage 3: Build final site
hugo --contentDir=stage/
```

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/vexyart/vexy-mkdocs-output-as-input
cd vexy-mkdocs-output-as-input

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .[dev]

# Install pre-commit hooks
pre-commit install
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=mkdocs_output_as_input --cov-report=html

# Run specific test
pytest tests/test_plugin.py::TestOutputAsInputPlugin::test_default_config
```

### Code Quality

```bash
# Format code
black src tests

# Lint code
ruff check src tests

# Type check
mypy src
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- 📧 Email: you@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/vexyart/vexy-mkdocs-output-as-input/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/vexyart/vexy-mkdocs-output-as-input/discussions)
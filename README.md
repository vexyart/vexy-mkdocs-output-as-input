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
uv pip install --system --upgrade vexy-mkdocs-output-as-input
```

Or install from source:

```bash
pip install git+https://github.com/vexyart/vexy-mkdocs-output-as-input
```

This also installs a CLI tool: `mkdocs-output-as-input`

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
      include_frontmatter: true # Include YAML frontmatter (default: true)
      preserve_links: false     # Convert absolute to relative links (default: false)
      verbose: false            # Enable verbose logging (default: false)
```

### Advanced Examples

Extract multiple elements:
```yaml
plugins:
  - output-as-input:
      html_element: [main, aside]  # Extract both main content and sidebar
```

Extract using CSS selectors:
```yaml
plugins:
  - output-as-input:
      html_element: .content  # Extract element with class="content"
```

### Options Explained

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `stage_dir` | string | `"stage"` | Directory name for output files (relative to project root) |
| `html_element` | string or list | `"main"` | CSS selector(s) for HTML elements to extract |
| `target_tag` | string | `"article"` | HTML tag to use in the output (replaces extracted element's tag) |
| `include_frontmatter` | boolean | `true` | Include YAML frontmatter in output files |
| `preserve_links` | boolean | `false` | Convert absolute links to relative (e.g., `/path` → `./path`) |
| `minify` | boolean | `false` | Minify HTML output (remove whitespace) |
| `prettify` | boolean | `false` | Prettify HTML output (add indentation) |
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

# Automated setup (recommended)
./scripts/dev-setup.sh

# Or manual setup
make dev-setup
```

### Common Development Tasks

```bash
# Run all tests and code quality checks
make test

# Build the package
make build

# Create a new patch release
make release

# Clean build artifacts
make clean

# View all available commands
make help
```

### Running Tests

```bash
# Run all tests with script
./scripts/test.sh

# Or run individual components
pytest --cov=mkdocs_output_as_input --cov-report=html
ruff check src tests
mypy src
```

### Build and Release

The project uses automated build and release workflows:

1. **Local Release Script:**
   ```bash
   ./scripts/release.sh patch  # Creates v1.0.1 -> v1.0.2
   ./scripts/release.sh minor  # Creates v1.0.2 -> v1.1.0
   ./scripts/release.sh major  # Creates v1.1.0 -> v2.0.0
   ```

2. **GitHub Actions:** Automatically triggered on git tags
   - Runs tests on multiple platforms (Linux, Windows, macOS)
   - Builds Python packages and standalone binaries
   - Publishes to PyPI using trusted publishing
   - Creates GitHub releases with artifacts

3. **Standalone Binaries:** Available for download from releases
   - Linux: `mkdocs-output-as-input-ubuntu-latest`
   - Windows: `mkdocs-output-as-input-windows-latest.exe`
   - macOS: `mkdocs-output-as-input-macos-latest`

See [BUILD_RELEASE.md](BUILD_RELEASE.md) for detailed documentation.

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
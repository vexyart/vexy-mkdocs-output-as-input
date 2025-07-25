---
title: Frequently Asked Questions
description: Common questions about MkDocs Output as Input plugin
---

# Frequently Asked Questions

## General Questions

### What is MkDocs Output as Input?

MkDocs Output as Input is a plugin that captures the HTML output from MkDocs and creates "cousin" Markdown files that combine your original YAML frontmatter with the processed HTML content. This enables post-processing workflows and integration with other static site generators.

### Why would I need this plugin?

Common use cases include:

- **Multi-stage pipelines**: Process with MkDocs first, then feed to another SSG like Hugo or Jekyll
- **Content extraction**: Extract just the article content without theme wrapper
- **Custom post-processing**: Apply your own templates to MkDocs-processed content
- **Documentation reuse**: Share processed content across multiple sites

### How is this different from just using MkDocs?

Standard MkDocs generates a complete HTML website. This plugin creates hybrid Markdown files that preserve your metadata while containing the processed HTML content, making it perfect for further processing.

## Installation & Setup

### What are the system requirements?

- Python 3.8 or higher
- MkDocs 1.4 or higher
- BeautifulSoup4 (installed automatically)
- PyYAML (installed automatically)

### Does it work with all MkDocs themes?

Yes! The plugin is theme-agnostic. You can configure it to extract the appropriate HTML elements for any theme:

- **Material**: Use `.md-content__inner`
- **ReadTheDocs**: Use `.rst-content`
- **Default**: Use `main`
- **Custom**: Use any CSS selector

### Can I use it with other MkDocs plugins?

Absolutely! The plugin works alongside other MkDocs plugins. It runs after the build process, so it captures the final rendered output including changes from other plugins.

## Configuration

### What's the difference between `html_element` and `target_tag`?

- **`html_element`**: What to extract FROM the rendered HTML (e.g., `main`, `.content`)
- **`target_tag`**: What tag to use IN the output file (e.g., `article`, `section`)

Example:
```yaml
# Extract <main class="content">...</main>
# Output as <article class="content">...</article>
plugins:
  - output-as-input:
      html_element: main
      target_tag: article
```

### Can I extract multiple elements?

Yes! Provide a list of selectors:

```yaml
plugins:
  - output-as-input:
      html_element:
        - main
        - aside.sidebar
        - nav.toc
```

### What happens to internal links?

By default, links are preserved as-is. Enable `preserve_links: true` to convert root-relative links to relative:

- `/docs/page.html` → `./docs/page.html`
- `https://example.com` → `https://example.com` (unchanged)

## Usage & Workflow

### Where do the output files go?

By default, files are created in a `stage/` directory at your project root. You can change this with the `stage_dir` option.

### How does file naming work?

The plugin maintains your original file structure:

- `docs/index.md` → `stage/index.md`
- `docs/guides/intro.md` → `stage/guides/intro.md`

### Can I exclude certain files?

Currently, the plugin processes all Markdown files. For selective processing, you can:

1. Use a separate MkDocs config for the plugin
2. Post-process to remove unwanted files
3. Use symbolic links to control what gets built

### How do I debug issues?

Enable verbose logging:

```yaml
plugins:
  - output-as-input:
      verbose: true
```

This will show:
- Which files are being processed
- What HTML elements are found
- Where cousin files are created

## Performance

### How does it handle large sites?

The plugin is optimized for performance:
- Processes files sequentially (parallel processing planned)
- Minimal memory footprint
- Efficient HTML parsing with BeautifulSoup

### Does it slow down the build?

The impact is minimal - typically adds 10-20% to build time depending on site size and configuration options.

### Can I speed up builds?

Tips for faster builds:
- Use `minify: true` instead of `prettify: true`
- Extract only necessary elements
- Disable `verbose` logging in production

## Troubleshooting

### Why are my cousin files empty?

Common causes:
1. The `html_element` selector doesn't match anything
2. The HTML file wasn't generated (check for build errors)
3. File permissions issue

### Why is my frontmatter missing?

Check that:
- Your source files have valid YAML frontmatter
- `include_frontmatter: true` (default)
- The frontmatter has proper `---` delimiters

### Why are some files not processed?

The plugin only processes Markdown files that MkDocs successfully builds. Check:
- MkDocs build logs for errors
- That files are included in `nav` or not excluded
- File extensions are `.md`

## Advanced Usage

### Can I customize the output format?

Currently, the plugin outputs Markdown files with HTML content. For custom formats:

1. Use the plugin as-is, then post-process
2. Extend the plugin class (see API docs)
3. Use template processing on the output

### Can I use it programmatically?

Yes! See the [API Reference](api/index.md) for examples of using the plugin in Python scripts.

### Does it support i18n/multiple languages?

Yes, it works with mkdocs-static-i18n and similar plugins. The directory structure is preserved, so language subdirectories are maintained.

## Integration Questions

### How do I use it with Hugo?

```yaml
# mkdocs.yml
plugins:
  - output-as-input:
      stage_dir: hugo/content

# Then run:
# mkdocs build && cd hugo && hugo
```

### How do I use it with Jekyll?

```yaml
plugins:
  - output-as-input:
      stage_dir: _includes/mkdocs
      minify: true

# In Jekyll layouts:
# {% include mkdocs/{{ page.name }} %}
```

### Can I use it with GitHub Pages?

Yes! Add to your GitHub Actions workflow:

```yaml
- name: Build with MkDocs
  run: |
    pip install mkdocs-material vexy-mkdocs-output-as-input
    mkdocs build

- name: Process with second SSG
  run: |
    # Your next build step using stage/ files
```

## Feature Requests

### Will you add feature X?

We welcome feature requests! Please:

1. Check [existing issues](https://github.com/vexyart/vexy-mkdocs-output-as-input/issues)
2. Open a [new discussion](https://github.com/vexyart/vexy-mkdocs-output-as-input/discussions)
3. Provide use case details

### Can I contribute?

Absolutely! See our [Development Guide](development.md) for details on:
- Setting up the development environment
- Running tests
- Submitting pull requests

### Is there a roadmap?

Key planned features:
- Async/parallel processing
- Custom output formats
- Template support
- Plugin API for extensions

## Comparison

### How does this compare to mkdocs-print-site-plugin?

- **mkdocs-print-site**: Creates a single combined page
- **output-as-input**: Preserves individual files with metadata

### How does this compare to mkdocs-pdf-export-plugin?

- **mkdocs-pdf-export**: Generates PDF files
- **output-as-input**: Generates Markdown+HTML for further processing

### Why not just parse MkDocs HTML output directly?

The plugin:
- Preserves your original frontmatter
- Maintains file structure
- Handles extraction consistently
- Integrates into the build pipeline

## Still Have Questions?

If your question isn't answered here:

1. Check the [Troubleshooting Guide](troubleshooting.md)
2. Search [GitHub Issues](https://github.com/vexyart/vexy-mkdocs-output-as-input/issues)
3. Ask in [GitHub Discussions](https://github.com/vexyart/vexy-mkdocs-output-as-input/discussions)
4. Open a [new issue](https://github.com/vexyart/vexy-mkdocs-output-as-input/issues/new)
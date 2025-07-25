---
title: Examples
description: Real-world examples and use cases for MkDocs Output as Input plugin
---

# Examples

This page demonstrates various real-world use cases and configurations for the MkDocs Output as Input plugin.

## Basic Examples

### Simple Documentation Site

The most straightforward use case - capturing rendered documentation:

=== "mkdocs.yml"

    ```yaml
    site_name: My Documentation
    theme:
      name: material
    
    plugins:
      - search
      - output-as-input
    ```

=== "Source (docs/guide.md)"

    ```markdown
    ---
    title: User Guide
    category: documentation
    ---
    
    # User Guide
    
    Welcome to our **user guide**!
    
    ## Getting Started
    
    1. Install the software
    2. Configure settings
    3. Start using
    ```

=== "Output (stage/guide.md)"

    ```markdown
    ---
    title: User Guide
    category: documentation
    ---
    
    <article class="md-content">
      <h1 id="user-guide">User Guide</h1>
      <p>Welcome to our <strong>user guide</strong>!</p>
      <h2 id="getting-started">Getting Started</h2>
      <ol>
        <li>Install the software</li>
        <li>Configure settings</li>
        <li>Start using</li>
      </ol>
    </article>
    ```

### Extracting Multiple Content Areas

Capture both main content and table of contents:

=== "Configuration"

    ```yaml
    plugins:
      - output-as-input:
          html_element:
            - article
            - nav.toc
          target_tag: div
    ```

=== "Result Structure"

    ```html
    <div>
      <article>
        <!-- Main content -->
      </article>
      <nav class="toc">
        <!-- Table of contents -->
      </nav>
    </div>
    ```

## Integration Examples

### Hugo Pipeline

Using MkDocs for initial processing, then Hugo for final site:

=== "Project Structure"

    ```
    my-docs/
    ├── mkdocs.yml
    ├── docs/           # MkDocs source
    ├── hugo/
    │   ├── config.toml
    │   ├── content/    # Output as Input target
    │   └── themes/
    └── build.sh
    ```

=== "mkdocs.yml"

    ```yaml
    site_name: Technical Documentation
    
    plugins:
      - output-as-input:
          stage_dir: hugo/content
          html_element: .md-content__inner
          include_frontmatter: true
    ```

=== "build.sh"

    ```bash
    #!/bin/bash
    # Build with MkDocs first
    mkdocs build
    
    # Then build with Hugo
    cd hugo
    hugo --minify
    ```

### Jekyll Integration

Feed processed content to Jekyll:

=== "Configuration"

    ```yaml
    plugins:
      - output-as-input:
          stage_dir: _includes/processed
          html_element: main
          target_tag: section
          minify: true
    ```

=== "Jekyll Layout"

    ```liquid
    ---
    layout: default
    ---
    
    <div class="post-content">
      {% include processed/{{ page.path }} %}
    </div>
    ```

### Eleventy (11ty) Pipeline

Process with MkDocs, enhance with Eleventy:

=== "Directory Structure"

    ```
    project/
    ├── mkdocs.yml
    ├── docs/
    ├── .eleventy.js
    └── src/
        └── processed/  # Stage directory
    ```

=== "MkDocs Configuration"

    ```yaml
    plugins:
      - output-as-input:
          stage_dir: src/processed
          prettify: true
    ```

=== "Eleventy Configuration"

    ```javascript
    module.exports = function(eleventyConfig) {
      eleventyConfig.addPassthroughCopy("src/processed");
      
      return {
        dir: {
          input: "src",
          output: "_site"
        }
      };
    };
    ```

## Advanced Workflows

### Multi-Language Documentation

Process documentation in multiple languages:

=== "Project Structure"

    ```
    docs/
    ├── en/
    │   ├── index.md
    │   └── guide.md
    ├── es/
    │   ├── index.md
    │   └── guide.md
    └── fr/
        ├── index.md
        └── guide.md
    ```

=== "Configuration"

    ```yaml
    plugins:
      - output-as-input:
          stage_dir: processed
          html_element: main
          verbose: true
    
    # Use with mkdocs-static-i18n
    plugins:
      - i18n:
          default_language: en
          languages:
            en: English
            es: Español
            fr: Français
      - output-as-input:
          stage_dir: processed
    ```

=== "Output Structure"

    ```
    processed/
    ├── en/
    │   ├── index.md
    │   └── guide.md
    ├── es/
    │   ├── index.md
    │   └── guide.md
    └── fr/
        ├── index.md
        └── guide.md
    ```

### API Documentation Processing

Extract API documentation for custom rendering:

=== "Source File"

    ```markdown
    ---
    title: API Reference
    api_version: 2.0
    ---
    
    # API Reference
    
    ::: mkdocs_output_as_input.plugin.OutputAsInputPlugin
        options:
          show_source: true
          show_bases: false
    ```

=== "Configuration"

    ```yaml
    plugins:
      - mkdocstrings:
          handlers:
            python:
              options:
                show_source: true
      - output-as-input:
          html_element: .doc-class
          target_tag: div
          stage_dir: api_docs
    ```

### Content Aggregation

Combine content from multiple sources:

=== "Aggregation Script"

    ```python
    #!/usr/bin/env python3
    import os
    from pathlib import Path
    import yaml
    
    # Read all cousin files
    stage_dir = Path("stage")
    aggregated = []
    
    for md_file in stage_dir.rglob("*.md"):
        with open(md_file) as f:
            content = f.read()
            
        # Parse frontmatter
        if content.startswith("---\n"):
            _, fm, body = content.split("---\n", 2)
            metadata = yaml.safe_load(fm)
            
            aggregated.append({
                "path": str(md_file),
                "metadata": metadata,
                "content": body
            })
    
    # Create aggregated index
    with open("aggregated_index.json", "w") as f:
        json.dump(aggregated, f, indent=2)
    ```

=== "Usage"

    ```bash
    # Build with MkDocs
    mkdocs build
    
    # Aggregate content
    python aggregate_content.py
    
    # Use aggregated content in your workflow
    ```

## Theme-Specific Examples

### Material for MkDocs

Optimal configuration for Material theme:

```yaml
theme:
  name: material
  features:
    - navigation.sections
    - navigation.expand
    - toc.integrate

plugins:
  - output-as-input:
      html_element: .md-content__inner
      target_tag: article
      preserve_links: true
```

### ReadTheDocs Theme

Configuration for ReadTheDocs theme:

```yaml
theme:
  name: readthedocs

plugins:
  - output-as-input:
      html_element: .rst-content
      target_tag: div
```

### Custom Theme

Working with custom themes:

```yaml
theme:
  name: null
  custom_dir: my_theme/

plugins:
  - output-as-input:
      # Use a specific selector for your theme
      html_element: "#content-wrapper > .main-content"
      target_tag: main
```

## Use Case Scenarios

### Documentation Versioning

Maintain versioned documentation:

=== "Version Script"

    ```bash
    #!/bin/bash
    VERSION=$1
    
    # Build current version
    mkdocs build
    
    # Archive processed files
    mkdir -p "versions/$VERSION"
    cp -r stage/* "versions/$VERSION/"
    
    # Update version index
    echo "- $VERSION" >> versions/index.txt
    ```

=== "Usage"

    ```bash
    ./version_docs.sh v1.2.0
    ```

### SEO Enhancement Pipeline

Process for SEO optimization:

=== "Configuration"

    ```yaml
    plugins:
      - output-as-input:
          stage_dir: seo_stage
          minify: true
          preserve_links: false
    ```

=== "Post-Processing"

    ```python
    from bs4 import BeautifulSoup
    import frontmatter
    
    def enhance_seo(filepath):
        post = frontmatter.load(filepath)
        soup = BeautifulSoup(post.content, 'html.parser')
        
        # Add meta descriptions
        if 'description' in post:
            meta = soup.new_tag('meta', 
                name='description', 
                content=post['description'])
            soup.insert(0, meta)
        
        # Update content
        post.content = str(soup)
        
        # Save enhanced version
        with open(filepath, 'w') as f:
            f.write(frontmatter.dumps(post))
    ```

### Static Site Search Index

Build search index from processed content:

```python
import json
from pathlib import Path
from bs4 import BeautifulSoup
import frontmatter

def build_search_index():
    index = []
    
    for file in Path("stage").rglob("*.md"):
        post = frontmatter.load(file)
        soup = BeautifulSoup(post.content, 'html.parser')
        
        # Extract text content
        text = soup.get_text(separator=' ', strip=True)
        
        index.append({
            "title": post.get("title", ""),
            "path": str(file.relative_to("stage")),
            "content": text[:200] + "...",  # Preview
            "tags": post.get("tags", [])
        })
    
    with open("search_index.json", "w") as f:
        json.dump(index, f)
```

## Debugging Examples

### Verbose Logging

Enable detailed logging for troubleshooting:

```yaml
plugins:
  - output-as-input:
      verbose: true
      stage_dir: debug_output
      html_element: main
```

### Test Configuration

Minimal test setup:

```yaml
# mkdocs-test.yml
site_name: Test Site
docs_dir: test_docs
site_dir: test_site

nav:
  - Home: index.md

plugins:
  - output-as-input:
      stage_dir: test_stage
      verbose: true
```

Run with:
```bash
mkdocs build -f mkdocs-test.yml
```

## Complete Project Example

Here's a complete example of a documentation pipeline:

=== "Project Structure"

    ```
    my-project/
    ├── mkdocs.yml
    ├── docs/
    │   ├── index.md
    │   ├── getting-started.md
    │   ├── api/
    │   │   ├── overview.md
    │   │   └── reference.md
    │   └── guides/
    │       ├── installation.md
    │       └── configuration.md
    ├── stage/              # Output as Input
    ├── final/              # Final output
    ├── scripts/
    │   ├── build.sh
    │   └── post_process.py
    └── templates/
        └── page.html
    ```

=== "mkdocs.yml"

    ```yaml
    site_name: My Project Documentation
    site_url: https://docs.example.com
    
    theme:
      name: material
      palette:
        primary: indigo
      features:
        - navigation.sections
        - navigation.expand
    
    plugins:
      - search
      - output-as-input:
          stage_dir: stage
          html_element: .md-content__inner
          preserve_links: true
          verbose: true
    
    markdown_extensions:
      - admonition
      - codehilite
      - toc:
          permalink: true
    ```

=== "build.sh"

    ```bash
    #!/bin/bash
    set -e
    
    echo "Building with MkDocs..."
    mkdocs build
    
    echo "Post-processing content..."
    python scripts/post_process.py
    
    echo "Building final site..."
    # Your final build step here
    
    echo "Done!"
    ```

## Next Steps

- Review the [Configuration Reference](configuration.md) for all available options
- Check the [API Documentation](api/index.md) for programmatic usage
- Read the [Troubleshooting Guide](troubleshooting.md) for common issues
- Explore the [Development Guide](development.md) to contribute
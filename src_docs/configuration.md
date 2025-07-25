---
title: Configuration Reference
description: Complete configuration guide for MkDocs Output as Input plugin
---

# Configuration Reference

This page provides a comprehensive reference for all configuration options available in the MkDocs Output as Input plugin.

## Overview

The plugin is configured in your `mkdocs.yml` file under the `plugins` section:

```yaml
plugins:
  - output-as-input:
      option_name: value
```

## Configuration Options

### `stage_dir`

**Type:** `string`  
**Default:** `"stage"`  
**Description:** Directory name for output files (relative to project root)

The `stage_dir` option specifies where the cousin files will be created. This directory is created automatically if it doesn't exist.

=== "Example: Default"

    ```yaml
    plugins:
      - output-as-input  # Uses "stage" directory
    ```

=== "Example: Custom Directory"

    ```yaml
    plugins:
      - output-as-input:
          stage_dir: processed_docs
    ```

=== "Example: Nested Directory"

    ```yaml
    plugins:
      - output-as-input:
          stage_dir: build/markdown
    ```

!!! tip "Best Practice"
    Choose a directory name that clearly indicates its purpose in your workflow. Common choices include `stage`, `processed`, `output`, or `cousin`.

---

### `html_element`

**Type:** `string` or `list[string]`  
**Default:** `"main"`  
**Description:** HTML element(s) to extract from the rendered page

This option determines which part of the rendered HTML to extract. You can specify:

- HTML tag names (e.g., `"main"`, `"article"`)
- CSS classes (e.g., `".content"`, `".md-content"`)
- CSS IDs (e.g., `"#main-content"`)
- Complex CSS selectors (e.g., `"article.post > div.content"`)
- Multiple selectors as a list

=== "Example: Tag Name"

    ```yaml
    plugins:
      - output-as-input:
          html_element: article
    ```

=== "Example: CSS Class"

    ```yaml
    plugins:
      - output-as-input:
          html_element: .md-content__inner
    ```

=== "Example: Multiple Elements"

    ```yaml
    plugins:
      - output-as-input:
          html_element: 
            - main
            - aside.sidebar
    ```

=== "Example: Complex Selector"

    ```yaml
    plugins:
      - output-as-input:
          html_element: "div.content > article:first-child"
    ```

!!! info "Theme Compatibility"
    Different MkDocs themes use different HTML structures:
    
    - **Material**: `.md-content__inner` or `article`
    - **ReadTheDocs**: `div.rst-content`
    - **MkDocs default**: `main` or `div.col-md-9`

---

### `target_tag`

**Type:** `string`  
**Default:** `"article"`  
**Description:** HTML tag to use in the output file

This option specifies what HTML tag should wrap the extracted content in the cousin file. The extracted element's tag is replaced with this value.

=== "Example: Default"

    ```yaml
    # Input: <main class="content">...</main>
    # Output: <article class="content">...</article>
    plugins:
      - output-as-input
    ```

=== "Example: Section Tag"

    ```yaml
    # Input: <main class="content">...</main>
    # Output: <section class="content">...</section>
    plugins:
      - output-as-input:
          target_tag: section
    ```

=== "Example: Div Tag"

    ```yaml
    # Input: <article>...</article>
    # Output: <div>...</div>
    plugins:
      - output-as-input:
          target_tag: div
    ```

---

### `include_frontmatter`

**Type:** `boolean`  
**Default:** `true`  
**Description:** Whether to include YAML frontmatter in output files

Controls whether the original YAML frontmatter from source files is preserved in the cousin files.

=== "Example: Include (Default)"

    ```yaml
    plugins:
      - output-as-input  # Frontmatter included
    ```

=== "Example: Exclude"

    ```yaml
    plugins:
      - output-as-input:
          include_frontmatter: false
    ```

!!! tip "Use Cases"
    - Set to `true` when feeding to other SSGs that use frontmatter
    - Set to `false` when you only need the HTML content

---

### `preserve_links`

**Type:** `boolean`  
**Default:** `false`  
**Description:** Convert absolute links to relative links

When enabled, this option converts root-relative links (starting with `/`) to relative links (starting with `./`).

=== "Example: Disabled (Default)"

    ```yaml
    # Input: <a href="/docs/guide.html">Guide</a>
    # Output: <a href="/docs/guide.html">Guide</a>
    plugins:
      - output-as-input
    ```

=== "Example: Enabled"

    ```yaml
    # Input: <a href="/docs/guide.html">Guide</a>
    # Output: <a href="./docs/guide.html">Guide</a>
    plugins:
      - output-as-input:
          preserve_links: true
    ```

!!! warning "Link Handling"
    This option only affects root-relative links. External links and protocol-relative links are never modified.

---

### `minify`

**Type:** `boolean`  
**Default:** `false`  
**Description:** Minify HTML output by removing unnecessary whitespace

When enabled, removes extra whitespace, newlines, and spaces between HTML tags to create compact output.

=== "Example: Normal Output"

    ```html
    <article>
      <h1>Title</h1>
      <p>
        Content here
      </p>
    </article>
    ```

=== "Example: Minified Output"

    ```html
    <article><h1>Title</h1><p>Content here</p></article>
    ```

Configuration:

```yaml
plugins:
  - output-as-input:
      minify: true
```

!!! note "Mutually Exclusive"
    `minify` and `prettify` options cannot be used together.

---

### `prettify`

**Type:** `boolean`  
**Default:** `false`  
**Description:** Format HTML output with proper indentation

When enabled, formats the HTML with proper indentation and line breaks for better readability.

=== "Example: Normal Output"

    ```html
    <article><h1>Title</h1><p>Content</p></article>
    ```

=== "Example: Prettified Output"

    ```html
    <article>
     <h1>
      Title
     </h1>
     <p>
      Content
     </p>
    </article>
    ```

Configuration:

```yaml
plugins:
  - output-as-input:
      prettify: true
```

!!! note "Mutually Exclusive"
    `prettify` and `minify` options cannot be used together.

---

### `verbose`

**Type:** `boolean`  
**Default:** `false`  
**Description:** Enable detailed logging for debugging

When enabled, the plugin logs detailed information about its operations, which is helpful for debugging.

```yaml
plugins:
  - output-as-input:
      verbose: true
```

Verbose output includes:
- Source file captures
- HTML path resolution
- Element extraction details
- Cousin file creation
- Processing statistics

Example verbose output:
```
INFO    -  OutputAsInput: site_dir=/path/to/site, docs_dir=/path/to/docs
INFO    -  OutputAsInput: Captured source docs/index.md
INFO    -  OutputAsInput: Created cousin file stage/index.md
INFO    -  OutputAsInput: Processed 15/15 files
```

## Complete Configuration Examples

### Minimal Configuration

```yaml
plugins:
  - output-as-input
```

### Material Theme Configuration

```yaml
plugins:
  - output-as-input:
      stage_dir: processed
      html_element: .md-content__inner
      target_tag: main
      verbose: true
```

### Multi-Stage Pipeline Configuration

```yaml
plugins:
  - output-as-input:
      stage_dir: hugo/content
      html_element: 
        - article
        - aside.toc
      include_frontmatter: true
      preserve_links: true
      prettify: true
```

### Performance-Optimized Configuration

```yaml
plugins:
  - output-as-input:
      stage_dir: output
      html_element: main
      minify: true
      verbose: false
```

## Configuration Validation

The plugin validates configuration options at startup. Common validation errors:

### Mutually Exclusive Options

```yaml
# This will raise an error
plugins:
  - output-as-input:
      minify: true
      prettify: true  # Error: Cannot use both
```

### Invalid Types

```yaml
# This will raise an error
plugins:
  - output-as-input:
      verbose: "yes"  # Error: Must be boolean
```

## Environment-Specific Configuration

You can use MkDocs inheritance to have different configurations for different environments:

=== "mkdocs.yml"

    ```yaml
    INHERIT: mkdocs-base.yml
    
    plugins:
      - output-as-input:
          stage_dir: stage
          verbose: false
    ```

=== "mkdocs-dev.yml"

    ```yaml
    INHERIT: mkdocs-base.yml
    
    plugins:
      - output-as-input:
          stage_dir: stage-dev
          verbose: true
          prettify: true
    ```

## Performance Considerations

Different configurations have different performance impacts:

| Option | Performance Impact | Notes |
|--------|-------------------|-------|
| `minify` | Low | Slight overhead for regex processing |
| `prettify` | Medium | BeautifulSoup prettify is slower |
| `preserve_links` | Low | Simple string replacements |
| `verbose` | Negligible | Only affects logging |
| Multiple `html_element` | Medium | Processes each selector separately |

## Migration Guide

### From Version 0.x to 1.x

If upgrading from an older version, note these changes:

```yaml
# Old configuration (0.x)
plugins:
  - output-as-input:
      output_dir: stage  # Renamed
      extract_tag: main  # Renamed

# New configuration (1.x)
plugins:
  - output-as-input:
      stage_dir: stage      # New name
      html_element: main    # New name
```

## Default Behavior Reference

When no configuration is provided, these defaults apply:

```yaml
plugins:
  - output-as-input:
      stage_dir: "stage"
      html_element: "main"
      target_tag: "article"
      include_frontmatter: true
      preserve_links: false
      minify: false
      prettify: false
      verbose: false
```

## See Also

- [Getting Started](getting-started.md) - Initial setup guide
- [Examples](examples.md) - Real-world configuration examples
- [API Reference](api/index.md) - Programming interface
- [Troubleshooting](troubleshooting.md) - Common configuration issues
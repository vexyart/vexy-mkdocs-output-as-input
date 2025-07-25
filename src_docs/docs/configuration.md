---
title: Configuration
description: Complete configuration reference for the MkDocs Output as Input plugin
---

# Configuration

The MkDocs Output as Input plugin provides several configuration options to customize its behavior. All options are set in your `mkdocs.yml` file.

## Configuration Options

### `stage_dir`

**Type**: `str`  
**Default**: `"stage"`

The directory where cousin files will be created. Can be relative to the MkDocs project root or an absolute path.

```yaml
plugins:
  - output-as-input:
      stage_dir: "output/markdown"
```

!!! tip
    Use an absolute path to place files outside your project:
    ```yaml
    stage_dir: "/var/www/content"
    ```

### `html_element`

**Type**: `str`  
**Default**: `"main"`

The HTML element or CSS selector to extract from rendered pages. 

Common values:
- `"main"` - Main content area (default)
- `"article"` - Article content
- `"#content"` - Element with id="content"
- `".documentation"` - Elements with class="documentation"
- `"div.content"` - Div elements with class="content"

```yaml
plugins:
  - output-as-input:
      html_element: "article"
```

!!! warning
    If the specified element is not found, the plugin will log a warning and skip that page.

### `target_tag`

**Type**: `str`  
**Default**: `"article"`

The HTML tag used to wrap the extracted content in cousin files.

```yaml
plugins:
  - output-as-input:
      target_tag: "section"
```

This would produce:
```markdown
---
title: Page Title
---

<section>
<!-- extracted content -->
</section>
```

### `verbose`

**Type**: `bool`  
**Default**: `false`

Enable detailed debug logging to help troubleshoot issues.

```yaml
plugins:
  - output-as-input:
      verbose: true
```

When enabled, the plugin logs:
- Each file being processed
- Extraction results
- Any errors or warnings
- File creation details

## Complete Example

Here's a complete configuration example showing all options:

```yaml
site_name: My Documentation
site_url: https://example.com/docs/

theme:
  name: material

plugins:
  - search
  - output-as-input:
      stage_dir: "staged-content"
      html_element: "article.md-content"
      target_tag: "div"
      verbose: true

nav:
  - Home: index.md
  - Guide: guide.md
  - API: api.md
```

## Configuration Patterns

### For Static Site Generators

When using with Hugo:
```yaml
plugins:
  - output-as-input:
      stage_dir: "../hugo/content/docs"
      html_element: "main"
      target_tag: "div"  # Hugo prefers div
```

When using with Jekyll:
```yaml
plugins:
  - output-as-input:
      stage_dir: "../jekyll/_posts"
      html_element: "article"
      target_tag: "article"
```

### For Different Themes

Material for MkDocs:
```yaml
plugins:
  - output-as-input:
      html_element: "article.md-content__inner"
```

ReadTheDocs theme:
```yaml
plugins:
  - output-as-input:
      html_element: "div.rst-content"
```

Default MkDocs theme:
```yaml
plugins:
  - output-as-input:
      html_element: "div.col-md-9"
```

### For Print/PDF Generation

```yaml
plugins:
  - output-as-input:
      stage_dir: "print-output"
      html_element: "main"
      target_tag: "div"
      # Then use pandoc or similar to convert
```

## Environment Variables

You can use environment variables in configuration:

```yaml
plugins:
  - output-as-input:
      stage_dir: "${OUTPUT_DIR:-stage}"
      verbose: "${DEBUG:-false}"
```

## Validation

The plugin validates configuration on startup:

- `stage_dir` must be a valid path
- `html_element` must be a non-empty string
- `target_tag` must be a valid HTML tag name
- `verbose` must be a boolean

Invalid configuration will raise an error during MkDocs build.

## Default Behavior

With no configuration, the plugin uses these defaults:

```yaml
plugins:
  - output-as-input
  # Equivalent to:
  # - output-as-input:
  #     stage_dir: "stage"
  #     html_element: "main"
  #     target_tag: "article"
  #     verbose: false
```
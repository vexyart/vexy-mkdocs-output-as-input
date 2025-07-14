---
title: Configuration
description: Complete configuration reference for the MkDocs Output as Input plugin
---

# Configuration

The MkDocs Output as Input plugin provides several configuration options to customize its behavior.

## Basic Configuration

```yaml
plugins:
  - output-as-input:
      stage_dir: stage          # Output directory (default: 'stage')
      html_element: main        # HTML element to extract (default: 'main')
      target_tag: article       # Tag to use in output (default: 'article')
      verbose: false           # Enable verbose logging (default: false)
```

## Configuration Options

### `stage_dir`

- **Type**: `string`
- **Default**: `"stage"`
- **Description**: Directory name for output files, relative to your project root

**Example**:
```yaml
plugins:
  - output-as-input:
      stage_dir: processed
```

This creates cousin files in a `processed/` directory instead of `stage/`.

### `html_element`

- **Type**: `string`
- **Default**: `"main"`
- **Description**: CSS selector for the HTML element to extract from the built pages

**Common values**:
- `"main"` - Extract the main content area
- `"article"` - Extract article elements
- `"div.content"` - Extract divs with class "content"
- `"#content"` - Extract element with id "content"

**Example**:
```yaml
plugins:
  - output-as-input:
      html_element: article.post-content
```

### `target_tag`

- **Type**: `string`
- **Default**: `"article"`
- **Description**: HTML tag to use in the output file (replaces the extracted element's tag)

**Example**:
```yaml
plugins:
  - output-as-input:
      html_element: main
      target_tag: section
```

This extracts `<main>` elements and converts them to `<section>` in the output.

### `verbose`

- **Type**: `boolean`
- **Default**: `false`
- **Description**: Enable detailed logging for debugging

**Example**:
```yaml
plugins:
  - output-as-input:
      verbose: true
```

## Configuration Examples

### Material Theme

For the Material theme, you might want to extract the inner content:

```yaml
plugins:
  - output-as-input:
      html_element: article.md-content__inner
      target_tag: div
```

### Custom Output Directory

```yaml
plugins:
  - output-as-input:
      stage_dir: hugo/content
      html_element: main
      target_tag: article
```

### Debug Mode

```yaml
plugins:
  - output-as-input:
      verbose: true
```

## Advanced Usage

### Multiple Processing Steps

You can use the plugin in a multi-step build process:

1. **MkDocs build** with output-as-input plugin
2. **Custom processing** of the stage directory
3. **Secondary build** with another static site generator

```bash
#!/bin/bash
# Build with MkDocs
mkdocs build

# Post-process the staged files
python process_stage.py

# Build with Hugo
hugo --contentDir=stage/
```

### Theme Compatibility

The plugin should work with any MkDocs theme. For best results:

1. Inspect your theme's HTML structure
2. Identify the main content element
3. Configure `html_element` accordingly

**Finding the right element**:
1. Build your site normally
2. Open a page in your browser
3. Use developer tools to inspect the HTML
4. Look for the element containing your content

## Troubleshooting

### No Output Files

If no cousin files are created:

1. Enable verbose mode
2. Check that HTML files exist in the site directory
3. Verify that the `html_element` selector matches your theme

### Empty Output Files

If cousin files are empty:

1. Check that the `html_element` selector is correct
2. Verify that the element exists in your HTML output
3. Try a more general selector like `"body"` for testing

### Permission Errors

If you get permission errors:

1. Ensure the project directory is writable
2. Try a different `stage_dir` location
3. Check file system permissions

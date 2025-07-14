---
title: API Reference
description: Complete API reference for the MkDocs Output as Input plugin
---

# API Reference

This page provides detailed API documentation for the MkDocs Output as Input plugin.

## Plugin Class

::: mkdocs_output_as_input.plugin.OutputAsInputPlugin

## Configuration Schema

The plugin accepts the following configuration options:

### stage_dir

**Type**: `str`  
**Default**: `"stage"`

Directory name for output files, relative to the project root.

### html_element

**Type**: `str`  
**Default**: `"main"`

CSS selector for the HTML element to extract from built pages.

### target_tag

**Type**: `str`  
**Default**: `"article"`

HTML tag to use in the output file (replaces the extracted element's tag).

### verbose

**Type**: `bool`  
**Default**: `False`

Enable detailed logging for debugging.

## Plugin Methods

### on_config

**Signature**: `on_config(self, config: dict[str, Any]) -> dict[str, Any]`

Called when MkDocs configuration is loaded. Stores site and docs directories for later use.

**Parameters**:
- `config`: The MkDocs configuration dictionary

**Returns**:
- The unmodified configuration dictionary

### on_page_read_source

**Signature**: `on_page_read_source(self, page: Page, config: dict[str, Any]) -> Optional[str]`

Called when MkDocs reads a source file. Captures the source content and frontmatter.

**Parameters**:
- `page`: The MkDocs Page object
- `config`: The MkDocs configuration dictionary

**Returns**:
- `None` (allows MkDocs to continue with original processing)

### on_post_build

**Signature**: `on_post_build(self, config: dict[str, Any]) -> None`

Called after MkDocs completes the build. Processes HTML files and creates cousin Markdown files.

**Parameters**:
- `config`: The MkDocs configuration dictionary

**Returns**:
- `None`

### _process_file

**Signature**: `_process_file(self, src_path: str, file_info: dict[str, Any], stage_dir: Path) -> None`

Internal method to process a single file: extract HTML and create cousin Markdown.

**Parameters**:
- `src_path`: Path to the source file relative to docs directory
- `file_info`: Dictionary containing frontmatter and source file path
- `stage_dir`: Path to the stage directory

**Returns**:
- `None`

## Usage Examples

### Basic Plugin Usage

```python
from mkdocs_output_as_input.plugin import OutputAsInputPlugin

# Create plugin instance
plugin = OutputAsInputPlugin()

# Configure plugin
plugin.config = {
    "stage_dir": "custom_stage",
    "html_element": "article",
    "target_tag": "div",
    "verbose": True,
}
```

### Manual Processing

```python
from pathlib import Path
from mkdocs_output_as_input.plugin import OutputAsInputPlugin

# Initialize plugin
plugin = OutputAsInputPlugin()
plugin.config = {
    "stage_dir": "stage",
    "html_element": "main",
    "target_tag": "article",
    "verbose": False,
}

# Set up directories
plugin.site_dir = Path("site")
plugin.docs_dir = Path("docs")

# Process a file manually
file_info = {
    "frontmatter": {"title": "Test Page"},
    "abs_src_path": "/path/to/source.md",
}
stage_dir = Path("stage")
stage_dir.mkdir(exist_ok=True)

plugin._process_file("test.md", file_info, stage_dir)
```

## Error Handling

The plugin includes comprehensive error handling:

### File Read Errors

```python
try:
    with open(page.file.abs_src_path, encoding="utf-8") as f:
        content = f.read()
except Exception as e:
    logger.error(f"OutputAsInput: Failed to read {src_path}: {e}")
    return None
```

### YAML Parse Errors

```python
try:
    frontmatter = yaml.safe_load(fm_text) or {}
except yaml.YAMLError as e:
    logger.warning(f"OutputAsInput: Failed to parse frontmatter in {src_path}: {e}")
```

### HTML Processing Errors

```python
try:
    with open(full_html_path, encoding="utf-8") as f:
        html_content = f.read()
except Exception as e:
    logger.error(f"OutputAsInput: Failed to read HTML {full_html_path}: {e}")
    return
```

## Logging

The plugin uses Python's standard logging module. Enable verbose mode to see detailed output:

```yaml
plugins:
  - output-as-input:
      verbose: true
```

**Log levels**:
- `INFO`: General information about processing
- `WARNING`: Non-fatal issues (missing HTML elements, YAML parse errors)
- `ERROR`: Fatal errors that prevent processing

## Dependencies

The plugin requires the following dependencies:

- `mkdocs>=1.6.0`
- `beautifulsoup4>=4.12.0`
- `pyyaml>=6.0`

## Version Information

The plugin version is managed by `setuptools-scm` and available as:

```python
from mkdocs_output_as_input import __version__
print(__version__)
```

## Thread Safety

The plugin is designed to be thread-safe and can handle concurrent MkDocs builds. Each plugin instance maintains its own state in the `source_files` dictionary.

## Performance Considerations

- The plugin processes files sequentially during the `on_post_build` phase
- Memory usage scales with the number of source files
- HTML parsing is done using BeautifulSoup4's built-in parser for consistency
- File I/O is optimized with proper encoding handling

## Extension Points

The plugin can be extended by subclassing `OutputAsInputPlugin`:

```python
from mkdocs_output_as_input.plugin import OutputAsInputPlugin

class CustomOutputPlugin(OutputAsInputPlugin):
    def _process_file(self, src_path, file_info, stage_dir):
        # Custom processing logic
        super()._process_file(src_path, file_info, stage_dir)
        
        # Additional post-processing
        cousin_path = stage_dir / src_path
        if cousin_path.exists():
            content = cousin_path.read_text()
            # Modify content as needed
            cousin_path.write_text(modified_content)
```

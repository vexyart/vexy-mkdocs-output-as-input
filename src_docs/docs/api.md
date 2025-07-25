---
title: API Reference
description: Technical API documentation for the MkDocs Output as Input plugin
---

# API Reference

This page provides detailed technical documentation for the MkDocs Output as Input plugin.

## Plugin Class

::: mkdocs_output_as_input.plugin.OutputAsInputPlugin
    options:
      show_source: true
      show_root_heading: true
      show_symbol_type_heading: true
      show_symbol_type_toc: true
      inherited_members: true
      members:
        - config_scheme
        - on_page_read_source
        - on_post_build

## Configuration Schema

The plugin uses MkDocs' configuration validation system:

```python
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

class OutputAsInputPlugin(BasePlugin):
    config_scheme = (
        ('stage_dir', config_options.Type(str, default='stage')),
        ('html_element', config_options.Type(str, default='main')),
        ('target_tag', config_options.Type(str, default='article')),
        ('verbose', config_options.Type(bool, default=False)),
    )
```

## Event Hooks

### `on_page_read_source`

Called when MkDocs reads a source file. The plugin uses this to capture frontmatter.

**Parameters:**
- `page` - The MkDocs Page object
- `config` - The MkDocs configuration

**Returns:**
- The original page content (unmodified)

**Behavior:**
1. Extracts YAML frontmatter from the source file
2. Stores source path and frontmatter for later use
3. Handles parsing errors gracefully

### `on_post_build`

Called after MkDocs completes the build. This is where cousin files are created.

**Parameters:**
- `config` - The MkDocs configuration

**Behavior:**
1. Creates the stage directory if needed
2. Processes each HTML file in the site directory
3. Extracts content using BeautifulSoup
4. Creates cousin Markdown files with frontmatter + HTML

## Internal Methods

### `_extract_frontmatter(content: str) -> tuple[dict, str]`

Extracts YAML frontmatter from Markdown content.

**Parameters:**
- `content` - Raw Markdown file content

**Returns:**
- Tuple of (frontmatter_dict, remaining_content)

**Example:**
```python
frontmatter, content = plugin._extract_frontmatter("""---
title: My Page
tags: [python, mkdocs]
---

# Content here
""")
# frontmatter = {'title': 'My Page', 'tags': ['python', 'mkdocs']}
# content = "\n# Content here\n"
```

### `_create_cousin_file(site_dir: str, rel_path: str, frontmatter: dict, html_content: str)`

Creates a cousin Markdown file with frontmatter and HTML content.

**Parameters:**
- `site_dir` - The MkDocs site output directory
- `rel_path` - Relative path of the source file
- `frontmatter` - Dictionary of frontmatter data
- `html_content` - Extracted HTML content

## Data Storage

The plugin stores page information during build:

```python
self.page_sources: Dict[str, Dict[str, Any]] = {
    'index.md': {
        'source_path': 'docs/index.md',
        'frontmatter': {'title': 'Home', 'date': '2024-01-20'}
    },
    'guide.md': {
        'source_path': 'docs/guide.md', 
        'frontmatter': {'title': 'User Guide'}
    }
}
```

## Error Handling

The plugin handles various error cases:

### Missing HTML Element
```python
if not element:
    logger.warning(f"Element '{self.config['html_element']}' not found")
    return
```

### Invalid Frontmatter
```python
try:
    frontmatter = yaml.safe_load(fm_text) or {}
except yaml.YAMLError as e:
    logger.error(f"Invalid YAML frontmatter: {e}")
    frontmatter = {}
```

### File I/O Errors
```python
try:
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
except IOError as e:
    logger.error(f"Failed to write file: {e}")
```

## Usage in Python

### Programmatic Usage

```python
from mkdocs_output_as_input import OutputAsInputPlugin
from mkdocs.config import load_config

# Load MkDocs configuration
config = load_config('mkdocs.yml')

# Create plugin instance
plugin = OutputAsInputPlugin()
plugin.load_config(
    options={'stage_dir': 'output', 'verbose': True},
    config_file_path='mkdocs.yml'
)

# Use in custom build process
plugin.on_page_read_source(page, config)
plugin.on_post_build(config)
```

### Custom Integration

```python
import mkdocs.plugins

# Register custom event handler
@mkdocs.plugins.event_priority(50)
def on_post_build(config):
    # Custom post-processing after Output as Input
    stage_dir = Path(config['plugins']['output-as-input']['stage_dir'])
    for md_file in stage_dir.glob('**/*.md'):
        # Additional processing
        process_cousin_file(md_file)
```

## CLI Tool

The plugin includes a CLI tool for testing:

::: mkdocs_output_as_input.cli
    options:
      show_source: true
      members:
        - main
        - process_file

### CLI Usage

```bash
# Process a single file
output-as-input process file.html --element main --output output.md

# Process directory
output-as-input process site/ --element article --stage-dir stage/

# With verbose output
output-as-input process site/ --verbose
```

## Type Hints

The plugin uses type hints for better IDE support:

```python
from typing import Dict, Any, Optional, Tuple
from mkdocs.structure.pages import Page
from mkdocs.config.defaults import MkDocsConfig

def on_page_read_source(
    self, 
    page: Page, 
    config: MkDocsConfig
) -> Optional[str]: ...

def _extract_frontmatter(
    self, 
    content: str
) -> Tuple[Dict[str, Any], str]: ...
```

## Logging

The plugin uses the `loguru` logger:

```python
from loguru import logger

# Info level (always shown)
logger.info(f"Processing page: {page.file.src_path}")

# Debug level (shown with verbose=true)
logger.debug(f"Extracted frontmatter: {frontmatter}")

# Warning level
logger.warning(f"Element not found: {element}")

# Error level  
logger.error(f"Failed to parse HTML: {e}")
```

## Testing

Test helpers for plugin development:

```python
import pytest
from mkdocs_output_as_input import OutputAsInputPlugin

@pytest.fixture
def plugin():
    plugin = OutputAsInputPlugin()
    plugin.load_config(options={}, config_file_path='')
    return plugin

def test_frontmatter_extraction(plugin):
    content = "---\ntitle: Test\n---\n# Content"
    fm, body = plugin._extract_frontmatter(content)
    assert fm == {'title': 'Test'}
    assert '# Content' in body
```
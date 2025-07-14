
# `https://github.com/vexyart/vexy-mkdocs-output-as-input`

## Project Overview

This is an MkDocs plugin called `vexy-mkdocs-output-as-input` that captures rendered HTML output from MkDocs and creates "cousin" Markdown files containing the original YAML frontmatter plus the extracted HTML content. This enables post-processing workflows with other static site generators.

## Development Commands

### Setup & Installation
```bash
# Install development dependencies
uv pip install -e ".[dev,test,docs]"

# Install pre-commit hooks
pre-commit install
```

### Testing
```bash
# Run full test suite
python -m pytest

# Run with coverage
python -m pytest --cov=mkdocs_output_as_input --cov-report=term-missing

# Run specific test
python -m pytest tests/test_plugin.py::test_plugin_default_config -v
```

### Code Quality
```bash
# Run all pre-commit hooks
pre-commit run --all-files

# Individual tools
python -m ruff check src tests
python -m ruff format src tests
python -m mypy src
```

### Documentation
```bash
# Serve documentation locally
mkdocs serve

# Build documentation
mkdocs build
```

## Architecture & Key Components

### Plugin Structure
The plugin is implemented in `src/mkdocs_output_as_input/plugin.py` with:
- `OutputAsInputPlugin` class extending `mkdocs.plugins.BasePlugin`
- Configuration schema with options: `stage_dir`, `html_element`, `target_tag`, `verbose`
- Two main hooks:
  - `on_page_read_source`: Captures source files and frontmatter during MkDocs processing
  - `on_post_build`: Post-processes HTML and creates cousin files after build

### Plugin Configuration
In `mkdocs.yml`:
```yaml
plugins:
  - output-as-input:
      stage_dir: stage          # Output directory (default: "stage")
      html_element: main        # HTML element to extract (default: "main")
      target_tag: article       # Tag to wrap content (default: "article")
      verbose: true            # Enable debug logging
```

### Key Implementation Details
- Uses BeautifulSoup4 for HTML parsing and extraction
- Preserves YAML frontmatter from source Markdown files
- Creates output files with pattern: `{stage_dir}/{original_path}.md`
- Handles edge cases: missing HTML elements, parsing errors, file I/O issues

## Testing Guidelines

The test suite in `tests/test_plugin.py` covers:
- Default configuration behavior
- Custom configuration options
- Frontmatter preservation
- HTML extraction with different selectors
- Error handling scenarios
- Verbose logging output

When adding features:
1. Write tests first following existing patterns
2. Ensure >90% code coverage (CI enforces this)
3. Test both success and error paths
4. Use the provided fixtures (`plugin_instance`, `temp_docs_dir`)

## Release Process

The project uses GitHub Actions for automated releases:
1. Update version in CHANGELOG.md following Keep a Changelog format
2. Create a release on GitHub with tag `v{version}`
3. CI automatically publishes to PyPI using trusted publishing

## Common Development Tasks

### Adding a New Configuration Option
1. Add to `config_scheme` in `plugin.py`
2. Update `__init__` method to use the option
3. Implement logic in relevant hook methods
4. Add tests for the new option
5. Update documentation in README.md and docs/

### Debugging Plugin Behavior
1. Enable verbose mode in mkdocs.yml
2. Use `logger.debug()` statements (already configured with loguru)
3. Run MkDocs with: `mkdocs build -v`
4. Check the stage directory for output files

### Working with MkDocs Events
The plugin uses MkDocs event hooks. Key references:
- [MkDocs Plugin Development](https://www.mkdocs.org/dev-guide/plugins/)
- [Available Events](https://www.mkdocs.org/dev-guide/plugins/#events)
- Current hooks: `on_page_read_source`, `on_post_build`

## Project-Specific Notes

- The plugin must handle various MkDocs themes gracefully
- Output files should be valid Markdown with proper YAML frontmatter
- The stage directory is created automatically if it doesn't exist
- BeautifulSoup parser uses 'html.parser' for consistency across platforms
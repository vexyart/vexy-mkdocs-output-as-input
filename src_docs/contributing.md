---
title: Contributing Guide
description: How to contribute to MkDocs Output as Input plugin
---

# Contributing to MkDocs Output as Input

Thank you for your interest in contributing to MkDocs Output as Input! This guide will help you get started.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct:

- **Be respectful**: Treat everyone with respect
- **Be collaborative**: Work together towards common goals
- **Be inclusive**: Welcome contributors of all backgrounds
- **Be professional**: Keep discussions focused and constructive

## Ways to Contribute

### 🐛 Report Bugs

Found a bug? Please help us fix it!

1. **Check existing issues** to avoid duplicates
2. **Create a new issue** with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)
   - Minimal example code

Example:
```markdown
**Description**
Cousin files are not created when using Material theme with custom HTML element.

**Steps to Reproduce**
1. Install plugin: `pip install vexy-mkdocs-output-as-input`
2. Configure with: `html_element: .custom-class`
3. Run: `mkdocs build`

**Expected Behavior**
Files created in stage/ directory

**Actual Behavior**
No files created, no error message

**Environment**
- OS: Ubuntu 22.04
- Python: 3.10.6
- MkDocs: 1.5.0
- Plugin: 1.0.0
```

### 💡 Suggest Features

Have an idea for improvement?

1. **Check existing issues** and discussions
2. **Open a discussion** to gather feedback
3. **Create a feature request** with:
   - Use case description
   - Proposed solution
   - Alternative approaches
   - Examples

### 📝 Improve Documentation

Documentation improvements are always welcome!

- Fix typos or clarify explanations
- Add examples or use cases
- Translate documentation
- Improve API documentation

### 🔧 Submit Code Changes

Ready to code? Follow these steps:

#### 1. Set Up Development Environment

```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/vexy-mkdocs-output-as-input.git
cd vexy-mkdocs-output-as-input

# Create a branch
git checkout -b feature/your-feature-name

# Install development dependencies
./scripts/dev-setup.sh
```

#### 2. Make Your Changes

Follow our coding standards:

**Python Style Guide**
```python
# Use type hints
from pathlib import Path
from typing import Optional, List

def process_files(
    paths: List[Path],
    verbose: bool = False
) -> Optional[int]:
    """Process multiple files.
    
    Args:
        paths: List of file paths to process
        verbose: Enable verbose logging
        
    Returns:
        Number of files processed, or None on error
    """
    count = 0
    for path in paths:
        if verbose:
            logger.info(f"Processing {path}")
        # Process file
        count += 1
    return count
```

**Commit Message Format**
```bash
# Format: <type>(<scope>): <subject>
#
# Types:
# - feat: New feature
# - fix: Bug fix
# - docs: Documentation only
# - style: Formatting, missing semi-colons, etc.
# - refactor: Code change that neither fixes a bug nor adds a feature
# - test: Adding missing tests
# - chore: Changes to build process or auxiliary tools

git commit -m "feat(plugin): add support for custom processors"
git commit -m "fix(parser): handle malformed HTML gracefully"
git commit -m "docs(readme): update installation instructions"
```

#### 3. Test Your Changes

```bash
# Run all tests
make test

# Run specific tests
pytest tests/test_plugin.py::test_specific_function -v

# Check coverage
pytest --cov=mkdocs_output_as_input --cov-report=term-missing
```

#### 4. Update Documentation

If your change affects user-facing functionality:

1. Update relevant docs in `src_docs/`
2. Add examples if applicable
3. Update CHANGELOG.md

#### 5. Submit Pull Request

1. **Push your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request** with:
   - Descriptive title
   - Summary of changes
   - Link to related issues
   - Screenshots if applicable

3. **PR Description Template**:
   ```markdown
   ## Description
   Brief description of changes
   
   ## Related Issue
   Fixes #123
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Performance improvement
   
   ## Checklist
   - [ ] Tests pass
   - [ ] Documentation updated
   - [ ] CHANGELOG.md updated
   - [ ] Code follows style guidelines
   ```

## Development Guidelines

### Code Quality Standards

#### Testing Requirements

- All new features must have tests
- Maintain or improve code coverage (>90%)
- Include both positive and negative test cases
- Test edge cases and error conditions

Example test:
```python
def test_custom_processor(plugin, temp_dir):
    """Test custom processor functionality."""
    # Arrange: Set up test conditions
    plugin.config["custom_processor"] = lambda x: x.upper()
    test_file = temp_dir / "test.md"
    test_file.write_text("# hello world")
    
    # Act: Execute the functionality
    plugin.process_file(test_file)
    
    # Assert: Verify the results
    output = (temp_dir / "stage" / "test.md").read_text()
    assert "HELLO WORLD" in output
```

#### Documentation Standards

- Use Google-style docstrings
- Include type hints
- Provide usage examples
- Document exceptions

```python
def extract_content(
    html: str,
    selector: str = "main"
) -> Optional[str]:
    """Extract content from HTML using CSS selector.
    
    Args:
        html: HTML document as string
        selector: CSS selector to match elements
        
    Returns:
        Extracted HTML content or None if not found
        
    Raises:
        ValueError: If selector is empty
        ParseError: If HTML is malformed
        
    Example:
        >>> html = "<main><p>Content</p></main>"
        >>> extract_content(html, "main")
        '<main><p>Content</p></main>'
    """
```

### Performance Considerations

- Use generators for large datasets
- Implement caching where appropriate
- Profile code for bottlenecks
- Consider memory usage

```python
# Good: Generator for memory efficiency
def process_files(self, paths: List[Path]) -> Iterator[Path]:
    """Process files one at a time."""
    for path in paths:
        yield self.process_single_file(path)

# Bad: Loading everything into memory
def process_files(self, paths: List[Path]) -> List[Path]:
    """Process all files at once."""
    return [self.process_single_file(p) for p in paths]
```

### Security Guidelines

- Sanitize user input
- Use safe YAML loading
- Validate file paths
- Handle sensitive data carefully

```python
# Good: Safe YAML loading
import yaml
data = yaml.safe_load(content)

# Bad: Unsafe loading
data = yaml.load(content, Loader=yaml.FullLoader)
```

## Review Process

### What to Expect

1. **Automated Checks**: CI runs tests, linting, and coverage
2. **Code Review**: Maintainers review code quality and design
3. **Feedback**: You may receive suggestions or requests for changes
4. **Iteration**: Make requested changes and push updates
5. **Merge**: Once approved, your PR will be merged

### Review Criteria

- **Correctness**: Does it work as intended?
- **Tests**: Are there adequate tests?
- **Documentation**: Is it well-documented?
- **Style**: Does it follow conventions?
- **Performance**: Is it efficient?
- **Security**: Is it secure?

## Recognition

### Contributors

All contributors are recognized in:
- GitHub contributors page
- CHANGELOG.md for significant contributions
- Special mentions for major features

### Types of Contributions

We value all contributions:
- 🐛 Bug reports and fixes
- 💡 Feature suggestions and implementations
- 📝 Documentation improvements
- 🧪 Test additions
- 🎨 UI/UX improvements
- 🌐 Translations
- 💬 Helping others in discussions

## Getting Help

### Before Asking

1. Read the documentation
2. Search existing issues
3. Check FAQ and troubleshooting guide
4. Try debugging yourself

### Where to Ask

- **GitHub Discussions**: General questions
- **Issue Comments**: Specific to an issue
- **Pull Request**: Code-related questions

### How to Ask

Provide:
- Context and background
- What you've tried
- Minimal example
- Error messages/logs

## Release Process

### Version Numbering

We follow [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

### Release Cycle

- **Patch releases**: As needed for bugs
- **Minor releases**: Monthly or bi-monthly
- **Major releases**: Yearly or as needed

### Becoming a Maintainer

Active contributors may be invited to become maintainers. Criteria:
- Consistent quality contributions
- Good understanding of codebase
- Helpful in community discussions
- Commitment to project values

## Thank You!

Your contributions make this project better for everyone. We appreciate your time and effort!

Questions? Feel free to ask in [GitHub Discussions](https://github.com/vexyart/vexy-mkdocs-output-as-input/discussions).
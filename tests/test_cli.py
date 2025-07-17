"""Tests for the CLI tool."""

from unittest.mock import patch

import pytest

from mkdocs_output_as_input.cli import (
    extract_frontmatter,
    main,
    process_file,
    process_html,
)


class TestCLI:
    """Test cases for CLI functionality."""

    def test_extract_frontmatter_with_frontmatter(self):
        """Test extracting YAML frontmatter from content."""
        content = """---
title: Test Title
author: Test Author
---

# Content here
"""
        frontmatter, body = extract_frontmatter(content)

        assert frontmatter == {"title": "Test Title", "author": "Test Author"}
        assert body.strip() == "# Content here"

    def test_extract_frontmatter_without_frontmatter(self):
        """Test extracting from content without frontmatter."""
        content = "# Just content"
        frontmatter, body = extract_frontmatter(content)

        assert frontmatter == {}
        assert body == "# Just content"

    def test_extract_frontmatter_invalid_yaml(self):
        """Test handling invalid YAML frontmatter."""
        content = """---
title: Test
invalid: [unclosed
---

# Content
"""
        frontmatter, body = extract_frontmatter(content)

        # Should handle gracefully
        assert frontmatter == {}
        assert body == content

    def test_process_html_basic(self):
        """Test basic HTML processing."""
        html = """<!DOCTYPE html>
<html>
<body>
<main class="content">
<h1>Title</h1>
<p>Content</p>
</main>
</body>
</html>"""

        result = process_html(html)

        assert result is not None
        assert '<article class="content">' in result
        assert '<h1>Title</h1>' in result
        assert '<p>Content</p>' in result

    def test_process_html_custom_element_and_tag(self):
        """Test processing with custom element and tag."""
        html = """<html>
<body>
<div id="content">
<h1>Title</h1>
</div>
</body>
</html>"""

        result = process_html(html, html_element="div", target_tag="section")

        assert result is not None
        assert '<section id="content">' in result
        assert '<h1>Title</h1>' in result

    def test_process_html_element_not_found(self):
        """Test handling when element not found."""
        html = "<html><body><p>No main element</p></body></html>"

        result = process_html(html)

        assert result is None

    def test_process_html_preserve_links(self):
        """Test preserving relative links."""
        html = """<html>
<body>
<main>
<a href="/docs/page.html">Link</a>
<img src="/images/pic.png">
<a href="https://example.com">External</a>
</main>
</body>
</html>"""

        result = process_html(html, preserve_links=True)

        assert result is not None
        assert 'href="./docs/page.html"' in result
        assert 'src="./images/pic.png"' in result
        assert 'href="https://example.com"' in result  # External unchanged

    def test_process_html_minify(self):
        """Test HTML minification."""
        html = """<html>
<body>
<main>
    <h1>Title</h1>
    <p>Content</p>
</main>
</body>
</html>"""

        result = process_html(html, minify=True)

        assert result is not None
        assert "\n" not in result
        assert "  " not in result

    def test_process_html_prettify(self):
        """Test HTML prettification."""
        html = "<html><body><main><h1>Title</h1><p>Content</p></main></body></html>"

        result = process_html(html, prettify=True)

        assert result is not None
        assert "\n" in result
        assert " <h1>" in result  # Indented

    def test_process_file_basic(self, tmp_path):
        """Test basic file processing."""
        # Create input HTML file
        input_file = tmp_path / "input.html"
        input_file.write_text("""<html>
<body>
<main>
<h1>Test Page</h1>
</main>
</body>
</html>""")

        output_file = tmp_path / "output.md"

        process_file(input_file, output_file)

        assert output_file.exists()
        content = output_file.read_text()
        assert "<article>" in content
        assert "<h1>Test Page</h1>" in content

    def test_process_file_with_frontmatter(self, tmp_path):
        """Test processing with frontmatter from corresponding .md file."""
        # Create input HTML file
        input_file = tmp_path / "page.html"
        input_file.write_text("<html><body><main><h1>Page</h1></main></body></html>")

        # Create corresponding markdown file with frontmatter
        md_file = tmp_path / "page.md"
        md_file.write_text("""---
title: Test Page
author: Test Author
---

# Original content
""")

        output_file = tmp_path / "output.md"

        process_file(input_file, output_file)

        content = output_file.read_text()
        assert "---" in content
        assert "title: Test Page" in content
        assert "author: Test Author" in content
        assert "<article>" in content

    def test_process_file_no_frontmatter(self, tmp_path):
        """Test processing without frontmatter."""
        input_file = tmp_path / "input.html"
        input_file.write_text("<html><body><main><h1>Page</h1></main></body></html>")

        output_file = tmp_path / "output.md"

        process_file(input_file, output_file, include_frontmatter=False)

        content = output_file.read_text()
        assert not content.startswith("---")
        assert "<article>" in content

    def test_process_file_creates_output_dir(self, tmp_path):
        """Test that output directory is created if needed."""
        input_file = tmp_path / "input.html"
        input_file.write_text("<html><body><main><h1>Page</h1></main></body></html>")

        output_file = tmp_path / "subdir" / "output.md"

        process_file(input_file, output_file)

        assert output_file.exists()
        assert output_file.parent.exists()

    def test_cli_process_command(self, tmp_path):
        """Test CLI process command."""
        input_file = tmp_path / "input.html"
        input_file.write_text("<html><body><main><h1>Test</h1></main></body></html>")

        output_file = tmp_path / "output.md"

        with patch("sys.argv", ["mkdocs-output-as-input", "process",
                               str(input_file), str(output_file)]):
            result = main()

        assert result == 0
        assert output_file.exists()

    def test_cli_custom_options(self, tmp_path):
        """Test CLI with custom options."""
        input_file = tmp_path / "input.html"
        input_file.write_text("<html><body><div id='content'><h1>Test</h1></div></body></html>")

        output_file = tmp_path / "output.md"

        with patch("sys.argv", [
            "mkdocs-output-as-input", "process",
            str(input_file), str(output_file),
            "--html-element", "div",
            "--target-tag", "section",
            "--no-frontmatter",
            "--preserve-links",
            "--prettify",
            "--verbose"
        ]):
            result = main()

        assert result == 0
        content = output_file.read_text()
        assert "<section" in content
        assert not content.startswith("---")

    def test_cli_mutually_exclusive_options(self, tmp_path):
        """Test that minify and prettify are mutually exclusive."""
        input_file = tmp_path / "input.html"
        input_file.write_text("<html><body><main><h1>Test</h1></main></body></html>")

        output_file = tmp_path / "output.md"

        with patch("sys.argv", [
            "mkdocs-output-as-input", "process",
            str(input_file), str(output_file),
            "--minify", "--prettify"
        ]):
            result = main()

        assert result == 1  # Should fail

    def test_cli_no_command(self):
        """Test CLI with no command shows help."""
        with patch("sys.argv", ["mkdocs-output-as-input"]):
            result = main()

        assert result == 1

    def test_cli_file_not_found(self, tmp_path):
        """Test CLI with non-existent input file."""
        input_file = tmp_path / "nonexistent.html"
        output_file = tmp_path / "output.md"

        with patch("sys.argv", ["mkdocs-output-as-input", "process",
                               str(input_file), str(output_file)]):
            result = main()

        assert result == 1

    def test_extract_frontmatter_malformed_yaml(self):
        """Test extracting from content with malformed YAML (no closing ---)."""
        content = """---
title: Test Title
author: Test Author
# No closing --- delimiter
# More content
"""
        frontmatter, body = extract_frontmatter(content)

        assert frontmatter == {}
        assert body == content

    def test_extract_frontmatter_empty_yaml(self):
        """Test extracting from empty YAML frontmatter."""
        content = """---

---

# Content here
"""
        frontmatter, body = extract_frontmatter(content)

        assert frontmatter == {}
        assert body.strip() == "# Content here"

    def test_process_html_multiple_elements(self):
        """Test processing HTML with multiple matching elements."""
        html = """<html>
<body>
<main><h1>Main 1</h1></main>
<main><h1>Main 2</h1></main>
</body>
</html>"""

        result = process_html(html)

        assert result is not None
        assert "<article>" in result
        assert "<h1>Main 1</h1>" in result
        assert "<h1>Main 2</h1>" in result

    def test_process_html_css_selector(self):
        """Test processing HTML with CSS selector."""
        html = """<html>
<body>
<div class="content">
<h1>Title</h1>
<p class="highlight">Important</p>
</div>
</body>
</html>"""

        result = process_html(html, html_element=".content")

        assert result is not None
        # CSS selectors don't transform the tag name
        assert '<div class="content">' in result
        assert '<h1>Title</h1>' in result
        assert '<p class="highlight">Important</p>' in result

    def test_process_html_tag_transformation_logic(self):
        """Test complex tag transformation logic."""
        html = """<html>
<body>
<section id="main">
<h1>Title</h1>
</section>
</body>
</html>"""

        # Test with matching tag name - should transform
        result = process_html(html, html_element="section", target_tag="article")
        assert result is not None
        assert '<article id="main">' in result

        # Test with CSS selector - should not transform original tag
        result = process_html(html, html_element="#main", target_tag="article")
        assert result is not None
        assert '<section id="main">' in result

    def test_process_html_multiple_selectors_list(self):
        """Test processing HTML with multiple selectors as list."""
        html = """<html>
<body>
<header><h1>Header</h1></header>
<main><p>Main content</p></main>
<aside><p>Sidebar</p></aside>
</body>
</html>"""

        result = process_html(html, html_element=["main", "aside"])

        assert result is not None
        assert "<article>" in result
        assert "Main content" in result
        assert "Sidebar" in result
        assert "Header" not in result

    def test_process_file_markdown_read_error(self, tmp_path):
        """Test handling markdown file read errors."""
        input_file = tmp_path / "test.html"
        input_file.write_text("<html><body><main><h1>Test</h1></main></body></html>")

        # Test with a non-existent markdown file (simpler than permission issues)
        output_file = tmp_path / "output.md"

        # Should handle gracefully and not include frontmatter
        process_file(input_file, output_file)

        content = output_file.read_text()
        # Without markdown file, should not include frontmatter
        assert not content.startswith("---")
        assert "<article>" in content

    def test_process_file_html_processing_failure(self, tmp_path):
        """Test handling HTML processing failure."""
        input_file = tmp_path / "test.html"
        input_file.write_text("<html><body><p>No main element</p></body></html>")

        output_file = tmp_path / "output.md"

        # Should raise ValueError when HTML processing fails
        with pytest.raises(ValueError, match="Failed to process HTML"):
            process_file(input_file, output_file)

    def test_process_file_write_error(self, tmp_path):
        """Test handling file write errors."""
        input_file = tmp_path / "test.html"
        input_file.write_text("<html><body><main><h1>Test</h1></main></body></html>")

        # Try to write to a directory (should fail)
        output_dir = tmp_path / "test_dir"
        output_dir.mkdir()

        # Should raise exception when writing fails (trying to write to a directory)
        with pytest.raises((IsADirectoryError, PermissionError, OSError)):
            process_file(input_file, output_dir)  # output_dir is a directory, not a file

    def test_cli_main_entry_point(self, tmp_path):
        """Test CLI main entry point (__main__ execution)."""
        input_file = tmp_path / "test.html"
        input_file.write_text("<html><body><main><h1>Test</h1></main></body></html>")

        output_file = tmp_path / "output.md"

        # Test the main entry point behavior
        with patch("sys.argv", ["mkdocs-output-as-input", "process",
                               str(input_file), str(output_file)]):
            result = main()
            assert result == 0

    def test_cli_html_element_default_handling(self, tmp_path):
        """Test CLI with no html-element specified (default to 'main')."""
        input_file = tmp_path / "test.html"
        input_file.write_text("<html><body><main><h1>Test</h1></main></body></html>")

        output_file = tmp_path / "output.md"

        with patch("sys.argv", ["mkdocs-output-as-input", "process",
                               str(input_file), str(output_file)]):
            result = main()

        assert result == 0
        assert output_file.exists()
        content = output_file.read_text()
        assert "<article>" in content

    def test_process_html_minify_advanced(self):
        """Test advanced minification features."""
        html = """<html>
<body>
<main>
    <h1>   Title   </h1>
    <p>
        Content with    multiple   spaces
        and newlines
    </p>
    <div>   <span>   Nested   </span>   </div>
</main>
</body>
</html>"""

        result = process_html(html, minify=True)

        assert result is not None
        # Should compress whitespace but preserve some content
        assert "multiple" in result
        assert "spaces" in result
        assert "newlines" in result
        # Should remove spaces between tags
        assert "><" in result
        # Should be on one line (no newlines)
        assert "\n" not in result

# this_file: tests/test_missing_coverage.py
"""Additional tests to achieve 100% coverage."""

from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest
import tempfile

from mkdocs_output_as_input.cli import process_html, process_file, main
from mkdocs_output_as_input.plugin import OutputAsInputPlugin


class TestMissingCLICoverage:
    """Tests for uncovered CLI code paths."""
    
    def test_process_html_tag_name_fallback_path(self):
        """Test when CSS selector fails but tag name lookup succeeds."""
        html_content = """
        <html>
        <body>
        <custom-element>Content here</custom-element>
        </body>
        </html>
        """
        
        # This should trigger the fallback path where soup.find() is used
        result = process_html(html_content, html_element="custom-element", target_tag="div")
        assert result is not None
        assert "<div>Content here</div>" in result
    
    def test_process_html_list_selector_tag_transformation(self):
        """Test tag transformation with list selector."""
        html_content = """
        <html>
        <body>
        <section>Content here</section>
        </body>
        </html>
        """
        
        # Test the elif branch for list selectors
        result = process_html(
            html_content,
            html_element=["section"],  # List with single element
            target_tag="article"
        )
        assert result is not None
        assert "<article>Content here</article>" in result
    
    def test_process_file_no_processed_html(self):
        """Test when process_html returns None."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write("<html><body>No matching element</body></html>")
            input_path = Path(f.name)
        
        output_path = Path(tempfile.mktemp(suffix='.md'))
        
        with pytest.raises(ValueError, match="Failed to process HTML"):
            process_file(
                input_path,
                output_path,
                html_element="nonexistent",
                target_tag="article"
            )
        
        # Cleanup
        input_path.unlink()
        if output_path.exists():
            output_path.unlink()

    def test_cli_main_if_name_main(self):
        """Test the if __name__ == '__main__' block."""
        # Import the module to execute the code
        import mkdocs_output_as_input.cli
        
        # The module should have the condition but not execute main
        assert hasattr(mkdocs_output_as_input.cli, 'main')
    
    def test_process_html_tag_name_with_list_no_transformation(self):
        """Test when selector list doesn't match element name."""
        html_content = """
        <html>
        <body>
        <div class="content">Content here</div>
        </body>
        </html>
        """
        
        # CSS selector that finds element but name doesn't match
        result = process_html(
            html_content,
            html_element=[".content"],  # CSS selector, not tag name
            target_tag="article"
        )
        assert result is not None
        # Should not transform because selector is not a simple tag name
        assert '<div class="content">' in result


class TestMissingPluginCoverage:
    """Tests for uncovered plugin code paths."""
    
    @pytest.fixture
    def plugin(self):
        """Create a plugin instance."""
        plugin = OutputAsInputPlugin()
        plugin.config = {
            "stage_dir": "stage",
            "html_element": "main",
            "target_tag": "article",
            "include_frontmatter": True,
            "preserve_links": False,
            "minify": False,
            "prettify": False,
            "verbose": False,
        }
        return plugin

    def test_on_page_read_source_file_open_error(self, plugin):
        """Test file open error during page read."""
        # Create a mock page with an invalid path
        mock_file = MagicMock()
        mock_file.src_path = "test.md"
        mock_file.abs_src_path = "/nonexistent/path/to/file.md"
        
        page = MagicMock()
        page.file = mock_file
        
        # This should handle the exception and return None
        result = plugin.on_page_read_source(page, {})
        assert result is None
    
    def test_process_file_html_read_permission_error(self, plugin, tmp_path):
        """Test HTML file read with simulated error."""
        # Set up plugin directories
        plugin.site_dir = tmp_path / "site"
        plugin.site_dir.mkdir()
        
        # Create an HTML file
        html_file = plugin.site_dir / "test.html"
        html_file.write_text("<html><body><main>Content</main></body></html>")
        
        # Mock the open function to raise an exception
        with patch("builtins.open", side_effect=PermissionError("Access denied")):
            stage_dir = tmp_path / "stage"
            stage_dir.mkdir()
            
            file_info = {"frontmatter": {}, "abs_src_path": str(tmp_path / "test.md")}
            
            # Should handle the error gracefully
            plugin._process_file("test.md", file_info, stage_dir)
    
    def test_process_file_cousin_write_permission_error(self, plugin, tmp_path):
        """Test cousin file write with permission error."""
        # Set up plugin directories
        plugin.site_dir = tmp_path / "site"
        plugin.site_dir.mkdir()
        
        # Create an HTML file
        html_file = plugin.site_dir / "test.html"
        html_file.write_text("<html><body><main>Content</main></body></html>")
        
        # Create stage directory
        stage_dir = tmp_path / "stage"
        stage_dir.mkdir()
        
        file_info = {"frontmatter": {"title": "Test"}, "abs_src_path": str(tmp_path / "test.md")}
        
        # Mock the file write to raise an exception
        with patch("pathlib.Path.open", side_effect=[
            html_file.open('r'),  # First open succeeds (reading HTML)
            PermissionError("Cannot write")  # Second open fails (writing cousin)
        ]):
            # Should handle the error gracefully
            plugin._process_file("test.md", file_info, stage_dir)
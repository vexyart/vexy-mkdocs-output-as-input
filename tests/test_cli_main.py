# this_file: tests/test_cli_main.py
"""Test CLI main execution."""

import subprocess
import sys


def test_cli_main_block_execution():
    """Test the if __name__ == '__main__' block executes."""
    result = subprocess.run(
        [sys.executable, "-m", "mkdocs_output_as_input.cli", "--help"],
        capture_output=True,
        text=True
    )
    
    # Should show help and exit with 0
    assert result.returncode == 0
    assert "Process HTML files with MkDocs Output as Input plugin logic" in result.stdout


def test_cli_version_flag():
    """Test --version flag."""
    result = subprocess.run(
        [sys.executable, "-m", "mkdocs_output_as_input.cli", "--version"],
        capture_output=True,
        text=True
    )
    
    # Should show version and exit with 0
    assert result.returncode == 0
    assert "mkdocs-output-as-input" in result.stdout
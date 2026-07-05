# this_file: tests/test_integration.py
"""End-to-end integration test: run a real MkDocs build on a tiny fixture site.

Unlike the unit tests, which drive the plugin hooks directly with mocks, this
test exercises the full MkDocs pipeline (config loading -> build -> post-build)
so regressions in how the plugin registers or fires against a real MkDocs
version are caught.
"""

from pathlib import Path

import pytest
from mkdocs.commands.build import build
from mkdocs.config import load_config


@pytest.fixture
def fixture_site(tmp_path: Path) -> Path:
    """Create a minimal MkDocs site that enables the output-as-input plugin."""
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()

    index_md = """\
---
title: Home
tags:
  - intro
---

# Hello

This is the body paragraph.
"""
    (docs_dir / "index.md").write_text(index_md, encoding="utf-8")

    # The default MkDocs theme wraps page content in <div role="main">, so target
    # it with a CSS selector rather than relying on the "main" tag default.
    site_dir = tmp_path / "site"
    mkdocs_yml = f"""\
site_name: Fixture Site
docs_dir: {docs_dir}
site_dir: {site_dir}
plugins:
  - output-as-input:
      html_element: 'div[role="main"]'
"""
    (tmp_path / "mkdocs.yml").write_text(mkdocs_yml, encoding="utf-8")
    return tmp_path


def test_full_build_creates_cousin_file(fixture_site: Path) -> None:
    """A real build should produce a cousin Markdown file in the stage dir."""
    config = load_config(str(fixture_site / "mkdocs.yml"))
    build(config)

    # The plugin writes cousins to `<docs_dir>.parent / stage_dir` (default "stage").
    cousin = fixture_site / "stage" / "index.md"
    assert cousin.exists(), "cousin Markdown file was not created"

    content = cousin.read_text(encoding="utf-8")

    # Original frontmatter is preserved at the top of the cousin file.
    assert content.startswith("---\n")
    assert "title: Home" in content
    assert "intro" in content

    # Extracted, rendered HTML (not the raw Markdown) follows the frontmatter.
    assert "<article>" in content or "<article " in content
    assert "This is the body paragraph." in content
    assert "# Hello" not in content  # Markdown heading was rendered to HTML


def test_full_build_site_html_still_produced(fixture_site: Path) -> None:
    """The plugin must not interfere with normal site output."""
    config = load_config(str(fixture_site / "mkdocs.yml"))
    build(config)

    assert (fixture_site / "site" / "index.html").exists()

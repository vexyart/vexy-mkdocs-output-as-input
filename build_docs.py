#!/usr/bin/env python3
"""
Documentation builder for vexy-mkdocs-output-as-input repository.

This script demonstrates the plugin's workflow:
1. Source: README.md → MkDocs + plugin → stage/README.md (intermediate with frontmatter + HTML)
2. Final: stage/README.md → MkDocs → docs/ (proper MkDocs site)
"""

import os
import shutil
import subprocess
import tempfile
from pathlib import Path
import yaml


def run_command(cmd, cwd=None):
    """Run a command and print output."""
    print(f"\n🚀 Running: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(f"⚠️  {result.stderr}")
    if result.returncode != 0:
        raise Exception(f"Command failed: {cmd}")
    return result


def create_stage_mkdocs_config(temp_dir):
    """Create mkdocs.yml for stage 1 (source → intermediate)."""
    config = """site_name: MkDocs Output as Input Plugin - Stage 1
site_url: https://vexyart.github.io/vexy-mkdocs-output-as-input/

# Build from docs directory
docs_dir: docs
site_dir: site

nav:
  - Home: README.md

# Minimal theme for processing
theme:
  name: material

# Plugins - this is where our plugin captures the output
plugins:
  - output-as-input:
      stage_dir: ../../stage  # Output to stage directory in project root
      html_element: article  # Extract article element from Material theme
      target_tag: div  # Convert to div in output
      include_frontmatter: true  # Include frontmatter for metadata
      verbose: false
"""
    config_path = temp_dir / "mkdocs.yml"
    config_path.write_text(config)
    return config_path


def create_final_mkdocs_config():
    """Create mkdocs.yml for final build (intermediate → final site)."""
    config = """site_name: MkDocs Output as Input Plugin
site_url: https://vexyart.github.io/vexy-mkdocs-output-as-input/
site_description: A plugin that captures HTML output and creates cousin Markdown files

# Build from stage directory (contains processed markdown with HTML)
docs_dir: stage
site_dir: docs

nav:
  - Home: README.md

# Full Material theme for final output
theme:
  name: material
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
  features:
    - navigation.instant
    - navigation.tracking
    - content.code.copy

# Markdown extensions
markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.superfences
  - pymdownx.snippets
  - admonition
  - pymdownx.details
  - toc:
      permalink: true

# Only search plugin for final build (no output-as-input)
plugins:
  - search
"""
    config_path = Path("mkdocs-final.yml")
    config_path.write_text(config)
    return config_path


def step1_create_intermediate():
    """Step 1: Build README.md → stage/README.md with plugin."""
    print("\n" + "=" * 60)
    print("STEP 1: Creating intermediate form with output-as-input plugin")
    print("Source: README.md → Intermediate: stage/README.md")
    print("=" * 60)
    
    # Create a temporary directory for the build
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # Create docs directory and copy README.md to it
        docs_path = temp_path / "docs"
        docs_path.mkdir()
        shutil.copy2("README.md", docs_path / "README.md")
        
        # Create mkdocs config for stage 1
        create_stage_mkdocs_config(temp_path)
        
        # Build with MkDocs + our plugin
        run_command("mkdocs build", cwd=temp_path)
        
        # The plugin should have created files in the stage directory
        stage_dir = Path("stage")
        if stage_dir.exists():
            print("\n📁 Intermediate file created:")
            stage_file = stage_dir / "README.md"
            if stage_file.exists():
                print(f"  ✅ {stage_file}")
                
                # Show preview of frontmatter
                content = stage_file.read_text()
                if content.startswith("---"):
                    lines = content.split('\n')
                    print("\n  📋 Frontmatter preview:")
                    for i, line in enumerate(lines[:15]):
                        print(f"      {line}")
                        if i > 0 and line == "---":
                            print("      ...")
                            break
        else:
            print("  ❌ No stage directory found!")
            raise Exception("Stage directory not created")


def step2_build_final_docs():
    """Step 2: Build stage/README.md → docs/ with standard MkDocs."""
    print("\n" + "=" * 60)
    print("STEP 2: Building final documentation with MkDocs")
    print("Intermediate: stage/README.md → Final: docs/")
    print("=" * 60)
    
    # Clean docs directory
    docs_dir = Path("docs")
    if docs_dir.exists():
        shutil.rmtree(docs_dir)
    
    # Create final mkdocs config
    config_path = create_final_mkdocs_config()
    
    try:
        # Build with standard MkDocs (no output-as-input plugin)
        run_command("mkdocs build -f mkdocs-final.yml")
        
        print("\n✅ Final documentation built in docs/")
        
        # List generated files
        if docs_dir.exists():
            print("\n📁 Generated files:")
            for file in sorted(docs_dir.rglob("*")):
                if file.is_file():
                    print(f"  - {file.relative_to(docs_dir)}")
    finally:
        # Clean up temporary config
        if config_path.exists():
            config_path.unlink()


def main():
    """Run the documentation build pipeline."""
    print("🎯 Building Documentation for vexy-mkdocs-output-as-input")
    print("=" * 60)
    print("This demonstrates the plugin's two-stage workflow:")
    print("1. Source → Intermediate (with plugin capturing HTML)")
    print("2. Intermediate → Final (standard MkDocs build)")
    
    try:
        # Step 1: Create intermediate form with plugin
        step1_create_intermediate()
        
        # Step 2: Build final docs from intermediate
        step2_build_final_docs()
        
        print("\n" + "=" * 60)
        print("✅ Documentation build completed successfully!")
        print("\n📍 Pipeline summary:")
        print("  1. Source:       ./README.md (original markdown)")
        print("  2. Intermediate: ./stage/README.md (frontmatter + HTML)")
        print("  3. Final:        ./docs/index.html (full MkDocs site)")
        print("\nThe intermediate form in stage/ shows what the plugin produces.")
        print("The final docs/ contains a proper MkDocs Material site.")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Build failed: {e}")
        raise


if __name__ == "__main__":
    main()
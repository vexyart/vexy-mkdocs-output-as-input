#!/usr/bin/env python3
"""
Real example pipeline showing how to use the MkDocs output-as-input plugin.

This script demonstrates:
1. Building with MkDocs + output-as-input plugin to create intermediate files
2. Post-processing the staged files 
3. Creating final documentation in a different format
"""

import os
import shutil
import subprocess
from pathlib import Path
import yaml
from bs4 import BeautifulSoup


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


def step1_build_with_mkdocs():
    """Step 1: Build documentation with MkDocs and output-as-input plugin."""
    print("\n" + "=" * 60)
    print("STEP 1: Building with MkDocs + output-as-input plugin")
    print("=" * 60)
    
    # Clean previous builds
    for dir in ["src_docs/site", "stage"]:
        if Path(dir).exists():
            shutil.rmtree(dir)
    
    # Build with MkDocs
    run_command("mkdocs build", cwd="src_docs")
    
    # Show what was created in stage directory
    print("\n📁 Files created in stage directory:")
    stage_dir = Path("stage")
    if stage_dir.exists():
        for file in stage_dir.rglob("*.md"):
            print(f"  - {file}")
            
            # Show a preview of the content
            content = file.read_text()[:500]
            print(f"    Preview: {content.replace(chr(10), ' ')[:100]}...")
    else:
        print("  ❌ No stage directory found!")


def step2_process_staged_files():
    """Step 2: Process the staged files to add custom transformations."""
    print("\n" + "=" * 60)
    print("STEP 2: Processing staged files")
    print("=" * 60)
    
    stage_dir = Path("stage")
    if not stage_dir.exists():
        print("❌ No stage directory found!")
        return
    
    for md_file in stage_dir.rglob("*.md"):
        print(f"\n📝 Processing: {md_file}")
        
        content = md_file.read_text()
        
        # Split frontmatter and body
        if content.startswith("---\n"):
            parts = content.split("---\n", 2)
            if len(parts) >= 3:
                frontmatter_text = parts[1]
                body = parts[2]
                
                # Parse frontmatter
                frontmatter = yaml.safe_load(frontmatter_text) or {}
                
                # Add custom metadata
                frontmatter['processed'] = True
                frontmatter['pipeline_version'] = '1.0'
                frontmatter['source'] = 'mkdocs-output-as-input'
                
                # Parse HTML body
                soup = BeautifulSoup(body, 'html.parser')
                
                # Example transformation: Add a custom class to all headings
                for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
                    heading['class'] = heading.get('class', []) + ['custom-heading']
                
                # Example: Extract all code blocks for special processing
                code_blocks = soup.find_all('pre')
                if code_blocks:
                    frontmatter['has_code'] = True
                    frontmatter['code_count'] = len(code_blocks)
                
                # Write back the processed file
                new_content = "---\n"
                new_content += yaml.safe_dump(frontmatter, default_flow_style=False)
                new_content += "---\n\n"
                new_content += str(soup)
                
                md_file.write_text(new_content)
                print(f"  ✅ Added custom metadata and transformations")


def step3_generate_final_docs():
    """Step 3: Generate final documentation from processed files."""
    print("\n" + "=" * 60)
    print("STEP 3: Generating final documentation")
    print("=" * 60)
    
    # Create final docs directory
    final_dir = Path("docs_final")
    if final_dir.exists():
        shutil.rmtree(final_dir)
    final_dir.mkdir()
    
    # Create an index file that combines all processed content
    index_content = """# Processed Documentation

This documentation was processed through the MkDocs output-as-input pipeline.

## Pipeline Steps

1. **Source**: Original Markdown files (README.md)
2. **MkDocs Build**: Rendered to HTML with Material theme
3. **Output-as-Input Plugin**: Extracted article content and preserved frontmatter
4. **Post-Processing**: Added custom metadata and transformations
5. **Final Output**: Combined into this final documentation

## Processed Files

"""
    
    stage_dir = Path("stage")
    for md_file in sorted(stage_dir.rglob("*.md")):
        print(f"\n📄 Including: {md_file}")
        
        content = md_file.read_text()
        
        # Parse frontmatter to get metadata
        if content.startswith("---\n"):
            parts = content.split("---\n", 2)
            if len(parts) >= 3:
                frontmatter = yaml.safe_load(parts[1]) or {}
                body = parts[2]
                
                # Add to index
                index_content += f"\n### {md_file.name}\n\n"
                index_content += f"- **Processed**: {frontmatter.get('processed', False)}\n"
                index_content += f"- **Has Code**: {frontmatter.get('has_code', False)}\n"
                if frontmatter.get('code_count'):
                    index_content += f"- **Code Blocks**: {frontmatter['code_count']}\n"
                index_content += "\n"
                
                # Copy the processed file to final directory
                final_file = final_dir / md_file.name
                shutil.copy2(md_file, final_file)
                print(f"  ✅ Copied to final directory")
    
    # Write the index file
    index_file = final_dir / "index.md"
    index_file.write_text(index_content)
    print(f"\n✅ Created index file: {index_file}")
    
    # Show final structure
    print("\n📁 Final documentation structure:")
    for file in sorted(final_dir.rglob("*")):
        if file.is_file():
            print(f"  - {file}")


def main():
    """Run the complete pipeline."""
    print("🎯 MkDocs Output-as-Input Pipeline Example")
    print("=" * 60)
    
    try:
        # Step 1: Build with MkDocs
        step1_build_with_mkdocs()
        
        # Step 2: Process staged files
        step2_process_staged_files()
        
        # Step 3: Generate final documentation
        step3_generate_final_docs()
        
        print("\n" + "=" * 60)
        print("✅ Pipeline completed successfully!")
        print("\n📍 Results:")
        print("  - Intermediate files: ./stage/")
        print("  - Final documentation: ./docs_final/")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Pipeline failed: {e}")
        raise


if __name__ == "__main__":
    main()

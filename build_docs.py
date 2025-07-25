#!/usr/bin/env python3
# this_file: build_docs.py
"""Build documentation from src_docs to docs directory."""

import subprocess
import sys
from pathlib import Path
import shutil
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def clean_docs_dir():
    """Clean the docs directory except for .gitkeep and specific files."""
    docs_dir = Path("docs")
    if docs_dir.exists():
        # Preserve specific files
        preserve = {".gitkeep", "README.md", "404.html"}
        
        # Remove all files and directories except preserved ones
        for item in docs_dir.iterdir():
            if item.name not in preserve:
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()
        logger.info("Cleaned docs directory")

def install_dependencies():
    """Check and install required MkDocs plugins."""
    required_plugins = [
        "mkdocs",
        "mkdocs-material",
        "mkdocstrings[python]",
        "mkdocs-git-revision-date-localized-plugin",
        "mkdocs-minify-plugin",
    ]
    
    logger.info("Checking dependencies...")
    
    # Check if plugins are installed
    missing = []
    for plugin in required_plugins:
        try:
            if plugin == "mkdocs":
                subprocess.run(["mkdocs", "--version"], check=True, capture_output=True)
            else:
                # Try to import the plugin
                plugin_name = plugin.split("[")[0].replace("-", "_")
                if plugin_name == "mkdocs_material":
                    __import__("material")
                elif plugin_name == "mkdocstrings":
                    __import__("mkdocstrings")
                else:
                    __import__(plugin_name)
        except (subprocess.CalledProcessError, ImportError, FileNotFoundError):
            missing.append(plugin)
    
    if missing:
        logger.warning(f"Missing dependencies: {', '.join(missing)}")
        logger.info("Installing missing dependencies...")
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install"] + missing,
                check=True
            )
            logger.info("Dependencies installed successfully")
        except subprocess.CalledProcessError:
            logger.error("Failed to install dependencies")
            return False
    
    return True

def build_docs():
    """Build documentation using MkDocs."""
    logger.info("Building documentation with MkDocs...")
    
    # Build the documentation
    try:
        # First, let's build without strict mode to see what happens
        result = subprocess.run(
            ["mkdocs", "build", "--clean"],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            logger.error(f"MkDocs build failed:\n{result.stderr}")
            # Try to build with verbose mode for debugging
            logger.info("Retrying with verbose mode...")
            result = subprocess.run(
                ["mkdocs", "build", "--clean", "-v"],
                text=True
            )
            return False
            
        logger.info("MkDocs build completed successfully")
        return True
        
    except Exception as e:
        logger.error(f"Error during build: {e}")
        return False

def create_missing_files():
    """Create any missing required files."""
    # Create abbreviations file if it doesn't exist
    includes_dir = Path("src_docs/includes")
    includes_dir.mkdir(exist_ok=True)
    
    abbr_file = includes_dir / "abbreviations.md"
    if not abbr_file.exists():
        abbr_file.write_text("""
*[HTML]: HyperText Markup Language
*[SSG]: Static Site Generator
*[API]: Application Programming Interface
*[CLI]: Command Line Interface
*[YAML]: YAML Ain't Markup Language
*[CSS]: Cascading Style Sheets
*[PR]: Pull Request
*[CI]: Continuous Integration
*[CD]: Continuous Deployment
""")
        logger.info("Created abbreviations file")
    
    # Create overrides directory
    overrides_dir = Path("src_docs/overrides")
    overrides_dir.mkdir(exist_ok=True)
    
    # Create placeholder logo and favicon if they don't exist
    for img in ["logo.png", "favicon.png"]:
        img_path = Path("src_docs/assets") / img
        if not img_path.exists():
            # Create a simple 1x1 transparent PNG as placeholder
            img_path.parent.mkdir(exist_ok=True, parents=True)
            img_path.write_bytes(
                b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01'
                b'\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\rIDATx\x9cc\xf8\x0f'
                b'\x00\x00\x01\x01\x00\x00\x05\x00\x01\x0d\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82'
            )
            logger.info(f"Created placeholder {img}")

def verify_build():
    """Verify the build output."""
    docs_dir = Path("docs")
    required_files = ["index.html", "sitemap.xml"]
    
    missing = []
    for file in required_files:
        if not (docs_dir / file).exists():
            missing.append(file)
    
    if missing:
        logger.warning(f"Missing expected files: {', '.join(missing)}")
        return False
    
    # Count HTML files
    html_files = list(docs_dir.rglob("*.html"))
    logger.info(f"Generated {len(html_files)} HTML files")
    
    # Check if stage directory was created
    stage_dir = Path("stage")
    if stage_dir.exists():
        stage_files = list(stage_dir.rglob("*.md"))
        logger.info(f"Plugin created {len(stage_files)} cousin files in stage/")
    
    return True

def main():
    """Main build process."""
    logger.info("Starting documentation build process...")
    
    # Create missing files
    create_missing_files()
    
    # Check dependencies
    if not install_dependencies():
        logger.error("Failed to install dependencies")
        sys.exit(1)
    
    # Clean existing docs
    clean_docs_dir()
    
    # Build documentation
    if not build_docs():
        logger.error("Build failed!")
        logger.info("Tip: Check that all referenced files exist in src_docs/")
        logger.info("Tip: Run 'mkdocs serve' to see detailed errors")
        sys.exit(1)
    
    # Verify build
    if not verify_build():
        logger.warning("Build verification found issues")
    
    logger.info("\n✅ Documentation build completed successfully!")
    logger.info("\n📚 View documentation:")
    logger.info("  - Locally: mkdocs serve")
    logger.info("  - Static: open docs/index.html")
    logger.info("\n🔌 Plugin output:")
    logger.info("  - Cousin files: stage/*.md")

if __name__ == "__main__":
    main()
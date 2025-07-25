# this_file: src/mkdocs_output_as_input/plugin.py
"""MkDocs plugin that captures HTML output and creates cousin Markdown files."""

import re
import time
from pathlib import Path
from typing import Any

import yaml
from bs4 import BeautifulSoup
from loguru import logger
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page

# Type aliases for better readability
type FrontmatterDict = dict[str, Any]
type ConfigDict = dict[str, Any]
type FileInfo = dict[str, Any]


class OutputAsInputPlugin(BasePlugin):  # type: ignore[type-arg,no-untyped-call]
    """MkDocs plugin that captures HTML output and creates cousin Markdown files.

    This plugin:
    1. Lets the entire MkDocs build process run normally
    2. Tracks all source Markdown files and their YAML frontmatter
    3. After the build, creates a "stage" directory that replicates the source structure
    4. For each source Markdown file, creates a cousin file with original frontmatter
       and extracted HTML
    """

    config_scheme = (
        ("stage_dir", config_options.Type(str, default="stage")),
        ("html_element", config_options.Type((str, list), default="main")),
        ("target_tag", config_options.Type(str, default="article")),
        ("include_frontmatter", config_options.Type(bool, default=True)),
        ("preserve_links", config_options.Type(bool, default=False)),
        ("minify", config_options.Type(bool, default=False)),
        ("prettify", config_options.Type(bool, default=False)),
        ("verbose", config_options.Type(bool, default=False)),
    )

    def __init__(self) -> None:
        """Initialize the plugin."""
        super().__init__()
        self.source_files: dict[str, FileInfo] = {}
        self.site_dir: Path | None = None
        self.docs_dir: Path | None = None

    def on_config(self, config: ConfigDict) -> ConfigDict:  # type: ignore[override]
        """Store site and docs directories and validate configuration.
        
        Args:
            config: MkDocs configuration dictionary
            
        Returns:
            The unmodified configuration dictionary
            
        Raises:
            ValueError: If mutually exclusive options are enabled
        """
        self.site_dir = Path(config["site_dir"])
        self.docs_dir = Path(config["docs_dir"])

        # Validate mutually exclusive options
        if self.config["minify"] and self.config["prettify"]:
            raise ValueError("Cannot use both 'minify' and 'prettify' options")

        if self.config["verbose"]:
            logger.info("Plugin initialized", site_dir=self.site_dir, docs_dir=self.docs_dir)
            logger.debug("Configuration", config=self.config)

        return config

    def on_page_read_source(self, page: Page, config: ConfigDict) -> str | None:  # type: ignore[override]  # noqa: ARG002
        """Capture source Markdown content and frontmatter.
        
        Args:
            page: MkDocs page object
            config: MkDocs configuration dictionary
            
        Returns:
            None to let MkDocs continue with original content
        """
        src_path = page.file.src_path
        start_time = time.time()

        # Read the full source content
        try:
            with open(page.file.abs_src_path, encoding="utf-8") as f:  # type: ignore[arg-type]
                content = f.read()
        except Exception as e:
            logger.error("Failed to read source file", path=src_path, error=str(e))
            return None

        # Extract frontmatter if present
        frontmatter: FrontmatterDict = {}
        if content.startswith("---\n"):
            try:
                end_idx = content.find("\n---\n", 4)
                if end_idx > 0:
                    fm_text = content[4:end_idx]
                    frontmatter = yaml.safe_load(fm_text) or {}
            except yaml.YAMLError as e:
                logger.warning("Failed to parse frontmatter", path=src_path, error=str(e))

        self.source_files[src_path] = {
            "frontmatter": frontmatter,
            "abs_src_path": page.file.abs_src_path,
        }

        if self.config["verbose"]:
            elapsed = time.time() - start_time
            logger.debug(
                "Captured source file",
                path=src_path,
                frontmatter_keys=list(frontmatter.keys()),
                elapsed_ms=f"{elapsed * 1000:.2f}"
            )

        return None  # Let MkDocs continue with original content

    def on_post_build(self, config: ConfigDict) -> None:  # type: ignore[override]  # noqa: ARG002
        """After build, process all HTML files and create cousin Markdowns.
        
        Args:
            config: MkDocs configuration dictionary
        """
        if self.docs_dir is None:
            logger.error("docs_dir not set, cannot process files")
            return
        
        start_time = time.time()
        stage_dir = self.docs_dir.parent / self.config["stage_dir"]

        # Create stage directory
        stage_dir.mkdir(exist_ok=True)
        logger.info("Creating stage directory", path=stage_dir)

        # Process each tracked source file
        processed = 0
        failed = 0
        
        with logger.contextualize(stage_dir=str(stage_dir)):
            for src_path, file_info in self.source_files.items():
                try:
                    self._process_file(src_path, file_info, stage_dir)
                    processed += 1
                except Exception as e:
                    failed += 1
                    logger.error(
                        "Failed to process file",
                        path=src_path,
                        error=str(e),
                        exc_info=self.config["verbose"]
                    )

        elapsed = time.time() - start_time
        logger.info(
            "Post-build processing complete",
            processed=processed,
            failed=failed,
            total=len(self.source_files),
            elapsed_s=f"{elapsed:.2f}"
        )

    def _process_file(self, src_path: str, file_info: FileInfo, stage_dir: Path) -> None:
        """Process a single file: extract HTML and create cousin Markdown.
        
        Args:
            src_path: Path to the source Markdown file
            file_info: Dictionary containing file metadata and frontmatter
            stage_dir: Directory where cousin files will be created
        """
        if self.site_dir is None:
            logger.error("site_dir not set")
            return

        # Determine HTML output path
        # Special case: README.md often becomes index.html at root
        if src_path.lower() == "readme.md":
            html_path = "index.html"
            full_html_path = self.site_dir / html_path
        else:
            html_path = src_path.replace(".md", "/index.html")
            full_html_path = self.site_dir / html_path

        if not full_html_path.exists():
            # Try without the index.html suffix
            html_path = src_path.replace(".md", ".html")
            full_html_path = self.site_dir / html_path

        if not full_html_path.exists():
            logger.warning(
                "No HTML output found",
                source=src_path,
                expected_path=str(full_html_path)
            )
            return

        # Read and parse HTML
        try:
            with open(full_html_path, encoding="utf-8") as f:
                html_content = f.read()
        except Exception as e:
            logger.error("Failed to read HTML file", path=full_html_path, error=str(e))
            return

        soup = BeautifulSoup(html_content, "html.parser")

        # Extract target element(s)
        html_elements = self.config["html_element"]
        if isinstance(html_elements, str):
            html_elements = [html_elements]

        extracted_elements: list[Any] = []
        for selector in html_elements:
            # Try CSS selector first
            elements = soup.select(selector)
            if elements:
                extracted_elements.extend(elements)
            else:
                # Fall back to tag name
                element = soup.find(selector)
                if element:
                    extracted_elements.append(element)

        if not extracted_elements:
            logger.warning(
                "No matching elements found",
                selectors=self.config['html_element'],
                html_file=str(full_html_path)
            )
            return

        # If multiple elements, wrap them in a container
        if len(extracted_elements) > 1:
            container = soup.new_tag(self.config["target_tag"])
            for elem in extracted_elements:
                container.append(elem.extract())
            target_element = container
        else:
            target_element = extracted_elements[0]  # type: ignore[assignment]
            # Transform to target tag if different and single selector was a tag name
            if (isinstance(self.config["html_element"], str) and 
                self.config["target_tag"] != self.config["html_element"]):
                target_element.name = self.config["target_tag"]

        # Handle link preservation if requested
        if self.config["preserve_links"]:
            # Convert absolute links back to relative
            for link in target_element.find_all(["a", "img", "link", "script"]):
                for attr in ["href", "src"]:
                    if link.has_attr(attr):
                        url = link[attr]
                        # Simple heuristic: if it starts with /, it's likely a root-relative link
                        # In a real implementation, this would be more sophisticated
                        if url.startswith("/") and not url.startswith("//"):
                            link[attr] = f".{url}"

        # Create cousin file path
        cousin_path = stage_dir / src_path
        cousin_path.parent.mkdir(parents=True, exist_ok=True)

        # Write cousin file
        try:
            with open(cousin_path, "w", encoding="utf-8") as f:
                # Write frontmatter if present and configured to include it
                if self.config["include_frontmatter"] and file_info["frontmatter"]:
                    f.write("---\n")
                    f.write(yaml.safe_dump(file_info["frontmatter"], default_flow_style=False))
                    f.write("---\n\n")

                # Write extracted HTML with formatting options
                if self.config["minify"]:
                    # Remove extra whitespace between tags
                    html_output = str(target_element)
                    # Remove newlines and compress multiple spaces
                    html_output = html_output.replace("\n", "")
                    html_output = re.sub(r'\s+', ' ', html_output)
                    # Remove spaces between tags
                    html_output = re.sub(r'>\s+<', '><', html_output)
                elif self.config["prettify"]:
                    html_output = target_element.prettify()
                else:
                    html_output = str(target_element)

                f.write(html_output)
                f.write("\n")

            if self.config["verbose"]:
                logger.debug("Created cousin file", path=cousin_path, size=cousin_path.stat().st_size)

        except Exception as e:
            logger.error("Failed to write cousin file", path=cousin_path, error=str(e))

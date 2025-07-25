# this_file: src/mkdocs_output_as_input/cli.py
"""CLI tool for standalone processing of HTML files with output-as-input plugin."""

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml
from bs4 import BeautifulSoup
from loguru import logger

# Type aliases
type FrontmatterDict = dict[str, Any]
type ElementList = str | list[str]


def setup_logging(verbose: bool = False) -> None:
    """Set up logging configuration.
    
    Args:
        verbose: Enable verbose logging with debug level
    """
    # Remove default logger and add custom format
    logger.remove()
    
    level = "DEBUG" if verbose else "INFO"
    format_string = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
        "<level>{message}</level>"
    ) if verbose else (
        "<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>"
    )
    
    logger.add(sys.stderr, format=format_string, level=level)


def extract_frontmatter(content: str) -> tuple[FrontmatterDict, str]:
    """Extract YAML frontmatter from Markdown content.
    
    Args:
        content: The markdown content
        
    Returns:
        Tuple of (frontmatter dict, content without frontmatter)
    """
    frontmatter: FrontmatterDict = {}
    body = content

    if content.startswith("---\n"):
        try:
            end_idx = content.find("\n---\n", 4)
            if end_idx > 0:
                fm_text = content[4:end_idx]
                frontmatter = yaml.safe_load(fm_text) or {}
                body = content[end_idx + 5:]  # Skip past the closing ---\n
        except yaml.YAMLError as e:
            logger.warning("Failed to parse frontmatter", error=str(e))

    return frontmatter, body


def process_html(
    html_content: str,
    html_element: ElementList = "main",
    target_tag: str = "article",
    preserve_links: bool = False,
    minify: bool = False,
    prettify: bool = False,
) -> str | None:
    """Process HTML content and extract specified element.
    
    Args:
        html_content: The HTML content to process
        html_element: CSS selector for element to extract
        target_tag: Tag to replace the extracted element with
        preserve_links: Whether to preserve relative links
        minify: Whether to minify the output
        prettify: Whether to prettify the output
        
    Returns:
        Processed HTML string or None if element not found
    """
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract target element(s)
    html_elements = html_element if isinstance(html_element, list) else [html_element]

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
        logger.error("No elements found", selectors=html_element)
        return None

    # If multiple elements, wrap them in a container
    if len(extracted_elements) > 1:
        container = soup.new_tag(target_tag)
        for elem in extracted_elements:
            container.append(elem.extract())
        target_element = container
    else:
        target_element = extracted_elements[0]  # type: ignore[assignment]
        # Transform to target tag if different
        # For single selector, check if it's not a CSS selector
        if target_tag != target_element.name:
            # Only transform if original selector was a simple tag name
            if isinstance(html_element, str):
                # Simple tag name check
                if html_element == target_element.name:
                    target_element.name = target_tag
            elif len(html_element) == 1 and html_element[0] == target_element.name:
                target_element.name = target_tag

    # Handle link preservation if requested
    if preserve_links:
        # Convert absolute links back to relative
        for link in target_element.find_all(["a", "img", "link", "script"]):
            for attr in ["href", "src"]:
                if link.has_attr(attr):
                    url = link[attr]
                    # Simple heuristic: if it starts with /, it's likely a root-relative link
                    # In a real implementation, this would be more sophisticated
                    if url.startswith("/") and not url.startswith("//"):
                        link[attr] = f".{url}"

    # Format output
    if minify:
        # Remove extra whitespace between tags
        result = str(target_element).replace("\n", "").replace("  ", " ")
    elif prettify:
        result = target_element.prettify()
    else:
        result = str(target_element)

    return result


def process_file(
    input_path: Path,
    output_path: Path,
    html_element: ElementList = "main",
    target_tag: str = "article",
    include_frontmatter: bool = True,
    preserve_links: bool = False,
    minify: bool = False,
    prettify: bool = False,
) -> None:
    """Process a single file.
    
    Args:
        input_path: Path to input HTML file
        output_path: Path to output Markdown file
        html_element: CSS selector for element to extract
        target_tag: Tag to replace the extracted element with
        include_frontmatter: Whether to include frontmatter in output
        preserve_links: Whether to preserve relative links
        minify: Whether to minify the output
        prettify: Whether to prettify the output
    """
    logger.info("Processing file", input=str(input_path), output=str(output_path))

    # Read input file
    try:
        content = input_path.read_text(encoding="utf-8")
    except Exception as e:
        logger.error("Failed to read input file", path=input_path, error=str(e))
        raise

    # Check if there's a corresponding markdown file for frontmatter
    frontmatter: FrontmatterDict = {}
    if include_frontmatter:
        md_path = input_path.with_suffix(".md")
        if md_path.exists():
            try:
                md_content = md_path.read_text(encoding="utf-8")
                frontmatter, _ = extract_frontmatter(md_content)
                logger.debug("Extracted frontmatter", path=md_path, keys=list(frontmatter.keys()))
            except Exception as e:
                logger.warning("Failed to read markdown file", path=md_path, error=str(e))

    # Process HTML
    processed_html = process_html(
        content,
        html_element=html_element,
        target_tag=target_tag,
        preserve_links=preserve_links,
        minify=minify,
        prettify=prettify,
    )

    if processed_html is None:
        raise ValueError(f"Failed to process HTML from {input_path}")

    # Create output directory if needed
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write output
    try:
        with output_path.open("w", encoding="utf-8") as f:
            # Write frontmatter if present and configured
            if include_frontmatter and frontmatter:
                f.write("---\n")
                f.write(yaml.safe_dump(frontmatter, default_flow_style=False))
                f.write("---\n\n")

            # Write processed HTML
            f.write(processed_html)
            f.write("\n")

        logger.info("Successfully wrote output file", path=output_path, size=output_path.stat().st_size)
    except Exception as e:
        logger.error("Failed to write output file", path=output_path, error=str(e))
        raise


def main() -> int:
    """Main CLI entry point."""
    from mkdocs_output_as_input import __version__
    
    parser = argparse.ArgumentParser(
        description="Process HTML files with MkDocs Output as Input plugin logic",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process a single file
  mkdocs-output-as-input process input.html output.md
  
  # Process with custom element and tag
  mkdocs-output-as-input process input.html output.md --html-element div --target-tag section
  
  # Process without frontmatter
  mkdocs-output-as-input process input.html output.md --no-frontmatter
  
  # Process with link preservation and prettify
  mkdocs-output-as-input process input.html output.md --preserve-links --prettify
        """,
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version=f"mkdocs-output-as-input {__version__}",
        help="Show version information and exit",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Process command
    process_parser = subparsers.add_parser("process", help="Process HTML file(s)")
    process_parser.add_argument("input", type=Path, help="Input HTML file")
    process_parser.add_argument("output", type=Path, help="Output Markdown file")
    process_parser.add_argument(
        "--html-element",
        action="append",
        help="HTML element(s) to extract (can be specified multiple times, default: main)",
    )
    process_parser.add_argument(
        "--target-tag",
        default="article",
        help="Target tag for output (default: article)",
    )
    process_parser.add_argument(
        "--no-frontmatter",
        action="store_false",
        dest="include_frontmatter",
        help="Exclude frontmatter from output",
    )
    process_parser.add_argument(
        "--preserve-links",
        action="store_true",
        help="Preserve relative links in HTML",
    )
    process_parser.add_argument(
        "--minify",
        action="store_true",
        help="Minify HTML output",
    )
    process_parser.add_argument(
        "--prettify",
        action="store_true",
        help="Prettify HTML output",
    )
    process_parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    # Set up logging
    setup_logging(args.verbose)

    try:
        if args.command == "process":
            # Validate mutually exclusive options
            if args.minify and args.prettify:
                logger.error("Cannot use both --minify and --prettify")
                return 1

            # Default to "main" if no elements specified
            html_element = args.html_element if args.html_element else "main"

            process_file(
                args.input,
                args.output,
                html_element=html_element,
                target_tag=args.target_tag,
                include_frontmatter=args.include_frontmatter,
                preserve_links=args.preserve_links,
                minify=args.minify,
                prettify=args.prettify,
            )
            return 0
    except Exception as e:
        logger.error("Command failed", error=str(e))
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

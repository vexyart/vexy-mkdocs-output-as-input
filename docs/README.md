# Documentation

This directory contains the generated documentation for the vexy-mkdocs-output-as-input plugin.

View the documentation at: https://vexyart.github.io/vexy-mkdocs-output-as-input/

## Build Process

The documentation is built using the plugin itself:

1. **Source**: `README.md` (root of repository)
2. **Intermediate**: `stage/README.md` (preserved in git)
3. **Final**: `docs/index.html` (this directory)

To rebuild the documentation, run: `python build_docs.py`

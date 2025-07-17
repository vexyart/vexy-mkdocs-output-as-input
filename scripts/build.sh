#!/bin/bash
# this_file: scripts/build.sh

set -e

echo "Building vexy-mkdocs-output-as-input..."

# Clean up any existing build artifacts
rm -rf build/ dist/ *.egg-info/

# Ensure we're in the project root
cd "$(dirname "$0")/.."

# Build the package
echo "Building package..."
uv build

echo "Build completed successfully!"
echo "Distribution files:"
ls -la dist/
#!/bin/bash
# this_file: scripts/dev-setup.sh

set -e

echo "Setting up development environment for vexy-mkdocs-output-as-input..."

# Ensure we're in the project root
cd "$(dirname "$0")/.."

# Install uv if not present
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source ~/.cargo/env
fi

# Create virtual environment
echo "Creating virtual environment..."
uv venv --python 3.12

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Install development dependencies
echo "Installing development dependencies..."
uv pip install -e ".[dev,test,docs]"

# Install pre-commit hooks
echo "Installing pre-commit hooks..."
uv run pre-commit install

echo "Development environment setup completed!"
echo "To activate the virtual environment, run: source .venv/bin/activate"
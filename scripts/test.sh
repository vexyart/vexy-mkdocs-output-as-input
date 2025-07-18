#!/bin/bash
# this_file: scripts/test.sh

set -e

echo "Running tests for vexy-mkdocs-output-as-input..."

# Ensure we're in the project root
cd "$(dirname "$0")/.."

# Install development dependencies
echo "Installing development dependencies..."
uv pip install -e ".[dev,test]"

# Run code quality checks
echo "Running code quality checks..."
echo "- Running ruff check..."
uv run ruff check src tests

echo "- Running ruff format check..."
uv run ruff format --check src tests

echo "- Running mypy..."
uv run mypy src

# Run tests with coverage
echo "Running tests with coverage..."
uv run pytest --cov=mkdocs_output_as_input --cov-report=term-missing --cov-report=html

echo "All tests passed!"
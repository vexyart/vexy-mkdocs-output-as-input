# this_file: Makefile

.PHONY: help install test build clean release docs dev-setup

help:
	@echo "Available commands:"
	@echo "  install     - Install the package in development mode"
	@echo "  test        - Run tests and code quality checks"
	@echo "  build       - Build the package"
	@echo "  clean       - Clean build artifacts"
	@echo "  release     - Create a new release (patch by default)"
	@echo "  docs        - Build and serve documentation"
	@echo "  dev-setup   - Set up development environment"

dev-setup:
	@echo "Setting up development environment..."
	./scripts/dev-setup.sh

install:
	@echo "Installing package in development mode..."
	uv pip install -e ".[dev,test,docs]"

test:
	@echo "Running tests and code quality checks..."
	./scripts/test.sh

build:
	@echo "Building package..."
	./scripts/build.sh

clean:
	@echo "Cleaning build artifacts..."
	rm -rf build/ dist/ *.egg-info/
	rm -rf .pytest_cache/ .coverage htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

release:
	@echo "Creating new release..."
	./scripts/release.sh patch

release-minor:
	@echo "Creating minor release..."
	./scripts/release.sh minor

release-major:
	@echo "Creating major release..."
	./scripts/release.sh major

docs:
	@echo "Building and serving documentation..."
	mkdocs serve
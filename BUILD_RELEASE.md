# Build and Release Guide

This guide explains how to build and release the `vexy-mkdocs-output-as-input` package using the automated workflows.

## Prerequisites

- Python 3.9+
- [uv](https://astral.sh/uv) package manager
- Git repository with proper permissions

## Local Development Setup

### 1. Initial Setup

```bash
# Clone the repository
git clone https://github.com/vexyart/vexy-mkdocs-output-as-input.git
cd vexy-mkdocs-output-as-input

# Run the development setup script
./scripts/dev-setup.sh
```

This script will:
- Install `uv` if not present
- Create a virtual environment
- Install all development dependencies
- Set up pre-commit hooks

### 2. Running Tests

```bash
# Run the full test suite
./scripts/test.sh
```

This will run:
- Code quality checks (ruff, mypy)
- Test suite with coverage reporting
- Pre-commit hooks

### 3. Building the Package

```bash
# Build the package locally
./scripts/build.sh
```

This creates distributable files in the `dist/` directory.

## Release Process

### Git Tag-Based Semversioning

The project uses git tags for versioning with [hatch-vcs](https://github.com/ofek/hatch-vcs). Version numbers are automatically generated from git tags.

### 1. Automated Release Script

```bash
# Create a patch release (e.g., v1.2.3 -> v1.2.4)
./scripts/release.sh patch

# Create a minor release (e.g., v1.2.3 -> v1.3.0)
./scripts/release.sh minor

# Create a major release (e.g., v1.2.3 -> v2.0.0)
./scripts/release.sh major
```

The release script will:
1. Check for uncommitted changes
2. Verify you're on the correct branch
3. Calculate the next version number
4. Run the full test suite
5. Prompt you to update the changelog
6. Create and push the git tag
7. Trigger automated CI/CD workflows

### 2. Manual Release Steps

If you prefer to release manually:

```bash
# 1. Ensure all changes are committed
git status

# 2. Update CHANGELOG.md with new version information
# Add new section for the release under ## [Unreleased]

# 3. Create and push the tag
git tag -a v1.2.3 -m "Release v1.2.3"
git push origin v1.2.3
```

## Automated CI/CD Workflows

### CI Workflow (`.github/workflows/ci.yml`)

Triggers on:
- Push to `main` branch
- Pull requests to `main` branch

**Multiplatform Testing:**
- **Operating Systems:** Ubuntu, Windows, macOS
- **Python Versions:** 3.9, 3.10, 3.11, 3.12

**Steps:**
1. Install dependencies with `uv`
2. Run code quality checks (ruff, mypy, pre-commit)
3. Run test suite with coverage
4. Build package and verify integrity
5. Upload build artifacts

### Release Workflow (`.github/workflows/release.yml`)

Triggers on:
- Git tag push matching pattern `v*`

**Multiplatform Binary Building:**
- Creates standalone executables for Linux, Windows, and macOS
- Uses PyInstaller to bundle the CLI tool

**Steps:**
1. **Build Wheels:** Test and build Python wheels for all supported platforms
2. **Build Binaries:** Create standalone executables using PyInstaller
3. **Combine Artifacts:** Merge all build artifacts
4. **PyPI Publishing:** Automatically publish to PyPI using trusted publishing
5. **GitHub Release:** Create GitHub release with changelog and artifacts

## Distribution Artifacts

### Python Packages
- **Wheel (`.whl`):** Binary distribution for pip installation
- **Source Distribution (`.tar.gz`):** Source code archive

### Standalone Binaries
- **Linux:** `mkdocs-output-as-input-ubuntu-latest`
- **Windows:** `mkdocs-output-as-input-windows-latest.exe`
- **macOS:** `mkdocs-output-as-input-macos-latest`

## Installation Methods

### 1. From PyPI (Recommended)

```bash
# Install latest version
pip install vexy-mkdocs-output-as-input

# Install specific version
pip install vexy-mkdocs-output-as-input==1.2.3
```

### 2. From GitHub Release

```bash
# Download and install wheel
pip install https://github.com/vexyart/vexy-mkdocs-output-as-input/releases/download/v1.2.3/vexy_mkdocs_output_as_input-1.2.3-py3-none-any.whl
```

### 3. Standalone Binary

Download the appropriate binary for your platform from the [GitHub Releases](https://github.com/vexyart/vexy-mkdocs-output-as-input/releases) page.

```bash
# Linux/macOS
chmod +x mkdocs-output-as-input-ubuntu-latest
./mkdocs-output-as-input-ubuntu-latest --help

# Windows
mkdocs-output-as-input-windows-latest.exe --help
```

## Changelog Management

Follow [Keep a Changelog](https://keepachangelog.com/) format in `CHANGELOG.md`:

```markdown
## [Unreleased]

### Added
- New feature descriptions

### Changed
- Modified feature descriptions

### Fixed
- Bug fix descriptions

## [1.2.3] - 2024-01-15

### Added
- Initial release
```

## Version Management

The project uses semantic versioning (SemVer):
- **MAJOR:** Incompatible API changes
- **MINOR:** Backwards-compatible functionality additions
- **PATCH:** Backwards-compatible bug fixes

Version numbers are automatically generated from git tags by `hatch-vcs`.

## Troubleshooting

### Release Failures

1. **Tag already exists:**
   ```bash
   git tag -d v1.2.3
   git push origin :refs/tags/v1.2.3
   ```

2. **Tests failing:**
   ```bash
   ./scripts/test.sh
   # Fix any issues and retry
   ```

3. **Build issues:**
   ```bash
   rm -rf dist/ build/ *.egg-info/
   ./scripts/build.sh
   ```

### CI/CD Issues

1. **PyPI publishing fails:** Check that trusted publishing is configured in PyPI
2. **Binary creation fails:** Ensure PyInstaller dependencies are properly installed
3. **Artifact upload fails:** Check GitHub Actions permissions and storage limits

## Security Considerations

- **Trusted Publishing:** PyPI publishing uses GitHub's OIDC for secure, keyless authentication
- **Dependency Scanning:** All dependencies are scanned for known vulnerabilities
- **Code Quality:** Automated linting and type checking enforce code quality standards

## Support

For issues with the build or release process, please:
1. Check the GitHub Actions logs
2. Review this documentation
3. Open an issue with detailed error information
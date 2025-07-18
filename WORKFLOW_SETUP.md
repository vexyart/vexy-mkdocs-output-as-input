# GitHub Actions Workflow Setup

Since GitHub Apps don't have permission to modify workflow files, you'll need to manually create the GitHub Actions workflows. Here are the complete workflow files to add to your repository.

## Required Setup

1. Create the `.github/workflows/` directory if it doesn't exist
2. Add the workflow files below
3. Configure PyPI trusted publishing (optional but recommended)

## 1. CI Workflow

Create `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ["3.9", "3.10", "3.11", "3.12"]

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Required for hatch-vcs

      - name: Install uv
        uses: astral-sh/setup-uv@v3
        with:
          version: "latest"

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: |
          uv pip install --system -e ".[dev,test]"

      - name: Run code quality checks
        if: matrix.os == 'ubuntu-latest' && matrix.python-version == '3.12'
        run: |
          uv run --system ruff check src tests
          uv run --system ruff format --check src tests
          uv run --system mypy src

      - name: Run pre-commit
        if: matrix.os == 'ubuntu-latest' && matrix.python-version == '3.12'
        run: uv run --system pre-commit run --all-files

      - name: Run tests
        run: |
          uv run --system pytest -v --cov=mkdocs_output_as_input --cov-report=xml --cov-report=term

      - name: Upload coverage
        if: matrix.os == 'ubuntu-latest' && matrix.python-version == '3.12'
        uses: codecov/codecov-action@v4
        with:
          file: ./coverage.xml
          fail_ci_if_error: true
          token: ${{ secrets.CODECOV_TOKEN }}

  build:
    runs-on: ubuntu-latest
    needs: test
    
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Required for hatch-vcs

      - name: Install uv
        uses: astral-sh/setup-uv@v3
        with:
          version: "latest"

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Build package
        run: |
          uv build

      - name: Check package
        run: |
          uv run --system twine check dist/*

      - name: Upload build artifacts
        uses: actions/upload-artifact@v4
        with:
          name: dist
          path: dist/
```

## 2. Release Workflow

Create `.github/workflows/release.yml`:

```yaml
name: Release

on:
  push:
    tags:
      - 'v*'

permissions:
  contents: write
  id-token: write  # Required for PyPI trusted publishing

jobs:
  build-wheel:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ["3.9", "3.10", "3.11", "3.12"]
    
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Required for hatch-vcs

      - name: Install uv
        uses: astral-sh/setup-uv@v3
        with:
          version: "latest"

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: |
          uv pip install --system -e ".[dev,test]"

      - name: Run tests
        run: |
          uv run --system pytest -v

      - name: Build package
        run: |
          uv build

      - name: Check package
        run: |
          uv run --system twine check dist/*

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: dist-${{ matrix.os }}-py${{ matrix.python-version }}
          path: dist/

  build-binaries:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
    
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Required for hatch-vcs

      - name: Install uv
        uses: astral-sh/setup-uv@v3
        with:
          version: "latest"

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          uv pip install --system -e ".[dev,test]"
          uv pip install --system pyinstaller

      - name: Create binary (Linux/macOS)
        if: matrix.os != 'windows-latest'
        run: |
          uv run --system pyinstaller --onefile --name mkdocs-output-as-input-${{ matrix.os }} src/mkdocs_output_as_input/cli.py

      - name: Create binary (Windows)
        if: matrix.os == 'windows-latest'
        run: |
          uv run --system pyinstaller --onefile --name mkdocs-output-as-input-${{ matrix.os }}.exe src/mkdocs_output_as_input/cli.py

      - name: Upload binary artifacts
        uses: actions/upload-artifact@v4
        with:
          name: binaries-${{ matrix.os }}
          path: dist/

  combine-artifacts:
    needs: [build-wheel, build-binaries]
    runs-on: ubuntu-latest
    steps:
      - name: Download all artifacts
        uses: actions/download-artifact@v4
        with:
          path: artifacts/

      - name: Combine artifacts
        run: |
          mkdir -p combined-dist
          # Copy wheels from one representative build (ubuntu-latest, py3.12)
          cp artifacts/dist-ubuntu-latest-py3.12/* combined-dist/
          # Copy binaries from all platforms
          find artifacts/binaries-* -type f -exec cp {} combined-dist/ \;

      - name: Upload combined artifacts
        uses: actions/upload-artifact@v4
        with:
          name: combined-dist
          path: combined-dist/

  publish-pypi:
    needs: combine-artifacts
    runs-on: ubuntu-latest
    environment:
      name: pypi
      url: https://pypi.org/p/vexy-mkdocs-output-as-input
    steps:
      - name: Download combined artifacts
        uses: actions/download-artifact@v4
        with:
          name: combined-dist
          path: dist/

      - name: Publish to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1
        # Trusted publishing configured in PyPI project settings

  create-release:
    needs: combine-artifacts
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Download combined artifacts
        uses: actions/download-artifact@v4
        with:
          name: combined-dist
          path: dist/

      - name: Extract changelog section
        id: changelog
        run: |
          version=${GITHUB_REF#refs/tags/v}
          awk "/## \[$version\]/{flag=1; next} /## \[/{flag=0} flag" CHANGELOG.md > release_notes.md
          echo "version=$version" >> $GITHUB_OUTPUT

      - name: Create Release
        uses: softprops/action-gh-release@v1
        with:
          name: v${{ steps.changelog.outputs.version }}
          body_path: release_notes.md
          files: dist/*
          draft: false
          prerelease: false
```

## 3. PyPI Trusted Publishing Setup (Optional)

To enable automatic PyPI publishing without API keys:

1. Go to your PyPI project settings
2. Navigate to "Publishing" → "Trusted publishing"
3. Add a new publisher with these settings:
   - Repository: `vexyart/vexy-mkdocs-output-as-input`
   - Environment: `pypi`
   - Workflow: `release.yml`

## 4. Repository Secrets (If not using trusted publishing)

Add these secrets to your GitHub repository:

- `PYPI_TOKEN`: Your PyPI API token
- `CODECOV_TOKEN`: Your Codecov token (optional, for coverage reporting)

## 5. Testing the Workflow

Once you've added the workflows:

1. Push a commit to trigger the CI workflow
2. Create a git tag to trigger the release workflow:
   ```bash
   git tag -a v0.3.0 -m "Release v0.3.0"
   git push origin v0.3.0
   ```

## Notes

- The workflows are designed to work with the `uv` package manager
- Binaries are created for Linux, Windows, and macOS
- The release workflow only publishes to PyPI on tagged releases
- All tests must pass before a release is created
- Build artifacts are available for download from the GitHub Actions runs
# Contributing

Bug reports and pull requests are welcome at [github.com/vexyart/vexy-mkdocs-output-as-input](https://github.com/vexyart/vexy-mkdocs-output-as-input). For larger changes, open an issue first to discuss the approach.

## Repository layout

| Path | Contents |
|------|----------|
| `src/mkdocs_output_as_input/plugin.py` | The MkDocs plugin, `OutputAsInputPlugin` |
| `src/mkdocs_output_as_input/cli.py` | The `mkdocs-output-as-input` command |
| `src/mkdocs_output_as_input/__init__.py` | Exports `OutputAsInputPlugin` and `__version__` |
| `tests/` | `pytest` test suite, including an end-to-end MkDocs build in `test_integration.py` |
| `src_docs/md/` | Source of this documentation site |
| `src_docs/mkdocs.yml` | Documentation site configuration |
| `docs/` | Built documentation site, served by GitHub Pages; do not edit by hand |
| `scripts/` | Helper scripts for setup, tests and builds |

## Set up a development environment

Prerequisites: Python 3.12 or newer and [`uv`](https://docs.astral.sh/uv/).

1. Clone the repository:

    ```bash
    git clone https://github.com/vexyart/vexy-mkdocs-output-as-input
    cd vexy-mkdocs-output-as-input
    ```

2. Create a virtual environment and install the package with its development extras:

    ```bash
    uv venv --python 3.12
    uv pip install -e ".[dev]"
    ```

3. Install the pre-commit hooks:

    ```bash
    uv run pre-commit install
    ```

`scripts/dev-setup.sh` performs the same steps.

## Run the tests and checks

Run the test suite:

```bash
uv run pytest
```

`scripts/test.sh` runs the full set of checks in this order: `ruff check`, `ruff format --check`, `mypy src`, and `pytest` with coverage. The coverage configuration in `pyproject.toml` sets `fail_under = 90`.

The pre-commit configuration also runs `pyupgrade`, `black`, `codespell` and the standard whitespace, YAML and TOML checks.

The GitHub Actions workflow `ci.yml` runs the tests on Ubuntu and Windows with Python 3.12 and 3.13, a MkDocs compatibility job, and a lint job with `ruff`, `black` and `mypy`.

## Build the package and the documentation

The root `build.sh` builds both:

```bash
./build.sh            # documentation and package
./build.sh docs       # documentation only
./build.sh package    # package only
```

- The documentation is built by `src_docs/build.sh` with ProperDocs and the MaterialX theme, in strict mode, from `src_docs/md/` into `docs/`. `src_docs/build.sh serve` starts a live preview at `http://127.0.0.1:8000`.
- The package is built with `uv build` into `dist/` and checked with `twine check`.

The version number comes from the latest Git tag through `hatch-vcs`. At build time it is written to `src/mkdocs_output_as_input/_version.py`, which is not committed. A checkout without that file reports the version `0.0.0+unknown`.

After a push to `main` that changes `src_docs/`, the `docs.yml` workflow rebuilds `docs/` and commits the result.

## Releases

`publish.sh` makes a release:

1. `gitnextver` commits pending changes, creates the next `vX.Y.Z` tag and pushes it.
2. `./build.sh package` builds the package from that tag.
3. `uv publish` uploads `dist/*` to PyPI. This needs `UV_PUBLISH_TOKEN` or another `uv publish` credential.

Pushing a `v*` tag also starts the `release.yml` workflow, which builds the package, uploads it to PyPI through trusted publishing (skipping files that already exist), and creates a GitHub release.

## Documentation style

Write documentation pages in `src_docs/md/`. Describe only behaviour that the code has, use sentence-case headings, and put commands, paths and option names in code style. Run `./build.sh docs` before you open a pull request; the build must pass in strict mode.

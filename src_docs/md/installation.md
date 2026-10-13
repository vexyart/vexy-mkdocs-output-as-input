# Installation

## Requirements

- Python 3.12 or newer. The package declares `requires-python = ">=3.12"` and uses Python 3.12 syntax.
- MkDocs 1.6.0 or newer.

Installing the package also installs its runtime dependencies:

| Package | Minimum version | Used for |
|---------|-----------------|----------|
| `mkdocs` | 1.6.0 | Plugin base class and configuration options |
| `beautifulsoup4` | 4.12.0 | Parsing the rendered HTML and selecting elements |
| `pyyaml` | 6.0 | Reading and writing YAML front matter |
| `loguru` | 0.7.0 | Log messages from the plugin and the CLI |

## Install from PyPI

Install the package into the same environment that runs MkDocs.

With `uv`:

```bash
uv pip install vexy-mkdocs-output-as-input
```

With `pip`:

```bash
pip install vexy-mkdocs-output-as-input
```

If you run MkDocs through `uvx`, add the package with `--with`:

```bash
uvx --from mkdocs --with vexy-mkdocs-output-as-input mkdocs build
```

## Install from source

```bash
git clone https://github.com/vexyart/vexy-mkdocs-output-as-input
cd vexy-mkdocs-output-as-input
uv pip install -e .
```

## Check the installation

1. Print the version of the command-line tool:

    ```bash
    mkdocs-output-as-input --version
    ```

    The output has the form `mkdocs-output-as-input <version>`.

2. Confirm that MkDocs can find the plugin. The package registers the plugin under the name `output-as-input` in the `mkdocs.plugins` entry-point group. If MkDocs cannot find it, `mkdocs build` stops with an error that names the missing plugin.

## Names at a glance

| What | Name |
|------|------|
| PyPI package | `vexy-mkdocs-output-as-input` |
| Plugin name in `mkdocs.yml` | `output-as-input` |
| Python import package | `mkdocs_output_as_input` |
| Plugin class | `mkdocs_output_as_input.plugin.OutputAsInputPlugin` |
| Command-line tool | `mkdocs-output-as-input` |

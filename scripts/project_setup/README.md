# Project Setup

This script is a self-sufficient, non-interactive tool that automates the setup process for every project in this monorepo.

## What it Does

When run, the script will automatically:

1.  Check if `uv` is installed and, if not, install it.
2.  Install a `uv`-managed version of Python.
3.  Scan the `apps/`, `scripts/`, and `playground/` directories for valid projects.
4.  For each project found, it will:
    -   Create a Python virtual environment (`.venv/`) using `uv venv`.
    -   Install all dependencies from `pyproject.toml` using `uv pip install -e .`.
    -   Run `ruff format .`, `ruff check --fix`, and `mypy .` to ensure code quality and type correctness.

## How to Use

From the root of the repository, run the script using your system's Python. This is the **only time you should use the `python` command directly** for setup. This script will install `uv` and a managed version of Python, which you will use for all subsequent commands.

```bash
python scripts/project_setup/setup.py
```

To re-run the setup script after the initial setup, or to update all project dependencies and run quality checks, use `uv run`:

```bash
uv run scripts/project_setup/setup.py
```

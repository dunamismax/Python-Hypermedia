# Project Setup

This script is a self-sufficient, non-interactive tool that automates the setup process for every project in this monorepo.

## What it Does

When run, the script will automatically:

1.  Check if `uv` is installed and, if not, install it.
2.  Check if `Node.js` and `npm` are installed. If not, it will attempt to install them (using Homebrew on macOS or providing instructions for Linux).
3.  Install a `uv`-managed version of Python.
4.  Scan the `apps/` and `scripts/` directories for valid projects.
5.  For each project found, it will:
    -   Create a Python virtual environment (`.venv/`) using `uv venv`.
    -   Install all dependencies from `pyproject.toml` using `uv pip sync`.
    -   Install all Node.js dependencies from `package.json` (if present).
    -   Run `uv run ruff format .` and `uv run ruff check --fix` to ensure code quality.

## How to Use

From the root of the repository, run the script using your system's Python. This is the only command needed to get the entire monorepo ready for development.

```bash
python scripts/project_setup/setup.py
```

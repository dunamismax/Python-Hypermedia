# Project Setup

This script is a self-sufficient, non-interactive tool that automates the setup process for every project in this monorepo.

## What it Does

When run, the script will automatically:

1. Check if `uv` is installed and, if not, install it.
2. Install a `uv`-managed version of Python.
3. Scan the `apps/` and `scripts/` directories for valid projects.
4. For each project found, it will:
   - Create a Python virtual environment (`.venv/`) using `uv venv`.
   - Install all dependencies from `pyproject.toml` using `uv pip sync`.
   - Install all Node.js dependencies from `package.json` (if present).
   - Run `uv run ruff format .` and `uv run ruff check --fix` to ensure code quality.

## How to Use

From the root of the repository, run the script using Python.

```bash
python scripts/project_setup/setup.py
```

The script is designed to be run on a fresh clone of the repository with no prior setup required.

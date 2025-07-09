# Project Setup

This script is a non-interactive tool that automates the setup process for every project (both applications and scripts) in this monorepo.

## What it Does

When run, the script will automatically:

1. Scan the `apps/` and `scripts/` directories for valid projects.
2. For each project found, it will:
   - Create a Python virtual environment (`.venv/`).
   - Install all dependencies from `pyproject.toml` using `uv pip sync`.
   - Install all Node.js dependencies from `package.json` (if present).
   - Run `ruff format` and `ruff check --fix` to ensure code quality.

## How to Use

Simply navigate to this directory and run the script with Python.

1. **Navigate to this directory:**

   ```bash
   cd scripts/project_setup
   ```

2. **Run the script:**

   ```bash
   python setup.py
   ```

The script has no external dependencies and will proceed to set up all projects in the repository automatically.

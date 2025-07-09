# Project Cleanup

This script recursively scans the entire monorepo from the project root and **immediately deletes** common temporary files and directories.

**Note:** This script runs non-interactively and does not ask for confirmation.

## What it Deletes

The script will search for and remove all occurrences of the following:

- `.ruff_cache/`
- `.__pycache__/`
- `.venv/`
- `build/`
- `node_modules/`
- `package-lock.json`
- `*.egg-info/`
- `static/`

## How to Use

From the root of the repository, run the script using `uv run`.

```bash
uv run --no-project scripts/project_cleanup/cleanup.py
```

The script has no external dependencies and will immediately begin cleaning the repository.

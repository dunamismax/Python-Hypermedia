# Project Cleanup

This script recursively scans the entire monorepo from the project root and **immediately deletes** common temporary files and directories.

**Note:** This script runs non-interactively and does not ask for confirmation.

## What it Deletes

The script will search for and remove all occurrences of the following:

- `.ruff_cache/`
- `.venv/`
- `build/`
- `node_modules/`
- `package-lock.json`
- `*.egg-info/`
- `static/`

## How to Use

Simply navigate to this directory and run the script with Python.

1. **Navigate to this directory:**

   ```bash
   cd scripts/project_cleanup
   ```

2. **Run the script:**

   ```bash
   python cleanup.py
   ```

The script has no external dependencies and will immediately begin cleaning the repository.

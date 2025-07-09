# App Cleaner

This script recursively scans the entire monorepo from the project root and deletes common temporary files and directories.

## What it Deletes

The script will search for and remove all occurrences of the following:
- `.ruff_cache/`
- `.venv/`
- `build/`
- `node_modules/`
- `package-lock.json`
- `*.egg-info/`

## How to Use

1.  **Navigate to this directory:**
    ```bash
    cd scripts/app_cleaner
    ```

2.  **Set up the script's environment (only needs to be done once):**
    ```bash
    # Create the virtual environment
    uv venv

    # Activate the environment
    source .venv/bin/activate

    # Install dependencies
    uv pip sync pyproject.toml
    ```

3.  **Run the script:**
    ```bash
    python clean.py
    ```
    The script will show you a list of all items it found to delete and ask for confirmation before proceeding.

4.  **Force Deletion (Optional):**
    To skip the confirmation prompt, you can use the `--force` or `-f` flag:
    ```bash
    python clean.py --force
    ```

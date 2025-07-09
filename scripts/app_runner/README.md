# App Runner

This script provides a command-line interface to manage and run the applications within the monorepo.

## How to Use

1.  **Navigate to this directory:**
    ```bash
    cd scripts/app_runner
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
    python run.py
    ```

The script will guide you through the available options.

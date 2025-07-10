## Project Cleanup

This script provides a safe and idempotent way to clean the monorepo by removing all common temporary files and build artifacts. It can be run at any time without risk.

It is the recommended first step in the standard workflow for keeping your environment in sync.

## How to Use

From the root of the repository, run the script using `uv run`:

```bash
uv run scripts/project_cleanup/cleanup.py
```

The script has no external dependencies and will immediately begin cleaning the repository.
# Monorepo Scripts

This directory contains various utility scripts for the repository. These can range from project management and automation tools to general-purpose scripts for development and testing.

## Available Scripts

- **[`project_setup/`](./project_setup/)**: A self-sufficient script to set up the entire repository. It automatically installs `uv`, a managed version of Python, and all project dependencies.
- **[`project_cleanup/`](./project_cleanup/)**: A script to clean temporary files and directories (`.venv`, `node_modules`, `__pycache__`, etc.) from the entire repository.

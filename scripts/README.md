# Monorepo Scripts

This directory contains various utility scripts for the repository. These can range from project management and automation tools to general-purpose scripts for development and testing.

## Available Scripts

- **[`project_setup/`](./project_setup/)**: A comprehensive, idempotent script to set up the entire repository. It can be run repeatedly to ensure the environment is always in sync.
- **[`project_cleanup/`](./project_cleanup/)**: A script to safely clean temporary files and directories from the entire repository. It is recommended to run this before the setup script.

"""
This script provides a safe and idempotent way to clean the monorepo.

It recursively scans the entire project from the root and removes common temporary
files and build artifacts. It can be run at any time without risk.
"""

import shutil
from pathlib import Path

import typer

app = typer.Typer()

# Directories and files to be deleted across the monorepo.
TARGETS_TO_DELETE = [
    ".ruff_cache",
    "__pycache__",
    ".venv",
    "build",
    "*.egg-info",
    "uv.lock",
    ".mypy_cache",
]


@app.command()
def main() -> None:
    """
    Finds and deletes temporary project files and directories automatically.
    """
    project_root = Path(__file__).parent.parent.parent

    typer.secho(f"🔍 Searching for items to delete in {project_root}...", fg=typer.colors.CYAN)

    items_to_delete = []
    for pattern in TARGETS_TO_DELETE:
        items_to_delete.extend(project_root.rglob(pattern))

    if not items_to_delete:
        typer.secho(
            "✅ No items to clean up. Project is already clean!",
            fg=typer.colors.GREEN,
            bold=True,
        )
        raise typer.Exit()

    typer.secho("\n🚀 Starting cleanup...", bold=True)

    for item in items_to_delete:
        try:
            if not item.exists():
                continue

            if item.is_dir():
                shutil.rmtree(item)
                typer.secho(
                    f"🗑️  Deleted directory: {item.relative_to(project_root)}",
                    fg=typer.colors.YELLOW,
                )
            else:
                item.unlink()
                typer.secho(
                    f"🗑️  Deleted file: {item.relative_to(project_root)}", fg=typer.colors.YELLOW
                )
        except OSError as e:
            typer.secho(f"Error deleting {item}: {e}", fg=typer.colors.RED)

    typer.secho("\n✅ Cleanup complete!", fg=typer.colors.GREEN, bold=True)


if __name__ == "__main__":
    app()
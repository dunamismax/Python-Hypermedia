"""
This script provides a safe and idempotent way to clean the monorepo.

It recursively scans the entire project from the root and removes common temporary
files and build artifacts. It can be run at any time without risk.
"""

import shutil
import sys
from pathlib import Path

def _print_color(text: str, color_code: str) -> None:
    """Prints text with ANSI color codes."""
    print(f"\u001b[{color_code}m{text}\u001b[0m")

def _print_green(text: str) -> None:
    _print_color(text, "32") # Green

def _print_yellow(text: str) -> None:
    _print_color(text, "33") # Yellow

def _print_red(text: str) -> None:
    _print_color(text, "31") # Red

def _print_cyan(text: str) -> None:
    _print_color(text, "36") # Cyan

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

def main() -> None:
    """
    Finds and deletes temporary project files and directories automatically.
    """
    project_root = Path(__file__).parent.parent.parent

    _print_cyan(f"🔍 Searching for items to delete in {project_root}...")

    items_to_delete = []
    for pattern in TARGETS_TO_DELETE:
        items_to_delete.extend(project_root.rglob(pattern))

    if not items_to_delete:
        _print_green("✅ No items to clean up. Project is already clean!")
        sys.exit()

    _print_yellow("\n🚀 Starting cleanup...")

    for item in items_to_delete:
        try:
            if not item.exists():
                continue

            if item.is_dir():
                shutil.rmtree(item)
                _print_yellow(f"🗑️  Deleted directory: {item.relative_to(project_root)}")
            else:
                item.unlink()
                _print_yellow(f"🗑️  Deleted file: {item.relative_to(project_root)}")
        except OSError as e:
            _print_red(f"Error deleting {item}: {e}")

    _print_green("\n✅ Cleanup complete!")


if __name__ == "__main__":
    main()

"""
This script provides a safe and idempotent way to clean the monorepo.

It recursively scans the entire project from the root and removes common temporary
files and build artifacts. It can be run at any time without risk and is the
recommended first step before running the main setup script to ensure a clean
environment.

Note: This script runs non-interactively and does not ask for confirmation.
"""

import shutil
import sys
from pathlib import Path
from typing import Optional


# --- ANSI Color Codes ---
class Colors:
    """A class for storing ANSI color codes for printing formatted output."""

    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    END = "\033[0m"


def cprint(text: str, color: Optional[str] = None, bold: bool = False) -> None:
    """Prints text with specified color and boldness."""
    style = Colors.BOLD if bold else ""
    color_code = getattr(Colors, color.upper(), "") if color else ""
    print(f"{style}{color_code}{text}{Colors.END}")


# --- Constants ---

# Directories and files to be deleted across the monorepo.
TARGETS_TO_DELETE = [
    ".ruff_cache",
    "__pycache__",
    ".venv",
    "build",
    "node_modules",
    "package-lock.json",
    "*.egg-info",
    "uv.lock",
    "static/**/main.css",
    ".mypy_cache",
]


# --- Core Logic ---


def get_project_root() -> Path:
    """Finds the project root by looking for the .git directory."""
    current_path = Path.cwd().resolve()
    while not (current_path / ".git").exists():
        if current_path.parent == current_path:
            raise FileNotFoundError(
                "Could not find project root. Make sure you are inside the repository."
            )
        current_path = current_path.parent
    return current_path


def find_items_to_delete(root: Path) -> list[Path]:
    """Finds all top-level files and directories matching the target patterns."""
    found_items: set[Path] = set()
    for pattern in TARGETS_TO_DELETE:
        # Use rglob to find all potential matches.
        matches = list(root.rglob(pattern))
        # Filter out nested matches. For example, if we match `a/b/node_modules`
        # and `a/node_modules`, we only want to keep `a/node_modules`.
        top_level_matches = set()
        for match in sorted(matches, key=lambda p: len(p.parts)):
            # If a parent of the current match is already in our set, skip it.
            if any(parent in top_level_matches for parent in match.parents):
                continue
            top_level_matches.add(match)
        found_items.update(top_level_matches)
    # Sort the final list for consistent output.
    return sorted(found_items, key=lambda p: p.as_posix())


def main() -> None:
    """
    Finds and deletes temporary project files and directories automatically.
    """
    try:
        project_root = get_project_root()
    except FileNotFoundError as e:
        cprint(f"Error: {e}", color="red")
        sys.exit(1)

    cprint(f"🔍 Searching for items to delete in {project_root}...", color="cyan")

    items_to_delete = find_items_to_delete(project_root)

    if not items_to_delete:
        cprint(
            "✅ No items to clean up. Project is already clean!",
            color="green",
            bold=True,
        )
        sys.exit(0)

    cprint("\n🚀 Starting cleanup...", bold=True)

    for item in items_to_delete:
        try:
            if not item.exists():
                # This can happen if a parent directory was already deleted.
                continue

            if item.is_dir():
                shutil.rmtree(item)
                cprint(
                    f"🗑️  Deleted directory: {item.relative_to(project_root)}",
                    color="yellow",
                )
            else:
                item.unlink()
                cprint(f"🗑️  Deleted file: {item.relative_to(project_root)}", color="yellow")
        except OSError as e:
            cprint(f"Error deleting {item}: {e}", color="red")

    cprint("\n✅ Cleanup complete!", color="green", bold=True)


if __name__ == "__main__":
    main()

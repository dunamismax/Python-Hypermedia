import shutil
import sys
from pathlib import Path
from typing import List


# --- ANSI Color Codes ---
class Colors:
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    END = "\033[0m"


def cprint(text, color=None, bold=False):
    """Prints text with specified color and boldness."""
    style = Colors.BOLD if bold else ""
    color_code = getattr(Colors, color.upper(), "") if color else ""
    print(f"{style}{color_code}{text}{Colors.END}")


TARGETS_TO_DELETE = [
    ".ruff_cache",
    "__pycache__",
    ".venv",
    "build",
    "node_modules",
    "package-lock.json",
    "*.egg-info",
    "static/**/main.css",
]


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


def find_items_to_delete(root: Path) -> List[Path]:
    """Finds all files and directories matching the target names."""
    found_items = []
    for target in TARGETS_TO_DELETE:
        found_items.extend(root.rglob(target))
    return found_items


def main():
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
            if item.is_dir():
                shutil.rmtree(item)
                cprint(
                    f"🗑️  Deleted directory: {item.relative_to(project_root)}",
                    color="yellow",
                )
            else:
                item.unlink()
                cprint(
                    f"🗑️  Deleted file: {item.relative_to(project_root)}", color="yellow"
                )
        except OSError as e:
            cprint(f"Error deleting {item}: {e}", color="red")

    cprint("\n✅ Cleanup complete!", color="green", bold=True)


if __name__ == "__main__":
    main()

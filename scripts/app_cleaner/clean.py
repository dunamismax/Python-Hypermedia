import shutil
from pathlib import Path
from typing import List

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    add_completion=False,
    help="A CLI tool to clean temporary files and directories from the monorepo.",
)

TARGETS_TO_DELETE = [
    ".ruff_cache",
    ".venv",
    "build",
    "node_modules",
    "package-lock.json",
    "*.egg-info",
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


@app.command()
def main(
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Force deletion without asking for confirmation.",
    ),
):
    """
    Finds and deletes temporary project files and directories.
    """
    console = Console()
    try:
        project_root = get_project_root()
    except FileNotFoundError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(1)

    console.print(f"🔍 Searching for items to delete in [cyan]{project_root}[/cyan]...")

    items_to_delete = find_items_to_delete(project_root)

    if not items_to_delete:
        console.print(
            "[bold green]✅ No items to clean up. Project is already clean![/bold green]"
        )
        raise typer.Exit()

    table = Table(title="Items to be Deleted", style="yellow")
    table.add_column("Type", style="magenta")
    table.add_column("Path", style="cyan")

    for item in items_to_delete:
        item_type = "Directory" if item.is_dir() else "File"
        table.add_row(item_type, str(item.relative_to(project_root)))

    console.print(table)

    if not force:
        confirmed = typer.confirm(
            "Are you sure you want to permanently delete these items?"
        )
        if not confirmed:
            console.print("[bold yellow]Aborted by user.[/bold yellow]")
            raise typer.Exit()

    console.print("\n[bold]🚀 Starting cleanup...[/bold]")

    for item in items_to_delete:
        try:
            if item.is_dir():
                shutil.rmtree(item)
                console.print(
                    f"🗑️  Deleted directory: [cyan]{item.relative_to(project_root)}[/cyan]"
                )
            else:
                item.unlink()
                console.print(
                    f"🗑️  Deleted file: [cyan]{item.relative_to(project_root)}[/cyan]"
                )
        except OSError as e:
            console.print(f"[bold red]Error deleting {item}: {e}[/bold red]")

    console.print("\n[bold green]✅ Cleanup complete![/bold green]")


if __name__ == "__main__":
    app()

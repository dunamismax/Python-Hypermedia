
"""
A comprehensive, idempotent setup script for the Python-Hypermedia monorepo.

This script is designed to be run at any time to ensure the development environment
is fully configured and up-to-date. It can be run repeatedly with no negative
side effects, as it will skip installations for tools that are already present.

Running this script is the standard way to onboard a new application or to sync the
environment after pulling changes or modifying dependencies.

The script will automatically:
1.  Check for and install `uv`, the project's Python package manager.
2.  Install a `uv`-managed version of the Python interpreter.
3.  Scan the `apps/`, `scripts/`, and `playground/` directories for valid projects.
4.  For each project found, it will:
    - Create a Python virtual environment (`.venv/`).
    - Install all Python dependencies, including optional `[dev]` dependencies.
    - Run Ruff to format and lint the code.
    - Run MyPy for static type checking.

Usage:
    python scripts/project_setup/setup.py
"""

import subprocess
import sys
from pathlib import Path

import typer

app = typer.Typer()


def is_command_installed(command: str) -> bool:
    """Checks if a command is installed and available in the system's PATH."""
    try:
        subprocess.run(
            [command, "--version"], check=True, capture_output=True, text=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def install_uv() -> None:
    """Installs uv using the official, non-interactive curl script."""
    typer.secho("uv not found. Installing...", fg=typer.colors.BLUE, bold=True)
    try:
        if not is_command_installed("curl"):
            typer.secho(
                "Error: `curl` is required to install uv, but it's not found.",
                fg=typer.colors.RED,
            )
            typer.secho("Please install `curl` and try again.", fg=typer.colors.YELLOW)
            raise typer.Exit(code=1)

        subprocess.run(
            "curl -LsSf https://astral.sh/uv/install.sh | sh",
            shell=True,
            check=True,
            stdout=sys.stdout,
            stderr=sys.stderr,
        )
        typer.secho("✅ uv installed successfully.", fg=typer.colors.GREEN)
        # Update PATH for the current process to include uv
        os.environ["PATH"] = f"{os.path.expanduser('~/.cargo/bin')}:{os.environ['PATH']}"
    except subprocess.CalledProcessError as e:
        typer.secho(f"❌ Failed to install uv: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)


def ensure_uv_managed_python_installed() -> None:
    """Ensures a uv-managed Python version is installed."""
    typer.secho("Ensuring uv-managed Python is installed...", fg=typer.colors.BLUE, bold=True)
    try:
        run_command(
            ["uv", "python", "install"], cwd=Path.cwd(), description="Install uv-managed Python"
        )
        typer.secho("✅ uv-managed Python installed successfully.", fg=typer.colors.GREEN)
    except typer.Exit:
        typer.secho("❌ Failed to install uv-managed Python.", fg=typer.colors.RED)
        raise


def run_command(command: list[str], cwd: Path, description: str) -> None:
    """Runs a command in a specified directory, handling errors and output."""
    typer.secho(f"🚀 Starting: {description} in {cwd.name}...", fg=typer.colors.YELLOW)
    try:
        process = subprocess.Popen(
            command, cwd=cwd, stdout=sys.stdout, stderr=sys.stderr, text=True
        )
        process.wait()
        if process.returncode == 0:
            typer.secho(f"✅ Success: {description}", fg=typer.colors.GREEN)
        else:
            typer.secho(
                f"❌ Error: {description} failed with exit code {process.returncode}",
                fg=typer.colors.RED,
            )
            raise typer.Exit(code=1)
    except FileNotFoundError:
        typer.secho(
            f"❌ Error: Command '{command[0]}' not found. Is it installed and in your PATH?",
            fg=typer.colors.RED,
        )
        raise typer.Exit(code=1)
    except Exception as e:
        typer.secho(f"❌ An unexpected error occurred: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)


def run_quality_checks(project_path: Path) -> None:
    """Runs Ruff formatter, linter, and MyPy type checker for a given project."""
    typer.secho(f"🔬 Running quality checks for: {project_path.name}", fg=typer.colors.BLUE, bold=True)

    run_command(
        ["uv", "run", "ruff", "format", "."], cwd=project_path, description="Run Ruff formatter"
    )
    run_command(
        ["uv", "run", "ruff", "check", ".", "--fix"],
        cwd=project_path,
        description="Run Ruff linter",
    )

    # Only run MyPy if there are Python files in the project to check.
    if list(project_path.rglob("*.py")):
        run_command(
            ["uv", "run", "mypy", "."], cwd=project_path, description="Run MyPy type checker"
        )
    else:
        typer.secho(f"⚪ Skipping MyPy: No Python files found in {project_path.name}", fg=typer.colors.YELLOW)


def get_project_directories(root: Path) -> list[Path]:
    """Scans directories and returns a list of valid project directories."""
    project_dirs = []
    for project_type in ["apps", "scripts", "playground"]:
        base_path = root / project_type
        if not base_path.is_dir():
            continue

        for d in base_path.iterdir():
            if d.is_dir() and (d / "pyproject.toml").exists():
                project_dirs.append(d)
    return sorted(project_dirs)


@app.command()
def main() -> None:
    """Main function to orchestrate the entire monorepo setup."""
    typer.secho("Starting repository setup...", fg=typer.colors.BLUE, bold=True)
    typer.secho("=" * 40, fg=typer.colors.BLUE)

    if not is_command_installed("uv"):
        install_uv()
    else:
        typer.secho("✅ uv is already installed.", fg=typer.colors.GREEN)

    ensure_uv_managed_python_installed()

    project_root = Path(__file__).parent.parent.parent

    all_projects = get_project_directories(project_root)

    if not all_projects:
        typer.secho("No applications or scripts found to set up.", fg=typer.colors.YELLOW)
        raise typer.Exit(code=0)

    typer.secho("\nSetting up all applications and scripts...", fg=typer.colors.BLUE, bold=True)
    for project_path in all_projects:
        run_command(
            ["uv", "venv"], cwd=project_path, description="Create Python virtual environment"
        )
        run_command(
            ["uv", "pip", "install", "-e", "."],
            cwd=project_path,
            description=f"Install dependencies for {project_path.name}",
        )
        run_quality_checks(project_path)

    typer.secho("\n" + "=" * 40, fg=typer.colors.GREEN, bold=True)
    typer.secho("🎉 All projects have been set up successfully!", fg=typer.colors.GREEN, bold=True)
    typer.secho("You are now ready to start development.", fg=typer.colors.YELLOW)


if __name__ == "__main__":
    import os
    app()

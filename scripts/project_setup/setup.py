
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
import os
from pathlib import Path


def _print_color(text: str, color_code: str) -> None:
    """Prints text with ANSI color codes."""
    print(f"\033[{color_code}m{text}\033[0m")

def _print_blue(text: str) -> None:
    _print_color(text, "34") # Blue

def _print_green(text: str) -> None:
    _print_color(text, "32") # Green

def _print_yellow(text: str) -> None:
    _print_color(text, "33") # Yellow

def _print_red(text: str) -> None:
    _print_color(text, "31") # Red


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
    _print_blue("uv not found. Installing...")
    try:
        if not is_command_installed("curl"):
            _print_red("Error: `curl` is required to install uv, but it's not found.")
            _print_yellow("Please install `curl` and try again.")
            sys.exit(1)

        subprocess.run(
            "curl -LsSf https://astral.sh/uv/install.sh | sh",
            shell=True,
            check=True,
            stdout=sys.stdout,
            stderr=sys.stderr,
        )
        _print_green("✅ uv installed successfully.")
        # Update PATH for the current process to include uv
        os.environ["PATH"] = f"{os.path.expanduser('~/.cargo/bin')}:{os.environ['PATH']}"
    except subprocess.CalledProcessError as e:
        _print_red(f"❌ Failed to install uv: {e}")
        sys.exit(1)


def ensure_uv_managed_python_installed() -> None:
    """Ensures a uv-managed Python version is installed."""
    _print_blue("Ensuring uv-managed Python is installed...")
    try:
        run_command(
            ["uv", "python", "install"], cwd=Path.cwd(), description="Install uv-managed Python"
        )
        _print_green("✅ uv-managed Python installed successfully.")
    except SystemExit: # Catch SystemExit from run_command
        _print_red("❌ Failed to install uv-managed Python.")
        raise


def run_command(command: list[str], cwd: Path, description: str) -> None:
    """Runs a command in a specified directory, handling errors and output."""
    _print_yellow(f"🚀 Starting: {description} in {cwd.name}...")
    try:
        process = subprocess.Popen(
            command, cwd=cwd, stdout=sys.stdout, stderr=sys.stderr, text=True
        )
        process.wait()
        if process.returncode == 0:
            _print_green(f"✅ Success: {description}")
        else:
            _print_red(
                f"❌ Error: {description} failed with exit code {process.returncode}"
            )
            sys.exit(1)
    except FileNotFoundError:
        _print_red(
            f"❌ Error: Command '{command[0]}' not found. Is it installed and in your PATH?"
        )
        sys.exit(1)
    except Exception as e:
        _print_red(f"❌ An unexpected error occurred: {e}")
        sys.exit(1)


def run_quality_checks(project_path: Path) -> None:
    """Runs Ruff formatter, linter, and MyPy type checker for a given project."""
    _print_blue(f"🔬 Running quality checks for: {project_path.name}")

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
        _print_yellow(f"⚪ Skipping MyPy: No Python files found in {project_path.name}")


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


def main() -> None:
    """Main function to orchestrate the entire monorepo setup."""
    _print_blue("Starting repository setup...")
    _print_blue("=" * 40)

    if not is_command_installed("uv"):
        install_uv()
    else:
        _print_green("✅ uv is already installed.")

    ensure_uv_managed_python_installed()

    project_root = Path(__file__).parent.parent.parent

    all_projects = get_project_directories(project_root)

    if not all_projects:
        _print_yellow("No applications or scripts found to set up.")
        sys.exit(0)

    _print_blue("\nSetting up all applications and scripts...")
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

    _print_green("\n" + "=" * 40)
    _print_green("🎉 All projects have been set up successfully!")
    _print_yellow("You are now ready to start development.")


if __name__ == "__main__":
    main()


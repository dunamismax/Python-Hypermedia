"""
A comprehensive, self-sufficient setup script for the Python-Hypermedia monorepo.

This script is designed to be run on a fresh clone of the repository, especially on a
new macOS or Linux machine. It ensures that all required development tools and
dependencies for every project in the monorepo are installed and configured.

The script will automatically:
1.  Check for and install `uv`, the project's Python package manager.
2.  Check for and install Node.js and npm if they are missing.
    - On macOS, it uses Homebrew (and installs Homebrew first if needed).
    - On Linux, it provides instructions for manual installation to avoid sudo.
3.  Install a `uv`-managed version of the Python interpreter.
4.  Scan the `apps/` and `scripts/` directories for valid projects.
5.  For each project found, it will:
   - Create a Python virtual environment (`.venv/`) using `uv venv`.
   - Install all Python dependencies from `pyproject.toml`.
   - Install all Node.js dependencies from `package.json` (if present).
   - Build static assets (e.g., Tailwind CSS).
   - Run Ruff for code formatting and linting to ensure code quality.

Usage:
    python scripts/project_setup/setup.py
"""

import os
import subprocess
import sys
from pathlib import Path
from typing import List


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


def cprint(text: str, color: str = None, bold: bool = False) -> None:
    """Prints text with specified color and boldness."""
    style = Colors.BOLD if bold else ""
    color_code = getattr(Colors, color.upper(), "") if color else ""
    print(f"{style}{color_code}{text}{Colors.END}")


# --- Prerequisite Checks and Installations ---


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
    cprint("uv not found. Installing...", color="blue", bold=True)
    try:
        # Ensure curl is available before attempting to use it.
        if not is_command_installed("curl"):
            cprint(
                "Error: `curl` is required to install uv, but it's not found.",
                color="red",
            )
            cprint("Please install `curl` and try again.", color="yellow")
            sys.exit(1)

        subprocess.run(
            "curl -LsSf https://astral.sh/uv/install.sh | sh",
            shell=True,
            check=True,
            stdout=sys.stdout,
            stderr=sys.stderr,
        )
        cprint("✅ uv installed successfully.", color="green")
        # Add uv to the current session's PATH for immediate use.
        os.environ["PATH"] = f"{os.path.expanduser('~/.cargo/bin')}:{os.environ['PATH']}"
    except subprocess.CalledProcessError as e:
        cprint(f"❌ Failed to install uv: {e}", color="red")
        sys.exit(1)


def install_homebrew() -> None:
    """Installs the Homebrew package manager on macOS."""
    cprint("Homebrew not found. Installing...", color="blue", bold=True)
    try:
        subprocess.run(
            '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',
            shell=True,
            check=True,
            stdout=sys.stdout,
            stderr=sys.stderr,
        )
        cprint("✅ Homebrew installed successfully.", color="green")
    except subprocess.CalledProcessError as e:
        cprint(f"❌ Failed to install Homebrew: {e}", color="red")
        sys.exit(1)


def ensure_node_npm_installed() -> None:
    """Ensures Node.js and npm are installed, handling OS-specific installation."""
    if is_command_installed("node") and is_command_installed("npm"):
        cprint("✅ Node.js and npm are already installed.", color="green")
        return

    cprint("Node.js or npm not found. Attempting installation...", color="yellow")
    platform = sys.platform

    if platform == "darwin":  # macOS
        if not is_command_installed("brew"):
            install_homebrew()
        cprint("Installing Node.js using Homebrew...", color="blue")
        run_command(["brew", "install", "node"], cwd=Path.cwd(), description="Install Node.js")

    elif platform.startswith("linux"):  # Linux
        cprint(
            "On Linux, please install Node.js and npm using your system's package manager.",
            color="red",
            bold=True,
        )
        cprint(
            "Example for Debian/Ubuntu: sudo apt update && sudo apt install nodejs npm",
            color="yellow",
        )
        cprint("After installation, please re-run this setup script.", color="yellow")
        sys.exit(1)

    else:
        cprint(f"Unsupported operating system: {platform}", color="red")
        cprint(
            "Please install Node.js and npm manually, then re-run this script.",
            color="yellow",
        )
        sys.exit(1)

    # Verify installation
    if not is_command_installed("node") or not is_command_installed("npm"):
        cprint("❌ Node.js installation failed.", color="red")
        sys.exit(1)

    cprint("✅ Node.js and npm installed successfully.", color="green")


# --- Project Discovery and Setup ---


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


def get_project_directories(root: Path, project_type: str) -> List[Path]:
    """Scans a directory ('apps' or 'scripts') and returns a list of valid project directories."""
    base_path = root / project_type
    if not base_path.is_dir():
        return []

    project_dirs = []
    for d in base_path.iterdir():
        # A valid project is a directory with a pyproject.toml file.
        if d.is_dir() and (d / "pyproject.toml").exists():
            # Exclude this setup script itself from being processed.
            if d.name == "project_setup":
                continue
            project_dirs.append(d)
    return sorted(project_dirs)


def run_command(command: List[str], cwd: Path, description: str) -> None:
    """Runs a command in a specified directory, handling errors and output."""
    cprint(f"🚀 Starting: {description} in {cwd.name}...", color="yellow")
    try:
        process = subprocess.Popen(
            command,
            cwd=cwd,
            stdout=sys.stdout,
            stderr=sys.stderr,
            text=True,
        )
        process.wait()
        if process.returncode == 0:
            cprint(f"✅ Success: {description}", color="green")
        else:
            cprint(
                f"❌ Error: {description} failed with exit code {process.returncode}",
                color="red",
            )
            sys.exit(1)
    except FileNotFoundError:
        cprint(
            f"❌ Error: Command '{command[0]}' not found. Is it installed and in your PATH?",
            color="red",
        )
        sys.exit(1)
    except Exception as e:
        cprint(f"❌ An unexpected error occurred: {e}", color="red")
        sys.exit(1)


def setup_project(project_path: Path) -> None:
    """Installs Python and Node.js dependencies for a given project."""
    cprint(f"\nProcessing project: {project_path.name}", color="cyan", bold=True)

    # Create Python virtual environment.
    run_command(["uv", "venv"], cwd=project_path, description="Create Python virtual environment")

    # Install Python dependencies if pyproject.toml exists.
    if (project_path / "pyproject.toml").exists():
        run_command(
            ["uv", "pip", "sync", "pyproject.toml"],
            cwd=project_path,
            description="Install Python dependencies",
        )

    # Install Node.js dependencies and build assets if package.json exists.
    if (project_path / "package.json").exists():
        run_command(
            ["npm", "install"], cwd=project_path, description="Install Node.js dependencies"
        )
        # Some projects may not have a build script, so we check for it.
        package_json_path = project_path / "package.json"
        if (
            '"build"'
            in package_json_path.read_text()
        ):
            run_command(
                ["npm", "run", "build"],
                cwd=project_path,
                description="Build static assets (CSS)",
            )

    run_quality_checks(project_path)


def run_quality_checks(project_path: Path) -> None:
    """Runs Ruff linter and formatter for a given project."""
    cprint(f"🔬 Running quality checks for: {project_path.name}", color="blue", bold=True)

    run_command(
        ["uv", "run", "ruff", "check", ".", "--fix"],
        cwd=project_path,
        description="Run Ruff linter",
    )
    run_command(
        ["uv", "run", "ruff", "format", "."],
        cwd=project_path,
        description="Run Ruff formatter",
    )


def main() -> None:
    """Main function to orchestrate the entire monorepo setup."""
    cprint("Starting repository setup...", color="blue", bold=True)
    cprint("=" * 40, color="blue")

    # --- Step 1: Ensure all prerequisites are met ---
    if not is_command_installed("uv"):
        install_uv()
    else:
        cprint("✅ uv is already installed.", color="green")

    ensure_node_npm_installed()

    # --- Step 2: Install uv-managed Python ---
    run_command(
        ["uv", "python", "install"], cwd=Path.cwd(), description="Install uv-managed Python"
    )

    # --- Step 3: Discover and set up all projects ---
    try:
        project_root = get_project_root()
    except FileNotFoundError as e:
        cprint(str(e), color="red")
        sys.exit(1)

    app_dirs = get_project_directories(project_root, "apps")
    script_dirs = get_project_directories(project_root, "scripts")
    all_projects = app_dirs + script_dirs

    if not all_projects:
        cprint("No applications or scripts found to set up.", color="yellow")
        sys.exit(0)

    cprint("\nSetting up all applications and scripts...", color="blue", bold=True)
    for project_path in all_projects:
        setup_project(project_path)

    cprint("\n" + "=" * 40, color="green", bold=True)
    cprint("🎉 All projects have been set up successfully!", color="green", bold=True)
    cprint("You are now ready to start development.", color="yellow")


if __name__ == "__main__":
    main()
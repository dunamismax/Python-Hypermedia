import os
import subprocess
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


# --- Utility Functions ---

def is_uv_installed() -> bool:
    """Checks if uv is installed and available in the system's PATH."""
    try:
        subprocess.run(["uv", "--version"], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def install_uv():
    """Installs uv using the official, non-interactive curl script."""
    cprint("uv not found. Installing...", color="blue", bold=True)
    try:
        subprocess.run(
            "curl -LsSf https://astral.sh/uv/install.sh | sh",
            shell=True,
            check=True,
            stdout=sys.stdout,
            stderr=sys.stderr,
        )
        cprint("✅ uv installed successfully.", color="green")
        # Add uv to the current session's PATH
        os.environ["PATH"] = f"{os.path.expanduser('~/.cargo/bin')}:{os.environ['PATH']}"
    except subprocess.CalledProcessError as e:
        cprint(f"❌ Failed to install uv: {e}", color="red")
        sys.exit(1)


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
        if d.is_dir() and (d / "pyproject.toml").exists():
            if d.name == "project_setup":
                continue
            project_dirs.append(d)
    return sorted(project_dirs)


def run_command(command: List[str], cwd: Path, description: str):
    """
    Runs a command in a specified directory.
    """
    cprint(f"🚀 Starting: {description} in {cwd}...", color="yellow")
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
                f"❌ Error: {description} failed with exit code {process.returncode}", color="red"
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


def setup_project(project_path: Path):
    """Installs Python and Node.js dependencies for a given project."""
    cprint(f"\nProcessing project: {project_path.name}", color="cyan", bold=True)

    run_command(["uv", "venv"], cwd=project_path, description="Create Python virtual environment")

    if (project_path / "pyproject.toml").exists():
        run_command(
            ["uv", "pip", "sync", "pyproject.toml"],
            cwd=project_path,
            description="Install Python dependencies",
        )

    if (project_path / "package.json").exists():
        run_command(
            ["npm", "install"], cwd=project_path, description="Install Node.js dependencies"
        )
        run_command(
            ["npm", "run", "build"],
            cwd=project_path,
            description="Build static assets (CSS)",
        )

    run_quality_checks(project_path)


def run_quality_checks(project_path: Path):
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


def main():
    """
    Main function to set up all projects in the monorepo.
    """
    if not is_uv_installed():
        install_uv()

    run_command(["uv", "python", "install"], cwd=Path.cwd(), description="Install uv-managed Python")

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

    cprint("Setting up all applications and scripts...", color="blue", bold=True)
    for project_path in all_projects:
        setup_project(project_path)

    cprint("\n🎉 All projects have been set up successfully!", color="green", bold=True)


if __name__ == "__main__":
    main()

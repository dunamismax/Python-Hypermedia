import os
import subprocess
import sys
from pathlib import Path
from typing import List

import typer

# Create a Typer application
app = typer.Typer(
    add_completion=False,
    help="A CLI tool to set up all projects in the Python-Hypermedia monorepo.",
)

# --- Utility Functions ---

def get_project_root() -> Path:
    """Finds the project root by looking for the .git directory."""
    current_path = Path.cwd().resolve()
    while not (current_path / ".git").exists():
        if current_path.parent == current_path:
            raise FileNotFoundError("Could not find project root. Make sure you are inside the repository.")
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
            # Exclude the setup script's own directory
            if d.name == "project_setup":
                continue
            project_dirs.append(d)
    return sorted(project_dirs)

def run_command(
    command: List[str],
    cwd: Path,
    description: str,
    clear_env_vars: List[str] = None,
):
    """
    Runs a command in a specified directory, optionally clearing environment variables.
    """
    typer.secho(f"🚀 Starting: {description} in {cwd}...", fg=typer.colors.YELLOW)

    env = os.environ.copy()
    if clear_env_vars:
        for var in clear_env_vars:
            if var in env:
                del env[var]

    try:
        process = subprocess.Popen(
            command,
            cwd=cwd,
            stdout=sys.stdout,
            stderr=sys.stderr,
            text=True,
            env=env,
        )
        process.wait()
        if process.returncode == 0:
            typer.secho(f"✅ Success: {description}", fg=typer.colors.GREEN)
        else:
            typer.secho(
                f"❌ Error: {description} failed with exit code {process.returncode}",
                fg=typer.colors.RED,
            )
            raise typer.Exit(1)
    except FileNotFoundError:
        typer.secho(
            f"❌ Error: Command '{command[0]}' not found. Is it installed and in your PATH?",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    except Exception as e:
        typer.secho(f"❌ An unexpected error occurred: {e}", fg=typer.colors.RED)
        raise typer.Exit(1)

def setup_project(project_path: Path):
    """Installs Python and Node.js dependencies for a given project."""
    typer.secho(f"\nProcessing project: {project_path.name}", bold=True, fg=typer.colors.CYAN)

    # Create virtual environment
    run_command(["uv", "venv"], cwd=project_path, description="Create Python virtual environment")

    # Install Python dependencies
    if (project_path / "pyproject.toml").exists():
        run_command(
            ["uv", "pip", "sync", "pyproject.toml"],
            cwd=project_path,
            description="Install Python dependencies",
            clear_env_vars=["VIRTUAL_ENV"],
        )

    # Install Node.js dependencies (if applicable)
    if (project_path / "package.json").exists():
        run_command(["npm", "install"], cwd=project_path, description="Install Node.js dependencies")

    # Run quality checks
    run_quality_checks(project_path)

def run_quality_checks(project_path: Path):
    """Runs Ruff linter and formatter for a given project."""
    typer.secho(f"🔬 Running quality checks for: {project_path.name}", bold=True, fg=typer.colors.BLUE)

    venv_python = project_path / ".venv" / "bin" / "python"
    if sys.platform == "win32":
        venv_python = project_path / ".venv" / "Scripts" / "python.exe"

    if not venv_python.exists():
        typer.secho(f"Could not find python executable in venv for {project_path.name}. Skipping.", fg=typer.colors.YELLOW)
        return

    # Run Ruff linter and formatter
    run_command([str(venv_python), "-m", "ruff", "check", ".", "--fix", "--ignore", "E501"], cwd=project_path, description="Run Ruff linter")
    run_command([str(venv_python), "-m", "ruff", "format", "."], cwd=project_path, description="Run Ruff formatter")

@app.command()
def main():
    """
    Sets up all projects in the monorepo by creating virtual environments,
    installing dependencies, and running quality checks.
    """
    try:
        project_root = get_project_root()
    except FileNotFoundError as e:
        typer.secho(str(e), fg=typer.colors.RED)
        raise typer.Exit(1)

    app_dirs = get_project_directories(project_root, "apps")
    script_dirs = get_project_directories(project_root, "scripts")
    all_projects = app_dirs + script_dirs

    if not all_projects:
        typer.secho("No applications or scripts found to set up.", fg=typer.colors.YELLOW)
        raise typer.Exit()

    typer.secho("Setting up all applications and scripts...", bold=True, fg=typer.colors.BLUE)
    for project_path in all_projects:
        setup_project(project_path)
    
    typer.secho("\n🎉 All projects have been set up successfully!", bold=True, fg=typer.colors.BRIGHT_GREEN)

if __name__ == "__main__":
    app()
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List

import questionary
import typer

# Create a Typer application
app = typer.Typer(
    add_completion=False,
    help="A CLI tool for managing and running projects in the Python-Hypermedia monorepo.",
)

# --- Utility Functions ---


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
        # A valid project is a directory containing a pyproject.toml
        if d.is_dir() and (d / "pyproject.toml").exists():
            # Exclude the app_runner itself to prevent recursion
            if d.name == "app_runner":
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

    # Install Python dependencies using the global uv, but with a cleared VIRTUAL_ENV
    if (project_path / "pyproject.toml").exists():
        run_command(
            ["uv", "pip", "install", "--no-cache", ".[dev]"],
            cwd=project_path,
            description="Install Python dependencies (including dev)",
            clear_env_vars=["VIRTUAL_ENV"],
        )
    else:
        typer.secho(
            "No pyproject.toml found, skipping Python dependency installation.",
            fg=typer.colors.YELLOW,
        )

    # Install Node.js dependencies (typically only for apps)
    if (project_path / "package.json").exists():
        run_command(
            ["npm", "install"], cwd=project_path, description="Install Node.js dependencies"
        )
    else:
        typer.secho("No package.json found, skipping npm install.", fg=typer.colors.YELLOW)

    # Run quality checks
    run_quality_checks(project_path)


def run_quality_checks(project_path: Path):
    """Runs Ruff linter and formatter for a given project."""
    typer.secho(
        f"🔬 Running quality checks for: {project_path.name}", bold=True, fg=typer.colors.BLUE
    )

    venv_python = project_path / ".venv" / "bin" / "python"
    if sys.platform == "win32":
        venv_python = project_path / ".venv" / "Scripts" / "python.exe"

    if not venv_python.exists():
        typer.secho(
            f"Could not find python executable in venv for {project_path.name}. Skipping quality checks.",
            fg=typer.colors.YELLOW,
        )
        return

    # Run Ruff linter (check and fix)
    run_command(
        [str(venv_python), "-m", "ruff", "check", ".", "--fix", "--ignore", "E501"],
        cwd=project_path,
        description="Run Ruff linter",
    )

    # Run Ruff formatter
    run_command(
        [str(venv_python), "-m", "ruff", "format", "."],
        cwd=project_path,
        description="Run Ruff formatter",
    )


# --- Typer Commands ---


@app.command()
def main():
    """
    Scans for projects, displays an interactive menu, and runs setup/launch tasks.
    """
    try:
        project_root = get_project_root()
    except FileNotFoundError as e:
        typer.secho(str(e), fg=typer.colors.RED)
        raise typer.Exit(1)

    app_dirs = get_project_directories(project_root, "apps")
    script_dirs = get_project_directories(project_root, "scripts")

    if not app_dirs and not script_dirs:
        typer.secho("No applications or scripts found.", fg=typer.colors.YELLOW)
        raise typer.Exit()

    # Create a mapping from name to path for easy lookup
    project_paths: Dict[str, Path] = {p.name: p for p in app_dirs + script_dirs}

    ALL_PROJECTS_OPTION = "🚀 ALL PROJECTS: Setup dependencies for all apps & scripts"

    choices = [questionary.Choice(title=ALL_PROJECTS_OPTION, value="all")]

    if app_dirs:
        choices.append(questionary.Separator("--- Select an App to Launch ---"))
        for app in app_dirs:
            choices.append(questionary.Choice(title=f"  ▶️  {app.name}", value=app.name))

    if script_dirs:
        choices.append(questionary.Separator("--- Select a Script to Setup ---"))
        for script in script_dirs:
            choices.append(questionary.Choice(title=f"  🛠️  {script.name}", value=script.name))

    try:
        selected_project_name = questionary.select(
            "Select a project to run, or choose to set up all projects:",
            choices=choices,
            use_indicator=True,
            style=questionary.Style([
                ("highlighted", "bold fg:yellow"),
                ("selected", "bold fg:ansibrightyellow"),
                ("pointer", "bold fg:yellow"),
            ]),
        ).ask()
    except KeyboardInterrupt:
        typer.secho("\n👋 User cancelled. Exiting.", fg=typer.colors.YELLOW)
        raise typer.Exit()

    if selected_project_name is None:
        typer.secho("No selection made. Exiting.", fg=typer.colors.YELLOW)
        raise typer.Exit()

    if selected_project_name == "all":
        typer.secho("Setting up all applications and scripts...", bold=True, fg=typer.colors.BLUE)
        for project_path in app_dirs + script_dirs:
            setup_project(project_path)
        typer.secho("\n🎉 All projects have been set up!", bold=True, fg=typer.colors.BRIGHT_GREEN)
        return

    # Handle selection of a single project
    selected_path = project_paths[selected_project_name]
    setup_project(selected_path)

    # Check if the selected project is an app and try to launch it
    is_app = selected_path in app_dirs
    if not is_app:
        typer.secho(
            f"\n✅ Setup complete for script: '{selected_project_name}'.",
            bold=True,
            fg=typer.colors.GREEN,
        )
        return

    # --- Launch Logic (only for apps) ---
    typer.secho(
        f"\n🚀 Launching app: '{selected_project_name}'...", bold=True, fg=typer.colors.BLUE
    )

    venv_python = selected_path / ".venv" / "bin" / "python"
    if sys.platform == "win32":
        venv_python = selected_path / ".venv" / "Scripts" / "python.exe"

    # Start Tailwind CSS watcher in the background
    tailwind_process = subprocess.Popen(["npm", "run", "watch"], cwd=selected_path)

    # Discover the package name inside the app's src directory
    src_path = selected_path / "src"
    app_module_name = next(src_path.iterdir()).name
    uvicorn_command = [
        str(venv_python),
        "-m",
        "uvicorn",
        f"src.{app_module_name}.main:app",
        "--reload",
        "--host",
        "127.0.0.1",
        "--port",
        "8000",
    ]

    typer.secho(f"Starting: Uvicorn server for {selected_project_name}...", fg=typer.colors.YELLOW)
    typer.secho(f"Running command: {' '.join(uvicorn_command)}", fg=typer.colors.MUTED)

    try:
        # Run Uvicorn in the foreground
        subprocess.call(uvicorn_command, cwd=project_root)
    except KeyboardInterrupt:
        typer.secho("\n🛑 Uvicorn server stopped by user.", fg=typer.colors.YELLOW)
    finally:
        typer.secho("Terminating Tailwind CSS watcher...", fg=typer.colors.YELLOW)
        tailwind_process.terminate()
        tailwind_process.wait()
        typer.secho("✅ Cleanup complete. Exiting.", fg=typer.colors.GREEN)


if __name__ == "__main__":
    app()

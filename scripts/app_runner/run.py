import os
import subprocess
import sys
from pathlib import Path
from typing import List

import questionary
import typer

# Create a Typer application
app = typer.Typer(
    add_completion=False,
    help="A CLI tool for managing and running applications in the Python-Hypermedia monorepo.",
)

# --- Utility Functions ---

def get_project_root() -> Path:
    """Finds the project root by looking for the .git directory."""
    current_path = Path.cwd()
    while current_path != current_path.parent:
        if (current_path / ".git").exists():
            return current_path
        current_path = current_path.parent
    raise FileNotFoundError("Project root not found. Make sure you are inside the repository.")

def get_app_directories(root: Path) -> List[Path]:
    """Scans the 'apps' directory and returns a list of app directories."""
    apps_path = root / "apps"
    if not apps_path.is_dir():
        return []
    return sorted([d for d in apps_path.iterdir() if d.is_dir()])

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


def install_dependencies(app_path: Path):
    """Installs Python and Node.js dependencies for a given app."""
    typer.secho(f"\nProcessing app: {app_path.name}", bold=True, fg=typer.colors.CYAN)

    # Create virtual environment
    run_command(["uv", "venv"], cwd=app_path, description="Create Python virtual environment")

    # Install Python dependencies using the global uv, but with a cleared VIRTUAL_ENV
    pyproject_path = app_path / "pyproject.toml"
    if pyproject_path.exists():
        run_command(
            ["uv", "pip", "install", "--no-cache", ".[dev]"],
            cwd=app_path,
            description="Install Python dependencies (including dev)",
            clear_env_vars=["VIRTUAL_ENV"],
        )
    else:
        typer.secho(
            "No pyproject.toml found, skipping Python dependency installation.",
            fg=typer.colors.YELLOW,
        )

    # Install Node.js dependencies
    if (app_path / "package.json").exists():
        run_command(
            ["npm", "install"], cwd=app_path, description="Install Node.js dependencies"
        )
    else:
        typer.secho("No package.json found, skipping npm install.", fg=typer.colors.YELLOW)

    # Run quality checks
    run_quality_checks(app_path)



def run_quality_checks(app_path: Path):
    """Runs Ruff linter and formatter for a given app."""
    typer.secho(f"🔬 Running quality checks for: {app_path.name}", bold=True, fg=typer.colors.BLUE)

    venv_python = app_path / ".venv" / "bin" / "python"
    if sys.platform == "win32":
        venv_python = app_path / ".venv" / "Scripts" / "python.exe"

    if not venv_python.exists():
        typer.secho(
            f"Could not find python executable in venv for {app_path.name}. Skipping quality checks.",
            fg=typer.colors.YELLOW,
        )
        return

    # Run Ruff linter (check)
    run_command(
        [str(venv_python), "-m", "ruff", "check", ".", "--fix"],
        cwd=app_path,
        description="Run Ruff linter",
    )

    # Run Ruff formatter
    run_command(
        [str(venv_python), "-m", "ruff", "format", "."],
        cwd=app_path,
        description="Run Ruff formatter",
    )


# --- Typer Commands ---

@app.command()
def main():
    """
    Scans for apps, displays an interactive menu, and runs setup/launch tasks.
    """
    try:
        project_root = get_project_root()
    except FileNotFoundError as e:
        typer.secho(str(e), fg=typer.colors.RED)
        raise typer.Exit(1)

    app_dirs = get_app_directories(project_root)
    if not app_dirs:
        typer.secho("No applications found in the 'apps' directory.", fg=typer.colors.YELLOW)
        raise typer.Exit()

    app_names = [app.name for app in app_dirs]
    
    ALL_APPS_OPTION = "🚀 ALL APPS: Create venv and install dependencies for all"
    
    choices = [
        questionary.Choice(title=ALL_APPS_OPTION, value="all"),
        questionary.Separator("--- Select an app to launch ---"),
    ]
    for name in app_names:
        choices.append(questionary.Choice(title=f"  ▶️  {name}", value=name))

    try:
        selected_app = questionary.select(
            "Select an application to run, or choose to set up all apps:",
            choices=choices,
            use_indicator=True,
            style=questionary.Style([
                ('highlighted', 'bold fg:yellow'),
                ('selected', 'bold fg:ansibrightyellow'),
                ('pointer', 'bold fg:yellow'),
            ])
        ).ask()
    except KeyboardInterrupt:
        typer.secho("\n👋 User cancelled. Exiting.", fg=typer.colors.YELLOW)
        raise typer.Exit()

    if selected_app is None:
        typer.secho("No selection made. Exiting.", fg=typer.colors.YELLOW)
        raise typer.Exit()

    if selected_app == "all":
        typer.secho("Setting up all applications...", bold=True, fg=typer.colors.BLUE)
        for app_dir in app_dirs:
            install_dependencies(app_dir)
        typer.secho("\n🎉 All applications have been set up!", bold=True, fg=typer.colors.BRIGHT_GREEN)

    else:
        app_path = project_root / "apps" / selected_app
        
        # 1. Install dependencies
        install_dependencies(app_path)
        
        # 2. Start development servers
        typer.secho(f"\n🚀 Launching '{selected_app}'...", bold=True, fg=typer.colors.BLUE)
        
        # Activate venv for subsequent commands
        venv_python = app_path / ".venv" / "bin" / "python"
        if sys.platform == "win32":
            venv_python = app_path / ".venv" / "Scripts" / "python.exe"

        # Start Tailwind CSS watcher in the background
        tailwind_watch_command = ["npm", "run", "watch"]
        typer.secho(f"Starting: Tailwind CSS watcher...", fg=typer.colors.YELLOW)
        tailwind_process = subprocess.Popen(tailwind_watch_command, cwd=app_path)
        
        # Start Uvicorn server in the foreground
        # We need to discover the package name inside the src directory
        src_path = app_path / "src"
        app_module_name = next(src_path.iterdir()).name
        uvicorn_command = [
            str(venv_python),
            "-m",
            "uvicorn",
            f"src.{app_module_name}.main:app",
            "--reload",
            "--host", "127.0.0.1",
            "--port", "8000",
        ]
        typer.secho(f"Starting: Uvicorn server for {selected_app}...", fg=typer.colors.YELLOW)
        typer.secho(f"Running command: {' '.join(uvicorn_command)}", fg=typer.colors.MUTED)
        
        try:
            # Use subprocess.call to run it in the foreground
            subprocess.call(uvicorn_command, cwd=project_root)
        except KeyboardInterrupt:
            typer.secho("\n🛑 Uvicorn server stopped by user.", fg=typer.colors.YELLOW)
        finally:
            # Clean up the background Tailwind process
            typer.secho("Terminating Tailwind CSS watcher...", fg=typer.colors.YELLOW)
            tailwind_process.terminate()
            tailwind_process.wait()
            typer.secho("✅ Cleanup complete. Exiting.", fg=typer.colors.GREEN)

if __name__ == "__main__":
    app()

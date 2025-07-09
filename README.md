<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" alt="The Python programming language logo." width="100"/>
</p>

<p align="center">
  <a href="https://github.com/dunamismax/Python-Hypermedia">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&pause=1000&color=4B8BBE&center=true&vCenter=true&width=800&lines=The+Python+Hypermedia+Stack;Building+Modern+Server-Rendered+Apps;FastAPI+%2B+HTMX+%2B+Tailwind+CSS;Minimal+JavaScript.+Maximum+Productivity." alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/astral-sh/uv"><img src="https://img.shields.io/badge/uv-0.1-blue.svg" alt="uv version"></a>
  <a href="https://img.shields.io/github/repo-size/dunamismax/Python-Hypermedia"><img src="https://img.shields.io/github/repo-size/dunamismax/Python-Hypermedia" alt="Repo Size"></a>
  <a href="https://github.com/dunamismax/Python-Hypermedia/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/dunamismax/Python-Hypermedia/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"></a>
  <a href="https://github.com/dunamismax/Python-Hypermedia/stargazers"><img src="https://img.shields.io/github/stars/dunamismax/Python-Hypermedia" alt="GitHub Stars"></a>
</p>

---

## About This Project

This monorepo is a collection of Python web applications that demonstrate a modern, server-rendered approach to web development. Each application is a standalone project with its own dependencies and environment, but all share a common set of tools and a unified development workflow.

The primary goal is to provide a structured and scalable environment for building web applications with a focus on performance, developer experience, and minimal frontend complexity.

### Target Environments

All code in this repository is developed and tested on **macOS** and is intended for production deployment on **Linux (Ubuntu)**.

<details>
<summary><h3>The Python Hypermedia Stack (Click to Expand)</h3></summary>

This stack is designed for building fast, modern web applications with server-rendered HTML, enhanced with dynamic interactivity. It prioritizes developer experience, performance, and maintainability by leveraging a curated set of modern tools.

### **1. Development & Tooling**

A streamlined toolchain for a productive and consistent development environment.

- [**uv**](https://astral.sh/uv)
  - **Why:** A next-generation, high-performance Python packaging tool. `uv` handles project dependency management and virtual environments with exceptional speed, replacing traditional tools like `pip` and `venv` for a faster, more efficient workflow.
- [**Ruff**](https://docs.astral.sh/ruff/)
  - **Why:** An extremely fast, all-in-one Python linter and code formatter. Ruff replaces multiple tools (like Black, isort, and Flake8) with a single, cohesive, and blazing-fast utility, ensuring consistent code quality and style across the project.

### **2. Backend**

The application's core, built for speed, resilience, and connectivity.

- [**FastAPI**](https://fastapi.tiangolo.com/)
  - **Why:** A modern, high-performance Python web framework. It uses standard Python type hints to build robust APIs and render server-side HTML templates, providing automatic data validation and documentation.
- [**Gunicorn**](https://gunicorn.org/)
  - **Why:** A battle-tested WSGI HTTP server used as a process manager for Uvicorn in production. Gunicorn manages multiple Uvicorn worker processes, enabling you to leverage multi-core CPUs, increase capacity, and improve fault tolerance.
- [**Uvicorn**](https://www.uvicorn.org/)
  - **Why:** A lightning-fast ASGI server that runs the FastAPI application. In production, it is managed by Gunicorn to run multiple worker processes, enabling high-performance asynchronous capabilities.
- [**HTTPX**](https://www.python-httpx.org/)
  - **Why:** A fully featured, modern HTTP client for Python. It provides both sync and async APIs, making it the ideal choice for a FastAPI application to interact with external services without blocking the event loop.

### **3. Database**

A unified and Pythonic approach to data modeling, interaction, and evolution.

- [**SQLModel**](https://sqlmodel.tiangolo.com/)
  - **Why:** The primary tool for database interaction, built by the creator of FastAPI. SQLModel cleverly combines Pydantic and SQLAlchemy, allowing you to define data, database tables, and API models in a single Python class. This significantly reduces code duplication and simplifies data management.
- [**Alembic**](https://alembic.sqlalchemy.org/en/latest/)
  - **Why:** A powerful database migration tool from the creator of SQLAlchemy. Alembic provides a reliable and systematic way to manage and version changes to your database schema as your application's models evolve.
- [**Pydantic**](https://docs.pydantic.dev/latest/)
  - **Why:** One of the foundational libraries that power SQLModel. Pydantic provides robust data validation and settings management using Python type hints.
- [**SQLAlchemy**](https://www.sqlalchemy.org/)
  - **Why:** One of the foundational libraries that power SQLModel. SQLAlchemy offers a powerful and flexible SQL toolkit and Object Relational Mapper (ORM) for comprehensive database control.

### **4. Frontend**

A hypermedia-driven frontend that delivers a rich user experience without requiring a heavy client-side JavaScript framework.

- [**Jinja2**](https://jinja.palletsprojects.com/)
  - **Why:** A fast and expressive templating engine used by FastAPI to render dynamic HTML, injecting backend data directly into the user interface.
- [**HTMX**](https://htmx.org/)
  - **Why:** The core of the interactive experience. HTMX allows you to trigger AJAX requests directly from HTML attributes, enabling smooth UI updates by swapping server-rendered HTML fragments without writing complex JavaScript.
- [**Tailwind CSS**](https://tailwindcss.com/docs/)
  - **Why:** A utility-first CSS framework for rapidly building custom user interfaces directly within your HTML, promoting speed and consistency in design.
- [**DaisyUI**](https://daisyui.com/)
  - **Why:** A plugin for Tailwind CSS that provides a library of pre-styled components (like buttons, cards, and menus). It accelerates development by offering ready-to-use UI elements that are fully customizable with Tailwind utilities.
- [**TypeScript**](https://www.typescriptlang.org/docs/)
  - **Why:** Used for minimal, targeted client-side interactions where HTMX may not be suitable. Vanilla TypeScript offers type safety for small, self-contained scripts without adding framework overhead.

### **5. CLI & Task Management**

Modern tools for building command-line interfaces and automating development tasks.

- [**Typer**](https://typer.tiangolo.com/)
  - **Why:** A library for building powerful and user-friendly CLI applications, created by the author of FastAPI. It uses the same Python type-hint philosophy, making it intuitive to create commands for database migrations, user management, or other administrative tasks.
- [**Invoke**](https://www.pyinvoke.org/)
  - **Why:** A Python task execution library for defining and running administrative tasks. Invoke is excellent for creating a clean, organized collection of commands for common operations like starting a dev server, running tests, or deploying the application.

### **6. Deployment**

A self-hosted, secure, and stable production environment.

- [**Ubuntu Server (LTS)**](https://ubuntu.com/server/docs)
  - **Why:** A popular, stable, and well-documented Linux distribution ideal for web servers. The Long-Term Support (LTS) version guarantees security and maintenance updates for years.
- [**Caddy**](https://caddyserver.com/docs/)
  - **Why:** A modern, powerful web server and reverse proxy with a focus on simplicity. Caddy's standout feature is fully automatic HTTPS, effortlessly securing your application with zero-touch TLS certificate provisioning and renewal.

</details>

---

## Project Structure

This monorepo is organized with a focus on complete application independence.

- **`apps/`**: Contains all independent applications. Each subdirectory is a complete, standalone project with its own dependencies, environment, and configuration.
  - **[`todo-app/`](https://github.com/dunamismax/Python-Hypermedia/tree/main/apps/todo-app)**: An example To-Do list application.
  - **[`dunamismax/`](https://github.com/dunamismax/Python-Hypermedia/tree/main/apps/dunamismax)**: A personal blog and portfolio website.
- **[`docs/`](https://github.com/dunamismax/Python-Hypermedia/tree/main/docs)**: Contains additional documentation and reference materials.
- **[`playground/`](https://github.com/dunamismax/Python-Hypermedia/tree/main/playground)**: A space for experimental projects and proofs-of-concept.
- **[`scripts/`](https://github.com/dunamismax/Python-Hypermedia/tree/main/scripts)**: Contains utility scripts for development, automation, and management.
- **`.gitignore`**: A single, top-level gitignore for the whole repository.
- **`LICENSE`**: The MIT license file for the project.
- **`README.md`**: This file.

---

## Getting Started

Setting up this monorepo is an automated process designed to get you from a fresh clone to a fully operational development environment with a single command.

### 1. Prerequisites

- A Unix-like operating system (macOS or Linux).
- `git` for cloning the repository.
- An internet connection.

The setup script will handle the installation of all other required tools, including `uv`, `python`, `node`, and `npm`.

### 2. Initial Repository Setup

First, clone the repository to your local machine:

```bash
git clone https://github.com/dunamismax/Python-Hypermedia.git
cd Python-Hypermedia
```

Next, run the **`project_setup`** script. This is the **only time you should use the `python` command directly**. This script will install `uv` and a managed version of Python, which you will use for all subsequent commands.

```bash
python scripts/project_setup/setup.py
```

After this script completes, the entire monorepo is configured and ready for development.

### 3. Using uv: The Only Python Command You Need

After you run the initial `python scripts/project_setup/setup.py` command, you should **no longer use the `python` command directly**. The setup script installs a managed version of Python via `uv`, and from that point on, `uv` should be used to run all Python-related tasks.

This ensures that you are always using the correct, project-defined version of Python and its dependencies, creating a perfectly consistent environment.

**From now on, to run any Python script, you will use `uv run`:**

```bash
# Example: Running a script
uv run some_script.py

# Example: Running the cleanup script
uv run scripts/project_cleanup/cleanup.py
```

`uv` is a powerful and extremely fast Python package installer, resolver, and version manager. It replaces `pip`, `pip-tools`, `virtualenv`, and `pyenv`. By using `uv run`, you gain:

- **Consistency**: Always use the correct Python version and dependencies for the project.
- **Speed**: `uv` is significantly faster than traditional Python tooling.
- **Simplicity**: A single tool for all your Python environment needs.

For a comprehensive overview of its capabilities, refer to the official [uv features documentation](https://docs.astral.sh/uv/getting-started/features/).

### 4. Running an Application

Once the initial setup is complete, running any application requires navigating to its directory and starting its development servers.

**Example using `todo-app`:**

1. **Navigate to the app's directory:**

   ```bash
   cd apps/todo-app
   ```

2. **Run the development servers (requires two separate terminals):**

   - **Terminal 1: Start the Tailwind CSS watcher.**
     This automatically rebuilds your CSS file when you make changes.

     ```bash
     npm run watch
     ```

   - **Terminal 2: Start the FastAPI server.**
     `uv run` automatically uses the project's virtual environment and dependencies. The `--reload` flag enables live reloading for your Python code.

     ```bash
     uv run uvicorn src.todo_app.main:app --reload
     ```

3. **Open the app in your browser:**
   Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 5. Keeping Your Environment Clean and Up-to-Date

To ensure a clean and consistent environment, you can use the `project_cleanup` and `project_setup` scripts together. This is the recommended workflow after pulling new changes, adding a new application, or changing dependencies.

1. **Run the cleanup script** to remove all temporary files and build artifacts.

   ```bash
   uv run scripts/project_cleanup/cleanup.py
   ```

2. **Run the setup script** to reinstall and sync all dependencies and configurations.

   ```bash
   uv run scripts/project_setup/setup.py
   ```

---

## Contributing

Contributions are welcome! As this is a learning and development project, suggestions, bug reports, and feature ideas are all highly appreciated. Please feel free to fork the repository, create a feature branch, and open a pull request.

---

## License

This repository is licensed under the **MIT License**. See the `LICENSE` file for more details.

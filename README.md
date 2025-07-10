<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" alt="The Python programming language logo." width="100"/>
</p>

<p align="center">
  <a href="https://github.com/dunamismax/Python-Hypermedia">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&pause=1000&color=4B8BBE&center=true&vCenter=true&width=800&lines=The+Python+Hypermedia+Stack;Building+Modern+Server-Rendered+Apps;FastAPI+%2B+HTMX+%2B+Pico.css;Minimal+JavaScript.+Maximum+Productivity." alt="Typing SVG" />
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

This monorepo is a collection of Python web applications that demonstrate a modern, server-rendered approach to web development. Each application is a standalone project with its own dependencies and environment, but all share a common set of tools and a unified development workflow based on **The Python Hypermedia Stack**.

The primary goal is to provide a structured and scalable environment for building web applications with a focus on performance, developer experience, and minimal frontend complexity.

### Target Environments

All code in this repository is developed and tested on **macOS** and is intended for production deployment on **Linux (Ubuntu)**.

<details>
<summary><h3>The Python Hypermedia Stack (Click to Expand)</h3></summary>

This Python Hypermedia Stack is a masterclass in modern web development, thoughtfully curating a suite of best-in-class tools to create a cohesive and powerful development experience. Its commitment to a fully asynchronous backend, paired with a hypermedia-driven frontend, represents a forward-thinking approach that champions simplicity, performance, and maintainability. This stack is a testament to the idea that you can build highly interactive, secure, and scalable web applications without the heavy complexity of traditional frontend frameworks, making it an elegant and productive choice for any development team.

---

### **1. Development & Tooling**

A streamlined toolchain for a productive and consistent development environment, ensuring rapid iteration and high code quality.

- [**uv**](https://astral.sh/uv)
  - **Why:** The next-generation, high-performance Python packaging tool. `uv` is central to all project environment and dependency management, providing an incredibly fast and reliable solution for reproducible environments.
- [**Ruff**](https://docs.astral.sh/ruff/)
  - **Why:** An extremely fast, all-in-one Python linter and code formatter. Ruff ensures consistent code quality and style across the project with a single, cohesive, and blazing-fast utility, integrating seamlessly into the development workflow.

### **2. Backend**

The application's core, built on a fully asynchronous foundation for maximum speed, concurrency, and efficient handling of web requests.

- [**FastAPI**](https://fastapi.tiangolo.com/)
  - **Why:** A modern, high-performance Python web framework. It leverages standard Python type hints for robust APIs and efficient server-side HTML template rendering, forming the backbone of the application.
- [**Uvicorn**](https://www.uvicorn.org/)
  - **Why:** A lightning-fast ASGI server that runs the FastAPI application. Uvicorn serves as the high-performance process manager for both development and production, ensuring rapid response times.
- [**HTTPX**](https://www.python-httpx.org/)
  - **Why:** A fully featured, modern HTTP client for Python. It provides both synchronous and asynchronous APIs, making it the ideal choice for a FastAPI application to interact with external services without blocking the event loop, maintaining responsiveness.

### **3. Database & Migrations**

A unified and fully asynchronous approach to data modeling, interaction, and schema evolution, ensuring data integrity and performance.

- [**PostgreSQL**](https://www.postgresql.org/docs/)
  - **Why:** A powerful, open-source object-relational database system renowned for its reliability, extensive features, and high performance, serving as the robust data store.
- [**SQLModel**](https://sqlmodel.tiangolo.com/)
  - **Why:** The primary tool for database interaction. SQLModel cleverly combines Pydantic and SQLAlchemy, allowing you to define data models, database tables, and API models in a single, elegant Python class, simplifying data management.
- [**Alembic**](https://alembic.sqlalchemy.org/en/latest/)
  - **Why:** A lightweight database migration tool designed for SQLAlchemy (which powers SQLModel) to manage the lifecycle of your database schema, enabling seamless evolution of the database structure.
- [**asyncpg**](https://magicstack.github.io/asyncpg/current/)
  - **Why:** A high-performance, asyncio-native database driver for PostgreSQL. `asyncpg` is the essential link between the asynchronous framework and the database, ensuring all database communication is non-blocking and highly efficient.

### **4. Asynchronous Task Processing**

A native, lightweight system for handling background tasks that should not block the response to the client, ensuring a smooth user experience.

- [**FastAPI BackgroundTasks**](https://fastapi.tiangolo.com/tutorial/background-tasks/)
  - **Why:** For short-lived, in-process background tasks, FastAPI's native `BackgroundTasks` feature is the perfect fit. It allows you to run operations like sending notifications or processing data after returning a response, simplifying the architecture by avoiding the need for external dependencies.

### **5. Frontend**

A pure hypermedia-driven frontend that delivers a rich user experience without requiring a complex JavaScript framework or a build step, focusing on server-rendered HTML.

- [**Jinja2**](https://jinja.palletsprojects.com/)
  - **Why:** A fast and expressive templating engine used by FastAPI to render dynamic HTML, injecting backend data directly into the user interface, providing a flexible and powerful templating solution.
- [**HTMX**](https://htmx.org/)
  - **Why:** The core of the interactive experience. HTMX allows you to trigger AJAX requests directly from HTML attributes, enabling smooth UI updates by swapping server-rendered HTML fragments without writing complex JavaScript, embracing the hypermedia approach.
- [**Pico.css**](https://picocss.com/)
  - **Why:** A minimalist CSS framework that makes semantic HTML look beautiful by default. By linking to a single CSS file, you get elegant styling for raw HTML elements, automatic dark mode, and responsive design, all without dependencies or a complex setup, aligning with the minimal frontend philosophy.

### **6. Testing**

A powerful and standard framework for ensuring code quality and correctness, providing confidence in the application's reliability.

- [**Pytest**](https://docs.pytest.org/en/stable/)
  - **Why:** The de facto standard testing framework for Python. Pytest makes it easy to write small, readable tests and scales to support complex functional testing, with excellent support for asynchronous code via plugins like `pytest-asyncio`.

### **7. CLI, Security & Configuration**

Modern tools for building command-line interfaces, securing the application, and managing configuration, enhancing developer productivity and application robustness.

- [**Typer**](https://typer.tiangolo.com/)
  - **Why:** A library for building powerful and user-friendly CLI applications. It uses the same Python type-hint philosophy as FastAPI, making it intuitive to create administrative commands and automate tasks.

### **8. Deployment**

A self-hosted, secure, and stable production environment, optimized for the Python Hypermedia Stack.

- [**Ubuntu Server (LTS)**](https://ubuntu.com/server)
  - **Why:** A popular, stable, and well-documented Linux distribution ideal for web servers, with long-term support for security and maintenance updates, providing a reliable foundation for deployment.
- [**Caddy**](https://caddyserver.com/docs/)
  - **Why:** A modern, powerful web server and reverse proxy with a focus on simplicity. Caddy manages incoming traffic, serves static files, and acts as a reverse proxy for Uvicorn. Its standout feature is fully automatic HTTPS, simplifying secure deployments.

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

This guide covers the one-time setup for this monorepo.

### Prerequisites

- A Unix-like OS (macOS/Linux)
- `git`
- Python 3.9+

### One-Time Setup

Clone the repository and run the setup script. This script will automatically install `uv` (if not already present), set up a `uv`-managed Python environment, and install all project dependencies across the monorepo. It will also configure Ruff for linting and formatting.

```bash
git clone https://github.com/dunamismax/Python-Hypermedia.git
cd Python-Hypermedia
python3 scripts/project_setup/setup.py
```

That's it! The `setup.py` script handles everything. From this point forward, `uv` is your primary tool for managing the monorepo's Python environments and running scripts.

### The `uv` Workflow: Your Primary Tool

After the initial setup, `uv` becomes your primary tool for managing the monorepo's Python environments and running scripts. `uv` is designed for speed, consistency, and simplicity, replacing the need for tools like `pip`, `virtualenv`, and `pyenv` for most tasks within this project.

All Python-related tasks, whether running scripts within this monorepo or any other Python script on your system, should now be executed through `uv run`. This ensures you're always using the correct project-defined Python version and dependencies.

For more details on `uv`'s capabilities, refer to the [official uv documentation](https://docs.astral.sh/uv/getting-started/features/).

#### Examples of `uv run` usage

```bash
# Running a script within this monorepo (e.g., a cleanup script)
uv run scripts/project_cleanup/cleanup.py

# Running a simple standalone Python script anywhere on your system
uv run example.py

# Running an application (e.g., the todo-app)
cd apps/todo-app
uv run uvicorn src.todo_app.main:app --reload
```

### Keeping Environments Fresh

After pulling changes or modifying dependencies, you can reset and resync your monorepo environment by running the cleanup script followed by the setup script again using `uv run`:

```bash
uv run scripts/project_cleanup/cleanup.py
```

```bash
uv run scripts/project_setup/setup.py
```

---

## Contributing

Contributions are welcome! As this is a learning and development project, suggestions, bug reports, and feature ideas are all highly appreciated. Please feel free to fork the repository, create a feature branch, and open a pull request.

---

## License

This repository is licensed under the **MIT License**. See the `LICENSE` file for more details.

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

This monorepo serves as a centralized showcase for a variety of Python web applications, each demonstrating a modern, robust, and productive approach to building server-rendered applications. It is built on the principle of project-level isolation, with each app being a completely independent entity.

The primary goal is to provide a structured, maintainable, and scalable environment for building modern web applications with a focus on performance, developer experience, and minimal frontend complexity, using **The Python Hypermedia Stack**.

### Target Environments

All code in this repository primarily targets **macOS** for development and testing. **Linux (Ubuntu)** is the target for production deployments.

<details>
<summary><h3>The Python Hypermedia Stack (Click to Expand)</h3></summary>

This stack is designed for building self-contained, high-performance, and interactive web applications. The architecture is centered around a powerful Python backend that renders HTML, enhanced with a minimal set of best-in-class libraries to create a rich user experience without the need for a heavy client-side framework.

---

### **1. Backend**

The core of the application, responsible for handling logic, routing, and rendering the user interface.

- **FastAPI**
  - **Why:** A modern, high-performance Python web framework ideal for building APIs and, in this case, serving server-rendered HTML. It uses standard Python type hints for data validation, which leads to robust, editor-friendly code. It will handle the routes and render the Jinja2 templates.
  - **Latest Version:** 0.111.0
  - **Official Documentation:** <https://fastapi.tiangolo.com/>
- **Uvicorn**
  - **Why:** A lightning-fast ASGI (Asynchronous Server Gateway Interface) server that is required to run FastAPI's asynchronous capabilities. It acts as the direct process manager for the Python application on your server.
  - **Latest Version:** 0.30.1
  - **Official Documentation:** <https://www.uvicorn.org/>

### **2. Database & Data Modeling**

This combination provides a powerful and Python-native way to define, validate, and interact with your database.

- **Pydantic**
  - **Why:** The backbone for data validation in FastAPI. It uses Python type hints to validate, serialize, and deserialize data, ensuring that all data flowing through your application is well-structured and correct. It's a core dependency of FastAPI.
  - **Latest Version:** 2.8.2
  - **Official Documentation:** <https://docs.pydantic.dev/>
- **SQLAlchemy**
  - **Why:** The premier SQL toolkit and Object Relational Mapper (ORM) for Python. It provides a full suite of powerful tools for interacting with your database, offering both a high-level ORM and a low-level SQL expression language for maximum flexibility and performance.
  - **Latest Version:** 2.0.31
  - **Official Documentation:** <https://www.sqlalchemy.org/>
- **SQLModel**
  - **Why:** Created by the author of FastAPI, SQLModel simplifies interaction between the database and the API. It is built on top of Pydantic and SQLAlchemy, allowing you to define your data models, database tables, and API responses from a single, clear Python class. This reduces code duplication significantly.
  - **Latest Version:** 0.1.1
  - **Official Documentation:** <https://sqlmodel.tiangolo.com/>

### **3. Frontend (The Hypermedia Stack)**

This stack creates a rich, interactive user experience by rendering HTML on the server, avoiding the need for a complex client-side JavaScript framework.

- **Jinja2**
  - **Why:** A fast, expressive, and widely-used templating engine for Python. FastAPI will use Jinja2 to render your HTML templates, injecting dynamic data from the backend before sending the final HTML page to the user's browser.
  - **Latest Version:** 3.1.4
  - **Official Documentation:** <https://jinja.palletsprojects.com/>
- **HTMX**
  - **Why:** This is the key to modern interactivity in this stack. HTMX allows you to access modern browser features like AJAX directly from HTML attributes. Instead of writing JavaScript to fetch data and update the UI, you can add simple attributes to your HTML elements that tell HTMX to fetch a new piece of HTML from the server and swap it into the page.
  - **Latest Version:** 2.0.1
  - **Official Documentation:** <https://htmx.org/>
- **Tailwind CSS**
  - **Why:** A utility-first CSS framework that allows for rapid UI development directly within your HTML. Instead of writing custom CSS files, you use pre-defined utility classes. This is highly efficient for prototyping and building custom designs without leaving your Jinja2 templates.
  - **Latest Version:** 3.4.4
  - **Official Documentation:** <https://tailwindcss.com/docs/>
- **DaisyUI**
  - **Why:** A plugin for Tailwind CSS that provides pre-styled components (like buttons, cards, menus, etc.) as Tailwind utility classes. This dramatically speeds up development by giving you beautifully designed components out-of-the-box, while still allowing for full customization through standard Tailwind utilities.
  - **Latest Version:** 4.12.10
  - **Official Documentation:** <https://daisyui.com/>
- **TypeScript (Vanilla)**
  - **Why:** As requested, for minimal, "sprinkled-in" use. While HTMX handles the vast majority of interactivity, you might occasionally need a small, self-contained script for a purely client-side interaction (e.g., toggling a class on a complex element without a server trip). Using vanilla TypeScript provides type-safety for these small, targeted use cases.
  - **Latest Version:** 5.5.3
  - **Official Documentation:** <https://www.typescriptlang.org/docs/>

### **4. CLI & Management**

This project uses **uv** for all Python-related tasks, including script running, dependency management, and environment setup. Scripts are executed directly with `uv run`, which automatically handles the environment and dependencies.

### **5. Deployment & Hosting**

Your specified self-hosted deployment on a Linux virtual machine.

- **Ubuntu Server**
  - **Why:** A stable, popular, and well-documented Linux distribution, making it an excellent choice for a web server. The Long-Term Support (LTS) version ensures security updates and stability for years.
  - **Latest Version:** 24.04 LTS ("Noble Numbat")
  - **Official Documentation:** <https://ubuntu.com/server/docs>
- **Caddy**
  - **Why:** An incredibly powerful and easy-to-use web server that excels as a reverse proxy. Its killer feature is automatic HTTPS, meaning it will provision and renew TLS certificates for your domains automatically. Its configuration file (the Caddyfile) is famously simple compared to alternatives. It will sit in front of your Uvicorn process, handling incoming traffic and routing it to your FastAPI application.
  - **Latest Version:** 2.8.4
  - **Official Documentation:** <https://caddyserver.com/docs/>

</details>

---

## Project Structure

This monorepo is organized with a focus on complete application independence.

- **`apps/`**: The main directory containing all independent applications. Each subdirectory is a complete, standalone project with its own dependencies, environment, and configuration.
  - **[`todo-app/`](https://github.com/dunamismax/Python-Hypermedia/tree/main/apps/todo-app)**: An example To-Do list application.
  - **[`dunamismax/`](https://github.com/dunamismax/Python-Hypermedia/tree/main/apps/dunamismax)**: A personal blog and portfolio website.
- **[`docs/`](https://github.com/dunamismax/Python-Hypermedia/tree/main/docs)**: Contains additional documentation and reference materials.
- **[`scripts/`](https://github.com/dunamismax/Python-Hypermedia/tree/main/scripts)**: Contains various utility scripts for development, automation, and management.
- **`.gitignore`**: A single, top-level gitignore for the whole repository.
- **`LICENSE`**: The MIT license file for the project.
- **`README.md`**: This file.

---

## Getting Started

The development workflow is designed to be simple and consistent across all projects in this repository, powered by **uv**.

### 1. Prerequisites

- A Unix-like operating system (macOS or Linux)
- `curl`
- **Node.js and npm**: For managing frontend dependencies in the web applications.

### 2. Initial Repository Setup

First, clone the repository to your local machine:

```bash
git clone https://github.com/dunamismax/Python-Hypermedia.git
cd Python-Hypermedia
```

Next, run the **`project_setup`** script. This is a one-time command that will automatically install `uv`, a `uv`-managed version of Python, and all project dependencies.

**Note:**

(This is the last time we will ever use the 'python' command. going forward all commands will be 'uv run script.py' since uv and it's python version get installed by this setup script.)

```bash
python scripts/project_setup/setup.py
```

After this script completes, every project in the monorepo is ready to be used.

### 3. Running an Application

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

### 4. Cleaning the Repository

To reset the repository to a clean state, you can use the **`project_cleanup`** script. It will immediately remove all generated files like virtual environments, `node_modules`, and caches.

```bash
uv run scripts/project_cleanup/cleanup.py
```

### 5. Using uv

`uv` is a powerful and extremely fast Python package installer and resolver, designed to be a direct replacement for `pip`, `pip-tools`, and `virtualenv`. It can also manage Python versions, effectively replacing tools like `pyenv`. For a comprehensive overview of its capabilities, refer to the official [uv features documentation](https://docs.astral.sh/uv/getting-started/features/).

With `uv`, you can:

- Install and manage Python versions.
- Create and manage virtual environments.
- Install and synchronize project dependencies from `pyproject.toml`.
- Run Python scripts and tools within managed environments.

---

## Contributing

Contributions are welcome! As this is a learning and development project, suggestions, bug reports, and feature ideas are all highly appreciated. Please feel free to fork the repository, create a feature branch, and open a pull request.

---

## License

This repository is licensed under the **MIT License**. See the `LICENSE` file for more details.

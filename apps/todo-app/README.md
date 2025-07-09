# To-Do App

This application is a simple and interactive To-Do list manager built with **The Python Hypermedia Stack**. It uses FastAPI for the backend and HTMX to create a smooth, single-page user experience without writing complex JavaScript.

The primary purpose of this app is to demonstrate a modern, server-side rendering approach to building fundamental CRUD (Create, Read, Update, Delete) applications.

## How It Works

The application starts a FastAPI server that renders a main HTML page using Jinja2 templates. All user interactions—such as adding, toggling, or deleting a To-Do item—are handled via HTMX. These actions send AJAX requests to the server, which processes the request, interacts with a local SQLite database, and returns a small HTML partial. HTMX then intelligently swaps this new HTML into the page, updating the UI instantly without a full page reload.

## How to Run This App

This app is managed by the central `project_setup` script in the repository's `scripts/` directory.

1. **Run the main setup script** from the root of the repository to install all dependencies for this app.

   ```bash
   python scripts/project_setup/setup.py
   ```

2. **Navigate to this app's directory:**

   ```bash
   cd apps/todo-app
   ```

3. **Run the development servers (requires two separate terminals):**

   - **Terminal 1 (CSS Watcher):**

     ```bash
     npm run watch
     ```

   - **Terminal 2 (FastAPI Server):**
     `uv run` automatically uses the project's virtual environment and dependencies. The `--reload` flag enables live reloading.

     ```bash
     uv run uvicorn src.todo_app.main:app --reload
     ```

### What You Get

Once the servers are running, you can access a fully functional To-Do application in your browser at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**.

# To-Do App

This application is a simple and interactive To-Do list manager built with **The Python Hypermedia Stack**. It uses FastAPI for the backend and HTMX to create a smooth, single-page user experience without writing complex JavaScript.

The primary purpose of this app is to demonstrate a modern, server-side rendering approach to building fundamental CRUD (Create, Read, Update, Delete) applications.

## How It Works

The application starts a FastAPI server that renders a main HTML page using Jinja2 templates. All user interactions—such as adding, toggling, or deleting a To-Do item—are handled via HTMX. These actions send AJAX requests to the server, which processes the request, interacts with a local SQLite database, and returns a small HTML partial. HTMX then intelligently swaps this new HTML into the page, updating the UI instantly without a full page reload.

## How to Run This App

Before running, ensure you have completed the initial repository setup by running the main `project_setup` script from the root directory. If you ever change dependencies or pull new code, it is recommended to run the setup script again.

Once the setup is complete:

1.  **Navigate to this app's directory:**

    ```bash
    cd apps/todo-app
    ```

2.  **Run the development servers (requires two separate terminals):**

    -   **Terminal 1 (CSS Watcher):**
        This command watches for changes in your Tailwind CSS files and rebuilds the stylesheet automatically.
        ```bash
        npm run watch
        ```

    -   **Terminal 2 (FastAPI Server):**
        This command starts the Python backend server with live reloading. `uv run` handles the virtual environment automatically.
        ```bash
        uv run uvicorn src.todo_app.main:app --reload
        ```

3.  **Open the app in your browser:**
    Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

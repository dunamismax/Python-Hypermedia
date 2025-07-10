# To-Do App

This application is a simple and interactive To-Do list manager built with **The Python Hypermedia Stack**. It uses FastAPI for the backend and HTMX to create a smooth, single-page user experience without writing complex JavaScript.

The primary purpose of this app is to demonstrate a modern, server-side rendering approach to building fundamental CRUD (Create, Read, Update, Delete) applications.

## How It Works

The application starts a FastAPI server that renders a main HTML page using Jinja2 templates. All user interactions—such as adding, toggling, or deleting a To-Do item—are handled via HTMX. These actions send AJAX requests to the server, which processes the request, interacts with a local SQLite database, and returns a small HTML partial. HTMX then intelligently swaps this new HTML into the page, updating the UI instantly without a full page reload.

## How to Run This App

Before running, ensure you have completed the initial repository setup by running the main `project_setup` script from the root directory. If you ever change dependencies or pull new code, it is recommended to run the setup script again.

Once the setup is complete:

1. **Navigate to this app's directory:**

   ```bash
   cd apps/todo-app
   ```

2. **Apply database migrations:**

   ```bash
   invoke db-upgrade
   ```

3. **Run the development server:**

   This command will start the FastAPI backend server and the Tailwind CSS watcher concurrently.

   ```bash
   invoke dev
   ```

4. **Open the app in your browser:**
   Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Development Tasks

This project uses `invoke` to automate common development tasks. Here are the available commands:

*   `invoke dev`: Starts the development server with auto-reloading and the Tailwind CSS watcher.
*   `invoke db-migrate -m "<your migration message>"`: Creates a new database migration.
*   `invoke db-upgrade`: Applies the latest database migrations.
*   `invoke build-css`: Builds the Tailwind CSS assets.
*   `invoke format`: Formats the frontend code with Prettier.
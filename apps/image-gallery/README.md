# Image Gallery App

This application is a simple and modern image gallery designed to handle file uploads and display content dynamically. It is built with **The Python Hypermedia Stack**, showcasing how to manage multipart form data and server-side state with FastAPI and HTMX.

The primary purpose of this app is to demonstrate how to build an interactive, content-driven application that handles file uploads gracefully without requiring a full page refresh.

## How It Works

The application features an upload form that sends image data to a FastAPI backend. The server saves the image file to a local `uploads/` directory and creates a corresponding record in a SQLite database. After a successful upload, the server re-renders the image gallery partial and sends the new HTML back to the client. HTMX receives this response and updates the gallery section of the page, making the newly uploaded image appear instantly.

## How to Run This App

This app is managed by the central `project_setup` script in the repository's `scripts/` directory.

1.  **Run the main setup script** from `scripts/project_setup` to install all dependencies and create the virtual environment for this app.

2.  **Navigate to this app's directory:**
    ```bash
    cd apps/image-gallery
    ```

3.  **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```

4.  **Run the development servers (requires two separate terminals):**

    - **Terminal 1 (CSS Watcher):**
      ```bash
      npm run watch
      ```

    - **Terminal 2 (FastAPI Server):**
      ```bash
      uvicorn src.image_gallery.main:app --reload
      ```

### What You Get

Once the servers are running, you can access a fully functional image gallery in your browser at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**. You will be able to upload images and see them appear in the gallery immediately.

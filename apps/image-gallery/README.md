# Image Gallery App

This application is a simple and modern image gallery designed to handle file uploads and display content dynamically. It is built with **The Python Hypermedia Stack**, showcasing how to manage multipart form data and server-side state with FastAPI and HTMX.

The primary purpose of this app is to demonstrate how to build an interactive, content-driven application that handles file uploads gracefully without requiring a full page refresh.

## How It Works

The application features an upload form that sends image data to a FastAPI backend. The server saves the image file to a local `uploads/` directory and creates a corresponding record in a SQLite database. After a successful upload, the server re-renders the image gallery partial and sends the new HTML back to the client. HTMX receives this response and updates the gallery section of the page, making the newly uploaded image appear instantly.

## How to Run This App

You can run the application by following the steps below.

1. **Navigate to the app directory:**

   ```bash
   cd apps/image-gallery
   ```

2. **Set up the environment and install dependencies:**

   ```bash
   # Create and activate a virtual environment
   uv venv
   source .venv/bin/activate

   # Install Python and Node.js packages
   uv pip sync pyproject.toml
   npm install
   ```

3. **Run the development servers:**
   You will need two separate terminals running in this directory.

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

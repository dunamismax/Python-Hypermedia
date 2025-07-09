import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from image_gallery.database import create_db_and_tables
from image_gallery.routers import router

# Define the directory for storing uploaded images
UPLOAD_DIRECTORY = "apps/image-gallery/uploads"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # On startup, create the database and tables
    print("Creating database and tables...")
    create_db_and_tables()
    # Also ensure the upload directory exists
    os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)
    yield
    # On shutdown
    print("Shutting down...")


app = FastAPI(
    title="Image Gallery App",
    description="A simple Image Gallery application with FastAPI and HTMX.",
    version="0.1.0",
    lifespan=lifespan,
)

# Mount the static files directory for CSS
app.mount(
    "/static",
    StaticFiles(directory="src/image_gallery/static"),
    name="static",
)

# Mount the uploads directory to be able to serve the images
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIRECTORY), name="uploads")


# Include the API routers
app.include_router(router)

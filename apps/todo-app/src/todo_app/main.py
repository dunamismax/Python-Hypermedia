from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .database import create_db_and_tables
from .routers import router


app = FastAPI(
    title="Todo App",
    description="A simple To-Do application with FastAPI and HTMX.",
    version="0.1.0",
)

# Mount the static files directory to serve CSS, JS, etc.
app.mount("/static", StaticFiles(directory="src/todo_app/static"), name="static")

# Include the API routers
app.include_router(router)

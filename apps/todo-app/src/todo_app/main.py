from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from todo_app.database import create_db_and_tables
from todo_app.routers import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # On startup, create the database and tables
    print("Creating database and tables...")
    create_db_and_tables()
    yield
    # On shutdown (not used here, but good practice)
    print("Shutting down...")


app = FastAPI(
    title="Todo App",
    description="A simple To-Do application with FastAPI and HTMX.",
    version="0.1.0",
    lifespan=lifespan,
)

# Mount the static files directory to serve CSS, JS, etc.
app.mount(
    "/static", StaticFiles(directory="src/todo_app/static"), name="static"
)

# Include the API routers
app.include_router(router)

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .database import engine
from .models import SQLModel
from .routers import router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # On startup, create the database and tables
    print("Creating database and tables...")
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
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
app.mount("/static", StaticFiles(directory="src/todo_app/static"), name="static")

# Include the API routers
app.include_router(router)


@app.get("/")
async def root() -> dict[str, str]:
    """
    Root endpoint to check if the API is running.
    """
    return {"message": "Hello World"}
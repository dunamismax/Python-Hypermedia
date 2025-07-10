from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from .database import engine
from .models import Todo

# Configure templates
templates = Jinja2Templates(directory="src/todo_app/templates")
router = APIRouter()


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency to get a new async database session for each request.
    Ensures the session is closed after the request is finished.
    """
    async with AsyncSession(engine) as session:
        yield session


@router.get("/", response_class=HTMLResponse)
async def get_all_todos(
    request: Request, session: Annotated[AsyncSession, Depends(get_session)]
) -> HTMLResponse:
    """
    Renders the main page with all To-Do items.
    """
    todos = await session.exec(select(Todo).order_by(Todo.id.asc()))
    return templates.TemplateResponse(
        "index.html", {"request": request, "todos": todos.all()}
    )


@router.post("/todos", response_class=HTMLResponse)
async def create_todo(
    request: Request,
    content: Annotated[str, Form()],
    session: Annotated[AsyncSession, Depends(get_session)],
) -> HTMLResponse:
    """
    Creates a new To-Do item and returns the updated list of todos.
    This endpoint is called by HTMX from the form submission.
    """
    # Create the new todo and add it to the database
    new_todo = Todo(content=content)
    session.add(new_todo)
    await session.commit()
    await session.refresh(new_todo)

    # Return the full list of todos to be swapped into the DOM
    todos = await session.exec(select(Todo).order_by(Todo.id.asc()))
    return templates.TemplateResponse(
        "partials/todos.html", {"request": request, "todos": todos.all()}
    )


@router.patch("/todos/{todo_id}", response_class=HTMLResponse)
async def toggle_todo(
    request: Request,
    todo_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
) -> HTMLResponse:
    """
    Toggles the completion status of a To-Do item.
    Returns the updated todo item partial to be swapped into the DOM.
    """
    todo = await session.get(Todo, todo_id)
    if todo:
        todo.is_completed = not todo.is_completed
        session.add(todo)
        await session.commit()
        await session.refresh(todo)

    return templates.TemplateResponse(
        "partials/todo_item.html", {"request": request, "todo": todo}
    )


@router.delete("/todos/{todo_id}", response_class=HTMLResponse)
async def delete_todo(
    todo_id: int, session: Annotated[AsyncSession, Depends(get_session)]
) -> HTMLResponse:
    """
    Deletes a To-Do item.
    Returns an empty response because HTMX will remove the element from the DOM.
    """
    todo = await session.get(Todo, todo_id)
    if todo:
        await session.delete(todo)
        await session.commit()

    # Return an empty response with a 200 status code
    return HTMLResponse(content="", status_code=200)
from typing import Annotated

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import desc, select
from sqlmodel.ext.asyncio.session import AsyncSession

from .database import get_session
from .models import Todo

# Configure templates
templates = Jinja2Templates(directory="src/todo_app/templates")
router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def get_all_todos(
    request: Request, session: Annotated[AsyncSession, Depends(get_session)]
) -> HTMLResponse:
    """
    Renders the main page with all To-Do items.
    """
    todos = await session.exec(select(Todo).order_by(desc(Todo.id)))
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
    Creates a new To-Do item and returns the new todo as an HTML partial.
    This endpoint is called by HTMX from the form submission.
    """
    if not content.strip():
        return HTMLResponse(
            content="<div class='error'>Todo content cannot be empty.</div>",
            status_code=400,
        )
    # Create the new todo and add it to the database
    new_todo = Todo(content=content)
    session.add(new_todo)
    await session.commit()
    await session.refresh(new_todo)

    # Return the new todo item to be appended to the list
    return templates.TemplateResponse(
        "partials/todo_item.html",
        {"request": request, "todo": new_todo},
        headers={"HX-Trigger": "todo-added"},
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
    if not todo:
        return HTMLResponse(content="Todo not found", status_code=404)

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
    if not todo:
        return HTMLResponse(content="Todo not found", status_code=404)

    await session.delete(todo)
    await session.commit()

    # Return an empty response with a 200 status code
    return HTMLResponse(content="", status_code=200)

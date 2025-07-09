import os
import shutil
from typing import Annotated

from fastapi import APIRouter, Depends, File, Form, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from image_gallery.database import engine
from image_gallery.models import Image

# Configure templates and upload directory
templates = Jinja2Templates(directory="src/image_gallery/templates")
router = APIRouter()
UPLOAD_DIRECTORY = "apps/image-gallery/uploads"


def get_session():
    """
    Dependency to get a new database session for each request.
    """
    with Session(engine) as session:
        yield session


@router.get("/", response_class=HTMLResponse)
def get_image_gallery(request: Request, session: Annotated[Session, Depends(get_session)]):
    """
    Renders the main page with the image gallery.
    """
    images = session.exec(select(Image).order_by(Image.id.desc())).all()
    return templates.TemplateResponse("index.html", {"request": request, "images": images})


@router.post("/upload", response_class=HTMLResponse)
async def upload_image(
    request: Request,
    title: Annotated[str, Form()],
    description: Annotated[str, Form()],
    file: Annotated[UploadFile, File()],
    session: Annotated[Session, Depends(get_session)],
):
    """
    Handles image upload, saves the file, adds it to the database,
    and returns the updated image gallery via HTMX.
    """
    # Ensure the upload directory exists
    os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

    # Save the uploaded file
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Create a new Image record in the database
    new_image = Image(title=title, description=description, filename=file.filename)
    session.add(new_image)
    session.commit()

    # Return the full gallery to be swapped into the DOM
    images = session.exec(select(Image).order_by(Image.id.desc())).all()
    return templates.TemplateResponse(
        "partials/gallery.html", {"request": request, "images": images}
    )

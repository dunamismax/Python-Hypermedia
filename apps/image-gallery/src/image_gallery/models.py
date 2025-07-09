from typing import Optional
from sqlmodel import Field, SQLModel


class Image(SQLModel, table=True):
    """
    Represents a single Image in the database.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    filename: str

from sqlmodel import Field, SQLModel


class Todo(SQLModel, table=True):
    """
    Represents a single To-Do item in the database.
    """

    id: int = Field(default=None, primary_key=True)
    content: str
    is_completed: bool = Field(default=False)

from sqlmodel import SQLModel, create_engine

# For simplicity, we'll use a local SQLite database.
# The file will be created in the same directory as this script.
DATABASE_URL = "sqlite:///todo_app.db"

# The connect_args are specific to SQLite to allow multiple threads to access the DB.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


def create_db_and_tables() -> None:
    """
    Creates the database and all tables defined by SQLModel metadata.
    This function should be called once when the application starts.
    """
    SQLModel.metadata.create_all(engine)

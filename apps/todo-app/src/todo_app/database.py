from sqlmodel import SQLModel, create_engine

# For simplicity, we'll use a local SQLite database.
# The file will be created in the same directory as this script.
DATABASE_URL = "sqlite:///todo_app.db"

# The connect_args are specific to SQLite to allow multiple threads to access the DB.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})




from sqlmodel import SQLModel, create_engine

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/todo_app"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
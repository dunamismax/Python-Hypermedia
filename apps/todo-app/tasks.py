from invoke import task

@task
def dev(c):
    """Run the development server."""
    c.run("uvicorn src.todo_app.main:app --reload", pty=True)

@task
def db_migrate(c, message):
    """Create a new database migration."""
    c.run(f"alembic -c src/alembic.ini revision --autogenerate -m \"{message}\"", pty=True)

@task
def db_upgrade(c):
    """Apply the latest database migrations."""
    c.run("alembic -c src/alembic.ini upgrade head", pty=True)

@task
def build_css(c):
    """Build the Tailwind CSS assets."""
    c.run("npm run build", pty=True)


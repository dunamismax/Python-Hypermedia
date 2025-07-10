from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlmodel.ext.asyncio.session import AsyncSession

from .config import settings

engine: AsyncEngine = create_async_engine(settings.database_url, echo=True)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(engine) as session:
        yield session

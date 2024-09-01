from typing import Generator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

from settings import settings

engine = create_async_engine(settings.database_url_asyncpg, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()


async def get_async_session() -> Generator:
    try:
        session: AsyncSession = async_session_maker()
        yield session
    finally:
        await session.close()
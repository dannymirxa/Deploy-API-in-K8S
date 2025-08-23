from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import text

from settings import app_env_settings as settings

class Database:
    """Manages asynchronous DB sessions with connection pooling."""

    def __init__(self) -> None:
        database_url = (
            f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
            f"@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
        )

        self.engine = create_async_engine(
            database_url,
            echo=True,
            future=True,
        )

    async def ping_database(self):
        try:
            async with self.engine.connect() as conn:
                await conn.execute(text("SELECT 1"))
            print("Successfully connected to the Database!")
        except Exception as e:
            print(f"Error connecting to database: {e}")
    
    @asynccontextmanager
    # any function decorated with @asynccontextmanager
    # internally becomes an async generator,
    # not a plain coroutine returning AsyncSession
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async_session = sessionmaker(self.engine, class_=AsyncSession)
        session = None
        try:
            session = async_session()
            async with session:
                yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()

    async def close_database(self) -> None:
        """Dispose of the database engine."""
        if self.engine:
            await self.engine.dispose()


base = declarative_base()
database = Database()

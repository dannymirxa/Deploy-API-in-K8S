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

    def __init__(self, database_url) -> None:
        self.database_url = database_url

        # echo=True allows SQL queries to be logged to the console, which is helpful during development, but should be False in production.
        # future=True ensures compatibility with SQLAlchemy 2.0-style code.

        self.engine = create_async_engine(
            self.database_url,
            echo=True,
            future=True,
        )

    # to check the database connection before any operations
    async def ping_database(self):
        try:
            async with self.engine.connect() as conn:
                await conn.execute(text("SELECT 1"))
            # print("Successfully connected to the Database!")
            return "connected"
        except Exception as e:
            # print(f"Error connecting to database: {e}")
            return "not connected"
    
    @asynccontextmanager
    # any function decorated with @asynccontextmanager
    # internally becomes an async generator,
    # not a plain coroutine returning AsyncSession

    # @asynccontextmanager is used to manage asynchronous resources (e.g database connections, network sockets) that needs the same setup and tear-down functionality.
    # we use sessionmaker to create sessions that serve as the interface to our database. With the sessionmaker, each request gets its own session, ensuring that database operations are isolated from each other.
    # async with ensures that sessions are used safely, allowing for automatic cleanup when the context is exited.
    # session.rollback() is called if an error occurs, ensuring that any partial changes are undone to maintain data consistency.
    # session.close() ensures that the session is closed after each transaction, freeing up resources for other operations.
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

# declarative_base is used to create the base class for our models. This base class will help in defining database tables later.
base = declarative_base()


database_url = (
            f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
            f"@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
        )
database = Database(database_url)
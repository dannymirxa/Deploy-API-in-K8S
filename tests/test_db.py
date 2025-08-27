import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest

from database import Database
from settings import app_env_settings_local_test as settings

# test connection to database
@pytest.mark.asyncio
async def test_ping_database():
    database_url = (
            f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
            f"@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
        )
    database = Database(database_url)
    result = await database.ping_database()
    assert result == "connected"

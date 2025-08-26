import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from database import Database
from settings import app_env_settings as settings

database = Database()

async def ping_database():
    result = await database.ping_database()
    assert result == "connected"
    print(result)

import asyncio

asyncio.run(ping_database())


import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest

from database import Database

@pytest.mark.asyncio
async def test_ping_database():
    database = Database()
    result = await database.ping_database()
    assert result == "connected"

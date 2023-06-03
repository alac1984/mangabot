import pytest
import asyncpg
from database import create_pool


@pytest.mark.asyncio
async def test_create_pool():
    connstr = 'postgresql://mangabot:a1k8u2@localhost:5433/mangabot'
    pool = await create_pool(connstr)

    # Assert if it is the right object
    assert isinstance(pool, asyncpg.pool.Pool)
    # Assert if it is connecting
    async with pool.acquire() as conn:
        result = await conn.fetchval('SELECT 1')
        assert result == 1

    await pool.close()


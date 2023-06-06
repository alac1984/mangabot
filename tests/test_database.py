import pytest
import asyncpg
from database import create_pool
from database import run_query


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


@pytest.mark.asyncio
async def test_run_query_select(pool):
    query = "SELECT $1"
    result = await run_query(pool, query, "1")

    assert isinstance(result, asyncpg.Record)
    assert result[0] == '1'

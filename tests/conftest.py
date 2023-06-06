import pytest_asyncio
import asyncpg


@pytest_asyncio.fixture(scope='function')
async def pool():
    connstr = 'postgresql://mangabot:a1k8u2@localhost:5433/mangabot'
    pool = await asyncpg.create_pool(connstr)

    yield pool
    await pool.close()

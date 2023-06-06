# mypy: disable-error-code="assignment"

import asyncpg
from typing import Optional, Any


async def create_pool(connstr: str):
    pool = await asyncpg.create_pool(connstr)

    return pool


async def run_query(pool: asyncpg.pool.Pool, query: str, *args) -> Optional[Any]:
    async with pool.acquire() as conn:
        return await conn.fetchrow(query, *args)


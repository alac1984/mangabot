import asyncpg


async def create_pool(connstr: str):
    pool = await asyncpg.create_pool(connstr)
    return pool

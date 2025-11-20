import os
import asyncpg

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgres://raguser:changeme@postgres:5432/cnt_hub"  # pravi url dolazi iz docker-compose
)

async def get_connection():
    return await asyncpg.connect(DATABASE_URL)

from db import get_connection  # <-- OVO je bitno, bez tačke

async def db_conn():
    conn = await get_connection()
    try:
        yield conn
    finally:
        await conn.close()

from fastapi import APIRouter, Depends, HTTPException
from typing import List

from deps import db_conn
from models import Workshop, WorkshopIn

router = APIRouter(prefix="/api/workshops", tags=["workshops"])


@router.get("", response_model=List[Workshop])
async def list_workshops(conn = Depends(db_conn)):
    rows = await conn.fetch(
        """
        SELECT id, title, description, date
        FROM workshops
        ORDER BY date DESC
        """
    )
    return [Workshop(**dict(r)) for r in rows]


@router.post("", response_model=Workshop)
async def create_workshop(workshop: WorkshopIn, conn = Depends(db_conn)):
    row = await conn.fetchrow(
        """
        INSERT INTO workshops (title, description, date)
        VALUES ($1, $2, $3)
        RETURNING id, title, description, date
        """,
        workshop.title,
        workshop.description,
        workshop.date,
    )
    if not row:
        raise HTTPException(status_code=500, detail="Failed to create workshop")
    return Workshop(**dict(row))

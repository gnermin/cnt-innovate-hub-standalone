from fastapi import APIRouter, Depends, HTTPException
from typing import List

from deps import db_conn
from models import Event, EventIn

router = APIRouter(prefix="/api/events", tags=["events"])

@router.get("", response_model=List[Event])
async def list_events(conn = Depends(db_conn)):
    rows = await conn.fetch(
        """
        SELECT id, title, description, start_date, end_date
        FROM events
        ORDER BY start_date DESC
        """
    )
    return [Event(**dict(r)) for r in rows]


@router.post("", response_model=Event)
async def create_event(event: EventIn, conn = Depends(db_conn)):
    row = await conn.fetchrow(
        """
        INSERT INTO events (title, description, start_date, end_date)
        VALUES ($1, $2, $3, $4)
        RETURNING id, title, description, start_date, end_date
        """,
        event.title,
        event.description,
        event.start_date,
        event.end_date,
    )
    if not row:
        raise HTTPException(status_code=500, detail="Failed to create event")
    return Event(**dict(row))

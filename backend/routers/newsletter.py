from fastapi import APIRouter, Depends, HTTPException
from typing import List

from deps import db_conn
from models import NewsletterSubscriber, NewsletterSubscriberIn

router = APIRouter(prefix="/api/newsletter", tags=["newsletter"])


@router.get("", response_model=List[NewsletterSubscriber])
async def list_subscribers(conn = Depends(db_conn)):
    rows = await conn.fetch(
        """
        SELECT id, email, created_at
        FROM newsletter_subscribers
        ORDER BY created_at DESC
        """
    )
    return [NewsletterSubscriber(**dict(r)) for r in rows]


@router.post("", response_model=NewsletterSubscriber)
async def subscribe(sub: NewsletterSubscriberIn, conn = Depends(db_conn)):
    row = await conn.fetchrow(
        """
        INSERT INTO newsletter_subscribers (email)
        VALUES ($1)
        RETURNING id, email, created_at
        """,
        sub.email,
    )
    if not row:
        raise HTTPException(status_code=500, detail="Failed to subscribe")
    return NewsletterSubscriber(**dict(row))

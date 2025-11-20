from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, date

class EventIn(BaseModel):
    title: str
    description: Optional[str] = None
    start_date: date
    end_date: Optional[date] = None

class Event(EventIn):
    id: int

class WorkshopIn(BaseModel):
    title: str
    description: Optional[str] = None
    date: date

class Workshop(WorkshopIn):
    id: int

class NewsletterSubscriberIn(BaseModel):
    email: EmailStr

class NewsletterSubscriber(NewsletterSubscriberIn):
    id: int
    created_at: datetime

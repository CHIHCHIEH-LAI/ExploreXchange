from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

from TripService.src.models.event import Event

class Trip(BaseModel):
    _id: Optional[str]
    title: str
    start_time: datetime
    end_time: datetime
    location: Optional[str] = ''
    description: Optional[str] = ''
    email: EmailStr
    public: Optional[bool] = False
    events: List[Event]
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from app.models.event import Event

class Trip(BaseModel):
    title: str
    start_time: datetime
    end_time: datetime
    location: Optional[str] = ''
    description: Optional[str] = ''
    owner: str
    events: List[Event]
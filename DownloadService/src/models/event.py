from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Event(BaseModel):
    title: str
    start_time: datetime
    end_time: datetime
    location: Optional[str] = ''
    description: Optional[str] = ''
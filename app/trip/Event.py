from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    title: str
    start_time: datetime
    end_time: datetime
    timezone: str
    location: str
    description: str
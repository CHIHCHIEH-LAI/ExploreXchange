from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from src.models.event import Event

class Trip(BaseModel):
    title: str
    start_time: datetime
    end_time: datetime
    location: Optional[str] = ''
    description: Optional[str] = ''
    owner: str = ''
    public: Optional[bool] = False
    events: List[Event]

    def update_owner(self, email):
        self.owner = email
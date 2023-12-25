from pydantic import BaseModel
from typing import List

from app.trip.Event import Event

class Trip(BaseModel):
    trip_name: str
    events: List[Event]
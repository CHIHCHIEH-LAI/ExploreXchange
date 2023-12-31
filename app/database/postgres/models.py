from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

class EventTripLink(SQLModel, table=True):
    event_id: Optional[int] = Field(
        default=None, foreign_key="event.id", primary_key=True
    )
    trip_id: Optional[int] = Field(
        default=None, foreign_key="trip.id", primary_key=True
    )


class Trip(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    start_time: datetime
    end_time: datetime
    location: Optional[str]
    description: Optional[str]
    owner: str = Field(index=True)

    events: List["Event"] = Relationship(back_populates="trips", link_model=EventTripLink)


class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    start_time: datetime
    end_time: datetime
    location: Optional[str]
    description: Optional[str]
    owner: str = Field(index=True)

    trips: List[Trip] = Relationship(back_populates="events", link_model=EventTripLink)
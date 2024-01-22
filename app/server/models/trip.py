from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime

from server.models.event import EventSchema

class TripSchema(BaseModel):
    title: str = Field(...)
    start_time: datetime = Field(...)
    end_time: datetime = Field(...)
    location: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    email: EmailStr = Field(...)
    public: Optional[bool] = Field(False)
    events: List[EventSchema] = []

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Sample Trip",
                "start_time": "2022-03-01T09:00:00",
                "end_time": "2022-03-01T17:00:00",
                "location": "123 Sample St",
                "description": "This is a sample trip",
                "email": "sample@example.com",
                "public": False,
                "events": [
                    {
                        "title": "Sample Event",
                        "start_time": "2022-03-01T09:00:00",
                        "end_time": "2022-03-01T10:00:00",
                        "location": "123 Sample St",
                        "description": "This is a sample event",
                    }
                ],
            }
        }

class UpdateTripModel(BaseModel):
    title: Optional[str]
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    location: Optional[str]
    description: Optional[str]
    email: Optional[EmailStr]
    public: Optional[bool]
    events: Optional[List[EventSchema]]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Updated Sample Trip",
                "start_time": "2022-03-02T09:00:00",
                "end_time": "2022-03-02T17:00:00",
                "location": "456 Updated St",
                "description": "This is an updated sample trip",
                "email": "updated_sample@example.com",
                "public": True,
                "events": [
                    {
                        "title": "Updated Sample Event",
                        "start_time": "2022-03-02T09:00:00",
                        "end_time": "2022-03-02T10:00:00",
                        "location": "456 Updated St",
                        "description": "This is an updated sample event",
                    }
                ],
            }
        }


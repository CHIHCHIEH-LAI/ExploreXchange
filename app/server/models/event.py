from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class EventSchema(BaseModel):
    title: str = Field(...)
    start_time: datetime = Field(...)
    end_time: datetime = Field(...)
    location: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = Field(None, max_length=500)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Sample Event",
                "start_time": "2022-03-01T09:00:00",
                "end_time": "2022-03-01T17:00:00",
                "location": "123 Sample St",
                "description": "This is a sample event",
            }
        }
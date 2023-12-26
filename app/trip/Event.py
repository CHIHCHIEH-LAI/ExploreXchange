from pydantic import BaseModel

class Event(BaseModel):
    title: str
    start_time: str
    end_time: str
    location: str
    description: str
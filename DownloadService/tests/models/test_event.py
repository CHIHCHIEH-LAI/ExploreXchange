import pytest

from datetime import datetime
from pydantic import ValidationError
from src.models.event import Event

def test_create_event_with_valid_data():
    event = Event(
        title="Sample Event",
        start_time=datetime(2024, 1, 1, 10, 0),
        end_time=datetime(2024, 1, 1, 12, 0),
        location="New York",
        description="This is a sample event."
    )
    
    assert event.title == "Sample Event"
    assert event.start_time == datetime(2024, 1, 1, 10, 0)
    assert event.end_time == datetime(2024, 1, 1, 12, 0)
    assert event.location == "New York"
    assert event.description == "This is a sample event."

def test_create_event_with_invalid_data():
    with pytest.raises(ValidationError):
        Event(
            title="Invalid Event",
            start_time="not a datetime",
            end_time=datetime(2024, 1, 1, 12, 0)
        )
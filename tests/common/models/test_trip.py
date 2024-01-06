import pytest
from datetime import datetime
from pydantic import ValidationError
from app.common.models.trip import Trip
from app.common.models.event import Event

def create_sample_event(title="Sample Event", owner="user123"):
    return Event(
        title=title,
        start_time=datetime(2024, 1, 1, 10, 0),
        end_time=datetime(2024, 1, 1, 12, 0),
        location="New York",
        description="This is a sample event.",
        owner=owner
    )

def test_create_trip_with_valid_data():
    trip = Trip(
        title="Adventure Trip",
        start_time=datetime(2024, 1, 10, 8, 0),
        end_time=datetime(2024, 1, 15, 18, 0),
        location="Mount Everest",
        description="Exciting adventure trip to Everest.",
        owner="user456",
        public=True,
        events=[create_sample_event(), create_sample_event(title="Another Event")]
    )

    assert trip.title == "Adventure Trip"
    assert trip.start_time == datetime(2024, 1, 10, 8, 0)
    assert trip.end_time == datetime(2024, 1, 15, 18, 0)
    assert trip.location == "Mount Everest"
    assert trip.description == "Exciting adventure trip to Everest."
    assert trip.owner == "user456"
    assert trip.public is True
    assert len(trip.events) == 2
    assert trip.events[0].title == "Sample Event"
    assert trip.events[1].title == "Another Event"

def test_create_trip_with_invalid_event_data():
    with pytest.raises(ValidationError):
        Trip(
            title="Faulty Trip",
            start_time=datetime(2024, 1, 10, 8, 0),
            end_time=datetime(2024, 1, 15, 18, 0),
            owner="user456",
            events=[create_sample_event(), Event(title="Invalid Event", start_time="not a datetime", end_time=datetime(2024, 1, 2, 12, 0), owner="user789")]
        )
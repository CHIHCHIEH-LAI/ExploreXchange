import pytest

from datetime import datetime
import ics

from src.models.event import Event
from src.models.trip import Trip
from src.utils.trip_to_ics_converter import TripToICSConverter

def create_sample_event(title="Sample Event"):
    return Event(
        title=title,
        start_time=datetime(2024, 1, 1, 10, 0),
        end_time=datetime(2024, 1, 1, 12, 0),
        location="New York",
        description="This is a sample event."
    )

def create_sample_trip():
    return Trip(
        title="Adventure Trip",
        start_time=datetime(2024, 1, 10, 8, 0),
        end_time=datetime(2024, 1, 15, 18, 0),
        location="Mount Everest",
        description="Exciting adventure trip to Everest.",
        owner="user123",
        public=True,
        events=[create_sample_event(), create_sample_event(title="Another Event")]
    )

def test_convert():
    mock_trip = create_sample_trip()
    calendar = TripToICSConverter.convert(mock_trip)

    assert isinstance(calendar, ics.Calendar)
    assert len(calendar.events) == len(mock_trip.events)
    for ics_event, mock_event in zip(calendar.events, mock_trip.events):
        assert ics_event.name == mock_event.title
        assert datetime.fromisoformat(str(ics_event.begin)) == mock_event.start_time
        assert datetime.fromisoformat(str(ics_event.end)) == mock_event.end_time
        assert ics_event.location == mock_event.location
        assert ics_event.description == mock_event.description
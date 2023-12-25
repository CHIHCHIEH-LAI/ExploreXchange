from datetime import datetime
import pytest

from app.trip.Event import Event

def test_valid_event():
    event_data = {
        "title": "Sample Event",
        "start_time": datetime(2023, 1, 1, 12, 0),
        "end_time": datetime(2023, 1, 1, 14, 0),
        "timezone": "UTC",
        "location": "Sample Location",
        "description": "Sample Description",
    }
    event = Event(**event_data)
    assert event.title == "Sample Event"
    assert event.start_time == datetime(2023, 1, 1, 12, 0)
    assert event.end_time == datetime(2023, 1, 1, 14, 0)
    assert event.timezone == "UTC"
    assert event.location == "Sample Location"
    assert event.description == "Sample Description"

def test_event_missing_title():
    with pytest.raises(ValueError):
        event_data = {
            "start_time": datetime(2023, 1, 1, 12, 0),
            "end_time": datetime(2023, 1, 1, 14, 0),
            "timezone": "UTC",
            "location": "Sample Location",
            "description": "Sample Description",
        }
        event = Event(**event_data)

def test_event_missing_start_time():
    with pytest.raises(ValueError):
        event_data = {
            "title": "Sample Event",
            "end_time": datetime(2023, 1, 1, 14, 0),
            "timezone": "UTC",
            "location": "Sample Location",
            "description": "Sample Description",
        }
        event = Event(**event_data)

def test_event_missing_end_time():
    with pytest.raises(ValueError):
        event_data = {
            "title": "Sample Event",
            "start_time": datetime(2023, 1, 1, 12, 0),
            "timezone": "UTC",
            "location": "Sample Location",
            "description": "Sample Description",
        }
        event = Event(**event_data)

def test_event_missing_timezone():
    with pytest.raises(ValueError):
        event_data = {
            "title": "Sample Event",
            "start_time": datetime(2023, 1, 1, 12, 0),
            "end_time": datetime(2023, 1, 1, 14, 0),
            "location": "Sample Location",
            "description": "Sample Description",
        }
        event = Event(**event_data)

def test_event_missing_location():
    with pytest.raises(ValueError):
        event_data = {
            "title": "Sample Event",
            "start_time": datetime(2023, 1, 1, 12, 0),
            "end_time": datetime(2023, 1, 1, 14, 0),
            "timezone": "UTC",
            "description": "Sample Description",
        }
        event = Event(**event_data)

def test_event_missing_description():
    with pytest.raises(ValueError):
        event_data = {
            "title": "Sample Event",
            "start_time": datetime(2023, 1, 1, 12, 0),
            "end_time": datetime(2023, 1, 1, 14, 0),
            "timezone": "UTC",
            "location": "Sample Location",
        }
        event = Event(**event_data)
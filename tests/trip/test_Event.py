from datetime import datetime
import pytest

from app.trip.Event import Event

@pytest.fixture
def generated_event_data():
    event_data = {
        "title": "Sample Event",
        "start_time": datetime(2023, 1, 1, 12, 0),
        "end_time": datetime(2023, 1, 1, 14, 0),
        "timezone": "UTC",
        "location": "Sample Location",
        "description": "Sample Description",
    }
    return event_data

def test_valid_event(generated_event_data):
    
    event = Event(**generated_event_data)
    assert event.title == "Sample Event"
    assert event.start_time == datetime(2023, 1, 1, 12, 0)
    assert event.end_time == datetime(2023, 1, 1, 14, 0)
    assert event.timezone == "UTC"
    assert event.location == "Sample Location"
    assert event.description == "Sample Description"

def test_event_missing_title(generated_event_data):
    del generated_event_data["title"]
    with pytest.raises(ValueError):
        event = Event(**generated_event_data)

def test_event_missing_start_time(generated_event_data):
    del generated_event_data["start_time"]
    with pytest.raises(ValueError):
        event = Event(**generated_event_data)

def test_event_missing_end_time(generated_event_data):
    del generated_event_data["end_time"]
    with pytest.raises(ValueError):
        event = Event(**generated_event_data)

def test_event_missing_timezone(generated_event_data):
    del generated_event_data["timezone"]
    with pytest.raises(ValueError):
        event = Event(**generated_event_data)

def test_event_missing_location(generated_event_data):
    del generated_event_data["location"]
    with pytest.raises(ValueError):
        event = Event(**generated_event_data)

def test_event_missing_description(generated_event_data):
    del generated_event_data["description"]
    with pytest.raises(ValueError):
        event = Event(**generated_event_data)
from datetime import datetime
import pytest

from app.trip.Trip import Trip
from app.trip.Event import Event

def test_valid_trip():
    event_data1 = {
        "title": "Event 1",
        "start_time": datetime(2023, 1, 1, 12, 0),
        "end_time": datetime(2023, 1, 1, 14, 0),
        "timezone": "UTC",
        "location": "Location 1",
        "description": "Description 1",
    }
    
    event_data2 = {
        "title": "Event 2",
        "start_time": datetime(2023, 1, 2, 12, 0),
        "end_time": datetime(2023, 1, 2, 14, 0),
        "timezone": "UTC",
        "location": "Location 2",
        "description": "Description 2",
    }
    
    trip_data = {
        "trip_name": "Sample Trip",
        "events": [Event(**event_data1), Event(**event_data2)]
    }
    
    trip = Trip(**trip_data)
    
    assert trip.trip_name == "Sample Trip"
    assert len(trip.events) == 2

def test_trip_missing_trip_name():
    with pytest.raises(ValueError):
        event_data1 = {
            "title": "Event 1",
            "start_time": datetime(2023, 1, 1, 12, 0),
            "end_time": datetime(2023, 1, 1, 14, 0),
            "timezone": "UTC",
            "location": "Location 1",
            "description": "Description 1",
        }
        
        event_data2 = {
            "title": "Event 2",
            "start_time": datetime(2023, 1, 2, 12, 0),
            "end_time": datetime(2023, 1, 2, 14, 0),
            "timezone": "UTC",
            "location": "Location 2",
            "description": "Description 2",
        }
        
        trip_data = {
            "events": [Event(**event_data1), Event(**event_data2)]
        }
        
        trip = Trip(**trip_data)

def test_trip_missing_events():
    with pytest.raises(ValueError):
        trip_data = {
            "trip_name": "Sample Trip",
        }
        trip = Trip(**trip_data)

def test_events_invalid_types():
    with pytest.raises(ValueError):
        trip_data = {
            "trip_name": "Sample Trip",
            "events": "Invalid Data Type"
        }
        trip = Trip(**trip_data)

import pytest

from app.trip.Trip import Trip

def test_valid_trip():
    trip_data = {
        "trip_name": "Sample Trip",
        "events": [
            {
                "title": "Event 1",
                "start_time": "2023-01-01T12:00:00Z",
                "end_time": "2023-01-01T14:00:00Z",
                "location": "Location 1",
                "description": "Description 1",
            },
            {
                "title": "Event 2",
                "start_time": "2023-01-02T12:00:00Z",
                "end_time": "2023-01-02T14:00:00Z",
                "location": "Location 2",
                "description": "Description 2",
            }
        ]
    }
    trip = Trip(**trip_data)
    
    assert trip.trip_name == "Sample Trip"
    assert len(trip.events) == 2

def test_trip_missing_trip_name():
    with pytest.raises(ValueError):
        trip_data = {
            "events": [
                {
                    "title": "Event 1",
                    "start_time": "2023-01-01T12:00:00Z",
                    "end_time": "2023-01-01T14:00:00Z",
                    "timezone": "UTC",
                    "location": "Location 1",
                    "description": "Description 1",
                },
                {
                    "title": "Event 2",
                    "start_time": "2023-01-02T12:00:00Z",
                    "end_time": "2023-01-02T14:00:00Z",
                    "timezone": "UTC",
                    "location": "Location 2",
                    "description": "Description 2",
                }
            ]
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

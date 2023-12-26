import pytest
from datetime import datetime
import os

from app.trip.Event import Event
from app.trip.Trip import Trip
from app.trip.ICSGenerator import ICSGenerator

@pytest.fixture
def ics_generator():
    return ICSGenerator()

@pytest.fixture
def generated_ics_file(ics_generator):
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

    ics_file_name = ics_generator.generate_ics(trip)

    yield ics_file_name

    # Define a finalizer function to delete the file
    if os.path.exists(ics_file_name):
        os.remove(ics_file_name)

def test_generated_ics_file_exists(generated_ics_file):
    assert os.path.exists(generated_ics_file)

def test_generated_ics_file_content(generated_ics_file):
    with open(generated_ics_file, 'r') as file:
        content = file.read()
        assert "BEGIN:VCALENDAR" in content
        assert "BEGIN:VEVENT" in content
        assert "END:VCALENDAR" in content
        assert "END:VEVENT" in content


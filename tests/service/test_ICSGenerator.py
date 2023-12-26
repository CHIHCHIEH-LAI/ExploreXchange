import pytest
import os

from app.trip.Trip import Trip
from app.service.ICSGenerator import ICSGenerator
from app.service import config

@pytest.fixture
def ics_generator():
    return ICSGenerator()

@pytest.fixture
def generated_ics_file(ics_generator):
    trip_data = {
        "trip_name": "Sample Trip",
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

    ics_file_name = ics_generator.generate_ics(trip)
    ics_file_path = os.path.join(config.ICS_DIR_PATH, ics_file_name)

    yield ics_file_path

    # Define a finalizer function to delete the file
    if os.path.exists(ics_file_path):
        os.remove(ics_file_path)

def test_generated_ics_file_exists(generated_ics_file):
    assert os.path.exists(generated_ics_file)

def test_generated_ics_file_content(generated_ics_file):
    with open(generated_ics_file, 'r') as file:
        content = file.read()
        assert "BEGIN:VCALENDAR" in content
        assert "BEGIN:VEVENT" in content
        assert "END:VCALENDAR" in content
        assert "END:VEVENT" in content


import pytest
import os

from fastapi.testclient import TestClient

from main import app
from tests.service.config import ICS_DIR_PATH

client = TestClient(app)

@pytest.fixture
def generated_ics_file():
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
    
    response = client.post("/trip/generate_ics", json=trip_data)

    yield response

    # with open("generated_event.ics", "wb") as f:
    #     f.write(response.content)

    # cleanup_generated_files()

def test_status_code(generated_ics_file):
    assert generated_ics_file.status_code == 200

def test_content_exists(generated_ics_file):
    assert generated_ics_file.content is not None
    
def test_content_download(generated_ics_file):
    ics_file_path = os.path.join(ICS_DIR_PATH, "Sample_Trip.ics")
    with open(ics_file_path, "wb") as f:
        f.write(generated_ics_file.content)
    
    assert os.path.exists(ics_file_path)

    os.remove(ics_file_path)
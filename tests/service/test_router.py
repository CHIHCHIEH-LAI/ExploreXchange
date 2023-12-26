import pytest
from datetime import datetime

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_generate_ics():
    trip_data = {
        "trip_name": "Test Trip",
        "events": [
            {
                "title": "Event 1",
                "start_time": datetime(2023, 1, 1, 12, 0),
                "end_time": datetime(2023, 1, 1, 14, 0),
                "timezone": "UTC",
                "location": "Test Location",
                "description": "Test Description"
            },
            {
                "title": "Event 1",
                "start_time": datetime(2023, 1, 2, 12, 0),
                "end_time": datetime(2023, 1, 2, 14, 0),
                "timezone": "UTC",
                "location": "Test Location",
                "description": "Test Description"
            }
        ]
    }
    
    response = client.post("/trip/generate_ics", json=trip_data)

    assert response.status_code == 200

    assert response.headers["content-type"] == "text/calendar"

    # cleanup_generated_files()

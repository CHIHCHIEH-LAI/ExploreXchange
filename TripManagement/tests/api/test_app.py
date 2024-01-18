import pytest

import os
from fastapi.testclient import TestClient

from TripManagement.src.api.app import app

client = TestClient(app)

def test_clean_collection():
    response = client.delete('trips/clean-collection')
    assert response.status_code == 200
    assert response.json() == {"message": "Successfully cleaned trip collection"}
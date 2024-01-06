import pytest

from app.trip_service.dependencies import get_trip_collection_manager

def test_get_trip_collection_manager():
    try:
        tripMgr = get_trip_collection_manager()
    except Exception as e:
        assert False, f"An error occurred while getting trip collection manager: {e}"
    
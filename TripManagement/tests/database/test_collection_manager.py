import pytest
from datetime import datetime

from src.models.event import Event
from src.models.trip import Trip

from TripManagement.src.database.collection_manager import CollectionManager
from TripManagement.config import MONGODB_URI, DATABASE_NAME, COLLECTION_NAME

def get_collection_manager():
    colMgr = CollectionManager(
        uri = MONGODB_URI,
        db_name = DATABASE_NAME,
        collection_name = COLLECTION_NAME
    )
    return colMgr

def test_collection_connection():
    colMgr = get_collection_manager()
    try:
        colMgr.connect()
    except Exception as e:
        assert False, f"An error occurred while connecting to MongoDB: {e}"

def create_sample_event(title="Sample Event"):
    return Event(
        title=title,
        start_time=datetime(2024, 1, 1, 10, 0),
        end_time=datetime(2024, 1, 1, 12, 0),
        location="New York",
        description="This is a sample event."
    )

def create_sample_trip():
    return Trip(
        title="Adventure Trip",
        start_time=datetime(2024, 1, 10, 8, 0),
        end_time=datetime(2024, 1, 15, 18, 0),
        location="Mount Everest",
        description="Exciting adventure trip to Everest.",
        owner="user123",
        public=True,
        events=[create_sample_event(), create_sample_event(title="Another Event")]
    )

def test_create_trip():
    colMgr = get_collection_manager()
    colMgr.connect()
    trip = create_sample_trip()
    try:
        colMgr.create_trip(trip)
    except Exception as e:
        assert False, f"An error occurred while creating trip to MongoDB: {e}"
    colMgr.clean_collection()

def test_clean_collection():
    colMgr = get_collection_manager()
    colMgr.connect()
    try:
        res = colMgr.clean_collection()
        if not res:
            assert False, "Cleaned Unsuccessfully"
    except Exception as e:
        assert False, f"An error occurred while cleaning trip collection: {e}"

def test_query_trip_by_id():
    colMgr = get_collection_manager()
    colMgr.connect()
    trip = create_sample_trip()
    trip_id = colMgr.create_trip(trip)
    query_result = colMgr.query_trip_by_id(trip_id)
    assert query_result.title == trip.title
    colMgr.clean_collection()

def test_delete_trip_by_id():
    colMgr = get_collection_manager()
    colMgr.connect()
    trip = create_sample_trip()
    trip_id = colMgr.create_trip(trip)
    res = colMgr.delete_trip_by_id(trip_id)
    assert res == 1
    query_result = colMgr.query_trip_by_id(trip_id)
    assert query_result == None
    colMgr.clean_collection()



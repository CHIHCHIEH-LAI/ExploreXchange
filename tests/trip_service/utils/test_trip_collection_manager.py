import pytest
from datetime import datetime

from app.common.models.event import Event
from app.common.models.trip import Trip
from app.trip_service.config import MONGODB_URI, DATABASE, TRIPS_COLLECTION
from app.database.mongo.database_manager import DatabaseManager
from app.trip_service.utils.trip_collection_manager import TripCollectionManager

def get_trip_collection_manager():
    dbMgr = DatabaseManager(MONGODB_URI, DATABASE)
    colMgr = TripCollectionManager(dbMgr, TRIPS_COLLECTION)
    return colMgr

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
    tripMgr = get_trip_collection_manager()
    trip = create_sample_trip()
    try:
        tripMgr.create_trip(trip)
    except Exception as e:
        assert False, f"An error occurred while creating trip to MongoDB: {e}"

# docs = colMgr.query_all_trips_of_owner('Alice')
# print(docs)
# doc = colMgr.query_trip_by_id('65915d3abd6eb1e6ae071420')
# trip = Trip(**doc)
# print(trip)
# colMgr.delete_trip_by_id('65915d3abd6eb1e6ae071420')
# colMgr.clean_collection('trips')
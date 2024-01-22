import pytest
from datetime import datetime
from TripService.src.models.event import Event
from TripService.src.models.trip import Trip
from TripService.src.database.collection_manager import CollectionManager
from TripService.config import MONGO_DETAILS, DATABASE_NAME, COLLECTION_NAME

def get_collection_manager():
    colMgr = CollectionManager(
        uri = MONGO_DETAILS,
        db_name = DATABASE_NAME,
        collection_name = COLLECTION_NAME
    )
    return colMgr

def test_collection_connection():
    try:
        get_collection_manager().connect()
        get_collection_manager().disconnect()
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
        email="user123@example.com",
        public=True,
        events=[create_sample_event(), create_sample_event(title="Another Event")]
    )

def test_create_trip():
    colMgr = get_collection_manager()
    colMgr.connect()
    trip = create_sample_trip()
    try:
        result = colMgr.create_trip(trip)
        assert result is not None
        print(result)
    except Exception as e:
        assert False, f"An error occurred while creating a trip: {e}"
    finally:
        colMgr.disconnect()

# async def test_delete_trip_by_id():
#     colMgr = get_collection_manager()
#     await colMgr.connect()
#     trip = create_sample_trip()
#     try:
#         created_trip = await colMgr.create_trip(trip)
#         result = await colMgr.delete_trip_by_id(str(created_trip.id))
#         assert result is True
#     except Exception as e:
#         assert False, f"An error occurred while deleting a trip: {e}"
#     finally:
#         await colMgr.disconnect()

# async def test_retrieve_all_trips_by_email():
#     colMgr = get_collection_manager()
#     await colMgr.connect()
#     trip = create_sample_trip()
#     try:
#         await colMgr.create_trip(trip)
#         result = await colMgr.retrieve_all_trips_by_email(trip.owner)
#         assert len(result) > 0
#     except Exception as e:
#         assert False, f"An error occurred while retrieving trips by email: {e}"
#     finally:
#         await colMgr.disconnect()

# async def test_delete_all_trips_by_email():
#     colMgr = get_collection_manager()
#     await colMgr.connect()
#     trip = create_sample_trip()
#     try:
#         await colMgr.create_trip(trip)
#         result = await colMgr.delete_all_trips_by_email(trip.owner)
#         assert result is True
#     except Exception as e:
#         assert False, f"An error occurred while deleting all trips by email: {e}"
#     finally:
#         await colMgr.disconnect()
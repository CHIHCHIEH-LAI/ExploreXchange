from pymongo import MongoClient

from app.models.Trip import Trip

class DatabaseManager:
    def __init__(self, uri, db):
        client = MongoClient(uri)
        self.db = client[db]

    def execute_query(self, collection, pipeline):
        collection = self.db[collection]
        result = collection.aggregate(pipeline)
        return result
    
    def clean_collection(self, collection):
        self.db[collection].delete_many({})
    
    def create_trip(self, collection: str, trip: Trip):
        trip_data = dict(trip.model_dump())
        self.db[collection].insert_one(trip_data)


from app.models.Event import Event
from datetime import datetime
from app.database.mongo.config import MONGODB_URI, DATABASE

mgr = DatabaseManager(MONGODB_URI, DATABASE)

trip = Trip(
    title="Mountain Adventure",
    start_time=datetime(2023, 1, 1, 9, 0),
    end_time=datetime(2023, 1, 4, 10, 0),
    location="Mountains",
    description="A trip to the mountains",
    owner="Alice",
    events=[
        Event(
            title="Hiking",
            start_time=datetime(2023, 1, 1, 10, 0),
            end_time=datetime(2023, 1, 1, 12, 0),
            description="A trip to the mountains",
            owner="Alice"
        ),
        Event(
            title="Camping",
            start_time=datetime(2023, 1, 2, 15, 0),
            end_time=datetime(2023, 1, 3, 10, 0),
            location="Campground",
            owner="Alice"
        )
    ]
)

# mgr.create_trip('trips', trip)
# mgr.clean_collection('trips')
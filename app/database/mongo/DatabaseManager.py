from pymongo import MongoClient

from app.database.mongo.model import Trip

class DatabaseManager:
    def __init__(self, host, port, db):
        client = MongoClient(host, port)
        self.db = client[db]

    def execute_query(self, collection, pipeline):
        collection = self.db[collection]
        result = collection.aggregate(pipeline)
        return result
    
    def clean_collection(self, collection):
        self.db[collection].delete_many({})
    
    def create_trip(self, collection: str, trip: Trip):
        trip_data = trip.model_dump_json()
        self.db[collection].insert_one(trip_data)


from app.database.mongo.model import Event
from datetime import datetime
from app.database.mongo.config import HOST, PORT, DATABASE

mgr = DatabaseManager(HOST, PORT, DATABASE)

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
            location="Trail",
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

mgr.create_trip('trips', trip)
# mgr.clean_collection('trips')
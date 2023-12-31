from app.database.mongo.CollectionManager import CollectionManager
from app.models.Trip import Trip

class TripCollectionManager(CollectionManager):
    def clean_collection(self) -> None:
        self.col.delete_many({})
    
    def create_trip(self, trip: Trip) -> None:
        trip_data = dict(trip.model_dump())
        self.col.insert_one(trip_data)

    def query_all_trips_of_owner(self, owner: str) -> list:
        query = {'owner': owner}
        docs = self.col.find(query)
        result = []
        for d in docs:
            result.append(d)
        return result
    
    def delete_trip_by_id(self, trip_id: str) -> None:
        query = {'_id': trip_id}
        self.col.delete_one(query)

from app.models.Event import Event
from datetime import datetime
from app.database.mongo.config import MONGODB_URI, DATABASE
from app.database.mongo.DatabaseManager import DatabaseManager

dbMgr = DatabaseManager(MONGODB_URI, DATABASE)
colMgr = TripCollectionManager(dbMgr, 'trips')

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
# docs = mgr.query_all_trips_of_owner('trips', 'Alice')
mgr.delete_trip_by_id('trips')
# mgr.clean_collection('trips')
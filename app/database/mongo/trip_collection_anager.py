from bson.objectid import ObjectId
from typing import Optional

from app.database.mongo.collection_manager import CollectionManager
from app.models.trip import Trip

class TripCollectionManager(CollectionManager):
    def clean_collection(self) -> None:
        self.col.delete_many({})
    
    def create_trip(self, trip: Trip) -> None:
        trip_data = dict(trip.model_dump())
        self.col.insert_one(trip_data)

    def query_all_trips_of_owner(self, owner: str) -> list:
        query = {'owner': owner}
        docs = self.col.find(query, {"events": 0})
        result = []
        for d in docs:
            result.append(d)
        return result
    
    def query_trip_by_id(self, trip_id: str) -> Optional[Trip]:
        query = {'_id': ObjectId(trip_id)}
        res = self.col.find_one(query)
        if res:
            trip = Trip(**doc)
            return trip
    
    def delete_trip_by_id(self, trip_id: str) -> None:
        query = {'_id': ObjectId(trip_id)}
        self.col.delete_one(query)
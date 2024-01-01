from bson.objectid import ObjectId
from typing import Optional, List

from app.database.mongo.collection_manager import CollectionManager
from app.common.models.trip import Trip

class TripCollectionManager(CollectionManager):
    def clean_collection(self) -> None:
        self.col.delete_many({})
    
    def create_trip(self, trip: Trip) -> None:
        trip_data = dict(trip.model_dump())
        self.col.insert_one(trip_data)

    def query_trips_by_owner(self, owner: str) -> Optional[List[Trip]]:
        query = {'owner': owner}
        docs = self.col.find(query)
        result = []
        for d in docs:
            result.append(d)
        return result
    
    def query_trip_by_id(self, trip_id: str) -> Optional[Trip]:
        query = {'_id': ObjectId(trip_id)}
        res = self.col.find_one(query)
        if res:
            trip = Trip(**res)
            return trip
    
    def delete_trip_by_id(self, trip_id: str) -> None:
        query = {'_id': ObjectId(trip_id)}
        self.col.delete_one(query)
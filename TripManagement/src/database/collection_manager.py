from bson.objectid import ObjectId
from typing import Optional, List
from pymongo import MongoClient

from src.models.trip import Trip

class CollectionManager():
    def __init__(self, uri, db_name, collection_name):
        self.uri = uri
        self.db_name = db_name
        self.collection_name = collection_name

    def connect(self) -> None:
        self.client = MongoClient(self.uri)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

    def disconnect(self) -> None:
        self.client.close()

    def clean_collection(self) -> None:
        self.collection.delete_many({})
    
    def create_trip(self, trip: Trip) -> None:
        trip_data = dict(trip.model_dump())
        self.collection.insert_one(trip_data)

    # def query_trips_by_owner(self, owner: str) -> Optional[List[Trip]]:
    #     query = {'owner': owner}
    #     docs = self.col.find(query)
    #     result = []
    #     for d in docs:
    #         result.append(d)
    #     return result
    
    # def query_trip_by_id(self, trip_id: str) -> Optional[Trip]:
    #     query = {'_id': ObjectId(trip_id)}
    #     res = self.col.find_one(query)
    #     if res:
    #         trip = Trip(**res)
    #         return trip
    
    # def delete_trip_by_id(self, trip_id: str) -> None:
    #     query = {'_id': ObjectId(trip_id)}
    #     self.col.delete_one(query)
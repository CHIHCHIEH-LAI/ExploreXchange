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
        document_count = 0
        for doc in self.collection.find({}):
            document_count += 1
        return document_count == 0
    
    def create_trip(self, trip: Trip) -> None:
        trip_data = dict(trip.model_dump())
        trip_id = self.collection.insert_one(trip_data).inserted_id
        return trip_id

    def query_trip_by_id(self, trip_id: str) -> Optional[Trip]:
        query = {'_id': ObjectId(trip_id)}
        res = self.collection.find_one(query)
        if res:
            trip = Trip(**res)
            return trip
        return None
    
    def delete_trip_by_id(self, trip_id: str) -> None:
        query = {'_id': ObjectId(trip_id)}
        del_count = self.collection.delete_one(query).deleted_count
        return del_count == 1

    # def query_trips_by_owner(self, owner: str) -> Optional[List[Trip]]:
    #     query = {'owner': owner}
    #     docs = self.col.find(query)
    #     result = []
    #     for d in docs:
    #         result.append(d)
    #     return result
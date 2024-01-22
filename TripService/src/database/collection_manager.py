from bson import ObjectId
from typing import Optional, List
import motor.motor_asyncio
from pydantic import EmailStr

from TripService.src.models.trip import Trip

class CollectionManager():
    def __init__(self, uri, db_name, collection_name):
        self.uri = uri
        self.db_name = db_name
        self.collection_name = collection_name

    async def connect(self) -> None:
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.uri)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

    async def disconnect(self) -> None:
        self.client.close()

    async def map_document_to_trip(self, document: dict) -> Trip:
        trip = Trip(**document)
        trip.id = str(document['_id'])
        return trip

    async def create_trip(self, trip: Trip) -> Optional[Trip]:
        trip_data = dict(trip.model_dump())
        new_trip_data = await self.collection.insert_one(trip_data)
        new_trip_data = await self.collection.find_one({"_id": new_trip_data.inserted_id})
        if new_trip_data:
            new_trip = await self.map_document_to_trip(new_trip_data)
            return new_trip

    async def retrieve_all_trips_by_email(self, email: EmailStr) -> List[Trip]:
        trips = []
        async for trip_data in self.collection.find({'email': email}):
            trip = await self.map_document_to_trip(trip_data)
            trips.append(trip)
        return trips
    
    async def retrieve_trip_by_id(self, trip_id: str) -> Optional[Trip]:
        trip_data = await self.collection.find_one({"_id": ObjectId(trip_id)})
        if trip_data:
            trip = await self.map_document_to_trip(trip_data)
            return trip

    async def delete_all_trips_by_email(self, email: EmailStr) -> bool:
        count = await self.collection.count_documents({'email': email})
        if count > 0:
            await self.collection.delete_many({'email': email})
            return True
        return False
    
    async def delete_trip_by_id(self, trip_id: str) -> None:
        trip_data = await self.collection.find_one({"_id": ObjectId(trip_id)})
        if trip_data:
            await self.collection.delete_one({"_id": ObjectId(trip_id)})
            return True
        return False
    
    async def update_trip(self, trip_id: str, trip: Trip) -> Optional[Trip]:
        trip_data = dict(trip.model_dump())
        trip_data.pop('id', None)  # Remove id as it should not be updated
        update_result = await self.collection.update_one({"_id": ObjectId(trip_id)}, {"$set": trip_data})
        if update_result.modified_count > 0:
            updated_trip_data = await self.collection.find_one({"_id": ObjectId(trip_id)})
            if updated_trip_data:
                updated_trip = await self.map_document_to_trip(updated_trip_data)
                return updated_trip
        return None
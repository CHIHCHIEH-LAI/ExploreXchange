import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config("MONGO_DETAILS")  # read environment variable

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.trips

trip_collection = database.get_collection("trips_collection")

# helpers
def trip_helper(trip) -> dict:
    return {
        "id": str(trip["_id"]),
        "title": trip["title"],
        "start_time": trip["start_time"],
        "end_time": trip["end_time"],
        "location": trip["location"],
        "description": trip["description"],
        "email": trip["email"],
        "public": trip["public"],
        "events": trip["events"],
    }

# crud operations

# Retrieve all trips present in the database
async def retrieve_trips():
    trips = []
    async for trip in trip_collection.find():
        trips.append(trip_helper(trip))
    return trips


# Add a new trip into to the database
async def add_trip(trip_data: dict) -> dict:
    trip = await trip_collection.insert_one(trip_data)
    new_trip = await trip_collection.find_one({"_id": trip.inserted_id})
    return trip_helper(new_trip)


# Retrieve a trip with a matching ID
async def retrieve_trip(id: str) -> dict:
    trip = await trip_collection.find_one({"_id": ObjectId(id)})
    if trip:
        return trip_helper(trip)

# Update a trip with a matching ID
async def update_trip(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    trip = await trip_collection.find_one({"_id": ObjectId(id)})
    if trip:
        updated_trip = await trip_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_trip:
            return True
        return False

# Delete a trip from the database
async def delete_trip(id: str):
    trip = await trip_collection.find_one({"_id": ObjectId(id)})
    if trip:
        await trip_collection.delete_one({"_id": ObjectId(id)})
        return True
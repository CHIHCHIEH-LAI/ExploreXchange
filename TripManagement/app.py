import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.models.trip import Trip
from src.database.collection_manager import CollectionManager
from config import MONGODB_URI, DATABASE_NAME, COLLECTION_NAME

app = FastAPI()

colMgr = CollectionManager(
    uri = MONGODB_URI,
    db_name = DATABASE_NAME,
    collection_name = COLLECTION_NAME
)
@asynccontextmanager
async def lifespan(app: FastAPI):
    colMgr.connect()
    yield
    colMgr.disconnect()

@app.post("/trips/create-trip")
async def create_trip(
    trip: Trip
):
    try:
        colMgr.create_trip(trip)
        return "Successfully created a trip", 200
    except Exception as e:
        return f"Unexpected error: {e}", 500
    
@app.delete("/trips/clean-collection")
async def clean_collection():
    try:
        colMgr.clean_collection()
        return "Successfully cleaned trip collection", 200
    except Exception as e:
        return f"Unexpected error: {e}", 500

if __name__ == '__main__':
    uvicorn.run(app, port=8001)
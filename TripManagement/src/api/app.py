import uvicorn
from typing import Optional
from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from TripManagement.src.models.trip import Trip
from TripManagement.src.database.collection_manager import CollectionManager
from TripManagement.config import MONGODB_URI, DATABASE_NAME, COLLECTION_NAME

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

@app.post("/trips/create-trip", status_code=status.HTTP_201_CREATED)
async def create_trip(trip: Trip):
    try:
        trip_id = colMgr.create_trip(trip)
        return JSONResponse(
            content={
                "message": "Successfully created a trip",
                "trip_id": trip_id
            }, 
            status_code=status.HTTP_201_CREATED
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(e)}")

@app.delete("/trips/clean-collection", status_code=status.HTTP_200_OK)
async def clean_collection():
    try:
        colMgr.clean_collection()
        return JSONResponse(content={"message": "Successfully cleaned trip collection"}, status_code=status.HTTP_200_OK)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(e)}")


@app.get("/trips/query-by-id/{trip_id}", response_model=Trip, status_code=status.HTTP_200_OK)
async def query_trip_by_id(trip_id: str) -> Optional[Trip]:
    trip = colMgr.query_trip_by_id(trip_id)

    if trip is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Trip not found")

    return trip

@app.delete("/trips/delete-trip/{trip_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_trip(trip_id: str):
    try:
        deletion_successful = colMgr.delete_trip_by_id(trip_id)

        if not deletion_successful:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Trip not found")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(e)}")

    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)


if __name__ == '__main__':
    uvicorn.run(app, port=8001)
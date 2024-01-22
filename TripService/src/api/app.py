from typing import List
from fastapi import FastAPI, status, HTTPException, BackgroundTasks
from starlette.responses import FileResponse
from contextlib import asynccontextmanager
import os

from TripService.src.models.trip import Trip
from TripService.src.database.collection_manager import CollectionManager
from TripService.config import MONGO_DETAILS, DATABASE_NAME, COLLECTION_NAME, ICS_DIR_PATH
from TripService.src.downloader.trip_downloader import TripDownloader

colMgr = CollectionManager(
    uri = MONGO_DETAILS,
    db_name = DATABASE_NAME,
    collection_name = COLLECTION_NAME
)
@asynccontextmanager
async def lifespan(app: FastAPI):
    await colMgr.connect()
    yield
    await colMgr.disconnect()

app = FastAPI(lifespan=lifespan)

@app.post("/trips/create-trip", response_model=Trip, status_code=status.HTTP_201_CREATED)
async def create_trip_endpoint(trip: Trip):
    try:
        new_trip = await colMgr.create_trip(trip)
        return new_trip
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(e)}")

@app.get("/trips/by-email/{email}", response_model=List[Trip], status_code=status.HTTP_200_OK)
async def retrieve_all_trips_by_email_endpoint(email: str):
    try:
        trips = await colMgr.retrieve_all_trips_by_email(email)
        return trips
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(e)}")

@app.get("/trips/by-id/{trip_id}", response_model=Trip, status_code=status.HTTP_200_OK)
async def retrieve_trip_by_id_endpoint(trip_id: str):
    try:
        trip = await colMgr.retrieve_trip_by_id(trip_id)
        return trip
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(e)}")

@app.delete("/trips/by-email/{email}", status_code=status.HTTP_200_OK)
async def delete_all_trips_by_email_endpoint(email: str):
    try:
        result = await colMgr.delete_all_trips_by_email(email)
        return {"success": result}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(e)}")

@app.delete("/trips/by-id/{trip_id}", status_code=status.HTTP_200_OK)
async def delete_trip_by_id_endpoint(trip_id: str):
    try:
        result = await colMgr.delete_trip_by_id(trip_id)
        return {"success": result}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(e)}")

@app.put("/trips/{trip_id}", response_model=Trip, status_code=status.HTTP_200_OK)
async def update_trip_endpoint(trip_id: str, trip: Trip):
    try:
        updated_trip = await colMgr.update_trip(trip_id, trip)
        if updated_trip is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Trip not found")
        return updated_trip
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(e)}")

@app.get("/trips/download/{trip_id}")
async def download_trip(trip_id: str, background_tasks: BackgroundTasks):

    trip = await colMgr.retrieve_trip_by_id(trip_id)
    file_path = os.path.join(ICS_DIR_PATH, f'trip{trip_id}.ics')
    TripDownloader.download_trip(trip, file_path)

    # Define a function to delete the file
    def delete_temp_file(file_path):
        os.unlink(file_path)

    # Add the delete_temp_file function as a background task
    background_tasks.add_task(delete_temp_file, file_path)

    response = FileResponse(path=file_path, media_type='text/calendar')
    return response
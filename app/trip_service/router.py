from fastapi import APIRouter, BackgroundTasks, status, Depends
from fastapi.responses import FileResponse
import os

from app.common.models.trip import Trip
from app.trip_service.dependencies import (
    get_trip_collection_manager,
    get_trip_to_ics_converter,
    get_ics_file_saver
)
from app.trip_service.config import ICS_DIR_PATH

router = APIRouter()

@router.delete("/clear-trips", status_code=status.HTTP_204_NO_CONTENT)
async def clear_trips(
    tripMgr = Depends(get_trip_collection_manager)
):
    tripMgr.clean_collection()
    return {"message": "Trips collection cleared successfully"}

@router.post("/create-trip", status_code=status.HTTP_201_CREATED)
async def create_trip(
    trip: Trip, 
    tripMgr = Depends(get_trip_collection_manager)
):
    tripMgr.create_trip(trip)
    return {"message": "Created trip successfully"}

@router.delete("/delete-trip", status_code=status.HTTP_204_NO_CONTENT)
async def delete_trip(
    trip_id: str,
    tripMgr = Depends(get_trip_collection_manager)
):
    tripMgr.delete_trip_by_id(trip_id)
    return {"message": "Trip deleted successfully"}

@router.get("/download-trip/{trip_id}")
async def download_trip(
    trip_id: str, 
    background_tasks: BackgroundTasks,
    tripMgr = Depends(get_trip_collection_manager),
    converter = Depends(get_trip_to_ics_converter),
    saver = Depends(get_ics_file_saver)
):
    file_path = os.path.join(ICS_DIR_PATH, f'trip{trip_id}.ics')

    trip = tripMgr.query_trip_by_id(trip_id)
    ics_calendar = converter.convert(trip)
    saver.save(ics_calendar, file_path)

    # Define a function to delete the file
    def delete_temp_file(file_path):
        os.unlink(file_path)

    # Add the delete_temp_file function as a background task
    background_tasks.add_task(delete_temp_file, file_path)

    response = FileResponse(path=file_path, media_type='text/calendar')
    return response
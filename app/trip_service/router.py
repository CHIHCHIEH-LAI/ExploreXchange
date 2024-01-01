from fastapi import APIRouter, BackgroundTasks, Depends
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

@router.get("/create/trip")
async def create_trip(
    trip: Trip, 
    tripMgr = Depends(get_trip_collection_manager)
):
    pass

@router.get("/download/trip/{trip_id}")
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
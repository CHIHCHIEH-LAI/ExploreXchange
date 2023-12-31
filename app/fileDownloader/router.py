from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import FileResponse
import os

from app.trip.Trip import Trip
from app.fileDownloader.ICSGenerator import ICSGenerator
from app.fileDownloader.config import ICS_DIR_PATH

router = APIRouter()

@router.post("/trip/generate_ics")
async def create_event(trip : Trip, background_tasks: BackgroundTasks):
    icsGenerator = ICSGenerator()
    ics_file_name = icsGenerator.generate_ics(trip)
    ics_file_path = os.path.join(ICS_DIR_PATH, ics_file_name)

    # Define a function to delete the file
    def delete_temp_file(file_path):
        os.unlink(file_path)

    # Add the delete_temp_file function as a background task
    background_tasks.add_task(delete_temp_file, ics_file_path)

    response = FileResponse(path=ics_file_path, filename=ics_file_name, media_type='text/calendar')
    return response

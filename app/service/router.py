from fastapi import APIRouter, FileResponse, BackgroundTask
import os

from app.trip.Trip import Trip
from app.service.ICSGenerator import ICSGenerator
from app.service import config

router = APIRouter()

@router.post("/trip/generate_ics")
async def create_event(trip : Trip):
    ics_file_name = ICSGenerator.generate_ics(trip)
    path = f'{config.ICS_FILE_PATH}/{ics_file_name}'
    response = FileResponse(path=path, filename=ics_file_name, media_type='text/calendar')

    # Delete the temporary file after sending the response
    response.background = BackgroundTask(os.unlink, path)
    return response

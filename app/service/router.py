from fastapi import APIRouter
import os

from app.trip.Trip import Trip
from app.service.ICSGenerator import ICSGenerator

router = APIRouter()

@router.post("/trip/generate_ics")
async def create_event(trip : Trip):
    pass
    ics_file_path = ICSGenerator.generate_ics(trip)
    # response = FileResponse(path=ics_file_path, filename="event.ics", media_type='text/calendar')

    # # Delete the temporary file after sending the response
    # response.background = BackgroundTask(os.unlink, ics_file_path)
    # return response

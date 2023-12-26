from fastapi import APIRouter
from app.trip.Trip import Trip
import os

router = APIRouter()

@router.post("/trip/generate_ics")
async def create_event(trip : Trip):
    pass
    # ics_file_path = generate_ics(event)
    # response = FileResponse(path=ics_file_path, filename="event.ics", media_type='text/calendar')

    # # Delete the temporary file after sending the response
    # response.background = BackgroundTask(os.unlink, ics_file_path)
    # return response

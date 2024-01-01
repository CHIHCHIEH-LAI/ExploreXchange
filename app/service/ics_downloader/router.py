from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import FileResponse
import os

from app.database.mongo.config import MONGODB_URI, DATABASE
from app.service.ics_downloader.config import ICS_DIR_PATH
from app.database.mongo.database_manager import DatabaseManager
from app.database.mongo.trip_collection_manager import TripCollectionManager
from app.service.ics_conversion.trip_to_ics_converter import TripToICSConverter
from app.service.ics_conversion.ics_file_saver import ICSFileSaver

router = APIRouter()

dbMgr = DatabaseManager(MONGODB_URI, DATABASE)
colMgr = TripCollectionManager(dbMgr, 'trips')
converter = TripToICSConverter()
saver = ICSFileSaver()

@router.get("/download/trip/{trip_id}")
async def download_trip(trip_id: str, background_tasks: BackgroundTasks):
    file_path = os.path.join(ICS_DIR_PATH, f'trip{trip_id}.ics')

    trip = colMgr.query_trip_by_id(trip_id)
    ics_calendar = converter.convert(trip)
    saver.save(ics_calendar, file_path)

    # Define a function to delete the file
    def delete_temp_file(file_path):
        os.unlink(file_path)

    # Add the delete_temp_file function as a background task
    background_tasks.add_task(delete_temp_file, file_path)

    response = FileResponse(path=file_path, media_type='text/calendar')
    return response

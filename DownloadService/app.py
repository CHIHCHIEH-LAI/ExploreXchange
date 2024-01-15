from fastapi import APIRouter, Request, BackgroundTasks, status, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, FileResponse
import os

from app.common.models.trip import Trip
from app.trip_service.dependencies import (
    get_trip_collection_manager,
    get_trip_downloader
)
from app.trip_service.config import ICS_DIR_PATH
from config import FRONTEND_TEMPLATE_DIR

router = APIRouter()

templates = Jinja2Templates(directory=FRONTEND_TEMPLATE_DIR)

# tripMgr = get_trip_collection_manager()
# downloader = get_trip_downloader()

@router.get("/trip/plan")
async def plan_trip(request: Request):
    return templates.TemplateResponse("trip_planning.html", {"request": request})

@router.post("/trip/create", status_code=status.HTTP_201_CREATED)
async def create_trip(
    request: Request,
    trip: Trip, 
    # tripMgr = Depends(get_trip_collection_manager)
):
    user_email = request.session.get('user').get('email')
    trip.update_owner(user_email)
    # tripMgr.create_trip(trip)

    return RedirectResponse(url='/', status_code=status.HTTP_303_SEE_OTHER)

# @router.delete("/clear-trips", status_code=status.HTTP_204_NO_CONTENT)
# async def clear_trips(
#     tripMgr = Depends(get_trip_collection_manager)
# ):
#     tripMgr.clean_collection()
#     return {"message": "Trips collection cleared successfully"}
    
# @router.get("/query-trip_by_id/{trip_id}", response_model=Trip, status_code=status.HTTP_200_OK)
# async def query_trip_by_id(
#     trip_id: str,
#     tripMgr = Depends(get_trip_collection_manager)
# ):
#     tripMgr.query_trip_by_id(trip_id)

# @router.delete("/delete-trip/{trip_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_trip(
#     trip_id: str,
#     tripMgr = Depends(get_trip_collection_manager)
# ):
#     tripMgr.delete_trip_by_id(trip_id)
#     return {"message": "Trip deleted successfully"}

# @router.get("/download-trip/{trip_id}")
# async def download_trip(
#     trip_id: str, 
#     background_tasks: BackgroundTasks,
#     tripMgr = Depends(get_trip_collection_manager),
#     downloader = Depends(get_trip_downloader)
# ):
#     file_path = os.path.join(ICS_DIR_PATH, f'trip{trip_id}.ics')

#     trip = tripMgr.query_trip_by_id(trip_id)
#     downloader.download_trip(trip)

#     # Define a function to delete the file
#     def delete_temp_file(file_path):
#         os.unlink(file_path)

#     # Add the delete_temp_file function as a background task
#     background_tasks.add_task(delete_temp_file, file_path)

#     response = FileResponse(path=file_path, media_type='text/calendar')
#     return response
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
    

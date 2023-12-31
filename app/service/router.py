from fastapi import APIRouter

from app.service.ics_downloader.router import router as ics_conversion_router

router = APIRouter()

router.include_router(ics_conversion_router)
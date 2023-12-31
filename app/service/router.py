from fastapi import APIRouter

from app.service.ics_conversion.router import ics_conversion_router

router = APIRouter()

router.include_router(ics_conversion_router)
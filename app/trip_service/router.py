from fastapi import APIRouter

from app.common.models.trip import Trip

router = APIRouter()

@router.get("/create/trip")
async def create_trip(trip: Trip):
    pass
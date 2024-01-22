from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from server.database import (
    add_trip,
    delete_trip,
    retrieve_trip,
    retrieve_trips,
    update_trip,
)
from server.models.trip import TripSchema, UpdateTripModel

router = APIRouter()


@router.post("/", response_description="Trip data added into the database")
async def add_trip_data(trip: TripSchema = Body(...)):
    trip = jsonable_encoder(trip)
    new_trip = await add_trip(trip)
    return JSONResponse(content=new_trip, status_code=201)


@router.get("/", response_description="Trips retrieved")
async def get_trips():
    trips = await retrieve_trips()
    if trips:
        return JSONResponse(content=trips, status_code=200)
    return JSONResponse(content=[], status_code=200)


@router.get("/{id}", response_description="Trip data retrieved")
async def get_trip_data(id):
    trip = await retrieve_trip(id)
    if trip:
        return JSONResponse(content=trip, status_code=200)
    raise HTTPException(status_code=404, detail="Trip doesn't exist.")


@router.put("/{id}", response_description="Trip data updated")
async def update_trip_data(id: str, req: UpdateTripModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_trip = await update_trip(id, req)
    if updated_trip:
        return JSONResponse(content={"message": "Trip updated successfully"}, status_code=200)
    raise HTTPException(status_code=404, detail="Error updating trip data.")


@router.delete("/{id}", response_description="Trip data deleted from the database")
async def delete_trip_data(id: str):
    deleted_trip = await delete_trip(id)
    if deleted_trip:
        return JSONResponse(content={"message": "Trip deleted successfully"}, status_code=200)
    raise HTTPException(status_code=404, detail="Trip with id {0} doesn't exist".format(id))
from fastapi import FastAPI
from app.trip.router import trip_router

app = FastAPI()

app.include_router(trip_router)

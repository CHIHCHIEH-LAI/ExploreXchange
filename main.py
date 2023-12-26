from fastapi import FastAPI
from app.service.router import trip_router

app = FastAPI()

app.include_router(trip_router)

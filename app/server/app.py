from fastapi import FastAPI

from server.routes.trip import router as TripRouter

app = FastAPI()

app.include_router(TripRouter, tags=["Trip"], prefix="/trip")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
import uvicorn
from typing import Optional
from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from TripService.src.models.trip import Trip
from TripService.src.database.collection_manager import CollectionManager
from TripService.config import MONGO_DETAILS, DATABASE_NAME, COLLECTION_NAME

colMgr = CollectionManager(
    uri = MONGO_DETAILS,
    db_name = DATABASE_NAME,
    collection_name = COLLECTION_NAME
)
@asynccontextmanager
async def lifespan(app: FastAPI):
    colMgr.connect()
    yield
    colMgr.disconnect()
app = FastAPI(lifespan=lifespan)

@app.post("/trips/create-trip", status_code=status.HTTP_201_CREATED)
async def create_trip(trip: Trip):
    try:
        trip_id = colMgr.create_trip(trip)
        return JSONResponse(
            content={
                "message": "Successfully created a trip",
                "trip_id": trip_id
            }, 
            status_code=status.HTTP_201_CREATED
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(e)}")

@app.delete("/trips/clean-collection", status_code=status.HTTP_200_OK)
async def clean_collection():
    try:
        colMgr.clean_collection()
        return JSONResponse(content={"message": "Successfully cleaned trip collection"}, status_code=status.HTTP_200_OK)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(e)}")


@app.get("/trips/query-by-id/{trip_id}", response_model=Trip, status_code=status.HTTP_200_OK)
async def query_trip_by_id(trip_id: str) -> Optional[Trip]:
    trip = colMgr.query_trip_by_id(trip_id)

    if trip is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Trip not found")

    return trip

@app.delete("/trips/delete-trip/{trip_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_trip(trip_id: str):
    try:
        deletion_successful = colMgr.delete_trip_by_id(trip_id)

        if not deletion_successful:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Trip not found")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(e)}")

    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

# @app.get("/download/trip/{trip_id}")
# async def download_trip(trip_id: str, background_tasks: BackgroundTasks):

#     trip_query_uri = os.path.join(TRIP_MANAGEMENT_URI, f'trips/query-by-id/{trip_id}')
#     response = requests.get(trip_query_uri)
    
#     # and extract trip data from requests response

#     # trip to ics
    
#     # save ics file

#     # download ics file

#     # future: save ics file to redic for caching

#     file_path = os.path.join(ICS_DIR_PATH, f'trip{trip_id}.ics')

#     downloader.download_trip(trip)

#     # Define a function to delete the file
#     def delete_temp_file(file_path):
#         os.unlink(file_path)

#     # Add the delete_temp_file function as a background task
#     background_tasks.add_task(delete_temp_file, file_path)

#     response = FileResponse(path=file_path, media_type='text/calendar')
#     return response


if __name__ == '__main__':
    uvicorn.run(app, port=8001)
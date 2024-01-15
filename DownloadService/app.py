import uvicorn
from fastapi import FastAPI, BackgroundTasks, FileResponse
import requests
import os

from config import TRIP_MANAGEMENT_URI, ICS_DIR_PATH

app = FastAPI()

@app.get("/download/trip/{trip_id}")
async def download_trip(
    trip_id: str, 
    background_tasks: BackgroundTasks
):
    
    trip_query_uri = os.path.join(TRIP_MANAGEMENT_URI, f'trips/query-by-id/{trip_id}')
    requests.get(trip_query_uri)
    
    # and extract trip data from requests response

    # trip to ics

    # save ics file

    # download ics file

    # future: save ics file to redic for caching

    file_path = os.path.join(ICS_DIR_PATH, f'trip{trip_id}.ics')

    downloader.download_trip(trip)

    # Define a function to delete the file
    def delete_temp_file(file_path):
        os.unlink(file_path)

    # Add the delete_temp_file function as a background task
    background_tasks.add_task(delete_temp_file, file_path)

    response = FileResponse(path=file_path, media_type='text/calendar')
    return response


if __name__ == '__main__':
    uvicorn.run(app, port=8002)
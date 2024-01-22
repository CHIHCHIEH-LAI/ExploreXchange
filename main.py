import uvicorn

from TripService.src.api.app import app

if __name__ == '__main__':
    uvicorn.run(app, port=8000)
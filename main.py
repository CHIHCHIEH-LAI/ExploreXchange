import uvicorn

from TripManagement.src.api.app import app

if __name__ == '__main__':
    uvicorn.run(app, port=8001)
import uvicorn

from TripManagement.app import app

if __name__ == '__main__':
    uvicorn.run(app, port=8001)
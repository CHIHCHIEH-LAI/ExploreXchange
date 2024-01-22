from dotenv import load_dotenv
import os

load_dotenv()

MONGO_DETAILS = os.getenv('MONGO_DETAILS')
DATABASE_NAME = 'trip_db'
COLLECTION_NAME = 'trip_collection'

PROJECT_PATH = os.getenv('PROJECT_PATH')
ICS_DIR_PATH = os.path.join(PROJECT_PATH, 'TripService/src/download_helper/ics_files')
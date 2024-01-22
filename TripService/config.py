from dotenv import load_dotenv
import os

load_dotenv()

MONGO_DETAILS = os.getenv('MONGO_DETAILS')
DATABASE_NAME = 'trip_db'
COLLECTION_NAME = 'trip_collection'

ICS_DIR_PATH = 'TripService/ics_files'
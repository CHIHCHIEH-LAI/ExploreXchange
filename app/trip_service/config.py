from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI')
DATABASE = 'exploreXchangeDB'

TRIPS_COLLECTION = 'trips'
ICS_DIR_PATH = 'app/service/ics_downloader/ics_files'
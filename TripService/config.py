from dotenv import load_dotenv
import os

load_dotenv()

MONGO_DETAILS = os.getenv('MONGO_DETAILS')
DATABASE_NAME = 'exploreXchangeDB'
COLLECTION_NAME = 'trips'
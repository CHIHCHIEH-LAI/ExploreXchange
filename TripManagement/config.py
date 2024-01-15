from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI')
DATABASE_NAME = 'exploreXchangeDB'
COLLECTION_NAME = 'trips'
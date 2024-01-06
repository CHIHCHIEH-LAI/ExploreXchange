import pytest

from app.database.mongo.database_manager import DatabaseManager
from app.trip_service.config import MONGODB_URI, DATABASE

def test_mongodb_connection():
    dbMgr = DatabaseManager(MONGODB_URI, DATABASE)
    try:
        dbMgr.client.admin.command('ping')
    except Exception as e:
        assert False, f"An error occurred while connecting to MongoDB: {e}"
    
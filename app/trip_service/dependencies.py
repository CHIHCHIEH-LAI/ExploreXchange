from app.trip_service.config import MONGODB_URI, DATABASE, TRIPS_COLLECTION
from app.database.mongo.database_manager import DatabaseManager
from app.trip_service.utils.trip_collection_manager import TripCollectionManager
from app.trip_service.utils.trip_downloader import TripDownloader

def get_trip_collection_manager():
    dbMgr = DatabaseManager(MONGODB_URI, DATABASE)
    colMgr = TripCollectionManager(dbMgr, TRIPS_COLLECTION)
    return colMgr

def get_trip_downloader():
    downloader = TripDownloader()
    return downloader
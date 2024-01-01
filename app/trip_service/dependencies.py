from app.trip_service.config import MONGODB_URI, DATABASE
from app.database.mongo.database_manager import DatabaseManager
from app.trip_service.utils.trip_collection_manager import TripCollectionManager
from app.trip_service.utils.trip_to_ics_converter import TripToICSConverter
from app.trip_service.utils.ics_file_saver import ICSFileSaver

def get_trip_collection_manager():
    dbMgr = DatabaseManager(MONGODB_URI, DATABASE)
    colMgr = TripCollectionManager(dbMgr, 'trips')
    return colMgr

def get_trip_to_ics_converter():
    converter = TripToICSConverter()
    return converter

def get_ics_file_saver():
    saver = ICSFileSaver()
    return saver
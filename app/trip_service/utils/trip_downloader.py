from app.trip_service.utils.trip_to_ics_converter import TripToICSConverter
from app.trip_service.utils.ics_file_saver import ICSFileSaver
from app.common.models.trip import Trip

class TripDownloader:
    def __init__(self):
        self.converter = TripToICSConverter()
        self.saver = ICSFileSaver
    
    def download_trip(self, trip: Trip, file_path: str):
        ics_calendar = self.converter.convert(trip)
        self.saver.save(ics_calendar, file_path)
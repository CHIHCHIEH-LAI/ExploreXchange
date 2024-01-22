from src.utils.trip_to_ics_converter import TripToICSConverter
from src.utils.ics_file_saver import ICSFileSaver
from src.models.trip import Trip

class TripDownloader:
    @staticmethod
    def download_trip(trip: Trip, file_path: str):
        ics_calendar = TripToICSConverter.convert(trip)
        ICSFileSaver.save(ics_calendar, file_path)

# class TripDownloader:
#     def __init__(self):
#         self.converter = TripToICSConverter
#         self.saver = ICSFileSaver
    
#     def download_trip(self, trip: Trip, file_path: str):
#         ics_calendar = self.converter.convert(trip)
#         self.saver.save(ics_calendar, file_path)
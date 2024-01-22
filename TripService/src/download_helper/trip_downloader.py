from TripService.src.download_helper.trip_to_ics_converter import TripToICSConverter
from TripService.src.download_helper.ics_file_saver import ICSFileSaver
from TripService.src.models.trip import Trip

class TripDownloader:
    @staticmethod
    def download_trip(trip: Trip, file_path: str):
        ics_calendar = TripToICSConverter.convert(trip)
        ICSFileSaver.save(ics_calendar, file_path)
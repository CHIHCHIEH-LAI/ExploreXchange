import ics
import os

from app.trip.Trip import Trip
from app.service.config import ICS_DIR_PATH

class ICSGenerator:
    def generate_ics(self, trip: Trip) -> str:
        calendar = ics.Calendar()

        for event in trip.events:

            ics_event = ics.Event()
            ics_event.name = event.title
            ics_event.begin = event.start_time
            ics_event.end = event.end_time
            ics_event.location = event.location
            ics_event.description = event.description
            calendar.events.add(ics_event)

        ics_file_name = f"{trip.trip_name.replace(' ', '_')}.ics"
        ics_file_path = os.path.join(ICS_DIR_PATH, ics_file_name)
        with open(ics_file_path, 'w') as trip_file:
            trip_file.writelines(calendar)

        return ics_file_name
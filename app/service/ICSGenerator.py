import ics
from datetime import datetime
import pytz

from app.trip.Trip import Trip

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
        with open(ics_file_name, 'w') as trip_file:
            trip_file.writelines(calendar)

        return ics_file_name
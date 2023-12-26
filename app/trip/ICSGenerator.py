import ics
from datetime import datetime
import pytz

from app.trip.Trip import Trip

class ICSGenerator:
    def generate_ics(self, trip: Trip) -> str:
        calendar = ics.Calendar()

        for event in trip.events:
            start_time = self.convert_to_timezone(event.start_time, event.timezone)
            end_time = self.convert_to_timezone(event.end_time, event.timezone)

            ics_event = ics.Event()
            ics_event.name = event.title
            ics_event.begin = start_time
            ics_event.end = end_time
            ics_event.location = event.location
            ics_event.description = event.description
            calendar.events.add(ics_event)

        ics_file_name = f"{trip.trip_name.replace(' ', '_')}.ics"
        with open(ics_file_name, 'w') as trip_file:
            trip_file.writelines(calendar)

        return ics_file_name

    def convert_to_timezone(self, time: datetime, timezone: str) -> datetime:
        return time.astimezone(pytz.timezone(timezone))      
import ics

from src.models.trip import Trip

class TripToICSConverter:
    @staticmethod
    def convert(self, trip: Trip) -> ics.Calendar:
        calendar = ics.Calendar()

        for event in trip.events:

            ics_event = ics.Event()
            ics_event.name = event.title
            ics_event.begin = event.start_time
            ics_event.end = event.end_time
            ics_event.location = event.location
            ics_event.description = event.description
            calendar.events.add(ics_event)

        return calendar
        
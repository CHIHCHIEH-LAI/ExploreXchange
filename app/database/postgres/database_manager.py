from sqlmodel import SQLModel, Session, create_engine, select

from app.database.postgres.models import Trip, Event

class DatabaseManager:
    def __init__(self, database_uri):
        self.engine = create_engine(database_uri, echo=True)

    def create_all_tables(self):
        SQLModel.metadata.create_all(self.engine)
    
    def delete_all_tables(self):
        SQLModel.metadata.drop_all(self.engine)

    def initializa_all_tables(self):
        SQLModel.metadata.drop_all(self.engine)
        SQLModel.metadata.create_all(self.engine)

    def create_trip(self, trip: Trip):
        with Session(self.engine) as session:
            session.add(trip)
            session.commit()

    def query_all_trips_of_owner(self, owner_email: str):
        trips = []
        with Session(self.engine) as session:
            statement = select(Trip).where(Trip.owner == owner_email)
            results = session.exec(statement)
            for trip in results:
                trips.append(trip)
        return trips
    
    def query_events_of_trip(self, trip_id: int):
        with Session(self.engine) as session:
            trip = session.get(Trip, trip_id)
            if trip:
                return trip.events
            else:
                return None
            
    def delete_trip(self, trip: Trip):
        pass
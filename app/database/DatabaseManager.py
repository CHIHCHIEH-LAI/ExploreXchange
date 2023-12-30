from sqlmodel import SQLModel, create_engine

from app.database.config import DATABASE_URI
from app.database.models import Trip

class DatabaseManager:
    def __init__(self, database_uri):
        self.engine = create_engine(database_uri, echo=True)

    def create_all_tables(self):
        SQLModel.metadata.drop_all(self.engine)
        SQLModel.metadata.create_all(self.engine)
    
    def delete_all_tables(self):
        SQLModel.metadata.drop_all(self.engine)

    def create_trip(self, trip: Trip):
        pass
from sqlmodel import SQLModel, create_engine

from app.database.config import DATABASE_URI

class DatabaseManager:
    def __init__(self, engine):
        self.engine = engine

    def create_all_tables(self):
        SQLModel.metadata.drop_all(self.engine)
        SQLModel.metadata.create_all(self.engine)
    
    def destroy_all_tables(self):
        SQLModel.metadata.drop_all(self.engine)

# engine = create_engine(DATABASE_URI, echo=True)
# databaseManager = DatabaseManager(engine)
# databaseManager.destroy_all_tables()
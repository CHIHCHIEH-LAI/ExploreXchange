from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

class postgres_tables:
    def __init__(self, database_uri):
        self.engine = create_engine(database_uri)
        self.Base = declarative_base()

    def get_Base(self):
        return self.Base
    
    def create(self):
        self.Base.metadata.create_all(self.engine)

    def destroy(self):
        self.Base.metadata.drop_all(self.engine)
    
    def recreate(self):
        self.destroy()
        self.create()
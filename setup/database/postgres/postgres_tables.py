from sqlalchemy import create_engine

class postgres_tables:
    def __init__(self, database_uri, Base):
        self.engine = create_engine(database_uri)
        self.Base = Base

    def initialize(self):
        self.destroy()
        self.create()
    
    def create(self):
        self.Base.metadata.create_all(self.engine)

    def destroy(self):
        self.Base.metadata.drop_all(self.engine)
    
    def recreate(self):
        self.destroy()
        self.create()
from sqlalchemy import Column, Integer, String, Date, ARRAY

from setup.database.postgres.setup_tables import tables

class trip_schema(tables.get_Base()):
    __tablename__ = 'trips'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    events = Column(ARRAY(Integer))
    start_time = Column(Date)
    end_time = Column(Date)
    location = Column(String)
    description = Column(String)
    owner = Column(String)
    
    def __repr__(self):
        return (f"<Trip("
                f"title='{self.title}', "
                f"events={self.events}, "
                f"start_time={self.start_time}, "
                f"end_time={self.end_time}, "
                f"location='{self.location}', "
                f"description='{self.description}', "
                f"owner='{self.owner}', "
                ")>")
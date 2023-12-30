from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date, ARRAY

from setup.database.postgres.config import DATABASE_URI

Base = declarative_base()

class trip_schema(Base):
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
    
class event_schema(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    start_time = Column(Date)
    end_time = Column(Date)
    location = Column(String)
    description = Column(String)
    owner = Column(String)
    
    def __repr__(self):
        return (f"<Book("
                f"title='{self.title}', "
                f"start_time={self.start_time}, "
                f"end_time={self.end_time}, "
                f"location='{self.location}', "
                f"description='{self.description}', "
                f"owner='{self.owner}', "
                ")>")

engine = create_engine(DATABASE_URI)

Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)
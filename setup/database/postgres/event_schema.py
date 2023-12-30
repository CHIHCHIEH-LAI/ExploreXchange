from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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
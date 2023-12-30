from sqlalchemy import Column, Integer, String, Date

from setup.database.postgres.setup_tables import tables

class event_schema(tables.get_Base()):
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
from app.database.mongo.DatabaseManager import DatabaseManager

class CollectionManager:
    def __init__(self, mgr: DatabaseManager, collection: str):
        self.mgr = mgr
        self.col = self.mgr.db[collection]

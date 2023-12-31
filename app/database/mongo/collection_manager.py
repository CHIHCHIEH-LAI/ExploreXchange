from app.database.mongo.database_manager import DatabaseManager

class CollectionManager:
    def __init__(self, mgr: DatabaseManager, collection: str):
        self.mgr = mgr
        self.col = self.mgr.db[collection]

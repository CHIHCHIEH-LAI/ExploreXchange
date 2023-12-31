from pymongo import MongoClient

class DatabaseManager:
    def __init__(self, uri: str, db: str) -> None:
        self.client = MongoClient(uri)
        self.db = self.client[db]
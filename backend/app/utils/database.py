from app.utils.vars import DB_USERNAME, DB_PASSWORD, DB_NAME
from pymongo import MongoClient
import datetime

class Database:
    def __init__(self):
        self.client = MongoClient(f"mongodb://{DB_USERNAME}:{DB_PASSWORD}@localhost:27017/")
        self.db = self.client[DB_NAME]

    def get_connection(self):
        return self.db
    
    def add_history_element(self, param_data: dict, param_type: str, param_args: list = []):
        """
        Add a new element to the history collection
        example:
        {
            "datetime": "2021-08-01T12:00:00.000Z",
            "type": "person",
            "args": ["John", "Doe"],
            "data": {
                ...
            }
        """
        history_element = {
            "datetime": datetime.utcnow(),
            "type": param_type,
            "args": param_args,
            "data": param_data
        }
        self.db.history.insert_one(history_element)
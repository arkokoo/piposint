import json
import os
import datetime
from uuid import uuid4

class History:
    def __init__(self):
        folder_path = os.path.join(os.path.dirname(__file__), "../../history")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        self.folder_path = folder_path

    def add_element(self, param_data: dict, param_type: str, param_args: list = []):
        """
        Add a new element to the history collection
        example:
        {
            "id": "e6d3e1e5-0e4b-4e0b-8e5f-4e5d5c4e3e2e",
            "datetime": "2021-08-01T12:00:00.000Z",
            "type": "person",
            "args": ["John", "Doe"],
            "data": {
                ...
            }
        }
        """
        uuid = str(uuid4())
        history_element = {
            "uuid": uuid,
            "datetime": datetime.datetime.now().isoformat(),
            "type": param_type,
            "args": param_args,
            "data": param_data
        }
        file_name = f"{uuid}.json"
        file_path = os.path.join(self.folder_path, file_name)
        with open(file_path, 'w') as file:
            json.dump(history_element, file)
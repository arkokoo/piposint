import json
import os
import datetime
from uuid import uuid4
import re

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

        data = param_data

        # if param_type == "overpass-turbo" and "service" in data:
        #     data.pop("service")
        #     if "query" in data and bool(re.search(r"## .+ ##", data["query"])):
        #         query_title = data["query"].split("## ")[1].split(" ##")[0]
        #         param_args.append(query_title)
        
        history_element = {
            "uuid": uuid,
            "datetime": datetime.datetime.now().isoformat(),
            "type": param_type,
            "args": param_args,
            "data": data
        }

        file_name = f"{uuid}.json"
        file_path = os.path.join(self.folder_path, file_name)
        with open(file_path, 'w') as file:
            json.dump(history_element, file)

def get_overpass_turbo_args(service_name: str, data: dict) -> list:
    """
    Extracts overpass turbo query title from the query if defined
    """
    output_args = []
    if service_name == "overpass-turbo":
        if "query" in data and bool(re.search(r"## .+ ##", data["query"])):
            query_title = data["query"].split("## ")[1].split(" ##")[0]
            output_args.append(query_title)
    return output_args
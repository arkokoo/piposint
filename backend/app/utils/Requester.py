import random
import requests
import os

class Requester:
    def __init__(self, url: str, headers={}, params={}):
        self.url = url
        self.head = headers
        self.params = params

    def get(self):
        try:
            self.head["user-agent"] = get_user_agent()
            response = requests.get(url=self.url, headers=self.head, params=self.params)
            return response

        except requests.exceptions.RequestException:
            #return requests.Response(status_code=500, content=f"Internal Server Error")
            pass


def get_user_agent():
    file_path = os.path.join(os.path.dirname(__file__), "user_agents.txt")
    with open(file_path, "r") as agent:
        user_agent = agent.read().split('\n')
    return random.choice(user_agent)
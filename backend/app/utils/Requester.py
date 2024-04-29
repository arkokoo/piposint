import random
import warnings
import requests
import os

class Requester:
    """A class to make requests with a random user agent."""
    def __init__(self, url: str, headers={}, params={}):
        self.url = url
        self.head = headers
        self.params = params

    def get(self):
        try:
            self.head["user-agent"] = get_user_agent()
            response = requests.get(url=self.url, headers=self.head, params=self.params)
            warnings.filterwarnings("ignore")
            return response

        except requests.exceptions.RequestException:
            pass

    def post(self, data={}, json={}):
        try:
            self.head["user-agent"] = get_user_agent()
            response = requests.post(url=self.url, headers=self.head, params=self.params, data=data, json=json)
            warnings.filterwarnings("ignore")
            return response

        except requests.exceptions.RequestException:
            pass


def get_user_agent():
    """Return a random user agent."""
    file_path = os.path.join(os.path.dirname(__file__), "user_agents.txt")
    with open(file_path, "r") as agent:
        user_agent = agent.read().split('\n')
    return random.choice(user_agent)
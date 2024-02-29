from app.utils.Requester import Requester
import os
from dotenv import load_dotenv

def hunter(domain) :
    json_data = {}
    load_dotenv()
    api_key = os.getenv('HUNTER_API_KEY')
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={api_key}"
    print(url)
    response = Requester(url=url).get()
    if response and response.status_code == 200 :
        json_data = response.json()
        return json_data

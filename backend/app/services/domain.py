from app.utils.Requester import Requester
from app.utils.vars import HUNTER_API_KEY
from flask import abort

def hunter(domain: str)-> dict:
    json_data = {}
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={HUNTER_API_KEY}&limit=100"
    print(url)
    response = Requester(url=url).get()
    if response and response.status_code == 200:
        json_data = response.json()
        return json_data
    elif response.status_code == 401:
        abort(500, description="Invalid Hunter API Key")
    else:
        abort(500, description="Failed to fetch data from Hunter API")
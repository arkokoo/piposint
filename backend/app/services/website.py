from app.utils.Requester import Requester
from app.utils.vars import WAPPALYZER_API_KEY
from flask import abort

def wappalyzer(url: str)-> dict:
    json_data = {}

    url = f"https://api.wappalyzer.com/v2/lookup/?urls={url}"
    headers = { "x-api-key": WAPPALYZER_API_KEY }

    response = Requester(url=url).get(headers=headers)
    if response and response.status_code == 200:
        json_data = response.json()
        return json_data
    elif response.status_code == 401:
        abort(500, description="Invalid Wappalyzer API Key")
    else:
        abort(500, description="Failed to fetch data from Wappalyzer API")
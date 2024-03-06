from app.utils.Requester import Requester
from app.utils.vars import HUNTER_API_KEY

def hunter(domain) :
    json_data = {}
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={HUNTER_API_KEY}"
    print(url)
    response = Requester(url=url).get()
    if response and response.status_code == 200 :
        json_data = response.json()
        return json_data

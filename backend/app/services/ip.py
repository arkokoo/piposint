from app.utils.Requester import Requester
from app.utils.tools import get_country, get_countries

def get_ip(search_value) :
    json_data = {}
    url = f"http://ip-api.com/json/{search_value}?fields=20474"
    response = Requester(url=url).get()
    if response and response.status_code == 200 :
        countries = get_countries()
        json_data = response.json()
        json_data['country'],json_data['country_flag'] = get_country(countries,json_data['countryCode'])
        del json_data['countryCode']
        return json_data
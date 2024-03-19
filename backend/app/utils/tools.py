from app.utils.Requester import Requester


def deepupdate(original_dict, new_dict):
    """Merge recursively two dictionaries"""
    for key, value in new_dict.items():
        if isinstance(value, dict) and key in original_dict and isinstance(original_dict[key], dict):
            deepupdate(original_dict[key], value)
        else:
            original_dict[key] = value


def get_countries():
    """Get countries data from country-flag-emoji-json package"""
    url = "https://cdn.jsdelivr.net/npm/country-flag-emoji-json@2.0.0/dist/by-code.json"
    response = Requester(url).get()
    countries = response.json()
    return countries


def get_country(countries, country_code):
    """Get country name and emoji from country code"""
    try:
        country_data = countries[country_code]
        country_name = country_data["name"]
        country_emoji = country_data["emoji"]
        return country_name, country_emoji
    except KeyError:
        pass
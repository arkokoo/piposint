from app.utils.tools import get_countries, get_country
import phonenumbers
from phonenumbers import carrier

async def lookup(phone_number):
    output = {
        "is_possible_number": None,
        "is_valid_number": None,
        "operator": None,
        "line_type": None,
        "country": None,
        "country_emoji": None
    }
    parsed = phonenumbers.parse(phone_number)

    output["is_possible_number"] = phonenumbers.is_possible_number(parsed)
    output["is_valid_number"] = phonenumbers.is_valid_number(parsed)

    output["operator"] = carrier.name_for_number(parsed, "fr")

    line = phonenumbers.number_type(parsed)
    
    if line == phonenumbers.PhoneNumberType.FIXED_LINE:
        output["line_type"] = "Fixed"

    elif line == phonenumbers.PhoneNumberType.MOBILE:
        output["line_type"] = "Mobile"

    country_code = phonenumbers.region_code_for_number(parsed)
    countries = get_countries()
    output["country"], output["country_emoji"] = get_country(countries, country_code)

    return output
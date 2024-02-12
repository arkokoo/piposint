import os
import phonenumbers
import json
from phonenumbers import carrier

async def lookup(phone_number):
    output = {
        "is_possible_number": None,
        "is_valid_number": None,
        "operator": None,
        "line_type": None,
        "countries": []
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

    file_path = os.path.join(os.path.dirname(__file__), "country_codes.json")
    with open(file_path, "r") as file:
        read = json.load(file)

    count_countries = 0

    for country, code in read.items():
        count_countries += 1 

        if phone_number.startswith(code):
            output["countries"].append(country)

            if count_countries == 153:
                break
            else:
                continue
        else:
            continue

    return output
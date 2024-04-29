import asyncio
from app.utils.tools import deepupdate
from app.utils.phone.lookup import lookup
from app.utils.phone.tellows import get_tellows
from app.utils.phone.spamcalls import get_spamcalls

async def get_phone_info(phone_number: str)->dict:
    output_dict = {
        "phone_number": phone_number,
        "is_possible_number": None,
        "is_valid_number": None,
        "operator": None,
        "country": None,
        "country_emoji": None,
        "line_type": None,
        "reputation": {
            "tellows": {
                "url": None,
                "notes": None,
                "score": None
            },
            "spamcalls": {
                "url": None,
                "is_spam": None
            }
        }
    }

    tasks = [
        lookup(phone_number),
        get_tellows(phone_number),
        get_spamcalls(phone_number)
    ]
    results = await asyncio.gather(*tasks)
    for result in results:
        deepupdate(output_dict, result)

    return output_dict

def format_phone(phone_number: str)->str:
    """
    Format phone number to E.164 standard
    """
    phone_number = phone_number.strip()

    if phone_number.startswith("%2B"):
        phone_number = phone_number.replace("%2B", "+")

    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number
    return phone_number
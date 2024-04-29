from app.utils.Requester import Requester
from bs4 import BeautifulSoup
from flask import abort

async def get_spamcalls(phone_number):
    url = f"https://spamcalls.net/fr/number/{phone_number.replace('+', '%2B')}"
    output = {
        "reputation": {
            "spamcalls": {
                "url": None,
                "is_spam": None
            }
        }
    }
    output["reputation"]["spamcalls"]["url"] = url
    try:
        with Requester(url=url).get() as response:
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                title = soup.title.string
                output["reputation"]["spamcalls"]["is_spam"] = title.startswith(phone_number)
            elif response.status_code == 410:
                output["reputation"]["spamcalls"]["is_spam"] = False
    except Exception as e:
        # TODO: Add a log
        abort(500, description=f"Failed to fetch data from Spamcalls: {e}")
    return output
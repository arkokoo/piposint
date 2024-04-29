from app.utils.Requester import Requester
from bs4 import BeautifulSoup
from flask import abort

async def get_tellows(phone_number):
    url = f"https://www.tellows.fr/num/{phone_number.replace('+', '%2B')}"
    output = {
        "reputation": {
            "tellows": {
                "url": None,
                "notes": None,
                "score": None
            }
        }
    }
    try:
        response = Requester(url=url).get()
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            output["reputation"]["tellows"]["url"] = url
            output["reputation"]["tellows"]["notes"] = [string.strip() for string in soup.find("div", {"class": "card-body"}).find_all(text=True, recursive=False) if string.strip()]
            score_soup = soup.find("img", {"class": "scoreimage"}).get("alt")
            output["reputation"]["tellows"]["score"] = int(score_soup.split("Score ",1)[1])
        else:
            abort(500, description="Failed to fetch data from Tellows")
    except Exception as e:
        # TODO: Add a log
        abort(500, description=f"Failed to fetch data from Tellows: {e}")

    return output
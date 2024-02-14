from app.utils.Requester import Requester
from bs4 import BeautifulSoup

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
        with Requester(url=url).get() as response:
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                output["reputation"]["tellows"]["url"] = url
                output["reputation"]["tellows"]["notes"] = [string.strip() for string in soup.find("div", {"class": "card-body"}).find_all(text=True, recursive=False) if string.strip()]
                score_soup = soup.find("img", {"class": "scoreimage"}).get("alt")
                output["reputation"]["tellows"]["score"] = int(score_soup.split("Score ",1)[1])
    except Exception as e:
        pass

    return output
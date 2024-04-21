from app.utils.Requester import Requester
from app.utils.tools import get_countries, get_country
from flask import abort

def get_person_info(firstname: str, lastname: str) -> tuple:

        # Initialisation des variables de sortie
        output_gender = {"value": None, "probability": None}
        output_country = None

        # Nationalize
        params = {
            "name": f"{firstname.lower()}"
        }
        response = Requester(url=f"https://api.genderize.io", params=params).get()
        
        try:
            if response and response.status_code == 200:
                parsed = response.json()
                output_gender["value"] = parsed['gender']
                output_gender["probability"] = parsed['probability']
            else:
                abort(500, description="Failed to fetch data from Genderize")
        except Exception as e:
            abort(500, description=f"Failed to fetch data from Genderize: {e}")
        
        # Genderize
        params = {
            "name": f"{firstname.lower()}"
        }
        response = Requester(url=f"https://api.nationalize.io", params=params).get()
        
        try:
            if response and response.status_code == 200:
                parsed = response.json()
                output_country = parsed['country']

                countries = get_countries()

                for country in output_country:
                    fetch_country = get_country(countries, country['country_id'])
                    if fetch_country:
                        country['name'], country['flag'] = fetch_country
                        del country['country_id']
                    else:
                        output_country.remove(country)
            else:
                abort(500, description="Failed to fetch data from Nationalize")
        except Exception as e:
             abort(500, description=f"Failed to fetch data from Nationalize: {e}")

        return output_gender, output_country
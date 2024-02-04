import requests

def get_person_info(firstname, lastname):
        output_gender = {"value": None, "probability": None}
        output_country = None

        try:
            x = requests.get(f"https://api.genderize.io?name={firstname.lower()}")
            x.raise_for_status()
            parsed = x.json()
            output_gender["value"] = parsed['gender']
            output_gender["probability"] = parsed['probability']
        except requests.exceptions.RequestException as e:
            pass

        try:
            x = requests.get(f"https://api.nationalize.io?name={firstname.lower()}")
            x.raise_for_status()
            parsed = x.json()
            output_country = parsed['country']
        except requests.exceptions.RequestException as e:
            pass

        return output_gender, output_country
import config
import requests
from datetime import datetime, timedelta

CITY_CODE_SEARCH_API_KEY = config.city_code_search_api_key
PRICE_FLIGHT_API_KEY = config.price_flight_api_key

class FlightSearch:

    def get_city_codes(self, location):
        # GET CITY CODES IF EMPTY
        location_endpoint = "https://tequila-api.kiwi.com/locations/query"
        location_input = location

        location_params = {
            "apikey": CITY_CODE_SEARCH_API_KEY,
            "term": socation_input,
            "locale": "en-US",
            "location-types": "city",
        }

        response = requests.get(url=location_endpoint, params=location_params)
        response.raise_for_status()
        data = response.json()["locations"]
        city_code = data[0]["code"]

        return city_code

    def get_flight_prices(self, from_location, to_location):

        now = datetime.now()
        tomorrow = now + timedelta(days=1)
        tomorrow_str = tomorrow.strftime("%d/%m/%Y")
        tomorrow_plus_six = now + timedelta(6*30)
        tomorrow_plus_six_str = tomorrow_plus_six.strftime("%d/%m/%Y")

        price_endpoint = "https://tequila-api.kiwi.com/v2/search"
        price_params = {
            "fly_from": f"city:{from_location}",
            "fly_to": f"city:{to_location}",
            "date_from": tomorrow_str,
            "date_to": tomorrow_plus_six_str,
            "flight_type": "round",
            "max_stopovers": 1,
            "curr": "USD"
        }

        headers = {
            "apikey": PRICE_FLIGHT_API_KEY
        }

        response = requests.get(url=price_endpoint, params=price_params, headers=headers)
        data = response.json()["data"]

        return data[0]["price"]


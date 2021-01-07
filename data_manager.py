import config
import requests

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def fill_city_code(self, location_code, id):
        post_endpoint = config.fill_city_endpoint
        params = {
            "price": {
                "iataCode": location_code,
            },
        }
        response =requests.put(url=f"{post_endpoint}{id}", json=params)
        print(response.text)

    def get_data_from_sheet(self):
        get_endpoint = config.get_data_endpoint
        response = requests.get(url=get_endpoint)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]

        return self.destination_data
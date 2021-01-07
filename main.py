from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

flight_search = FlightSearch()
data_manager = DataManager()
notification = NotificationManager()


def fill_city_codes(city_name, city_id):
    city_code = flight_search.get_city_codes(city_name)
    data_manager.fill_city_code(city_code, city_id)

    return city_code


def main():
    departure_city = "FRA"
    data = data_manager.get_data_from_sheet()
    cities = [city["city"] for city in data]
    for destination in range(len(cities)):
        to_city = data[destination]["city"]
        city_id = data[destination]["id"]
        if data[destination]["iataCode"] == "":
            city_code = fill_city_codes(to_city, city_id)
        else:
            city_code = data[destination]["iataCode"]

        actual_price = flight_search.get_flight_prices(departure_city, city_code)
        max_price = data[destination]["lowestPrice"]
        print(f"New Price: {actual_price} - old Price: {max_price}")
        if actual_price < max_price:
            subject = f"New Flight Prices to {to_city}"
            message = f"\nActual Price from {departure_city} to {to_city} has dropped to: ${actual_price}!\n" \
                      f"That's ${max_price - actual_price} lower than max price!"
            notification.send_mail(message, subject)

main()

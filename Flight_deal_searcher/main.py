import requests_cache
from data_manager import DataManager
from datetime import datetime,timedelta
from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from notification_manager import NotificationManager


requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

sheet_data = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

destinations = sheet_data.get_flight_data()

outbound_date = (datetime.today()).strftime("%Y-%m-%d")
return_date = (datetime.today() + timedelta(days=7)).strftime("%Y-%m-%d")


for city in destinations:

    flight_info = flight_search.check_flight(
        departure_id = "LHR",
        arrival_id = city["code"],
        outbound_date =outbound_date,
        return_date=return_date
    )

    cheapest_flight = find_cheapest_flight(flight_info,return_date)
    print(f"Flight to {city['city']}: EUR {cheapest_flight.price}")

    if cheapest_flight.price != "N/A":
        print(f"Flight found to {city['city']} for {cheapest_flight.price} EUR")

        if cheapest_flight.price < city["lowestPrice"]:
            print(f"Super deal!The price is lower than {cheapest_flight.price} EUR")
            sheet_data.change_the_price(
                row_id=city["id"],
                new_price=cheapest_flight.price
            )
            message = f"Low price alert! Only {cheapest_flight.price} EUR to fly from LON to {city['city']}, from {cheapest_flight.out_date} to {cheapest_flight.return_date}."
            #notification_manager.send_notification(message)
    else:
        print(f"There are no flights available for {city['city']}.")








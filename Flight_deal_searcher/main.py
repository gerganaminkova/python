from turtledemo.round_dance import stop

import requests_cache
from twilio.rest.preview_iam.versionless.organization import user

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

user_data = sheet_data.get_customer_email()
customer_emails = [row["what'sYourEmail?"] for row in user_data]

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
        if cheapest_flight.price < city["lowestPrice"]:
            print(f"Super deal for a DIRECT flight! Lower than {city['lowestPrice']} EUR")
            sheet_data.change_the_price(
                row_id=city["id"],
                new_price=cheapest_flight.price
            )
            message = (f"Low price alert! Only {cheapest_flight.price} EUR to fly DIRECT from LON to {city['city']}"
                       f", from {cheapest_flight.out_date} to {cheapest_flight.return_date}.")

            notification_manager.send_email(email_list=customer_emails,message_body=message)

    else:
        print(f"No direct flights to {city['city']}. Searching for indirect flights...")
        stopover_flights = flight_search.check_flight(
            departure_id="LHR",
            arrival_id=city["code"],
            outbound_date=outbound_date,
            return_date=return_date,
            is_direct=False
        )
        cheapest_flight= find_cheapest_flight(stopover_flights, return_date)
        print(f"Indirect flight tp {city['city']}: EUR {cheapest_flight.price}")

        if cheapest_flight.price != "N/A" and cheapest_flight.price < city["lowestPrice"]:
            print(f"🎉 Super deal for an INDIRECT flight! Lower than {city['lowestPrice']} EUR")
            sheet_data.change_the_price(
                row_id=city["id"],
                new_price=cheapest_flight.price
            )
            message = (f"Low price alert! Only {cheapest_flight.price} EUR to fly with {cheapest_flight.stops} "
                       f"stop(s) from LON to {city['city']}, from {cheapest_flight.out_date} "
                       f"to {cheapest_flight.return_date}.")

            # notification_manager.send_notification(message)
            notification_manager.send_email(email_list=customer_emails,message_body=message)







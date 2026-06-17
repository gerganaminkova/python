#  Flight Deal Searcher ✈️

An automated Python application that monitors live flight prices for your favorite destinations. The program reads target locations from a Google Sheet, searches for the cheapest current flights using Google Flights data, caches the requests to optimize performance, and automatically updates the spreadsheet while sending an SMS alert if a price drops below your budget.

---

## Features

* **Google Sheets Integration:** Uses the Sheety API to dynamically read vacation destinations and log new lowest prices.
* **Real-time Flight Search:** Powered by SerpAPI (Google Flights API) to fetch live pricing, departure times, and carrier details.
* **Smart Request Caching:** Utilizes `requests_cache` to cache flight search results, saving API credits and accelerating execution.
* **Robust Error Handling:** Built-in protection against missing flight data (`N/A` handling) to prevent application crashes.
* **Instant SMS Notifications:** Fully integrated with the Twilio API to send text alerts the moment a flight deal is found.
* **Automated Email Club Alerts:** Integrated with `smtplib` to email all retrieved customers simultaneously when a budget-friendly flight is located.
---

##  Third-Party APIs Used

This project relies on the following external services:
* **Google Sheet Data Management:** [Sheety API](https://sheety.co/)
* **Flight Data Search:** [SerpAPI Google Flights API](https://serpapi.com/google-flights-api)
* **SMS Delivery Service:** [Twilio Messaging API](https://www.twilio.com/docs/messaging/quickstart/python)
* **Email Delivery Service:** Gmail SMTP Server (`smtp.gmail.com`)
---

##  Tech Stack & Imports

The application leverages the following Python built-in and third-party modules:
* `requests` & `requests_cache` — For handling optimized API HTTP requests.
* `twilio.rest` — For managing SMS notifications through Twilio.
* `python-dotenv` & `os` — For securely loading environment variables.
* `datetime` & `timedelta` — For dynamic departure and return date calculations.

---

##  Setup & Installation

1. Clone this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install requests requests-cache python-dotenv twilio
# Gym Class Auto-Booker 

This project is a Python script that uses Selenium WebDriver to automate the process of booking gym classes on the [AppBrewery Gym Portal](https://appbrewery.github.io/gym/). 

The script logs into the system, finds all classes for **Tuesday (Tue)** and **Thursday (Thu)** at **6:00 PM**, books your spot (or adds you to the waitlist), and finally automatically verifies whether the reservations were successful on the "My Bookings" page.

## Key Features

* **Automated Login:** Logs into your account using hidden credentials from a `.env` file.
* **Targeted Booking:** Filters workouts by specific days (Tuesday/Thursday) and time (6:00 PM).
* **Status Management:** Intelligently recognizes if a class is already booked, has open spots, or requires joining a waitlist.
* **Resilience (Retry Mechanism):** Built-in retry function (up to 7 attempts) to handle slow-loading elements and `TimeoutException` errors gracefully.
* **Session Persistence:** Uses a local Chrome profile (`chrome_profile`) to save cookies and session states for faster future runs.
* **Automated Verification:** After booking, the script navigates to "My Bookings", cross-references the expected number of bookings with the actual ones, and outputs a detailed report to the console.

## Prerequisites

Before running the script, ensure you have the following installed:

* [Python 3.7+](https://www.python.org/downloads/)
* Google Chrome browser

You will also need the following Python libraries:
* `selenium`
* `python-dotenv`

##  Installation and Setup

**1. Clone or download the project**

**2. Install the required dependencies**
Open your terminal in the project directory and run:
```bash
pip install selenium python-dotenv
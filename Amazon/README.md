# Amazon Price Tracker Alert

A Python automation script that tracks the price of a specific product on Amazon. It scrapes the product page and automatically sends an email notification if the price drops below a user-defined target, ensuring you never miss a good deal.

## Features
* **Web Scraping:** Uses `BeautifulSoup` and `requests` with custom HTTP headers to bypass basic bot protections and extract live price data from Amazon.
* **Data Parsing:** Accurately extracts and combines the whole number and fractional parts of the price tag into a usable float format.
* **Email Automation:** Utilizes the built-in `smtplib` library to establish a secure TLS connection and send automated email alerts.
* **Secure Configuration:** Protects sensitive information (like email passwords and SMTP addresses) using environment variables via the `python-dotenv` package.

##  Technologies Used
* Python 3
* [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) (Web Scraping)
* [Requests](https://pypi.org/project/requests/) (HTTP requests)
* `smtplib` (Email protocol client)
* [Python-dotenv](https://pypi.org/project/python-dotenv/) (Environment variable management)


### 1. Local Environment Setup
1. Clone this repository.
2. Install the required Python packages:
   ```bash
   pip install bs4 requests python-dotenv
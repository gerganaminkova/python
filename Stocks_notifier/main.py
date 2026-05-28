import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client
from datetime import datetime, timedelta

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_KEY = os.environ.get("STOCK_KEY")

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = os.environ.get("NEWS_KEY")

ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
AUTH_TOKEN= os.environ.get("AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
MY_NUMBER = os.environ.get("MY_NUMBER")


parameters_stock={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_KEY,
}
response = requests.get(STOCK_ENDPOINT,params=parameters_stock )
response.raise_for_status()
stock_data = response.json()


data_list = [value for (key, value) in stock_data["Time Series (Daily)"].items()]
yesterday_closing_value = float(data_list[0]["4. close"])

pre_yesterday_closing_value = float(data_list[1]["4. close"])
difference = abs(yesterday_closing_value - pre_yesterday_closing_value)

percentage = (difference/pre_yesterday_closing_value)*100


yesterday_date = datetime.now() - timedelta(days=1)
formatted_date = yesterday_date.strftime("%Y-%m-%d")
if percentage > 0.1:

    parameters_news={
        "q":COMPANY_NAME,
        "from":formatted_date,
        "sortBy":"popularity",
        "apiKey":NEWS_KEY
    }

    r = requests.get(NEWS_ENDPOINT, params=parameters_news)
    r.raise_for_status()
    news_data = r.json()

    three_articles = news_data["articles"][:3]

    formatted_articles = [f"Headline: {article['title']} \nBrief: {article['description']}"
                          for article in three_articles]

    up_down = "🔺" if difference > 0 else "🔻"

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=f"{STOCK_NAME}: {up_down}{round(percentage)}% \n{article}",
            from_=TWILIO_PHONE_NUMBER,
            to=MY_NUMBER
        )


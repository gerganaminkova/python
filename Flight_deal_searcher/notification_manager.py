import os
from dotenv import load_dotenv
from twilio.rest import Client

class NotificationManager:
    def __init__(self):
        load_dotenv()
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.my_number = os.getenv("MY_NUMBER")
        self.twilio_number = os.getenv("TWILIO_NUMBER")
        self.client = Client(account_sid, auth_token)

    def send_notification(self,message):
        ms = self.client.messages.create(
            body=message,
            from_=self.twilio_number,
            to=self.my_number
        )
        print(ms.status)

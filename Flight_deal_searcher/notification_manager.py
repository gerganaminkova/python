import os
import smtplib

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

        self.smtp_address = os.getenv("SMTP_ADDRESS")
        self.my_email = os.getenv("MY_EMAIL")
        self.my_password = os.getenv("MY_EMAIL_PASSWORD")

    def send_notification(self,message):
        ms = self.client.messages.create(
            body=message,
            from_=self.twilio_number,
            to=self.my_number
        )
        print(ms.status)

    def send_email(self,email_list,message_body):
        with smtplib.SMTP(self.smtp_address, port=587) as connection:
            connection.starttls()
            connection.login(self.my_email, self.my_password)

            for email in email_list:
                email_message = f"Subject:New Flight Deal Found! 🎉\n\n{message_body}"

                connection.sendmail(
                    from_addr=self.my_email,
                    to_addrs=email,
                    msg=email_message.encode('utf-8')
                )

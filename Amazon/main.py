import os
import smtplib
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv


AMAZON_URL="https://www.amazon.co.uk/Instant-WhisperQuiet-Multi-Cooker-Smart-Cooker/dp/B0BYSZYRZH/ref=sr_1_4?crid=1D9X77N749N50&dib=eyJ2IjoiMSJ9.-y13_Mhv9lyV1Vsrg17m8vjf1gMAbnxRv59HvxuC_vcQr3nFtn6vA6V0bUmsrSwi4MP4x5LzQm8bqNg7fWKvsH8qvvS6cqfZkQyXEC1WNgNy0LqzCa36CITjt413GCJeaKc3cm08Da1LiEQZs2cREjzbuR2LWR0MgQ6Pa_N2amNmmNFb1oWgnedkz2jwF4U1G_xjY4iVAk18VU52OJ3XLfVyHwlbVgpFUeU2Qx7ko7g._0n-s2mWVOy2m0_SAM6bk6__fzzREQnkUzz4Uh3oFPo&dib_tag=se&keywords=instant%2Bpot%2Bduo%2Bplus&qid=1782115039&sprefix=instant%2Bpot%2Bduo%2Bplu%2Caps%2C207&sr=8-4&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(AMAZON_URL,headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find("span", class_="a-price-whole")
fraction = soup.find("span", class_="a-price-fraction")
combined_number = float(price.get_text() + fraction.get_text())

print(combined_number)

load_dotenv()
smtp_address=os.getenv("SMTP_ADDRESS")
email_password=os.getenv("MY_EMAIL_PASSWORD")
my_email=os.getenv("MY_EMAIL")


if combined_number < 300.00:
    with smtplib.SMTP(smtp_address, port=587) as connection:
        connection.starttls()
        connection.login(my_email,email_password)

        subject = "New deal for thе pot"

        body=(f"Instant Pot Duo Plus with WhisperQuiet Multi-Cooker 5.7L - Black,"
              f" Electric Pressure Cooker, is now {combined_number}$ {AMAZON_URL}")

        email_message = f"Subject: {subject}\n\n{body}"

        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=email_message.encode('utf-8')
        )

import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = 0
        self.down = 0
        self.Y_URL = "https://app.100daysofpython.dev/services/y/login"

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)



    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        wait = WebDriverWait(self.driver, 15)
        long_wait = WebDriverWait(self.driver, 120)


        accept_btn = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        accept_btn.click()
        sleep(2)


        go_btn=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a")))
        go_btn.click()

        # cancel_btn = long_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "svg-icon")))
        # cancel_btn.click()

        long_wait.until(EC.url_contains("result"))

        download_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".download-speed")))
        self.down = download_element.text

        upload_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".upload-speed")))
        self.up = upload_element.text

    def tweet_at_provider(self, down , up):
        load_dotenv()
        Y_GMAIL = os.getenv('Y_GMAIL')
        Y_PASSWORD = os.getenv('Y_Password')

        self.driver.get("https://app.100daysofpython.dev/services/y/login")


        wait = WebDriverWait(self.driver, 10)

        email = self.driver.find_element(By.ID, "email")
        email.send_keys(Y_GMAIL)

        password = self.driver.find_element(By.ID, "password")
        password.send_keys(Y_PASSWORD)

        log_in_btn = self.driver.find_element(By.CLASS_NAME, "y-login-submit")
        log_in_btn.click()

        post_button = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/nav/button')))
        post_button.click()

        complain_line = self.driver.find_element(By.ID, "modal-compose")
        complain_line.send_keys(f"Hey Internet Provider, why is my internet speed "
                                f"{down}down/{up}up when i pay for 150down/10up?")

        post_btn = self.driver.find_element(By.ID, "modal-post-btn")
        post_btn.click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider(bot.down, bot.up)



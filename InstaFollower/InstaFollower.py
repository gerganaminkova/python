import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

URL="https://app.100daysofpython.dev/services/share-a-naan/welcome"

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        load_dotenv()
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")
        self.driver.get(URL)

        email_bar = self.driver.find_element(By.NAME, "username")
        email_bar.send_keys(email)

        password_bar = self.driver.find_element(By.NAME, "password")
        password_bar.send_keys(password)

        log_in_button = self.driver.find_element(By.CSS_SELECTOR, "button.naan-welcome-submit")
        log_in_button.click()

        save_info_pop_up = self.driver.find_element(By.CLASS_NAME, "naan-popup-dismiss")
        save_info_pop_up.click()

        notification_pop_up = self.driver.find_element(By.CSS_SELECTOR, "button.naan-popup-dismiss")
        notification_pop_up.click()

    def find_followers(self):
        search_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/nav/button")
        search_button.click()

        chefsteps_profile = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='chefsteps']")))
        try:
            chefsteps_profile.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", chefsteps_profile)

    def follow(self):
        followers = self.driver.find_element(By.CSS_SELECTOR, "a.naan-followers-link")
        followers.click()

        scrollable_popup = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".followers-scroll")))
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".followers-scroll")))

        for i in range(10):
            buttons = scrollable_popup.find_elements(By.CSS_SELECTOR, "button.naan-follow-btn:not(.is-following)")

            for button in buttons:
                 button.click()

            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scrollable_popup)
            sleep(2)



bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()



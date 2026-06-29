import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException,ElementClickInterceptedException

load_dotenv()

TINDER_DOG_URL = "https://app.100daysofpython.dev/services/tindog/u/9rkuObMsmSHEklcVUSWfzNFmmJ2P5GDR"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(TINDER_DOG_URL)

wait = WebDriverWait(driver, 10)

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Log in"]')))
login_button.click()

facebark_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'btn-facebark')))
facebark_button.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# FACEBOOK LOG IN

email=os.getenv('FACEBARK_EMAIL')
password=os.getenv('FACEBARK_PASSWORD')

facebark_email = driver.find_element(By.ID, "email")
facebark_email.send_keys(email)

facebark_password = driver.find_element(By.ID, "pass")
facebark_password.send_keys(password)

confirm_button = driver.find_element(By.XPATH,"/html/body/div[2]/div/form/button")
confirm_button.click()

driver.switch_to.window(base_window)
print(driver.title)

# POP UPS

location_allowance = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/form/button")))
location_allowance.click()

notification_allowance = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/form/button[2]")))
notification_allowance.click()

cookies_acceptance = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/form/button")))
cookies_acceptance.click()


# SLIPPING

for i in range(20):
    sleep(1)
    try:
        like_button = driver.find_element(By.CLASS_NAME, "btn-like")
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup_close_button =  driver.find_element(By.LINK_TEXT, "Back to Tindog")
            match_popup_close_button.click()

        except NoSuchElementException:
            sleep(2)

    except NoSuchElementException:
        sleep(2)








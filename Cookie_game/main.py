from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "langSelect-EN")))

language = driver.find_element(By.ID, "langSelect-EN")
language.click()

sleep(2)

cookies_btn = driver.find_element(By.CLASS_NAME, "cc_btn_accept_all")
cookies_btn.click()

big_cookie = driver.find_element(By.ID, "bigCookie")

money = driver.find_element(By.ID, "cookieNumbers")


item_ids = [f"product{i}" for i in range(20)]

wait_time = 5
timeout = time() + wait_time
five_min = time() + 60 * 5

while True:
    big_cookie.click()
    if time() > timeout :
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            cookie_text = cookies_element.text
            cookie_count = int(cookie_text.split()[0].replace(",", ""))

            affordable_upgrades = driver.find_elements(By.CSS_SELECTOR, ".product.enabled")

            if affordable_upgrades:
                most_expensive_upgrade = affordable_upgrades[-1]
                most_expensive_upgrade.click()

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")

        timeout = time() + wait_time

    if time() > five_min:
        try:
            cookies_element = driver.find_element(By.ID, value="cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Cookie not found")
        break





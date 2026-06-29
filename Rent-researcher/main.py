import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# WEB SCRAPPING
zilllow_url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(zilllow_url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

prices = []
links = []
addresses = []

for price_element in soup.find_all('span', attrs={'class': 'PropertyCardWrapper__StyledPriceLine'}):
    raw_price = price_element.text
    clean_price  = raw_price.split('+')[0].split('/')[0].split(' ')[0]
    clean_price = clean_price.replace(",", "")
    prices.append(clean_price)


for link in soup.find_all('a', attrs={'class': "property-card-link"}):
    links.append(link.get('href'))

for address_elements in soup.find_all('address', attrs={'data-test': "property-card-addr"}):
    clean_address = address_elements.text.strip()
    addresses.append(clean_address)

# AUTOMATION
GOOGLE_DOCS_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfOrI2KrSJ4gpAw2_YISPfAyzmouPGRJluKcBVZjVSQYBTNSA/viewform?usp=publish-editor"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

for i in range(len(prices)):
    driver.get(GOOGLE_DOCS_URL)
    inputs = driver.find_elements(By.CSS_SELECTOR, 'input.whsOnd.zHQkBf')

    inputs[0].send_keys(addresses[i])
    inputs[1].send_keys(prices[i])
    inputs[2].send_keys(links[i])

    submit_button = driver.find_element(By.CSS_SELECTOR, 'span.NPEfkd.RveJvd.snByac')
    submit_button.click()

    wait = WebDriverWait(driver, 10)
    another_response_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Изпращане на друг отговор"))
    )
    another_response_link.click()





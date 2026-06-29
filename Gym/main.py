import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException

load_dotenv()
email=os.getenv("ACCOUNT_EMAIL")
password=os.getenv("ACCOUNT_PASSWORD")


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")


def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            sleep(1)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

wait = WebDriverWait(driver, 10)

def login():

    login_btn = driver.find_element(By.ID,"login-button")
    login_btn.click()

    wait.until(EC.presence_of_element_located((By.NAME,"email")))

    email_input = driver.find_element(By.NAME,"email")
    email_input.clear()
    email_input.send_keys(email)

    password_input = driver.find_element(By.NAME,"password")
    password_input.clear()
    password_input.send_keys(password)

    login_final_btn = driver.find_element(By.ID,"submit-button")
    login_final_btn.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[id^='class-card-']")))

retry(login, description='login')


def book_class(btn):
    btn.click()
    wait.until(lambda d: btn.text in ["Booked", "Waitlisted"])
    return btn.text

class_cards = driver.find_elements(By.CSS_SELECTOR,"div[id^='class-card-']")

booked_count = 0
waitlist_count = 0
already_booked_count = 0

processed_classes = []

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    if "Tue" in day_title or "Thu" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

            class_info = f"{class_name} on {day_title}"

            if button.text == "Booked":
                print(f"✓ Already booked: {class_info}")
                already_booked_count += 1
                processed_classes.append(f"[Booked] {class_info}")
            elif button.text == "Waitlisted":
                print(f"✓ Already on waitlist: {class_info}")
                already_booked_count += 1
                processed_classes.append(f"[Waitlisted] {class_info}")
            elif button.text == "Book Class":
                retry(lambda: book_class(button), description="Booking")
                print(f"✓ Successfully booked: {class_info}")
                booked_count += 1
                processed_classes.append(f"[New Booking] {class_info}")
                sleep(0.5)
            elif button.text == "Join Waitlist":
                retry(lambda: book_class(button), description="Waitlisting")
                print(f"✓ Joined waitlist for: {class_info}")
                waitlist_count += 1
                processed_classes.append(f"[New Waitlist] {class_info}")
                sleep(0.5)




total_booked = already_booked_count + booked_count + waitlist_count
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

def get_my_bookings():
    my_booking_link = wait.until(EC.element_to_be_clickable((By.ID, "my-bookings-link")))
    my_booking_link.click()

    wait.until(EC.presence_of_element_located((By.ID, "my-bookings-page")))
    sleep(2)
    cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

    if not cards:
        raise TimeoutException("No booking cards found - page may not have loaded")
    return cards


verified_count = 0
all_cards = retry(get_my_bookings, description="fetching my bookings")

for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        if("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        pass


print(f"\n --- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if total_booked == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")



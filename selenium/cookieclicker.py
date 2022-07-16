from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os

load_dotenv()
driver_path = os.getenv('CHROME_DRIVER')
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Auto-clicker for the cockieclicker game
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(3)
navigate = driver.find_element(By.ID, "langSelect-EN")
navigate.click()
time.sleep(2)
submit = driver.find_element(By.ID, "bigCookie")
start_time = time.time()
seconds = 300
interval = 1
upgrade_time = interval
upgrade_count = 1
while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    submit.click()
    cookies = int(driver.find_element(By.ID, "cookies").text.split()[0].replace(',', ""))
    # print(f'{cookies}')
    if elapsed_time >= upgrade_time:
        unlocked = list(driver.find_elements(By.CLASS_NAME, "unlocked"))
        for item in reversed(unlocked):
            item.click()
        # upgrade = unlocked[-1].text.split("\n")[1]
        # unlocked[-1].click()
        if len(unlocked) > upgrade_count:
            interval += 1
        upgrade_time = elapsed_time + interval
        upgrade_count = len(unlocked)
            # break
    if elapsed_time > seconds:
        cookie_per_sec = driver.find_element(By.ID, "cookiesPerSecond").text
        print(f"cookie(s) {cookie_per_sec}")
        print(f"Finished iterating in: {int(elapsed_time)} seconds")
        break
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()
driver_path = os.getenv('CHROME_DRIVER')
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Get Events in python website
driver.get("https://www.python.org/")
event_dates = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
events = {i: {"time": item.text, "name": event_names[i].text} for i, item in enumerate(event_dates)}
print(events)
driver.close()
# driver.quit()

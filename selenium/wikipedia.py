from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()
driver_path = os.getenv('CHROME_DRIVER')
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Sample auto-search in wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# count = driver.find_element(By.CSS_SELECTOR, '#articlecount a').text
count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# count.click()

link_tab = driver.find_element(By.LINK_TEXT, "View source")
# link_tab.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# search_button = driver.find_element(By.ID, "searchButton")
# search_button.click()

# driver.close()








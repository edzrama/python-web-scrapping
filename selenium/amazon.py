from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()
driver_path = os.getenv('CHROME_DRIVER')
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com/ASUS-Gaming-VG27AQ-G-SYNC-Monitor/dp/B07WQ4FXY9")

# Get description and price of the item
item = driver.find_element(By.ID, "productTitle").text
price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
# price = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]').text
print(f'Item: {item}')
print(f'Price: {price}')

driver.close()
# driver.quit()

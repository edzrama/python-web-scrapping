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

# auto sign-up to newsletter
driver.get("http://secure-retreat-92358.herokuapp.com/")
f_name = driver.find_element(By.NAME, "fName")
l_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
submit = driver.find_element(By.CLASS_NAME, "btn")
f_name.send_keys("John")
l_name.send_keys("Doe")
email.send_keys("johndoe@test.com")
time.sleep(2)
submit.click()









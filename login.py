import os
from selenium.webdriver.chrome.options import Options
import time
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options() 
path = os.getcwd() + "\\UserData"
options.add_argument(f"--user-data-dir={path}")

driver = webdriver.Chrome('C:/Users/LENOVO/Downloads/chromedriver_win32/chromedriver.exe', options=options)
driver.get('https://www.linkedin.com')
time.sleep(2)

#make sure that the domain is already open
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name = 'session_key']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name = 'session_password']")))

#ID = os.environ.get("LinkedIn_username")
#assword = os.environ.get("LinkedIn_pass")
username.send_keys(config("LinkedIn_username"))
password.send_keys(config("LinkedIn_pass"))

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(2)

driver.quit()





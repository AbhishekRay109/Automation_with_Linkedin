from ast import arguments
from fileinput import close
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

#from symbol import argument

driver = webdriver.Chrome('C:/Users/LENOVO/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://www.linkedin.com')
time.sleep(2)

#******** LOG IN ***********

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name = 'session_key']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name = 'session_password']")))

username.clear()
password.clear()

username.send_keys('abhishekray1092@gmail.com')
password.send_keys('itsmeabhi@123')

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(2)

search_box = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))
search_box.clear()
keyword = "Masters Computer Science Student"
search_box.send_keys(keyword)
search_box.send_keys(Keys.ENTER)

driver.get('https://www.linkedin.com/search/results/people/?keywords=Rv&origin=SWITCH_SEARCH_VERTICAL&sid=wnd')
time.sleep(5)
i=1
while (i != 10):
    all_buttons = driver.find_elements(By.TAG_NAME,'button')
    connect_button = [btn for btn in all_buttons if btn.text == "Connect"]

    for btn in connect_button:
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(5)
        note = driver.find_element(By.XPATH,"//button[@aria-label = 'Add a note']")
        driver.execute_script("arguments[0].click();", note)
        #time.sleep(2)

        adding_note = driver.find_element(By.XPATH,".//*[@id='custom-message']")
        adding_note.clear()
        custom_note = "CUSTOM NOTE"
        adding_note.send_keys(custom_note)
        sent = driver.find_element(By.XPATH,".//*[@aria-label='Send now']").click()
        #not_found =  driver.find_element(By.XPATH,"//button[@aria-label = 'Dismiss']")
        #driver.execute_script("arguments[0].click();", close)
        time.sleep(2)
    i = i+1
    next_page = driver.find_element(By.XPATH,".//*[@aria-label='Next']")
    next_page.click()
    time.sleep(10)


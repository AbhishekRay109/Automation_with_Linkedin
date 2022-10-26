from cProfile import label
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import time
import os

options = Options() 
path = os.getcwd() + "\\UserData"
options.add_argument(f"--user-data-dir={path}")

driver = webdriver.Chrome('C:/Users/LENOVO/Downloads/chromedriver_win32/chromedriver.exe', options=options)

driver.get('https://www.linkedin.com')


search_box = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))

search_box.clear()
keyword = "Masters Computer Science Student"
i=0
while i!=len(keyword):
    search_box.send_keys(keyword[i])
    i+=1
    #time.sleep(randint(1,3))
    

search_box.send_keys(Keys.ENTER)
driver.implicitly_wait(10)
people = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='People']")))
driver.execute_script ("arguments[0].click();",people)

#time.sleep(randint(5,10))

all_filter = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='All filters']")))
driver.execute_script ("arguments[0].click();",all_filter)

#time.sleep(randint(5,10))

us = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='United States']")))
driver.execute_script ("arguments[0].click();",us)

#time.sleep(randint(5,10))

show_result = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,"search-reusables__secondary-filters-show-results-button")))

driver.execute_script ("arguments[0].click();",show_result)

time.sleep(randint(5,10))


file1 = open(r"connections",'a')



all_buttons = driver.find_elements(By.TAG_NAME,'button')
connect_button = [btn for btn in all_buttons if btn.text == "Connect"]


for btn in connect_button:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(5)
    name = btn.get_attribute("aria-label")
    new_name = name[7:-11]
    file1.write(new_name)
    file1.write("\n")



    try:
        know = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='We don't know each other']")))
        driver.execute_script ("arguments[0].click();",know)
        connect2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Connect']")))
        driver.execute_script ("arguments[0].click();",connect2)
        connect3 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Connect']")))
        driver.execute_script ("arguments[0].click();",connect3)
    except:
        pass


    add_note = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Add a note']")))
    driver.execute_script ("arguments[0].click();",add_note)

    time.sleep(randint(5,10))


    adding_note = driver.find_element(By.XPATH,".//*[@id='custom-message']")
    adding_note.clear()
    custom_note = "CUSTOM NOTE"
    adding_note.send_keys(custom_note)

    sent = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Send']")))
    driver.execute_script ("arguments[0].click();",sent)


file1.close()   
time.sleep(10)
driver.quit()

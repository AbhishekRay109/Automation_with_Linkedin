from asyncore import write
from itertools import count
from random import randint
from tokenize import Name
from xml.etree.ElementTree import tostring
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os


options = Options() 
path = os.getcwd() + "\\UserData"
options.add_argument(f"--user-data-dir={path}")
driver = webdriver.Chrome('C:/Users/LENOVO/Downloads/chromedriver_win32/chromedriver.exe', options=options)

driver.get('https://www.linkedin.com')


network = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//span[@title='My Network']")))

driver.execute_script ("arguments[0].click();",network)
time.sleep(randint(5,10))


connections = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[normalize-space()='Connections']")))
driver.execute_script ("arguments[0].click();",connections)

time.sleep(randint(5,10))

elems = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"mn-connection-card__name")))


for elem in elems:
    found1 = 0
    file2 = open(r"connections",'r')
    name = elem.text
    for line in file2.readlines():
        if line.rstrip() == name:
            print(name)
            found1 = 1
            
            
    if found1 == 0:
        break



        

file2.close()
driver.quit()





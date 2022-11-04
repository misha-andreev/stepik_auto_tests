from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "link"
    driver = webdriver.Chrome()
    driver.get(link)

 
finally:
    time.sleep(5)
    driver.quit()
    
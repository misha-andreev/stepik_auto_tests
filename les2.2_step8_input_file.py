from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    driver = webdriver.Chrome()
    driver.get(link)

    firstname = driver.find_element(By.NAME, "firstname")
    firstname.send_keys("Mikhail")
    lastname = driver.find_element(By.NAME, "lastname")
    lastname.send_keys("Andreev")
    email = driver.find_element(By.NAME, "email")
    email.send_keys("email")

    upload = driver.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")
    upload.send_keys(file_path) 

    driver.find_element(By.TAG_NAME, "button").click()
 
finally:
    time.sleep(5)
    driver.quit()
    
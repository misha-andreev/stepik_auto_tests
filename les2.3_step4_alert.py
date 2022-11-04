from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
import time

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    driver = webdriver.Chrome()
    driver.get(link)

    driver.find_element(By.TAG_NAME, "button").click()
    alert = driver.switch_to.alert
    alert.accept()

    time.sleep(1)

    x = driver.find_element(By.ID, "input_value").text
    x = str(log(abs(12*sin(int(x)))))
    inputx = driver.find_element(By.ID, "answer")
    inputx.send_keys(x)
    driver.find_element(By.TAG_NAME, "button").click()
 
finally:
    time.sleep(5)
    driver.quit()
    
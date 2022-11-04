from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
import time

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    driver = webdriver.Chrome()
    driver.get(link)

    driver.find_element(By.TAG_NAME, "button").click()
    driver.switch_to.window(driver.window_handles[1])

    time.sleep(1)

    x = driver.find_element(By.ID, "input_value").text
    x = str(log(abs(12*sin(int(x)))))
    inputx = driver.find_element(By.ID, "answer")
    inputx.send_keys(x)
    driver.find_element(By.TAG_NAME, "button").click()
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(alert_text.split(': ')[1])
 
finally:
    driver.quit()
    
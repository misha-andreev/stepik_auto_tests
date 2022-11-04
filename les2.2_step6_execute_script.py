from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
import time

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    driver = webdriver.Chrome()
    driver.get(link)

    x = driver.find_element(By.ID, "input_value").text
    x = str(log(abs(12*sin(int(x)))))

    inputx = driver.find_element(By.ID, "answer")
    driver.execute_script("return arguments[0].scrollIntoView(true);", inputx)
    inputx.send_keys(x)


    driver.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    driver.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    driver.find_element(By.TAG_NAME, "button").click()
 
finally:
    time.sleep(5)
    driver.quit()
    
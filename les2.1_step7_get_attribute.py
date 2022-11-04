from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

def calculate(x):
	return log(abs(12 * sin(x)))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    driver = webdriver.Chrome()
    driver.get(link)

    chest = driver.find_element(By.ID, "treasure")
    x = int(chest.get_attribute("valuex"))
    y = calculate(x)

    inputx = driver.find_element(By.ID, "answer")
    inputx.send_keys(y)

    option1 = driver.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = driver.find_element(By.ID, "robotsRule")
    option2.click()

    button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()
 
finally:
    time.sleep(15)
    driver.quit()

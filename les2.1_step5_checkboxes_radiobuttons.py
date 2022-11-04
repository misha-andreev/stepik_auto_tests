from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

def calc(x):
  return str(log(abs(12*sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    driver = webdriver.Chrome()
    driver.get(link)
    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    num = calc(x)
    input_x = driver.find_element(By.ID, "answer")
    input_x.send_keys(num)
    
    option1 = driver.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()
    option2 = driver.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click()

    button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()
 
finally:
    time.sleep(15)
    driver.quit()
    
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    driver = webdriver.Chrome()
    driver.get(link)

    num1 = driver.find_element(By.ID, "num1")
    num1 = num1.text
    num2 = driver.find_element(By.ID, "num2")
    num2 = num2.text
    answer = str(int(num1) + int(num2))
    select = Select(driver.find_element(By.ID, "dropdown")) 
    select.select_by_value(answer)

    driver.find_element(By.TAG_NAME, "button").click()
 
finally:
    time.sleep(5)
    driver.quit()
    
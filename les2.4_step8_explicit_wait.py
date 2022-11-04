from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from math import log, sin

try:
	driver = webdriver.Chrome()
	driver.get("http://suninjuly.github.io/explicit_wait2.html")

	WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
	driver.find_element(By.XPATH, "//button[text()='Book']").click()

	x = driver.find_element(By.ID, "input_value").text
	x = str(log(abs(12*sin(int(x)))))
	inputx = driver.find_element(By.ID, "answer")
	inputx.send_keys(x)
	driver.find_element(By.XPATH, "//button[text()='Submit']").click()
	WebDriverWait(driver, 5).until(
        EC.alert_is_present()
    )
	alert = driver.switch_to.alert
	alert_text = alert.text
	print(alert_text.split(': ')[1])
 
finally:
    driver.quit()

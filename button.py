from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://translate.yandex.ru/"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.ID, "userButton")
button.click()


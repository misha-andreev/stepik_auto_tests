from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_service = Service(executable_path="/Users/mac/selenium/chromedriver")
driver = webdriver.Chrome(service=driver_service)

# PATH = "/Users/mac/selenium/chromedriver"
# driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")

search = driver.find_element(By.CLASS_NAME, "search-field")  # нашли элемент под именем s
search.send_keys("test")  # написали в элементе test 
search.send_keys(Keys.RETURN)  # нажали Enter

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )  # драйвер ждёт 10 сек, пока элемент main не появится на странице
    
    articles = main.find_elements(By.TAG_NAME, "article")  # в main нашли элементы с тэгом article
    for article in articles:
    	header = article.find_element(By.CLASS_NAME, "entry-summary")  # в каждом элементе с тэгом article нашли элемент с классом entry-summary
    	print(header.text)  # вывели все entry-summary

    time.sleep(5)

finally:
    driver.quit()  
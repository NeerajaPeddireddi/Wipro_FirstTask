import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://google.com")
time.sleep(5)

driver.execute_script("alert('Hello World')")

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://letcode.in/alert")
time.sleep(2)
driver.find_element(By.ID, "confirm").click()
print("Button clicked")

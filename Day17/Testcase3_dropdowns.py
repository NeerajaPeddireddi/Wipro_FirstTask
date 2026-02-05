import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/")
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Desktops").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Mac (1)").click()
time.sleep(2)
dropdown=Select(driver.find_element(By.ID,"input-sort"))
time.sleep(2)


options=dropdown.options
for option in options:
    print(option.text)

dropdown.select_by_index(4)
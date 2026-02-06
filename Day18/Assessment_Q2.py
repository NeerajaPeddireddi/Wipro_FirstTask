import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")

parent=driver.current_window_handle
driver.find_element(By.LINK_TEXT,"Click Here").click()
time.sleep(5)
for window in driver.window_handles:
    driver.switch_to.window(window)
    time.sleep(5)
    print("window handle:",driver.title)
    time.sleep(5)
for window in driver.window_handles:
    if window!=parent:
        driver.switch_to.window(window)
        time.sleep(5)
        driver.close()
driver.switch_to.window(parent)
print("Returned to Parent Window")
driver.quit()
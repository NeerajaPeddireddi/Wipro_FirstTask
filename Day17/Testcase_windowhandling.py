from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
options = Options()
options.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome(options=options)
driver.get("https://letcode.in/window")
time.sleep(5)
driver.find_element(By.ID,"multi").click()
# # wait until more than 1 window is opened
# WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
windows=driver.window_handles
for child in windows:
    driver.switch_to.window(child)
    time.sleep(10)
    print("current url",driver.current_url)
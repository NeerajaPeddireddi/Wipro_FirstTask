from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.get("https://www.amazon.in")
# driver.execute_script("alert('Hello Amazon')")
time.sleep(5)
driver.execute_script("window.scrollBy(0,900)")

# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# for i in range(0, 900, 50):   # scroll 50px at a time
#     driver.execute_script(f"window.scrollBy(0, 50)")
#     time.sleep(0.2)          # control speed here
#
# # Take screenshot
# driver.save_screenshot("amazon_scroll.png")
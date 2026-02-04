from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo")
driver.maximize_window()

print("Initial title:", driver.title)

driver.get("https://www.google.com/")
print("After navigating to Google:", driver.title)

time.sleep(3)

driver.back()
time.sleep(2)
print("Title after back:", driver.title)

driver.forward()
time.sleep(2)
print("Title after forward:", driver.title)


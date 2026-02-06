from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://letcode.in/frame")
driver.maximize_window()
driver.implicitly_wait(10)
iframe=driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(iframe)
driver.find_element(By.NAME,"fname").send_keys("neeru")
driver.find_element(By.NAME,"lname").send_keys("p")
driver.switch_to.default_content()
insight=driver.find_element(By.XPATH,"//p[text()=' Insight ']").is_displayed()
print("Insight is displayed:",insight)

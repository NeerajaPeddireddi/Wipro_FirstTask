from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.google.com")
title=driver.title
curren_url=driver.current_url
page_source=driver.page_source

print("Title:",title)
print("Current URl:",curren_url)
print(page_source)
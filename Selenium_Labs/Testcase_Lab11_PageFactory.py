from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from Selenium_Labs.Lab11_PageFactory import OpenCartActionsForLab4

driver=webdriver.Chrome()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()
driver.implicitly_wait(10)

# opencartobjlab3=OpenCartActionsForLab3(driver)
# opencartobjlab3.click_desktop()
# opencartobjlab3.click_mac()
# opencartobjlab3.click_name_az()
# opencartobjlab3.click_add_to_cart()
# opencartobjlab3.hover_cart()

opencartobjlab4=OpenCartActionsForLab4(driver)
opencartobjlab4.click_desktop()
opencartobjlab4.click_mac()
opencartobjlab4.click_name_az()
opencartobjlab4.click_add_to_cart()
opencartobjlab4.hover_cart()
opencartobjlab4.search_from_header("Mobiles")
opencartobjlab4.verify_search_text("Mobiles")

driver.quit()



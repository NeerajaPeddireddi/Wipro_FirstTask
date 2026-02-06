from pywin.dialogs import login
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from Day18.LoginPage_PageFactory import LoginPageFactory
from Day18.Loginpage import LoginPage

driver=webdriver.Chrome()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
loginobj=LoginPageFactory(driver)
loginobj.enter_username("Admin")
loginobj.enter_password("admin123")
loginobj.click_login()
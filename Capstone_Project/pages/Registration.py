from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ----------- LOCATORS ------------

    sign_up_btn = (By.LINK_TEXT, "My Account")



    email_input= (By.XPATH, "//input[@id='reg_email']")
    password_input = (By.XPATH, "//input[@id='reg_password']")

    register = (By.XPATH, "//input[@name='register']")

    # ----------- METHODS ------------

    def click_sign_up(self):
        self.wait.until(EC.element_to_be_clickable(self.sign_up_btn)).click()




    def enter_email(self, value):
        self.wait.until(
            EC.element_to_be_clickable(self.email_input)
        ).send_keys(value)
    def enter_password(self,name):
        self.wait.until(
            EC.visibility_of_element_located(self.password_input)
        ).send_keys(name)


    def click_register(self):
        self.wait.until(EC.element_to_be_clickable(self.register)).click()




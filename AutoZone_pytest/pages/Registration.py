from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ----------- LOCATORS ------------

    sign_up_btn = (By.LINK_TEXT, "Signup / Login")


    name_input = (By.XPATH, "//input[@data-qa='signup-name']")
    email_input= (By.XPATH, "//input[@data-qa='signup-email']")

    signup_btn = (By.XPATH, "//button[@data-qa='signup-button']")

    # ----------- METHODS ------------

    def click_sign_up(self):
        self.wait.until(EC.element_to_be_clickable(self.sign_up_btn)).click()

    def enter_name(self,name):
        self.wait.until(
            EC.visibility_of_element_located(self.name_input)
        ).send_keys(name)


    def enter_email(self, value):
        self.wait.until(
            EC.element_to_be_clickable(self.email_input)
        ).send_keys(value)


    def click_signupbtn(self):
        self.wait.until(EC.element_to_be_clickable(self.signup_btn)).click()




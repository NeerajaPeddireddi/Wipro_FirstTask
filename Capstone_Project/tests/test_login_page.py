# tests/test_login.py


import pytest
from prompt_toolkit.contrib.telnet.protocol import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Capstone_Project.pages.Login import LoginPage


def test_login_after_registration(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Open My Account page
    login_page.click_login()

    # Use credentials from registered_user fixture
    email = "Rani12@gmail.com"
    password = "Neeru@34523456"

    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_checkbox()  # optional
    login_page.click_loginbtn()




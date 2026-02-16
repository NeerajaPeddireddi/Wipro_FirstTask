import pytest
import random
import string
from AutoZone_pytest.pages.Registration import RegistrationPage


def generate_random_email():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"test{random_string}@gmail.com"


def test_user_registration(setup):

    driver = setup
    registration = RegistrationPage(driver)

    # Step 1: Click Sign In
    registration.click_sign_up()

    # Step 4:name
    registration.enter_name("Test")
    # Step 3: Enter Email OR Username
    email = generate_random_email()
    registration.enter_email(email)


    registration.click_signupbtn()

    # # Assertion
    # assert "Account" in driver.page_source or "Welcome" in driver.page_source

import pytest
import random
import string

from Capstone_Project.conftest import logger
from Capstone_Project.pages.Registration import RegistrationPage


def generate_random_email():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"tests{random_string}@gmail.com"


def test_user_registration(setup):
    logger.info("========== STARTING USER REGISTRATION TEST ==========")
    driver = setup
    registration = RegistrationPage(driver)

    # Step 1: Click Sign In
    logger.info("Clicking on Sign Up / My Account link")
    registration.click_sign_up()
    logger.info("Verifying registration page is loaded")
    assert registration.is_registration_page_loaded(), "Registration page did not load"
    # Step 2: Enter Email OR Username
    email = generate_random_email()
    password = "TestPassword123!@Bjl"
    logger.info(f"Generated Email: {email}")
    # Step 3: Enter Email
    logger.info("Entering email")
    registration.enter_email(email)
    entered_email = driver.find_element(*registration.email_input).get_attribute("value")
    logger.info(f"Entered Email Field Value: {entered_email}")
    assert entered_email == email, f"Email was not entered correctly. Expected '{email}', got '{entered_email}'"
    # Step 4: Enter Password
    logger.info("Entering password")
    registration.enter_password(password)
    assert driver.find_element(*registration.register).is_enabled(), \
        "Register button is not enabled after entering password"
    # Step 5: Click Register
    logger.info("Clicking Register button")
    registration.click_register()

    driver.implicitly_wait(3)
    # Step 6: Validate Successful Registration
    logger.info("Validating successful registration (Logout link visible)")
    assert registration.is_registration_successful(), \
        "User registration failed"
    logger.info("========== USER REGISTRATION TEST PASSED ==========")


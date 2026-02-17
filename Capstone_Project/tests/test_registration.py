import pytest
import random
import string

from Capstone_Project.pages.Registration import RegistrationPage


def generate_random_email():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"test{random_string}@gmail.com"


def test_user_registration(setup):

    driver = setup
    registration = RegistrationPage(driver)

    # Step 1: Click Sign In
    registration.click_sign_up()

    # Step 4:name

    # Step 3: Enter Email OR Username
    email = generate_random_email()
    password="Neeru@34523456"
    registration.enter_email(email)
    registration.enter_password(password)

    registration.click_register()
    driver.implicitly_wait(3)
    return {"email": email, "password": password}


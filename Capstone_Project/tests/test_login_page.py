# tests/test_login.py
import csv
import os
import pytest
from Capstone_Project.pages.Login import LoginPage

def read_login_data(csv_file_name):
    base_path = os.path.join(os.path.dirname(__file__), "../data")
    csv_path = os.path.join(base_path, csv_file_name)

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


login_test_data = read_login_data("login_test_data.csv")
@pytest.mark.parametrize("data", login_test_data)
def test_login(setup,data):
    driver = setup
    login_page = LoginPage(driver)

    # Open My Account page
    login_page.click_login()

    login_page.enter_email(data["email"])
    login_page.enter_password(data["password"])
    login_page.click_checkbox()  # optional
    login_page.click_loginbtn()

    # Check login success
    login_page.assert_login_success(data["username"])

    # Optionally, sign out after assertion
    login_page.sign_out()
@pytest.mark.parametrize("data", login_test_data)
def test_logout(setup,data):
    driver = setup
    login_page = LoginPage(driver)

    # Open My Account page
    login_page.click_login()

    login_page.enter_email(data["email"])
    login_page.enter_password(data["password"])
    login_page.click_checkbox()  # optional
    login_page.click_loginbtn()

    # Check login success
    login_page.assert_login_success(data["username"])

    # Optionally, sign out after assertion
    login_page.sign_out()

# tests/test_login.py
import csv
import os
import pytest

from Capstone_Project.pages.FindOrders_Byuser import FindOrdersPage
from Capstone_Project.pages.Login import LoginPage

def read_login_data(csv_file_name):
    base_path = os.path.join(os.path.dirname(__file__), "../data")
    csv_path = os.path.join(base_path, csv_file_name)

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


login_test_data = read_login_data("login_test_data.csv")
@pytest.mark.parametrize("data", login_test_data)
def test_findOrdersByUser(setup,data):
    driver = setup
    find_orders_page = FindOrdersPage(driver)

    # Open My Account page
    find_orders_page.click_login()

    find_orders_page.enter_email(data["email"])
    find_orders_page.enter_password(data["password"])
    find_orders_page.click_checkbox()  # optional
    find_orders_page.click_loginbtn()

    find_orders_page.find_orders()
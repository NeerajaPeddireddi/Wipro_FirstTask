import csv
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Capstone_Project.pages.Order_product import OrderProduct
import os

# Function to read CSV data
def read_order_data(csv_file_name):
    base_path = os.path.join(os.path.dirname(__file__), "../data")
    csv_path = os.path.join(base_path, csv_file_name)
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

# Load data
order_test_data = read_order_data("Placeorder_data.csv")

# Parametrize pytest with CSV rows
@pytest.mark.parametrize("data", order_test_data)
def test_place_order_cod(setup, data):
    driver = setup
    order = OrderProduct(driver)

    # Step 1: Go to Shop
    order.go_to_shop()

    # Step 2: Add product to basket
    order.add_product_to_basket()

    # Step 3: View basket
    order.click_view_basket()

    # Step 4: Proceed to checkout
    order.click_proceed_to_checkout()

    # Step 5: Fill billing details
    order.enter_first_name(data["first_name"])
    order.enter_last_name(data["last_name"])
    order.enter_company_name(data["company"])
    order.enter_email(data["email"])
    order.enter_phone(data["phone"])

    # Step 6: Select country
    order.select_country_using_search(data["country"])

    # Step 7: Address details
    order.enter_address(data["address"])
    order.enter_city(data["city"])
    order.select_state(data["state"])
    order.enter_zipcode(data["zipcode"])

    # Step 8: Order notes
    order.enter_order_notes(data["order_notes"])

    # Step 9: Select payment method
    order.select_payment_method(data["payment_method"])

    # Step 10: Place order
    order.click_place_order()

    # Step 11: Verify thank you message
    wait = WebDriverWait(driver, 10)
    thank_you_msg = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"))
    )
    assert "Thank you. Your order has been received." in thank_you_msg.text

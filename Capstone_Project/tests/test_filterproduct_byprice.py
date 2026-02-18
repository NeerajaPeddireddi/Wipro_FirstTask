import csv
import os

import pytest

from Capstone_Project.pages.FilterProduct_ByPrice import FilterProduct

def read_sort_data(csv_file_name):
    base_path = os.path.join(os.path.dirname(__file__), "../data")
    csv_path = os.path.join(base_path, csv_file_name)
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

filter_test_data = read_sort_data("price_filters_data.csv")


# --------- Test ----------
@pytest.mark.parametrize("data", filter_test_data)
def test_filter_product(setup, data):
    driver = setup
    filter_page = FilterProduct(driver)
    # Go to Shop
    filter_page.go_to_shop()

    min_price = data["min_price"]
    max_price = data["max_price"]

    filter_page.filter_by_price(min_price, max_price)

    # Optional: verify filtered products
    # products = driver.find_elements(By.CSS_SELECTOR, "ul.products li")
    # assert all(min_price <= int(p.text) <= max_price for p in products)

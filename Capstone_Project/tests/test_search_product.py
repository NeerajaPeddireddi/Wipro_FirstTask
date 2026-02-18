import csv
import os

import pytest
from selenium.webdriver.common.by import By

from Capstone_Project.pages.Search_Product import SearchProduct

# ---------- Read CSV ----------
def read_search_data(csv_file_name):
    base_path = os.path.join(os.path.dirname(__file__), "../data")
    csv_path = os.path.join(base_path, csv_file_name)

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


search_test_data = read_search_data("search_products.csv")
@pytest.mark.parametrize("data", search_test_data)
def test_search_product(setup,data):

    driver = setup
    search_page=SearchProduct(driver)


    # Go to Shop
    search_page.go_to_shop()
    #taing from csv
    product_name = data["product_name"]
    # Search product
    search_page.search_product(product_name)

    # Validate search results appear
    assert search_page.validate_search_results()

    # Click search result
    search_page.click_search_result()

    # Validate product page opened
    product_title = driver.find_element(By.CSS_SELECTOR, "h1.product_title")
    assert product_name in product_title.text

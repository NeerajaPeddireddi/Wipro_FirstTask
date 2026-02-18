import os
import csv
import pytest

from Capstone_Project.pages.Sort_Products import SortProducts


def read_sort_data(csv_file_name):
    base_path = os.path.join(os.path.dirname(__file__), "../data")
    csv_path = os.path.join(base_path, csv_file_name)
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

sort_test_data = read_sort_data("product_sort_data.csv")

@pytest.mark.parametrize("data", sort_test_data)
def test_sort_products(setup, data):
    """
    Test sorting products based on user interest from CSV
    """
    driver = setup
    product_page = SortProducts(driver)

    # Go to shop page (assuming base URL already handled in setup)
    driver.get("https://practice.automationtesting.in/shop/")

    # Select sorting option from CSV
    product_page.select_sort_option(data["sort_by"])

    # Wait a moment for page to reload (optional, adjust if needed)
    driver.implicitly_wait(20)

    # Assert the URL contains the correct 'orderby' parameter
    current_url = driver.current_url
    if data['sort_by'] == "menu_order":
        # Default sorting doesn't change the URL
        assert "shop" in current_url
    else:
        # Other sorts append ?orderby=...
        expected_param = f"orderby={data['sort_by']}"
        assert expected_param in current_url, f"Expected '{expected_param}' in URL but got '{current_url}'"

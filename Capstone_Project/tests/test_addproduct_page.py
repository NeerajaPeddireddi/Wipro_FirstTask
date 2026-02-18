import pytest
from selenium.webdriver.common.by import By

from Capstone_Project.pages.Add_Product import AddProduct


def test_add_product_to_cart(setup):

    driver = setup
    product = AddProduct(driver)

    # Step 1: Go to Shop
    product.go_to_shop()

    # Step 2: Add product to basket
    product.add_product_to_basket()

    # Step 3: Click View Basket
    product.click_view_basket()

    # -------- Assertions --------
    assert "basket" in product.get_current_url().lower()

    assert driver.title == "Basket – Automation Practice Site"

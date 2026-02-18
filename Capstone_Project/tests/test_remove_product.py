from Capstone_Project.pages.Remove_Product import RemoveProduct


def test_remove_product(setup):
    driver = setup
    cart_page = RemoveProduct(driver)

    # Go to shop and add product
    cart_page.go_to_shop()
    cart_page.add_product_to_basket()
    cart_page.click_view_basket()

    # Remove first product
    cart_page.remove_product_from_cart()

    # Optional: check cart is empty or product removed
    assert "basket" in cart_page.get_current_url()

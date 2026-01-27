def test_order_creation(user, app_connection):
    assert user["name"] == "Arun"
    assert app_connection == "App connected"

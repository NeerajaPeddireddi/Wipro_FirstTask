def setup_module(module):
    print("\n[setup_module] test_user")
def teardown_module(module):
    print("\n[teardown_module] test_user")
def setup_function(function):
    print("\n[setup_function] test_user")
def teardown_function(function):
    print("\n[teardown_function] test_user")
def test_user_name(user):
    assert user["name"] == "Arun"
def test_user_age(user):
    assert user["age"] == 24
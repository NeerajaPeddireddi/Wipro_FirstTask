import pytest

@pytest.fixture(scope="session")
def base_url():
    print("\n--- Setup: Starting API Tests ---")
    url = "http://127.0.0.1:5000"
    yield url
    print("\n--- Teardown: API Tests Completed ---")

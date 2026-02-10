import pytest

@pytest.fixture
def base_url():
    print("\n----- setup started-------")
    url="http://127.0.0.1:5000"
    yield url
    print("\n----- teardown started-------")


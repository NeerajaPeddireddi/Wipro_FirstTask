#Automatically available to all test files
# No import needed
import pytest
#function-scoped fixture
@pytest.fixture(scope="function")
def user():
    print("\nCreating user")
    return {"name":"Arun","age":24}
#module-scoped fixture
@pytest.fixture(scope="module")
def app_connection():
    print("\nCreating app connection")
    yield "App connected"
    print("App disconnected")

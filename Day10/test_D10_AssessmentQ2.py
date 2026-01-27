# Question 2 – Setup/Teardown, Fixtures & conftest.py
# Topics Covered:
# xUnit style setup and teardown, Test fixtures, conftest.py
# Enhance the test suite created in Question 1.
# Requirements:
# 1. Implement xUnit-style methods (setup_module, teardown_module, setup_function, teardown_function)
# 2. Create reusable fixtures for test data and resources
# 3.Move common fixtures to a conftest.py file
# 4. Demonstrate fixture scope (function, module)
# 5. Use fixtures in multiple test file

import pytest
@pytest.fixture
def data():
    return [1,2,3]

def test_one(data):
    # data=[1,2,3]
    assert 2 in data
    print(data)
def test_two(data):
    # data=[1,2,3]
    assert len(data)==3
    print(data)
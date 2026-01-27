# Question 1 – Pytest Basics, Test Discovery & Assertions
# Topics Covered:
# Pytest overview, Test discovery, Writing and running unit tests, Assert statements and exceptions
# Requirements:
# 1. Write unit tests using Pytest conventions (test_*.py, test_ functions)
# 2. Demonstrate automatic test discovery
# 3. Use assert statements to validate results
# 4. Write a test to validate that an exception is raised for division by zero
# 5.Execute tests using the pytest command

import pytest
def test_add():
    assert add(2,3) == 5
def test_sub():
    assert sub(2,1) == 1
def test_mul():
    assert mul(2,3) == 6
def test_div():
    assert div(5,3) == 1
def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(5,0)

#Implementation

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        raise ZeroDivisionError
    return a//b
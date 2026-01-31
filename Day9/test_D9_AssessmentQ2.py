# Question 2 – Unit Testing & Test Driven Development (TDD)
# Topics Covered:
# Unit testing, Test Driven Development
# Implement Test Driven Development (TDD) for a simple calculator module.
# Requirements:
# 1. Write unit test cases first for operations:
# Addition
# Subtration
# Multiplication
# Division
# 2. Use a Python unit testing framework (unittest or pytest)
# 3. Implement the calculator functions to make the tests pass
# 4. Demonstrate handling of edge cases (e.g., division by zero)
# 5. Explain the TDD cycle: Red → Green → Refactor

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

#---------Output--------
# Testing started at 14:07 ...
# Launching pytest with arguments C:\Users\Neeraja\Desktop\Wipro_Practice\Day9\test_D10_AssessmentQ2.py --no-header --no-summary -q in C:\Users\Neeraja\Desktop\Wipro_Practice
#
# ============================= test session starts =============================
# collecting ... collected 5 items
#
# Day9/test_D10_AssessmentQ2.py::test_add PASSED                           [ 20%]
# Day9/test_D10_AssessmentQ2.py::test_sub PASSED                           [ 40%]
# Day9/test_D10_AssessmentQ2.py::test_mul PASSED                           [ 60%]
# Day9/test_D10_AssessmentQ2.py::test_div PASSED                           [ 80%]
# Day9/test_D10_AssessmentQ2.py::test_div_by_zero PASSED                   [100%]
#
# ============================== 5 passed in 0.03s ==============================

# 5. Explain the TDD cycle: Red → Green → Refactor
# Red-->Test Written First
# def test_add():
#     assert add(2, 3) == 5
# here add not existing so test fails(red)
# NameError: name 'add' is not defined
#
# Green -->Write minimum code to pass
# def add(a,b):
#     return a+b
# output green we get some thing like test pass
# Blue -->Improve code without breaking tests
# def add(a: int, b: int) -> int:
#     """Returns the sum of two numbers"""
#     return a + b
# Phase	    Action	            Result
# RED	    Write test first	Test fails
# GREEN	    Write minimal code	Test passes
# REFACTOR	Improve code	     Tests still pass

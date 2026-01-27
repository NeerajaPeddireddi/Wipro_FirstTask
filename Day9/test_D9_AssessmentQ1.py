# Question 1 – Automation Framework Basics & Environment Setup
# Topics Covered:
# Introduction to automation frameworks in Python, Setting up the development environment
# Design a basic Python automation testing framework.
# Requirements:
# 1. Set up a virtual environment
from prompt_toolkit.application import create_app_session
#
# Created Virtual Environment  with name venv456  by using below commands
# python -m venv venv456
# activate using this command --> venv456\Scripts\activate
#
# # 2. Install required tools and libraries (e.g., pytest or unittest)
# Installed pytest using this command -->pip install pytest
# # 3. Create a project structure for an automation framework (tests, utilities, configuration)
# automation_framework/
# │
# ├── tests/
# │   ├── test_sample.py
# │
# ├── utilities/
# │   ├── math_utils.py
# │
# ├── config/
# │   ├── config.py
# │
# ├── reports/
# │   └── (HTML/XML reports)
# │
# ├── pytest.ini
# │
# └── venv/
#
# tests-->All test cases
# utilities -->Reusable functions,helpers
# congig -->Environment setting (URLs,credentials)
# reports -->test  execution results
# pytest.ini -->pytest configuration

# 4.Explain the role of:
# Test runner
# Test runner Executes test cases
# Collects tests
# Provides execution status
# pytest
# here pytest acts as the test runner
# Test reports
# Shows pass/fail status
# Execution time
# Error details
# Used for analysis & CI/CD
# pytest --html=reports/report.html
# (Using pytest-html plugin)
# Configuration files
# Store environment-specific data
# Avoid hardcoding values
# Easy maintenance
#  Example (config/config.py):
# BASE_URL = "https://example.com"
# BROWSER = "chrome"
# pytest.ini:
# [pytest]
# markers =
#     smoke: smoke test cases
#     regression: regression test cases
# 5. Write a sample test case to validate a simple function
import pytest
def test_add():
    assert 2+3 ==5

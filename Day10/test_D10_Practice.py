def test_add():
    assert 2+4==6
def test_sub():
    assert 4-2==2

#If you want run above write pytest in cmd
#using fixtures this is passing data
#if you want run single file pytest filename,.py
# pytest -s Day10\test_work.py will give print data also
#we need to set method as test_ method name then only that methods executed inside test file
#Fixures
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

#Using Yield
import pytest
@pytest.fixture
def setup_teardown():
    print("setup")
    yield
    print("teardown")

def test_example(setup_teardown):
    print("test running")

#we use two like this
def test_example1(setup_teardown):
    print("test2 running")

# parameters passing syntax
# @pytest.mark.parametrize("param_names", [param_values])

import pytest
@pytest.mark.parametrize("a,b,res",[(2,3,5),(3,4,7)])
def test_add(a,b,res):
    assert a+b ==res

#Smoke testing
@pytest.mark.smoke
def test_smoke():
    assert True
#only smoke test is executed when we use pytest -m smoke


#To skip the test with a reason
@pytest.mark.skip(reason="Not Ready")
def test_skip():
    pass

# -----------Output-------------
# Day10/test_work.py::test_add[2-3-5]
# Day10/test_work.py::test_add[3-4-7]
# Day10/test_work.py::test_smoke
# Day10/test_work.py::test_skip
#
# =================== 3 passed, 1 skipped, 1 warning in 0.03s ===================
# PASSED                               [ 25%]PASSED                               [ 50%]PASSED                                    [ 75%]SKIPPED (Not Ready)                        [100%]
# Skipped: Not Ready

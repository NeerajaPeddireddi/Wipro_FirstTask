import pytest
@pytest.mark.parametrize("a,b,res",[(2,3,5),(3,4,7)])
def test_add(a,b,res):
    assert a+b ==res

@pytest.mark.smoke
def test_smoke():
    assert True
#only smoke test is executed when we use pytest -m smoke
#To skip the test with a reason
@pytest.mark.skip(reason="Not Ready")
def test_skip():
    pass

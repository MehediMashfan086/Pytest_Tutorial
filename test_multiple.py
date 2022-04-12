import pytest

@pytest.mark.one
def test_method1():
    x = 10
    y = 15
    assert x == y

@pytest.mark.two    
def test_method2():
    a = 10
    b = 15
    assert a + 5 == b
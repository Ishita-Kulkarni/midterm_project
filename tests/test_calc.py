import pytest
from app.calc import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(2.5, 3.5) == 6.0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(2.5, 1.0) == 1.5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(2.0, 3.5) == 7.0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(7.5, 2.5) == 3.0
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

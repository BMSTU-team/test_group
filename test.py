# Тесты для калькулятора

import pytest
from calc import add, subtract, multiply, divide

def test_add():
    assert add(10, 5) == 15
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(10, 5) == 50
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1

def test_divide():
    assert divide(10, 5) == 2
    assert divide(-1, 1) == -1
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        divide(10, 0)

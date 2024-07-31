from math_operations import add, subtract, multiply
import pytest


@pytest.mark.parametrize(
    "a,b,expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0), (1.5, 2.5, 4)]
)
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(3, 5) == 15

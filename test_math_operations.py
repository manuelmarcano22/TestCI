from math_operations import add, subtract, multiply, mean
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


@pytest.mark.parametrize("numbers, expected", [
  ([10, 20, 30], 20),
  ([1.5, 2.5, 3.5], 2.5)
])


def test_mean(numbers, expected):
  if numbers:
    assert mean(numbers) == expected

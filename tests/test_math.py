import pytest


def test_addition():
    assert 1+1 == 2


def test_subtractions():
    diff = 1 - 1
    assert diff == 0


# Testing with multiple inputs of data
@pytest.mark.parametrize("num1, num2, expected", [(1, 2, 2), (3, 5, 15),
                                                  (4, 5, 20), (3, 4, 12)])
def test_multiplication(num1, num2, expected):
    assert num1 * num2 == expected



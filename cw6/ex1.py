import pytest
from common import fmin, sub, UndefinedRecursiveFunctionCallError


test_data = ((0, 2), (3, 4), (5, 5), (4, 2), (7, 4), (3, 1))


def div(n : int, m: int) -> int:
    """
    returns n // m
    """
    if m == 0:
        raise UndefinedRecursiveFunctionCallError("zero division")
    return sub(fmin(lambda k: n < k * m), 1)


def test_div_zero():
    with pytest.raises(UndefinedRecursiveFunctionCallError):
        _ = div(13, 0)


@pytest.mark.parametrize("n, m", test_data)
def test_div(n: int, m: int):
    assert div(n, m) == n // m


def mod(n: int, m: int) -> int:
    """
    returns n % m
    """
    return sub(n, div(n, m) * m)


def test_mod_zero():
    with pytest.raises(UndefinedRecursiveFunctionCallError):
        _ = mod(13, 0)


@pytest.mark.parametrize("n, m", test_data)
def test_mod(n: int, m: int):
    assert mod(n, m) == n % m

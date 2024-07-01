import pytest
import math
from typing import Callable

from common import ch, fmin, sub, UndefinedRecursiveFunctionCallError
from ex1 import mod


def fmax(m: int, f: Callable[[int], bool]) -> int:
    """
    returns max k such that 0 <= k < m and f(m - k) = True
    """
    return sub(m, fmin(lambda k: f(m - k) and k > 0 and k <= m))


def max_div(n: int) -> int:
    """
    returns max k such that k < n and k | n
    """
    if n == 0:
        raise UndefinedRecursiveFunctionCallError("zero division")
    return fmax(n, lambda k: mod(n, k) == 0)


def test_max_div_throw():
    with pytest.raises(UndefinedRecursiveFunctionCallError):
        _ = max_div(0)

    with pytest.raises(UndefinedRecursiveFunctionCallError):
        _ = max_div(1)


@pytest.mark.parametrize("n", (2, 4, 5, 9, 15))
def test_max_div(n: int):
    def _max_div(x: int) -> int:
        for i in reversed(range(2, x)):
            if x % i == 0:
                return i
        return 1

    assert max_div(n) == _max_div(n)


def max2(x: int, y: int) -> int:
    """
    returns max from x and y
    """
    return x * ch(x < y) + y * (1 - ch(x < y))


@pytest.mark.parametrize("n, m", ((3, 3), (2, 5), (5, 2)))
def test_max2(n: int, m: int):
    assert max2(n, m) == max(n, m)


def gcd(n: int, m: int) -> int:
    """
    returns max k such that k < n and k < m and k | n and k | m
    """
    return fmax(max2(n, m) + 1, lambda k: mod(n, k) == 0 and mod(m, k) == 0)


def test_gcd_throw():
    with pytest.raises(UndefinedRecursiveFunctionCallError):
        _ = gcd(0, 0)


@pytest.mark.parametrize("n, m", ((0, 5), (5, 0), (1, 4), (7, 5), (9, 6), (12, 18)))
def test_gcd(n: int, m: int):
    assert gcd(n, m) == math.gcd(n, m)

import pytest
import math

from common import fmin, sub


def sqrt(n: int) -> int:
    """
    returns ceil(sqrt(n))
    """
    return fmin(lambda k: sub(n, k * k) == 0)

@pytest.mark.parametrize("n", (0, 1, 2, 4, 8, 9))
def test_sqrt(n: int):
    assert sqrt(n) == math.ceil(math.sqrt(n))


def log(n: int) -> int:
    """
    returns floor(log2(n))
    """
    return sub(fmin(lambda k: math.pow(2, k) > n + 1), 1)


@pytest.mark.parametrize("n", (0, 1, 2, 4, 8))
def test_log(n: int):
    assert log(n) == math.floor(math.log2(n + 1))

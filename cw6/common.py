from typing import Callable


class UndefinedRecursiveFunctionCallError(Exception):
    def __init__(self, fcall: str):
        super().__init__(f"Undefined function call: {fcall}")


def ch(b: bool) -> bool:
    return not b


def fmin(f: Callable[[int], bool]) -> int:
    k = 0
    while not f(k):
        k += 1
    return k

def sub(n: int, m: int) -> int:
    return max(n - m, 0)

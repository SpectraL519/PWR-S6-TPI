def ceil_log2(n: int) -> int:
    """
    calculates ceiling(log2(n + 1))
    """
    result = 0
    while n > 0:
        n >>= 1
        result += 1
    return result


print(ceil_log2(1))  # 1
print(ceil_log2(2))  # 2
print(ceil_log2(4))  # 3
print(ceil_log2(8))  # 4
print(ceil_log2(16)) # 5

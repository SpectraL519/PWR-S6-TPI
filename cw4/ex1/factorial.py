def factorial(n: int) -> int:
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


print(factorial(0)) # 1
print(factorial(1)) # 1
print(factorial(2)) # 2
print(factorial(3)) # 6
print(factorial(4)) # 24
print(factorial(5)) # 120

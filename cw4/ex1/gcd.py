def gcd(a: int, b: int) -> int:
    while b > 0:
        tmp = a % b
        a = b
        b = tmp
    return a


print(gcd(0, 5))   # 5
print(gcd(5, 0))   # 5
print(gcd(7, 5))   # 1
print(gcd(9, 6))   # 3
print(gcd(12, 18)) # 6

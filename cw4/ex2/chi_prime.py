def chi_prime(n: int) -> bool:
    if n < 2:
        return False

    i = 2
    while i * i < n:
        if n % i == 0:
            return False
        i += 1

    return True


print(chi_prime(1)) # F
print(chi_prime(2)) # T
print(chi_prime(3)) # T
print(chi_prime(12)) # F
print(chi_prime(17)) # T

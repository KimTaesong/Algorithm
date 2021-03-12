def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


def gcd1(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


print(gcd(24, 16))
print(gcd1(24, 16))

def solution(n: int, m: int) -> list:
    def gcd(a: int, b: int) -> int:
        if b > a:
            a, b = b, a
        return b if a % b == 0 else gcd(b, a % b)
    return [gcd(n, m), n * m // gcd(n, m)]

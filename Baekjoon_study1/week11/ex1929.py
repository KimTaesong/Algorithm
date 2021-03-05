# BOJ 소수구하기 1929
def isPrime(N):
    if N == 1:
        return False
    i = 2
    while i * i <= N:
        if N % i == 0:
            return False
        i += 1
    return True


M, N = map(int, input().split())
for i in range(M, N+1):
    if isPrime(i):
        print(i)

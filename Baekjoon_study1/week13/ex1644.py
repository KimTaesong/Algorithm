# BOJ 소수의 연속합 1644
import sys


def era(N):
    ck, p = [False for _ in range(N+1)], []
    for i in range(2, N+1):
        if ck[i] == True:
            continue
        p.append(i)
        for j in range(i*i, N+1, i):
            ck[j] = True
    return ck, p


input = sys.stdin.readline
n = int(input())  # 자연수 N
prime_numbers = era(n)[1]
# print(prime_numbers)
cnt = 0
for i in range(len(prime_numbers)):
    sum_value = 0
    for j in range(i, len(prime_numbers)):
        sum_value += prime_numbers[j]
        if sum_value == n:
            cnt += 1
            break
print(cnt)

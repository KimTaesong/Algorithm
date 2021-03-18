# BOJ 동전 1 2293
import sys
input = sys.stdin.readline
n, k = map(int, input().split())  # n가지의 동전, k원
coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
dp[0] = 1
'''
    1   2   3   4   5   6   7   8   9   10
1   1   1   1   1   1   1   1   1   1    1   
2   0   1   1   2   2   3   3   4   4    5
5   0   0   0   0   1   1   2   2   3    4
t   1   2   2   3   4   5   6   7   8   10
'''
for i in coins:
    for j in range(i, k+1):
        dp[j] += dp[j-i]
print(dp[k])

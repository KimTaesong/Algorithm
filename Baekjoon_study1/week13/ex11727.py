# BOJ 2 x n 타일링 2 11727
n = int(input())
dp = [0] * (n+1)
dp[1] = 1
if n >= 2:
    dp[2] = 3
if n >= 3:
    for i in range(3, n+1):
        dp[i] = dp[i-2] * 2 + dp[i-1]
print(dp[n] % 10007)

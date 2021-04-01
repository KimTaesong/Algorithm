# BOJ 이친수 2193
n = int(input())
dp = [0] * 91
dp[1] = 1
dp[2] = 1
for i in range(3, 91):
    dp[i] = dp[i-2] + dp[i-1]
print(dp[n])

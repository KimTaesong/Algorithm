# BOJ dp 포도주 시식 2156
n = int(input())  # 포도주 잔의 개수 n
grape_wine = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)

if n >= 1:
    dp[1] = grape_wine[1]
if n >= 2:
    dp[2] = dp[1] + grape_wine[2]
if n >= 3:
    dp[3] = max(dp[2], grape_wine[2] + grape_wine[3], dp[1] + grape_wine[3])
if n >= 4:
    for i in range(4, n+1):
        dp[i] = max(dp[i-1], dp[i-2] + grape_wine[i],
                    dp[i-3] + grape_wine[i-1] + grape_wine[i])
print(dp)

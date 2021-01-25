n = int(input())

stair = [0]
dp = [0] * (n+1)
for i in range(n):
    stair.append(int(input()))

if n >= 1:
    dp[1] = stair[1]
if n >= 2:
    dp[2] = stair[1] + stair[2]
if n >= 3:
    dp[3] = max(dp[1] + stair[3], (stair[2] + stair[3]))
    for i in range(4, n+1):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

print(dp[n])

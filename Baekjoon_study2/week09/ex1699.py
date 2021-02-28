import math

N = int(input())
dp = [10000] * 100001
dp[1] = 1
for i in range(2, N+1):
    square_root = math.sqrt(i)
    if i % square_root == 0:
        dp[i] = 1
    for j in range(1, int(square_root)+1):
        tmp = 1 + dp[i-int(j)*int(j)]
        dp[i] = min(dp[i], tmp)

print(dp[N])

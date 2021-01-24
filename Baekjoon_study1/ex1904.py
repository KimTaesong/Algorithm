import sys
input = sys.stdin.readline()
N = int(input)
dp = [0] * 1000000
dp[0] = 1
dp[1] = 2
for i in range(2, N):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746
print(dp[N-1])

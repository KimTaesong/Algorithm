# BOJ DP 쉬운 계단 수10844
N = int(input())  # 길이가 N인 계단
stair_cnt = 0
dp = [[0] * 10 for _ in range(N+1)]

for i in range(1, 10):
    dp[0][i] = 1
if N >= 2:
    for i in range(1, N+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
stair_cnt = sum(dp[N-1])
print(stair_cnt % 1000000000)

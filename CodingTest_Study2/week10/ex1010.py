# BOJ 1010 다리놓기
import sys
t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, input().split())  # n 서쪽 사이트의 개수, m 동쪽 사이트의 개수
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, m+1):
        dp[1][i] = i
    for i in range(2, n+1):
        for j in range(i, m+1):
            if j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    print(dp[n][m])

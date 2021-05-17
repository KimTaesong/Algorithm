n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dp = [[0] * (m+1) for _ in range(n+1)]
max_value = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dp[i+1][j+1] = min(dp[i][j], min(dp[i+1][j], dp[i][j+1])) + 1
            max_value = max(max_value, dp[i+1][j+1])

print(max_value ** 2)

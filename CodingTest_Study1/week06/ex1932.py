# BOJ 동적계획법1 정수 삼각형 1932
n = int(input())

dp = [[0] * (n+1) for _ in range(n+1)]
tri_cost = [[0]]

for i in range(n):
    tri_cost.append([0] + list(map(int, input().split())))

dp[1][1] = tri_cost[1][1]
if n >= 2:
    dp[2][1] = dp[1][1] + tri_cost[2][1]
    dp[2][2] = dp[1][1] + tri_cost[2][2]
if n >= 3:
    for i in range(3, n+1):
        for j in range(1, i+1):
            if j == 1:
                dp[i][j] = tri_cost[i][j] + dp[i-1][j]
            elif j == i:
                dp[i][j] = tri_cost[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = tri_cost[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n]))

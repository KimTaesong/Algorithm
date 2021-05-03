# BOJ 파이프 옮기기 1
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

# 0: 가로, 1: 세로, 2: 대각
vector = [[(0, 1, 0, 1), (0, 1, 1, 1)], # 가로 이동, 대각 이동
          [(1, 0, 1, 0), (1, 0, 1, 1)], # 세로 이동, 대각 이동
          [(1, 1, 1, 0), (1, 1, 0, 1), (1, 1, 1, 1)]] # 가로 이동, 세로 이동, 대각 이동

def check_pipe_state(a1, b1, a2, b2):
    if a1 == a2 and b2 - b1 == 1:
        return 0 # 가로 방향
    elif a2 - a1 == 1 and b2 == b1:
        return 1 # 세로 방향
    elif a2- a1 == 1 and b2 - b1 == 1:
        return 2 # 대각 방향


def dfs(x1, y1, x2, y2):
    global cnt

    if x2 == n-1 and y2 == n - 1:
        cnt += 1
        return
    pipe_state = check_pipe_state(x1, y1, x2, y2)

    for i in range(len(vector[pipe_state])):
        nx1, ny1 = x1 + vector[pipe_state][i][0], y1 + vector[pipe_state][i][1]
        nx2, ny2 = x2 + vector[pipe_state][i][2], y2 + vector[pipe_state][i][3]

        if nx1 < 0 or nx1 > n-1 or ny1 < 0 or ny1 > n-1 or nx2 < 0 or nx2 > n-1 or ny2 < 0 or ny2 > n-1:
            continue

        # 가로, 세로
        if nx2 - nx1 != ny2 - ny1 and graph[nx2][ny2] != 1:
            dfs(nx1, ny1, nx2, ny2)

        # 대각성 이동
        if nx2 - nx1 == ny2 - ny1 and graph[nx1][ny1] != 1 and graph[nx2][ny2] != 1 and graph[nx1][ny2] != 1 and graph[nx2][ny1] != 1:
            dfs(nx1, ny1, nx2, ny2)

if n <= 0:
    dfs(0, 0, 0, 1)
    print(cnt)

else:
    # 가로, 세로, 대각선 방향의 파이프 이동을 저장하는 3차원 배열 [0][][]: 가로, [1][][]: 대각, [2][][]: 세로
    dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]
    print(dp)
    dp[0][0][1] = 1

    # 가로방향으로 파이프를 계속 이동
    for i in range(2, n):
        if graph[0][i] == 0:
            dp[0][0][i] = dp[0][0][i-1]


    for x in range(1, n):
        for y in range(1, n):
            if graph[x][y] == 0 and graph[x][y-1] == 0 and graph[x-1][y] == 0:
                dp[1][x][y] = dp[0][x-1][y-1] + dp[1][x-1][y-1] + dp[2][x-1][y-1] # 가로 -> 대각선 이동, 대각선 -> 대각선 이동, 세로 -> 대각선 이동

            if graph[x][y] == 0:
                dp[0][x][y] = dp[0][x][y-1] + dp[1][x][y-1] # 가로 -> 가로,  대각선 -> 가로
                dp[2][x][y] = dp[2][x-1][y] + dp[1][x-1][y] # 세로 -> 세로, 대각선 -> 세로로

    print(sum(dp[i][n-1][-1] for i in range(3)))


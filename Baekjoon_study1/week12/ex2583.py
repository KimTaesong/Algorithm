# BOJ 영역 구하기 2583
import sys
sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split())  # M 열, N 행 K 직사각형의 개수\
graph = [[1] * (M+1) for _ in range(N+1)]
visited = [[0] * (M+1) for _ in range(N+1)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
width = 1
sub_areas = []
for i in range(K):
    # 직사각형의 왼쪽 아래 좌표 (x1, y1), 오른쪽 위 좌표 (x2, y2)
    x1, y1, x2, y2 = map(int, input().split())
    for a in range(x1+1, x2+1):
        for b in range(y1+1, y2+1):
            graph[a][b] = 0


def dfs(x, y):
    global width
    visited[x][y] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 1 <= nx <= N and 1 <= ny <= M:
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                width += 1
                dfs(nx, ny)


for i in range(1, N+1):
    for j in range(1, M+1):
        if graph[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)
            sub_areas.append(width)
            cnt += 1
            width = 1
print(cnt)
sub_areas.sort()
for k in sub_areas:
    print(k, end=' ')

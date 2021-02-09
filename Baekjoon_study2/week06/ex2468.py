# BOJ 안전 영역 2468
import sys
sys.setrecursionlimit(10**6)
N = int(input())  # 행과 열의 개수 N
area_graph = [[0]]
visited = [[0] * (N+1) for _ in range(N+1)]
safe_areas = [0]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    area_graph.append([0] + list(map(int, input().split())))  # 물에 잠기는 영역 지도
max_value = max(map(max, area_graph))
# print(area_graph)


def dfs(x, y, rain):
    visited[x][y] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 1 <= nx <= N and 1 <= ny <= N:
            if area_graph[nx][ny] > rain and visited[nx][ny] == 0:
                dfs(nx, ny, rain)


for k in range(0, max_value):
    cnt = 0
    visited = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            if area_graph[i][j] > k and visited[i][j] == 0:
                dfs(i, j, k)
                cnt += 1
    safe_areas.append(cnt)
print(max(safe_areas))

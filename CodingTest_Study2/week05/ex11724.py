import sys
sys.setrecursionlimit(10000)


def dfs(v):
    visited[v] = v
    for i in graph[v]:
        if (i != 0) and (i not in visited):
            dfs(i)


N, M = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = y
    graph[y][x] = x

for k in range(1, N+1):
    if k not in visited:
        dfs(k)
        cnt += 1

print(cnt)

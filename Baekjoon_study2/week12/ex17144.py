import sys
input = sys.stdin.readline
r, c, t = map(int, input().split())  # R행, C열, T초
cnt = 0  # 미세먼지의 양
graph = [list(map(int, input().split())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
# 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move_init(visited):
    visited = [[0] * C for _ in range(R)]


for i in range(t):
    move_air(move_dust(graph))
    move_init(visited)
print(cnt)


def move_dust(graph):
    for x in range(r):
        for y in range(c):
            if graph[i][j] == -1 or graph[i][j] == 0:
                continue

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or nx > r-1 or ny < 0 or ny > c - 1:
                    continue

                if graph[nx][ny] == -1 or graph[ny][ny] == 0:
                    continue

                visited[nx][ny] += graph[x][y] // 5
                visited[x][y] = graph[x][y] - graph[x][y] // 5
    return visited


def move_air(graph):

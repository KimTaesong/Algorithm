from collections import deque
vector = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

def bfs(x1, y1, x2, y2):
    queue = deque([[x1, y1]])
    graph[x1][y1] = 1

    while queue:
        x, y = queue.popleft()
        if (x, y) == (x2, y2):
            return graph[x][y] - 1

        for i in range(8):
            nx = x + vector[i][0]
            ny = y + vector[i][1]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                queue.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1

for i in range(int(input())):
    n = int(input())
    graph = [[0] * n for _ in range(n)]
    cur_x, cur_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    print(bfs(cur_x, cur_y, target_x, target_y))

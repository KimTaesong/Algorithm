from collections import deque


def solution(maps):
    vector = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    graph = maps
    n, m = len(graph), len(graph[0])

    def bfs(a, b):
        q = deque([[a, b]])
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + vector[i][0], y + vector[i][1]
                if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                    continue

                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))

        if graph[n-1][m-1] == 1:
            return -1
        return graph[n-1][m-1]

    return bfs(0, 0)

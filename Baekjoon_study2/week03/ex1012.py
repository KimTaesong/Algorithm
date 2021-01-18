import sys
from collections import deque
limit_number = 10**6
sys.setrecursionlimit(limit_number)

T = int(input())  # 테스트 케이스의 개수
for i in range(T):
    M, N, K = map(int, input().split())  # M 가로의 길이, N 세로의 길이, K 배추의 개수
    graph = [[0] * M for _ in range(N)]  # M x N 배추 밭
    visited = [[0] * M for _ in range(N)]  # M x N 배추 밭
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    for _ in range(K):
        X, Y = map(int, input().split())  # 배추의 위치
        graph[Y][X] = 1  # 배추가 심어진 위치 1로 변경

    def dfs(i, j):
        visited[i][j] = True
        for k in range(4):
            ii = i + dy[k]
            jj = j + dx[k]

            if 0 <= ii <= N-1 and 0 <= jj <= M-1:
                if visited[ii][jj] == 0 and graph[ii][jj] == 1:
                    dfs(ii, jj)
                    visited[ii][jj] = 1

    def bfs(i, j):
        queue = deque([[i, j]])
        visited[i][j] = True
        while queue:
            V = queue.popleft()
            for k in range(4):
                ii = V[0] + dx[k]
                jj = V[1] + dy[k]
                if 0 <= ii <= N-1 and 0 <= jj <= M-1:
                    if visited[ii][jj] == 0 and graph[ii][jj] == 1:
                        queue.append([ii, jj])
                        visited[ii][jj] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                cnt += 1
    print(cnt)

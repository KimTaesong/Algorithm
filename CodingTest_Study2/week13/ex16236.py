# BOJ 16236 아기 상어
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())  # 수족관의 크기 n
graph = [list(map(int, input().split()))
         for i in range(n)]  # 수족관, 0: 빈칸, 1~6: 물고기의 크기, 9: 아기 상어의 위치


# 아기 상어의 위치를 찾는 함수
def check(graph):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                return [i, j]


# 아기 상어의 수족관 탐색 함수
def bfs(a: int, b: int):
    q = deque([[a, b]])
    cnt = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 칸을 벗어나면 종료
            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue

            # 크기보다 큰 물고기가 있는 칸은 지나갈 수 없음.
            if graph[nx][ny] > baby_size:
                continue

            # 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.
            if graph[nx][ny] != 0:
                if graph[nx][ny] != baby_size:
                    graph[nx][ny] = 0
                q.append([nx, ny])
                cnt += 1

            # 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
            if baby_size == cnt:
                baby_size += 1
                cnt = 0


# 아기상어 상하좌우 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

baby_size = 2
location = check(graph)
bfs(location[0], location[1])

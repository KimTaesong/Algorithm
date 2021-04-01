# BOJ 7569 토마토
from collections import deque

M, N, H = map(int, input().split())
tomato = []
for i in range(H):
    tomato.append([list(map(int, input().split())) for _ in range(N)])
# print(tomato)

# 3차원 방향 벡터
dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]

answer = 0
queue = deque([])


def bfs(queue, answer):
    count = answer
    while queue:
        v = queue.popleft()
        nowX = v[0]
        nowY = v[1]
        nowZ = v[2]
        count = v[3]
        for i in range(6):
            newX = nowX + dx[i]
            newY = nowY + dy[i]
            newZ = nowZ + dz[i]
            if 0 <= newX < H and 0 <= newY < N and 0 <= newZ < M:
                if tomato[newX][newY][newZ] == 0:
                    tomato[newX][newY][newZ] = 1
                    queue.append([newX, newY, newZ, count+1])
    return count


def check(answer, tomato):
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 0:
                    return -1
    return answer


for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                queue.append([i, j, k, answer])


answer = bfs(queue, answer)

print(check(answer, tomato))

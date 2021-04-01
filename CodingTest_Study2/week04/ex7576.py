from collections import deque


def bfs(q, answer):
    count = answer
    while q:
        v = q.popleft()
        nowX = v[0]
        nowY = v[1]
        count = v[2]
        for i in range(4):
            newX = nowX + dx[i]
            newY = nowY + dy[i]
            if 0 <= newX < N and 0 <= newY < M:
                if tomato[newX][newY] == 0 and tomato[newX][newY] != -1:
                    tomato[newX][newY] = 1
                    q.append([newX, newY, count+1])
    return count


def check(answer, tomato):
    for i in range(len(tomato)):
        for j in range(len(tomato[i])):
            if tomato[i][j] == 0:
                return -1
    return answer


M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer = 0
q = deque([])

for i in range(len(tomato)):
    for j in range(len(tomato[i])):
        if tomato[i][j] == 1:
            q.append([i, j, answer])
answer = bfs(q, answer)

print(check(answer, tomato))

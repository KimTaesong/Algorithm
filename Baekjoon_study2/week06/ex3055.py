from collections import deque

R, C = map(int, input().split())  # R행 C열
forest = [list(input()) for _ in range(R)]
start = deque()  # 두더지의 집 위치
water = deque()  # 물의 위치 좌표
end = deque()  # 비버의 굴 위치

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(forest, R, C, start, end, water):
    cnt = 0
    while start:
        cnt += 1
        for j in range(len(water)):
            nowX, nowY = water.popleft()
            for i in range(4):
                newX = nowX + dx[i]
                newY = nowY + dy[i]
                if 0 <= newX < R and 0 <= newY < C:
                    if forest[newX][newY] == '.' or forest[newX][newY] == 'S':
                        forest[newX][newY] = '*'
                        water.append([newX, newY])

        for i in range(len(start)):
            nowX, nowY = start.popleft()
            for k in range(4):
                newX = nowX + dx[k]
                newY = nowY + dy[k]
                if newX == end[0][0] and newY == end[0][1]:
                    return cnt
                if 0 <= newX < R and 0 <= newY < C:
                    if forest[newX][newY] == '.':
                        forest[newX][newY] = 'S'
                        start.append([newX, newY])
    return "KAKTUS"


for i in range(R):
    for j in range(C):
        if forest[i][j] == 'S':  # 두더지의 시작 위치를 저장
            start.append([i, j])
        if forest[i][j] == 'D':  # 비버의 굴 위치를 저장
            end.append([i, j])
        if forest[i][j] == '*':  # 물이 있는 위치들을 저장
            water.append([i, j])

answer = bfs(forest, R, C, start, end, water)
print(answer)

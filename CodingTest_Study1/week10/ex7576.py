#BOJ 토마토 7576
from collections import deque
M, N = map(int, input().split()) # 상자의 크기 M 가로, N 세로
tomato = [0] 
cnt = 0 # 토마토가 익는 날짜
queue = deque() # 1인 토마토를 저장하는 큐
dx = [-1,1,0,0] # 방향벡터 dx (북,남,서,동)
dy = [0,0,-1,1] # 방향벡터 dy
for i in range(N):
    tomato.append([0] + list(map(int, input().split())))

def bfs(q: deque, cnt: int):
    day = cnt
    while q:
        v = q.popleft()
        nowX = v[0]
        nowY = v[1]
        day = v[2]

        for i in range(4):
            newX = nowX + dx[i]
            newY = nowY + dy[i]

            if 1 <= newX <= N and 1 <= newY <= M:
                if tomato[newX][newY] == 0 and tomato[newX][newY] != -1:
                    tomato[newX][newY] = 1
                    q.append([newX, newY, day+1])
    return day

def check(day: int, tomato: deque):
    for i in range(1, N+1):
        for j in range(1, M+1):
            if tomato[i][j] == 0:
                return -1
    return day

# 익은 토마토의 위치를 찾아서 tomato 배열에 좌표값을 저장
for i in range(1,N+1):
    for j in range(1,M+1):
        if tomato[i][j] == 1:
            queue.append([i,j, cnt])

# 인접한 토마토에 의해 익지 않은 토마토를 익혀주는 과정을 bfs를 통해 탐색한다.
cnt = bfs(queue, cnt) 
# 토마토가 모두 익었는지를 체크해준다.
print(check(cnt, tomato))



import sys
sys.setrecursionlimit(10000)


def dfs(x, y, color):
    visited.append((x, y))
    # 4방향 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < N) and (0 <= ny < N):
            # 정상인
            if color == 0:
                pass

            elif color == 1:
                pass


N = int(input())
graphs = [list(input()) for _ in range(N)]
visited = [[1, 0]]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 정상인인 경우

cnt_aver = 0

for i in range(N):
    for j in range(N):
        if graphs[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j, 0)
            cnt_aver += 1

# 적록색맹인 경우
for i in range(N):
    for j in range(N):
        if graphs[i][j] == 'G':
            graphs[i][j] = 'R'


cnt_color = 0
for i in range(N):
    for j in range(N):
        if graphs[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j, 1)
            cnt_color += 1

print(cnt_aver, cnt_color)

# BOJ 미로탈출 2178
from collections import deque
N, M = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = [0] + [[0] + list(map(int, input())) for _ in range(N)]

# 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs
def bfs(x: int, y: int):
    # 큐를 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 대까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 1 or ny < 1 or nx > N or ny > M:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 위치를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[N][M]

# 최단거리를 기록하는 BFS를 호출
print(bfs(1, 1))
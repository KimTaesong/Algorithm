# N, M을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = [list(map(int, input())) for _ in range(n)]

# 상하좌우 방향을 정하는 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 헤당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우 위치도 모두 재귀적으로 호출
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            dfs(nx, ny)
        return True
    return False


# 모든 노드(위치)에 대하여 음료수 채우기
ice_cnt = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            ice_cnt += 1
# 정답 출력
print(ice_cnt)

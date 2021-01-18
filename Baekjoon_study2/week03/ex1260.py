# dfs bfs 1260
from collections import deque

N, M, V = map(int, input().split())  # N 정점의 개수, M 간선의 개수, V 시작 정점
graph = [[0] * (N+1) for _ in range(N+1)]  # 인접 행렬 방식으로 그래프 초기화
for i in range(M):  # 사용자로부터 입력 받은 그래프의 정보
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [False] * (N+1)  # 노드 방문 여부 체크하는 배열
dfs_answer = []
bfs_answer = []


def dfs(V):
    visited[V] = True  # 노드 방문 표시
    dfs_answer.append(V)
    for i in range(1, N+1):
        if visited[i] == 0 and graph[V][i] == 1:
            dfs(i)


def bfs(V):
    queue = deque([V])
    visited[V] = False
    while queue:
        V = queue.popleft()
        bfs_answer.append(V)
        for i in range(1, N+1):
            if visited[i] == 1 and graph[V][i] == 1:
                queue.append(i)
                visited[i] = False


dfs(V)
for i in dfs_answer:
    print(i, end=' ')
print()
bfs(V)
for i in bfs_answer:
    print(i, end=' ')

# BOJ dfs/bfs 바이러스 2606

from collections import deque

com_num = int(input())  # 컴퓨터(노드)의 수
net_num = int(input())  # 네트워크(간선)의 개수
# 컴퓨터가 연결된 그래프: 네트워크 인접 행렬 방식으로 구현 0으로 초기화
network = [[0] * (com_num+1) for _ in range(com_num+1)]
visited = [0] * (com_num+1)  # 방문 노드를 표시하기 위한 배열
cnt = 0  # 바이러스의 개수
dfs_answer = []
bfs_answer = []
for i in range(net_num):
    a, b = map(int, input().split())
    network[a][b] = network[b][a] = 1


def dfs(V):
    visited[V] = True
    global cnt
    dfs_answer.append(V)
    for i in range(1, com_num+1):
        if visited[i] == 0 and network[V][i] == 1:
            dfs(i)
            cnt += 1


def bfs(V):
    queue = deque([V])
    visited[V] = True
    global cnt
    while queue:
        V = queue.popleft()
        bfs_answer.append(V)
        for i in range(1, com_num+1):
            if visited[i] == 0 and network[V][i] == 1:
                queue.append(i)
                visited[i] = 1
                cnt += 1


# dfs(1)
# for i in dfs_answer:
#     print(i, end=' ')
# print()
bfs(1)
# for i in bfs_answer:
#     print(i, end=' ')
print(cnt)

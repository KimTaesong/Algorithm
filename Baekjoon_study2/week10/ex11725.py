# BOJ 11725 트리의 부모 찾기
import sys
input = sys.stdin.readline
node = int(input())  # 노드의 개수
node_graph = [[] for _ in range(node + 1)]  # 그래프
parent = [[] for _ in range(node + 1)]  # 부모 노드를 저장하는 배열

# 트리를 그래프 형태로 생성

for _ in range(node - 1):
    i, j = map(int, input().split())
    node_graph[i].append(j)
    node_graph[j].append(i)

# DFS로 탐색


def dfs(graph_list, start, parent):
    stack = [start]

    while stack:
        node = stack.pop()
        for i in graph_list[node]:
            parent[i].append(node)
            stack.append(i)
            graph_list[i].remove(node)
    return parent


for i in list(dfs(node_graph, 1, parent))[2:]:
    print(i[0])

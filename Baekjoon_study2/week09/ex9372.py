# BOJ 9372 상근이의 여행
# . 1 최소 신장 트리
"""
N개의 노드를 잇는 최소 신장 트리를 구하는 것
간선의 가중치 동일 -> 사이클이 없는 그래프
입력은 항상 연결 그래프 -> 모든 노드가 다른 노드와 연결되는 간선을 하나씩만 가지기 때문에
그 간선의 개수만 구해주면 되는 문제 노드이 개수 N개 -> 간선의 개수: N-1 개 why? 0 - 0
"""

# from sys import stdin
# for _ in range(int(stdin.readline())):
#     n, m = map(int, stdin.readline().split())

#     for _ in range(m):
#         a, b = map(int, stdin.readline().split())

#     print(n-1)

# . 2 BFS를 이용한 풀이
import sys
from collections import deque
input = sys.stdin.readline


def bfs(x: int):
    queue = deque()
    queue.append(x)
    c[x] = 1
    cnt = 0
    while queue:
        x = queue.popleft()
        for nx in a[x]:
            if c[nx] == 0:
                c[nx] = 1
                cnt += 1
                queue.append(nx)
    return cnt


testcase = int(input())
while testcase:
    n, m = map(int, input().split())
    a = [[] for _ in range(n)]
    c = [0] * n
    for _ in range(m):
        x, y = map(int, input().split())
        a[x-1].append(y-1)
        a[y-1].append(x-1)

    ans = 0
    for i in range(n):
        if c[i] == 0:
            ans += bfs(i)
    print(ans)
    testcase -= 1

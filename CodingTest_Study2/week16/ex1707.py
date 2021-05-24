import sys
from collections import deque


def bfs(x):
    visited[x] = 1
    q = deque([x])
    while q:
        a = q.popleft()
        for i in queue[a]:
            if visited[i] == 0:
                visited[i] = - visited[a]
                q.append(i)
            else:
                if visited[i] == visited[a]:
                    return False
    return True


k = int(input())
for i in range(k):
    v, e = map(int, input().split())
    queue = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    flag = 1

    for j in range(e):
        a, b = map(int, input().split())
        queue[a].append(b)
        queue[b].append(a)

    for k in range(1, v+1):
        if visited[k] == 0:
            if not bfs(k):
                flag = -1
                break

    print("YES" if flag == 1 else "NO")

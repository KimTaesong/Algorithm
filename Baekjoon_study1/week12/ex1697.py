# BOJ 1697 숨바꼭질
# from collections import deque


# def bfs(v: int):
#     q = deque([v])
#     while q:
#         x = q.popleft()
#         if x == k:
#             print(distance[x])
#             break
#         for nx in (x - 1, x + 1, x * 2):
#             if 0 <= nx <= Max and not distance[nx]:
#                 distance[nx] = distance[x] + 1
#                 q.append(nx)


# Max = 10 ** 5
# distance = [0] * (Max + 1)
# n, k = map(int, input().split())
# bfs(n)

from collections import deque


def bfs(v):
    count = 0
    q = deque([[v, count]])
    while q:
        v = q.popleft()
        x = v[0]
        count = v[1]
        if not visited[x]:
            visited[x] = True
            if x == K:
                return count
            count += 1
            if (x * 2) <= 100000:
                q.append([x * 2, count])
            if (x + 1) <= 100000:
                q.append([x + 1, count])
            if (x - 1) >= 0:
                q.append([x - 1, count])
    return count


N, K = map(int, input().split())
visited = [False] * 100001
print(bfs(N))

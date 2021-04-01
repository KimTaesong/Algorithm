from collections import deque
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    queue = []
    cnt = 0
    for i in range(len(priority)):
        queue.append([priority[i], i])
    while queue:
        if queue[0][0] < max(queue)[0]:
            V = queue.pop(0)
            queue.append(V)
        else:
            V = queue.pop(0)
            print(queue)
            cnt += 1
            if V[1] == M:
                print(cnt)

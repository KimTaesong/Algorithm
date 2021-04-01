# BOJ 회전하는 큐 1021
from collections import deque
N, M = map(int, input().split())  # 큐의 크기 N, 뽑아내려고 하는 수의 개수 M
queue = deque([i for i in range(1, N+1)])  # 1 ~ N까지 들어있는 큐
choice_idx = list(map(int, input().split()))  # 뽑으려고 하는 수의 위치
total_cnt = 0
for i in choice_idx:
    # print(i)
    if i == queue[0]:
        queue.popleft()
    else:
        left_cnt = 0
        right_cnt = 0
        while i != queue[left_cnt]:
            left_cnt += 1
            # print(f"left_cnt: {left_cnt}")

        while i != queue[right_cnt]:
            right_cnt -= 1
            # print(f"right_cnt: {right_cnt}")

        right_cnt = abs(right_cnt)

        if left_cnt < right_cnt:
            total_cnt += left_cnt
            for k in range(left_cnt):
                queue.append(queue.popleft())
            queue.popleft()

        else:
            total_cnt += right_cnt
            for j in range(right_cnt):
                queue.appendleft(queue.pop())
            queue.popleft()

        # print(queue)
print(total_cnt)

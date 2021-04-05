from collections import deque


def solution(priorities, location):
    priorities = deque(priorities)
    queue = deque([])
    cnt = 0
    target = priorities[location]
    for i in range(len(priorities)):
        queue.append(i)

    while priorities:
        if priorities[0] != max(priorities):
            priorities.append(priorities.popleft())
            queue.append(queue.popleft())
        else:
            cnt += 1
            priority = priorities.popleft()
            idx = queue.popleft()
            if priority == target and idx == location:
                return cnt
        print(queue, priorities)

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    ready_q = deque(truck_weights)
    bridge_q = deque([0]*bridge_length)
    arrive_stack = []
    time = 0
    sum_value = 0
    while len(arrive_stack) != len(truck_weights):
        if sum_value:
            bridge_q.rotate(1)

        if ready_q and sum_value + ready_q[0] <= weight:
            sum_value += ready_q[0]
            bridge_q[0] = ready_q.popleft()
        time += 1

        if bridge_q[-1]:
            arrive_stack.append(bridge_q[-1])
            sum_value -= bridge_q[-1]
            bridge_q[-1] = 0

    time += 1
    answer = time
    print(answer)
    return answer


bridge_length = [2, 100, 100]
weight = [10, 100, 100]
truck_weights = [[7, 4, 5, 6], [10], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]

for i in range(3):
    solution(bridge_length[i], weight[i], truck_weights[i])

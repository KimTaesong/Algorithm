# BOJ 20055 컨베이어 벨트 위의 로봇
import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([0]*2*n)

level = 1
while True:
    # 과정 1
    belt.rotate(1)  # 오른쪽으로 1칸씩 회전, deque의 내장함수 중 하나 rotate()
    robot.rotate(1)  # 벨트가 움직이면 위에 있는 로봇도 같이 회전
    robot[n-1] = 0  # 회전하면 내려가는 벨트 위치에 있는 로봇은 떨어짐

    # 과정 2 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    for i in range(n-2, -1, -1):
        # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다
        if robot[i] and not robot[i+1] and belt[i+1]:
            belt[i+1] -= 1
            robot[i+1], robot[i] = robot[i], 0
    robot[n-1] = 0

    # 과정 3 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    if not robot[0] and belt[0]:
        robot[0] = 1
        belt[0] -= 1

    # 과정 4 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if belt.count(0) >= k:
        print(level)
        break

    level += 1

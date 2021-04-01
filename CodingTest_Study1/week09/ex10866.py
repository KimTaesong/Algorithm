# BOJ 10866 덱
from collections import deque
import sys

N = int(sys.stdin.readline().strip())  # N 명령의 수
integer = deque()  # 정수를 저장하는 덱


def check(comnd: str):

    # print(comnd[0])

    if comnd[0] == 'push_back':
        integer.append(comnd[1])

    elif comnd[0] == 'push_front':
        integer.appendleft(comnd[1])

    elif comnd[0] == 'pop_front':
        if integer:
            print(integer.popleft())
        else:
            # print("현재 덱이 비어있습니다.")
            print(-1)

    elif comnd[0] == 'pop_back':
        if integer:
            print(integer.pop())
        else:
            # print("현재 덱이 비어있습니다.")
            print(-1)

    elif comnd[0] == 'front':
        if integer:
            print(integer[0])
        else:
            print(-1)

    elif comnd[0] == 'back':
        if integer:
            print(integer[-1])
        else:
            print(-1)

    elif comnd[0] == 'size':
        print(len(integer))

    elif comnd[0] == 'empty':
        if integer:
            print(0)
        else:
            print(1)


for i in range(N):
    command = sys.stdin.readline().strip().split()
    check(command)
    # print(integer)

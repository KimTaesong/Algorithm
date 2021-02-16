#  BOJ 뱀 3190
from collections import deque

N = int(input())  # N: 정사각 보드의 한 변의 길이
K = int(input())  # K: 사과의 개수
game_board = [[0] * (N+1) for _ in range(N+1)]  # N x N 게임 보드
visited = [[0] * (N+1) for _ in range(N+1)]  # N x N 뱀이 보드판을 방문한 위치를 체크하는 배열
rotate_data = deque()  # 회전 정보에 대한 배열 [회전 시간, 회전 방향]
cur_time = 0  # 현재 시간
snake = deque()

for i in range(K):
    a, b = map(int, input().split())  # a: 행, b: 열
    game_board[a][b] = 1  # 게임판 위의 사과 위치를 1로 표시

L = int(input())  # 뱀의 방향 변환 횟수

for i in range(L):
    # X: 경과 시간(초) X초가 끝난 뒤 C: 회전 방향 1) L: 왼쪽 90도 방향으로 회전, 2) D: 오른쪽 90도 방향으로 회전
    X, C = input().split()
    rotate_data.append([int(X), C])

cur_vector = [1, 0]  # 뱀이 움직이는 방향
# print(rotate_data[0])


def check_vector(vector: list, C: str):

    # print(vector, C)
    if vector == [-1, 0]:
        if C == 'L':
            return [0, 1]
        if C == 'D':
            return [0, -1]

    elif vector == [1, 0]:
        if C == 'L':
            return [0, -1]
        if C == 'D':
            return [0, 1]

    elif vector == [0, -1]:
        if C == 'L':
            return [-1, 0]
        if C == 'D':
            return [1, 0]

    elif vector == [0, 1]:
        if C == 'L':
            return [1, 0]
        if C == 'D':
            return [-1, 0]

    else:
        print("예외가 발생했습니다.")
        exit()


# print(rotate_data)


def dfs(x: int, y: int):

    global cur_time
    global cur_vector

    snake.append([x, y])

    while True:

        cur_time += 1
        # print(f"cur_time: {cur_time}")

        x = x + cur_vector[1]
        y = y + cur_vector[0]
        # print(x, y)

        if rotate_data and rotate_data[0][0] == cur_time:
            # print("회전이 시작됩니다.")
            time, rotation = rotate_data.popleft()
            cur_vector = check_vector(cur_vector, rotation)
            # print(cur_vector)

        if (x <= 0 or N+1 <= x) or (y <= 0 or N+1 <= y):
            # print("범위를 벗어났습니다.")
            # print(x, y)
            print(cur_time)
            exit()

        else:
            if game_board[x][y] == 0:
                game_board[x][y] = 2
                snake.append([x, y])
                a, b = snake.popleft()
                game_board[a][b] = 0

            elif game_board[x][y] == 1:
                game_board[x][y] = 2
                snake.append([x, y])

            elif game_board[x][y] == 2:
                # print("뱀 자신의 몸에 부딪쳤습니다.")
                print(cur_time)
                exit()

            else:
                # print("예외가 발생했습니다.")
                exit()


dfs(1, 1)

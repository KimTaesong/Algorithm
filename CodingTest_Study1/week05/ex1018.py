#  BOJ 브루트포스 체스판 다시 칠하기 1018
N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]  # 입력 받은 체스판
min_list = []  # 최소값들이 저장될 배열
white_chess = [  # (0,0)이 W로 시작하는 체스판
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

]

black_chess = [  # (0,0)이 B로 시작하는 체스판
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
]


# 체스판을 자를 수 있는 왼쪽위 상단의 위치
for i in range(N-7):
    for j in range(M-7):
        black_cnt = 0  # 윗상단이 블랙 체스판에서 다시 칠해줘야 하는 개수
        white_cnt = 0  # 윗상단이 흰색 체스판에서 다시 칠해줘야 하는 개수
        # 체스판을 자를 수 있는 모든 위치에서 전수 조사
        for a in range(i, i+8):
            for b in range(j, j+8):
                if graph[a][b] != white_chess[a-i][b-j]:  # 윗 상단이 흰색 체스판의 경우와 일치하지 않으면 추가
                    white_cnt += 1
                if graph[a][b] != black_chess[a-i][b-j]:  # 윗 상단이 블랙 체스판의 경우와 일치하지 않으면 추가
                    black_cnt += 1
        min_value = min(white_cnt, black_cnt)  # 두가지 경우 중 최소값을 최소값 배열에 저장
        min_list.append(min_value)
print(min(min_list))  # 최소값 배열 중 가장 작은 수를 출력

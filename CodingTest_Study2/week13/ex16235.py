# BOJ 16235 나무재테크
import sys
from collections import deque
input = sys.stdin.readline


def myprint(arr):
    for a in arr:
        print(a)
    print()


# 1. 초기 주어진 정보
# 상 하 좌 우 좌상 좌하 우상 우하
d = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, -1], [-1, 1], [1, 1]]
n, m, k = map(int, input().split())  # n개의 길이, m개의 나무, k년 이후
A = [list(map(int, input().split())) for _ in range(n)]  # 매년 영양분 추가량
trees = [list(map(int, input().split())) for _ in range(m)]  # m개의 나무가 심어지는 위치
# board: 나무가 심어져 있는지를 저장하는 배열
# deque을 사용한 이유: 나무들을 효과적으로 관리하기 위해서
board = [[deque() for _ in range(n)] for _ in range(n)]
nutri = [[5 for _ in range(n)] for _ in range(n)]  # 초기 땅의 영양분 상태

# 나무를 땅에 심는 과정
for tree in trees:
    r, c, old = tree  # r: 행, c: 열, old: 나무의 나이
    board[r-1][c-1].append(old)

# print("초기")
# myprint(board)
# myprint(nutri)

# 2. k년을 경과 시킴
for year in range(k):
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            tree_cnt = len(board[r][c])

            if tree_cnt == 0:
                nutri[r][c] += A[r][c]  # 나무가 없어도 영양분은 모두 주니까
                continue

            sub_nutri = 0  # 봄에 빠지는 양분
            add_nutri = 0  # 여름에 빠지는 양분
            slice_num = tree_cnt  # 이 나무 이상으로 늙은나무는 다 죽는다.

            # 정렬되어 있으므로 어린나무부터 성장
            for i in range(tree_cnt):
                # 양분이 부족하면 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
                if sub_nutri + board[r][c][i] > nutri[r][c]:
                    slice_num = i
                    break

                sub_nutri += board[r][c][i]  # 자신의 나이만큼 양분을 먹은 후
                board[r][c][i] += 1  # 나무의 나이가 1 증가
            nutri[r][c] -= sub_nutri  # 봄에 빠지는 양분

            # 여름에는 봄에 죽은 나무가 양분으로 변하게 된다.
            # 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가됨.
            for i in range(slice_num, tree_cnt):
                add_nutri += (board[r][c][i] // 2)

            nutri[r][c] += add_nutri  # 여름에 빠지는 양분

            for _ in range(tree_cnt - slice_num):
                board[r][c].pop()  # 늙은 나무 죽음

            tree_cnt = len(board[r][c])
            # 가을 부분
            for i in range(tree_cnt):
                if board[r][c][i] % 5 != 0:
                    continue

                for j in range(8):
                    nr, nc = r + d[j][0], c + d[j][1]
                    if 0 <= nr < n and 0 <= nc < n:
                        # 새로 추가할 1랩나무 개수
                        temp[nr][nc] += 1
            # 겨울 부분
            nutri[r][c] += A[r][c]   # 겨울에 더해지는 양분

# 번식할 나무를 반영한다.
for r in range(n):
    for c in range(n):
        if temp[r][c] <= 0:
            continue

        for _ in range(temp[r][c]):
            board[r][c].appendleft(1)

print(year+1)
myprint(board)
myprint(nutri)

ans = 0
for r in range(n):
    for c in range(n):
        ans += len(board[r][c])
print(ans)

# BOJ 1080 행렬
N, M = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(N)]  # 첫번째 행렬
B = [list(map(int, list(input()))) for _ in range(N)]  # 두번째 행렬
cnt = 0  # 뒤집는 횟수

# A 행렬과 B 행렬이 같은지 체크하는 함수


def check():
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return False
    return True

# 뒤집기 함수


def reversed(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]  # 뒤집기 # 3*3 행렬의 왼쪽 상단 지점을 기준으로 삼는다.


for i in range(0, N-2):  # 0 ~ N-3
    for j in range(0, M-2):  # 0 ~ M-3
        if A[i][j] != B[i][j]:  # 같지 않으면 뒤집기 시작
            cnt += 1
            reversed(i, j)
if check():  # 만약에 뒤집힌 A 행렬과 B 행렬이 같으면 뒤집기 횟수 출력
    print(cnt)

else:
    print(-1)

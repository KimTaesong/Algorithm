# BOJ 재귀 별 찍기 10 2447
import sys

input = sys.stdin.readline
N = int(input())
graph = [['*'] * N for _ in range(N)]


def star_print(a, b, n):  # a: 행의 시작 위치, b: 열의 시작 위치, n: 정사각형의 길이

    if n == 3:  # 재귀 종료 조건, 길이가 3인 정사각형에서는 가운데 원소만 공백으로 초기화
        graph[a+1][b+1] = ' '

    else:  # 길이가 3이상인 정사각형에서는 다음을 반복
        idx = n // 3  # 길이가 n인 정사각형을 3등분한 길이
        for i in range(a+idx, a+idx*2):  # 길이가 n인 정사각형의 시작위치 좌표가 (a,b)인 가운데 정사각형 부분을 공백으로 바꿔 줌
            for j in range(b+idx, b+idx*2):
                graph[i][j] = ' '

        # 재귀함수의 시작 위치를 지정
        for i in range(a, a+n):
            for j in range(b, b+n):
                if i % idx == 0 and j % idx == 0:
                    star_print(i, j, idx)


star_print(0, 0, N)
for i in range(N):
    for j in range(N):
        print(graph[i][j], end='')
    print()

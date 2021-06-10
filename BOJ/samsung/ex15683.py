import sys
from collections import deque
sys.stdin = open("BOJ/samsung/input01.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    cctv = []
    up, right, down, left = 0, 1, 2, 3
    total_cnt = 0
    check_cnt = 0

    def check(x, y, dir):
        result = set()
        for d in dir:
            nx, ny = x, y
            while True:
                nx += dx[d]
                ny += dy[d]

                if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                    break

                if graph[nx][ny] == 6:
                    break

                if graph[nx][ny] == 0:
                    result.add((nx, ny))

        return result

    def dfs(n, union_set):
        global check_cnt
        if n == len(cctv):
            if check_cnt < len(union_set):
                check_cnt = len(union_set)
            return

        for i in cctv[n]:
            dfs(n+1, union_set | i)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                total_cnt += 1
            # 1번 CCTV
            elif graph[i][j] == 1:
                cctv.append([check(i, j, [up]), check(i, j, [right]),
                             check(i, j, [down]), check(i, j, [left])])

            # 2번 CCTV
            elif graph[i][j] == 2:
                cctv.append(
                    [check(i, j, [up, down]), check(i, j, [right, left])])

            # 3번 CCTV
            elif graph[i][j] == 3:
                cctv.append([check(i, j, [up, right]), check(
                    i, j, [right, down]), check(i, j, [down, left]), check(i, j, [left, up])])

            # 4번 CCTV
            elif graph[i][j] == 4:
                cctv.append([check(i, j, [up, right, down]), check(
                    i, j, [right, down, left]), check(i, j, [down, left, up]), check(i, j, [left, up, right])])

            # 5번 CCTV
            elif graph[i][j] == 5:
                cctv.append([check(i, j, [up, right, down, left])])

    dfs(0, set())
    print(total_cnt - check_cnt)

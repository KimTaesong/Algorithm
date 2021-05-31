def solution(n):
    # 직각 삼각형 리스트 생성 및 초기화
    graph = [[0 for j in range(1, i+1)] for i in range(1, n+1)]

    # 좌표 초기화 => 처음 시작은 아래 방향
    x, y = -1, 0 # 처음에 x좌표부터 시작하므로
    num = 1

    for i in range(n):  # n번의 방향 전환 (아래 -> 오른 -> 위 -> 아래 .. 반복)
        for j in range(i, n):  # 방향에 따른 좌표값 채우기
            if i % 3 == 0:  # 아래
                x += 1

            elif i % 3 == 1:  # 오른
                y += 1

            else:  # 위
                x -= 1
                y -= 1

            graph[x][y] = num
            num += 1
            print(f"x: {x}, y: {y}, graph[x][y]: {graph[x][y]}, num: {num}")


solution(4)

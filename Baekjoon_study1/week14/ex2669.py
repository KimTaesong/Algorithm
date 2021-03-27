# BOJ 2669 직사각형 네개의 합집합 구하기
sqares = [list(map(int, input().split())) for i in range(4)]
graph = [[0] * 101 for i in range(101)]
cnt = 0
for i in range(4):
    j = sqares[i]
    for y in range(j[1], j[3]):
        for x in range(j[0], j[2]):
            if graph[y][x] == 0:
                graph[y][x] = 1
                cnt += 1
print(cnt)

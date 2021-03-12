# BOJ 15686 치킨 배달
from itertools import combinations
N, M = map(int, input().split())  # N x N 도시를 만들기 위한 N, 폐업시키지 않을 치킨집: M
city_map = [list(map(int, input().split()))
            for _ in range(N)]  # 도시의 지도 0: 빈 집, 1: 집, 2: 치킨집
chicken_store = []  # 치킨집의 위치를 저장하는 배열
house = []  # 집의 위치를 저장하는 배열
chicken_length_sum = 0  # 치킨 거리의 합을 저장할 변수

for i in range(N):
    for j in range(N):
        if city_map[i][j] == 1:
            house.append([i, j])
        if city_map[i][j] == 2:
            chicken_store.append([i, j])

chicken_store_combination = list(combinations(
    chicken_store, M))  # M개의 치킨 집의 조합을 저장하는 배열
chicken_length = [1000] * len(house)  # 각 집의 치킨 거리를 저장하기 위한 배열 ex)
# print(house, chicken_store_combination, chicken_length)

for i in range(len(chicken_store_combination)):  # 치킨 집의 조합의 개수 x 각 집의 개수의 치킨 거리를 조사
    for j in range(len(house)):  # 집의 개수
        for k in range(M):  # M가지 선택된 치킨 집의 개수만큼 조사

            tmp = abs(chicken_store_combination[i][k][0] - house[j][0]) + \
                abs(chicken_store_combination[i][k][1] -
                    house[j][1])  # 각 집의 치킨 거리를 tmp 변수에 임시 저장
            # print(i, j, k, tmp)

            # 새로 구한 치킨 거리와 기존의 치킨 거리를 비교해서 더 작으면 치킨 배열을 갱신
            if tmp < chicken_length[j]:
                chicken_length[j] = tmp

    # print(chicken_length)
    if i == 0:
        chicken_length_sum = sum(chicken_length)

    else:  # 새로 구한 치킨 거리와 기존의 치킨 거리를 비교해서 더 작으면 치킨 거리의 합을 갱신
        if chicken_length_sum > sum(chicken_length):
            chicken_length_sum = sum(chicken_length)
    # print(chicken_length_sum)

    chicken_length = [1000] * len(house)  # 하나의 치킨 집 조합에 대한 검사를 마치면 초기화

print(chicken_length_sum)

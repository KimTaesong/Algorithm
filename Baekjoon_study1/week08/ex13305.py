# BOJ 주유소 13305
N = int(input())  # 도시의 개수 N
road_length = list(map(int, input().split()))  # 인접한 두 도시 사이의 도로 길이
city_oil_cost = list(map(int, input().split()))  # 도시에 있는 주유소의 리터당 가격
min_oil = city_oil_cost[0]  # 처음 도시에서 출발하는 최소 기름
min_oil_cost = 0  # 최소 기름의 양
for i in range(len(road_length)):

    min_oil_cost += min_oil * road_length[i]
    if min_oil > city_oil_cost[i+1]:
        min_oil = city_oil_cost[i+1]
print(min_oil_cost)

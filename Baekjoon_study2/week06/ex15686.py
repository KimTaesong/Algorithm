# BOJ 15686 치킨 배달

N, M = map(int, input().split())  # N: N x N개의 도시 정보, M: 폐업시키질 않을 치킨집의 최대 개수
city_map = [list(map(int, input().split())) for _ in range(N)]
print(city_map)
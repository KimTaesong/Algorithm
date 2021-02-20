# BOJ 공유기 설치 2110
N, C = map(int, input().split())  # N 집의 개수, C 공유기의 개수
home = [int(input()) for i in range(N)]  # 집의 좌표
home.sort()
print(home)

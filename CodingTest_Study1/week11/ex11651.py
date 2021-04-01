# BOJ 좌표 정렬하기 2 11651
N = int(input())  # 점의 개수
location = []  # 좌표의 집합 배열
for i in range(N):
    x, y = map(int, input().split())  # x좌표, y좌표
    location.append([x, y])  # 리스트 형태로 좌표 배열에 저장

sorted_location = sorted(location, key=lambda x: (x[1], x[0]))
for k in sorted_location:
    print(k[0], k[1])

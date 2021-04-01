# BOJ 예산 2512
import sys
input = sys.stdin.readline

n = int(input())  # 지방의 수 n
city_budget = list(map(int, input().split()))  # 마을의 요청 예산
total_budget = int(input())  # 총 예산
# why? 이진
start, end = 1, max(city_budget)
while start <= end:
    mid = (start+end) // 2
    tmp_budget = 0
    for i in city_budget:
        if mid > i:
            tmp_budget += i
        else:
            tmp_budget += mid

    if tmp_budget <= total_budget:
        start = mid + 1
    else:
        end = mid - 1
print(end)

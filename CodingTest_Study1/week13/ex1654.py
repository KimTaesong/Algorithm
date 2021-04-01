# BOJ 랜선 자르기 1654
import sys
input = sys.stdin.readline
k, n = map(int, input().split())  # k : 랜선의 개수, n: 필요한 랜선의 개수
lan_wire = [int(input()) for _ in range(k)]  # 주어진 랜선

# why ? 이진탐색인가 N: 1,000,000이라는 큰 수이기 때문에 순차탐색으로 하면 시간 초과.
start, end = 1, max(lan_wire)
while start <= end:
    mid = (start + end) // 2
    lan_cnt = 0  # 랜선의 개수
    # 주어진 랜선에서 mid 값인 랜선의 개수를 구하는 과정
    for i in lan_wire:
        lan_cnt += i // mid
    # 주어진 랜선의 개수보다 크거나 같으면 랜선의 탐색 범위를 mid+1 ~ end 로 갱신.
    if lan_cnt >= n:
        start = mid + 1
    # 주어진 랜선의 개수보다 작으면 랜선의 탐색 범위를 start ~ mid - 1 로 갱신.
    else:
        end = mid - 1
print(end)

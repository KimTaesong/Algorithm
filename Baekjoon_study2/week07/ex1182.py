# BOJ 1182 부분수열의 합
from itertools import combinations
N, S = map(int, input().split())  # 정수의 개수 N, 정수의 합 S
nums = list(map(int, input().split()))  # 배열 nums
cnt = 0  # S의 값과 같은 조합의 개수

for i in range(1, N+1):
    sub = list(combinations(nums, i))
    for j in sub:
        if sum(j) == S:
            cnt += 1

print(cnt)

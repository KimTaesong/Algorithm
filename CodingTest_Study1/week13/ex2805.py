# BOJ 2805 나무 자르기
import sys
input = sys.stdin.readline
n, m = map(int, input().split())  # 나무의 수 n, 나무의 길이 m
trees = list(map(int, input().split()))  # 나무 배열
start, end = 1, max(trees)
while start <= end:
    mid = (start + end) // 2
    slicing_tree = 0
    for tree in trees:
        if tree > mid:
            slicing_tree += tree - mid

    if slicing_tree >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)

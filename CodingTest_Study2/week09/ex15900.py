# BOJ 15900 나무 탈출 - 미해결
# 1. 루트노드에서 리프노드의 거리의 총합이 짝수이면 성원이가 필승, 홀수이면 성원이가 필패
total_leaf_cnt = 0
N = int(input())
for i in range(N-1):
    a, b = map(int, input().split())

if total_leaf_cnt % 2 == 0:
    print('Yes')
else:
    print('No')

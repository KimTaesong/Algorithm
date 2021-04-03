# BOJ 스타트와 링크 14889
from itertools import combinations
N = int(input())
start_link = []
people = [i for i in range(1, N+1)]
combi = list(combinations(people, N//2))
start = combi

for i in range(N):
    start_link.append(list(map(int, input().split())))


min_value = 100000
for i in range(len(start)//2):
    start_cnt = 0
    link_cnt = 0
    combi1 = list(combinations(start[i], 2))
    combi2 = list(combinations(start[len(start)-1-i], 2))
    # print(combi1)
    # print(combi2)
    for k in combi1:
        start_cnt += start_link[k[0]-1][k[1]-1] + start_link[k[1]-1][k[0]-1]

    for k in combi2:
        link_cnt += start_link[k[0]-1][k[1]-1] + start_link[k[1]-1][k[0]-1]
    # print(start_cnt)
    # print(link_cnt)
    tmp = abs(start_cnt-link_cnt)
    # print(tmp)
    if tmp < min_value:
        min_value = tmp
print(min_value)

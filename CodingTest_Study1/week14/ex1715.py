# BOJ 1715 카드 정렬하기
# import sys
# input = sys.stdin.readline
# N = int(input())
# card_list = []
# temp = 0
# cnt = 0
# for i in range(N):
#     card = int(sys.stdin.readline())
#     card_list.append(card)

# while card_list:
#     temp = 0
#     if len(card_list) == 1:
#         cnt += card_list.pop()

#     if len(card_list) == 2:
#         temp += card_list.pop()
#         temp += card_list.pop()
#         cnt += temp

#     if len(card_list) > 2:
#         for i in range(2):
#             for j in range(len(card_list)-1-i):
#                 if card_list[j] <= card_list[j+1]:
#                     card_list[j], card_list[j+1] = card_list[j+1], card_list[j]
#         temp += card_list.pop() + card_list.pop()
#         cnt += temp
#         card_list.append(temp)

# print(cnt)

import heapq

n = int(input())
card_list = []
for i in range(n):
    heapq.heappush(card_list, int(input()))

if len(card_list) == 1:
    print(0)
else:
    cnt = 0
    while len(card_list) > 1:
        temp1 = heapq.heappop(card_list)
        temp2 = heapq.heappop(card_list)
        cnt += temp1 + temp2
        heapq.heappush(card_list, temp1+temp2)
    print(cnt)

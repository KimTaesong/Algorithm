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

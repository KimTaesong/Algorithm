import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while scoville[0] < K:
        try:
            mix_sco = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        except IndexError:
            return -1

        heapq.heappush(scoville, mix_sco)

        cnt += 1
    return cnt

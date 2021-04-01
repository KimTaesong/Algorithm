# BOJ 우선 순위 큐 11279 최대 힙
import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for i in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (-num))
    else:
        if not heap:
            print(0)
        else:
            print(-1 * heapq.heappop(heap))

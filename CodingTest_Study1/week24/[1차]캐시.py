from collections import deque


def solution(cacheSize, cities):
    cache = deque([])
    cnt = 0
    for i in cities:
        i = i.lower()
        if i not in cache:
            if cacheSize == 0:
                return 5 * len(cities)

            if len(cache) == cacheSize:
                cache.popleft()
            cnt += 5
            cache.append(i)
        else:
            cnt += 1
            cache.remove(i)
            cache.append(i)
        # print(cache)

    return cnt

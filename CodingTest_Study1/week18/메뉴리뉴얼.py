from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []

    for course_cnt in course:
        temp = []
        # print(course_cnt)
        for order in orders:
            combi = combinations(sorted(order), course_cnt)
            temp += combi
            # print(temp)
        counter = Counter(temp)
        # print(counter)

        if len(counter) != 0 and max(counter.values()) != 1:
            # print(counter.values())
            answer += [''.join(f) for f in counter if counter[f]
                       == max(counter.values())]
            # print(answer)

    return sorted(answer)

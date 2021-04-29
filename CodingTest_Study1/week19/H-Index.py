def solution(citations):
    n = len(citations)
    citations = sorted(citations)
    # 0 1 3 5 6
    # 0 1 2 3 4
    # 5 4 3 2 1
    for i in range(n):
        # 논문의 인용 횟수 >= 논문의 개수
        print(citations[i], n-i)
        if citations[i] >= n - i:
            return n - i

    return 0

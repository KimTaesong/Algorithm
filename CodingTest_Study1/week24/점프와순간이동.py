def solution(n):
    cnt = 0
    while n:
        if n % 2 == 0:
            n = n // 2

        elif n % 2 == 1:
            n -= 1
            cnt += 1
    return cnt

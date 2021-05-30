def solution(n, a, b):
    cnt = 0
    while a != b:
        cnt += 1
        a = (a+1) // 2
        b = (b+1) // 2
    return cnt

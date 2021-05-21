def solution(left, right):
    result = 0
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                cnt += 1
                print(i, cnt)
        cnt += 1
        if cnt % 2 == 0:
            result += i
        else:
            result -= i
    return result

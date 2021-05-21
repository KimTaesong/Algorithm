def solution(n):
    tmp = []
    while n:
        tmp.append(n % 3)
        n = n // 3

    answer = 0
    for i in range(len(tmp)):
        answer += 3 ** (i) * tmp[n-1-i]
        print(i, tmp[i], answer)
    return answer

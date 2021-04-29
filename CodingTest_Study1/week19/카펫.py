def solution(brown, yellow):
    answer = []
    total = brown + yellow
    tmp = []
    for i in range(total//2 - 1, 2, -1):
        if total % i == 0:
            tmp.append(i)

    n = len(tmp)
    if n % 2 == 0:
        for k in range(n // 2):
            if ((tmp[k] + tmp[n-1-k]) * 2) - 4 == brown:
                return [tmp[k], tmp[n-1-k]]
    else:
        for k in range(n // 2):
            if (tmp[k] + tmp[n-1-k] * 2) - 4 == brown:
                return [tmp[k], tmp[n-1-k]]
        return [tmp[n//2], tmp[n//2]]

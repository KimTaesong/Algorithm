def solution(a, b):
    cnt = 0
    for i in range(len(a)):
        cnt += a[i] * b[i]

    return cnt


a = [[1, 2, 3, 4], [-1, 0, 1]]
b = [[-3, -1, 0, 2], [1, 0, -1]]
for i in range(len(a)):
    print(solution(a[i], b[i]))

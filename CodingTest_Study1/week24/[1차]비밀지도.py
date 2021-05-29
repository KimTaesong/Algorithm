def solution(n, arr1, arr2):
    graph = [[" "] * n for _ in range(n)]
    for i in range(n):
        value1 = arr1[i]
        value2 = arr2[i]
        for j in range(n):
            if value1 % 2:
                graph[i][n-1-j] = '#'
            if value2 % 2:
                graph[i][n-1-j] = '#'
            value1 //= 2
            value2 //= 2

    answer = []
    for i in range(n):
        tmp = ""
        for j in range(n):
            tmp += graph[i][j]
        answer.append(tmp)
    return answer

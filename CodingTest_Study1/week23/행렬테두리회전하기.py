def solution(rows, columns, queries):
    graph = [[row * columns + col +
              1 for col in range(columns)] for row in range(rows)]
    answer = []

    for i in queries:
        x1, y1, x2, y2 = i[0]-1, i[1]-1, i[2]-1, i[3]-1
        tmp = graph[x1][y1]
        minimum = tmp

        for y in range(x1, x2):
            value = graph[y+1][y1]
            graph[y][y1] = value
            minimum = min(minimum, value)

        for x in range(y1, y2):
            value = graph[x2][x+1]
            graph[x2][x] = value
            minimum = min(minimum, value)

        for y in range(x2, x1, -1):
            value = graph[y-1][y2]
            graph[y][y2] = value
            minimum = min(minimum, value)

        for x in range(y2, y1, -1):
            value = graph[x1][x-1]
            graph[x1][x] = value
            minimum = min(minimum, value)

        graph[x1][y1+1] = tmp
        answer.append(minimum)

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))

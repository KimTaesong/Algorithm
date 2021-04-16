def solution(array: list, commands: list) -> int:
    answer = []
    for a in range(len(commands)):
        i, j, k = commands[a][0] - 1, commands[a][1] - 1, commands[a][2] - 1
        answer.append(sorted(array[i:j+1])[k])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

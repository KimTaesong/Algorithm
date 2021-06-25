def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if (arr[i] % divisor == 0):
            answer.append(arr[i])
    if(len(answer) == 0):
        answer.append(-1)
    answer.sort()
    return answer

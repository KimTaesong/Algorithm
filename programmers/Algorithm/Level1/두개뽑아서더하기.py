def solution(numbers):
    answer = []
    cnt = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                cnt = numbers[i] + numbers[j]
                if cnt not in answer:
                    answer.append(cnt)
    answer.sort()
    return answer

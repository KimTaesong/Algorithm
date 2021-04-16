def solution(answers: list):
    n = len(answers)
    answer = []
    user1 = [1, 2, 3, 4, 5] * (n//5) + [1, 2, 3, 4, 5][:n % 5]
    user2 = [2, 1, 2, 3, 2, 4, 2, 5] * \
        (n//8) + [2, 1, 2, 3, 2, 4, 2, 5][:n % 8]
    user3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * \
        (n//10) + [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][:n % 10]
    score = [0, 0, 0]

    for i in range(n):
        if answers[i] == user1[i]:
            score[0] += 1
        if answers[i] == user2[i]:
            score[1] += 1
        if answers[i] == user3[i]:
            score[2] += 1

    for i in range(3):
        if score[i] == max(score):
            answer.append(i+1)

    return answer


answers = [[1, 2, 3, 4, 5], [1, 3, 2, 4, 2]]
for i in range(2):
    print(solution(answers[i]))

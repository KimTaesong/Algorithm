def solution(clothes):
    answer = 1
    cloth = dict()
    for i in clothes:
        if i[1] not in cloth:
            cloth[i[1]] = 1
        else:
            cloth[i[1]] += 1

    for key, value in cloth.items():
        print(key, value)
        answer *= (value+1)

    return answer - 1

def solution(s):
    data = list(s.split(" "))
    result = ''
    for i in data:
        for j in range(len(i)):
            if j % 2 == 0:
                result += i[j].upper()
            else:
                result += i[j].lower()
        result += ' '

    return result[:-1]

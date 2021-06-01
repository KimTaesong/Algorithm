def solution(s):
    answer = []
    string = sorted([s.split(',') for s in s[2:-2].split('},{')], key=len)

    # print(string)

    for item in string:
        # print(item)
        for digit in item:
            # print(digit)
            if int(digit) not in answer:
                answer.append(int(digit))
                # print(answer)
                # break

    return answer

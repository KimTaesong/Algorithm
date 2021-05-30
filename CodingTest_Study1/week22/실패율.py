def solution(N, stages):
    answer = []
    total_cnt = len(stages)
    check = [0] * (N+1)
    cnt = 0

    for i in range(total_cnt):
        check[stages[i]-1] += 1

    for i in range(N):
        cnt = check[i]
        if total_cnt == 0:
            answer.append([0, i+1])
        # print(cnt / total_cnt)
        else:
            answer.append([cnt / total_cnt, i+1])
            total_cnt -= cnt

    answer.sort(key=lambda x: (x[0]), reverse=True)

    result = []
    for i in answer:
        result.append(i[1])

    return result

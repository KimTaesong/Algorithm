def solution(progresses, speeds):
    answer = []
    i = 1
    N = len(progresses)
    idx = 0
    while idx != len(progresses):
        cnt = 0
        for i in range(idx, N):
            if progresses[i] < 100:
                progresses[i] += speeds[i]

        for i in range(idx, N):
            if progresses[i] >= 100:
                cnt += 1
            else:
                break

        if cnt > 0:
            idx += cnt
            answer.append(cnt)
    #     print(progresses, cnt, count, N)
    # print(answer)
    return answer


progresses = [[93, 30, 55], [95, 90, 99, 99, 80, 99]]
speeds = [[1, 30, 5], [1, 1, 1, 1, 1, 1]]
for i in range(2):
    solution(progresses[i], speeds[i])

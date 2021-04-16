def solution(n, lost, reserve):
    # 자료구조 set을 이용한 풀이
    reserve_n = list(set(reserve) - set(lost))  # 여벌옷이 있는 학생에서 중복 제거
    lost_n = list(set(lost) - set(reserve))  # 도둑 맞은 학생에서 중복 제거
    answer = n - len(lost_n)
    for i in lost_n:
        if i - 1 in reserve_n:
            answer += 1
            reserve_n.remove(i-1)

        elif i + 1 in reserve_n:
            answer += 1
            reserve_n.remove(i+1)
    return answer


n = [5, 5, 3]
lost = [[2, 4], [2, 4], [3]]
reserve = [[1, 3, 5], [3], [1]]

for i in range(3):
    print(solution(n[i], lost[i], reserve[i]))

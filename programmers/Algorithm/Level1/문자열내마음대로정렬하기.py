strings = ["sun", "bed", "car"]
n = 1


def solution(strings: str, n: int):
    strings.sort()
    answer = sorted(strings, key=lambda x: x[n])
    return answer


print(solution(strings, n))

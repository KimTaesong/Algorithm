def solution(strings: str, n: int):
    answer = sorted(sorted(strings), key=lambda strings: strings[n])
    return answer

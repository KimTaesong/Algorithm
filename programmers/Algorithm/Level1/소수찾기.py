def solution(n: int):
    # # 1. 효율성 테스트 - 시간초과
    # answer = 0
    # def isPrime(N: int):
    #     i = 2
    #     while i * i <= N:
    #         if N % i == 0: return False
    #         i += 1
    #     return True
    # for i in range(2, n+1):
    #     if isPrime(i):
    #         answer += 1
    # return answer

    # 2. 에라토스테네스의 체
    answer = 0

    def era(N: int):
        ck, p = [False for _ in range(N+1)], []
        for i in range(2, N+1):
            if ck[i] == True:
                continue
            p.append(i)
            for j in range(i*i, N+1, i):
                ck[j] = True
        return ck, p
    answer = len(era(n)[1])
    return answer

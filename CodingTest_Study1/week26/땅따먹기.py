# 내가 푼 방식 - pythonic하지 않음.
def solution(land):
    n = len(land)
    m = len(land[0])
    dp = [[0] * len(land[0]) for _ in range(n)]

    for i in range(m):
        dp[0][i] = land[0][i]

    for i in range(1, n):
        for j in range(m):
            max_tmp = 0
            for k in range(m):
                if k == j:
                    continue

                if max_tmp < dp[i-1][k]:
                    max_tmp = dp[i-1][k]

            dp[i][j] = max_tmp + land[i][j]

    # print(dp)
    return max(dp[n-1])

# Pythonic한 풀이


def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            # 연속된 열이 되지 않게 슬라이싱으로 해당 열을 제외한 새로운 리스트를 만듬.
            land[i][j] = max(land[i-1][:j] + land[i-1][j+1:]) + land[i][j]

    return max(land[-1])

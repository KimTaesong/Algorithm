# BOJ 동적계획법 1 9461 파도반 수열
import sys

T = int(input())  # 테스트 케이스의 개수
for i in range(T):
    input = sys.stdin.readline()
    N = int(input)  # N번째 인덱스
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    dp[6] = 3
    dp[7] = 4
    for i in range(8, N+1):  # 규칙을 찾으니까 8번째 인덱스부터 5번째 전 인덱스와 그 전 인덱스를 더하면 인접한 정삼각형의 길이
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[N])

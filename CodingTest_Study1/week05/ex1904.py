# BOJ 동적계획법 1 01타일 1904
import sys
input = sys.stdin.readline()
N = int(input)
dp = [0] * 1000000
dp[0] = 1
dp[1] = 2
for i in range(2, N):  # 2번째 전 인덱스 - 00타일, 1번째 전 인덱스 - 1타일을 놓으면 해당 인덱스의 타일 개수
    dp[i] = (dp[i-2] + dp[i-1]) % 15746
print(dp[N-1])

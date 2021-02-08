# BOJ 가장 긴 증가하는 부분 수열 DP 11053
N = int(input())  # 수열의 길이
A = [0] + list(map(int, input().split()))
dp = [0] * (N+1)
for i in range(1, N+1):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)
            print(dp)
print(max(dp))

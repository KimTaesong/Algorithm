# 퇴사 DP
n = int(input())
T, P = [0 for i in range(n+1)], [0 for i in range(n+1)]
for i in range(n):
    a, b = map(int, input().split())
    T[i] = a  # 소요 기간
    P[i] = b  # 수익

dp = [0 for i in range(n+1)]

for i in range(len(T)-1, -1, -1):      # 역순으로 진행
    if T[i]+i <= n:       # 날짜를 초과하지 않을 경우.
        dp[i] = max(P[i]+dp[i+T[i]], dp[i+1])
    else:                 # 날짜를 초과할 경우.
        dp[i] = dp[i+1]
print(dp[0])

def solution(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 1000000007
    return dp[n]

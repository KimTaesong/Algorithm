# BOJ 포도주 시식 2156
n = int(input())  # 포도주 잔의 개수 n
grape_wines = [0]  # 포도주를 저장하는 배열
dp = [0] * (n+1)
for i in range(n):
    one_bottle = int(input())  # 포도주
    grape_wines.append(one_bottle)
if n >= 1:
    dp[1] = grape_wines[1]
if n >= 2:
    dp[2] = grape_wines[1] + grape_wines[2]
if n >= 3:
    dp[3] = max(dp[2], grape_wines[1]+grape_wines[3],
                grape_wines[2] + grape_wines[3])
if n >= 4:
    for i in range(4, n+1):
        dp[i] = max(dp[i-1], dp[i-2] + grape_wines[i],
                    dp[i-3] + grape_wines[i-1] + grape_wines[i])
print(dp[n])

# BOJ 타일 채우기 2133
N = int(input())  # 3 x N 타일 N: 가로
dp = [0] * (N+1)  # 타일의 개수를 저장하는 배열
for i in range(2, N+1, 2):
    if i == 2:
        dp[i] = 3
    else:
        cnt = 0
        for j in range(0, i+1, 2):
            if j == i:
                cnt += 2
            else:
                if j == i-2:
                    cnt += dp[j] * dp[i-j]
                else:
                    cnt += dp[j] * 2
        dp[i] = cnt

print(dp[N])

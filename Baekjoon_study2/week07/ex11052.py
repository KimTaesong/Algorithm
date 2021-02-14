# BOj 카드 구매하기 11052
N = int(input())  # 민규가 구매하려고 하는 카드의 개수 N
P = [0] + list(map(int, input().split()))  # 카드팩의 가격을 저장할 리스트 P
dp = [0] * (N+1)  # 최대 가격을 저장할 dp 배열

dp[1] = P[1]

for i in range(2, N+1):
    for j in range(1, i+1):
        tmp = dp[i-j] + P[j]
        if tmp > dp[i]:
            dp[i] = tmp

print(dp[N])

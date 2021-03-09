# BOJ 12865 평범한 배낭 - 클론 코딩
# https://kils-log-of-develop.tistory.com/247
# N: 물품 수 / K: 무게제한
N, K = map(int, input().split(" "))

#  (N+1) * (K+1) 배열 생성
dp = [[0] * (K+1) for _ in range(N+1)]

#  물품별로 [무게(w), 가치(v)] 받기
items = []
for _ in range(N):
    w, v = map(int, input().split(" "))
    items.append([w, v])

# (1,1)부터 (N,K) 까지 한번씩 돌기
for i in range(1, N+1):
    for j in range(1, K+1):

        # items[][0] : 무게 / items[][1] : 가치
        # 이 아이템의 무게가 j보다 가벼울 경우
        if items[i-1][0] <= j:
            # 윗 칸의 값이랑 비교해서 더 큰값을 저장
            dp[i][j] = max(dp[i-1][j], dp[i-1]
                           [j-items[i-1][0]] + items[i-1][1])

        else:  # 윗 칸의 값 그대로 저장
            dp[i][j] = dp[i-1][j]

# 표의 우측하단 끝이 답
print(dp[N][K])

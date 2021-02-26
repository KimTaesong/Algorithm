# BOJ LCS 9251 최장 공통 부분 문자열
# X = x1, x2, x3 , ... , xn
# Y = y1, y2, y3 , ... , yn
# Lcs(Xn, Ym) = Xn, Ym의 최장 길이 공통부분 문자열의 길이
#=> LCS(i,j) => Xi와 Yj의 LCS 길이
#=> Xi = x1, x2 ... , xi
#=> Yj = y1, y2 ... , yj
# if xi = yj(마지막 문자열이 같은 경우) 길이를 포함시키는 게 손해는 아님. - 같으면 공통 부분 문자열롤 뽑는다 => +1
# 즉, LCS(i,j) = LCS(i-1, j-1) + 1
# if xi != yj가 다른 경우(마지막 문자열이 서로 다른 경우)
# xi와 Yj-1의 LCS와 Xi-1과 Yj의 LCS 중 가장 큰 값이 LCS ex) ACBD ADC - LCS: 2, ACB ADCB - LCS: 3 

fisrt_word = input()
second_word = input()
dp = [[0] * (len(second_word)+1) for _ in range((len(fisrt_word)+1))]

for i in range(1, len(fisrt_word)+1):
    for j in range(1, len(second_word)+1):
        if fisrt_word[i-1] == second_word[j-1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
print(dp[-1][-1])
# BOJ 동적계획법 쉬운 계단 수 10844
# 1. 정답 확인용 코드, 배열을 직접 출력
N = int(input())  # 자리수 N
dp = [0] * (N+1)
result = [[] for _ in range(N+1)]
dp[1] = 9
result[1] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if N >= 2:
    for i in range(2, N+1):
        for j in range(len(result[i-1])):
            if str(result[i-1][j])[-1] == '0':
                result[i].append(int(str(result[i-1][j]) + str(1)))
            elif str(result[i-1][j])[-1] == '1':
                result[i].append(int(str(result[i-1][j]) + str(0)))
                result[i].append(int(str(result[i-1][j]) + str(2)))
            elif str(result[i-1][j])[-1] == '2':
                result[i].append(int(str(result[i-1][j]) + str(1)))
                result[i].append(int(str(result[i-1][j]) + str(3)))
            elif str(result[i-1][j])[-1] == '3':
                result[i].append(int(str(result[i-1][j]) + str(2)))
                result[i].append(int(str(result[i-1][j]) + str(4)))
            elif str(result[i-1][j])[-1] == '4':
                result[i].append(int(str(result[i-1][j]) + str(3)))
                result[i].append(int(str(result[i-1][j]) + str(5)))
            elif str(result[i-1][j])[-1] == '5':
                result[i].append(int(str(result[i-1][j]) + str(4)))
                result[i].append(int(str(result[i-1][j]) + str(6)))
            elif str(result[i-1][j])[-1] == '6':
                result[i].append(int(str(result[i-1][j]) + str(5)))
                result[i].append(int(str(result[i-1][j]) + str(7)))
            elif str(result[i-1][j])[-1] == '7':
                result[i].append(int(str(result[i-1][j]) + str(6)))
                result[i].append(int(str(result[i-1][j]) + str(8)))
            elif str(result[i-1][j])[-1] == '8':
                result[i].append(int(str(result[i-1][j]) + str(7)))
                result[i].append(int(str(result[i-1][j]) + str(9)))
            elif str(result[i-1][j])[-1] == '9':
                result[i].append(int(str(result[i-1][j]) + str(8)))
            else:
                pass

print(len(result[N]) % 1000000000)

# 2. 동적 계획법을 적용한 문제 풀이
N = int(input())  # 자리수 N
dp = [[0] * 10 for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[N]) % 1000000000)

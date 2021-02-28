# BOJ 11051 이항 계수 2
# 이항 계수 nCk = n ! / k!(n-k)!
N, K = map(int, input().split())  # 자연수 N 정수 K
cnt = 1
for i in range(1, N+1):
    cnt *= i
for j in range(1, K+1):
    cnt = cnt // j

for k in range(1, N-K+1):
    cnt = cnt // k

print(cnt)

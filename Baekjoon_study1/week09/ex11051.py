# BOJ 이항계수 1 11051
N, K = map(int, input().split())  # N 자연수 K 정수
cnt = 1
for i in range(N, N-K, -1):
    cnt *= i

if K == 0:
    cnt = 1
else:
    for j in range(K, 0, -1):
        cnt //= j

print(cnt % 10007)

# BOJ 행렬 곱셈 2740
N, M = map(int, input().split())  # 행렬 A의 크기 N, M
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())  # 행렬 B의 크기 M. K
B = []
for i in range(M):
    B.append(list(map(int, input().split())))

C = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            C[i][j] += A[i][k] * B[k][j]
        print(C[i][j], end=' ')
    print()

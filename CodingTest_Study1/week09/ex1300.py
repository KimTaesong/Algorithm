# BOJ K번째 수 1300
N = int(input())  # N 배열의 크기
B = []
for i in range(1, N+1):
    for j in range(1, N+1):
        B.append(i*j)
B.sort()
print(B[7])

# BOJ 로프 2217
N = int(input())
loaf_list = [int(input()) for i in range(N)]
loaf_list.sort()

weight_case = [loaf_list[j] * (N-j) for j in range(N)]

print(max(weight_case))

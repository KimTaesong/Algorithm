N = int(input())  # 총 설탕의 양
count_list = []
for i in range(N//3+1):
    count = 0
    for j in range(N//5+1):
        if (3 * i + 5 * j) == N:
            count = i + j
            count_list.append(count)
if count_list:
    print(min(count_list))
else:
    print(-1)

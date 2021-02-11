# BOJ 영화감독 숌 1436
N = int(input())  # N번째 종말의 수
end_nums = []  # 종말의 수들을 저장할 배열
first = 666
cnt = 0
while cnt != N:
    a = str(first)
    b = len(a)
    for i in range(b-2):
        if a[i] == a[i+1] == a[i+2] == '6':
            end_nums.append(first)
            cnt += 1
            break
    first += 1

print(end_nums[cnt-1])

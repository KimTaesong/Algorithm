N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

# 버블 정렬로 가장 큰수와 두번째로 큰 수를 찾아 줌.
for i in range(2):
    for j in range(N-1-i):
        if nums[j] >= nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
max_value = nums[-1]
sec_value = nums[-2]
cnt = 0

cnt += (M // (K+1)) * ((max_value * K) + sec_value)
cnt += (M % (K+1)) * max_value
print(cnt)

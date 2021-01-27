N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

#
for i in range(2):
    for j in range(N-1-i):
        if nums[j] >= nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
max_value = nums[-1]
sec_value = nums[-2]
cnt = 0
if nums.count(max_value) > 1:
    cnt = max_value * M
else:
    for i in range(M):
        if i % (K+1) == 0:
            cnt += sec_value
        else:
            cnt += max_value

print(cnt)

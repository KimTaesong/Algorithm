N, K = map(int, input().split())
nums = [i for i in range(1, N+1)]
idx = (K-1)
print('<', end='')
while nums:
    idx = idx % len(nums)
    num = nums.pop(idx)
    if len(nums) >= 1:
        print(num, end=', ')
    else:
        print(num, end='>')
    idx += (K-1)

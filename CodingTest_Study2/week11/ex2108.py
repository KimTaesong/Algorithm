# BOJ 2108 통계학
import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for i in range(n)]
nums.sort()
avg_value = sum(nums) / n
mid_value = nums[n//2]
offen_value = []
diff = max(nums) - min(nums)
for i in nums:
    if [i, nums.count(i)] not in offen_value:
        offen_value.append([i, nums.count(i)])
print(format(avg_value, ".0f"))
print(mid_value)
print(offen_value)
print(diff)

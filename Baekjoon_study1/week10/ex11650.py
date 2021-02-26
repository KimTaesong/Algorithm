N = int(input())
nums = [] 
for i in range(N): 
     [a, b] = map(int, input().split()) 
     nums.append([a, b]) 
nums.sort(key = lambda num: (num[0], num[1]))

for i in range(N): 
    print(nums[i][0], nums[i][1])


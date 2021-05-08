def solution(nums):
    n = len(set(nums))
    if n < len(nums) // 2:
        return n
    return len(nums) // 2
#     def dfs(k):
#         if k == n // 2:
#             answer.append(len(set(tmp)))
#             return

#         for i in range(n):
#             if not visited[i]:
#                 visited[i] = 1
#                 tmp.append(nums[i])
#                 dfs(k+1)
#                 tmp.pop()

#                 for j in range(i+1, n):
#                     visited[j] = 0

#     n = len(nums)
#     visited = [0] * n
#     result = 0
#     tmp = []
#     answer = []
#     dfs(0)

#     return max(answer)

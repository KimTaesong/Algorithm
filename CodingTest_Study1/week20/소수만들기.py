def solution(nums):
    global cnt
    cnt = 0
    n = len(nums)
    visited = [0] * n

    def check(x):
        i = 2
        while i * i <= x:
            if x % i == 0:
                return False
            i += 1
        return True

    def dfs(k, arr):
        global cnt
        answer = arr
        if k == 3:
            if check(sum(answer)):
                cnt += 1
            return

        for i in range(k, n):
            if visited[i] == 0:
                visited[i] = 1
                answer.append(nums[i])
                dfs(k+1, answer)
                for j in range(i+1, n):
                    visited[j] = 0
                answer.pop()

    dfs(0, [])
    return cnt

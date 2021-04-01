N = int(input())  # 수의 개수 N
A = list(map(int, input().split()))  # 연산을 해줄 수의 배열 A
# 연산자의 개수를 저장하는 배열: + / - / x(곱) / // (몫)
operator = list(map(int, input().split()))
arr = [0]
nums = [0] * N
visited = [0] * N
result = []


for i in range(len(operator)):
    for j in range(operator[i]):
        arr.append(i+1)


def dfs(k: int):
    if k == N-1:
        cnt = A[0]
        for i in range(1, N):
            if nums[i] == 1:
                cnt += A[i]
            elif nums[i] == 2:
                cnt -= A[i]
            elif nums[i] == 3:
                cnt *= A[i]
            else:
                cnt = int(cnt / A[i])
        result.append(cnt)
        return

    for i in range(1, len(arr)):
        if not visited[i]:
            nums[k+1] = arr[i]
            visited[i] = 1
            dfs(k+1)
            visited[i] = 0


dfs(0)
print(max(result))
print(min(result))

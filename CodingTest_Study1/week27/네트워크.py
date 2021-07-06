def dfs(computers, visited, v):
    visited[v] = 1
    for i in range(len(visited)):
        if visited[i] == 0 and computers[v][i] == 1:
            dfs(computers, visited, i)


def solution(n: int, computers: list):
    cnt = 0
    visited = [0] * n

    for i in range(n):
        if visited[i] == 0:
            dfs(computers, visited, i)
            cnt += 1
    return cnt

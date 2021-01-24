# BOJ 백트래킹 N과 M (4) 15652
N, M = map(int, input().split())

check = [0] * (N+1)
answer = [0] * (M+1)


def dfs(idx):
    if idx == M + 1:
        for i in range(1, M+1):
            print(answer[i], end=' ')
        print()
        return

    for i in range(1, N+1):
        if answer[idx-1] > i:
            continue
        check[i] = True
        answer[idx] = i
        dfs(idx+1)
        check[i] = False


dfs(1)

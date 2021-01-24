# BOJ 백트래킹 N과 M (3) 15651
# 서로 다른 N개에서 M개를 중복해서 선택 - 중복순열
N, M = map(int, input().split())  # 1~N까지의 숫자, M가지를 선택
check = [0] * (N+1)  # 방문 노드를 체크하는 배열 ex: 1번 원소를 선택 check[1] = 1
answer = [0] * (M+1)  # M개의 원소를 저장하는 배열

# M개의 원소의 모든 조합을 찾아내기 위해서 dfs로 탐색


def dfs(idx):
    if idx == M + 1:
        for i in range(1, M+1):
            print(answer[i], end=' ')
        print()
        return

    for i in range(1, N+1):
        check[i] = True
        answer[idx] = i
        dfs(idx+1)
        check[i] = False


dfs(1)  # 인덱스 1부터 탐색 시작

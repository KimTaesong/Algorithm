N, M = map(int, input().split())  # N개의 자연수에서 중복 없이 M개를 선택
nums = [0] * (M+1)
visited = [0] * (N+1)


def dfs(k: int):  # 현재 k개의 수를 선택 했음
    if k == M:  # M개를 모두 선택했으면
        for i in range(1, M+1):
            print(nums[i], end=' ')  # nums에 기록한 수를 출력
        print()
        return

    for i in range(1, N+1):
        if not visited[i]:  # 아직 i를 방문하지 않았다면
            nums[k+1] = i  # k번째 수를 i로 정함
            visited[i] = 1  # i를 사용되었다고 표시
            dfs(k+1)  # 다음 수를 선택하러 감
            visited[i] = 0  # M개를 모두 선택한 것을 출력했기 때문에 다시 방문하지 않은 걸로 초기화


dfs(0)

while True:
    w, h = map(int, input().split())
    graphs = [[0]]
    visited = [[0] * (w+1) for _ in range(h+1)]
    cnt = 0
    if w == 0 and h == 0:
        break
    for i in range(h):
        graphs.append([0] + list(map(int, input().split())))

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    def dfs(i, j):
        visited[i][j] = True
        for k in range(8):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 < nx <= h and 0 < ny <= w:
                if visited[i][j] == 0 and graphs[i][j] == 1:
                    dfs(nx, ny)

    for i in range(1, h+1):
        for j in range(1, w+1):
            if graphs[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                cnt += 1
    print(cnt)

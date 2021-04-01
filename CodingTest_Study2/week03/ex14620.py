N = int(input())
G = [list(map(int, input().split())) for i in range(N)]

# 0*N+0
# 0 ~ N**N -1 까지

ans = 10000
# 정지,위,아래,우,좌
dx, dy = [0, 0, 0, 1, -1], [0, 1, -1, 0, 0]

# 꽃 a,b,c에 대한 비용


def ck(list):
    ret = 0
    flow = []
    for flower in list:
        x = flower // N
        y = flower % N
        if x == 0 or x == N-1 or y == 0 or y == N-1:
            return 10000  # return 10000을 해주는 이유는 후보의 가능성을 지워주기 위해서.
        for w in range(5):
            flow.append((x+dx[w], y+dy[w]))
            ret += G[x+dx[w]][y+dy[w]]

    if len(set(flow)) != 15:
        return 10000
    return ret


for i in range(N*N):
    for j in range(i+1, N*N):
        for k in range(j+1, N*N):
            ans = min(ans, ck([i, j, k]))

print(ans)

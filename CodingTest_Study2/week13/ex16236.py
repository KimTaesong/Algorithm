from collections import deque

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def bfs(x, y):
    q, visited = deque([(x, y)]), set([(x, y)])
    time = 0
    shark_size = 2  # 현재 아기 상어의 크기.
    eaten = 0  # 현재 크기에서 , 지금까지 먹은 물고기 수
    eaten_flag = False  # 현재 상태에서 물고기를 먹은 경우,
    # for _ in range(size) 구문을 진행하지 않기 위한 플래그
    answer = 0
    print(f"q: {q}, visited: {visited}, time: {time}, shark_size: {shark_size}, eaten: {eaten}, eaten_flag: {eaten_flag}, answer: {answer}")

    while q:
        size = len(q)
        # 위, 그리고 왼쪽을 더 우선시해서 가야하기 때문에 , BFS  queue를 소개팅해준다.
        q = deque(sorted(q))
        print(q)
        for _ in range(size):
            x, y = q.popleft()
            print(x, y)
            # 현재 위치에 아기 상어보다 작은 물고기가 있어서, 이를 먹는 경우.
            if board[x][y] != 0 and board[x][y] < shark_size:
                board[x][y] = 0
                eaten += 1

                # 아기 상어의 크기 만큼 먹었다면, 아기 상어의 크기를 +1 해둬야 한다.

                if eaten == shark_size:
                    shark_size += 1
                    eaten = 0

                # 먹고 난 뒤, 현재 위치를 기준으로 다시 근처를 탐색해야 하기 때문

                # BFS queue와 visited 를 초기화 해준다.
                q, visited = deque(), set([(x, y)])
                eaten_flag = True

                # 먹었을 때의 시간을 저장해둔다.
                answer = time

            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < n and (nx, ny) not in visited:
                    if board[nx][ny] <= shark_size:
                        q.append((nx, ny))
                        visited.add((nx, ny))

            # 현재 위치에서 먹었다면, 더 이상 위 반복문을 돌 필요가 없다.
            if eaten_flag:
                eaten_flag = False
                break
        time += 1
    return answer


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 1. 초기 상어(자신)의 위치를 파악하고, 해당 자리는 판에서 비워둔다.
s_x, s_y = None, None
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            s_x, s_y = i, j
            board[i][j] = 0

# 2. 시작점에서 BFS 진행
print(bfs(s_x, s_y))

# import sys
# from collections import deque
# import heapq

# def bfs(x, y):
#     q = deque()
#     heap = []
#     q.append((x, y, 0))

#     while q:
#         x, y, d = q.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if -1 < nx < n and -1 < ny < n and not visited[nx][ny]:
#                 visited[nx][ny] = True

#                 if arr[nx][ny] == 0 or size == arr[nx][ny]:
#                     q.append((nx, ny, d+1))

#                 elif size > arr[nx][ny]:
#                     heapq.heappush(heap, [d+1, nx, ny])

#     if heap:
#         return heap[0]

#     else:
#         return None

# dx = [-1, 1, 0 , 0]
# dy = [0, 0, -1, 1]

# input = sys.stdin.readline
# n = int(input().strip())
# arr = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False] * n for _ in range(n)]
# fishes = []
# size = 2
# eaten = 0
# cnt = 0
# s1, s2 = 0, 0

# # 물고기와 상어의 위치를 파악.
# for i in range(n):
#     for j in range(n):
#         if 0 < arr[i][j] < 7:
#             fishes.append((i, j))
#         elif arr[i][j] == 9:
#             arr[i][j] = 0
#             s1 = i
#             s2 = j

# while len(fishes) != 0:
#     visited = [[False] * n for _ in range(n)] # 수족관
#     visited[s1][s2] = True # 상어 위치

#     result = bfs(s1, s2)

#     if result == None:
#         break

#     else:
#         eaten += 1
#         cnt += result[0]
#         arr[result[1]][result[2]] = 0

#     if eaten == size:
#         eaten = 0
#         size += 1

#     s1, s2 = result[1], result[2]

# print(cnt)


# # BOJ 16236 아기 상어
# import sys
# from collections import deque
# input = sys.stdin.readline
# n = int(input())  # 수족관의 크기 n
# graph = [list(map(int, input().split()))
#          for i in range(n)]  # 수족관, 0: 빈칸, 1~6: 물고기의 크기, 9: 아기 상어의 위치
# # 아기상어 상하좌우 방향 벡터
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# request_time = 0
# baby_size = 2
# location = check(graph)
# bfs(location[0], location[1])


# # 아기 상어의 위치를 찾는 함수
# def check(graph):
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] == 9:
#                 return [i, j]


# # 아기 상어의 수족관 탐색 함수
# def bfs(a: int, b: int):
#     q = deque([[a, b]])
#     cnt = 0
#     while q:
#         x, y = q.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]

#             # 칸을 벗어나면 종료
#             if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
#                 continue

#             # 크기보다 큰 물고기가 있는 칸은 지나갈 수 없음.
#             if graph[nx][ny] > baby_size:
#                 continue

#             # 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.
#             if graph[nx][ny] != 0:
#                 if graph[nx][ny] != baby_size:
#                     graph[nx][ny] = 0
#                 q.append([nx, ny])
#                 request_time += 1
#                 cnt += 1

#             # 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
#             if baby_size == cnt:
#                 baby_size += 1
#                 cnt = 0

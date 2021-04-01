import sys
input = sys.stdin.readline
# 세로, 가로, 초(반복 횟수)
R, C, T = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 초기 방의 미세먼지와 공기 청정기 위치
room = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 찾기, 1열에 있음.
air_fresh = (0, 0)
for i in range(R):
    if room[i][0] == -1 and room[i+1][0] == -1:
        air_fresh = (i, i+1)
        break


# T번 반복
for _ in range(T):

    # 확산
    new_room = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):

            # 미세먼지가 5 이상이어야 유의미한 계산 가능
            if room[i][j] >= 5:

                # 주변에 나눠줄 애들
                each = room[i][j] // 5

                # 주변에 나눠준 횟수 카운팅 위함
                count = 0

                # 확산이 가능한지 탐색
                for k in range(4):

                    nx = i + dx[k]
                    ny = j + dy[k]

                    # 범위 안에 들어오고, 공기청정기의 자리가 아닌 경우
                    if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != -1:

                        # 카운트를 1 늘려주고
                        count += 1

                        # 새 배열에 미세먼지를 받은만큼 더해줌
                        new_room[nx][ny] += each

                # 나눠준 애 업데이트 (나눠준만큼 빼기)
                room[i][j] = room[i][j] - count * each

    # 두 배열 값 합치기
    for i in range(R):
        for j in range(C):
            room[i][j] += new_room[i][j]

    # 순환
    # upper bound (오 위 왼 아래 순서) - 시계 반대 방향
    temp = room[air_fresh[0]][C-1]  # 위로 올라가는 애
    for i in range(C-2, 0, -1):
        room[air_fresh[0]][i+1] = room[air_fresh[0]][i]

    temp2 = room[0][C-1]  # 왼쪽으로 가는 애
    for i in range(air_fresh[0]-1):
        room[i][C-1] = room[i+1][C-1]
    room[air_fresh[0]-1][C-1] = temp

    temp = room[0][0]  # 아래쪽으로 갈 애
    for i in range(C-1):
        room[0][i] = room[0][i+1]
    room[0][C-2] = temp2

    for i in range(air_fresh[0]-1, 1, -1):
        room[i][0] = room[i-1][0]
    room[air_fresh[0]][1] = 0  # 공기청정기 위치에서 오른쪽으로 1칸 위치: 깨끗한 공기가 나오니까.
    room[1][0] = temp

    # lower boud (오 아래 왼 위 순서) - 시계 방향
    temp = room[air_fresh[1]][C-1]  # 아래쪽으로 가는 애
    for i in range(C-2, 0, -1):
        room[air_fresh[1]][i+1] = room[air_fresh[1]][i]

    temp2 = room[R-1][C-1]  # 왼쪽으로 가는 애
    for i in range(R-1, air_fresh[1], -1):
        room[i][C - 1] = room[i-1][C - 1]
    room[air_fresh[1]+1][C-1] = temp

    temp = room[R-1][0]  # 위로 가는 애
    for i in range(C-1):
        room[R-1][i] = room[R-1][i+1]
    room[R-1][C-2] = temp2

    for i in range(air_fresh[1]+1, R-1):
        room[i][0] = room[i+1][0]
    room[air_fresh[1]][1] = 0  # 공기청정기 위치에서 오른쪽으로 1칸 위치: 깨끗한 공기가 나오니까.
    room[R-2][0] = temp


# 남은 미세먼지 수 계산
cnt = 0
for each in room:
    cnt += sum(each)

# 공기청정기 2칸을 각각 -1로 표현했으니 최종값에 2를 더해줌
print(cnt+2)

# BOJ 14891 톱니바퀴
import sys
input = sys.stdin.readline
# N극 0, S극 1, 입력은 12시 방향부터 시계 방향으로 주어짐, 주목할 부분 2번째, 6번째 인덱스
gear = [0] + [list(map(int, input().rstrip())) for _ in range(4)]
k = int(input())  # 회전 수 k

for j in range(k):
    gear_num, rotate_dir = map(int, input().split())
    gear_check = [0] * 5  # 톱니바퀴 회전 체크 겸 회전 방향을 저장
    gear_check[gear_num] = rotate_dir  # 시작 톱니 회전 방향을 저장

    # 시작 톱니의 왼쪽 부분의 인접 톱니들 조사
    for i in range(gear_num-1, 0, -1):
        if gear[i][2] == gear[i+1][6]:
            break
        gear_check[i] = -gear_check[i+1]

    # 시작 톱니의 오른쪽 부분의 인접 톱니들 조사
    for i in range(gear_num+1, 5):
        if gear[i][6] == gear[i-1][2]:
            break
        gear_check[i] = -gear_check[i-1]

    # 모든 톱니의 회전 방향 조사 마친 후 회전 시작
    for num in range(1, 5):
        if gear_check[num] == 1:    # 시계 방향 회전
            # print(num, gear_num)
            gear[num] = gear[num][7:] + gear[num][:7]

        elif gear_check[num] == -1:  # 반시계 방향 회전
            # print(num, gear_num)
            gear[num] = gear[num][1:] + gear[num][:1]

        # print(gear)

score = 0  # k번 회전후 톱니바퀴의 점수합
for i in range(1, 5):
    if gear[i][0] == 1:
        score += 2 ** (i-1)

print(score)

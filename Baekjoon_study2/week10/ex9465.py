# BOJ 9465 스티커
T = int(input())  # 테스트 케이스의 개수
for _ in range(T):
    n = int(input())  # n줄의 스티커
    sticker = [list(map(int, input().split())) for _ in range(2)]  # 2n줄의 스티커
    # 1번째 인덱스의 최대값은 해당 인덱스의 값 + 왼쪽 아래 대각성분을 더해준 값
    sticker[0][1] += sticker[1][0]
    # 1번째 인덱스의 최대값은 해당 인덱스의 값 + 오른쪽 위 대각성분을 더해준 값
    sticker[1][1] += sticker[0][0]
    for i in range(2, n):  # 2번째 인덱스 부터는 달라짐
        # 해당 인덱스의 값 + (왼쪽 아래 대각성분의 이전 인덱스, 이이전 인덱스 중 최대값)
        sticker[0][i] += max(sticker[1][i-1], sticker[1][i-2])
        # 해당 인덱스의 값 + (오른쪽 위 대각성분의 이전 인덱스, 이이전 인덱스 중 최대값)
        sticker[1][i] += max(sticker[0][i-1], sticker[0][i-2])
    print(max(sticker[0][n-1], sticker[1][n-1]))

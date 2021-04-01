# BOJ 기타레슨 2343
# 클론코딩 - https://dirmathfl.tistory.com/266
N, M = map(int, input().split())
lesson = list(map(int, input().split()))
left = max(lesson)
right = sum(lesson)


while left <= right:
    mid = (left + right) // 2
    cnt = 0
    play_time = 0
    for i in lesson:
        # play_time이 m보다 커지면 새로운 블루레이 필요
        if play_time + i > mid:
            cnt += 1
            play_time = 0
        play_time += i

    cnt += 1 if play_time else 0

    if cnt <= M:
        right = mid - 1
    elif cnt > M:
        left = mid + 1
print(left)

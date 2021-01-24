# BOJ 브루트 포스 하노이탑 11729
def hanoi_tower(n, start, end):  # n 원판의 개수, start: 시작 기둥 위치, end: 옮겨야 할 기둥 위치
    if n == 1:
        print(start, end)
        return

    hanoi_tower(n-1, start, 6-start-end)  # 1단계 - 옮겨야 할 개수: 2^(n-1) - 1
    print(start, end)  # 2단계 - 옮겨야 할 개수: 1
    hanoi_tower(n-1, 6-start-end, end)  # 3단계 - 옮겨야 할 개수: 2^(n-1) - 1


n = int(input())  # 원판의 개수
print(2**n-1)  # 원판을 옮기는 횟수 출력
hanoi_tower(n, 1, 3)  # 원판을 옮기는 경로 출력 함수

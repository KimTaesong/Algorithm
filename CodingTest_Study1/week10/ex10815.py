#BOJ 10815 숫자 카드
N = int(input()) # 숫자 카드의 개수
cards = list(map(int, input().split())) # 상근이의 숫자 카드
M = int(input()) # 숫자 카드인지 아닌지를 구해야 할 M개의 정수
compare_cards = list(map(int, input().split())) # 비교할 카드

def binary_search(target: int, data: list):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid

        elif data[mid] < target:
            start = mid + 1

        else:
            end = mid - 1
    
    return None

cards.sort()
for i in range(M):
    if binary_search(compare_cards[i], cards) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
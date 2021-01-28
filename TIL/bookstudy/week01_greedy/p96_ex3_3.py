N, M = map(int, input().split())  # N 행의 개수, M 열의 개수
card = []  # 숫자 카드를 저장할 배열
max_card = 0  # 최소값 카드 중 가장 큰 수

for i in range(N):
    max_card = min(list(map(int, input().split())))
    idx = i
    card.append([max_card, idx])
card.sort(reverse=True)
print(card[0][0])


for i in range(N):
    if i == 0:
        max_card = min(list(map(int, input().split())))
        idx = i
    else:
        temp_value = min(list(map(int, input().split())))
        if temp_value > max_card:
            max_card = temp_value
            idx = i
print(max_card, idx)
